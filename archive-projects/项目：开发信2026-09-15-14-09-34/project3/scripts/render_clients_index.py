# -*- coding: utf-8 -*-
"""从 recs.json 渲染 project3/clients/INDEX.md"""
import json, os
from collections import Counter, defaultdict

ROOT = r"C:\Users\win\WorkBuddy AI\项目：开发信2026-09-15-14-09-34"
recs = json.load(open(os.path.join(ROOT, ".workbuddy-ai", "tmp", "recs.json"), encoding="utf-8"))

L = []
w = L.append

w("# clients/ · 客户信件索引")
w("")
w("> ⚠️ **本文件是派生文件，不要在这里手改客户行。**")
w("> 数据来自 `开发信跟进表.md`（客户/买家类型/骨架/国家/状态）+ 各封信的批注（钩子/切片/开场）。")
w("> 改完源数据后重跑生成脚本即可刷新（脚本见文末 §五）。")
w("")
w("## 一、用途（写新信前先查这里）")
w("")
w("写一封新开发信时，**先在本表里找 1–2 家同类客户**，看当时用的是哪种钩子、")
w("切的是哪片段、开场引的是什么证据 —— 避免同一买家里用重复措辞，")
w("也避免重新发明已经验证过的角度。")
w("")
w("| 要查什么 | 看哪一列 |")
w("|---|---|")
w("| 这家是什么买家 | 买家类型 |")
w("| 同类买家上次用什么钩子 | 钩子 |")
w("| 落点收在哪段产品 | 产品切片 |")
w("| 开场引的是什么证据 | 开场角度 |")
w("| 信文件 | 文件 |")
w("")
w("> 🔴 **铁律提醒（`01` §三）**：钩子落点只落在**自己真有的产品**上。")
w("> 本表「产品切片」列记录的就是实际落点，可作同类的参考基线。")
w("")

# ---------- 统计 ----------
buyers = Counter(r["buyer"] for r in recs)
hooks = Counter(r["hook"] for r in recs)
slices = Counter(r["slice"] for r in recs)
explicit_n = sum(1 for r in recs if r["explicit"])

w("## 二、速查统计")
w("")
w("**买家类型分布**（共 %d 家）" % len(recs))
w("")
w("| 买家类型 | 家数 | 默认钩子（`01` §三）|")
w("|---|---|---|")
DEFAULT_BY_BUYER = {
    "承包商": "工厂测试数据 / 规格书（按电压切片）",
    "分销商": "价格阶梯 + MOQ + 交期",
    "合作社": "价格阶梯 + MOQ + 交期",
    "渠道": "价格阶梯 + MOQ + 交期",
    "EPC": "报审 submittals",
    "服务商": "工厂测试数据",
    "OEM": "OEM 产能补位",
    "咨询": "（试探函）",
}
for b, n in buyers.most_common():
    w("| %s | %d | %s |" % (b, n, DEFAULT_BY_BUYER.get(b, "—")))
w("")
w("**钩子实际使用分布**")
w("")
w("| 钩子 | 家数 | 备注 |")
w("|---|---|---|")
NOTE = {
    "工厂测试数据+规格书": "承包商默认（多数信未显式标注，按买家类型归类）",
    "价格阶梯+MOQ+交期": "分销商/合作社/渠道默认",
    "报审 submittals": "design-build 有选型权的客户",
    "测试报告样本": "信件中显式记载",
    "文档备档 for bids": "投标驱动总包（Williams）",
    "PSC 品类直引": "联邦承包商（ALB，最锋利钩子）",
    "工厂测试数据": "调试/测试专家（TPS）",
    "规格书（分电压）": "早期信件显式记载（BG / Ontario）",
}
for h, n in hooks.most_common():
    w("| %s | %d | %s |" % (h, n, NOTE.get(h, "")))
w("")
w("> 其中 **%d 家**信件批注里有显式钩子记载，其余按买家类型归入默认钩子类。" % explicit_n)
w("")

# ---------- 主索引 ----------
w("## 三、索引表（%d 家）" % len(recs))
w("")
w("按买家类型分组，同组内按跟进表序号排列。")
w("")

ORDER = ["承包商", "分销商", "合作社", "渠道", "EPC", "服务商", "OEM", "咨询"]
groups = defaultdict(list)
for r in recs:
    groups[r["buyer"]].append(r)

for b in ORDER:
    if b not in groups:
        continue
    gl = groups[b]
    w("### %s（%d 家）" % (b, len(gl)))
    w("")
    w("| # | 客户 | 国家/州 | 骨架 | 钩子 | 产品切片 | 开场角度 | 文件 |")
    w("|---|---|---|---|---|---|---|---|")
    for r in sorted(gl, key=lambda x: x["num"]):
        fl = r["file"] if r["file"] else "（电话店，无信文件）"
        w("| %d | %s | %s | %s | %s | %s | %s | %s |" % (
            r["num"], r["name"], r["country"], r["skel"],
            r["hook"], r["slice"], r["opening"], fl))
    w("")

# ---------- 使用规程 ----------
w("## 四、使用规程")
w("")
w("### 写新信前（3 步）")
w("")
w("1. **定买家类型** → 在本表 §二 找到该类默认钩子。")
w("2. **查同组已有信** → 看「钩子」「开场角度」两列，**不要重复用同一措辞**。")
w("   同类文档钩子要换行话：`for your bids`（投标）/ `for your submittals`（报审）/")
w("   `test report samples`（联邦项目文件）。")
w("3. **定产品切片** → 参考同组「产品切片」列，再按对方电压等级收窄")
w("   （15kV 配电级客户**刻意不提 500kV**；输电/变电站级才谈高压电力变）。")
w("")
w("### 写完后（2 项同步）")
w("")
w("- 把新客户追加到 `开发信跟进表.md`（**主数据在这里**）。")
w("- 在本表 §三 对应分组里能看到新行 → 重跑生成脚本即可，**不要手改**。")
w("")
w("### ⛔ 不要做的事")
w("")
w("- ❌ 直接在 INDEX 里手改/新增客户行（会被下次重跑覆盖）。")
w("- ❌ 把「产品切片」当成对某客户的产品范围承诺（它只记录**首封实际落点**）。")
w("")
w("## 五、生成脚本")
w("")
w("脚本在 `project3/scripts/`（两条命令，按顺序跑）：")
w("")
w("```")
w("python project3/scripts/gen_clients_index.py     # 解析源 → recs.json")
w("python project3/scripts/render_clients_index.py  # 渲染 → 本文件")
w("```")
w("")
w("脚本逻辑：客户名/买家类型/骨架/国家 ← 跟进表；")
w("钩子（显式批注优先，否则按买家类型兜底）/ 产品切片（「落点」记载优先，")
w("否则从正文产品词反推）/ 开场角度 ← 各封信。")
w("")
w("**何时重跑**：")
w("")
w("- 新增客户信件后（跟进表追加 + `clients/` 放信）")
w("- 改了某封信的「钩子」或「落点」批注后")
w("- 改了 `01` §三 钩子表里买家类型与钩子的对应关系后")
w("")

out = os.path.join(ROOT, "project3", "clients", "INDEX.md")
open(out, "w", encoding="utf-8").write("\n".join(L))
print("written:", out)
print("lines:", len(L))
