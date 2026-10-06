#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""后台刷新器：队列状态一变就重生成投递报告，直到全部发完（或到截止时刻）。

为什么需要它：投递跨小时进行（本批 01:00–02:30 十封 + 13:00 一封）。
手写报告一写就过时；本脚本让报告**自动变成最终版**。

用法（用 Bash 工具的 run_in_background 启动）：
  python3 scripts/刷新投递报告-跟进0930.py
"""

import json
import subprocess
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(Path(__file__).resolve().parents[1])
QUEUE = ROOT / "发信队列-跟进0930.json"
OUT = "跟进0930投递结果-20261001.md"
BJ = timezone(timedelta(hours=8))
DEADLINE = datetime(2026, 10, 1, 13, 15, tzinfo=BJ)     # 覆盖 13:00 的 Scientechnic

CMD = [sys.executable, str(ROOT / "scripts/写投递报告.py"), QUEUE.name, OUT,
       "--title", "9/30 跟进信 · 投递结果（2026-10-01）",
       "--queue-label", "独立队列，未改动主队列",
       "--prelude", "scripts/报告前文-跟进0930.md",
       "--postlude", "scripts/报告后文-跟进0930.md"]


def snapshot():
    try:
        items = json.loads(QUEUE.read_text(encoding="utf-8"))
    except Exception:
        return None
    return tuple((i["status"], i.get("sent_at")) for i in items)


def main():
    last = None
    while True:
        cur = snapshot()
        now = datetime.now(BJ)
        if cur is not None and cur != last:
            r = subprocess.run(CMD, cwd=ROOT, capture_output=True, text=True)
            stamp = now.strftime("%H:%M:%S")
            if r.returncode == 0:
                first = (r.stdout or "").strip().splitlines()[0] if r.stdout else ""
                print(f"[{stamp}] 已刷新报告：{first}", flush=True)
            else:
                print(f"[{stamp}] ⚠️ 生成失败：{(r.stderr or '')[:200]}", flush=True)
            last = cur
            if cur is not None and all(s == "sent" or s == "failed" or s == "skipped"
                                       for s, _ in cur):
                print(f"[{stamp}] ✅ 队列已无 pending，刷新器退出", flush=True)
                return 0
        if now > DEADLINE:
            print(f"[{now:%H:%M:%S}] 到截止时刻，刷新器退出", flush=True)
            return 0
        time.sleep(60)


if __name__ == "__main__":
    sys.exit(main())
