# 待移交 · 项目2（找客户） · canada-b2b-prospecting

> **这是一个自包含的完整技能结构，可直接搬到「找客户」项目使用。**
> 归档自本项目分层改造（2026-09-23）时清理出的 opencode 残留技能。

---

## 这是什么

**加拿大 B2B 背调 5 步法** —— 目标：找到**公司 + 公开商务联系方式**。

⚠️ **它属于「找客户/背调」职责（项目2），不是本项目（写信）的。**
本项目保留它，只为**待移交**。

---

## 怎么移交（三选一）

### 方案 A · 并入项目2 主力技能（推荐）

项目2 的主力技能是 `b2b-buyer-research`（`~/.workbuddy-ai/skills/b2b-buyer-research/`），
**已覆盖加拿大**（注册库 / 商会 / 协会 / 黄页 / 掩码邮箱交叉验证）。

→ **把下面 3 处独有入口补进 `references/02-sources.md`，然后本技能可删**：

| 补充内容 | 写进哪 |
|---|---|
| **CATB** `catb.on.ca/members/...`（拿 Email/Phone/Fax/Services/Division）<br>**MineConnect** `mineconnect.com/corporate-members/...`（矿业供应链）<br>**ECAO / Ontario Electrical League**（电力） | `references/02-sources.md` §行业工会/联盟/协会名录 |
| **Thunder Bay Chamber** `business.tbchamber.ca/list/member/...` | `references/02-sources.md` §美国商业名录（可扩为"北美"）|
| **加拿大区号表**（807=安省西北 / 416,647=多伦多 / 604=BC） | `references/03-traps.md` 或 `02-sources.md` |

> 🔴 **注意**：`b2b-buyer-research` 有**维护护栏**（SKILL.md 顶部明确写）：
> **禁止向其 SKILL.md 追加渠道 URL** —— 渠道必须进 `references/02-sources.md`。
> 搬运时务必遵守。

### 方案 B · 注册为独立用户级技能

整个目录复制到：`C:\Users\win\.workbuddy-ai\skills\canada-b2b-prospecting\`
（`SKILL.md` 已含合法 frontmatter，`name` / `description` 齐全，可直接被识别）

⚠️ 缺点：与 `b2b-buyer-research` 职责重叠，未来容易漂移。

### 方案 C · 放项目2 的 `.opencode/skills/`

原位置就是这种形态（`.opencode/skills/canada-b2b-prospecting/`）。
若项目2 仍用 opencode 工具链，可直接搬回。

---

## 内容摘要（5 步法）

| Step | 做什么 |
|---|---|
| **1 · 确认主体** | 输入可能只有截图/名字/LinkedIn 头衔 → websearch 确认官网域名、LinkedIn 公司页、地址一致性；记录 `/contact` 页总机与 info 邮箱 |
| **2 · 政府注册验真** | Corporations Canada（`ised-isde.canada.ca/cc/lgcy/fdrlCrprSrch.html`）查联邦公司名+董事；Ontario Business Registry 查省注册号+officer+地址 |
| **3 · 商会查负责人直连**（优先级最高）| 商会名录是企业自己为接单提交的 → Thunder Bay Chamber / OCC `occ.ca` / `chamber.ca` / Toronto Region Board of Trade `bot.com` |
| **4 · 行业协会查直邮** | CATB / MineConnect / ECAO / CCA。**实例**：GRID LINK CORP. 页登记 `jbernst@gridlink.ca / 807-683-0350 / 1499 Rosslyn Road` |
| **5 · 黄页补全+交叉验证** | YellowPages.ca / Canada411 / 411.ca / BBB / Google Maps；**掩码邮箱（`j***@gridlink.ca`）必须与 Step 3/4 明文交叉** |

**Output**：三段中文（① 人物 ② 所在公司 ③ 联系方式，**每个来源必注明**）+ 触达建议。

**Rules**：先官网→商会协会→黄页；掩码邮箱必须交叉；区号表；**不确定就写"未找到公开信息"，不编邮箱电话**。

---

## 与 `b2b-buyer-research` 的关系（重要）

| 项 | b2b-buyer-research（项目2 主力）| 本技能 |
|---|---|---|
| 加拿大注册库 | ✅ 有（用 **opengovca.com**，免登录，比本技能更实用）| ✅ 有（用 ised-isde）|
| 商会 | ✅ 有（无加拿大具体 URL）| ✅ **有具体路径** ← 独有 |
| 行业协会 | ✅ 有（无加拿大协会）| ✅ **CATB/MineConnect/ECAO** ← 独有 |
| 黄页 | ✅ 有（Yahoo/Yelp/BBB/Manta）| ✅ YellowPages.ca 等 ← 独有 |
| 掩码邮箱交叉 | ✅ 铁律 #2/#3 | ✅ 同 |
| 买家类型判定 / 停业判定 / 海关 / SAM.gov | ✅ 有（**本技能完全没有**）| ❌ |

**结论**：本技能 = `b2b-buyer-research` 的一个**加拿大地区补充包**，
不是竞争关系。**建议按方案 A 合并**。

---

*状态：待移交。移交后本目录可从 project3 删除。*
