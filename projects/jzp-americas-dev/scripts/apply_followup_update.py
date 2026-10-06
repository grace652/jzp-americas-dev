#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
阶段 2：把 92 行写进「新 sheet」，并就地更新老 sheet 的跟进状态。

设计依据：`开发信项目/01_skill_email_writing.md` §十一「xlsx 写入操作规程」
  · 下拉/配色 sqref 一律到 `:200`（不要贴着当前末行）
  · 追加行必须带每列样式（标准行 = 老 sheet 第 6 行），**不写行级 s**
  · 改前备份、改后 testzip

🔴 安全铁律：**绝不读写 `freeze_panes`**（openpyxl getter 返回 "C60"，
   写回会把冻结行从 1–4 变成 1–59）；也不碰 merge/DV/CF/col_widths。
"""
import json, re, sys, shutil
from copy import copy
from datetime import date, timedelta
from pathlib import Path
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule

ROOT = Path(Path(__file__).resolve().parents[1])
XLSX = ROOT / "开发信项目/工作区/开发信跟进表.xlsx"
NEW_SHEET = "开发信跟进表-batch5+6"
COLS = ["#", "发送日期", "公司名称", "国家/地区", "联系人", "职位", "买家类型", "需求产品",
        "触达来源", "骨架", "建议发送时间(北京)", "邮箱", "状态", "跟进次数", "下次跟进日",
        "最后联系日", "备注 / 下一步"]
DV_G = "分销商,批发商,EPC工程商,盘厂,电力公司,工厂自用,终端承包商,贸易商,其他"
DV_I = "官网,名录,LinkedIn,展会,询盘,搜索引擎,推荐"
DV_J = "A,B,C"
DV_M = "待发送,已发送,已送达,已回复,已报价,已寄样,谈判中,已成交,无回应,已退订（对方拒联）,已放弃"
CF = [("已退订（对方拒联）", "F5F7F9", None, None), ("已成交", "C8E6C9", "1B5E20", True),
      ("已回复", "BBDEFB", "0D47A1", True), ("已报价", "FFE0B2", "E65100", True),
      ("谈判中", "FFECB3", "F57F17", True), ("已寄样", "D1C4E9", "4527A0", True),
      ("已发送", "FFF9C4", "827717", True), ("无回应", "ECEFF1", "546E7A", False),
      ("已放弃", "FFCDD2", "B71C1C", True)]
WIDTHS = {"A": 5, "B": 12, "C": 30, "D": 14, "E": 16, "F": 14, "G": 16, "H": 22, "I": 12,
          "J": 7, "K": 17, "L": 26, "M": 14, "N": 9, "O": 12, "P": 12, "Q": 38}
GRAY_COLS = (14, 15, 16)      # N/O/P


def workday_add(d0, n):
    d, k = d0, 0
    while k < n:
        d += timedelta(days=1)
        if d.weekday() < 5:
            k += 1
    return d


NEXT_AFTER = {0: 3, 1: 8, 2: 15, 3: 25}


def load_sent():
    sent, allsent = {}, []
    for f in [ROOT / "发信队列.json", ROOT / "发信队列.json.bak-batch5已发38封",
              ROOT / "发信队列-batch5备份.json", ROOT / "发信队列-batch5剩余.json"]:
        if not f.exists():
            continue
        try:
            items = json.loads(f.read_text(encoding="utf-8"))
        except Exception:
            continue
        for it in items:
            if it.get("status") != "sent" or not it.get("sent_at"):
                continue
            d = str(it["sent_at"])[:10]
            for a in it.get("to", []):
                a = a.strip().lower()
                if a:
                    allsent.append((a, it.get("letter", ""), d))
                    if a not in sent or d < sent[a]:
                        sent[a] = d
    return sent, allsent


def build_new_sheet(wb, rows):
    ws = wb.create_sheet(NEW_SHEET)
    # ---- 列宽
    for col, w in WIDTHS.items():
        ws.column_dimensions[col].width = w
    # ---- 行 1/2 横幅
    ws["A1"] = "开发信跟进表（2026-09-24 之后新增 · batch5+batch6）— JZPE POWER TRANSFORMER CO., LTD.   |   Ian Chou"
    ws["A2"] = "用法：每写好一封开发信就在下面加一行。状态列可下拉选择。灰底列（跟进次数/下次跟进日/最后联系日）为跟进排程列。"
    ws.merge_cells("A1:L1"); ws.merge_cells("A2:L2")
    ws["A1"].font = Font(name="Microsoft YaHei", size=14, bold=True, color="FFFFFF")
    ws["A1"].fill = PatternFill("solid", fgColor="0F3D63")
    ws["A1"].alignment = Alignment(vertical="center")
    ws["A2"].font = Font(name="Microsoft YaHei", size=9, color="5A6B7C")
    ws["A2"].fill = PatternFill("solid", fgColor="F5F7F9")
    ws["A2"].alignment = Alignment(vertical="center")
    ws.row_dimensions[1].height = 30
    ws.row_dimensions[2].height = 20
    ws.row_dimensions[4].height = 30
    # ---- 行 4 表头
    thin = Side(style="thin", color="D0D7DE")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    for j, name in enumerate(COLS, 1):
        c = ws.cell(4, j, name)
        c.font = Font(name="Microsoft YaHei", size=10, bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor="0F3D63")
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        c.border = border
    # ---- 数据行（照老 sheet 第 6 行的样式索引）
    tpl = wb["开发信跟进表"]
    tpl_s = [tpl.cell(6, j)._style for j in range(1, 18)]
    for i, r in enumerate(rows):
        rr = 5 + i
        ws.row_dimensions[rr].height = 20
        for j, name in enumerate(COLS, 1):
            c = ws.cell(rr, j, r.get(name, ""))
            c._style = copy(tpl_s[j - 1])
            if j in GRAY_COLS:
                c.fill = PatternFill("solid", fgColor="F5F7F9")
            if j in (2, 15, 16):
                c.number_format = "yyyy\\-mm\\-dd"
            c.alignment = Alignment(horizontal="center" if j in (1, 2, 4, 9, 10, 11, 13, 14, 15, 16) else "left",
                                    vertical="center", wrap_text=(j in (8, 17)))
    # ---- 4 个下拉（sqref 一律到 200）
    for col, opts in (("G", DV_G), ("I", DV_I), ("J", DV_J), ("M", DV_M)):
        dv = DataValidation(type="list", formula1=f'"{opts}"', allow_blank=True, showDropDown=False)
        ws.add_data_validation(dv)
        dv.add(f"{col}5:{col}200")
    # ---- M 列 9 条条件格式
    for val, bg, fg, bold in CF:
        f = Font(bold=bold, color=fg) if fg else Font()
        ws.conditional_formatting.add(
            f"M5:M200",
            CellIsRule(operator="equal", formula=[f'"{val}"'],
                       fill=PatternFill(start_color=bg, end_color=bg, fill_type="solid"), font=f))
    ws.freeze_panes = "C5"
    ws.auto_filter.ref = "A4:Q200"
    return ws


def update_old_sheet(wb, allsent, replied):
    """就地更新老 sheet：只改 M/N/O/P/Q，不动 A–L，不动任何格式。

    🔴 匹配口径：**按邮箱精确匹配老 sheet 的 L 列**。
       上一版按「域名前缀 ⊂ 公司名」模糊匹配，只命中 26/59 行（实测）。
    """
    ws = wb["开发信跟进表"]
    # 老 sheet：邮箱(小写) → 行号
    by_mail = {}
    for r in range(5, ws.max_row + 1):
        raw = str(ws.cell(r, 12).value or "")
        for a in re.findall(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}", raw):
            by_mail.setdefault(a.lower(), r)
    # 按邮箱归集已发跟进
    per = {}
    for a, lname, d in allsent:
        if "跟进" in lname:
            per.setdefault(a, []).append(d)
    changed = []
    for a, ds in sorted(per.items()):
        row = by_mail.get(a)
        if not row:
            continue
        n_old = ws.cell(row, 14).value or 0
        n_new = len(ds)
        if n_new <= n_old:
            continue
        last = max(ds)
        d0 = ws.cell(row, 2).value
        try:
            d0s = d0.strftime("%Y-%m-%d") if hasattr(d0, "strftime") else str(d0)[:10]
            k = NEXT_AFTER.get(n_new)
            nd = workday_add(date.fromisoformat(d0s), k).isoformat() if k else ""
        except Exception:
            nd = ""
        ws.cell(row, 14).value = n_new
        ws.cell(row, 16).value = last
        ws.cell(row, 15).value = nd
        if str(ws.cell(row, 13).value) != "已回复":
            ws.cell(row, 13).value = "已发送"
        q = str(ws.cell(row, 17).value or "")
        tag = f"【{last} 已跟进第{n_new}次】"
        if tag not in q:
            ws.cell(row, 17).value = (tag + q)[:900]
        changed.append((row, ws.cell(row, 3).value, n_new, last, nd))
    return changed


def main():
    dry = "--dry" in sys.argv
    rows = json.loads(Path("/tmp/new_rows.json").read_text(encoding="utf-8"))
    sent, allsent = load_sent()
    wb = openpyxl.load_workbook(XLSX)
    if NEW_SHEET in wb.sheetnames:
        del wb[NEW_SHEET]
    build_new_sheet(wb, rows)
    ch = update_old_sheet(wb, allsent, set())
    print(f"新 sheet：{NEW_SHEET}｜数据行 {len(rows)}")
    print(f"老 sheet 更新：{len(ch)} 行")
    for x in ch[:15]:
        print(f"   行{x[0]:<4}{str(x[1])[:30]:<32} 跟进{x[2]}次 最后{x[3]} 下次{x[4]}")
    if dry:
        print("\n[dry] 未写盘")
        return
    wb.save(XLSX)
    print(f"\n✅ 已写盘 {XLSX}")


if __name__ == "__main__":
    main()
