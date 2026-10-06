#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从 batch11 四路候选 md 中抽取「制表符分隔清单块」，生成 _batch11_candidates_raw.txt"""
import re
from pathlib import Path

BASE = Path(Path(__file__).resolve().parents[1] / "线索资产")
FILES = [
    "_batch11_A_加拿大_候选.md",
    "_batch11_A_美国_候选.md",
    "_batch11_B_加拿大_候选.md",
    "_batch11_B_美国_候选.md",
]

rows = []
for fn in FILES:
    txt = (BASE / fn).read_text(encoding="utf-8")
    blocks = re.findall(r"```(.*?)```", txt, re.S)
    picked = None
    for b in blocks:
        lines = [l.strip() for l in b.strip().splitlines() if l.strip()]
        if lines and sum(1 for l in lines if "\t" in l) >= max(3, len(lines) * 0.8):
            picked = lines
            break
    if not picked:
        print(f"⚠️ {fn} 未找到制表符清单块")
        continue
    print(f"{fn}: {len(picked)} 行")
    rows += picked

# 去重（按域名）
seen, out = set(), []
for r in rows:
    parts = r.split("\t")
    name, dom = parts[0].strip(), parts[1].strip().lower() if len(parts) > 1 else ""
    key = dom or name.lower()
    if key in seen:
        print(f"  ⚠️ 重复丢弃: {name} ({dom})")
        continue
    seen.add(key)
    out.append(f"{name}\t{dom}")

(BASE / "_batch11_candidates_raw.txt").write_text("\n".join(out) + "\n", encoding="utf-8")
print(f"\n合计 {len(out)} 家 -> _batch11_candidates_raw.txt")

# 同时生成纯域名文件供排重
(BASE / "_batch11_domains.txt").write_text("\n".join(r.split("\t")[1] for r in out) + "\n", encoding="utf-8")
print("域名清单 -> _batch11_domains.txt")
