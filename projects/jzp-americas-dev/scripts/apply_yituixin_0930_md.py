#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""新增「已退信」状态 + 把主送退信的客户改标（.md 文本备份 + 图例 + 对照表）

与 `apply_yituixin_0930.py`（.xlsx）**逐字段一致**。
另：`00_custom_instructions.md` §六之二 的「已退订 vs 已放弃」对照表扩成三方。
"""

import re
import sys
from pathlib import Path

ROOT = Path(Path(__file__).resolve().parents[1])
MD = ROOT / "开发信项目/工作区/开发信跟进表.md"
DOC = ROOT / "开发信项目/00_custom_instructions.md"

ROW_TAIL = r"\s*\|[ \t]*$"
TARGETS = {
    13:  ("2026-10-17", "⛔ 主送已退信：软退信-暂时停用（bellsouth.net 554.30 邮箱停用）。冷却至 2026-10-17；重试须换发法（改主题+重写正文+去链接+纯文本+间隔≥2周）。"),
    63:  ("2026-10-13", "⛔ 主送已退信：软退信-服务商拒收（EXO `550 5.4.1 Access denied`）×2 地址 + 整域封锁 `birminghamec.com`。冷却至 2026-10-13；重试须换发法。"),
    82:  ("—",          "⛔ 主送已退信：硬退信-地址不存在（`jrav@` 9/24，唯一具名直邮）→ **永久排除**。备选 `info@heicontractors.com`（B档）未验证；改走电话 219-922-9886。"),
    90:  ("—",          "⛔ 主送已退信：硬退信-地址不存在（Google NoSuchUser 9/25）→ **永久排除**。仅剩电话 907 跟进。"),
    104: ("2026-10-08", "⛔ 主送已退信：软退信-服务商拒收（Mimecast `5.4.1` 9/24）。冷却至 2026-10-08；重试须换发法。"),
    106: ("2026-10-09", "⛔ 主送已退信：软退信-服务商拒收（EXO `550 5.4.1` 9/25）。冷却至 2026-10-09；重试须换发法。"),
    126: ("2026-10-09", None),
    135: ("2026-10-14", None),
    151: ("2026-10-13", "⛔ 主送已退信：软退信-服务商拒收（EXO `550 5.4.1` 9/29）。冷却至 2026-10-13；重试须换发法。"),
    213: ("2026-10-30", None),
}


def block(text, num):
    m = re.search(rf"^### {num}\.\s.*?(?=^### |\Z)", text, re.S | re.M)
    if not m:
        raise SystemExit(f"⛔ 找不到块 ### {num}.")
    return m.group(0)


def set_field(blk, field, value):
    pat = re.compile(rf"^\| {field} \| (.*?){ROW_TAIL}", re.M)
    n = len(pat.findall(blk))
    if n != 1:
        raise SystemExit(f"⛔ 字段 `{field}` 命中 {n} 处")
    return pat.sub(lambda m: f"| {field} | {value} |", blk, count=1)


def main():
    text = MD.read_text(encoding="utf-8")
    log = []

    # ---- 1. 10 行改标 ----
    for num, (nxt, note) in TARGETS.items():
        old = block(text, num)
        blk = set_field(old, "状态", "**已退信**")
        blk = set_field(blk, "下次跟进日", nxt)
        if note:
            m = re.search(rf"^\| 备注 \| (.*?){ROW_TAIL}", blk, re.M)
            cur = m.group(1)
            blk = blk[:m.start(1)] + (cur + "｜" if cur and cur != "—" else "") + note + blk[m.end(1):]
        text = text.replace(old, blk, 1)
        log.append(f"  #{num} 状态→已退信 ｜ 下次 {nxt}")

    # ---- 2. 状态图例加一行 ----
    old_legend = "| 已放弃 | **我方判断**确认无机会（停业/地址失效）|"
    new_legend = (old_legend + "\n"
                  "| **已退信** | ⛔ **该客户主送地址被退信**（地址不存在 / 服务商拒收）→ "
                  "**邮件渠道已关闭**；冷却期内不得重发，到期须**换发法** |")
    if text.count(old_legend) != 1:
        raise SystemExit(f"⛔ 图例锚点命中 {text.count(old_legend)} 处")
    text = text.replace(old_legend, new_legend, 1)
    log.append("  状态图例 → 加「已退信」一行")

    # ---- 3. 三方对照表 ----
    old_cmp = ("> | **已退订（对方拒联）** | **对方明确拒绝** | ⛔ **永久不行** | 必须同步登记 `不再联系名单.md` |\n"
               "> | 已放弃 | 我方判断无机会 | ⚠️ 有条件可复活（如恢复经营）| 无 |")
    new_cmp = ("> | **已退订（对方拒联）** | **对方**明确拒绝 | ⛔ **永久不行** | 必须同步登记 `不再联系名单.md` |\n"
               "> | **已退信** | **收件端**（技术性） | ⚠️ 冷却到期后可**换发法**重试 | 登记 `退信黑名单.json`（`扫描退信.py` 自动维护）|\n"
               "> | 已放弃 | **我方**判断无机会 | ⚠️ 有条件可复活（如恢复经营）| 无 |")
    if text.count(old_cmp) != 1:
        raise SystemExit(f"⛔ 对照表锚点命中 {text.count(old_cmp)} 处")
    text = text.replace(old_cmp, new_cmp, 1)
    log.append("  三方对照表 → 加「已退信」一行")

    MD.write_text(text, encoding="utf-8")

    # ---- 4. 00_custom_instructions.md ----
    doc = DOC.read_text(encoding="utf-8")
    old_doc = ("> | `已退订（对方拒联）` | **对方明确拒绝** | ⛔ **永久不行**（合规要求）|\n"
               "> | `已放弃` | 我方判断无机会（停业/地址失效）| ⚠️ 有条件可复活 |")
    new_doc = ("> | `已退订（对方拒联）` | **对方**明确拒绝 | ⛔ **永久不行**（合规要求）|\n"
               "> | **`已退信`** | **收件端**（技术性：地址不存在/服务商拒收）| ⚠️ 冷却到期后可**换发法**重试 |\n"
               "> | `已放弃` | **我方**判断无机会（停业/地址失效）| ⚠️ 有条件可复活 |")
    if doc.count(old_doc) != 1:
        raise SystemExit(f"⛔ 00 对照表锚点命中 {doc.count(old_doc)} 处")
    doc = doc.replace(old_doc, new_doc, 1)
    DOC.write_text(doc, encoding="utf-8")
    log.append("  00_custom_instructions.md §六之二 → 加「已退信」一行")

    print(f"✅ 已更新（{len(log)} 处）")
    for l in log:
        print(l)
    return 0


if __name__ == "__main__":
    sys.exit(main())
