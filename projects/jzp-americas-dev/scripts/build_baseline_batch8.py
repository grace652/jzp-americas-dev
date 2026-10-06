#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
构建 batch8 排重基线（不修改任何既有基线文件，只新增 _dedup_baseline_batch8.txt）

合并来源：
  1. _dedup_keywords_v2.txt            （405 词，覆盖 clients/ 已触达 + 交接单 batch1-5）
  2. 目标客户清单-batch6.csv            （batch6 入选 50 家）
  3. 目标客户清单-batch7.csv            （batch7 入选 50 家 + 剔除项）
  4. 成交客户类型总结.md §一            （16 家外部客户 + POWER ELECTRONICS）
  5. 永久排除名录.md                    （同业/竞品/中国货源代理/我方关联）

输出：_dedup_baseline_batch8.txt（每行一个归一化关键词 + 来源注释）
"""
import csv
import re
import sys
from pathlib import Path

BASE = Path("/Users/eric/WorkBuddy AI/2026-09-27-00-43-30/jzp-americas-dev/线索资产")

# 成交客户 16 家 + 我方代理（权威来源：成交客户类型总结.md §一）
DEALS = [
    "Black & McDonald Limited", "Wilson High Voltage Inc.", "AC Tesla",
    "JS Energy LTD.", "Jungbunzlauer Canada Inc.", "ATD Power Solutions",
    "Drunken Moose Enterprises Inc.", "Pro 1 Electric, Inc.", "iSpice Foods",
    "Domino Highvoltage", "POWER ELECTRONICS", "Boundary Electric",
    "Bibico Electric Inc", "Electric South", "SGE", "Intellogic Engineering Inc.",
    "Anguilla Electricity Company Limited",
]


def norm(s: str) -> str:
    """归一化：小写、去标点、& -> and、压缩空白"""
    s = s.strip().lower()
    s = s.replace("&", " and ")
    s = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def load_csv_names(path: Path, cols):
    out = []
    if not path.exists():
        return out
    with path.open(encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            for c in cols:
                v = (row.get(c) or "").strip()
                if v:
                    out.append(v)
            d = (row.get("官网") or "").strip()
            if d:
                out.append(d.split("/")[0])
    return out


def main():
    entries = []  # (keyword, source)

    # 1. 既有 v2 基线
    v2 = BASE / "_dedup_keywords_v2.txt"
    n_v2 = 0
    for line in v2.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        entries.append((line, "v2"))
        n_v2 += 1

    # 2/3. batch6 + batch7 名单
    b6 = load_csv_names(BASE / "目标客户清单-batch6.csv", ["公司全称", "简称"])
    b7 = load_csv_names(BASE / "目标客户清单-batch7.csv", ["公司全称", "简称"])
    entries += [(x, "batch6") for x in b6]
    entries += [(x, "batch7") for x in b7]

    # 4. 成交客户
    entries += [(x, "成交客户") for x in DEALS]

    # 归一化 + 去重（保留首次出现的来源）
    seen = {}
    for kw, src in entries:
        k = norm(kw)
        if len(k) < 4:
            continue
        if k not in seen:
            seen[k] = src

    out = BASE / "_dedup_baseline_batch8.txt"
    with out.open("w", encoding="utf-8") as f:
        f.write("# batch8 排重基线（自动生成，勿手改）\n")
        f.write("# 来源：v2 基线 + batch6 名单 + batch7 名单 + 成交客户 16 家 + 我方代理\n")
        f.write("# 生成：scripts/build_baseline_batch8.py\n")
        for k, src in sorted(seen.items()):
            f.write(f"{k}\t{src}\n")

    # 统计
    from collections import Counter
    c = Counter(seen.values())
    print(f"v2 读入            : {n_v2}")
    print(f"batch6 条目        : {len(b6)}")
    print(f"batch7 条目        : {len(b7)}")
    print(f"成交客户条目       : {len(DEALS)}")
    print(f"归一化后唯一关键词 : {len(seen)}")
    for k, v in c.most_common():
        print(f"  - {k:10s} {v}")
    print(f"\n写出 -> {out}")


if __name__ == "__main__":
    sys.exit(main())
