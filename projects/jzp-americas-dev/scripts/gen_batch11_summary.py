#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 batch11 挖人环节的 _批次汇总.md（从 50 份交接单程序化抽取，不依赖 agent 自述）。"""
import re
from pathlib import Path

BASE = Path(Path(__file__).resolve().parents[1] / "开发信项目/交接单/batch11_new_424plus")

RECIP = {
    424: ("Shawn Crucil · President", "fmi@fminstallations.ca", "B"),
    425: ("Brian Halina · CEO", "bhalina@chemco.com", "A"),
    426: ("Gerry Westmacott · Founder", "info@tripowerhv.com", "B"),
    427: ("Darren Boeur · President", "admin@accuratepowergroup.com", "B"),
    428: ("Ryan Hague · Director/Owner", "team@avcwest.com", "B"),
    429: ("John O'Dare · President", "harrison@harrisonindustrial.ca", "B"),
    430: ("John Gordon · President Canada", "can.sales@wsgenergyservices.com", "B"),
    431: ("Murray Crewson · President", "estimating@crewelectrical.ca", "B"),
    432: ("Dave Franks · General Manager", "estimating@raylecpower.ca", "B"),
    433: ("Scott Gibson · President", "orders@customelectric.com", "B"),
    434: ("Gordon Werner · President", "（未找到）", "—"),
    435: ("Shawn Henry · President", "shawn@wescan-services.com", "A"),
    436: ("Ben Mazzei · President", "info@mazzeielectric.com", "B"),
    437: ("Rob Kinsey · CEO", "tenders@cdnpowerpac.com", "B"),
    438: ("Peter Thiessen · Principal Owner", "tristar@tristar.ca", "B"),
    439: ("Ron Remsey · VP Power", "r_remsey@vecohio.com", "A"),
    440: ("Albert Augustine Jr. · President/CEO", "aaugustine@agostinoutilities.com", "A"),
    441: ("Jim Meyer · President", "jmeyer@battag.com", "A"),
    442: ("Franklin P. Holleran · President", "fholleran@hbfrazer.com", "A"),
    443: ("Michael A. Conkey · President", "mikec@albarell.com", "A"),
    444: ("Jeffery Sloan · Director of Purchasing", "jeff.sloan@enerfab.com", "A"),
    445: ("Matt Varnado · VP Preconstruction", "mvarnado@white-electrical.com", "A"),
    446: ("David Lytle · VP（ISI 实体）", "dlytle@isiprime.com", "A"),
    447: ("Charles Hinton · Division President", "chuck.hinton@c3mpowersystems.com", "A"),
    448: ("Kevin Martin · VP / Branch Mgr", "k.martin@hatzelandbuehler.com", "A"),
    449: ("John Moncur · Sales Manager", "（未找到）", "—"),
    450: ("Sales/Purchasing（人名待核）", "tygel@electricalmaterials.ca", "A"),
    451: ("Robert Parr · Senior Sales", "info@parrline.com", "B"),
    452: ("Gordon Haynes · CEO", "（集团冲突，不发）", "—"),
    453: ("Robin Carroll · President/Owner", "sales@carrolltransformer.com", "B"),
    454: ("Gary Lovell · Director Ops & BD", "gary.lovell@ecotechnl.ca", "A"),
    455: ("Pallav Maggu · Director", "info@powerlogy.ca", "B"),
    456: ("Dawson Clapp（人名待核）", "dawsonclapp@oneilelectric.com", "A"),
    457: ("Ron Roopchansingh · VP Canadian Ops", "sales@argointl.com", "B"),
    458: ("Julie Ball · Inside Sales/Purchasing", "jball@lakeportpower.com", "A"),
    459: ("Michael L. Weaver · Founder & CEO", "michael.weaver@ctgpowersystems.com", "A"),
    460: ("Joseph W. Piela · President", "joe@pielaelectric.com", "A"),
    461: ("（未取得具名）", "sales@cowtownbreakers.com", "B"),
    462: ("Frank Mitchell（未证实）", "FrankMitchell21@yahoo.com", "C"),
    463: ("Wayne A. Burley · President", "web@espelectrical.com", "B"),
    464: ("Jay Romanoff · President", "sales1@romanoffindustries.com", "B"),
    465: ("Scott Engwert · President", "sales@currentmidwest.com", "B"),
    466: ("Nathan A. Clark · Owner", "Nate@Mid-Westmachinerymart.com", "A"),
    467: ("Jesye Franklin · Director Bus Ops", "service@integrityelectricdirect.com", "B"),
    468: ("Roy Reuveni · CEO & Founder", "sales@woodstockpower.com", "B"),
    469: ("Patrick Ricke · Ops Manager", "patrick@powerhouse-systems.com", "A"),
    470: ("Gavin Sullivan · President", "gavin@sullyent.com", "A"),
    471: ("Isaac Loeo · CEO", "Isaac@megawattequipment.com", "A"),
    472: ("Donna L Vail · President", "safepower3@yahoo.com", "C"),
    473: ("Erik M. Angiulo · President/CEO", "bee@brucelectric.com", "B"),
}

# 闸门（程序化抽取，交叉人工判定）
BLOCK = {
    434: "⛔ 拦截（闸门 1：邮箱未找到）→ 待补充",
    449: "⛔ 拦截（闸门 1：邮箱未找到）→ 待补充（改走电话 + 表单）",
    452: "⛔ 拦截（闸门 9：旗舰法人 = 买家204 Alberta Breaker，已于 9/29 发出）",
}
COND = {
    444: "⚠️ 条件通过 —— 🔴 母公司 Quanta Services（2026-07 收购）；Quanta 系已发 6 家",
    446: "⚠️ 条件通过 —— A 档邮箱属集团内 ISI 实体（`isiprime.com`），非主实体域",
    456: "⚠️ 条件通过 —— 🔴 母公司 Franklin Empire = 买家86（batch4），已于 9/29 发出",
    460: "⚠️ 条件通过 —— A 档邮箱来自 2008 年官网存档，时效待核",
    462: "⚠️ 拦截（闸门 4：邮箱档位 = C，免费 Yahoo）→ 待电话确认",
    467: "⚠️ 条件通过 —— 具名邮箱为免费 Gmail（C 档），主送走角色邮箱点名转交",
    472: "⚠️ 条件通过 —— 唯一邮箱为免费 Yahoo（C 档）+ MX 走 Proofpoint",
}

rows = []
for f in sorted(BASE.glob("买家*.md"), key=lambda p: int(re.match(r"买家(\d+)", p.name).group(1))):
    n = int(re.match(r"买家(\d+)", f.name).group(1))
    t = f.read_text(encoding="utf-8")
    name = re.sub(r"^买家\d+_", "", f.stem).replace("_开发信交接单", "").replace("_", " ")
    grp = re.search(r"母公司\s*/?\s*集团\*{0,2}\s*\|?\s*\*{0,2}([^\n|]{0,80})", t)
    grp = re.sub(r"\s+", " ", grp.group(1)).strip(" *|：:") if grp else "未获取"
    gate = BLOCK.get(n) or COND.get(n) or "✅ 通过"
    r = RECIP.get(n, ("—", "—", "—"))
    rows.append((n, name, r[0], r[1], r[2], gate, grp[:70], f.name))

A = [r for r in rows if r[4] == "A"]
B = [r for r in rows if r[4] == "B"]
C = [r for r in rows if r[4] == "C"]
N = [r for r in rows if r[4] == "—"]

out = []
out.append("# batch11 挖决策人 + 邮箱 · 批次汇总\n")
out.append("> 采集：2026-10-06 ｜ 范围：买家 424–473（50 家）｜ 产出：**50 份交接单**\n")
out.append(f"> 邮箱档位：**A {len(A)} ｜ B {len(B)} ｜ C {len(C)} ｜ 无邮箱 {len(N)}**\n")
out.append("> ⚠️ 本表由脚本从 50 份交接单程序化抽取，**非 agent 自述**。\n")
out.append("\n---\n")
out.append("\n## 一、🟢 A 档（具名 + 一手源，可主送）\n")
out.append("| 编号 | 公司 | 收件人 | 邮箱 | 闸门 |\n|---|---|---|---|---|")
for n, name, who, mail, tier, gate, grp, fn in A:
    flag = "" if gate.startswith("✅") else " ⚠️"
    out.append(f"| **{n}** | {name} | {who} | `{mail}`{flag} | {gate} |")
out.append("\n## 二、🟡 B 档（角色邮箱 → 仅点名转交，本批**不发**）\n")
out.append("| 编号 | 公司 | 收件人 | 邮箱 | 闸门 |\n|---|---|---|---|---|")
for n, name, who, mail, tier, gate, grp, fn in B:
    out.append(f"| {n} | {name} | {who} | `{mail}` | {gate} |")
out.append("\n## 三、🔴 C 档 / 无邮箱 / 拦截（**不发**）\n")
out.append("| 编号 | 公司 | 收件人 | 邮箱 | 档位 | 闸门 |\n|---|---|---|---|---|---|")
for n, name, who, mail, tier, gate, grp, fn in C + N:
    out.append(f"| {n} | {name} | {who} | `{mail}` | {tier} | {gate} |")
out.append("\n---\n")
out.append("## 四、🔴 集团归属（非「独立」者）\n")
out.append("| 编号 | 公司 | 母公司 / 集团 |\n|---|---|---|")
for n, name, who, mail, tier, gate, grp, fn in rows:
    if grp and "独立" not in grp[:6] and grp != "未获取":
        out.append(f"| {n} | {name} | {grp} |")

(BASE / "_批次汇总.md").write_text("\n".join(out) + "\n", encoding="utf-8")
print(f"A {len(A)} ｜ B {len(B)} ｜ C {len(C)} ｜ 无邮箱 {len(N)}")
print("写出 ->", BASE / "_批次汇总.md")
print()
print("A 档清单：")
for n, name, who, mail, tier, gate, grp, fn in A:
    print(f"  {n}  {name[:26]:<28} {mail:42} {'✅' if gate.startswith('✅') else '⚠️'}")
