#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
把「跟进信-20260928」的 4 个汇总文件，拆成**逐家独立信件文件**，
写入本项目 `开发信项目/clients/`，格式对齐 `发送开发信.py: parse_letter()`。

为什么拆
--------
定时发送/发送开发信 的链路是**一文件一信**（`parse_letter` 只认单个
`【Subject 备选】/【正文】/【中文批注】` 三元组）。汇总文件里一节一客户，
必须拆开才能进队列。

为什么转格式
------------
我写的跟进信用的是 `**主题**：\`…\`` + `【批注】`；
而 `parse_letter()` 认的是 `【Subject 备选】` + `【中文批注】`。
不转 → subjects 为空、notes 为空 → 收件人取不到 → 静默不发。

抄送来源
--------
以**我写的信件表头**为准（清单里的抄送列是给人看的，含「建议加」「⛔ 已剔除」等说明文字，
不能直接当地址用）。
"""
import re
import sys
from pathlib import Path

SRC = Path("/Users/eric/Downloads/开发客户流程agent/项目：开发信2026-09-15-14-09-34"
           "/project3/clients/跟进信-20260928")
DST = Path(__file__).resolve().parent / "开发信项目" / "clients"

FILES = [
    "跟进信-第2轮-20260928-A已跟进1次.md",
    "跟进信-第1轮-20260928-B首封0922批次.md",
    "跟进信-第1轮-20260928-C首封0923批次.md",
    "跟进信-20260928-D-PSS已回复线程推进.md",
]

# (公司名匹配键, 主送, 抄送列表, slug)
# 主送/抄送以信件表头为准；抄送只写**真实可用**地址
RECIP = {
    "B.G. High Voltage":        (["bberneche@bg-high-voltage.ca"], ["mail@bg-high-voltage.ca"], "BG-High-Voltage"),
    "Ontario High Voltage":     (["taylor@ontariohighvoltage.com"], ["Office@ontariohighvoltage.com"], "Ontario-High-Voltage"),
    "ISCOCA":                   (["iscoca@iscoca.ca"], [], "ISCOCA"),
    "Williams Electric":        (["keith@williamsele.com"], ["ron@williamsele.com"], "Williams-Electric"),
    "ALCO Electric":            (["brian@alco-electric.com"], ["jason@alco-electric.com", "kylie@alco-electric.com"], "ALCO-Electric"),
    "Alaska Line Builders":     (["andyk@aklinebuilders.com"], ["amey@aklinebuilders.com", "robby@aklinebuilders.com"], "Alaska-Line-Builders"),
    "PowerTec Electric":        (["info@ptellc.com"], [], "PowerTec-Electric"),
    "Power Substation":         (["joe.holler@epsonline.com"], [], "PSS"),
    "Reeve Electric":           (["info@reeve-electric.com"], [], "Reeve-Electric"),
    "DECH High Voltage":        (["office@dechhighvoltage.com"], [], "DECH-High-Voltage"),
    "Rogers Electrical":        (["info@r-ecci.com"], ["kwalters@r-ecci.com"], "Rogers-Electrical"),
    "South Charleston":         (["sales@southcharlestonelectric.com"], [], "South-Charleston"),
    "Washington State Power":   (["donna@wastatepower.com"], [], "Washington-State-Power"),
    "VoltCore":                 (["william@voltcoreelectrical.com"], [], "VoltCore-Electrical"),
    "GLS Electric":             (["contact@glselectricinc.com"], [], "GLS-Electric"),
    "Rexel Utility":            (["UtilitySalesCanada@rexel.ca"], [], "Rexel-Utility"),
    "GEC":                      (["info@gecincorporated.com"], ["sypolt@gecincorporated.com"], "GEC"),
    "Sunbelt Solomon":          (["info@sunbeltsolomon.com"], [], "Sunbelt-Solomon"),
    "Westmoreland":             (["bowens@westmorelandelectric.com"], [], "Westmoreland"),
    "Dana Power":               (["danapowerpoles@gmail.com"], [], "Dana-Power"),
    "GRIDLINK":                 (["info@gridlink.ca"], ["jbernst@gridlink.ca"], "GRIDLINK"),
    "Kirby Electric":           (["RMCMILLAN@KIRBYELECTRICINC.COM"], [], "Kirby-Electric"),
    "Stewart Electric":         (["info@stewartelectricinc.com"], [], "Stewart-Electric"),
    "Texas Electric Coop":      (["utilitysales@texas-ec.org"], ["directory@texas-ec.org"], "TEC"),
    "Birmingham Electrical":    (["walt@birminghamec.com", "jwarren@birminghamec.com"], [], "Birmingham-Electric"),
    "Everlast Electric":        (["mike@everlastelectric.ca"], ["info@everlastelectric.ca"], "Everlast-Electric"),
    "Priester":                 (["sales@pmn-inc.com"], [], "Priester"),
    "Tryggr":                   (["greg@tryggrtech.ca"], [], "Tryggr"),
    "Amps Powerline":           (["rnault@ampspowerline.ca"], ["knewman@ampspowerline.ca"], "Amps-Powerline"),
    "Fullford Electric":        (["FEI@fullfordelectric.com"], ["lael@fullfordelectric.com"], "Fullford-Electric"),
    "Arkansas Electric":        (["communications@aecc.com"], [], "AECI"),
    "United Utility Supply":    (["etalley@uus.coop"], [], "UUS"),
    "Western United Electric":  (["customerservice@wue.coop"], [], "WUE"),
    "CEEUS":                    (["tkyzer@ceeus.com"], ["tbrown@ceeus.com"], "CEEUS"),
    "General Pacific":          (["contractorsales@generalpacific.com"], [], "General-Pacific"),
    "GNS Technologies":         (["robertg@gns-technologies.com"], [], "GNS-Technologies"),
    "RESA Power":               (["sales@resapower.com"], [], "RESA-Power"),
    "TM3":                      (["tmcswain@tm3inc.com"], [], "TM3"),
}

ROUND_OF = {}
for f in FILES:
    rnd = "第2轮(D0+8)" if "-第2轮-" in f else ("推进已回复线程" if "-D-PSS" in f else "第1轮(D0+3)")
    ROUND_OF[f] = rnd


def match_recip(company: str):
    """按公司名前缀匹配收件人表。"""
    for key, val in RECIP.items():
        if company.startswith(key) or key in company:
            return val
    return None


def parse_sections(text: str):
    """把汇总文件切成 (序号, 公司名, 联系人, 主题, 正文, 是否不发)。"""
    parts = re.split(r"\n(?=## )", text)
    out = []
    for p in parts:
        m = re.match(r"##\s*([①-⑳])\s*(.+?)(?:\n|$)", p)
        if not m:
            continue
        head = m.group(2).strip()
        if "本轮不发" in head or "⏸️" in head:
            continue                                   # 跳过不发项
        if "WinAsia" in head:
            continue                                   # 用户决定跳过
        # 公司名 / 联系人
        if "—" in head:
            company, contact = head.split("—", 1)
        else:
            company, contact = head, ""
        company = re.sub(r"\s*\(.*?\)\s*$", "", company.strip()).strip()
        company = company.replace("~~", "").strip()
        contact = contact.strip()
        # 主题
        ms = re.search(r"\*\*主题\*\*：`([^`]+)`", p)
        if not ms:
            continue
        subject = ms.group(1).strip()
        # 正文（【正文】 → 【批注】）
        mb = re.search(r"【正文】\n(.*?)(?=\n【批注】|\n【中文批注】|\n>|\Z)", p, re.S)
        if not mb:
            continue
        body = mb.group(1).strip()
        # 去掉正文里可能残留的删除线/提示行
        body = "\n".join(l for l in body.split("\n")
                         if not l.strip().startswith(("~~", "⛔", ">", "⚠️")))
        body = body.strip()
        if not body or len(body) < 40:
            continue
        out.append(dict(company=company, contact=contact, subject=subject, body=body))
    return out


def main():
    DST.mkdir(parents=True, exist_ok=True)
    written, skipped = [], []
    for fn in FILES:
        p = SRC / fn
        if not p.exists():
            print(f"⛔ 缺文件：{p}")
            return 1
        rnd = ROUND_OF[fn]
        for s in parse_sections(p.read_text(encoding="utf-8")):
            r = match_recip(s["company"])
            if not r:
                skipped.append((s["company"], "无收件人映射"))
                continue
            to, cc, slug = r
            to_line = "、".join(f"`{a}`" for a in to)
            cc_line = "、".join(f"`{a}`" for a in cc) if cc else "—"
            txt = (
                f"【Subject 备选】\n1. `{s['subject']}`\n\n"
                f"【正文】\n\n{s['body']}\n\n"
                f"【中文批注】\n"
                f"- **收件人**：**{s['contact'] or s['company']}**（{to_line}）\n"
                f"- **抄送**：{cc_line}\n"
                f"- 轮次：{rnd}\n"
                f"- 公司：{s['company']}\n"
                f"- 说明：跟进信（同主题 Re: 回复原线程）\n"
            )
            out = DST / f"开发信-跟进-{slug}.md"
            out.write_text(txt, encoding="utf-8")
            written.append((slug, to, cc, s["subject"][:46]))

    print(f"✅ 写出 {len(written)} 封\n")
    for slug, to, cc, subj in written:
        ccx = ("｜cc " + ",".join(cc)) if cc else ""
        print(f"  {slug:28s} → {','.join(to):38s}{ccx}")
    if skipped:
        print(f"\n⚠️ 跳过 {len(skipped)}：")
        for c, why in skipped:
            print(f"   {c} — {why}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
