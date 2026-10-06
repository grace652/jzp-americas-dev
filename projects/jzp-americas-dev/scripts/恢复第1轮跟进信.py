#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""事故恢复：把被覆盖的 16 封「第 1 轮跟进信」从 `Sent Messages` 还原

事故（2026-10-02 21:41）：生成 10/02 第 2 轮跟进信时，**沿用了第 1 轮的同名文件**
（`开发信-跟进-<Name>.md`），把这 16 封 9/28 批次的第 1 轮记录**覆盖**了。
非 git、无备份。

恢复策略：
  · 第 2 轮（我刚写的）→ 改名为 `开发信-跟进-第2轮-<Name>.md`（不再与第 1 轮同名）
  · 第 1 轮 → 从 `Sent Messages` 取**实际发出的正文**（权威原文）写回原名文件
    ⚠️ 原文件的「中文批注」**无法恢复**（未随邮件发出），已在文件头注明。
"""
import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path("/Users/eric/WorkBuddy AI/2026-09-27-00-43-30/jzp-americas-dev")
CL = ROOT / "开发信项目/clients"

# 16 家第 2 轮客户的【第 1 轮】文件原名（= 将被还原的名字）
R1 = {
    36: "开发信-跟进-Reeve-Electric.md", 37: "开发信-跟进-DECH-High-Voltage.md",
    38: "开发信-跟进-Rogers-Electrical.md", 39: "开发信-跟进-South-Charleston-Electric.md",
    40: "开发信-跟进-Washington-State-Power.md", 42: "开发信-跟进-VoltCore-Electrical.md",
    43: "开发信-跟进-GLS-Electric.md", 44: "开发信-跟进-Rexel-Utility.md",
    47: "开发信-跟进-GEC.md", 53: "开发信-跟进-Sunbelt-Solomon.md",
    55: "开发信-跟进-Westmoreland.md", 56: "开发信-跟进-Dana-Power.md",
    58: "开发信-跟进-GRIDLINK.md", 59: "开发信-跟进-Kirby-Electric.md",
    61: "开发信-跟进-Stewart-Electric.md", 62: "开发信-跟进-TEC.md",
}
# 收件人（用于在 Sent Messages 里定位第 1 轮那封）
TO = {
    36: "info@reeve-electric.com", 37: "office@dechhighvoltage.com",
    38: "info@r-ecci.com", 39: "sales@southcharlestionelectric.com",
    40: "donna@wastatepower.com", 42: "william@voltcoreelectrical.com",
    43: "contact@glselectricinc.com", 44: "utilitysalescanada@rexel.ca",
    47: "info@gecincorporated.com", 53: "info@sunbeltsolomon.com",
    55: "bowens@westmorelandelectric.com", 56: "danapowerpoles@gmail.com",
    58: "info@gridlink.ca", 59: "rmcmillan@kirbyelectricinc.com",
    61: "info@stewartelectricinc.com", 62: "utilitysales@texas-ec.org",
}


def main():
    # ---- ① 第 2 轮改名 ----
    renamed = []
    for f in R1.values():
        src = CL / f
        dst = CL / f.replace("开发信-跟进-", "开发信-跟进-第2轮-")
        if src.exists() and "第2轮" not in src.name:
            src.rename(dst)
            renamed.append(dst.name)
    print(f"① 第 2 轮改名 {len(renamed)} 个 → 开发信-跟进-第2轮-*.md")

    # ---- ② 从 Sent Messages 取第 1 轮正文 ----
    spec = importlib.util.spec_from_file_location("mcr", ROOT / "邮箱客户端.py")
    mc = importlib.util.module_from_spec(spec)
    sys.modules["mcr"] = mc
    spec.loader.exec_module(mc)
    m = mc.imap_connect(mc.load_config())
    m.select('"Sent Messages"', readonly=True)
    typ, d = m.search(None, "ALL")
    ids = d[0].split()

    idx = {}
    for num in ids:
        raw = mc.fetch_headers(m, num, "TO DATE")
        to = (mc.raw_header(raw, "To") or "").lower()
        dt = mc.raw_header(raw, "Date") or ""
        for n, addr in TO.items():
            if addr in to and ("28 Sep 2026" in dt or "29 Sep 2026" in dt):
                idx.setdefault(n, []).append(num)
    print(f"② 定位到第 1 轮发送：{sorted(idx)}")

    restored = []
    for n, nums in idx.items():
        num = nums[0]
        typ, dd = m.fetch(num, "(BODY.PEEK[])")
        import email
        msg = email.message_from_bytes(dd[0][1])
        txt = ""
        for p in msg.walk():
            if p.get_content_type() == "text/plain":
                txt = mc.smart_decode(p.get_payload(decode=True) or b"")
                break
        if not txt:
            for p in msg.walk():
                if p.get_content_type() == "text/html":
                    txt = mc.html_to_text(mc.smart_decode(p.get_payload(decode=True) or b""))
                    break
        body = re.split(r"\n\s*Sales Manager", txt)[0].rstrip()
        # 去掉引用的原邮件段（从第一个 From:/发件人 起）
        body = re.split(r"\n\s*(?:From:|发件人[:：])", body)[0].rstrip()
        head = ("## ⚠️ 本文件由 `Sent Messages` 还原（2026-10-02）\n\n"
                "> 事故：生成 10/02 第 2 轮跟进信时**误用同名文件**，覆盖了本封第 1 轮记录。\n"
                "> 现从邮箱**实际发出的原文**还原正文。\n"
                "> 🔴 **原「中文批注」无法恢复**（未随邮件发出）。第 2 轮信件已改名 `开发信-跟进-第2轮-*.md`。\n\n---\n\n")
        (CL / R1[n]).write_text(head + "【正文（还原自 Sent Messages）】\n\n" + body + "\n",
                                encoding="utf-8")
        restored.append((n, R1[n], len(body.split())))
    m.logout()
    print(f"③ 已还原 {len(restored)} 封第 1 轮跟进信：")
    for n, f, wc in sorted(restored):
        print(f"   #{n:<5}{wc:>3} 词  {f}")
    missing = [n for n in R1 if n not in idx]
    if missing:
        print("   ⚠️ 未在 Sent Messages 找到:", missing)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
