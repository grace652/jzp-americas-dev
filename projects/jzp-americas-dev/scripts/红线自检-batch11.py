#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""batch11 首封信红线自检 —— 复用项目自身的 parse_letter + compliance_check（不复刻逻辑）。"""
import sys
from pathlib import Path

ROOT = Path("/Users/eric/WorkBuddy AI/2026-09-27-00-43-30/jzp-americas-dev")
sys.path.insert(0, str(ROOT))

import importlib.util
spec = importlib.util.spec_from_file_location("senddev", ROOT / "发送开发信.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

LETTERS = [
    "开发信-Chemco.md", "开发信-Wescan.md", "开发信-VEC.md", "开发信-Agostino-Utilities.md",
    "开发信-Battaglia.md", "开发信-HB-Frazer.md", "开发信-Albarell.md", "开发信-White-Electrical.md",
    "开发信-C3M-Power.md", "开发信-Hatzel-Buehler.md", "开发信-Enerfab.md", "开发信-Inglett-Stubbs.md",
    "开发信-EMC-Electrical-Materials.md", "开发信-EcoTech-NL.md", "开发信-ONeil-Electric.md",
    "开发信-Lakeport-Power.md", "开发信-CTG-Power.md", "开发信-Piela-Electric.md",
    "开发信-Midwest-Machinery-Mart.md", "开发信-Powerhouse-Systems.md", "开发信-Sully-Enterprises.md",
    "开发信-Megawatt-Equipment.md",
]

CLIENTS = ROOT / "开发信项目/clients"
ok = fail = 0
for fn in LETTERS:
    p = CLIENTS / fn
    if not p.exists():
        print(f"❌ 缺文件 {fn}")
        fail += 1
        continue
    subjects, body, notes = m.parse_letter(p)
    problems = m.compliance_check(body, "", followup=False)
    words = len(body.split())
    if problems:
        fail += 1
        print(f"⛔ {fn}  ({words} 词)")
        for x in problems:
            print(f"      · {x}")
    else:
        ok += 1
        print(f"✅ {fn}  ({words} 词)  主题 {len(subjects)} 条")

print(f"\n通过 {ok} / 不通过 {fail} / 共 {len(LETTERS)}")
