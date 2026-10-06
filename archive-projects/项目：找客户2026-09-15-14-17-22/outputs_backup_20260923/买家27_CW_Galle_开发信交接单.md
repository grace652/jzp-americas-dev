# 【买家 27】开发信交接单 — C.W. Galle Contracting, Inc.

> 采集日期：2026-09-21
> 名单来源：你提供的（公司名 + 国家/地区 + 服务区域 + 官网 galleelectric.com，已逐项独立核实）
> ⚠️ 本表严格区分「已验证」与「未获取」，未找到的信息一律标注，不做推断填充
> 🟡 **本家结论前置：家族微型住宅/轻商业电工（208/240/480V），官网只写 buck/boost 小变压器，无配电/电力变压器采购证据 —— 配电主力错位，但用户确认小变压器也可做，可作次级切入，建议中低优先级**
> 🔴 **地址陷阱：官网/MS官方登记地址 2953 Bienville Blvd = UPS Store #3713 邮箱租赁点，且该店已于 2026-04/05 永久关闭 —— 不要寄样品**
> ➕ **用户补充（2026-09-21）：小变压器也做，配电是主力 —— 本单钩子已按此更新，小变压器按干式/隔离变压器切入（均无 UL，需按项目确认）**

---

## ✅ 先核对你提供的信息

| 你提供的 | 核实结果 | 来源 |
|---|---|---|
| **公司名 C.W. Galle Contracting, Inc.** | ✅ **正确** | 官网首页标题 + MSBOC 官方库一致 |
| **国家/地区 美国 (AL/MS Gulf Coast)** | ✅ **正确** | 官网 "Serving Mississippi and Alabama Gulf Coast" |
| **详细地址：服务 MS and AL Gulf Coast (Mobile/Baldwin County一带)** | 🟡 **基本正确但需精确** —— 官网只写 "MS and AL Gulf Coast"，**未写 Mobile/Baldwin County**；官方登记地址为 **2953 Bienville Blvd, Ocean Springs, MS 39564（Jackson County）**，电话另有 **251 区号（AL Mobile 方向）** | 官网 + MSBOC 官方库 |
| **官网 galleelectric.com** | ✅ **正确**（实际为 `www.galleelectric.com`，Weebly 建站，Cloudflare 前端） | 实测 HTTP 200 |

**➜ 修正1：服务区域官网未细化到 Mobile/Baldwin County，不要在开发信中写具体县名**
**➜ 修正2：登记地址是 UPS Store 邮箱地址，且该店已永久关闭（见风险章节）**

---

## 标准字段

**公司全称**
**C.W. Galle Contracting, Inc.**
- 品牌名：**Galle Electric**
- 实体类型：Inc.（MSBOC 登记为 Commercial 承包商）
- ⚠️ **MS 州务卿注册号/注册日期：未获取**（本次未查询到 SOS 直连记录；Wisesearch 镜像显示 Clifford W. Galle 为 Incorporator/Treasurer，状态 Inactive，但为第三方聚合，**未经一手源印证，仅供参考**）
- ℹ️ 官网自述："Founded in Ocean Springs, MS in **1935**" —— **未经注册库印证**，暂按官网自述引用

**国家 + 城市**
美国（USA）+ **密西西比州 Ocean Springs 市（Ocean Springs, MS）**
- **官方登记地址：2953 Bienville Blvd, Ocean Springs, MS 39564** ✅（MSBOC 官方库 + BuildZoom + 官网三源一致，Jackson County）
- 🔴 **地址性质：邮箱租赁点（UPS Store #3713, Seashore Plaza）**，非实体施工场地 —— 见 §矛盾点#1
- 另有历史关联地址（第三方聚合，未经一手源印证）：**9120 Dixie St / 9120 Dixie Street, Ocean Springs, MS 39564**（Wisesearch 高管页）—— ⚠️ **不要用于邮寄**
- 服务区域：**Mississippi and Alabama Gulf Coast**（官网原话）

**联系方式**
- **电话1：(228) 243-5045** ✅（MSBOC 官方库 + 官网 Contact 页 + 首页三源一致；228 = MS Gulf Coast 区号）
- **电话2：(251) 272-9555** ✅（官网首页 + Contact 页明文；251 = AL Mobile 方向区号）
- **传真：未获取**（MSBOC 库 Fax 字段为空）
- **邮箱**：
  - 🟢 **`cwgallecontracting@gmail.com`** —— 官网 Contact 页 Cloudflare 保护邮箱（解码 `data-cfemail=f99a...` 得出）+ 官网 `<meta og:description>` 明文一致，**双位置自印证，A 级来源**
  - 🔴 **无 @galleelectric.com 域邮箱** —— 该域名**无 MX、无 TXT**（dns.google API 实测仅返回 SOA），**无法收信**，故全站用 Gmail 是合理的
- **营业时间：未获取**（官网未公布）
- **官网询价表单**：`/contact.html` 有 Estimate Request 表单（Name/Email/Phone/Comment）

**联系人 / 职位**

| 姓名 | 职位 | 来源与印证数 |
|---|---|---|
| 🔥 **Clifford W. Galle（Cliff Galle）** | **President（MSBOC 登记）/ 第三代 Owner-Operator（官网自述）** | **MSBOC 官方库（Officer表 President + Classification Qualifying Name 双出现）** + 官网 About 页 "third generation owner and operator" + BuildZoom "Owned by: Clifford W. Galle" —— **三源一致** |
| Owen Nordan | Electrician（前员工，2022-11 至 2023-03，仅4个月） | LinkedIn 个人页单源，**未经第二方印证**，仅作规模旁证，不写入开发信 |

- 🎯 **决策人：Cliff Galle 本人** —— 家族微型企业，无专职采购
- ⚠️ **采购负责人、技术负责人：未获取**（官网无 Team 页；B2B 库无有效记录）
- ⚠️ **Cliff Galle 个人邮箱/电话/LinkedIn：未获取**（LinkedIn 搜 "Cliff Galle" 无本人页；同名 Chris Galle/Todd Galle 经核实为宾州金融人士与路易斯安那 Galle's Electric，均非本家）

**邮箱（汇总）**
- 🟢 **主送：`cwgallecontracting@gmail.com`** —— 官网唯一直邮地址，A 级
- 🔴 **无个人邮箱样本** —— B2B 库（LeadSwift 等）返回的均为宾州/加州同名 "Galle Electric"（`jgalle25@yahoo.com`、`brett...`），**与本家无关，禁用**
- 🟡 **命名规则推演：不可做** —— 全站仅 1 个 Gmail 样本，无 `@galleelectric.com` 样本，**无推演依据**

**LinkedIn / 网站**
- **官网**：http://www.galleelectric.com/（⚠️ `https://` 直连失败，必须用 `http://www.`；Weebly 建站 `editmysite.com`，Cloudflare 前端）
  - 页面结构（全站仅4页）：`/`（服务清单）+ `/about.html` + `/photos.html`（42 张现场照片，无文件名情报价值，均为 `img-xxxx` 编号）+ `/contact.html`
  - ✅ **无拦截，curl/WebFetch 均可抓**
  - ⚠️ **页脚无社媒、无执照号、无其他地址**（Weebly 极简站）
- **LinkedIn 公司页：未找到**（搜 "C.W. Galle Contracting" 无公司页；符合 <5 人微企特征）
- **Facebook：`facebook.com/galleelectric/`（Daphne, AL 定位）** —— 搜索仅确认页面存在，**内容需登录，未获取粉丝数/发帖**
- ⚠️ **同名干扰极多，必须严格区分**：
  - ❌ `galle-electric.com`（宾州 Delaware County 住宅电工，610区号）
  - ❌ Galle Electric Inc（加州 Yorba Linda，714区号，已注销）
  - ❌ Galle's Electric Enterprises（路易斯安那 New Orleans，Todd Galle）
  - ✅ **本家唯一标识：`galleelectric.com`（无横杠）+ 228/251 电话 + Ocean Springs, MS**

**买家类型**
**终端承包商（Terminal Contractor）— 住宅 + 轻商业/轻工业微型电工**

- 官网自述："residential, commercial and **light industrial** electrical business"
- ✅ 自有施工（家族经营），按项目采购安装材料，**不转售**
- ✅ 无 Shop/Store/Inventory/仓库/多办公点 —— **非渠道商**（§0.5 判定清单 0/6 命中）
- ✅ 无 "manufacturer/factory" 自述 —— **非同行**
- ⚠️ **非工会证据**：官网无 IBEW/NECA/ABC 表述；MSBOC 无工会字段 —— 判 **非工会（merit shop 倾向），未经协会名录印证**

**需求品类**

**① 低压配电安装与维修（核心，全部 ≤480V）** 🔥 唯一已验证
- 官网原文："Design, repair, and upgrade service entrance **(208v, 240v, 480v)**"
- 配电盘/断路器/插座/开关/吊扇维修、code correction、troubleshooting、emergency services

**② 小型变压器安装（buck/boost，仅此一句）**
- 官网原文："Installation of transformers **(buck/boost)**"
- → 即**小型干式自耦/隔离调压变压器**（解决 208V↔240V 等小压差），**非配电变压器、非电力变压器、非美变/柱上变**，官网无任何 kVA/kV 数值

**③ 发电机与二次电源**
- "Installation and maintenance Secondary Power Systems **(generator, transfer switch, UPS)**" + 住宅 "back up generator power supply"

**④ 电机与控制**
- VFD/VSD 安装维护、MCC/Part Winding/Y-Delta/Autotransformer 电机控制设计、单/三相电机安装维护、制冷/制冰/生产设备电气、燃油输送系统

**⑤ 照明与住宅特色**
- 室内外照明、码头/船吊/附属建筑电气、泳池电气、化粪池研磨系统、烟雾报警、装饰照明、新家电回路

**⑥ 未获取**：中压/高压、变电站、架空线路、变压器容量电压等级、开关柜、箱变、光伏 —— **官网全站无一字提及**

**触达来源**
1. **官网全站抓取**（4页全文：服务清单 208/240/480V + buck/boost + About 1935/三代 + Contact 双电话 + Gmail 解码）—— 主来源
2. **MSBOC 密西西比承包商委员会官方库**（`search.msboc.us`，ContractorID 33054）—— 地址/电话/执照有效期/President 姓名来源
3. **DNS（dns.google API）** —— `galleelectric.com` 无 MX/无 TXT 实测
4. **BuildZoom** —— AL 执照 #05398 旁证 + 地址旁证（⚠️ AL执照页标注 "not verified since 2016"）
5. **WebSearch 交叉** —— UPS Store #3713 关闭新闻（Sun Herald + Ocean Springs Weekly Record + MapQuest/Yahoo Local）确认地址陷阱
6. **LinkedIn 搜索索引** —— 前员工 Owen Nordan 旁证规模；确认无公司页/无老板页
7. **ImportYeti 搜索** —— "C W Galle Contracting" **零结果**（无进口记录）
8. ⚠️ **未能获取**：MS SOS 注册详情、AL 执照官方库直连验证、SAM.gov/UEI、CAGE、USAspending 明细（小微住宅电工，无联邦合同预期）、BBB 本家档案、D&B 本家档案、Facebook 内容（需登录）

**我为什么找他（具体观察，1-2 句）**
**C.W. Galle Contracting, Inc.（品牌 Galle Electric）是 1935 年创立于密西西比 Ocean Springs 的家族三代微型电工企业**，由 **Clifford W. (Cliff) Galle 任 President**，持 **MS 执照 25102-MC（Licensed 至 2026-12-14）** 与 **AL 执照 #05398**，服务 **MS/AL Gulf Coast**，官网服务清单明确写出 **service entrance (208v, 240v, 480v)** 与 **transformers (buck/boost)**，并含发电机/转换开关/UPS、VFD/MCC 电机控制 —— **属低压终端安装方**。

**电压 / 频率 / 认证要求**
- **电压等级：已获取（低压）** 🟢
  - 官网明文：**208V / 240V / 480V**（service entrance）+ **buck/boost 变压器**（小型调压用）
  - ⚠️ **无任何中压/高压数值**（无 4160V/12.47kV/34.5kV/138kV 等），**无 kVA 容量**
  - ℹ️ 美国低压国别常识 120/208/240/480V、**60Hz** —— 属常识，**非该公司披露，勿写入开发信**
- **频率：未获取**（美国 60Hz，出口注意与 50Hz 区别）
- **认证要求：部分获取**
  - ✅ **Licensed and Insured**（官网首页原话）
  - ✅ **MS 25102-MC（Electrical Work）** + **AL #05398（Elec Contractor）**
  - ⚠️ **对供应商产品的认证要求（UL/NEMA/IEEE/DOE）：未获取**（官网无一字）
  - ⚠️ **NEC 版本、县/市 permit 要求：未获取**

**采购信号（按强度排序）** 🔥 本家信号弱，如实写
- 🟡 **弱信号1：官网有 "Installation of transformers (buck/boost)"** —— 证明经手小变压器安装，但**规格与 JZP 主力（配电/电力变压器）不在同一电压/容量带**
- 🟡 **弱信号2：发电机/转换开关/UPS + VFD/MCC 安装维护** —— 有配套电气材料持续需求，但**单体量小**
- 🟡 **弱信号3：MS 执照有效至 2026-12-14（Licensed）** —— 仍在营（见 §7.5 判定）
- ⚪ **无以下信号**：无可买断清单、无库存表、无招聘、无项目案例、无中标公告、无海关进口（ImportYeti 零结果）、无联邦合同预期、无扩建新闻
- **结论：无批量/项目型变压器采购证据**

---

## 【补充信息】

### 1. 公司规模（多源对比 + 判断）

| 来源 | 员工数 | 营收 | 说明 |
|---|---|---|---|
| 官网 | 未披露 | — | "family-owned" |
| LinkedIn | **仅1名前员工可查（Owen Nordan，4个月）**；无公司页 | — | 微企特征 |
| D&B/Manta | **未获取本家档案**（搜到 Gallego Construction 系不同公司，禁用） | — | — |
| BuildZoom | Employees 栏**为空** | Avg Project **为空**，Reviews 0 | 微企特征 |

**判断**：
- ✅ **微型家族承包商（推测 1–5 人）** —— 全站4页极简站、无团队页、无社媒运营、无名录规模数据均指向此
- ⚠️ **员工数/营收：未获取**（无第二方印证，不做数字推测）
- 🎯 **开发信话术定位**：**微型终端** —— 决策链为零（Cliff Galle 一人），但**项目体量小、电压带低**，不适用"框架协议/批量供货"话术

### 2. 客户/项目实证

- **具名项目：无**（官网 Photos 页 42 张均为无标注现场照片，无客户名、无项目描述、无规格）
- **客户证言：无**（官网无 testimonials 板块）
- **合作客户名单：未获取**
- ➜ **开发信无可引用的项目素材**，只能引用其服务清单原文（208/240/480V、buck/boost）

### 3. 可利用的"钩子"（按强度排序，落点收在 JZP 真有产品上）

> ⚠️ 前提：本家电压带（≤480V）与 JZP 配电主力（美变/柱上变/中高压）**错位**，但**用户已确认小变压器也可做**，以下钩子按"小变压器（干式/隔离，⚠️均无 UL，需按项目确认）为主、配电为辅"更新。仍为小批量终端需求，勿报大容量/高压规格。

**① buck/boost 原话钩子（最对口）🔥**
官网原文："Installation of transformers **(buck/boost)**"
→ JZP **小变压器可做（干式/隔离方向）**，可写："注意到贵司提供 buck/boost transformer 安装…我们可提供对应电压比的小容量干式方案及 60Hz 选型支持" —— ⚠️ **干式/隔离均无 UL（见公司 skill 02-产品表 #8/#10），不可承诺 UL，按项目确认**。

**② 480V service entrance 钩子**
官网原文："service entrance **(208v, 240v, 480v)**"
→ 切入低压配电配套（断路器/配电方案不做，只谈变压器侧）："针对贵司 208/240/480V service entrance 升级业务…" —— **点到为止，不假设其电压以外的需求**。

**③ 发电机/ATS/UPS 配套钩子**
官网有 generator/transfer switch/UPS 安装维护 → 若 JZP 箱变/开关柜有小容量配套能力，可作次切入；**无 UL 开关柜证书（见公司 skill），需按项目确认，不可承诺**。

**④ 家族三代 + 1935 年历史钩子（关系型）**
"Founded 1935, third generation" → 表达对长期本地经营的尊重，**不引用营收/规模数字**。

**⑤ Gulf Coast 滨海环境钩子（技术型，需确认）**
Ocean Springs 滨海高湿/盐雾/飓风区 → 若 JZP 产品有防潮/防腐/抗风等级可讲，可作技术切入；**无则不用，勿编造**。

**⑥ 鐘点：无高压钩子** —— 本家无变电站/中压/配电网业务，**禁止写 pad-mount/substation/12.47kV/34.5kV 等词**（会立刻暴露没做功课）。

### 4. 开发信建议（本对话不写信，仅给交接策略）

**推荐开场角度（按优先级）**
1. buck/boost + 208/240/480V 原话切入（前提是有对应小干变规格）
2. 家族长期经营尊重 + 轻商业/住宅升级业务配合
3. 发电机/ATS 配套（次选）

**收件人策略**
- 🎯 **主送：`cwgallecontracting@gmail.com`** —— ✅ 官网唯一邮箱，A 级（meta + Cloudflare 解码双印证）
  - ⚠️ **Gmail 非企业域** —— 首封**纯文本、无附件、无图片**，主题写具体低压技术点（如 "buck/boost transformer for 208/240/480V service work"），**不要写高压产品名**
- 🎯 **决策人：Cliff Galle（President / Owner-Operator）** —— 正文点名 "Mr. Galle" 即可，无个人邮箱，不做推演
- ✅ **电话：(228) 243-5045（MS 主号，MSBOC 官方）**；(251) 272-9555（AL 方向）
  - ⚠️ **官网无营业时间** —— 建议 **北京时间 22:00–24:00** 首呼（对应对方 CT 8:00–10:00），避开早晚
- ℹ️ **官网有 Estimate Request 表单**（`/contact.html`）—— 可作邮件之外的第二触达，但**不要同时多通道轰炸**
- 🔴 **不要邮寄** —— 登记地址是已关闭的 UPS Store 邮箱（见下）

**✅ 邮件送达率**
- **域名无 MX/无 SPF** → **不涉及企业网关**（无 Proofpoint/Mimecast/Barracuda）
- **收件方为 Gmail** → Gmail 过滤可预测，**纯文本+具体技术首句**过虑率最高
- ⚠️ 但 Gmail 对营销词敏感，仍需：无附件、避开 free/discount/best price/click here、确保己方 SPF/DKIM/DMARC 正确

**注意事项**
- ⚠️ **这是美国密西西比/阿拉巴马买家，时区为 CT（Central）**，非 ET —— **北京时间 22:00–24:00 发信**（对应对方 8:00–10:00；冬令时推后1小时）
- ⚠️ **不要提 Mobile/Baldwin County** —— 官网未写，为用户推断
- ⚠️ **不要引用 1935 年以外任何年份/人数/营收** —— 均未印证
- ⚠️ **不要写任何中高压词汇**（pad-mount、substation、12.47kV、138kV、MVA）—— 本家无此业务
- ⚠️ **不要指出其用 Gmail、地址是 UPS Store** —— 显得挑剔
- ⚠️ **严格区分同名公司** —— 投递写全称 "C.W. Galle Contracting, Inc., Ocean Springs, MS"
- ℹ️ **飓风季（6–11月）Gulf Coast 应急维修忙** —— 电话避开灾后高峰，周一早高峰亦避开

### 5. ⚠️ 矛盾点与风险提示

| # | 矛盾/风险 | 详情 | 建议 |
|---|---|---|---|
| 1 | 🔴 **登记地址是已关闭的邮箱租赁点** | 2953 Bienville Blvd = **UPS Store #3713（Seashore Plaza）**；MapQuest/Yahoo Local/Apple Maps 均定位该店；Sun Herald + Ocean Springs Weekly Record 2026-04/05 报道 **该店永久关闭（Permanent Closed）**，客戶郵箱需转址 | **不要寄样品/函件到此地址**；开发信不写地址；电话确认现址 |
| 2 | 🔴 **官网域名无法收信** | dns.google API 实测 `galleelectric.com` **无 MX、无 TXT**（仅 SOA），**无 SPF/DMARC** | 只用 Gmail；**不要推演任何 @galleelectric.com 邮箱** |
| 3 | 🟡 **AL 执照有效性存疑** | BuildZoom AL #05398 显示 Active，但标注 "**not verified since Sep 2016**" | 引用时写"BuildZoom 显示 Active（2016年后未复核）"，建议电话时顺口确认 |
| 4 | 🟡 **1935 年成立无一手源印证** | 仅官网 About 一句话；MS SOS 未直连；MSBOC First Issue 为 **2022-12-14**（系执照首发，非成立） | 开发信引用写"自1935年服务本地（据官网）"，或干脆只写"家族三代经营" |
| 5 | 🟡 **9120 Dixie St 地址冲突** | Wisesearch 高管页写 9120 Dixie St, Ocean Springs，MSBOC/官网用 2953 Bienville Blvd | **以 MSBOC 官方为准**，Dixie 地址不写入开发信 |
| 6 | 🟢 **是否在营：判为在营（证据链见下）** | 执照有效 + 官网可访问 + 电话三源一致 | 可投入电话首触，但**产品错位**是更大风险 |
| 7 | 🔴 **主力产品错位，但小变压器可谈（用户已确认）** | 本家 ≤480V + buck/boost；JZP 配电主力（美变/柱上变/主变）错位，但**小变压器（干式/隔离）可切入** | **中低优先级**；小变压器按项目确认（无 UL），配电主力不硬推 |

**是否还在经营判定（§7.5 七判据）**：
- ✅ 执照：MS 25102-MC **Licensed，过期 2026-12-14**（强在营）
- ✅ 官网：可访问，Weebly 最后构建时间戳 2026（Cloudflare 头 `buildtime=1780945167`，虽为平台时间，仍佐证站点未废弃）
- ✅ 电话：228/251 双号官网+官方库一致
- ✅ 地址反向：UPS Store 关闭是**地址方**关闭，非本家关闭（该楼仍有 PMB 294/132/#285 等多租户）
- ⚠️ 反向：无 LinkedIn 公司页、无招聘、无新闻 —— 符合微企常态，**不作停业证据**
- ➜ **结论：在营。行动：先电话一句话定性电压带（"Do you handle anything above 480V / pad-mount?"），再定是否发信。列为首条行动建议。**

### 6. 信息缺口清单（请勿编造）

| 缺失项 | 说明 |
|---|---|
| **MS SOS 注册号/注册日期/状态** | 未获取（SOS 未直连；聚合站状态冲突，不采信） |
| **AL 执照官方验证** | 未获取（仅 BuildZoom 第三方，2016年后未复核） |
| **员工精确数 / 年营收 / NAICS** | 未获取（无 D&B/LinkedIn JSON-LD；不做推测） |
| **Cliff Galle 个人邮箱/手机/LinkedIn** | 未获取 |
| **具体 kVA / 变压器品牌偏好** | 未获取（官网仅 buck/boost 一词） |
| **现有供应商名单** | 未获取 |
| **联邦合同（SAM/UEI/CAGE/USAspending）** | 未查询到记录（微型住宅电工，无预期；如需投标场景再查） |
| **海关提单** | **ImportYeti 零结果**（符合其不直接进口画像） |
| **BBB 本家档案 / Yelp 评分** | 未找到本家（同址多为其他租户） |
| **Facebook 内容 / 粉丝数** | 未获取（需登录） |
| **营业时间** | 未获取 |
| **UL/NEMA/IEEE 供应商要求** | 未获取 |

### 7. 一句话画像

> **C.W. Galle Contracting, Inc.（Galle Electric）是 1935 年创立于密西西比 Ocean Springs 的家族三代住宅/轻商业微型电工**，Owner **Clifford W. (Cliff) Galle**，持 **MS 25102-MC（至2026-12-14）** 与 **AL #05398**，服务 **MS/AL Gulf Coast**，业务为 **208/240/480V 进户线升级、buck/boost 小变压器安装、发电机/ATS/UPS、VFD/MCC 电机控制及住宅全屋维修**；✅ **主送 `cwgallecontracting@gmail.com`（官网唯一，Gmail）**，电话 **(228) 243-5045 / (251) 272-9555**；🔴 但**登记地址为已永久关闭的 UPS Store 邮箱、无中高压/变电站业务** —— **配电主力错位，但小变压器（干式/隔离，无 UL，按项目确认）可切入，建议中低优先级，电话确认电压带与小变压器规格后再定**。

---

## 附：渠道覆盖清单

| 渠道 | 结果 |
|---|---|
| 官网全站（4页，curl+WebFetch） | ✅ 服务清单/About/Contact/Gmail解码 |
| 官网页脚 | ✅ 已读（极简，无社媒/执照） |
| LinkedIn（公司/个人搜索索引） | ⚠️ 无公司页/无老板页，仅1名前员工 |
| MS MSBOC 官方执照库 | ✅ 地址/电话/有效期/President |
| AL 执照官方库 | ❌ 未直连；⚠️ BuildZoom 第三方旁证 |
| MS SOS 注册库 | ❌ 未获取 |
| SAM.gov / CAGE / USAspending | ❌ 未发现记录（微企，无预期） |
| DNS（MX/TXT via dns.google） | ✅ 无MX/无TXT（关键结论） |
| RDAP/NS | ⚠️ 本环境直连受限，未获取 |
| 商业名录（BuildZoom/D&B/Manta） | ⚠️ 仅 BuildZoom；D&B 无本家 |
| 本地黄页（Yahoo Local/MapQuest/BBB/Yelp） | ✅ 确认 UPS Store 地址陷阱；BBB/Yelp 无本家 |
| 同址集群（opencorpdata/BBB同址） | ✅ 同址多租户（PMB/Suite/#），佐证邮箱租赁属性 |
| 社媒（Facebook） | ⚠️ 仅确认页面存在，内容未获取 |
| 海关（ImportYeti） | ✅ 零结果 |
| 州/联邦采购信号 | ✅ 无（已查 ImportYeti + 官网招聘/项目，联邦库无预期） |

*交接信息来源截止：2026-09-21*
*所有"未获取"项均经官网全站（4页，Weebly）、MSBOC 官方库、dns.google MX/TXT、BuildZoom、LinkedIn 搜索索引、ImportYeti、本地址黄页多渠道核查，确认无公开信息，非采集遗漏*

*本次相较你提供的原始信息，新增/更正：*
- ✅ 公司名/区域/官网全部核实无误
- 🔴 登记地址 2953 Bienville Blvd 系 **UPS Store #3713 邮箱租赁点，且已于 2026-04/05 永久关闭** —— 不可邮寄
- ➕ 主送邮箱解码 **`cwgallecontracting@gmail.com`**（官网 meta + Cloudflare 双印证）；**域名无 MX，禁用 @galleelectric.com 推演**
- ➕ 双电话：**(228) 243-5045**（MSBOC官方）+ **(251) 272-9555**（AL方向）
- ➕ 决策人 **Clifford W. (Cliff) Galle，President，三代经营**
- ➕ 电压带 **208/240/480V + buck/boost**（低压），**无中高压证据**
- ⚠️ **产品错位预警**：与 JZP 配电/主变主力不匹配，建议低优先级
