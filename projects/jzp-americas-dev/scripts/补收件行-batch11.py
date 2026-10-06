#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""batch11 A 档 22 封：在「中文注解」段首插入 `- **收件人**：…` 行，使 recipients_of() 可解析。

🔴 教训（batch8 犯过）：收件人行必须插在**注解段首**，插到文件头 `>` 块里**无效**。
"""
import re
from pathlib import Path

CLI = Path(Path(__file__).resolve().parents[1] / "开发信项目/clients")

# 文件名 -> (姓名, 职务, 邮箱, 来源说明)
R = {
    "开发信-Chemco.md": ("Brian Halina", "CEO", "bhalina@chemco.com", "ECAA 2026-2027 省理事会页 mailto 一手明文"),
    "开发信-Wescan.md": ("Shawn Henry", "President", "shawn@wescan-services.com", "官网一手明文"),
    "开发信-VEC.md": ("Ron Remsey", "VP, Power", "r_remsey@vecohio.com", "NECA North Central Ohio 名录一手明文"),
    "开发信-Agostino-Utilities.md": ("Albert Augustine, Jr.", "President / CEO", "aaugustine@agostinoutilities.com", "NECA Penn-Del-Jersey 名录一手明文"),
    "开发信-Battaglia.md": ("Jim Meyer", "President", "jmeyer@battag.com", "NECA Penn-Del-Jersey 名录一手明文"),
    "开发信-HB-Frazer.md": ("Franklin P. Holleran", "President", "fholleran@hbfrazer.com", "NECA Penn-Del-Jersey 名录一手明文"),
    "开发信-Albarell.md": ("Michael A. Conkey", "President", "mikec@albarell.com", "NECA Penn-Del-Jersey 名录一手明文"),
    "开发信-White-Electrical.md": ("Matt Varnado", "VP, Preconstruction", "mvarnado@white-electrical.com", "官网 Leadership 页一手明文"),
    "开发信-C3M-Power.md": ("Charles \"Chuck\" Hinton", "Division President", "chuck.hinton@c3mpowersystems.com", "cage.report CAGE 一手 + 母集团官网双印证"),
    "开发信-Hatzel-Buehler.md": ("Kevin Martin", "VP / Branch Manager (Philadelphia HQ)", "k.martin@hatzelandbuehler.com", "官网 Contact 页一手明文"),
    "开发信-Enerfab.md": ("Jeffery Sloan", "Director of Purchasing", "jeff.sloan@enerfab.com", "cage.report CAGE 一手明文"),
    "开发信-Inglett-Stubbs.md": ("David Lytle", "VP, Inglett & Stubbs International (ISI 实体)", "dlytle@isiprime.com", "政府 NCAGE 登记一手明文"),
    "开发信-EMC-Electrical-Materials.md": ("Sales / Purchasing（人名待核）", "—", "tygel@electricalmaterials.ca", "官网 Contact 页 Sales/Purchasing 入口一手明文"),
    "开发信-EcoTech-NL.md": ("Gary Lovell", "Director, Operations & Business Development", "gary.lovell@ecotechnl.ca", "官网一手明文（Storyblok CMS 全站唯一具名邮箱）"),
    "开发信-ONeil-Electric.md": ("Josh Matthews", "分支经理（GTA West / Woodbridge）", "joshmatthews@oneilelectric.com", "官网 Contact 页一手明文"),
    "开发信-Lakeport-Power.md": ("Julie Ball", "Inside Sales / Purchasing", "jball@lakeportpower.com", "官网一手明文"),
    "开发信-CTG-Power.md": ("Michael L. Weaver", "Founder & CEO", "michael.weaver@ctgpowersystems.com", "官网 Leadership 页一手明文"),
    "开发信-Piela-Electric.md": ("Joseph W. Piela", "President", "joe@pielaelectric.com", "官网 Contact 页 2008 年存档一手明文（时效待核）"),
}

HEAD_RE = re.compile(r"^(##\s*三、中文注解[^\n]*\n)", re.M)
FIRST_ITEM_RE = re.compile(r"^(?:\s*\n)*(?=1\.\s*\*\*发信资格\*\*)", re.M)

fixed, skipped, already = [], [], []
for fn, (who, title, mail, src) in R.items():
    p = CLI / fn
    if not p.exists():
        skipped.append(f"{fn}（文件不存在）")
        continue
    t = p.read_text(encoding="utf-8")
    if re.search(r"\*\*收件人\*\*[：:]", t):
        already.append(fn)
        continue
    m = HEAD_RE.search(t)
    if not m:
        skipped.append(f"{fn}（未找到注解段标题）")
        continue
    line = f"\n- **收件人**：**{who} · {title}**（`{mail}`）—— {src}\n"
    insert_at = m.end()
    # 若标题后紧跟空行，插在空行之后、正文条目之前
    rest = t[insert_at:]
    mm = re.match(r"\s*", rest)
    insert_at += mm.end() if mm else 0
    t2 = t[:insert_at] + line.lstrip("\n") + t[insert_at:]
    p.write_text(t2, encoding="utf-8")
    fixed.append(fn)

print(f"✅ 已插入 {len(fixed)} 封")
for f in fixed:
    print("   ", f)
if already:
    print(f"\n⏭  已有收件人行（跳过）{len(already)} 封：")
    for f in already:
        print("   ", f)
if skipped:
    print(f"\n❌ 未处理 {len(skipped)} 封：")
    for f in skipped:
        print("   ", f)
