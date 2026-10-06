# batch10 目标客户名单 · 使用说明（2026-10-05）

> 用户指令：「开始找今天的 50 家，10.5 日周一」
> 参数沿用 batch6–9 口径：**A 电气承包商 25 + B 分销商 25**；**加拿大 25 : 美国 25**；**换新来源**。
> 起始编号 **买家 374**（batch9 止于 373）。

> **本名单只做「找客户」，不含任何正文。写信是写开发信 agent 的活。**

---

## 一、名单构成

| 类型 | 家数 | 加拿大 | 美国 |
|---|---|---|---|
| **A 电气承包商 / 工程公司** | **25** | 13 | 12 |
| **B 分销商 / 贸易商** | **25** | 12 | 13 |
| **合计** | **50** | **25** | **25** |

**⭐ 高价值档：43 / 50（86%）** —— **六批最高**（batch9 是 68%）。
口径：官网业务描述原句出现 `substation` / `high voltage` / `transformer` / `transmission`。

---

## 二、🔴 搜索来源（与 batch5–9 **全部不同**）

| 批次 | A 类来源 | B 类来源 |
|---|---|---|
| batch7 | NECA 分会、IEC 分会、ENR Top 600、州执照库、SAM.gov | NAED、AD、IMARK、EW Top 150、Hammond |
| batch8 | CMEQ、NLCA、NETA、MMUA、Centex IEC、ISNetworld | CEDA、poidata.io、electricalindustry.ca、Electrical Advertiser、EASA |
| batch9 | CECA、省级采购门户、PCCA、NUCA、ABC、AGC、RMEL、CanadaBuys、Avetta | NEMRA、MDM Top Distributors、NAW、PEARL、Alberta Electrical League、BC Electrical Association |
| **batch10 本批** | **ECAS/SICA（萨省）**、**CCIB 原住民企业名录**、**NECA 其余分会（如 South Texas Chapter）**、**展会参展商名录**、州级电气承包商协会 | **EUDA 电力公用事业分销商协会**、**T&D World Buyers Guide**、**CTI 名录（Electrical Wholesalers, ON/BC/QC/AB）**、**companylisting.ca NAICS 416110**、**Weidmüller 分销商名录** |

> ⚠️ **来源池确实在收窄**（见 §六）。本批 A 类靠「NECA 其余分会 + 州级协会」补，B 类靠「EUDA + CTI 名录」补。

### 检索方法
**4 路并行 agent**：A 加拿大 / A 美国 / B 加拿大 / B 美国，每路 20 家候选（共 80 → 筛 50）。

---

## 三、🔴 排重结果

| 项 | 结果 |
|---|---|
| 基线 | **`_dedup_baseline_batch10.txt`（1193 个有效关键词）** |
| 候选 | 80 家 |
| **命中基线** | **3 家** → 全部剔除 |
| **命中永久排除名录** | **1 家**（Miami Transformers，制造商）|
| **命中退信域名** | **0 家** ✅ |

### 🔴🔴 本批修了排重工具的 **3 个真缺陷**（都是历史漏网）

| # | 缺陷 | 后果 | 修法 |
|---|---|---|---|
| **1** | **`&` 与空格写法不一致** | 基线存 `turtlehughes`（无空格无 and），查询 `Turtle & Hughes` 归一化成 `turtle and hughes` → **匹配不上** | `check_dedup.py` 增加**多变体比对**（原样 / 去空格 / 去 and 再去空格）+ **去空格前缀**判定 |
| **2** | **括注差异** | 基线存 `Southern Transformer Services (STS)`，查询 `Southern Transformer Services` → 匹配不上（**batch9 自己的客户**） | 基线生成器**追加去括注变体** |
| **3** | **`EECOL / Westburne` 根本不在基线** | 只在 `排重核对表.md` 的**说明文字**里写着「多批次已触达」→ **从未进过数据** | 基线生成器新增 **`CHAINS` 手工清单**（含 EECOL / Westburne / Gescan / Wesco / Rexel / Sonepar / Graybar / Guillevin 等 15 家）|

**修后实测**：`Valard Construction` / `Turtle & Hughes` / `EECOL` / `McNaughton-McKay` / `Van Meter` 全部命中；
`Relectric`（`relectric` ⊂ `belangerelectric` 的结构性假阳性）/ `Power Systems`（通用短语）**不误报** ✅

> 📌 **这是本项目第三次「写在文档里 ≠ 落到数据里」**：
> ① batch7 成交客户没进基线 → ② batch9 3 字母名被长度过滤丢弃 → ③ batch10 连锁只写在说明文字里。
> **凡「已触达/已排除」的判定，必须落到 `_dedup_baseline` 或 `永久排除名录` 的**数据行**，不能只写进文档叙述。**

### 🔴 另一处：batch8 识破的制造商**从未登记**
**`Miami Transformers` / `Core Transformers` / `BCS Switchgear`** 三家在 **batch8 就被检索 agent 识破并剔除**，
但当时**只写在 agent 的「剔除记录」里、从未登记进 `永久排除名录.md`** → **batch10 又被当新候选报上来**。

**已补登 11 家**（Miami Transformers / Triton Transformer / Premier Transformer / Core Transformers /
BCS Switchgear / Multicast / Wismer & Rawlings / IG Power / Friesen / Strong Electric / Raffin /
Hampton Power / AVH Supply）。

---

## 四、本轮剔除（4 家）

| 公司 | 类型 | 剔除依据 |
|---|---|---|
| **McNaughton-McKay Electric Company**（MI）| B | 排重命中基线 v2「mcnaughtonmckay」|
| **Van Meter Inc.**（IA）| B | 排重命中基线 v2「vanmeter」|
| **Turtle & Hughes, Inc.**（NJ）| B | 排重命中基线 v2「turtlehughes」|
| **Miami Transformers**（FL）| B | 🔴 **制造商** —— 官网 *"in-house remanufacturing"* + *"coil rewinding"* ⇒ 在营绕线产线 |

> ⚠️ **A 类加拿大 agent 还人工拦下 `Valard Construction LP`** —— 基线有 `valardconstruction`（无空格），
> 查询带空格 → **脚本当时没命中，靠 agent 人工发现**。这条直接促成了 §三 缺陷 1 的修复。

---

## 五、⚠️ 入选但需投递前注意

| 编号 | 公司 | 风险 |
|---|---|---|
| **379** Stratus E&I / **390** Westfield / **392** Michels / **393** T&D Services / **397** Bel-Air | — | **MX 走 Proofpoint**（`pphosted`）→ 按 batch9 实测，此类域**可能可探测也可能不可**，须实跑控制地址协议 |
| **419** Womack Electric | — | **MX 走 Mimecast**（项目有 PBL 拦截史）→ 投递前复验 |
| **420** M.V. Supply | — | **MX 走 Network Solutions / Vade**（`netsol.xion.oxcs.net`）→ **batch9 实测该网关曾按源 IP 回 `550 Spamhaus PBL`** → 投递前复验 |
| **416** Mountain West Transformer | — | **MX 为转发域**（`_dc-mx.…`）→ 投递前复验 |
| **396** C-Phase Services | — | 🔴 **官网域 `cphaseservices.com` 无 MX**；真实收件域为 **`c-phase.com`**（官网 footer 即 `gwhaley@c-phase.com`）→ **必须用 `c-phase.com`** |
| **414** Power Up Electrical Solutions | — | 同名实体在 **Arlington TX** 亦有登记 → 挖人时须**先确认主体** |
| **380** APG HV Engineering / **387**（工程咨询类）| — | **工程咨询 = 规格制定方，非采购方** → 建议低优先级 / 条件切入 |

---

## 六、🔴 来源池见底的直接证据

| 观察 | 数据 |
|---|---|
| **EUDA（美国电力公用事业分销商协会）全量 9 家** | **全部命中前批基线** → 本批 **0 家可用** |
| **T&D World Buyers Guide** | 目录内多为**制造商**（G&W / PPC / Mica 等），B 类可用者极少 |
| **SupplyForce / The Distribution Group / Network Distribution / AD** | 成员名录**全部 JS 门控或需登录**，无静态可读列表 |
| **EASA 分会/会员名录** | 会员库需登录，且站内明示「member profiles **不得用于营销**」→ **主动放弃抓取** |
| **ThomasNet / GlobalSpec / IndustryNet** | 全站 JS 门控 |
| B 类美国 agent 触达约 **90 家**候选 | 其中 **约 35 家命中前批基线**被剔（**39% 重复率**）|
| **SK/MB 配额** | B 类加拿大 agent **颗粒无收** —— 唯一像的 EECOL 属前批连锁，其余全在基线，变压器实体**全是制造商** |

### batch11 起的来源建议（按可行性排序）
1. ⭐ **NECA 其余分会逐个翻**（100+ 分会，本批只用了 South Texas 一个）
2. ⭐ **州 SoS 按 NAICS 423610 / 238210 逐州筛**（用未用过的州）
3. ⭐ **Surplus Record 经销商目录**（二手/租赁垂直平台）
4. **各州电气承包商协会**（各州独立协会，非 NECA）
5. **展会参展商名录**（PowerGen / DistribuTECH / IEEE PES T&D / RE+）
6. **原住民企业名录**（CCIB / CAMSC）—— 本批验证有效（Nawash / EME 两家）
7. ⚠️ **黄页 / 商会名录**（ThomasNet 等）—— JS 门控，需替代方案

---

## 七、🔴 本批尚未做的（下一环节的工作）

**这 50 家目前只是「公司级线索」**，与 batch9 交付时状态相同。尚未做：

| 缺口 | 说明 |
|---|---|
| **具名决策人** | 全部 50 家均未挖人 |
| **邮箱** | 全部 50 家均未挖邮箱（只有官网域 + MX 已验证）|
| **still_here 在职核验** | 未做 |
| **⓪ 层逐家复核** | 检索 agent 已逐家读官网原文（80/80 = 100%），我另做了排重、MX 独立复核；**未对全部 50 家做二次官网复核** |

> 🔴 **按「信息不够就不发」原则，这 50 家现在都还不能进写信环节。**

### 挖人时可优先用的 A 档来源（batch8/9 已验证）
1. **`cage.report/<CAGE号>`** 的 "Published business email"
2. **行业协会会员名录**（NECA 各分会 / PEARL / 州级协会）—— **常直接暴露「具名+职务+邮箱」**
3. **FMCSA 承运人登记镜像站**（BrokerSnapshot / DataTruck）
4. **魁省 Law 25 隐私政策页** + **CMEQ 持牌企业库**
5. **官网 Careers 页** + **footer mailto（须 `curl | grep`）**

---

## 八、⭐ 信号最强的 8 家（建议先做这批）

| 编号 | 公司 | 类型 | 地区 | 官网原文信号 |
|---|---|---|---|---|
| **411** | **Worldwide Power Distribution** | B | 美国 TX | *"fleet … includes low and medium-voltage **transformers**, distribution equipment…"* |
| **412** | **Southern Electrical Surplus** | B | 美国 TX | 品类页明列 *"**Transformer Buyers** … **Oil Filled** Transformers Buyers ▪ **Substation**"* |
| **422** | **T&R Electric Supply** | B | 美国 SD | *"dependable supplier of **transformers** … to municipalities, REA's, investor-owned utilities"* |
| **423** | **Hernandez Power Sales** | B | 美国 LA | *"Louisiana's trusted source for electrical **transformers** for sale … transformer maintenance services"* |
| **399** | **VCM Solutions** | B | 加拿大 ON | *"**Transformer Rentals and Sales** Servicing Toronto and All of Canada"* |
| **400** | **Power System Solutions** | B | 加拿大 ON | *"sourcing and supply of new and surplus electrical power distribution equipment for **high-voltage (HV)**…"* |
| **378** | **United Power Ltd.** | A | 加拿大 BC | *"**SUBSTATIONS** — over 40 years of continuous experience for 12kV and 69kV installations"* |
| **394** | **American Power, LLC** | A | 美国 AZ | *"complete range of **transmission, substation, and distribution** construction services … to **500kV**"* |

---

## 九、下一步（等你确认）

1. **名单是否可用** —— 要保留 / 剔除哪些？
2. **是否按计划先做 ⭐ 高价值档**（建议先做 §八 的 8 家）
3. **§三 的三处排重工具修复**是否认可（已落码）
4. **§四 的 4 家剔除**是否认可

确认后进入「**挖决策人 + 邮箱**」环节，**起始编号 买家 374**。

---

## 附：文件清单

| 文件 | 内容 |
|---|---|
| **`目标客户清单-batch10.csv`** | **87 行**（50 入选 + 4 剔除 + 32 备选），含「高价值档」「核实状态」列 |
| `名单说明-batch10.md` | 本文件 |
| `_dedup_baseline_batch10.txt` | **1193 词基线**（含连锁已触达 15 家）|
| `batch10_加拿大B类候选_环节①_20261005.md` | B 类加拿大 agent 的完整产出 |
| `_batch10_candidates_raw.txt` | 80 家原始候选，供复核 |
| `scripts/build_baseline.py` | 通用基线生成器（**本批新增 CHAINS + 去括注变体**）|
| `scripts/check_dedup.py` | 排重校验器（**本批新增多变体 + 去空格前缀**）|
| `scripts/gen_batch10_csv.py` | CSV 生成脚本 |
| `永久排除名录.md` | ✅ **本批补登 11 家制造商**（batch8 识破但未登记的）|
