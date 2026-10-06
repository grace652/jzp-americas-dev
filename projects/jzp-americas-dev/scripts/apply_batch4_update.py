#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""阶段 2：老 sheet 追加 batch4 历史缺口 31 行 + 新 sheet 重编号

设计依据：`开发信项目/01_skill_email_writing.md` §十一
  · 追加行 = **照抄第 6 行（标准行）每列样式索引**，**不写行级 s**
  · 下拉/条件格式 sqref 一律到 `:200`
  · 改前备份、改后 testzip

🔴 安全铁律：**绝不读写 `freeze_panes`**（getter 返回 "C60"，写回会把冻结行变 1–59）
"""
import json, sys
from copy import copy
from pathlib import Path
import openpyxl
from openpyxl.styles import PatternFill, Alignment

ROOT = Path("/Users/eric/WorkBuddy AI/2026-09-27-00-43-30/jzp-americas-dev")
XLSX = ROOT / "开发信项目/工作区/开发信跟进表.xlsx"
OLD = "开发信跟进表"
NEW = "开发信跟进表-batch5+6"
COLS = ["#", "发送日期", "公司名称", "国家/地区", "联系人", "职位", "买家类型", "需求产品",
        "触达来源", "骨架", "建议发送时间(北京)", "邮箱", "状态", "跟进次数", "下次跟进日",
        "最后联系日", "备注 / 下一步"]
GRAY = (14, 15, 16)
DATE_COLS = (2, 15, 16)
CENTER = (1, 2, 4, 9, 10, 11, 13, 14, 15, 16)
WRAP = (8, 17)
RENUM_OFFSET = 31          # 新 sheet 117–208 → 148–239


def main():
    dry = "--dry" in sys.argv
    rows = json.loads(Path("/tmp/batch4_rows.json").read_text(encoding="utf-8"))
    wb = openpyxl.load_workbook(XLSX)
    ws = wb[OLD]
    start = ws.max_row + 1                      # 119
    tpl_s = [ws.cell(6, j)._style for j in range(1, 18)]
    print(f"老 sheet：现有 {ws.max_row} 行 → 追加 {len(rows)} 行（{start}–{start+len(rows)-1}）")
    for i, r in enumerate(rows):
        rr = start + i
        ws.row_dimensions[rr].height = 20
        for j, name in enumerate(COLS, 1):
            c = ws.cell(rr, j, r.get(name, ""))
            c._style = copy(tpl_s[j - 1])
            if j in GRAY:
                # 🔴 必须写 8 位 ARGB（`FFF5F7F9`）—— 写 `F5F7F9` 会得到 alpha=00，
                #    与原表 `FFF5F7F9` 的样式索引不同（实测 93 格不一致）
                c.fill = PatternFill("solid", fgColor="FFF5F7F9")
            if j in DATE_COLS:
                c.number_format = "yyyy\\-mm\\-dd"
            c.alignment = Alignment(horizontal="center" if j in CENTER else "left",
                                    vertical="center", wrap_text=(j in WRAP))
    # 修正 AutoFilter 覆盖新数据
    old_ref = ws.auto_filter.ref
    ws.auto_filter.ref = f"A4:Q{start + len(rows) - 1}"
    print(f"  AutoFilter {old_ref} → {ws.auto_filter.ref}")

    # ---- 新 sheet 重编号（117–208 → 148–239）
    #   🔴 幂等保护：只在「尚未重编号」时执行（首行 # < 148），
    #      否则 dry-run 后再跑会变成 +62（实测踩过）
    if NEW in wb.sheetnames:
        wn = wb[NEW]
        first = wn.cell(5, 1).value
        if isinstance(first, int) and first < 148:
            n = 0
            for rr in range(5, wn.max_row + 1):
                v = wn.cell(rr, 1).value
                if isinstance(v, int):
                    wn.cell(rr, 1).value = v + RENUM_OFFSET
                    n += 1
            print(f"新 sheet 重编号：{n} 行（+{RENUM_OFFSET}）")
            p = Path("/tmp/new_rows.json")
            if p.exists():
                nr = json.loads(p.read_text(encoding="utf-8"))
                if nr and nr[0]["#"] < 148:
                    for x in nr:
                        x["#"] = x["#"] + RENUM_OFFSET
                    p.write_text(json.dumps(nr, ensure_ascii=False, indent=1), encoding="utf-8")
                    print(f"  /tmp/new_rows.json 编号已同步（{nr[0]['#']}–{nr[-1]['#']}）")
                else:
                    print(f"  /tmp/new_rows.json 已是 {nr[0]['#']}–{nr[-1]['#']}，跳过")
        else:
            print(f"新 sheet 已重编号（首行 #{first}），跳过")
        # 顺手把新 sheet 的 N/O/P 灰底 alpha 也对齐原表（00F5F7F9 → FFF5F7F9）
        fixed = 0
        for rr in range(5, wn.max_row + 1):
            for j in GRAY:
                f = wn.cell(rr, j).fill
                if f.fill_type == "solid" and str(f.fgColor.rgb) == "00F5F7F9":
                    wn.cell(rr, j).fill = PatternFill("solid", fgColor="FFF5F7F9")
                    fixed += 1
        if fixed:
            print(f"  新 sheet 灰底 alpha 对齐：{fixed} 格")

    if dry:
        print("\n[dry] 未写盘")
        return
    wb.save(XLSX)
    print(f"\n✅ 已写盘 {XLSX}")


if __name__ == "__main__":
    main()
