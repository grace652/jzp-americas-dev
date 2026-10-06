#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""batch7 A 档 7 家 · 投递结果登记进跟进表（xlsx + md）

依据：`01_skill_email_writing.md` §十一 与 skill `scheduled-mail-send-guard` §六
  · 🔴 绝不读写 freeze_panes
  · 状态须与 M 列下拉逐字一致
  · xlsx 操作环境：受管 venv（openpyxl 3.1.5）

做法：
  1. 备份 xlsx 与 md
  2. 由 `开发信跟进表-batch5+6` 复制出子表 `开发信跟进表-batch7`（保留表头/样式/DV/CF），
     清空数据区后写入 7 行
  3. md 末尾追加 `### 240.`–`### 246.` 明细块
  4. 校验：freeze_panes 未变、testzip 通过、DV/CF 数量、# 唯一

只做新增，不改动任何既有行。
"""
import json
import shutil
import sys
import zipfile
from datetime import datetime, timedelta
from pathlib import Path

import openpyxl

ROOT = Path(Path(__file__).resolve().parents[1])
XLSX = ROOT / "开发信项目/工作区/开发信跟进表.xlsx"
MD = ROOT / "开发信项目/工作区/开发信跟进表.md"
STAMP = "20261001-batch7A"
BAK_X = ROOT / f".workbuddy-ai/开发信跟进表.bak-{STAMP}前.xlsx"
BAK_M = ROOT / f".workbuddy-ai/开发信跟进表.bak-{STAMP}前.md"
SRC_SHEET = "开发信跟进表-batch5+6"
NEW_SHEET = "开发信跟进表-batch7"
ROWS_JSON = Path("/tmp/batch7a_rows.json")

# 队列实际收件人（权威：实际发出的地址）
SENT = {
    229: ("tyler@graypowerline.ca", "2026-10-01 01:37", "美中 CT", "09-30 12:37"),
    231: ("laurie@midwaypower.com", "2026-10-01 01:03", "美西 PT", "09-30 09:03"),
    239: ("dawebb@webbelectric.com", "2026-10-01 01:47", "美中 CT", "09-30 12:47"),
    243: ("andrew@tenergynm.com", "2026-10-01 01:52", "美山 MT", "09-30 11:52"),
    250: ("jpeters@lizcosales.com", "2026-10-01 01:25", "美东 ET", "09-30 13:25"),
    263: ("dave.mossman@transformernet.com", "2026-10-01 01:47", "美中 CT", "09-30 12:47"),
    269: ("ericsine@metrowire.net", "2026-10-01 01:32", "美东 ET", "09-30 13:32"),
}
COUNTRY = {
    229: "加拿大 · MB",
    231: "加拿大 · BC",
    239: "美国 · FL",
    243: "美国 · NM",
    250: "加拿大 · ON",
    263: "美国 · SD",
    269: "美国 · MI",
}
LETTER = {
    229: "开发信-Gray-Construction.md",
    231: "开发信-Midway-Power-Line-Services.md",
    239: "开发信-Webb-Electric.md",
    243: "开发信-Tenergy.md",
    250: "开发信-Lizco-Sales-Rentals.md",
    263: "开发信-Transformer-Network.md",
    269: "开发信-Metro-Wire-Cable.md",
}
SEQ_START = 240   # 跟进表 # 为独立顺序索引，源表末行为 #239
SEND_DATE = "2026-10-01"
NEXT_FU = "2026-10-06"   # 首封后第 3 个工作日（10-01 周四 → 10-06 周二）

C_STATUS, C_CNT, C_NEXT, C_LAST, C_NOTE = 13, 14, 15, 16, 17
HEADER_ROWS = 4


def main():
    rows = json.loads(ROWS_JSON.read_text(encoding="utf-8"))
    by_num = {r["买家编号"]: r for r in rows}
    missing = [n for n in SENT if n not in by_num]
    if missing:
        raise SystemExit(f"⛔ 交接单提取缺号：{missing}")

    # ---------- 备份 ----------
    if not BAK_X.exists():
        shutil.copy2(XLSX, BAK_X)
        print(f"已备份 xlsx → {BAK_X.name}")
    if not BAK_M.exists():
        shutil.copy2(MD, BAK_M)
        print(f"已备份 md   → {BAK_M.name}")

    # ---------- xlsx ----------
    wb = openpyxl.load_workbook(XLSX)
    fp_before = {ws.title: ws.freeze_panes for ws in wb.worksheets}
    dv_before = {ws.title: len(ws.data_validations.dataValidation) for ws in wb.worksheets}
    cf_before = {ws.title: len(list(ws.conditional_formatting)) for ws in wb.worksheets}

    if NEW_SHEET in wb.sheetnames:
        raise SystemExit(f"⛔ 子表 `{NEW_SHEET}` 已存在 —— 请先人工确认，避免重复登记")

    src = wb[SRC_SHEET]

    # 🔴 不用 copy_worksheet：它会把源表 92 行数据行复制成「空样式行」残留
    #    （openpyxl 的 delete_rows 不删 Row 记录），表里会多出 85 行空白带框行。
    #    改为手工建表：只复制表头 1–4 行 + 列宽 + 行高 + 合并单元格。
    from copy import copy as _copy

    ws = wb.create_sheet(NEW_SHEET)
    for r in range(1, HEADER_ROWS + 1):
        for c in range(1, src.max_column + 1):
            s, t = src.cell(r, c), ws.cell(r, c)
            t.value = s.value
            t._style = s._style
        if r in src.row_dimensions and src.row_dimensions[r].height:
            ws.row_dimensions[r].height = src.row_dimensions[r].height
    for k, dim in src.column_dimensions.items():
        if dim.width:
            ws.column_dimensions[k].width = dim.width
    for mc in src.merged_cells.ranges:
        if mc.min_row <= HEADER_ROWS:
            ws.merge_cells(str(mc))

    # copy_worksheet 同样不复制 DV / CF / freeze —— 必须手工补齐，
    # 否则新子表 M 列没有下拉、状态不变色（skill §六 的硬约束）。
    for dv in src.data_validations.dataValidation:
        ws.add_data_validation(_copy(dv))
    for cf in src.conditional_formatting:
        for rule in cf.rules:
            ws.conditional_formatting.add(str(cf.sqref), _copy(rule))
    ws.freeze_panes = src.freeze_panes

    # 样式模板：源表第 5 行（有数据的那行）
    style_row = HEADER_ROWS + 1

    nums = sorted(SENT)
    for k, num in enumerate(nums):
        r = style_row + k
        d = by_num[num]
        email, sent_bj, tzlab, sent_local = SENT[num]
        note = (
            f"买家{num}｜batch7 A 档｜首封 {sent_bj} 北京发出"
            f"（{tzlab} 当地 {sent_local}，破例未走 9–10 点窗口）"
            f"｜下一步：D+3（{NEXT_FU}）首轮跟进，须带新信息点"
        )
        vals = [
            SEQ_START + k,     # 1  #：顺序索引 240 起
            SEND_DATE,         # 2  发送日期
            d["公司名称"],      # 3
            COUNTRY[num],      # 4
            d["联系人"],        # 5
            d["职位"],          # 6
            d["买家类型"],      # 7
            d["需求产品"],      # 8
            "官网一手源",       # 9  触达来源
            "A",               # 10 骨架
            sent_bj[11:],      # 11 建议发送时间(北京)
            email,             # 12 邮箱
            "已发送",           # 13 状态
            0,                 # 14 跟进次数
            NEXT_FU,           # 15 下次跟进日
            SEND_DATE,         # 16 最后联系日
            note,              # 17 备注/下一步
        ]
        for c, v in enumerate(vals, start=1):
            cell = ws.cell(r, c)
            cell.value = v
            if k == 0:
                pass
        # 复制样式（含边框/字体/对齐）—— 源行同列
        for c in range(1, src.max_column + 1):
            s = src.cell(style_row, c)
            t = ws.cell(r, c)
            t._style = s._style
        if style_row in src.row_dimensions and src.row_dimensions[style_row].height:
            ws.row_dimensions[r].height = src.row_dimensions[style_row].height

    wb.save(XLSX)

    # ---------- 校验 ----------
    with zipfile.ZipFile(XLSX) as z:
        bad = z.testzip()
    if bad:
        raise SystemExit(f"⛔ xlsx 损坏：{bad}")
    wb2 = openpyxl.load_workbook(XLSX)
    fp_after = {w.title: w.freeze_panes for w in wb2.worksheets}
    for t in fp_before:
        if fp_after.get(t) != fp_before[t]:
            raise SystemExit(f"⛔ freeze_panes 被改动：{t} {fp_before[t]} → {fp_after.get(t)}")
    w = wb2[NEW_SHEET]
    got = [w.cell(r, 1).value for r in range(5, 12)]
    if got != [240, 241, 242, 243, 244, 245, 246]:
        raise SystemExit(f"⛔ # 列异常：{got}")
    # DV / CF / freeze 必须与源表一致
    n_dv_src = len(wb2[SRC_SHEET].data_validations.dataValidation)
    n_dv_new = len(w.data_validations.dataValidation)
    n_cf_src = sum(len(c.rules) for c in wb2[SRC_SHEET].conditional_formatting)
    n_cf_new = sum(len(c.rules) for c in w.conditional_formatting)
    if n_dv_new != n_dv_src:
        raise SystemExit(f"⛔ 新表 DV 数不符：{n_dv_new} != {n_dv_src}")
    if n_cf_new != n_cf_src:
        raise SystemExit(f"⛔ 新表 CF 规则数不符：{n_cf_new} != {n_cf_src}")
    if w.freeze_panes != wb2[SRC_SHEET].freeze_panes:
        raise SystemExit(f"⛔ 新表 freeze 不符：{w.freeze_panes!r} != {wb2[SRC_SHEET].freeze_panes!r}")
    st = {w.cell(r, 13).value for r in range(5, 12)}
    if st != {"已发送"}:
        raise SystemExit(f"⛔ 状态列异常：{st}")
    print(f"✅ xlsx 已更新：新增子表 `{NEW_SHEET}`，#240–246 共 7 行")
    print(f"   DV {n_dv_src} → {n_dv_new} ｜ CF 规则 {n_cf_src} → {n_cf_new} ｜ freeze {w.freeze_panes!r}")
    print(f"   freeze 全表：{fp_after}")

    # ---------- md ----------
    md = MD.read_text(encoding="utf-8")
    if "### 240." in md:
        raise SystemExit("⛔ md 中已存在 `### 240.` —— 请先人工确认")
    blocks = []
    for k, num in enumerate(nums):
        r = 240 + k
        d = by_num[num]
        email, sent_bj, tzlab, sent_local = SENT[num]
        blocks.append(
            f"### {r}. {d['公司名称']}\n\n"
            f"| 字段 | 内容 |\n|---|---|\n"
            f"| 发送日期 | {SEND_DATE} |\n"
            f"| 公司名称 | {d['公司名称']} |\n"
            f"| 国家/地区 | {COUNTRY[num]} |\n"
            f"| 联系人 | {d['联系人']} |\n"
            f"| 职位 | {d['职位']} |\n"
            f"| 买家类型 | {d['买家类型']} |\n"
            f"| 需求产品 | {d['需求产品']} |\n"
            f"| 触达来源 | 官网一手源 |\n"
            f"| 骨架 | A（batch7 A 档 —— 具名 + 一手源，可主送） |\n"
            f"| 建议发送时间 | {sent_bj[11:]}（{tzlab} 当地 {sent_local}，破例未走 9–10 点窗口） |\n"
            f"| 邮箱 | {email} |\n"
            f"| 状态 | 已发送 |\n"
            f"| 跟进次数 | 0 |\n"
            f"| 下次跟进日 | {NEXT_FU} |\n"
            f"| 最后联系日 | {SEND_DATE} |\n"
            f"| 备注 | 买家{num}｜batch7 A 档｜首封 {sent_bj} 北京发出；下一步 D+3（{NEXT_FU}）首轮跟进，须带新信息点 |\n\n"
            f"**信文件**：{LETTER[num]}\n\n---\n\n"
        )
    md = md.rstrip("\n") + "\n\n" + "".join(blocks)
    MD.write_text(md, encoding="utf-8")
    print(f"✅ md 已追加 7 个明细块（### 240. – ### 246.）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
