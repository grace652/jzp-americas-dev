#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""新增「已退信」状态 + 把 11 家主送退信的客户改标（.xlsx 主文件）

依据 `开发信项目/01_skill_email_writing.md` §十一：
  · 🔴 **绝不读写 `freeze_panes`**（getter 返回 "C60"，写回会把冻结行变 1–59）
  · 新增一个状态 = **① 下拉 ② 配色 ③ 图例，三处齐改**（§十一 L711–717 的教训）
  · 只改已有单元格值，不新增行

配色：`已退信` = **EF9A9A**（Material Red 200），与 `已放弃` 的 FFCDD2（Red 100）同族更深。
⚠️ 老 sheet 的 dxf 用 `FFxxxxxx`，新 sheet 用 `00xxxxxx` —— **各按各自既有写法**，不互抄。
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
BAK = ROOT / ".workbuddy-ai/开发信跟进表.bak-20261001-加已退信前.xlsx"

C_STATUS, C_NEXT, C_NOTE = 13, 15, 17
NEW_STATUS = "已退信"
NEW_COLOR = "EF9A9A"          # Material Red 200
CF_RANGE = "M5:M200"

# # → (下次跟进日, 备注追加；None = 不追加)
TARGETS = {
    13:  ("2026-10-17", "⛔ 主送已退信：软退信-暂时停用（bellsouth.net 554.30 邮箱停用）。冷却至 2026-10-17；重试须换发法（改主题+重写正文+去链接+纯文本+间隔≥2周）。"),
    63:  ("2026-10-13", "⛔ 主送已退信：软退信-服务商拒收（EXO `550 5.4.1 Access denied`）×2 地址 + 整域封锁 `birminghamec.com`。冷却至 2026-10-13；重试须换发法。"),
    82:  ("—",          "⛔ 主送已退信：硬退信-地址不存在（`jrav@` 9/24，唯一具名直邮）→ **永久排除**。备选 `info@heicontractors.com`（B档）未验证；改走电话 219-922-9886。"),
    90:  ("—",          "⛔ 主送已退信：硬退信-地址不存在（Google NoSuchUser 9/25）→ **永久排除**。仅剩电话 907 跟进。"),
    104: ("2026-10-08", "⛔ 主送已退信：软退信-服务商拒收（Mimecast `5.4.1` 9/24）。冷却至 2026-10-08；重试须换发法。"),
    106: ("2026-10-09", "⛔ 主送已退信：软退信-服务商拒收（EXO `550 5.4.1` 9/25）。冷却至 2026-10-09；重试须换发法。"),
    126: ("2026-10-09", None),      # 备注上轮已写全
    135: ("2026-10-14", None),
    151: ("2026-10-13", "⛔ 主送已退信：软退信-服务商拒收（EXO `550 5.4.1` 9/29）。冷却至 2026-10-13；重试须换发法。"),
    213: ("2026-10-30", None),
}
# 说明：**#9 KVA Electric 保留 `已放弃`**（确认停业，属「我方判断」，不是单纯地址问题）


def find_row(ws, num):
    hits = [r for r in range(5, ws.max_row + 1) if ws.cell(r, 1).value == num]
    if len(hits) != 1:
        raise SystemExit(f"⛔ 表 `{ws.title}` 中 #{num} 命中 {len(hits)} 行")
    return hits[0]


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
    """按该 sheet 既有 dxf 写法新增一条 cellIs 规则。"""
    for rng, rules in ws.conditional_formatting._cf_rules.items():
        for r in rules:
            if str(r.formula) == f'["\'{opt}\'"]'.replace("'", '"') or opt in str(r.formula):
                return "已有"
    if alpha == "FF":      # 老 sheet：fgColor 上色，bg 黑
        fill = PatternFill(patternType="solid", fgColor=alpha + hexcolor, bgColor="00000000")
    else:                  # 新 sheet：fg/bg 同色
        fill = PatternFill(patternType="solid", fgColor=alpha + hexcolor, bgColor=alpha + hexcolor)
    dxf = DifferentialStyle(fill=fill)
    rule = Rule(type="cellIs", operator="equal", formula=[f'"{opt}"'], dxf=dxf, stopIfTrue=False)
    ws.conditional_formatting.add(CF_RANGE, rule)
    return "已加"


def main():
    if not BAK.exists():
        shutil.copy2(XLSX, BAK)
        print(f"已备份 → {BAK.name}")

    wb = openpyxl.load_workbook(XLSX)
    freeze_before = {ws.title: ws.freeze_panes for ws in wb.worksheets}
    print("改前 freeze:", freeze_before)
    print()

    for ws in wb.worksheets:
        alpha = "FF" if ws.title == "开发信跟进表" else "00"
        print(f"[{ws.title}] DV {add_dv_option(ws, NEW_STATUS)} ｜ CF {add_cf_rule(ws, NEW_STATUS, NEW_COLOR, alpha)}")

    print()
    for num, (nxt, note) in TARGETS.items():
        ws = next((w for w in wb.worksheets
                   if any(w.cell(r, 1).value == num for r in range(5, w.max_row + 1))), None)
        if ws is None:
            raise SystemExit(f"⛔ 两个 sheet 都找不到 #{num}")
        r = find_row(ws, num)
        old = ws.cell(r, C_STATUS).value
        ws.cell(r, C_STATUS).value = NEW_STATUS
        ws.cell(r, C_NEXT).value = nxt
        if note:
            cur = ws.cell(r, C_NOTE).value or ""
            ws.cell(r, C_NOTE).value = (cur + "｜" if cur and cur != "—" else "") + note
        print(f"  #{num:<5}[{ws.title}] r{r:<4} 状态 {old!r} → {NEW_STATUS!r} ｜ 下次 {nxt}")

    wb.save(XLSX)

    with zipfile.ZipFile(XLSX) as z:
        bad = z.testzip()
    if bad:
        raise SystemExit(f"⛔ xlsx 损坏：{bad}")

    # ---- 复核 ----
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
                    if NEW_STATUS in str(rule.formula):
                        f = rule.dxf.fill
                        print(f"   ✅ 新增规则 {rule.formula} fg={f.fgColor.rgb} bg={f.bgColor.rgb} {f.patternType}")
        print(f"   M 列 CF 规则数 = {n}（应为 10）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
