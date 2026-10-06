# 【买家 132】开发信交接单 — Western Technical Installations Ltd.

> 采集日期：2026-09-28 ｜ 名单来源：`线索资产/目标客户清单.csv` 序号 5（A 类 · ⭐ 高价值档）
> 采集方：找客户环节（本环节只产出交接单，不写正文/不碰模板/不定话术）
> ⚠️ 本表严格区分「已验证」与「未获取」，未找到的信息一律标注，**不做推断填充**（H1）
> ✅ 一句话结论：**2005 年成立、BC 纳奈莫的工业/高压电气承包商**，**Mott Electric 集团成员**
> （官网原句 *"WTI operates as part of the Mott Electric family"*）；
> 项目履历**全是一手变电站工程**（Horseshoe Bay 12kV 断路器更换、Walters 69/230kV 隔离开关、
> Valemount 25kV GIS 馈线、Kemano 备用隧道、Telkwa/Glenannan 高压断路器更换等）；
> **决策人锁定 Michel Lamoureux（President），实名邮箱 `mlamoureux@westerntechnical.ca`
> 取自官网 JSON-LD 结构化数据（一手）+ LinkedIn 职称交叉验证（双源）。**

---

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示(如有)
Western Technical Installations Ltd. | Michel Lamoureux | President（总裁） | mlamoureux@westerntechnical.ca | A 档（一手官网 JSON-LD + LinkedIn 双源，SMTP 因集团租户策略无法探测） | https://ca.linkedin.com/in/michel-lamoureux-60661026 | BC 纳奈莫（Nanaimo）工业/高压电气承包商，2005 年注册；Mott Electric 集团成员；专营变电站建设、高压电缆终端、断路器、仪表控制、电信；项目履历覆盖 BC Hydro 多个 12/25/69/230kV 变电站工程 | 官网全站实抓（含 JSON-LD 结构化数据）+ BC Corporate Registry（orgbook API）+ LinkedIn 公开摘要 + DNS/SPF 分析 | ⚠️ 集团成员（Mott Electric family），需注意其采购或受集团层面影响；SMTP 探测被集团租户策略拒绝（非地址问题）
```

**发信资格：✅ 通过**（九条闸门全过）
**邮箱档位：A（具名决策人 · 双源验证 · 非 catch-all 域）**

> 📌 **验证方式说明**：本单的 A 档依据**不是 SMTP 探测**（该域被集团统一拒绝），
> 而是 **①官网 JSON-LD 结构化数据明列** + **②LinkedIn 独立确认职称** 的**双源交叉**。
> 按硬规则 H3「≥1 一手来源 + 至少 1 个交叉源」，**本单满足**。

---

## 二、补充信息（扩展段）

### 标准字段明细

| 项 | 内容 | 来源 |
|---|---|---|
| **公司全称** | **WESTERN TECHNICAL INSTALLATIONS LTD.**（官网亦简称 WTI）| 🔴 **BC Corporate Registry（一手）** |
| **国家 + 城市** | **加拿大 BC 省 Nanaimo（纳奈莫）** | 官网 Contact 页 + 注册库（双源✅）|
| **州省** | **BC ✅** | 官网 + 注册库 |
| **详细地址** | **1718 Kidson Road, Nanaimo, BC V9S 3H2**（官网页脚写 V9S 3H5，Contact 页写 V9S 3H2 → ⚠️ 邮编不一致，见风险提示第 4 条）| 官网 Contact 页 + 页脚（皆一手）|
| **电话** | **(250) 751-0362** | 官网 Contact 页 + JSON-LD（双处一致✅）|
| **注册信息** | BC 注册号 **BC0734458**；Business Number **827096678**；注册日 **2005-09-08**；状态 **ACT（有效）**；类型 **BC** | 🔴 **BC Corporate Registry（一手，经 orgbook.gov.bc.ca API）** |
| **成立年份** | **2005**（注册库 2005-09-08；官网自述 *"since its inception in 2005"*）✅ **双源一致** | 注册库 + 官网 |
| **域名** | westerntechnical.ca（MX 与 SPF 均指向 **Mott Electric 集团**）| DNS 分析 |
| **规模** | ⚠️ 未获取确切人数（官网称 "seasoned team"、项目有 project managers / on-site management / skilled craftsmen 层级）| 官网定性描述 |
| **营收** | ⚠️ 未获取 | — |
| **官网** | https://westerntechnical.ca | — |
| **坐标** | 49.1665900, -123.9404470（JSON-LD 明列）| 官网 JSON-LD（一手）|

> 🔴 **集团归属判定（本单必读）**：
> **官网 About 页原句**：*"WTI operates as part of the **Mott Electric** family."*
> **DNS 三重印证**：
> - MX 主记录 = `mottelectric-com.mail.protection.outlook.com`（Mott 的 M365 租户）
> - SPF = `v=spf1 a:mail.mottelectric.com include:spf.protection.outlook.com ~all`
> - **与 `mottelectric.com` 的 SPF 记录逐字相同**
>
> **判定：WTI 是 Mott Electric 集团的成员公司（子公司/关联公司）。**
> ⚠️ **这不构成排除理由** —— WTI 是**独立运营的承包商主体**，有独立官网、独立地址（纳奈莫）、
> 独立注册号、独立总裁（Michel Lamoureux）。**Mott Electric 是 BC 最大的电气承包商之一**。
> → **但需注意**：大型集团可能存在**集中采购/框架协议**，其变压器采购未必由 WTI 本级决定。
> 见风险提示第 1 条。

### 联系人（含 still_here 在职核验）

| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| **Michel Lamoureux** | **President（总裁 · 首封主送）** | LinkedIn 公开摘要明列「**president at western technical installations ltd**」（小写原样）；官网 JSON-LD 明列其邮箱 | ⚠️ 未知（LinkedIn 未显示起始年月）| **高**：LinkedIn 页在列；官网 JSON-LD 用其邮箱作 customer service 联系点 | **低**（总裁级）| ✅ https://ca.linkedin.com/in/michel-lamoureux-60661026 |

> 🔴 **机读结论**：
> 1. **Michel Lamoureux 是唯一可确认的决策人**，且**双重独立源**：
>    - **源 ①**：官网 `westerntechnical.ca` 的 **JSON-LD 结构化数据**（`@type: Organization` → `contactPoint.email`）
>      明列 `mlamoureux@westerntechnical.ca` —— **这是网站自己声明的一手数据**，非第三方猜测。
>    - **源 ②**：LinkedIn 公开摘要显示其职称为 **president at western technical installations ltd**。
> 2. **姓名与邮箱前缀完全吻合**：`m`(ichel) + `lamoureux` → `mlamoureux@` ✅ 命名规则自洽。
> 3. ⚠️ **官网无团队页**，除总裁外**无其他管理层公开**。
> 4. ⚠️ **任职时长未获取** —— LinkedIn 未显示起始年月，不得推断。

### 邮箱分档（A/B/C）

| 档 | 地址 | 依据 | 可否主送 |
|---|---|---|---|
| **A** | **`mlamoureux@westerntechnical.ca`** | ①**官网 JSON-LD 结构化数据明列**（一手）<br>②**LinkedIn 独立确认 Michel Lamoureux = President**（交叉源）<br>③姓名/邮箱前缀自洽 | ✅ **主送** |
| B | ⚠️ 未在官网发现 `info@` / `sales@` 等角色邮箱 | 官网仅列总裁邮箱 + 电话 | — |
| C | — | 无 | — |

**🔴 邮箱验证方法与证据链（可复现 —— 本单结论是「SMTP 不可用，改用双源法」）：**

```
域名 westerntechnical.ca
MX 主 = mottelectric-com.mail.protection.outlook.com   （Mott Electric 集团 M365 租户）
MX 备 = mx-capricab.easydns.com

🔴 SMTP RCPT 探测结果（2026-09-28 实测）：
   postmaster@westerntechnical.ca        → 550  5.4.1 Recipient address rejected: Access denied
   zzz_nonexistent_probe_9987@           → 550  5.4.1 Access denied   （随机地址）
   john.smith@                           → 550  5.4.1 Access denied   （假姓名）
   mlamoureux@                           → 550  5.4.1 Access denied
   info@                                 → 550  5.4.1 Access denied
   postmaster@mottelectric.com           → 550  5.4.1 Access denied   （母域同样）

🔴 对照组（证明来源 IP 未被拉黑）：
   info@martechelectrical.com            → ✅ 250  Recipient OK      （另一 M365 域，正常应答）

⇒ 判定：**Mott Electric 集团 M365 租户配置了「对外部来源一律 5.4.1 拒绝」的策略**
   （错误码是 5.4.1 Access denied，**不是** 5.1.1 User unknown）
   → 该域内**任何地址**都无法通过 SMTP 区分真伪，**SMTP 探测对本域完全失效**
   ⚠️ 与本批 131（catch-all）失效原因不同：131 是「一律 250」，本单是「一律 550」

⇒ 因此本单采用 **双源交叉法**：
   源① 官网 JSON-LD（站点自声明，一手文档）
   源② LinkedIn 公开摘要（独立平台，职称确认）
```

> ✅ **双源交叉 + 命名自洽** —— 按 H3「≥1 一手来源 + ≥1 交叉源」，满足 A 档要求。
> ⚠️ **但本单无法获得 SMTP 层面的可达性证明**。若发送环节要求 SMTP 确认，**请知悉本域不可能给出**。

### 我为什么找他

**这家公司的项目履历表，几乎就是一份「变压器上游的变电站设备清单」。**

| # | 具体观察（均有官网原句出处） |
|---|---|
| 1 | **官网 Services 页原句**：*"Our services, like **Electrical Substation Construction**, **High Voltage Terminations**, and Process and Power Piping"* —— 变电站建设是其首位业务 |
| 2 | **Horseshoe Bay Substation** 项目：*"**12kV Circuit Breaker and Disconnect Removal and Replacement**, **69kV disconnect and strain bus replacement** project."* —— 明确 12kV / 69kV |
| 3 | **Walters Substation** 项目：*"**69kV & 230kV Strain Bus Insulator Replacement, 69kV & 230kV Disconnect replacement & SS Panel boards**."* —— 明确 69kV / 230kV |
| 4 | **Valemount Substation** 项目：*"installing a new **25KV GIS feeder section** at a **BC Hydro facility**"* —— 明确 25kV，且直接服务 BC Hydro |
| 5 | **Telkwa & Glenannan Substations** 项目：*"replacing **high-voltage breakers** in substations across two locations"* |
| 6 | **RCE Upper Harrison & Sachteen Substations** 项目：*"expansion and commissioning of a new substation in Pemberton, BC. Working in collaboration with **Black & McDonald**"* —— 与大型 EPC 协作 |
| 7 | **Kemano Backup Tunnel Project**：为 **Kemano Generating Station**（大型水电站）建立二次配电系统 + *"Advanced backup **generator installation**"* |
| 8 | **Site C Project 电信**：*"telecom and waveguide modifications to remote microwave towers across **Peace River region** and Northern BC"* —— **Site C 是 BC 最大的在建水电项目** |
| 9 | **自述定位**：*"WTI and our affiliates aim to become the **top contractor in the utility sector in British Columbia**."* —— *"our affiliates"* 再次暗示集团结构 |
| 10 | **服务内容含中压/高压电缆终端**：*"Medium and HV Cable Terminations"*、*"Circuit Breaker Specialists"* |

> 📌 **开场可用的合法事实**（措辞由写信环节定）：
> 「Walters 变电站的 69/230kV 隔离开关更换」或「Valemount 变电站的 25kV GIS 馈线（BC Hydro 设施）」
> —— **均为官网项目页原句，只有这家成立**。

### 买家类型 / 需求品类

**买家类型：🔥 B — 工业/高压电气承包商（EPC / 施工型，纯 B 型）**
判定依据（六层过筛结果）：
- ⓪ 反身排除：**通过** —— 官网**无任何 "manufacturer / we manufacture / our factory" 字样**；不做设备制造；未发现代理任何品牌（尤其**未见 YAWEI**）
- ① 价值链：主营 = 变电站建设 + 高压终端 + 断路器 → 价值链中间环节 ✅
- ② 类型：**B（工业/高压电气承包商）** —— 依据 *"Electrical Substation Construction"* + 全部项目均为施工/更换类
- ③ 产品形态：**变电站变 / 配电变**（见下）
- ④ 地域：**BC（加拿大，权重高）** → **可谈高压 E541626**
- ⑤ 规模：⚠️ 未获取（Mott 集团成员，独立团队规模不明）

**需求品类（带结论态 —— 加拿大客户，可谈高压）：**

```
- `变电站变 / 小主变（UL E541626，750–110,000 kVA，可直供）`  ← 主谈：官网项目全为 12/25/69/230kV 变电站工程
- `三相液浸电力变（UL E541626，可直供）`                     ← 同 E541626 区间
- `三相美变 / padmount（UL E541627，可直供）`                ← 配电侧配套，备选
- `站用变 / 接地变（需人工确认具体规格）`                     ← 官网 substation construction 有联想空间
- `干变（加拿大可谈：built to CSA/IEEE，需人工确认）`         ← 备选，不首推
```

> 🔴 **特别注意**：官网给出 **12kV / 25kV / 69kV / 230kV** 四个等级，
> **但这些是「断路器/隔离开关/母线/GIS 馈线」的电压，不是其更换的变压器电压。**
> 项目描述中**从未出现 "transformer" 一词** —— 其披露的项目全是**开关类设备更换**。
> → ⛔ **不得写成「他们需要 230kV 变压器」**（无证据）。
> → 但**变电站承包商必然涉及变压器安装场景**，首推落在 **E541626 变电站变区间**合理，
>    ⚠️ **具体 kV/kVA 列为缺口**。

### 电压·频率·认证要求

| 项 | 内容 | 来源 |
|---|---|---|
| **频率** | **60 Hz**（加拿大）✅ 零改造适配 | 国别推定 |
| **电压** | 官网项目明列 **12kV / 25kV / 69kV / 230kV**（⚠️ 均为**开关设备**电压，非变压器电压）| 官网原话 |
| **客户资质** | 服务 **BC Hydro** 设施；与 **Black & McDonald** 协作；参与 **Site C** 项目 | 官网项目页 |
| **认证（我方口径）** | 加拿大可写 `built to CSA/IEEE/IEC standards`；美变亮 `UL E541627`；电力变亮 `UL E541626` | 我方能力边界 |
| ⛔ **禁止写法** | `CSA Certified`／`cUL and CSA`／`SASO`／`SONCAP`；**不得写变压器具体 kV/kVA** | 红线 §二 |

> 🔴 **12/25/69/230kV 出自官网项目描述，均为「断路器/隔离开关/GIS 馈线」电压。**
> 正文**可以引用其项目电压**（原话），但 ⛔ **不得据此推断变压器规格**。

### 采购信号

| # | 信号 | 强度 | 出处 |
|---|---|---|---|
| 1 | **项目履历连续覆盖多个 BC Hydro 变电站工程**（Horseshoe Bay / Valemount / Telkwa / Glenannan / Walters）| 🔥🔥🔥 | 官网项目页（一手）|
| 2 | **参与 Site C**（BC 最大在建水电）+ **Kemano 发电站** 项目 → 大型项目资质 | 🔥🔥🔥 | 官网项目页（一手）|
| 3 | **官网自述目标是 BC utility 领域的 top contractor** → 扩张期 | 🔥🔥 | 官网 Services 页（一手）|
| 4 | **BC 注册状态 ACT**，2005 年至今 21 年持续经营 | 🔥🔥 | 注册库（一手）|
| 5 | 与 **Black & McDonald**（大型 EPC）协作 → 有供应链协作经验 | 🔥 | 官网项目页 |
| 6 | ⚠️ Mott 集团成员 → 可能有**集团集中采购**，本级决策权受限 | ⚠️ 双刃 | 官网 + DNS |

> ⚠️ **信号强度：强**。项目履历密集且全为变电站，是名单中**变电站经验最密集的一家之一**。
> ⚠️ **但集团归属是双刃剑** —— 见风险提示第 1 条。

### 可利用的钩子（按强度排序）

| 序 | 钩子 | 强度 | 落点品类 | 是否可写 |
|---|---|---|---|---|
| 1 | **官网项目页的 Walters 69/230kV 隔离开关更换** | 🔥🔥🔥 | 变电站变 / 小主变 | ✅ |
| 2 | **Valemount 25kV GIS 馈线（BC Hydro 设施）** | 🔥🔥🔥 | 变电站变 | ✅ |
| 3 | **参与 Site C / Kemano 水电站** —— 大型项目背书 | 🔥🔥🔥 | — | ✅ |
| 4 | **Horseshoe Bay 12kV 断路器更换** | 🔥🔥 | 配电侧 | ✅ |
| 5 | **与 Black & McDonald 协作** → 有 EPC 供应链协作经验 | 🔥 | — | ⚠️ 第三方公司名，引用需谨慎 |
| 6 | **Mott Electric 集团成员** | ⚠️ | — | ⛔ **不建议写入正文**（可能触发集团采购流程，反而绕远）|

### 开发信建议

> 📌 本段是**给写信环节的输入**，不是正文。**不含主题行、开场句、产品切片措辞**（分工铁律）。

- **收件人策略**：主送 **Michel Lamoureux（President）** `mlamoureux@westerntechnical.ca`（A 档，双源验证）
  - 🔴 **一家公司只发 1 人**（skill §3.0 红线）—— 官网未公开其他管理层，**无双送选项**
  - ⚠️ **集团层面提示**：因 Mott Electric 集团可能存在集中采购，
    若两轮无回应，**可考虑转向 Mott Electric 集团层面**（`mottelectric.com`）—— 但**需用户先确认**（非本单范围）
- **称呼**：Michel Lamoureux（LinkedIn 公开摘要明列 President）
- **开场角度（供选择，非指定）**：可考虑从「官网项目表里的 Walters 69/230kV 隔离开关更换」或「Valemount 25kV GIS（BC Hydro）」切入 —— **最终写法归写信环节**
- **附件建议**：不带供货记录名录（H7 红线）；可备 **UL E541626 区间说明（750–110,000 kVA）**
- **发送时段**：客户在 **BC 省 = 太平洋时区（PT）**
  - 目标送达：**当地工作日 08:00–10:00**
  - 北京发送窗口（夏令时）：**23:00–01:00（跨日）**
  - 冬令时：24:00–02:00（跨日）
  - ⚠️ **周末不发**（按客户当地星期判断）
- **送达配置**：
  - 网关 = **Mott Electric 集团 M365 租户**（`mottelectric-com.mail.protection.outlook.com`）
  - ⚠️ SPF = `v=spf1 a:mail.mottelectric.com include:spf.protection.outlook.com ~all`（**~all 软失败**，非 -all）
  - ⚠️ 发信前**须复核 DMARC**（本单未取 DMARC，见缺口）
  - ⚠️ **该租户对外部 SMTP 探测一律 5.4.1 拒绝** → 说明其**反探测策略较严**，
    写信/发送环节**务必确保我方域名 SPF/DKIM/DMARC 齐全**，否则易被拒
  - 建议**纯文本**（无图片签名需求）

### ⚠️ 矛盾点与风险提示

| # | 风险 | 详情 | 处置 |
|---|---|---|---|
| 1 | ⚠️ **Mott Electric 集团成员（双刃剑）** | 官网原句 *"part of the Mott Electric family"* + DNS 三重印证。**不是排除理由**（独立实体、独立总裁），**但集团可能有集中采购/框架协议**，WTI 本级对变压器采购的决策权未知 | **正常发信**；若两轮无回应，**可考虑转 Mott 集团层面**（需用户确认）；⛔ **不建议在首封就提"集团"，可能触发复杂采购流程** |
| 2 | ⚠️ **SMTP 无法验证邮箱** | 集团租户对外部来源一律 `5.4.1 Access denied`（非地址不存在）| **改用双源法**（官网 JSON-LD + LinkedIn）；已如实标注；**发送环节若要求 SMTP 确认，本域给不出** |
| 3 | ⚠️ **项目描述中从未出现 "transformer" 一词** | 全部项目是**断路器/隔离开关/母线/GIS 馈线**更换 | ⛔ **不得写成"他们采购变压器"**；但变电站承包商涉及变压器安装属合理范畴 |
| 4 | ⚠️ **官网邮编不一致** | Contact 页写 **V9S 3H2**，页脚写 **V9S 3H5** | 寄样前须核实；**建议以 Contact 页 V9S 3H2 为准** |
| 5 | ⚠️ **除总裁外无管理层信息** | 官网无团队页 | 无双送选项；如需第二联系人，需用户另行提供 |
| 6 | ⚠️ **Michel Lamoureux 任职时长未知** | LinkedIn 未显示起始年月 | **不得推断**；只知其"现任 President" |
| 7 | ⚠️ **DMARC 未查** | 本单只取了 MX/TXT/SPF | 见缺口清单，交发送环节补 |
| 8 | ⚠️ **"our affiliates" 表述含义未明** | 官网 Services 页称 *"WTI and our affiliates"* | 可能指 Mott 集团其他成员；**不得展开推断** |
| 9 | ⚠️ **规模/营收未获取** | 无第三方数据命中（D&B/Cybo 均被 Cloudflare 拦）| 列为缺口 |

### 信息缺口清单（请勿编造）

> 🔴 **以下字段正文一个字都不能出现**（红线：比"不编造"更严格，连模糊表述都不行）。

| 缺失项 | 说明 |
|---|---|
| **变压器侧电压等级（kV）** | 未获取。只用官网**项目**电压原话（12/25/69/230kV，均为开关设备）|
| **常用变压器容量段（kVA）** | 未获取。**不得假设** |
| **员工人数 / 营收** | 未获取 |
| **Michel Lamoureux 任职起始年份** | 未获取。**不得推断** |
| **其他管理层名单** | 未获取（官网无团队页）|
| **变压器采购方式（本级 vs 集团）** | 未获取 |
| **是否已有中国供应商** | 未查（未启用海关数据源）|
| **DMARC 记录** | 未查 |
| **公司 LinkedIn 页** | 未找到（只有总裁个人页）|
| **"Mott Electric family" 的具体股权结构** | 未获取。**不得推断为全资子公司** |
| **正确邮编（V9S 3H2 or V9S 3H5）** | 官网自相矛盾，未核实 |
| **Kemano / Site C 项目金额** | 未获取 |
| **任何未在官网列出的客户名** | 未获取。**不得编造** |

### 一句话画像

**2005 年成立的 BC 纳奈莫工业/高压电气承包商，Mott Electric 集团成员** ——
项目履历是名单中最密集的变电站工程集（Horseshoe Bay 12kV、Walters 69/230kV、Valemount 25kV GIS、
Telkwa/Glenannan 高压断路器、Kemano 水电站、Site C 电信），
自述目标是「BC utility 领域 top contractor」；
**决策人 Michel Lamoureux（President）已锁定，邮箱取自官网 JSON-LD 一手 + LinkedIn 交叉验证** ——
**人明确、信号强、邮箱达（A 档双源）**，⚠️ 但需注意集团采购权归属问题。

### 渠道覆盖清单（L-1、L0–L7）

| 层 | 结果 | 一句话 |
|---|---|---|
| **L-1 锁人** | ✅ | LinkedIn 公开摘要锁定 **President Michel Lamoureux**；⚠️ 官网无团队页 |
| **L0 官网全量** | ✅ | 主页 / about / services / projects / contact 5 页实抓；🔴 **官网 JSON-LD 明列总裁邮箱**（本单关键一手源）|
| **L1 政府一手** | ✅ | 🔴 **BC Corporate Registry 命中**：BC0734458 / BN 827096678 / **2005-09-08** / 状态 ACT |
| **L2 命名 + DNS** | ✅ | MX/SPF/TXT 全取；🔴 **判定集团租户**（MX+SPF 指向 Mott）；**SMTP 探测被 5.4.1 拒绝**（已用对照组证明非 IP 问题）；DMARC 未查 |
| **L3 B2B 库** | ❌ | D&B / Cybo / Infobel 均命中条目，**但全部被 Cloudflare 拦截，未取到内容** |
| **L4 社媒协会** | ⚠️ | LinkedIn 个人页命中；**无公司页**；未发现行业协会会员页 |
| **L5 黄页同址** | ⚠️ | 地址已取（1718 Kidson Rd）；⚠️ 邮编官网自相矛盾 |
| **L6 电话表单** | ✅ | **电话 (250) 751-0362 已取**（官网 + JSON-LD 双处）|
| **L7 付费** | ❌ | 未启用 |

> 🔴 **集团层面的追加机会（超出本单范围，供决策）**：
> Mott Electric（`mottelectric.com`）是 BC 大型电气承包商集团。
> 若 WTI 本级无回应，**可考虑升级至集团采购口** —— 但**需用户明确授权**（涉及新实体、新背调）。

---

## 三、交付方自检（写单者留痕）

- [x] **第 0 步判定已做**：类型归属（B 工业/高压电气承包商）+ 判定依据 + 可对应产品形态
- [x] **第 ⓪ 层反身排除已做**：官网无 "manufacturer" 字样；不制造设备；未代理品牌（无 YAWEI）；**集团归属已明确标注（非排除理由）**
- [x] **背调 13 步「必做 6 步」已走**：公司名 ✅ / 版权主体 ✅（© 2026 WTI）/ 简介历史 ✅ / **注册库 ✅** / 无街景（地址已取）/ LinkedIn 锁人 ✅
- [x] **排重已做**：与 `_dedup_keywords.txt`（164 词）+ `_bounce_domains.txt` + `00_buyer_master_dedup.md` 比对，**无命中**
- [x] **按公司归并**：仅 1 个实名邮箱（总裁），**无并送风险**
- [x] `.md` 已实际写入磁盘
- [x] 9 核心字段 + 12 扩展段齐
- [x] 「我为什么找他」为**具体观察**（10 条，均有官网原句）
- [x] 「信息缺口清单」明确列出不能写的字段（13 项）
- [x] 「需求品类」**带结论态**
- [x] 联系人四栏（still_here）已核
- [x] 邮箱已分 A/B/C 档，**验证方法可复现（并诚实说明 SMTP 不可用、改用双源法）**
- [x] 过完 §三 九条闸门
- [x] 未写任何邮件正文 / 主题行 / 开场句措辞（分工铁律）
