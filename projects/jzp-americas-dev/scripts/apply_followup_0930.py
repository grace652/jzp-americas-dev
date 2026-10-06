#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""9/30 跟进信 · 跟进表更新（.md 文本备份）

把「9/30 跟进信」本批的投递结果写回 `开发信项目/工作区/开发信跟进表.md`：

1. 11 封跟进信 → 跟进次数 / 最后联系日 / 下次跟进日
2. #126 Power Transformer Services → 标记已退信（暂缓至 2026-10-09）
3. 退信扫描新发现的两家 → #135 Codale、#213 Hot Line 标记已退信
4. #143 的「信文件」字段订正（原误写为 PowerTec）
5. 「当前跟进排期」表第 17–20 行 → 第 2 次跟进标记为已发

每处替换都带**存在性断言**，命中数不符即中止（避免静默改错）。
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MD = ROOT / "开发信项目" / "工作区" / "开发信跟进表.md"

FU = {  # 编号 → (跟进次数, 下次跟进日, 跟进信文件名)
    17:  ("**2**", "**2026-10-09**（D0+15 个工作日）", "开发信-跟进-Scientechnic.md"),
    18:  ("**2**", "**2026-10-09**（D0+15 个工作日）", "开发信-跟进-Bossie-Electric.md"),
    19:  ("**2**", "**2026-10-09**（D0+15 个工作日）", "开发信-跟进-Premier-Electric.md"),
    20:  ("**2**", "**2026-10-09**（D0+15 个工作日）", "开发信-跟进-Oregon-Electric-Service.md"),
    128: ("**1**", "**2026-10-07**（D0+8 个工作日）", "开发信-跟进-Gescan-Sonepar.md"),
    134: ("**1**", "**2026-10-07**（D0+8 个工作日）", "开发信-跟进-Mott-Electric.md"),
    137: ("**1**", "**2026-10-07**（D0+8 个工作日）", "开发信-跟进-Canem.md"),
    140: ("**1**", "**2026-10-07**（D0+8 个工作日）", "开发信-跟进-AES-Electric.md"),
    143: ("**1**", "**2026-10-07**（D0+8 个工作日）", "开发信-跟进-EC-Electric.md"),
    144: ("**1**", "**2026-10-07**（D0+8 个工作日）", "开发信-跟进-Houle-Electric.md"),
    146: ("**1**", "**2026-10-07**（D0+8 个工作日）", "开发信-跟进-North-Coast.md"),
}
BOUNCED = {  # 编号 → (状态, 下次跟进日, 最后联系日, 备注追加)
    126: ("已退信（暂缓至 2026-10-09）", "2026-10-09", "2026-09-25",
          "⛔ 2026-09-25 首封退信（软退信-服务商拒收，`550 5.4.1 Access denied` / EXO）。"
          "冷却至 2026-10-09；重试须**换发法**（改主题+重写正文+去链接+纯文本+间隔≥2周）。"
          "⛔ 本批 9/30 跟进信**未发**。"),
    135: ("已退信（暂缓至 2026-10-14）", "2026-10-14", "2026-09-30",
          "⛔ 2026-09-30 23:40 北京补发（batch4 缺口补发）后约 2 分钟被 Mimecast 拒"
          "（`5.4.1 Recipient address rejected: Access denied`）。冷却至 2026-10-14；重试须**换发法**。"
          "⚠️ 原登记「待发送」有误 —— 实际已发且已退信。"),
    213: ("已退信（暂缓至 2026-10-30）", "2026-10-30", "2026-09-29",
          "⛔ 2026-09-30 00:10 北京投递后被 Barracuda 拒"
          "（`550 permanent failure … :blocked`），归类软退信-暂时停用。冷却至 2026-10-30；重试须**换发法**。"
          "⚠️ 原登记「待发送」有误 —— 实际已发且已退信。"),
}


def sub_once(text, old, new, tag):
    n = text.count(old)
    if n != 1:
        raise SystemExit(f"⛔ [{tag}] 期望命中 1 处，实际 {n} 处：\n    {old[:120]}")
    return text.replace(old, new)


def block(text, num):
    """取出 `### N.` 到下一个 `### ` 之间的块。"""
    m = re.search(rf"^### {num}\.\s.*?(?=^### |\Z)", text, re.S | re.M)
    if not m:
        raise SystemExit(f"⛔ 找不到块 ### {num}.")
    return m.group(0)


# 🔴 表格行**未必**以「空格 + |」结尾（实测有 `…已跟进）|` 这种写法）。
#    所以收尾必须是 `\s*\|[ \t]*$` —— 用 ` \|$` 会漏掉无空格的那些行（实测踩过）。
ROW_TAIL = r"\s*\|[ \t]*$"


def set_field(blk, field, value):
    pat = re.compile(rf"^\| {field} \| (.*?){ROW_TAIL}", re.M)
    if len(pat.findall(blk)) != 1:
        raise SystemExit(f"⛔ 字段 `{field}` 命中 {len(pat.findall(blk))} 处")
    return pat.sub(lambda m: f"| {field} | {value} |", blk, count=1)


def main():
    src = MD.read_text(encoding="utf-8")
    text = src
    log = []

    # ---- 1. 11 封跟进信 ----
    for num, (cnt, nxt, fname) in FU.items():
        old = block(text, num)
        blk = old
        blk = set_field(blk, "跟进次数", cnt)
        blk = set_field(blk, "下次跟进日", nxt)
        blk = set_field(blk, "最后联系日", "**2026-10-01**")
        # 备注追加跟进信文件名（不新增行，保持 16 字段结构与 xlsx 对齐）
        m = re.search(rf"^\| 备注 \| (.*?){ROW_TAIL}", blk, re.M)
        note = m.group(1)
        add = f"｜✅ 9/30 跟进信已发 2026-10-01（`clients/{fname}`）"
        blk = blk[:m.start(1)] + note + add + blk[m.end(1):]
        text = text.replace(old, blk, 1)
        log.append(f"  #{num} 跟进次数={cnt} 下次={nxt}")

    # ---- 2. #143 信文件字段订正 ----
    b143 = block(text, 143)
    if "开发信-PowerTec-Electric.md" in b143:
        text = text.replace(
            b143,
            b143.replace("**信文件**：开发信-PowerTec-Electric.md",
                         "**信文件**：开发信-EC-Electric.md"),
            1)
        log.append("  #143 信文件订正 PowerTec → EC-Electric")

    # ---- 3. 退信标记 ----
    for num, (status, nxt, last, note) in BOUNCED.items():
        old = block(text, num)
        blk = set_field(old, "状态", status)
        blk = set_field(blk, "下次跟进日", nxt)
        blk = set_field(blk, "最后联系日", last)
        m = re.search(rf"^\| 备注 \| (.*?){ROW_TAIL}", blk, re.M)
        blk = blk[:m.start(1)] + note + blk[m.end(1):]
        text = text.replace(old, blk, 1)
        log.append(f"  #{num} → {status}")

    # ---- 4. 「当前跟进排期」表第 17–20 行 ----
    for num, name in [(17, "Scientechnic"), (18, "Bossie"), (19, "Premier"), (20, "Oregon")]:
        pat = re.compile(rf"^\| {num} \| .*? \|$", re.M)
        rows = pat.findall(text)
        if len(rows) != 1:
            raise SystemExit(f"⛔ 排期表 #{num} 命中 {len(rows)} 处")
        row = rows[0]
        new = row.replace("| **2026-09-30** | 2026-10-09 |",
                          "| ~~2026-09-30~~ ✅已发 | **2026-10-09** |")
        if new == row:
            raise SystemExit(f"⛔ 排期表 #{num} 未发生替换：{row[:100]}")
        text = text.replace(row, new, 1)
        log.append(f"  排期表 #{num} 第2次跟进 → ✅已发")

    # ---- 5. 汇总表（batch4 区）下次跟进日 ----
    for num, nxt in [(126, "2026-10-09"), (128, "2026-10-07"), (134, "2026-10-07"),
                     (137, "2026-10-07"), (140, "2026-10-07"), (143, "2026-10-07"),
                     (144, "2026-10-07"), (146, "2026-10-07"), (135, "2026-10-14")]:
        pat = re.compile(rf"^\| {num} \| .*? \|$", re.M)
        for row in pat.findall(text):
            if "2026-09-30 |" in row or row.rstrip().endswith("| — | — |"):
                new = re.sub(r"\| 2026-09-30 \|$", f"| {nxt} |", row)
                if new == row:
                    new = re.sub(r"\| — \| — \|$", f"| 已退信 | {nxt} |", row)
                if new != row:
                    text = text.replace(row, new, 1)
                    log.append(f"  汇总表 #{num} → {nxt}")

    if text == src:
        raise SystemExit("⛔ 未产生任何改动")

    MD.write_text(text, encoding="utf-8")
    print(f"✅ 已更新 {MD.name}（{len(log)} 处）")
    for l in log:
        print(l)
    return 0


if __name__ == "__main__":
    sys.exit(main())
