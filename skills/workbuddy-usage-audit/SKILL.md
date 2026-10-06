---
name: workbuddy-usage-audit
description: 统计本机 WorkBuddy 的真实 token 用量与会话活动。当用户说「我今天用了多少 token」「这个月 token 消耗」「哪个会话最费 token」「查一下用量」「token 都花在哪了」「WorkBuddy 用量统计」时使用。核心是读 ~/.workbuddy-ai/traces/*/trace_*.json 里 trace.modelInfo 的 totalInputTokens / totalOutputTokens / totalCachedTokens / callCount，按本地时区聚合，并把「缓存命中」与「新增输入」拆开讲——两者成本差一个量级，混在一起报会误导。
agent_created: true
---

# WorkBuddy 用量审计

## 何时用

用户问「今天用了多少 token」「本月消耗」「哪个会话最费」「用量花在哪」。
目标不是报一个总数，而是给出**可核对的口径**：总量、缓存占比、按会话/按次拆解、以及覆盖盲区。

## 数据在哪里（关键，别猜）

| 位置 | 内容 | 说明 |
|---|---|---|
| `~/.workbuddy-ai/traces/<pid>/trace_*.json` | **唯一权威 token 来源** | 每个文件一次 Agent workflow。`trace.modelInfo` 里有 `models` / `totalInputTokens` / `totalOutputTokens` / `totalCachedTokens` / `lastCallInputTokens` / `callCount` |
| `~/.workbuddy-ai/workbuddy.db` → `session_usage` | `used` / `size` / `credit_json` | `used/size` 是**上下文窗口占用**，不是累计消耗；`credit_json` 是 messageId→credits，**按会话累计、无法按天切分** |
| `~/.workbuddy-ai/logs/<date>/sdk/conversations/*.log` | 事件流 | 只有 `usage_update` 事件标记（`hasUsage:true`），**不含 token 数字**，别在这里找 |
| `~/.workbuddy-ai/audit-log/<date>.jsonl` | 操作审计 | **完全没有 token 信息** |
| `~/.workbuddy-ai/usage-log.json` | skill/MCP 使用日期 | 只有日期，无 token |

`traces/*/trace.json` 里的 `trace.totalTokens` 与 `modelInfo` 的 input+output 之和一致，可作交叉校验；但**很多 trace 的 `totalTokens` 是 0**（无 modelInfo），不能只用它求和。

## 操作步骤

1. 遍历 `traces/`，`json.load` 每个文件，跳过解析失败的。
2. 取 `trace.modelInfo`，**没有就跳过**（这类 trace 无 token 数据）。
3. **时区**：`trace.startedAt` 是 UTC（`...Z`），必须转成 UTC+8 再按日期分组，否则会把前一天的晚间会话算到今天。
4. 按 `sessionId` / `workerPid` 分组聚合，输出 `callCount` / input / output / cached。
5. 交叉核对：`sessions` 表里 `last_activity_at` 落在当天的会话列表，与 trace 覆盖的会话做差集，**明确报出未覆盖的会话**。

参考脚本（直接改日期即可）：

```python
import json, os, datetime, collections
LOCAL = datetime.timezone(datetime.timedelta(hours=8))
TARGET = datetime.date(2026, 10, 5)
rows = []
for root, _, fs in os.walk(os.path.expanduser('~/.workbuddy-ai/traces')):
    for f in fs:
        try:
            d = json.load(open(os.path.join(root, f)))
        except Exception:
            continue
        t = d.get('trace', {}); mi = t.get('modelInfo')
        if not mi or not t.get('startedAt'):
            continue
        dt = datetime.datetime.fromisoformat(
            t['startedAt'].replace('Z', '+00:00')).astimezone(LOCAL)
        if dt.date() == TARGET:
            rows.append((dt, t.get('sessionId'), mi))
rows.sort(key=lambda r: r[0])
TI = sum(r[2].get('totalInputTokens', 0) for r in rows)
TO = sum(r[2].get('totalOutputTokens', 0) for r in rows)
TC = sum(r[2].get('totalCachedTokens', 0) for r in rows)
CC = sum(r[2].get('callCount', 0) for r in rows)
print(f"运行 {len(rows)} 次 | 调用 {CC} | 输入 {TI:,} | 输出 {TO:,} | 缓存 {TC:,} | 新增输入 {TI-TC:,}")
```

用 `python3` 即可，**不需要 venv**（纯标准库）。traces 目录可能有 90MB 级的单文件，全量遍历约十几秒，属正常。

## 必须讲清的三件事

1. **输入 ≠ 成本**。Agent 每次调用都重发整个上下文，所以 `totalInputTokens` 是**跨调用累加**的。真正新增的只有 `input - cached`。经验值：重上下文场景缓存命中率 95% 以上，报总数不报新增会让人误判成本。
2. **覆盖盲区**。正在进行的会话没有 trace；纯自动化短跑可能不落 trace。结论里要写「实际值略高于此」。
3. **credits 与 token 不成比例**（实测 3.3 万～10.9 万 token/credit 都有），别用 credits 反推 token。

## 输出格式

- 先给一行总账：`总 token = 输入 X（其中缓存 Y / 新增 Z）+ 输出 W`，调用次数。
- 再给按次/按会话的明细表，按时间排序。
- 最后一行写盲区声明。
- 图表用堆叠横向条形图：缓存命中 + 新增输入两段，最费的那次一眼可见。
