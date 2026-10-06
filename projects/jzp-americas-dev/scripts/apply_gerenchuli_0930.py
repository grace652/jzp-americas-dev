#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 `个人处理` 补进 M 列下拉 + 条件格式 + md 图例

背景：`#72 RESCO (Rural Electric Supply Coop)` 的 M 列填了 `个人处理`，
但**不在下拉列表里**（历史遗留）→ Excel 标无效、条件格式不变色。

与上一轮「已退信」同一套**三处齐改**（`01_skill_email_writing.md` §十一 的教训）：
  ① DV（M 列，两个 sheet）② CF（M5:M200，两个 sheet）③ 图例（.md）

配色：`个人处理` = **B0BEC5**（Blue Grey 200）—— 中性灰蓝，不与现有 11 色冲突。
⚠️ 老 sheet 的 dxf 用 `FFxxxxxx`（fg 上色 / bg 黑），新 sheet 用 `00xxxxxx`（fg/bg 同色）—— 各按各自写法。
"""

import shutil
import sys
import zipfile
from pathlib import Path

import openpyxl
from openpyxl.formatting.rule import Rule
from openpyxl.styles import PatternFill
from openpyxl.styles.differential import DifferentialStyle

ROOT = Path(Path(__file__).resolve().parents[1])
XLSX = ROOT / "开发信项目/工作区/开发信跟进表.xlsx"
BAK = ROOT / ".workbuddy-ai/开发信跟进表.bak-20261001-加个人处理前.xlsx"

OPT = "个人处理"
COLOR = "B0BEC5"
CF_RANGE = "M5:M200"


def add_dv_option(ws, opt):
    for dv in ws.data_validations.dataValidation:
        if not str(dv.sqref).startswith("M"):
            continue
        f = dv.formula1 or ""
        if opt in f:
            return "已有"
        if not (f.startswith('"') and f.endswith('"')):
            raise SystemExit(f"⛔ {ws.title} M 列 DV 格式异常：{f[:60]}")
        dv.formula1 = f[:-1] + "," + opt + '"'
        return "已加"
    raise SystemExit(f"⛔ {ws.title} 找不到 M 列 DataValidation")


def add_cf_rule(ws, opt, hexcolor, alpha):
    for rng, rules in ws.conditional_formatting._cf_rules.items():
        for r in rules:
            if opt in str(r.formula):
                return "已有"
    if alpha == "FF":
        fill = PatternFill(patternType="solid", fgColor=alpha + hexcolor, bgColor="00000000")
    else:
        fill = PatternFill(patternType="solid", fgColor=alpha + hexcolor, bgColor=alpha + hexcolor)
    rule = Rule(type="cellIs", operator="equal", formula=[f'"{opt}"'], dxf=DifferentialStyle(fill=fill),
                stopIfTrue=False)
    ws.conditional_formatting.add(CF_RANGE, rule)
    return "已加"


def main():
    if not BAK.exists():
        shutil.copy2(XLSX, BAK)
        print(f"已备份 → {BAK.name}")

    wb = openpyxl.load_workbook(XLSX)
    freeze_before = {ws.title: ws.freeze_panes for ws in wb.worksheets}
    print("改前 freeze:", freeze_before)

    for ws in wb.worksheets:
        alpha = "FF" if ws.title == "开发信跟进表" else "00"
        print(f"[{ws.title}] DV {add_dv_option(ws, OPT)} ｜ CF {add_cf_rule(ws, OPT, COLOR, alpha)}")

    wb.save(XLSX)

    with zipfile.ZipFile(XLSX) as z:
        bad = z.testzip()
    if bad:
        raise SystemExit(f"⛔ xlsx 损坏：{bad}")

    wb2 = openpyxl.load_workbook(XLSX)
    freeze_after = {ws.title: ws.freeze_panes for ws in wb2.worksheets}
    print()
    print("改后 freeze:", freeze_after)
    if freeze_after != freeze_before:
        raise SystemExit("⛔ freeze_panes 被改动！")
    print("✅ freeze_panes 未被改动")
    for ws in wb2.worksheets:
        dv = [d.formula1 for d in ws.data_validations.dataValidation if str(d.sqref).startswith("M")]
        print(f"[{ws.title}] DV = {dv}")
        n = 0
        for rng, rules in ws.conditional_formatting._cf_rules.items():
            for rule in rules:
                if str(rng.sqref).startswith("M"):
                    n += 1
                    if OPT in str(rule.formula):
                        f = rule.dxf.fill
                        print(f"   ✅ 新规则 {rule.formula} fg={f.fgColor.rgb} bg={f.bgColor.rgb} {f.patternType}")
        print(f"   M 列 CF 规则数 = {n}（应为 11）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
