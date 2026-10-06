# 【买家 149】开发信交接单 — Shermco Industries, Inc.（美国总部 TX · 加拿大温尼伯服务点）

> 采集日期：2026-09-28 ｜ 名单来源：`线索资产/目标客户清单.csv` 序号 15（A 类 · 电气承包商/工程公司）
> ⚠️ **实体澄清**：CSV 填「Shermco Industries **Canada** Inc. · MB」，但**主体是美国公司**（总部德州 Irving）；
> MB 指向其**温尼伯服务点**。**主送用美国域名 `shermco.com`**（加拿大站 `shermco.ca` 未检出可用邮箱）。
> 采集方：找客户环节（本环节只产出交接单，不写正文/不碰模板/不定话术）
> ⚠️ 本表严格区分「已验证」与「未获取」，未找到的信息一律标注，**不做推断填充**（H1）
> ✅ 一句话结论：**北美最大 NETA 认证电气测试机构**（美国德州 Irving 总部，1974 年 Pete Sherman 创立，50+ 年）；
> **41 服务中心 / 700+ NETA 技师 / 230+ 工程师**；加拿大温尼伯设服务点（1375 Church Ave）；
> ⭐ **CEO 具名邮箱 `phil.petrocelli@shermco.com` 已通过多格式命名规则探测实证** ——
> 本批**唯一取得 C 级高管直接邮箱**的目标；
> ⓪ 反身排除判定：**电气测试/维护服务平台，非制造商 ⇒ 通过**；
> 🔴 **但须注意**：其业务为「**测试服务**」而非「采购」⇒ **需求匹配度偏低**（见 §二 评估）。

---

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示(如有)
Shermco Industries, Inc. | Phil Petrocelli | CEO | phil.petrocelli@shermco.com | ✅ SMTP 多格式探测实证（250；同域 phil@/petrocelli@/同姓无点均 550）| ⛔ 未定位 | 北美最大且增长最快的电气测试机构（NETA 认可），1974 年成立，总部美国德州 Irving；41 个服务中心（美加）；700+ NETA 技术人员、230+ 工程师；业务覆盖现场服务、电力系统工程、控制系统集成、灾难恢复、电机与发电机维修、断路器翻新、培训 | 官网 Leadership 页（一手）+ DNS/MX + SMTP 控制地址协议与多格式命名规则探测 | ⚠️ 官网未明列变压器采购；体量大、决策链可能长
```

**发信资格：✅ 通过**（C 级高管姓名 + 职位 + 具名邮箱均一手/实证）
**邮箱档位：A（具名高管个人邮箱，SMTP 多格式探测实证通过）**

---

## 二、补充信息（扩展段）

### 标准字段明细

| 项 | 内容 | 来源 |
|---|---|---|
| **公司全称** | **Shermco Industries, Inc.** | 官网（一手）|
| **国家 + 城市** | **美国 TX 州 Irving（达拉斯都会区）** | 官网 Contact 页（一手）|
| **州省** | **TX ✅**（CSV 填 TX，**正确**）| — |
| **详细地址** | ⚠️ **两个地址口径不一**：<br>① 官网 contact-shermco：**511 E John W Carpenter Fwy #700, Irving, TX 75062**<br>② 第三方（allbiz）：2425 E Pioneer Dr, Irving, TX 75061 | 官网（一手）+ 三方 |
| **电话** | **888-743-7626**（= 888-SHERMCO，24/7 应急）；本地 972-793-5523 | 官网（一手）|
| **邮箱** | **`phil.petrocelli@shermco.com`**（CEO）；`info@shermco.com`（总）| 官网 + SMTP 实证 |
| **域名** | shermco.com | — |
| **邮件网关** | **Microsoft Exchange Online + Trend Micro（`mailsecurity.in.tmes.trendmicro.com`）双层** | DNS MX |
| **SPF** | ⚠️ **未在 TXT 中检出标准 `v=spf1` 记录**（DNS TXT 返回多条：`contractworksverify`、dropbox 验证等）—— **异常，发送环节需注意** | DNS TXT |
| **DMARC** | 🔴 **`v=DMARC1; p=reject;`** —— **最严格策略**（拒收未通过 DMARC 的邮件）| DNS TXT |
| **成立年份** | **1974**（官网 *"Trusted since 1974"*；官网另称 *"In 1974, **Pete Sherman** founded Shermco"*、*"50+ Years of Experience"*）| 官网（一手）|
| **规模** | **41 个服务中心 / 700+ NETA 技术人员 / 230+ 工程师**（另 100+ 资质 P&C 工程师）| 官网（一手）|
| **官网** | https://shermco.com ／ 加拿大站 https://shermco.ca | — |

### 🇨🇦 加拿大侧信息（因 CSV 序号 15 标注为「Shermco Industries **Canada** Inc. · MB」）

> ⚠️ **实体说明**：Shermco 是**美国公司**（总部德州 Irving），加拿大为其**服务网络的一部分**。
> CSV 指向的 MB 省，实为**温尼伯服务点**。

| 项 | 内容 | 来源 |
|---|---|---|
| **加拿大侧品牌** | *"Shermco Canada"*（站点 `shermco.ca`）| 官网（一手）|
| **温尼伯服务点地址** | **1375 Church Avenue, Winnipeg, Manitoba R2X 2T7**（🟢 官网明文，**第一方**）| 官网 shermco.ca（一手）|
| **温尼伯电话** | **204.925.4022**（🟢 官网明文）| 官网 shermco.ca（一手）|
| **加拿大侧背书** | 官网自述 *"North America's largest and fastest-growing electrical testing organization accredited by NETA"* | 官网（一手）|
| **🔎 招聘线索** | LinkedIn 有 **"Sr Transformer Technician (Field Based)"** 招聘帖<br>（📍 **Winnipeg area, Manitoba**，2026-07）<br>⇒ 说明**温尼伯点设有变压器技术团队** —— ⚠️ 但**是技术岗，非采购岗** | LinkedIn 招聘帖（第三方）|

> ⚠️ **注意**：本单主送用**美国总部域名 `shermco.com`**（`phil.petrocelli@shermco.com`），
> **不用** `shermco.ca` —— 后者是加拿大展示站，**未检出可用邮箱**。

### 业务定位（官网一手，逐字）

> *"Shermco is **North America's largest and fastest-growing electrical testing organization**
> accredited by the **InterNational Electrical Testing Association**. Trusted since **1974**,
> Shermco has you covered when it comes to **electrical testing, maintenance**, and industry requirements."*

> *"**Shermco is an Electrical Services Platform.** We specialize in technically differentiated
> **Field, Shop, and Engineering & Control (E&C) services**. Our goal is simple: make our clients safer"*

服务清单：*Field Services / Power Systems Engineering / Control Systems Integration /
Disaster Recovery Services / Motor & Generator Repair Services / **Breaker Refurbishment** / Training*

行业覆盖：*Data Center / Utilities / Semiconductor / Oil, Gas, & Chemical / Manufacturing / Renewables*

⚠️ **官网未明列变压器采购** —— 属电气测试机构常规画像，**触点属行业推断**。

### ⓪ 反身排除判定（本环节强制首层）

| 检查项 | 结论 |
|---|---|
| 官网是否自称 manufacture / 制造 | ❌ **无**（自称 *"Electrical Services Platform"*）|
| 是否有自有产品规格书（kVA/kV 参数表） | ❌ 无 |
| 是否销售自有品牌变压器 | ❌ 无（但有 **Breaker Refurbishment** 断路器翻新服务，**属翻新非制造**）|
| 定性 | ✅ **电气测试 / 维护 / 工程服务平台 ⇒ 非同业制造商 ⇒ 通过 ⓪ 层** |

> 📌 注意：**「Breaker Refurbishment」（断路器翻新）** 与 **「Motor & Generator Repair」（电机与发电机维修）**
> 均为**服务**，不等于制造。**不得据此认为其制造变压器。**
> ⚠️ 第三方库（ContactOut）将其归类为 *"Appliances, Electrical, and Electronics **Manufacturing**"* ——
> **属分类库误标，官网无任何制造证据，不予采信。**

#### 🔴 补充复核：官网 "Manufacturing Services" 页名易误判（必须澄清）

⚠️ **风险点**：Shermco 官网有 *"**Manufacturing Services**"* 页面，**标题极易被误判为「制造变压器」**。
已逐字核实 ⇒ **结论：不是制造，是「服务制造业客户」**：

> 页面原文（官网，一手，逐字）：
> *"Power your facility's future with **manufacturing solutions** designed to elevate reliability, resilience, and performance."*
> *"Shermco delivers comprehensive electrical lifecycle services that help **manufacturers** improve reliability,
> reduce downtime, and keep critical operations running."*
> *"Our teams have decades of experience **supporting critical manufacturing environments**, including pulp and paper,
> food and beverage, metals, mining, and transportation facilities…"*

**⇒ 「Manufacturing Services」= 面向制造业客户的服务产品线**（提供测试/维护/工程），
**不是 Shermco 自己制造设备**。

**其变压器相关业务（官网 field-services / manufacturing-services 页，一手，逐字）**：
> - *"**Transformer Repair and Testing**"*
> - *"**Oil Processing for Transformers** and Breakers"*
> - *"**Transformer Testing & Diagnostics**"*、*"**Substation Inspection & Maintenance**"*

#### 🔴 需求匹配度评估（本单核心风险，须如实标注）

⚠️ **Shermco 的业务本质是「为客户提供测试/维修服务」，而非「为自身采购变压器」**。

| 维度 | 评估 |
|---|---|
| **是否会自行采购变压器？** | ⚠️ **可能性低** —— 它是**服务方**，变压器属**客户资产**（客户送来测试/维修）|
| **是否有采购影响力？** | ⚠️ **间接**：其为客户提供 *"Electrical System Assessments & Modernization Planning"*，<br>可能在**客户设备更新时提供选型建议** → **有间接影响力，但非决策方** |
| **是否有其他匹配点？** | ⚠️ **有一处**：官网列 *"Temporary Power & Critical Infrastructure Support"*（应急响应页）<br>⇒ **可能需外部租赁/采购应急变压器**（但这是推测，**官网未明述**）|

🔴 **判定**：**本单的「采购需求匹配度」偏低** —— 但**与买家 149 原判（不合格）不同点在于**：
**本版已取得 CEO 具名邮箱实证（A 档），触达质量高** ⇒ **建议策略**：
**以「设备选型建议影响力 + 应急变压器潜在需求」为切入，而非假设其为终端采购方。**

### 联系人（含仍_here 在职核验）

| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| **Phil Petrocelli** | **CEO（首封主送）** | **官网 Leadership 页明列**（一手）| ⚠️ 未知 | 🟢 高：官网在列 + 邮箱实证 | ⚠️ 低 | ⛔ 未定位 |
| Chris Duffell | CFO | 官网 Leadership 页明列 | ⚠️ 未知 | 🟢 高 | ⚠️ 低 | ⛔ 未定位 |
| Michael Messinger | CIO | 官网 Leadership 页明列 | ⚠️ 未知 | 🟢 高 | ⚠️ 低 | ⛔ 未定位 |
| Dave Robertson | CHRO | 官网 Leadership 页明列 | ⚠️ 未知 | 🟢 高 | ⚠️ 低 | ⛔ 未定位 |
| Jack Frost | CSO（Chief Safety Officer）| 官网 Leadership 页明列 | ⚠️ 未知 | 🟢 高 | ⚠️ 低 | ⛔ 未定位 |
| Thiago Moraes | CCO（Chief Commercial Officer）| 官网 Leadership 页明列 | ⚠️ 未知 | 🟢 高 | ⚠️ 低 | ⛔ 未定位 |

> 🔴 **机读结论**：
> 1. **官网 Leadership 页公开 6 人执行领导层**，**不含采购/供应链职位** ⇒
>    **采购决策人未公开**，需靠首封切入点或后续跟进撬开。
> 2. **Phil Petrocelli（CEO）是官网明列的最高决策人**，且**邮箱已实证** ⇒ **首封最优路径**。
> 3. ⚠️ **公司体量大（41 中心 / 900+ 技术人员）** ⇒ **决策链可能较长**，
>    首封直达 CEO 的成功率不高，但**作为「高价值目标」值得优先投入**。
> 4. ⚠️ **Thiago Moraes（CCO, Chief Commercial Officer）** 是商务口负责人 ⇒
>    **若 CEO 无回应，可作为第二轮目标**（但邮箱未实证）。

### 邮箱分档（A/B/C）

| 档 | 地址 | 依据 | 可否主送 |
|---|---|---|---|
| **A** | **`phil.petrocelli@shermco.com`** | **官网 Leadership 页确认姓名与职务 + SMTP 多格式命名规则探测实证（250）** | ✅ **主送**（点名 Phil Petrocelli, CEO）|
| **B** | `info@shermco.com`（兜底）；`inquiries@shermco.com`（官网 Contact 页明文，SMTP 校验 250、非 catch-all）| SMTP 实证存在 | ✅ 兜底主送（无具名）|
| C | `phil@` / `petrocelli@` / `ppetrocelli@shermco.com` | ⚠️ **已实测均为 550（不存在）** | ⛔ **禁止使用**（H2，已实证否定）|
| C | `sales@shermco.com` | ⚠️ **已实测 550** ⇒ 该司**无 sales 别名** | ⛔ 禁用 |

**🔴 邮箱验证方法与证据链（可复现）：**

```
域名 shermco.com
MX   = shermco-com.mail.protection.outlook.com   （Microsoft Exchange Online）
       + mailsecurity.in.tmes.trendmicro.com     （Trend Micro 前置，优先级 5）
SMTP 控制地址协议 + 多格式命名规则并行探测（源 IP 223.64.2.43，HELO jiezougroup.com）：
  RCPT info@shermco.com              -> 250 2.1.5 Recipient OK   （控制地址 A：已知真实）
  RCPT zzq9k2x7@shermco.com          -> 550 5.4.1 Access denied  （控制地址 B：随机地址，正确拒绝）
  ── 以下为命名规则并行测试 ──
  RCPT phil.petrocelli@shermco.com   -> 250 2.1.5 Recipient OK   ⭐ 【命中：CEO 邮箱】
  RCPT phil@shermco.com              -> 550 5.4.1 Access denied
  RCPT petrocelli@shermco.com        -> 550 5.4.1 Access denied
  RCPT ppetrocelli@shermco.com       -> 550 5.4.1 Access denied
  RCPT sales@shermco.com             -> 550 5.4.1 Access denied  （注：无 sales 别名）
⇒ ✅ 控制 250 + 随机 550 + 候选 250 ⇒ 判定【真正存在】。
⇒ ✅ 同时确定本域邮箱命名规则为 **`{first}.{last}@`**（非 `{f}{last}@`）——
     同域其他高管可按此规则推导（但**必须逐一实证后方可使用**，H2）。
```

> ⭐ **本批方法论价值**：这是**首次成功用「多格式命名规则并行探测」拿到 C 级高管邮箱**。
> 该手法成立的前提是**域公开目录成员信息**（随机地址返回 550）。
> ⇒ 已写入 `渠道状态清单.md`。

---

## 三、开发信建议（**仅限：收件人 / 时机 / 附件 —— 不含正文、不含主题行、不含开场句**）

| 项 | 建议 | 依据 |
|---|---|---|
| **主送** | `phil.petrocelli@shermco.com`，**正文点名 Phil Petrocelli（CEO）** | A 档实证最强路径 |
| **抄送/备选** | `info@shermco.com`（兜底）| SMTP 实证存在 |
| **进阶路径（第二轮）** | 若 CEO 无回应 ⇒ 转 **Thiago Moraes（CCO, Chief Commercial Officer）**；⚠️ 其邮箱需另行实证 | 官网一手 |
| **建议时机** | **中部时间（CT）工作日 08:00–10:00**（Irving TX = America/Chicago）| — |
| **建议附件** | ① UL 证书 **E541627**（三相液浸配电变 45–5,000 kVA）<br>② 公司介绍<br>🔴 **不建议首封附 E541626**（美国无高压主变成交证据）| 🔴 **美国客户 ⇒ 主推配电级 E541627** |
| **切入角度提示**（**仅提示，不代拟文案**）| ① 该公司做 **Breaker Refurbishment（断路器翻新）** ⇒ **已在配电设备翻新领域布局**，与配电变供给形成天然衔接<br>② 官网愿景强调 *"safety"* 与 *"reliability"* ⇒ 可强调**合规认证与质量一致性**<br>③ 52 年历史 + 41 中心 ⇒ **规模与供货稳定性**导向<br>④ 24/7 应急服务定位 ⇒ **响应速度**是核心价值 | 官网（一手）|
| ⛔ **禁止事项** | ① 不得称 certified（柱上变 E544629 仅 ECD 计划函）<br>② 不得提 YAWEI<br>③ 首封不报交期/价格<br>④ **不得对美国客户谈干式变**<br>⑤ **不得把「断路器翻新」误述为其制造变压器**<br>⑥ 不得发送供货记录 PDF | — |

---

## 四、⚠️ 矛盾点与风险提示

| # | 风险 | 说明 |
|---|---|---|
| 1 | ⚠️ **体量大、决策链长** | 41 中心 / 900+ 人 ⇒ 首封直达 CEO 成功率低 |
| 2 | ⚠️ **采购决策人未公开** | Leadership 页无采购/供应链职位 |
| 3 | ⚠️ **两个办公地址口径不一** | 官网 511 E John W Carpenter Fwy #700 vs 三方 2425 E Pioneer Dr |
| 4 | ⚠️ **第三方库误标为「Manufacturing」** | ContactOut 分类不实，官网无制造证据 |
| 5 | ⚠️ **美国客户 / 无高压主变证据** | 必须严守配电级（E541627）定位 |
| 6 | ⚠️ **多格式探测的边界** | `phil.petrocelli@` 已实证；**其他高管邮箱不得据规则直接推导使用**（H2）|
| 7 | 🔴 **DMARC = p=reject（最严）** | **发信须确保我方域通过 SPF/DKIM**，否则被直接拒收（本批最高风险域之一）|
| 8 | ⚠️ **SPF 记录异常** | TXT 中未检出标准 `v=spf1` |
| 9 | 🔴 **业务本质为「测试服务商」非采购方** | **需求匹配度低** ⇒ 切入角度须为「选型建议影响力」而非「终端采购」|

---

## 五、信息缺口清单（请勿编造）

| 缺口 | 状态 |
|---|---|
| **采购 / 供应链决策人** | ⛔ **未获取** |
| **Phil Petrocelli 任职时长** | ⛔ 未获取 |
| **员工总数（精确）** | 🟡 官网披露 700+ 技术人员 / 230+ 工程师 |
| **注册号 / 法人实体结构** | ⛔ 未获取 |
| **个人 LinkedIn 页** | ⛔ 未定位 |
| **变压器采购证据** | ⛔ 未获取 |
| **Thiago Moraes 邮箱** | ⛔ 未实证 |

---

## 六、一句话画像

**北美最大的电气测试机构（1974 年成立，NETA 认可，总部德州 Irving，
41 个服务中心 / 700+ 技术人员 / 230+ 工程师）。⓪ 层判定：电气测试与维护服务平台，
非制造商 ⇒ 通过。CEO Phil Petrocelli 由官网一手确认，具名邮箱
`phil.petrocelli@shermco.com` 已通过多格式命名规则探测实证 ——
**本批唯一取得 C 级高管直接邮箱的目标**。美国客户 ⇒ 主推配电级 E541627。**

---

## 七、渠道覆盖清单

| 渠道 | 状态 |
|---|---|
| **L-1 锁人** | ✅ **Phil Petrocelli（CEO）—— 官网一手；+ 5 名 C 级高管全公开** |
| **L0 官网** | ✅ 首页 + About + Leadership + Contact 抓取；拿到领导层 + 电话 + `info@` |
| **L1 政府一手** | ⛔ 未查 |
| **L2 命名+DNS** | ✅ 域名存活（EO + Trend Micro）；⭐ **SMTP 多格式命名规则探测成功命中 CEO 邮箱** |
| **L3 B2B 库** | 🟡 ContactOut / getprospect 有档案（**分类误标为 Manufacturing，未采信**）|
| **L4 社媒协会** | ⛔ 公司 LinkedIn 未定位 |
| **L5 黄页同址** | 🟡 allbiz 提及（未采信）|
| **L6 电话表单** | ✅ 电话 888-743-7626 / 972-793-5523；**温尼伯点 204.925.4022** |
| **L7 付费** | ⛔ 未启用 |

---

## 八、给下一环节的交付说明

**可直接使用的成果：**
1. **主送邮箱 `phil.petrocelli@shermco.com`（CEO，A 档实证）+ 备选 `info@` / `inquiries@shermco.com`**
2. **可在正文点名 Phil Petrocelli（CEO）**，另 5 名 C 级高管（CFO/CIO/CHRO/CSO/CCO）官网公开
3. **公司公开业务事实**：北美最大 NETA 认证电气测试机构；1974 年 Pete Sherman 创立；
   总部德州 Irving；**41 服务中心 / 700+ NETA 技师 / 230+ 工程师**；
   变压器相关能力：**Transformer Testing & Diagnostics / Transformer Repair and Testing / Oil Processing for Transformers**
4. 美国总部：**511 E John W Carpenter Fwy #700, Irving, TX 75062**；电话 **888-743-7626**
5. 加拿大温尼伯服务点：**1375 Church Avenue, Winnipeg, MB R2X 2T7**；电话 **204.925.4022**
6. ✅ **⓪ 层已通过**（不制造、不销售变压器；"Manufacturing Services" 实为服务制造业客户）

**必须知悉的风险：**
1. 🔴 **DMARC = p=reject（最严）** ⇒ **发信须确保 SPF/DKIM 合规，否则被直接拒收**
2. 🔴 **业务本质是「测试服务商」，非变压器采购方** ⇒ **需求匹配度低**，
   切入角度应为「设备选型建议影响力 + 应急变压器潜在需求」，**不可假设其为终端采购方**
3. ⚠️ **采购决策人未公开**（Leadership 页无采购岗）⇒ 需靠首封撬动或后续跟进
4. ⚠️ **体量大、决策链长** ⇒ 首封直达 CEO 成功率不高
5. ⚠️ **SPF 记录异常**；公司主体是**美国公司**（非加拿大本地企业）

**本环节未做（属其他环节职责）：**
- 未写正文、主题行、开场句、钩子、产品切片（→ 环节 ② 写开发信 agent）
- 未定最终发送时间与时区窗口排程（→ 环节 ③/④ 脚本）
