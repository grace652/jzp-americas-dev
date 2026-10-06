# 【买家 137】开发信交接单 — RIES Equipment & Utility Distribution（RIES Utility Supply）

> 采集日期：2026-09-28 ｜ 名单来源：`线索资产/目标客户清单.csv` 序号 47（**B 类 · 分销商/贸易商**）
> 采集方：找客户环节（本环节只产出交接单，不写正文/不碰模板/不定话术）
> ⚠️ 本表严格区分「已验证」与「未获取」，未找到的信息一律标注，**不做推断填充**（H1）
> ✅ 一句话结论：**安大略 Cobourg 的公用事业器材分销商（B 类，非制造商）**，
> 官网自述 "one of Ontario's largest inventory of new, re-manufactured and reconditioned transformers"，
> 且**明确经营 station style transformers 1MVA–50MVA / 一次电压至 138kV**（高压品类需求真实存在）；
> **实际控制人 Shane Weatherby（NuVolt Group CEO/Founder）已锁定，`shane@riesequipment.ca` 为官网第一方来源（A 档）**；
> 🔴 **但集团已绑定变压器制造伙伴（Kodion Energy，美国），存在采购渠道锁定风险**。

---

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示(如有)
RIES Equipment & Utility Distribution | Shane Weatherby | CEO / Founder (NuVolt Group) | shane@riesequipment.ca | ✅ 已验证（A 档 · 官网第一方 + 电话交叉一致）| ca.linkedin.com/in/shane-weatherby-292ba953（摘要可见，未直接抓取）| 安大略公用事业器材分销/代理商，位于多伦多以东 1 小时（Cobourg）；自有变压器库存（new/re-manufactured/reconditioned，一年保修）；产品含配电变压器（至 2500kVA）、电力变压器（1MVA–50MVA / 至 138kV）、变压器租赁、Corflo 管路、Transformer Sac；同时代理 Ilpea Industries 与 Milwaukee 工具；预拥有吊车/挖掘/林业车等车队业务 | 官网实抓（首页/about-us/contact/distribution-transformers/power-transformers）+ NuVolt 集团官网（Shane/Stacy 名录页）+ SMTP 探测 + DNS/SPF/DMARC | 🔴 集团含变压器制造伙伴（Kodion Energy）；🔴 官网 smtp 为 catch-all 不可探测
```

**发信资格：⚠️ 有条件通过**（九条闸门：**人明确、邮箱有第一方来源**；缺口在"⓪ 反身排除"需带风险标注）
**邮箱档位：A（具名联系人 · 官网第一方来源 · 非猜测）**

---

## 二、补充信息（扩展段）

### 标准字段明细

| 项 | 内容 | 来源 |
|---|---|---|
| **公司全称** | **RIES Equipment & Utility Distribution**（官网标题 *"RIES:Contact"* 页题 *"RIES Equipment & Utility Distribution"*；about 页另用 *"RIES Equipment Solutions & Utility Distribution"*；变压器业务对外称 **RIES Utility Supply**）| 官网（一手，三处称谓并存）|
| **国家 + 城市** | **加拿大 ON 省 Cobourg（科堡）**，官网自述 *"located just one hour east of Toronto"* | 官网 about-us（一手）|
| **州省** | **ON ✅**（CSV 填 ON，**正确**）| 官网 |
| **详细地址** | **90 Princess Street, Cobourg, Ontario K9A 5T2** | 官网 Contact 页（一手）|
| **电话** | **P 905 396 5964** ／ **F 905 372 2633** | 官网 Contact 页（一手）|
| **注册信息** | ⚠️ **未获取**（ON Registry 查询需交互，公开搜索未产出；**不做断言**）| — |
| **成立年份** | ⚠️ **未获取**（官网未标注；about 页无年份）| — |
| **域名** | riesequipment.ca（🔴 **CATCH-ALL，SMTP 探测无效**）| 探测确认 |
| **邮件网关** | **Barracuda ESS**（`d354414a/…b.ess.barracudanetworks.com`）| DNS MX |
| **SPF** | `v=spf1 a mx a:relay.eagle.ca ~all`（**~all 软失败**，策略偏松）| DNS TXT |
| **DMARC** | `v=DMARC1; p=quarantine; pct=100;`（⚠️ 中等严格，无报告地址 rua）| DNS TXT |
| **规模** | ⚠️ 员工数未获取。官网自述库存为 *"one of Ontario's largest"*（自述，**非第三方核验**）| 官网 |
| **官网** | https://riesequipment.ca | — |

### 🔴 第一发现：这是真·高压需求方，不只是普通分销商

官网 **Power Transformers 页原文**（一手，逐字）：

> *"RIES Utility Supply also supplies **station style transformers from 1MVA through 50MVA in primary voltages to 138KV**. We can offer a **turnkey solution for your station needs** offering new, re-manufactured and reconditioned materials. Financing options like leasing and lease to own are also available."*

官网 **Distribution Transformers 页原文**（一手，逐字）：

> *"Single-phase and three-phase pole mount and pad mount, oil filled and dry type **up to 2500KVA**. We can provide new units to your specifications for options and loss values in mild steel and stainless steel."*
> *"Polemount … HV **34.5 KV**; LV 8.0 kV; **200kV BIL**."*
> *"Padmount … Ranges from **75 to 5000 KVA**."*
> *"Vault Type … Single phase range from 50 KVA to 750 KVA. Three phase range from **150 KVA to 3000 KVA**."*

🔴 **业务含义（供写信环节自行判断，本环节不定话术）**：
- 该司**明码标价地做 138kV / 50MVA 级站用变压器**（E541626 适用区间），**不是只做 45–5,000kVA 配电级**。
- ⛔ **但这不等于他们自行采购**：官网通篇为 *"we supply / we can provide"*（**供方口吻**），
  且 *"re-manufactured and reconditioned"* 说明相当比例货源来自**翻新/改造**而非全新整机采购。
  **⇒ 不得据此认定其为稳定新机采购方**（H1）。

### 联系人（含 still_here 在职核验）

| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| **Shane Weatherby** | **实际控制人（首封主送）** | **官网 NuVolt 名录页原句：*"Shane Weatherby … CEO / Founder"***；LinkedIn 摘要：*"President / CEO at NuVolt Group of Companies"* | ⚠️ 20 年（自述：*"spent the last 20 years building and growing utility businesses"*）| **高**：NuVolt 官网名录页在列，RIES 官网 Contact 页直接署名 | 低（**所有者级**）| ca.linkedin.com/in/shane-weatherby-292ba953（**仅摘要可见，未直接抓取**）|
| **Stacy Weatherby** | **President, Utility Products（产品线对口，备选）** | 官网 NuVolt 名录页原句：*"Stacy Weatherby … President, Utility Products"* | 15 年（自述）| **高**：NuVolt 官网名录页在列 | ⚠️ 未知 | ⚠️ 未获取 |
| （RIES 联系页具名联系人）| 对外接待/商务 | **官网 Contact 页仅列 *"Shane Weatherby"* 一人 + 电话 + 邮箱**（无职称字样）| — | — | — | — |

> 🔴 **机读结论 —— 归属关系已确证（证据链三重交叉）：**
>
> | 证据 | 内容 | 强度 |
> |---|---|---|
> | ① **电话一致** | RIES Contact 页 `P 905 396 5964` = NuVolt 官网 Shane 页 `Phone Number (905) 396-5964` **逐位相同** | 🔴 强 |
> | ② **邮箱同域** | RIES 官网唯一实名邮箱 `shane@riesequipment.ca`；NuVolt 官网 `shane@nuvoltgrp.com` —— **同一人、两域双属** | 🔴 强 |
> | ③ **MX 同构** | RIES 与 **CDF Utility Supply（NuVolt 体系另一公司）** 同为 **Barracuda ESS** 网关（`d354414a/b…` vs `d337817a/b…`）| 🟡 中（同族但非同一网关）|
>
> **⇒ 判定：RIES 属于 Shane Weatherby 旗下（NuVolt Group Canada）体系**，与 CDF Utility Supply
> 属同一控制人。**Shane 是 RIES 的实际控制人，可作首封主送对象。**
>
> ⚠️ **注意**：**RIES 官网 About 页通篇未提 NuVolt**（对外为独立品牌，`riesequipment.ca` 为独立域）。
> ⛔ **正文中不得以"贵司隶属于 NuVolt 集团"起头** —— 集团关联未在 RIES 侧公开声明，
> 直接点名可能造成对方不适或显得越界。**建议只谈 RIES 侧的公开业务**。

### 🔴⓪ 反身排除（六层过筛第 0 层）— 本单最关键判断

| 检查项 | 结论 | 依据 |
|---|---|---|
| 是否为**制造商/竞对**？ | ❌ **不是**。RIES 是分销商/代理商（agent of Ilpea Industries；Milwaukee 工具分销；自有与三方货源混售）| 官网首页（一手）|
| 是否为他方**代理**？ | ⚠️ **是，但代理的是非变压器品类**（Ilpea Industries 的 PVC U-Guard / Corflo 管路；Milwaukee 工具）→ **不构成同业排斥** | 官网首页（一手）|
| **集团是否存在变压器制造绑定？** | 🔴 **存在**。NuVolt 集团官网原文：*"**Kodion Energy**, NuVolt Group's **transformer manufacturing partner**, has officially broken ground on a new state-of-the-art facility in **Paola, Kansas**."* | NuVolt 官网（一手，逐字）|
| Kodion Energy 性质 | 美国堪萨斯州 Paola 的变压器制造商（2021 年落地；AI-powered transformer 方向；与 **美国能源部（DOE）** 有军事基地变压器安装合同）| 公开报道（KMEA / KOFO Radio，非官网）|

> 🔴 **判断（本环节只做事实与风险标注）**：
> - **RIES 本身不是制造商，也不是竞对**，按 ⓪ 层**不排除**。
> - **但集团层面已与 Kodion Energy 建立变压器制造伙伴关系** —— 这意味着集团内的变压器采购
>   通道**大概率优先走 Kodion**。RIES 作为集团内的分销窗口，采购决策**可能受集团层面约束**。
> - ⚠️ **Kodion 资质未核实**：公开报道仅称其在 Paola 建厂、做 AI 变压器、有 DOE 军事基地合同；
>   **未见其 UL / CSA 认证信息，也未见其电压等级上限**。**不得推断 Kodion 覆盖 138kV 级** ——
>   若 Kodion 只覆盖中低压配电级，则 RIES 的 1MVA–50MVA/138kV 段**仍可能外采**。
> - **⇒ 结论：可开发，但必须带"集团采购绑定"风险标注；建议以"补位/扩容/交期"角度切入而非正面替代。**
>   （**具体怎么写属写信环节职责，本环节不代拟。**）

### 邮箱分档（A/B/C）

| 档 | 地址 | 依据 | 可否主送 |
|---|---|---|---|
| **A** | **`shane@riesequipment.ca`** | ① **官网 Contact 页明文列出**（一手，逐字 `E shane@riesequipment.ca`）<br>② **电话与 NuVolt 官网 Shane 页逐位一致**（交叉佐证为同一人） | ✅ **主送** |
| A（集团口径备选）| `shane@nuvoltgrp.com` | **NuVolt 官网 Shane 个人页明文列出**（一手）| ⚠️ 备选，**不与主送同发** |
| A（产品线对口）| `stacy@nuvoltgrp.com` | **NuVolt 官网 Stacy 个人页明文列出**（一手）；职务 *President, Utility Products*（**变压器产品线对口**）| ⚠️ **第二轮备选**（首封建议走 Shane，Stacy 作 follow-up）|
| B | ⚠️ **未发现** `info@` / `sales@` 等角色邮箱 | 官网 Contact 页**只有实名邮箱**，无角色邮箱 | — |
| C | — | 无 | — |

**🔴 邮箱验证方法与证据链（可复现）：**

```
域名 riesequipment.ca
MX   = d354414a.ess.barracudanetworks.com / d354414b.ess.barracudanetworks.com  （Barracuda ESS 网关）
SPF  = v=spf1 a mx a:relay.eagle.ca ~all        （~all 软失败）
DMARC= v=DMARC1; p=quarantine; pct=100;         （中等严格）

SMTP RCPT 探测（对照组协议）：
  250  info@riesequipment.ca                        ← 未列出，但存在
  250  zzz_nonexistent_probe_9987@riesequipment.ca  ← 🔴 随机地址也 250 ⇒ CATCH-ALL，本轮探测作废
  250  shane@riesequipment.ca
  250  sweatherby@riesequipment.ca                  ← 同样 250，但无法区分真假
⇒ 🔴 判定：该域为 CATCH-ALL，SMTP 探测【对验证人名邮箱无效】。
   ⇒ shane@ 的可信度【不依赖 SMTP】，而依赖【官网第一方明文列出】，已达 A 档标准（H5：≥1 第一方来源）。
```

> ⚠️ **catch-all 的连带影响（发送阶段必须知悉）**：
> 该域**对任何收件人地址都回 250** ⇒ **退信（bounce）是本单唯一的真实性反馈渠道**。
> `sweatherby@riesequipment.ca` 之类的**推断格式不可使用**（H2：不得臆造邮箱；
> 且 catch-all 域无法用 SMTP 证伪，风险更高）。

---

## 三、开发信建议（**仅限：收件人 / 时机 / 附件 —— 不含正文、不含主题行、不含开场句**）

> 依分工铁律：**措辞/钩子/产品切片/主题行全部归环节 ②（写开发信 agent）**。本节只给**收件人与时机**层面的建议。

| 项 | 建议 | 依据 |
|---|---|---|
| **主送** | `shane@riesequipment.ca`（Shane Weatherby）| 所有者级，决策链最短 |
| **抄送** | ⛔ **首封不建议抄送**（避免触发内部转发或招致"乱发"印象）| — |
| **Follow-up 对象**（第二轮及以后）| `stacy@nuvoltgrp.com`（Stacy Weatherby，President, Utility Products）| **变压器产品线对口**，首封无回应时可换线 |
| **建议时机** | **美东工作日 09:00–11:00**（Cobourg = America/Toronto 时区）| 分销商通常上午处理询价 |
| **建议附件** | ① UL 证书 **E541626**（三相液浸电力变压器 750–110,000 kVA / 72–121 kV）—— **对应其官网自述的 1MVA–50MVA / 至 138kV 段**<br>② UL 证书 **E541627**（三相配电/座装 45–5,000 kVA）—— 对应其配电段<br>③ 公司介绍（中英）| 附件选择属写信环节可调用素材；**本环节只提示"该公司涉足两类电压段，故两类证书都可备"** |
| **切入角度提示**（**仅提示，不代拟文案**）| 对方是**分销商 + 翻新/改造商**，且官网强调 *"cost effective and lead-time sensitive"* —— **交期与成本敏感度高于技术指标** | 官网 distribution-transformers 页（一手）|
| ⛔ **禁止事项** | ① 不得提"贵司隶属 NuVolt 集团"（未在 RIES 侧公开）<br>② 不得提 Kodion Energy（对方制造伙伴，属敏感）<br>③ 不得假设其自行采购（其为供方口吻，大量货源为翻新）| 见上 §二 |

---

## 四、合规自查（H1–H7）

| 规则 | 自查结果 |
|---|---|
| **H1 不虚构** | ✅ 全部字段标注来源；未获取项（成立年份、注册信息、员工数）**留白并标注**；未从 "station style transformers" 推断其自行采购 |
| **H2 不臆造邮箱** | ✅ 只用官网明列地址；`sweatherby@` 类推断格式**已明确禁用**；catch-all 域已标注无法证伪 |
| **H3 格式校验 + ≥1 交叉来源** | ✅ 邮箱格式合法；`shane@riesequipment.ca` 有 **官网第一方明文 + 电话与集团官网逐位一致** 双重来源 |
| **H4 标注验证状态** | ✅ A 档标注为"官网第一方来源（非 SMTP 验证，因域为 catch-all）"，**未混称"SMTP 已验证"** |
| **H5 交叉验证需 ≥1 第一方** | ✅ 第一方 = RIES 官网 Contact 页 与 NuVolt 官网个人页 |
| **H6 角色邮箱不得单独交付** | ✅ 本单无角色邮箱；B 档为空 |
| **H7 落盘 .md** | ✅ 本文件 |

---

## 五、给下一环节的交付说明

**可直接使用的成果：**
1. 主送人 **Shane Weatherby** + 邮箱 **`shane@riesequipment.ca`**（官网第一方，A 档）
2. **公司公开业务事实**：安大略 Cobourg 分销商；变压器 new/re-manufactured/reconditioned；
   **配电至 2500kVA / 5000kVA**、**电力 1MVA–50MVA / 至 138kV**；一年保修；租赁与租购金融方案
3. **两类电压段均有需求** ⇒ 附件可同时备 E541626 与 E541627

**必须知悉的风险：**
1. 🔴 **集团采购绑定**：NuVolt 与 Kodion Energy（美国变压器制造商）为合作伙伴 ⇒ 采购通道可能被占
2. 🔴 **域为 catch-all** ⇒ 发送阶段**只能靠退信判断可达性**，无法预验证
3. ⚠️ ⛔ **不得提及 NuVolt 隶属关系、不得提及 Kodion**

**本环节未做（属其他环节职责）：**
- 未写正文、主题行、开场句、钩子、产品切片（→ 环节 ② 写开发信 agent）
- 未定最终发送时间与时区窗口排程（→ 环节 ③/④ 脚本）
