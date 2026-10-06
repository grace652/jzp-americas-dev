#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""阶段 4：md 同步（batch4 补登记）

改动：
  1. 插入 batch4 索引段 + 31 个明细块（`### 117.`–`### 147.`），位置在
     `## 新 sheet 索引（batch5+6 …）` 之前
  2. 把原 batch5+6 的 92 个块 `### 117.`–`### 208.` **顺延为 148–239**
  3. 同步更新 batch5+6 索引表里的 `#` 列
"""
import json, re, sys
from pathlib import Path

ROOT = Path(Path(__file__).resolve().parents[1])
MD = ROOT / "开发信项目/工作区/开发信跟进表.md"
OFFSET = 31
SPLIT = "## 新 sheet 索引（batch5+6"
MD_KEYS = ["发送日期", "公司名称", "国家/地区", "联系人", "职位", "买家类型", "需求产品",
           "触达来源", "骨架", "建议发送时间", "邮箱", "状态", "跟进次数", "下次跟进日",
           "最后联系日", "备注"]


def block(n, r):
    L = [f"### {n}. {r['公司名称']}", "", "| 字段 | 内容 |", "|---|---|"]
    for k in MD_KEYS:
        L.append(f"| {k} | {str(r.get(k, '') or '—')} |")
    L += ["", f"**信文件**：{r['_letter'] or '（未写信）'}", "", "---", ""]
    return "\n".join(L)


def main():
    dry = "--dry" in sys.argv
    rows = json.loads(Path("/tmp/batch4_rows.json").read_text(encoding="utf-8"))
    t = MD.read_text(encoding="utf-8")
    if "## 跟进明细（batch4 历史补登记" in t:
        print("⚠️ md 已含 batch4 段，跳过插入")
        return

    i = t.find(SPLIT)
    if i < 0:
        print("❌ 找不到 batch5+6 索引段起点")
        sys.exit(1)
    head, tail = t[:i], t[i:]

    # ---- 2) batch5+6 的 92 块顺延（### 117.–208. → 148.–239.）
    def rb(m):
        return f"### {int(m.group(1)) + OFFSET}. "
    tail_new = re.sub(r"^### (1[1-9]\d|20[0-8])\. ", rb, tail, flags=re.M)
    # 索引表的 # 列
    tail_new = re.sub(r"^\| (1[1-9]\d|20[0-8]) \| ", lambda m: f"| {int(m.group(1))+OFFSET} | ",
                      tail_new, flags=re.M)

    # ---- 1) batch4 段
    idx = ["## batch4 历史补登记（31 家 · 已发 2026-09-23–25）", "",
           "> 🔴 这 31 家**当时已发出但从未登记**，导致跟进排期被漏。本次补齐。",
           "> 其中 **5 家写了信但从未发出**（Graybar Canada / A&W High Voltage / Amtek / Codale / Gresco），已标记待补发。", "",
           "| # | 公司 | 买家号 | 国家/地区 | 状态 | 首封日 | 下次跟进日 |", "|---|---|---|---|---|---|---|"]
    for r in rows:
        idx.append(f"| {r['#']} | {r['公司名称'][:34]} | {r['_buyer']} | {r['国家/地区']} | "
                   f"{r['状态']} | {r['发送日期'] or '—'} | {r['下次跟进日'] or '—'} |")
    idx += ["", "---", "", "## 跟进明细（batch4 历史补登记 31 家）", ""]
    blocks = "\n".join(block(r["#"], r) for r in rows)
    mid = "\n".join(idx) + "\n" + blocks + "\n"

    out = head.rstrip() + "\n\n" + mid + "---\n\n" + tail_new
    if dry:
        print(f"[dry] {len(t)} → {len(out)} 字符")
        return
    MD.write_text(out, encoding="utf-8")
    print(f"✅ 已同步 {MD}")
    print(f"   {len(t)} → {len(out)} 字符（+{len(out)-len(t)}）")
    n = len(re.findall(r"^### \d+\. ", out, re.M))
    print(f"   明细块总数：{n}（应 116 + 31 + 92 = 239）")


if __name__ == "__main__":
    main()
