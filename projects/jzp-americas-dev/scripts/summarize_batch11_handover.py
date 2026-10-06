#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从 batch11 交接单里抽取闸门行 / 邮箱档位 / 收件人 / 母公司，做权威汇总。"""
import re
from pathlib import Path

BASE = Path(Path(__file__).resolve().parents[1] / "开发信项目/交接单/batch11_new_424plus")

rows = []
for f in sorted(BASE.glob("买家*.md"), key=lambda p: int(re.match(r"买家(\d+)", p.name).group(1))):
    n = int(re.match(r"买家(\d+)", f.name).group(1))
    t = f.read_text(encoding="utf-8")
    head = t[:3000]

    # 收件人行（batch10/11 惯例：`> 收件人：**姓名 · 职务** ｜ 主送 \`email\`（档位说明）`）
    rcpt = re.search(r"收件人[：:]\s*(.+)", head)
    rcpt = rcpt.group(1).strip() if rcpt else "—"

    # 发信资格
    gate = re.search(r"发信资格[：:]\s*(.+)", head)
    gate = gate.group(1).strip() if gate else "—"

    # 邮箱档位
    tier = re.search(r"邮箱档位[：:]\s*\*{0,2}([ABC][+\-−]?)", head)
    tier = tier.group(1) if tier else "—"

    # 邮箱地址（全文中所有邮件地址，取前 3）
    mails = re.findall(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}", t)
    mails = [m for m in dict.fromkeys(mails) if not m.lower().endswith(("example.com",))][:3]

    # 母公司/集团
    grp = re.search(r"母公司\s*/?\s*集团\*{0,2}\s*\|?\s*\*{0,2}([^\n|]{0,70})", t)
    grp = grp.group(1).strip(" *|") if grp else "—"

    name = re.sub(r"^买家\d+_", "", f.stem).replace("_开发信交接单", "")

    rows.append(dict(n=n, name=name, tier=tier, gate=gate, rcpt=rcpt[:90],
                     mails=" ｜ ".join(mails), grp=grp[:60], size=f.stat().st_size))

print(f"{'号':>4} {'档':<4} {'公司':<26} {'收件人':<46} {'邮箱'}")
print("-" * 150)
for r in rows:
    print(f"{r['n']:>4} {r['tier']:<4} {r['name'][:26]:<26} {r['rcpt'][:46]:<46} {r['mails'][:70]}")

from collections import Counter
print()
print("档位分布：", Counter(r["tier"] for r in rows))
gates = Counter("✅" if r["gate"].startswith("✅") else ("⛔" if "⛔" in r["gate"] else "⚠️") for r in rows)
print("发信资格：", gates)
print()
print("=== ⛔ / ⚠️ 需处理 ===")
for r in rows:
    if not r["gate"].startswith("✅"):
        print(f"  买家{r['n']} {r['name']} ｜ 档{r['tier']} ｜ {r['gate'][:80]}")
print()
print("=== 集团归属（非「独立」者）===")
for r in rows:
    g = r["grp"]
    if g and g != "—" and "独立" not in g[:4]:
        print(f"  买家{r['n']} {r['name'][:24]:<24} → {g[:70]}")
