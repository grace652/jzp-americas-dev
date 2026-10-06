#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""投递报告生成器（可反复重跑刷新）

用法：
  python3 scripts/写投递报告.py <队列文件> <输出md> [--title "…"] [--queue-label "…"] [--note "…"]

为什么做成生成器：投递是**跨小时进行**的，手写的报告一写就过时。
本脚本从队列 JSON 的 `status` / `sent_at` 现场生成结果表，
**任何时候重跑都是当前真相** —— 交付时不必等投递跑完。
"""

import argparse
import json
import sys
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path("/Users/eric/WorkBuddy AI/2026-09-27-00-43-30/jzp-americas-dev")
BJ = timezone(timedelta(hours=8))
TZ_CN = {"ET": "美东", "CT": "美中", "MT": "美山", "PT": "美西", "AK": "阿拉斯加",
         "UAE": "阿联酋", "AT": "大西洋", "AZ": "亚利桑那"}


def dev(plan: str, actual: str):
    if not actual or not plan:
        return None
    try:
        a = datetime.strptime(plan, "%Y-%m-%d %H:%M")
        b = datetime.strptime(actual[:19], "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return None
    return int((b - a).total_seconds())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("queue")
    ap.add_argument("out")
    ap.add_argument("--title", default="投递结果")
    ap.add_argument("--queue-label", default="")
    ap.add_argument("--note", default="")
    # 静态叙事段（批次构成 / 闸门 / 破例说明 / 未投递 …）：
    # 放进文件里，**重跑生成器不会丢** —— 手写进报告会被下次重跑覆盖掉。
    ap.add_argument("--prelude", default="", help="插在「逐封结果」之前的静态 md")
    ap.add_argument("--postlude", default="", help="追加在报告末尾的静态 md")
    args = ap.parse_args()

    items = json.loads((ROOT / args.queue).read_text(encoding="utf-8"))
    now = datetime.now(BJ)
    cnt = Counter(i["status"] for i in items)
    done = cnt.get("sent", 0) + cnt.get("failed", 0) + cnt.get("skipped", 0)
    all_done = cnt.get("pending", 0) == 0

    L = [f"# {args.title}", "",
         f"> 队列：`{args.queue}`" + (f"（{args.queue_label}）" if args.queue_label else ""),
         f"> 报告生成：**{now:%Y-%m-%d %H:%M}（北京）**",
         f"> 进度：**{done}/{len(items)}**"
         f"（已发 {cnt.get('sent',0)} ｜ 失败 {cnt.get('failed',0)} ｜ "
         f"跳过 {cnt.get('skipped',0)} ｜ 待发 {cnt.get('pending',0)}）", ""]
    if args.note:
        L += [f"> {args.note}", ""]
    L += ["---", ""]
    if args.prelude:
        L += [(ROOT / args.prelude).read_text(encoding="utf-8").rstrip(), "", "---", ""]
    L += ["## 一、逐封结果", "",
          "| 计划（北京）| 送达（当地）| 收件人 | 状态 | 实际发出 | 偏差 |",
          "|---|---|---|---|---|---|"]
    for i in items:
        plan = i.get("scheduled_at_bj") or ""
        tz = i.get("tz", "")
        local = (i.get("scheduled_at_local") or "")[5:16]
        to = ", ".join(i.get("to") or [])
        if i.get("cc"):
            to += f"<br>cc {', '.join(i['cc'])}"
        d = dev(plan, i.get("sent_at") or "")
        dtxt = "—" if d is None else (f"{d:+d}s" if abs(d) < 3600 else f"{d/60:+.1f}min")
        st = {"sent": "✅ 已发", "pending": "⏳ 待发", "failed": "❌ **失败**",
              "skipped": "⛔ 跳过"}.get(i["status"], i["status"])
        L.append(f"| {plan[5:16]} | {TZ_CN.get(tz,tz)} {local} | `{to}` | {st} | "
                 f"{(i.get('sent_at') or '—')} | {dtxt} |")
    L.append("")

    fails = [i for i in items if i["status"] == "failed"]
    if fails:
        L += ["## 二、❌ 失败清单（必须处理）", ""]
        for i in fails:
            L.append(f"- `{', '.join(i['to'])}` —— `{i.get('blocked_reason','')}`")
        L.append("")
    skips = [i for i in items if i["status"] == "skipped"]
    if skips:
        L += ["## 三、⛔ 跳过清单", ""]
        for i in skips:
            L.append(f"- `{', '.join(i['to'])}` —— `{i.get('blocked_reason','')}`")
        L.append("")

    pend = [i for i in items if i["status"] == "pending"]
    if pend:
        L += ["## 四、⏳ 尚未到点", "", "| 计划（北京）| 收件人 |", "|---|---|"]
        for i in pend:
            L.append(f"| {i['scheduled_at_bj'][5:16]} | `{', '.join(i['to'])}` |")
        L += ["", f"> 剩余 **{len(pend)}** 封由守护进程 / 看护自动化负责；"
                  "**重跑本脚本即可刷新本报告**。", ""]
    else:
        L += ["## 四、✅ 全部投递完毕", "",
              f"> 共 **{len(items)}** 封：已发 {cnt.get('sent',0)} ｜ "
              f"失败 {cnt.get('failed',0)} ｜ 跳过 {cnt.get('skipped',0)}。", ""]

    if args.postlude:
        L += ["", "---", "", (ROOT / args.postlude).read_text(encoding="utf-8").rstrip(), ""]

    (ROOT / args.out).write_text("\n".join(L), encoding="utf-8")
    print(f"✅ 已写 {args.out}：{done}/{len(items)} 完成"
          + ("（全部完毕）" if all_done else "（仍有待发）"))
    for k, v in sorted(cnt.items()):
        print(f"   {k}: {v}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
