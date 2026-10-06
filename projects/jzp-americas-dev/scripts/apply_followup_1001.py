#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""10/01 跟进批次 · 跟进表更新（.md + .xlsx 双份同步）

三块内容：
  A. **本批已发 33 家** → 跟进次数 +1 ｜ 最后联系日 = 2026-10-01 ｜ 下次跟进日 = 首封日 + N 个工作日
  B. **13 家「已跟过但表格没推进」**（实测修正）→ 按 `Sent Messages` 实测值回填
  C. **30 家积压未跟** → 备注标记（**不改状态**，本轮不发）

另：#24 / #31 的收件地址按实测订正；#29 的跟进次数按实测订正（上一轮实际未发出）。
"""

import json
import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

import openpyxl

ROOT = Path("/Users/eric/WorkBuddy AI/2026-09-27-00-43-30/jzp-americas-dev")
XLSX = ROOT / "开发信项目/工作区/开发信跟进表.xlsx"
MD = ROOT / "开发信项目/工作区/开发信跟进表.md"
TODAY = date(2026, 10, 1)
C_STATUS, C_CNT, C_NEXT, C_LAST, C_NOTE = 13, 14, 15, 16, 17
ROW_TAIL = r"\s*\|[ \t]*$"


def add_bd(d: date, n: int) -> date:
    cur = d
    while n > 0:
        cur += timedelta(days=1)
        if cur.weekday() < 5:
            n -= 1
    return cur


def pdate(s):
    m = re.search(r"(\d{4})-(\d{2})-(\d{2})", str(s or ""))
    return date(int(m.group(1)), int(m.group(2)), int(m.group(3))) if m else None


def main():
    work = json.loads((ROOT / ".workbuddy-ai/今日工作单.json").read_text(encoding="utf-8"))
    calc = json.loads((ROOT / ".workbuddy-ai/今日跟进名单-算.json").read_text(encoding="utf-8"))
    sent_nums = {x["num"] for x in work}
    fixed = calc["done"]                       # 13 家：已跟过但表格没推进
    backlog = [x for x in calc["todo"] if x["nxt"] != "2026-10-01"]   # 30 家积压

    wb = openpyxl.load_workbook(XLSX)
    rows = {}
    for ws in wb.worksheets:
        for r in range(5, ws.max_row + 1):
            n = ws.cell(r, 1).value
            if n is not None:
                rows[n] = (ws, r)
    print(f"表内 {len(rows)} 行 ｜ 本批 {len(sent_nums)} ｜ 修正 {len(fixed)} ｜ 积压 {len(backlog)}\n")

    log = []
    # ---- A. 本批已发 ----
    for x in work:
        num = x["num"]
        if num not in rows:
            print(f"  ⚠️ #{num} 表内找不到"); continue
        ws, r = rows[num]
        old_cnt = ws.cell(r, C_CNT).value or 0
        new_cnt = int(old_cnt) + 1
        first = pdate(ws.cell(r, 2).value)
        nxt = add_bd(first, 8 if new_cnt == 1 else 15) if first else None
        ws.cell(r, C_CNT).value = new_cnt
        ws.cell(r, C_LAST).value = "2026-10-01"
        if nxt:
            ws.cell(r, C_NEXT).value = nxt.isoformat()
        fn = {"21": "CW-Galle", "23": "Romar-Electrical", "24": "Hillfort", "25": "MVA-Power",
              "26": "Purcee-Industrial-Power", "27": "Tri-State-Utility",
              "28": "Vancouver-Industrial-Electric", "29": "Amped-Electric",
              "30": "Brownstown-Electric", "31": "Power-Line-Supply", "32": "Irby-Utilities",
              "45": "RA-Electrical", "46": "Ross-Morrison", "48": "Fletcher-Reinhardt",
              "49": "KBS-Electrical", "50": "K2-Electric", "51": "Valley-Electrical",
              "52": "Border-States", "153": "Montgomery-Industrial", "154": "KPC-Power",
              "155": "ABCO-Supply", "156": "RIES-Equipment", "159": "Alliance-Engineering",
              "160": "Ardoch-Electric", "161": "Bradmoore-Electric", "165": "NorTec-Group",
              "166": "Shermco-Industries", "172": "Trotter-and-Morton", "176": "JRS-Industrial",
              "180": "Pro-Energy", "181": "Prairie-Central", "183": "RS-Breakers",
              "186": "Access-Electrical"}[str(num)]
        add = f"｜✅ 10/01 跟进信已发 2026-10-01（clients/开发信-跟进-{fn}.md）"
        cur = ws.cell(r, C_NOTE).value or ""
        ws.cell(r, C_NOTE).value = (cur + add) if cur and cur != "—" else add.lstrip("｜")
        log.append(f"  A #{num:<5} 次数 {old_cnt}→{new_cnt}  下次 {nxt}")

    # ---- B. 实测修正 ----
    for x in fixed:
        num = x["num"]
        if num not in rows:
            continue
        ws, r = rows[num]
        n_re = int(x.get("sent_re") or 0)
        last = x.get("sent_last")
        nxt = add_bd(pdate(last), 8 if n_re <= 1 else 15) if last else None
        ws.cell(r, C_CNT).value = n_re
        ws.cell(r, C_LAST).value = last
        if nxt:
            ws.cell(r, C_NEXT).value = nxt.isoformat()
        cur = ws.cell(r, C_NOTE).value or ""
        add = (f"🔧 2026-10-01 按 `Sent Messages` 实测回填：实际已跟进 {n_re} 次，"
               f"最近发出 {last}（原登记未推进）")
        ws.cell(r, C_NOTE).value = (cur + "｜" + add) if cur and cur != "—" else add
        log.append(f"  B #{num:<5} 次数→{n_re}  最后→{last}  下次→{nxt}")

    # ---- C. 积压标记 ----
    for x in backlog:
        num = x["num"]
        if num not in rows:
            continue
        ws, r = rows[num]
        cur = ws.cell(r, C_NOTE).value or ""
        add = (f"⏸️ 积压未跟：应跟 {x['nxt']}，实测最近发出 {x.get('sent_last')} "
               f"→ **本轮（10/01）未发**，待补")
        ws.cell(r, C_NOTE).value = (cur + "｜" + add) if cur and cur != "—" else add

    # ---- D. 地址/档位订正 ----
    if 24 in rows:
        ws, r = rows[24]
        ws.cell(r, 12).value = "info@hillfort.us（⚠️ 原登记 RFQ@ 从未实际使用；实测两轮均发至 info@）"
    if 31 in rows:
        ws, r = rows[31]
        ws.cell(r, 12).value = "jeff_carls@uscco.com（⚠️ 原登记 information@ 从未实际使用；实测两轮均发至 jeff_carls@）"
    if 29 in rows:
        ws, r = rows[29]
        cur = ws.cell(r, C_NOTE).value or ""
        ws.cell(r, C_NOTE).value = (cur + "｜🔧 上一轮跟进信虽写过，但实测**未发出** → 本轮按「第 1 次」处理").lstrip("｜")

    wb.save(XLSX)
    print(f"✅ xlsx 已保存（A {len(sent_nums)} + B {len(fixed)} + C {len(backlog)}）")

    # ---- E. .md 同步（逐字段一致）----
    md = MD.read_text(encoding="utf-8")

    def blk(t, num):
        m = re.search(rf"^### {num}\.\s.*?(?=^### |\Z)", t, re.S | re.M)
        return m.group(0) if m else None

    def setf(b, field, val):
        pat = re.compile(rf"^\|\s*{field}\s*\|\s*(.*?)\s*\|\s*$", re.M)
        if len(pat.findall(b)) != 1:
            return None
        return pat.sub(lambda m: f"| {field} | {val} |", b, count=1)

    def addnote(b, add):
        pat = re.compile(r"^\|\s*备注\s*\|\s*(.*?)\s*\|\s*$", re.M)
        m = pat.search(b)
        if not m:
            return None
        cur = m.group(1)
        new = (cur + "｜" + add) if cur and cur != "—" else add
        return b[:m.start(1)] + new + b[m.end(1):]

    changed = 0
    for num in list(sent_nums) + [x["num"] for x in fixed] + [x["num"] for x in backlog] + [24, 31, 29]:
        ws, r = rows.get(num, (None, None))
        if ws is None:
            continue
        old = blk(md, num)
        if old is None:
            print(f"  ⚠️ md 找不到 ### {num}")
            continue
        b = old
        b = setf(b, "跟进次数", str(ws.cell(r, C_CNT).value)) or b
        b = setf(b, "下次跟进日", str(ws.cell(r, C_NEXT).value)) or b
        b = setf(b, "最后联系日", str(ws.cell(r, C_LAST).value)) or b
        b = addnote(b, (ws.cell(r, C_NOTE).value or "").split("｜")[-1]) or b
        if b != old:
            md = md.replace(old, b, 1)
            changed += 1
    MD.write_text(md, encoding="utf-8")
    print(f"✅ md 已同步（{changed} 个块）")

    # ---- 一致性复核 ----
    bad = 0
    for num in list(sent_nums) + [x["num"] for x in fixed] + [x["num"] for x in backlog]:
        ws, r = rows.get(num, (None, None))
        if ws is None:
            continue
        b = blk(md, num)
        if b is None:
            continue
        for col, f in ((C_CNT, "跟进次数"), (C_NEXT, "下次跟进日"), (C_LAST, "最后联系日")):
            x = str(ws.cell(r, col).value)
            m = re.search(rf"^\|\s*{f}\s*\|\s*(.*?)\s*\|\s*$", b, re.M)
            y = m.group(1).replace("**", "").split("（")[0].strip() if m else None
            if x != y and not (x == "0" and y == "—"):
                print(f"  ❌ #{num} {f}: xlsx={x!r} md={y!r}")
                bad += 1
    print(f"一致性：差异 {bad} 处" + (" ✅" if bad == 0 else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
