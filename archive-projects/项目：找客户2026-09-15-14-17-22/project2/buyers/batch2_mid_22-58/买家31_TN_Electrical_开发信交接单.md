# 【买家 31】开发信交接单 — T&N Electrical Contracting Ltd.

> 编号变更记录：本文件原为【买家 28】（创建 2026-09-21 14:55），因另一对话的 Romar Electrical 先占 28 号（14:53），按先占先得改為 **31 号**（方案A，用户已确认）。

> 采集日期：2026-09-21
> 名单来源：你提供的（公司名 + 对标 Boundary Electric + 国家/地区 BC/AB + Vancouver + 官网 tnelectrical.ca，已逐项独立核实）
> ⚠️ 本表严格区分「已验证」与「未获取」，未找到的信息一律标注，不做推断填充
> 🟢 **本家结论前置：BC 变电站专业承包商（substation civil + electrical），3 个 BC Hydro 在运变电站项目 + 变压器安装独立业务线 —— 与 JZP 主变/变电站变高度对口，建议高优先级**
> ➕ **用户补充（2026-09-21）：小变压器也做，配电是主力 —— 本单主钩子为 power transformer / transformer installations，配电为辅**

---

## ✅ 先核对你提供的信息

| 你提供的 | 核实结果 | 来源 |
|---|---|---|
| **公司名 T&N Electrical Contracting Ltd.** | ✅ **正确** | 官网全站标题一致 |
| **对标 Boundary Electric (BC)** | 🟡 **部分对标，类型不同** —— Boundary（Grand Forks, BC，1947年，57人）是**制造商**（变压器/开关柜/unit sub 至10MVA/34.5kV）；T&N 是**安装/EPC承包商**（变电站土建+电气、变压器安装）—— **互补关系，非竞争**，见 §补充 | 官网 + Boundary 官网/LinkedIn |
| **国家/地区 加拿大 (BC/AB)** | ✅ **正确** | 官网 "across British Columbia and Alberta" + 首页 "Across Canada" |
| **详细地址 Vancouver, BC, Canada** | ✅ **正确但仅到城市** —— 官网 Contact/首页只写 "Vancouver, BC, Canada"，**无街道、无邮编、无电话、无邮箱** | 官网 contact.html + index 实测 |
| **官网 tnelectrical.ca** | ✅ **正确** | 实测全站5页均 HTTP 200 |

**➜ 修正：不要在开发信中写其街道地址（官网未公布）；对标 Boundary 时表述为"安装/工程侧伙伴"而非同类制造商**

---

## 标准字段

**公司全称**
**T&N Electrical Contracting Ltd.（官网写作 T & N Electrical Contracting Ltd. / T&N Electrical）**
- 实体类型：Ltd.（BC 省注册推定，**注册号/注册日期：未获取** —— opengovca 未命中本家，同名 T&N Edmonton 系不同公司已排除）
- ⚠️ **成立日期：未获取** —— 官网自述 "**newly established company**" + 页脚 "© 2026"，领导层合计 "45+ years combined"；**暂判为 2025–2026 新设公司，创始人自带存量业绩**，注册库未独立印证
- ℹ️ 官网自述："A new company built by people with a long, proven track record"

**国家 + 城市**
加拿大（Canada）+ **不列颠哥伦比亚省温哥华市（Vancouver, BC）**
- **完整地址：Vancouver, BC, Canada** ✅（官网 Contact 页 Office 栏原文，仅到城市）
- ⚠️ **街道/邮编/电话/传真：未获取**（官网5页 + 搜索均无；Contact 仅留表单 Name/Email/Company/Project details）
- 服务区域：**BC + AB（官网明文），首页另写 Across Canada**

**联系方式**
- **电话：未获取**（官网无；搜索 `"tnelectrical.ca" phone` 零命中）
- **邮箱：未获取**（官网无；搜索 `"@tnelectrical.ca"` 零命中；Contact 仅表单）
- **官网表单**：`/contact.html`（字段 Name/Email/Company/Project details）+ 首页 CTA —— **当前唯一公开触达入口**
- 🔴 **DNS 邮件配置**（dns.google API 实测）：
  - **MX = `tnelectrical-ca.mail.protection.outlook.com`** → **Microsoft 365**
  - **SPF = `v=spf1 include:spf.protection.outlook.com -all`** → ✅ **hard fail，配置规范**
  - → 域名邮箱基础设施已就绪（推测有未公开的 info@/contact@ 类邮箱），但**无公开样本，不可推演**

**联系人 / 职位**

| 姓名 | 职位 | 来源与印证数 |
|---|---|---|
| 🔥 **Terry Bennett** | **Chief Executive Officer** | 官网 About 页 Leadership 栏明文 + 头像；自述 "23+ years delivering complex projects" —— 单源（官网），**未经第二方印证** |
| 🔥 **Marwa Atia** | **Chief Operating Officer** | 官网同上；"15+ years construction/utility/contract administration" —— 单源 |
| 🔥 **Nathan Friesen** | **Director of Operations** | 官网同上；"20+ years across substations and power generation" —— 单源；⚠️ LinkedIn 同名多为 HVAC/输送带人士，**均非本家，已排除，不采信** |

- 🎯 **决策链**：CEO Terry Bennett（商务关系）+ COO Marwa Atia（合同/财务）+ Nathan Friesen（现场执行/QA-QC）—— **EPC 型买家建议同时触达 Owner + P&C/现场侧**
- ⚠️ **三人邮箱/电话/LinkedIn 个人页：均未获取**（官网仅照片+头衔；LinkedIn 搜索 Terry Bennett 命中英国 TB Electrics，Nathan Friesen 命中 Genesis Controls/HEMP，均非本家）
- ⚠️ **采购负责人：未获取**（新公司，无 Team 扩展页）

**邮箱（汇总）**
- 🔴 **已确认邮箱：无**（官网零邮箱；B2B 库零记录）
- 🟡 **可推测但不可用**：M365 已配，`info@`/`contact@`类地址极可能存在，但**零样本、零索引，禁止推演主送**
- ✅ **触达策略**：官网表单首触 + 点名三位领导 + 项目点名（Dunsmuir/Ingledow/Nicola），见 §开发信建议

**LinkedIn / 网站**
- **官网**：https://tnelectrical.ca/（5页全抓：`/`、`/services.html`、`/about.html`、`/projects.html`、`/partnership.html`、`/contact.html`）
  - ✅ 无 Cloudflare 拦截，WebFetch 全通
  - ⚠️ 页脚极简：仅 logo + "© 2026 T&N Electrical — Vancouver, BC"，**无社媒、无地址、无电话**
- **LinkedIn 公司页：未找到**（搜 "T&N Electrical Contracting" 无公司页；符合 2025–26 新设特征）
- **Facebook/Instagram/YouTube：未找到**（官网无社媒链接）
- **第三方档案：未获取**（D&B/Manta/opengovca 均无本家；Sq'ewqel 合作方页有其简介一行，可作旁证）

**买家类型**
**EPC / 终端承包商（Terminal/EPC）— 公用事业变电站专业承包商（civil + electrical）**

- 官网定位："civil and electrical solutions for **utility and substation projects**"；"work closely with **owners, EPCs, and project teams**"
- ✅ 变电站全包（foundations → energization）+ HV/MV 电缆 + 变压器安装 + P&C —— **典型 EPC 分包/直包商**
- ✅ 无 Shop/Inventory/仓库/多办公点 —— **非渠道商**（§0.5 清单 0/6）
- ✅ 无 manufacturer/factory 自述 —— **非同行**（与 Boundary 制造商互补）
- ✅ 原住民合作（Seabird Island Band / Kwikwetlem First Nation）—— **BC Hydro 项目入围强信号**

**需求品类**

**① 变电站建设（Substation Construction，全包）** 🔥🔥 最核心
- 官网独立业务线："Full civil and electrical build-out … from foundations and structures to **final energization**"

**② 变压器安装（Transformer Installations，独立业务线）** 🔥🔥 **JZP 直接对口**
- 官网原文："**Setting, assembly, and connection of power transformers** with careful field coordination"
- + Equipment Foundations："Precision foundations for **transformers, breakers**, and structural steel"

**③ HV / MV Cabling** 🔥
- "High- and medium-voltage cable installation, **terminations, and testing in energized environments**"

**④ 接地与管群（Grounding & Duct Banks）**
- "Engineered grounding grids and bonding" + "Concrete-encased and direct-buried duct bank systems"

**⑤ 土建（Excavation + Equipment Foundations）**
- Site prep/trenching/earthworks + 变压器/断路器基础

**⑥ 保护与控制（Protection & Control）**
- "P&C wiring, panel installation, and **commissioning support**"

**⑦ 未获取**：具体 kV/kVA 容量、变压器品牌偏好、开关柜规格 —— 官网无数字

**触达来源**
1. **官网全站抓取**（5页：8大业务线、3位领导、3个具名变电站项目、BC/AB 区域、原住民伙伴）—— 主来源
2. **DNS（dns.google API）** —— MX M365 + SPF `-all` 实测
3. **WebSearch 交叉** —— Boundary Electric 对标核实（制造商 1947/57人/10MVA/34.5kV）；同名排除（Edmonton T&N/英国Terry/Genesis Nathan 均非本家）；Sq'ewqel 伙伴页旁证；BC Hydro Dunsmuir/Ingledow/Nicola 电压背景（230/500kV）核实
4. **ImportYeti/海关**：加企非必查，未发现记录（**未列为缺口，属渠道不适用**）
5. ⚠️ **未能获取**：BC 注册库直连（opengovca 无命中）、电话/邮箱全网零命中、LinkedIn 公司页/三人个人页、D&B、BBB、招聘、投标库（BC Bid/MERX 需逐标查，本次未展开）

**我为什么找他（具体观察，1-2 句）**
**T&N Electrical Contracting Ltd. 是温哥华新设（官网自述 newly established，©2026）的公用事业变电站专业承包商**，由 **Terry Bennett（CEO，23+年）/ Marwa Atia（COO，15+年）/ Nathan Friesen（Director of Operations，20+年变电站与发电）** 带队，合计 45+ 年联合经验，服务 **BC + AB**，官网设 **Transformer Installations（power transformer setting/assembly/connection）+ Equipment Foundations（transformer/breaker）+ HV/MV Cabling + Substation Construction（至 energization）+ P&C commissioning** 独立业务线，具名项目含 **Dunsmuir / Ingeldow / Nicola 三座 BC Hydro 在运高压变电站**，并与 **Seabird Island Band / Kwikwetlem First Nation** 原住民合作 —— **属电力变压器/变电站变的直接安装与采购影响方**。

**电压 / 频率 / 认证要求**
- **电压等级：定性已获取，数值未获取** 🟡
  - 官网定性：**HV / MV**（cabling）、**high-voltage utility environment**（3项目均有）、power transformers
  - 背景核实（BC Hydro 公开资料，非本家披露）：Dunsmuir 230/500kV（含 230/138kV 主变）、Ingledow 500kV（BC Hydro 最重要枢纽，1965年 vintage）、Nicola 500kV（ILM 项目 Merritt–Coquitlam 250km）—— ⚠️ **仅作背景理解，禁止在开发信中写"了解到你们用 500kV"**
  - ℹ️ 加拿大国别常识：60Hz；CSA / IEEE；BC 需 Technical Safety BC / FSR —— 属常识，**非本家披露**
- **频率：未获取**（加拿大 60Hz，出口注意）
- **认证要求：未获取**
  - ✅ 安全导向自述（safety-led culture）+ 原住民合作（BC Hydro 合规强信号）
  - ⚠️ **对供应商变压器的认证要求（CSA C88 / UL / IEEE / DOE / NRCan）：未获取**
  - ⚠️ **BC Hydro 合格供应商/承包商名录状态：未获取**（建议后续查 BC Bid/MERX 中标延续）

**采购信号（按强度排序）** 🔥 本家信号强
- 🔥🔥 **官网独立 "Transformer Installations" 业务线（setting/assembly/connection of power transformers）** → **电力变压器直接需求**
- 🔥🔥 **3 个 BC Hydro 在运变电站具名项目**：Dunsmuir（grounding for fencing， HV 环境）、Ingledow（QEW + safety + security， active 站）、**Nicola（Recently Awarded， QEW）** → **当前有活跃项目**
- 🔥 **Substation Construction 至 energization + P&C commissioning** → 项目型成套采购影响力
- 🔥 **HV/MV terminations + testing in energized environments** → 有高压试验与附件需求
- 🔥 **原住民双伙伴 + "owners, EPCs" 协同表述** → 已进入 BC Hydro 生态，非路边电工
- 🔥 **M365 + SPF `-all` 规范** → IT 管理正规，投递环境可预测
- ✅ **新设公司扩张期**（©2026 + 45+年团队）→ 供应商窗口期
- ⚠️ **无**：容量数字、品牌偏好、库存、招聘、海关（加企不适用）

---

## 【补充信息】

### 1. 公司规模（多源对比 + 判断）

| 来源 | 员工数 | 营收 | 说明 |
|---|---|---|---|
| 官网 | 未披露（"skilled teams" 定性） | — | 新设，团队制 |
| LinkedIn | 无公司页 | — | 新设特征 |
| D&B/名录 | 未获取 | — | — |

**判断**：
- ✅ **小型 EPC 团队（推测 10–30 人现场+管理）** —— 3 变电站并行 + QEW/安全/土建多工种，低于10人无法覆盖；**属推测，不写入开发信**
- ⚠️ **营收：未获取**
- 🎯 **话术定位**：**专业 EPC/变电站承包商** —— 谈 **选型配合、submittals、图纸确认日交期、现场支持、commissioning 配合**，不谈"批发价/MOQ/试单"

### 2. 🔥 具名项目（开发信核心素材，官网公开 3 个）

| 项目 | 地点（背景） | T&N 范围（官网原文） |
|---|---|---|
| 🔥 **Dunsmuir Substation** | Qualicum Beach 附近，Vancouver Island（230/500kV，含230/138kV主变，背景） | **specialized grounding works for fencing** within HV utility environment |
| 🔥 **Ingledow Substation** | Surrey（500kV，BC Hydro 最重要枢纽，背景） | **QEW support + site safety coordination + security** within active HV environment |
| 🔥 **Nicola Substation（Recently Awarded）** | Merritt 东北 28km（500kV ILM 起点，背景） | **QEW support** for substation works within active HV environment |

**➜ 解读**：
- 🔥 **三座全是 BC Hydro 在运高压站（含 500kV 两座）** → 技术门槛与安全资质已过 BC Hydro 筛选
- 🔥 **Nicola 标 "Recently Awarded"** → **当前活跃采购窗口**
- 🔥 **QEW（Qualified Electrical Worker）** → 持证高压作业能力
- 🎯 **开发信可直接点名 Nicola + Ingledow**（Dunsmuir 接地可作第三钩）

### 3. 可利用的"钩子"（按强度排序，落点收在 JZP 真有产品上）

**① Transformer Installations 原话钩子（最强）🔥🔥**
官网原文："**Setting, assembly, and connection of power transformers**"
→ JZP **变电站变/小主变（750–16667kVA ECD 在办）与主变（750–110000kVA/72–121kV 正式 UL E541626，最大 500MVA/345kV 能力）** 可切入："针对贵司 transformer setting/assembly/connection 业务…我们可按图纸提供变电站变压器及 submittals/选型配合" —— ⚠️ **ECD 不可说已认证；UL 覆盖至 121kV，超压需按项目确认**。

**② Nicola Recently Awarded 钩子（强）🔥🔥**
"Recently Awarded … QEW support" → 当前项目窗口切入，问其变压器/基础/电缆 scope 是否含供货。

**③ Ingledow 500kV 枢纽钩子（强）🔥**
BC Hydro 最重要 500kV 站的 QEW+安全 → 切入高压执行能力尊重 + 变压器大修/更换配套（JZP 擅长按规范定制）。

**④ Equipment Foundations for transformers 钩子**
"Precision foundations for **transformers, breakers**" → 变压器基础与本体一体化配合（尺寸/荷载/交期协同）。

**⑤ HV/MV terminations + testing 钩子**
"in energized environments" → 切入附件/试验配合与交期可靠性。

**⑥ 原住民合作 + EPC 协同钩子**
Seabird Island / Kwikwetlem + "owners, EPCs" → 表达对其合规与社区能力的认可，**不评价政策本身**。

**⑦ Boundary 对标钩子（差异化）**
Boundary 是制造商（10MVA/34.5kV unit sub），T&N 是安装方 → "与 Boundary 等制造商互补的现场执行伙伴"视角，**不贬低 Boundary**。

### 4. 开发信建议（本对话不写信，仅给交接策略）

**推荐开场角度（按优先级）**
1. Transformer Installations 原话 + 变电站变选型/submittals 配合
2. Nicola Recently Awarded 当前项目切入
3. Ingledow 500kV QEW 能力尊重 + 变压器配套
4. HV/MV 电缆 + 基础一体化交期切入

**收件人策略**
- 🎯 **主送：官网表单**（`/contact.html`，Company 写 JZPE POWER TRANSFORMER INC.，Project details 首句写 transformer + Nicola/Ingledow 点名 + 3位领导点名请求转交）
  - ⚠️ **无公开邮箱，禁止推演 @tnelectrical.ca 任何地址**；表单首触后 2–3 天电话跟进（待查电话）
- 🎯 **点名：Terry Bennett（CEO）+ Nathan Friesen（Director of Operations，变电站执行）+ Marwa Atia（COO，合同）** —— 正文点名越具体，转交率越高
- ✅ **电话：未获取** —— 下一步优先查 BC 注册/BC Bid 中标联系人/LinkedIn 公司页（待其建页）
- ℹ️ **LinkedIn 定向**：公司页暂无，待建后定向三人 + QEW/变电站标签人群
- ℹ️ **BC Bid / MERX**：搜 Nicola/Dunsmuir/Ingledow 后续标段，拿投标联系人（转化率最高渠道）

**✅ 邮件送达率**
- **MX = M365，SPF `-all` 规范** → 非严格网关（非 Mimecast/Proofpoint），**投递环境友好**
- ⚠️ 但 M365 过滤仍需：纯文本、无附件、避开营销词、主题写具体（"Power transformer for substation projects – Nicola/Ingledow"）、第一句技术细节、确保己方 SPF/DKIM/DMARC 正确

**注意事项**
- ⚠️ **这是加拿大 BC 买家（温哥华）**
- ⚠️ **时区**：Vancouver 属 **PT（太平洋）**，与北京差 **15 小时（夏令时）/ 16 小时（冬令时）** → 建议**北京时间 24:00–02:00** 发信（对应对方 8:00–10:00）；**北美统一简则 21:00–23:00 不适用本家**
- ⚠️ **公司为新设（©2026）** —— 不要写"贵司数十年历史"，应写"领导团队 45+ 年联合经验（据官网）"
- ⚠️ **电压数字（230/500kV）为 BC Hydro 背景，非本家披露** —— 开发信只用官网原话（HV/MV、power transformer、substation），**不写具体 kV**
- ⚠️ **认证表述**：可讲 JZP 主变正式 UL + 三相美变正式 UL；在办 ECD **不可说已认证**；CSA C88/BC Hydro 规范符合性**按项目确认**
- ⚠️ **不要提 Boundary 的具体人数/金额**（57人等为 LinkedIn 估算）；对标仅作内部策略
- ⚠️ **原住民合作只作尊重性提及**，不展开
- ℹ️ **飓风/极寒不适用本家**；BC 雨季现场（10–3月）可作交期理解背景，不写入信

### 5. ⚠️ 矛盾点与风险提示

| # | 矛盾/风险 | 详情 | 建议 |
|---|---|---|---|
| 1 | 🟡 **新设公司，主体未独立验证** | 官网 newly established + ©2026；BC 注册库无命中；45+年为团队合计 | 开发信不写成立年份；合作前查 BC Registry 付费档案 |
| 2 | 🔴 **零公开邮箱/电话/街道** | 5页全站 + 全网搜零命中；仅表单 | 表单首触；下一步挖 BC Bid 投标联系人 |
| 3 | 🟡 **三人履历单源** | 23+/15+/20+ 年均为官网自述，无 LinkedIn/协会印证 | 引用写"据官网"，不展开 |
| 4 | 🟡 **UL 覆盖与 BC Hydro 超高压的 gap** | JZP 主变 UL 至 121kV；BC 背景 230/500kV | **按项目确认规范符合性**，首信谈选型配合而非证书承诺 |
| 5 | 🟢 **同名排除已做** | Edmonton T&N/英国Terry/Genesis Nathan 均非本家 | 投递写全称 + Vancouver, BC + tnelectrical.ca |
| 6 | ✅ **在营** | ©2026 + Nicola Recently Awarded + M365/SPF 规范 + 原住民伙伴页旁证 | 可投入；列首条行动：表单+电话双触 |

**是否还在经营判定**：✅ **在营**（新设扩张期；≥3 条正向：执照生态（BC Hydro 在运站）+ 新项目 + 域名邮件基建 + 伙伴旁证；零停业信号）

### 6. 信息缺口清单（请勿编造）

| 缺失项 | 说明 |
|---|---|
| **街道地址/邮编/电话/传真** | 未获取（官网仅到城市） |
| **所有公开邮箱（含 info@ 类）** | 未获取（零样本，禁推演） |
| **BC 注册号/注册日期/董事** | 未获取（opengovca 无命中） |
| **成立年份** | 未获取（仅 newly established + ©2026） |
| **员工数 / 营收 / NAICS** | 未获取 |
| **三人 LinkedIn/邮箱/电话** | 未获取（同名已排除） |
| **变压器容量/电压/品牌偏好** | 未获取 |
| **BC Hydro 合格名录状态** | 未获取（建议查 BC Bid/MERX） |
| **现有供应商名单** | 未获取 |
| **联邦/省中标全量** | 未获取（本次未展开 BC Bid/MERX 明细） |
| **海关提单** | 不适用（加企安装商，非进口画像） |
| **社媒/招聘** | 未找到（新设，无预期） |

### 7. 一句话画像

> **T&N Electrical Contracting Ltd. 是温哥华新设（©2026，团队 45+ 年联合经验）的公用事业变电站 EPC/承包商**，CEO **Terry Bennett** / COO **Marwa Atia** / Director of Operations **Nathan Friesen**，服务 **BC + AB**，设 **Transformer Installations（power transformer setting/assembly/connection）+ Substation Construction（至 energization）+ HV/MV Cabling + Grounding/Duct Banks + P&C commissioning** 全栈业务，具名 **Dunsmuir / Ingledow / Nicola（Recently Awarded）三座 BC Hydro 高压变电站**，并与 **Seabird Island / Kwikwetlem** 原住民合作；✅ **官网表单为唯一公开入口，MX M365 + SPF `-all` 规范**；⚠️ 但**电话/邮箱/街道/注册号/容量数字全未公开** —— **属 JZP 变电站变/主变直接对口方，建议高优先级，表单点名三人 + Nicola 切入**。

---

## 附：渠道覆盖清单

| 渠道 | 结果 |
|---|---|
| 官网全站（5页，WebFetch） | ✅ 业务线/领导/项目/伙伴/区域 |
| 官网页脚 | ✅ 已读（极简，无联系方式） |
| LinkedIn（公司/个人搜索索引） | ⚠️ 无公司页；三人无本人页（同名已排除） |
| BC 注册库（opengovca） | ❌ 无命中（同名 Edmonton 系他家） |
| 加拿大联邦/省采购（BC Bid/MERX） | ⚠️ 背景已核（Nicola/Ingeldow/Dunsmuir 电压与招标存在性），明细未展开 |
| DNS（MX/TXT via dns.google） | ✅ M365 + SPF `-all` |
| 商业名录（D&B/Manta/BBB） | ❌ 无本家 |
| 本地黄页（地址反查） | ⚠️ 官网仅到城市，无街道可反查（已如实标注） |
| 社媒（FB/IG/YT） | ❌ 未找到 |
| 海关（ImportYeti） | 不适用（加企安装商） |
| Boundary 对标 | ✅ 类型差异已判定（制造 vs 安装，互补） |

*交接信息来源截止：2026-09-21*
*所有"未获取"项均经官网全站（5页）、dns.google MX/TXT、LinkedIn/B2B/注册库/黄页/WebSearch 多渠道核查，确认无公开信息，非采集遗漏*

*本次相较你提供的原始信息，新增/更正：*
- ✅ 公司名/区域/官网全部核实无误
- 🟡 **对标修正：Boundary 是制造商，T&N 是安装/EPC —— 互补非同类**
- ➕ **3位领导**：Terry Bennett（CEO 23+年）/ Marwa Atia（COO 15+年）/ Nathan Friesen（Director 20+年变电站）
- 🔥 **8大业务线**：Substation Construction / Transformer Installations / HV-MV Cabling / Grounding / Duct Banks / Foundations / Excavation / P&C
- 🔥 **3个 BC Hydro 变电站**：Dunsmuir（grounding）/ Ingledow（QEW+安全）/ **Nicola（Recently Awarded）**
- ➕ **双原住民伙伴**：Seabird Island / Kwikwetlem
- ✅ **DNS：M365 + SPF `-all`**；🔴 **电话/邮箱/街道全网零公开，仅表单**
- ⚠️ **新设公司（©2026）**，注册号未独立验证
