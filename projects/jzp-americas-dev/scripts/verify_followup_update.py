#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""阶段 3：校验写入结果。必须能证明三件事：
   ① 新 sheet 行数/下拉/条件格式正确
   ② 老 sheet **未被破坏**（结构与备份逐项相等，pane 字节不变）
   ③ （md 同步后）md 与 xlsx 一致
"""
import re, sys, zipfile, json
from pathlib import Path
import openpyxl

ROOT = Path("/Users/eric/WorkBuddy AI/2026-09-27-00-43-30/jzp-americas-dev")
XLSX = ROOT / "开发信项目/工作区/开发信跟进表.xlsx"
BAK = ROOT / ".workbuddy-ai/开发信跟进表.bak-20260929-补登记前.xlsx"
NEW = "开发信跟进表-batch5+6"
OLD = "开发信跟进表"
ok_all = True


def chk(label, cond, detail=""):
    global ok_all
    print(f"  {'✅' if cond else '❌'} {label}{('  ' + detail) if detail else ''}")
    if not cond:
        ok_all = False


def sheet_facts(p):
    z = zipfile.ZipFile(p)
    names = [n for n in z.namelist() if re.match(r"xl/worksheets/sheet\d+\.xml", n)]
    return {n: z.read(n).decode("utf-8") for n in names}


print("=" * 70)
print("① 新 sheet")
wb = openpyxl.load_workbook(XLSX)
chk("sheet 存在", NEW in wb.sheetnames, f"现有 {wb.sheetnames}")
ws = wb[NEW]
chk("数据行 = 96（4 表头 + 92）", ws.max_row == 96, f"实际 {ws.max_row}")
chk("列数 = 17", ws.max_column == 17, f"实际 {ws.max_column}")
hdr = [ws.cell(4, j).value for j in range(1, 18)]
chk("表头逐字同老 sheet", hdr == [c.value for c in wb[OLD][4][:17]], str(hdr[:4]) + "…")
dvs = {str(dv.sqref): dv.formula1 for dv in ws.data_validations.dataValidation}
chk("下拉 4 个", len(dvs) == 4, f"实际 {len(dvs)}")
chk("下拉 sqref 全部到 :200", all(s.endswith("200") for s in dvs), str(list(dvs)))
cf = list(ws.conditional_formatting)
rules = sum(len(x.rules) for x in cf)
chk("条件格式 M5:M200 且 9 条", str(cf[0].sqref) == "M5:M200" and rules == 9, f"{cf[0].sqref} / {rules} 条")
chk("冻结窗格 C5", str(ws.freeze_panes) == "C5", str(ws.freeze_panes))
chk("AutoFilter A4:Q200", str(ws.auto_filter.ref) == "A4:Q200", str(ws.auto_filter.ref))
empty_c = [r for r in range(5, 97) if not ws.cell(r, 3).value]
chk("公司名无空", not empty_c, f"空 {len(empty_c)} 行")
n_gray = sum(1 for r in range(5, 97) for j in (14, 15, 16)
             if ws.cell(r, j).fill.start_color.rgb in ("00F5F7F9", "FFF5F7F9", "F5F7F9"))
chk("N/O/P 灰底（应 276 格）", n_gray == 276, f"实际 {n_gray}")

print()
print("② 老 sheet 未被破坏")
wo = wb[OLD]
bo = openpyxl.load_workbook(BAK)[OLD]
chk("max_row 仍 = 118", wo.max_row == 118, f"实际 {wo.max_row}")
chk("合并单元格一致", sorted(map(str, wo.merged_cells.ranges)) == sorted(map(str, bo.merged_cells.ranges)))
chk("冻结窗格一致", str(wo.freeze_panes) == str(bo.freeze_panes), f"{wo.freeze_panes}")
chk("下拉 sqref 一致", sorted(str(d.sqref) for d in wo.data_validations.dataValidation) ==
    sorted(str(d.sqref) for d in bo.data_validations.dataValidation))
chk("条件格式规则数一致", sum(len(x.rules) for x in wo.conditional_formatting) ==
    sum(len(x.rules) for x in bo.conditional_formatting),
    f"{sum(len(x.rules) for x in wo.conditional_formatting)} vs {sum(len(x.rules) for x in bo.conditional_formatting)}")
cw_o = {k: v.width for k, v in wo.column_dimensions.items() if v.width}
cw_b = {k: v.width for k, v in bo.column_dimensions.items() if v.width}
chk("列宽一致", cw_o == cw_b, f"{len(cw_o)} 列")
chk("AutoFilter 一致", str(wo.auto_filter.ref) == str(bo.auto_filter.ref), f"{wo.auto_filter.ref}")

# pane 字节比对（老 sheet 是 sheet1.xml）
fa, fb = sheet_facts(XLSX), sheet_facts(BAK)
pa = re.search(r"<pane[^>]*/>", fa["xl/worksheets/sheet1.xml"])
pb = re.search(r"<pane[^>]*/>", fb["xl/worksheets/sheet1.xml"])
chk("老 sheet <pane> 字节不变", (pa.group(0) if pa else None) == (pb.group(0) if pb else None),
    (pa.group(0) if pa else "无"))
chk("testzip 通过", zipfile.ZipFile(XLSX).testzip() is None)

print()
print("③ 数据抽查")
rows = json.loads(Path("/tmp/new_rows.json").read_text(encoding="utf-8"))
mism = 0
for i, r in enumerate(rows):
    rr = 5 + i
    if ws.cell(rr, 3).value != r["公司名称"] or str(ws.cell(rr, 13).value) != r["状态"]:
        mism += 1
chk("新 sheet 与构建数据一致", mism == 0, f"不一致 {mism} 行")
print()
print("=" * 70)
print("✅ 全部通过" if ok_all else "⚠️ 有未通过项，需复查")
sys.exit(0 if ok_all else 1)
