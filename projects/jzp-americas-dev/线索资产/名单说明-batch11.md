# batch11 目标客户名单 · 使用说明（2026-10-06 周二）

> 用户指令：「找今天的 50 家」
> 参数沿用 batch6–10 口径：**A 电气承包商 25 + B 分销商 25**；**加拿大 25 : 美国 25**；**换新来源**。
> 起始编号 **买家 424**（batch10 止于 423）。

> **本名单只做「找客户」，不含任何正文。写信是写开发信 agent 的活。**

---

## 一、名单构成

| 类型 | 家数 | 加拿大 | 美国 |
|---|---|---|---|
| **A 电气承包商 / 工程公司** | **25** | 15 | 10 |
| **B 分销商 / 贸易商** | **25** | 10 | 15 |
| **合计** | **50** | **25** | **25** |

**高价值档：35 / 50（70%）** —— 较 batch10 的 86% 回落。
口径：官网业务描述原句出现 `substation` / `high voltage` / `transformer` / `transmission`。

| 批次 | 高价值档 |
|---|---|
| batch9 | 68% |
| batch10 | 86% |
| **batch11** | **70%** |

**州省分布**：BC 8 ｜ ON 8 ｜ AB 6 ｜ PA 6 ｜ OH 3 ｜ GA 3 ｜ IN 3 ｜ MB 2 ｜ FL 2 ｜ TX 2 ｜ MD / NL / CT / WA / TN / UT / NY 各 1。

> ✅ **地理改善**：batch10 美国侧高度集中在 PA/TX/AZ；本批主动把 A 类美国散到 **PA 5 · OH 2 · GA 2 · MD 1**，加拿大侧把重心从 ON 移到 **BC / AB**。

---

## 二、搜索来源（与 batch5–10 **全部不同**）

| 批次 | A 类来源 | B 类来源 |
|---|---|---|
| batch9 | CECA、省级采购门户、PCCA、NUCA、ABC、AGC、RMEL、CanadaBuys | NEMRA、MDM Top Distributors、NAW、PEARL、Alberta Electrical League |
| batch10 | ECAS/SICA（萨省）、CCIB、NECA South Texas、展会名录 | EUDA、T&D World Buyers Guide、CTI 名录、companylisting.ca、Weidmüller |
| **batch11 本批** | **ECABC（BC 省协会）**、**ECAA（AB 省协会）**、**ECAM（MB 省协会）**、**NECA 各分会（Penn-Del-Jersey / North Central Ohio / Washington DC / Southern Indiana）**、**AECA（Atlanta 分会）** | **Surplus Record 经销商目录**（变压器 / 断路器 / 开关三专业目录）、**CTI 名录其余类别**、定向检索 |

### 检索方法
**4 路并行 agent**：A 加拿大 / A 美国 / B 加拿大 / B 美国，产出 **70 家候选**（A加 20 · A美 20 · B加 10 · B美 20）→ 筛 50。

> ⚠️ **B 类加拿大只找到 10 家**（目标 20）—— 见 §六。

---

## 三、🔴 排重结果

| 项 | 结果 |
|---|---|
| 基线 | **`_dedup_baseline_batch11.txt`（1499 个有效关键词）** |
| 候选 | **70 家** |
| **命中基线** | **0 家** ✅ |
| **命中永久排除名录** | **0 家** ✅ |
| **命中退信域名** | **0 家** ✅ |
| **无 MX** | **0 家** ✅（70/70 全部有 MX，`dig @8.8.8.8` 独立复验）|

### 🔴🔴 本轮修了**基线生成器的真缺陷**（本项目第四次「写在文档里 ≠ 落到数据里」）

**缺陷**：`scripts/build_baseline.py` 的 docstring 明确写着「合并来源：… 4. 永久排除名录.md」，
**但代码里从来没有加载过它**。实测 batch11 首版基线里，**13 家已登记排除的公司完全不在基线**：

```
triton transformer  premier transformer llc  core transformers  bcs switchgear
wismer and rawlings  avh supply  multicast  ig power  friesen  strong electric
raffin  hampton power  rionex energy  crown mountain solutions  jdd electrical supply
```

⇒ 若不修，**这 13 家（全是制造商/中国货源代理）下一批还会被当成新候选报上来** —— 与 batch10 的 Miami Transformers 完全同型。

**修法**：新增 `load_exclusions()`，解析《永久排除名录.md》**标题带 ⛔ 的小节**（一/二/四/五），
**显式跳过 §三「反向陷阱」**（那是防误杀清单，`Beaver Electrical Machinery` / `RS Breakers and Controls` 是**真客户**，误纳入会误杀）。

**修后实测**：基线关键词 1477 → **1499**，永久排除来源条目 **32 → 54**。
✅ 13 家已全部进基线；✅ Beaver / RS Breakers **未被误纳入排除项**。

> 📌 **四次同型事故**：① batch7 成交客户没进基线 ② batch9 三字母名（SGE）被长度过滤丢弃
> ③ batch10 连锁经销商只写在说明文字里 ④ **batch11 永久排除名录只写在 docstring 里**。
> **教训固化：凡「已触达 / 已排除」的判定，必须落到 `_dedup_baseline` 或《永久排除名录》的**数据行**，
> 且**基线生成器必须真的读它**。写在文档叙述里 = 没有。**

### 本轮新登记的永久排除（**+22 家**，已写入《永久排除名录》）

| 类别 | 新增 |
|---|---|
| **变压器/开关柜制造商** | Surplec、MGB、CSL、Duke Electric、JCL Energy、H C Transformer & Switchgear / Oregon Power、American Electric Components、Voltique、Fargo Electric、Allison-Smith、3L2R、Transcanada Transformers & Switchgear |
| **再制造/重绕** | Circuit Breaker Sales NE、National Power Equipment、ARM Camco、III Phase、Switchgear Unlimited、National Switchgear / South East Switchgear（IPS 系）|
| **中国货源→北美** | Canpower Global、Rockwill |
| **已触达连锁体系** | Trydor Industries（Rexel Utility）|

---

## 四、本轮剔除（20 家，仅列主因）

| 公司 | 类型 | 剔除依据 |
|---|---|---|
| **InfraSource LLC**（PA）| A | 🔴 **Quanta Services 全资子公司**（官网 *"a wholly-owned subsidiary of Quanta Services"*）。**Quanta 在 batch9 已发 4 家** → 集团冲突，本批剔除 |
| **The Superior Group**（OH）| A | 🔴 **MasTec 于 2026-07 宣布以 $16.5 亿收购**（*"MasTec to Acquire The Superior Group"*）→ 采购权将上移，且属大型全国承包商 |
| **Matrix NAC**（PA）| A | ⚠️ **Matrix Service Company（NASDAQ: MTRX）子公司** —— 集团结构明确、采购集中，**转「备选」** |
| **JCL Energy / H C Transformer / American Electric Components / Voltique / Fargo / Allison-Smith** | A·B | 制造商（详见 §三 名录）|
| **Circuit Breaker Sales NE / ARM Camco / III Phase / National Switchgear 等** | B | 再制造（详见 §三 名录）|
| **EEC of Virginia** | B | 域 `eec945.com` **无 MX** → 闸门 6 不过 |
| **Brilliant Equipment / Green Industrial / Mayer Electric** | B | 官网 **Cloudflare 拦截**，取不到业务描述原句（按纪律未硬闯）|
| **transwesternelectric.ca / midwaypower.com / completepower.ca** 等 5 家 | A | 无 MX 或 **MX 自指**（无实际邮件主机）—— 含两家高价值线路承包商，按规则仍丢 |
| **Valard Construction / I.B. Abel / New River Electrical / United Electric / Turtle & Hughes / McNaughton-McKay / Van Meter** | A·B | 排重命中基线（已触达）|
| **Casey Equipment / Pump & Motor Works / Optimal Control Systems / A-Line E.D.S. / OK Sales** | B | 类型不符（钢mill设备 / 泵与电机制造 / 面板制造 / 变压器退役回收 / 废金属回收）|

---

## 五、⚠️ 入选但需投递前注意

| 编号 | 公司 | 风险 |
|---|---|---|
| **454** EcoTech NL | — | ⚠️ 主营「新设备供应 + **旧设备翻新再利用**」，含变压器。**无绕线/无生产线**（参照保留先例 Beaver Electrical）⇒ 判为**保留**，但商业模型偏好二手，**新造机切入需话术支撑** |
| **458** Lakeport Power | — | ⭐ 明确 *"supply **brand new** transformers from industry-leading manufacturers, **fabricated to your exact specifications**"* ⇒ **本批 B 类最高优先**。⚠️ 另有 in-house repair/reconditioning 服务线（非制造）|
| **459** CTG Power Systems | — | ⭐ *"We **take title** and stand behind the equipment. Not a broker"* + *"new, used and refurbished"* ⇒ **本批 B 类次高优先**。⚠️ 其主力是 **1–750 MVA 变电站/电力变**，对美定位需用 `E541627` 区间切入 |
| **473** Bruce Electric | — | 🔴 **专营干式变压器**（*"Our specialty is **Dry Type** Transformers"*）⇒ 与我方**液浸**产品线错配（对美不谈干变）→ **低优先 / 条件切入** |
| **472** Safe Power Distributors | — | **MX 走 Proofpoint**（`pphosted`）→ 按 batch9 实测此类域**可能可探测也可能不可**，须实跑控制地址协议 |
| **461** Cowtown Breakers / **464** Romanoff | — | 均为「买 + 卖」双向商，**收购侧属性强**（Romanoff 前身 REMS 曾做绕线，**现主体无在运产线**，按名录判据 3 保留）|
| **470** Sully / **471** Megawatt | — | 定位为**变电站级变压器收购商** ⇒ 客单容量可能超出我方配电级主推区间，切入时**先探其转售渠道是否有配电级需求** |
| **462** Breakers & Beyond / **469** Powerhouse | — | 均为**拆除/回收型**贸易商（*"buying and removing"* / *"decommissioning entire data centers"*）→ 对新造机需求弱，**宜作长期渠道培育** |

### 🔴 本批 B 类的**结构性短板**（必须让用户知道）

**B 类 25 家里约 13 家来自 Surplus Record，属「二手/剩余设备贸易商」，而非「新品库存分销商」。**

- 其商业模型是**低价收旧、翻新转售** → 对我方**新造机**的价格接受度天然偏低
- 好处：它们**有客户网络、有采购决策权、是真实转售渠道**，且多家明示同时经营 **new / new surplus**（Romanoff、Piela、Current Midwest、Midwest Machinery Mart、CTG、Cowtown）
- 代价：**首封转化预期应低于 batch9/10 的常规分销商**

> 根因是**来源池见底**（见 §六），不是选人标准放松。

---

## 六、🔴 来源池见底的直接证据

| 观察 | 数据 |
|---|---|
| **Surplus Record 变压器/断路器/开关三目录** | 美国条目约 **88 家**，逐家核官网后 **≥16 家命中前批基线**（North American Switchgear、Belyea、UTB、Row、Select Equipment、MARS、Transformer Exchange、Alamo、North Coast、Voyten、Denver Breaker、Scott Electric、Schaedler Yesco、RESA/PARC、Lonestar…）→ **重复率 35–40%**，与 batch10 一致 |
| **Surplus Record 加拿大变压器经销商** | 共 14 家，**5 家直接命中基线**（A C Nelson / Surplus Electrical Equipment / Boundary Electric 等），其余多为制造商或翻新商 |
| **B 类加拿大** | **只产出 10 家**（目标 20，达成 50%）。**SK / MB 连续两批为零**（当地变压器实体全为制造商）；**BC / QC 几乎被 batch6–10 吃光**（Westgrid、Dubo、Distributeck、Besco、CAYER、Renegade、Evolt、FEL、SIB 全在基线）|
| **A 类加拿大** | BC 协会名录里**过半是 batch5–10 已触达**（Houle、Black & McDonald、Canem、Mott、Sasco、Western Pacific、Wismer & Rawlings…）；agent 原选的 4 家高价值线路承包商 **Central Island Powerline / Trans Power / Power Up / Trueline 全部撞基线** |
| **ECAO（NECA 加国分会）** | 会员检索 **JS 门控**，未能取到 |
| **PEARL 会员名录** | 无公开名单，且会员多为**再条件/再制造商** |
| **NEMRA / ThomasNet / IQS / GlobalSpec / IndustryNet** | 均 **JS 门控或需登录** |
| **州级电力协会** | Electric League of Western PA 与 Electrical League of Ohio **有可读成员页**，但分销商多为前批已触达或连锁（Wesco / Graybar / Gexpro / CED）|
| **「transformer buyer」类 .com 站** | transformerbuyers.net / padmounttransformerbuyers.com / mjelectricaltransformersbuyers.com 等**疑为同一 SEO 引流网络**，非实体公司 → **下一批勿再碰** |

### batch12 起的来源建议（按可行性排序）
1. ⭐ **州级电力 league 逐个翻**（GA / TN / IN / KY / MO 等，本批只试了 PA / OH 两家）
2. ⭐ **NECA 剩余分会**（100+ 分会，累计只用了 5 个）
3. ⭐ **省 SoS 按 NAICS 238210 逐省筛**（加拿大 BC / AB / SK / MB 未系统做过）
4. **展会参展商名录**（PowerGen / DistribuTECH / IEEE PES T&D / RE+）—— 本批未用
5. **原住民企业名录**（CCIB / CAMSC）—— 本批验证仍有效（Wescan 1 家），可加大力度
6. ⚠️ **Surplus Record 其余专业目录**（MRO-electrical 等）—— 重复率 35–40%，性价比在下降

---

## 七、🔴 本批尚未做的（下一环节的工作）

**这 50 家目前只是「公司级线索」**，与 batch9/10 交付时状态相同。尚未做：

| 缺口 | 说明 |
|---|---|
| **具名决策人** | 全部 50 家均未挖人 |
| **邮箱** | 全部 50 家均未挖邮箱（只有官网域 + MX 已验证）|
| **still_here 在职核验** | 未做 |
| **⓪ 层逐家二次复核** | 检索 agent 已逐家读官网原文（70/70），我另做了排重、MX 独立复核、**8 家高风险家的官网二次抽验**；**未对全部 50 家做二次官网复核** |

> 🔴 **按「信息不够就不发」原则，这 50 家现在都还不能进写信环节。**

### 挖人时可优先用的 A 档来源（batch8/9/10 已验证）
1. **`cage.report/<CAGE号>`** 的 "Published business email"
2. **行业协会会员名录**（NECA 各分会 / PEAC / 州级协会）—— **常直接暴露「具名+职务+邮箱」**
3. **FMCSA 承运人登记镜像站**（BrokerSnapshot / DataTruck）—— batch10 命中 5 家
4. **魁省 Law 25 隐私政策页** + **CMEQ 持牌企业库**
5. **官网 Careers 页** + **footer mailto（须 `curl | grep`）**

---

## 八、⭐ 信号最强的 10 家（建议先做这批）

| 编号 | 公司 | 类型 | 地区 | 官网原文信号 |
|---|---|---|---|---|
| **458** | **Lakeport Power** | B | 加拿大 ON | *"we supply **brand new transformers** from industry-leading manufacturers, **fabricated to your exact specifications**"* |
| **453** | **Carroll Transformer & Switchgear** | B | 加拿大 ON | *"a 'dedicated' **high voltage substation distribution** company… our network of **global supply partners**"* |
| **459** | **CTG Power Systems** | B | 美国 FL | *"global supplier of **new** and reconditioned… **high voltage** electrical equipment… We **take title**… Not a broker"* |
| **424** | **F&M Installations** | A | 加拿大 BC | *"utility electrical infrastructure, delivering **200+ substations**"* |
| **430** | **WSG Energy Services** | A | 加拿大 AB | *"**Turnkey HV Installations**"* |
| **439** | **VEC, Inc.** | A | 美国 OH | *"infrastructure to handle **high-voltage substation construction**"* |
| **452** | **Northern Breaker Group** | B | 加拿大 AB | 三仓网络 + 常备 **REX 变压器**（品类页）|
| **457** | **Argo International** | B | 加拿大 ON | 1952 年创立，**变压器全品类**（Pad Mount / Oil filled / Dry type）|
| **426** | **Tripower Electrical Services** | A | 加拿大 BC | *"**MV and HV cabling**… testing for all Medium Voltage (1kV-100kV) and High-Voltage (100kV+)"* |
| **450** | **E.M.C. Ltd.** | B | 加拿大 ON | *"authorized distributors… **Rex / Marcus / Bemag** transformers"* |

---

## 九、下一步（等你确认）

1. **名单是否可用** —— 要保留 / 剔除哪些？（**建议先看 §五 的两条 🔴**：Bruce Electric 产品错配、B 类二手商占比偏高）
2. **是否按计划先做 ⭐ 高价值档**（建议先做 §八 的 10 家）
3. **§三 的基线生成器修复**是否认可（已落码，`build_baseline.py` 新增 `load_exclusions()`）
4. **§三 新登记的 22 家永久排除**是否认可
5. **§四 剔除的 InfraSource（Quanta 冲突）/ The Superior Group（MasTec 收购）** 是否认可

确认后进入「**挖决策人 + 邮箱**」环节，**起始编号 买家 424**。

---

## 附：文件清单

| 文件 | 内容 |
|---|---|
| **`目标客户清单-batch11.csv`** | **50 行**，含「高价值档」「核实状态」列 |
| `名单说明-batch11.md` | 本文件 |
| `_dedup_baseline_batch11.txt` | **1499 词基线**（含永久排除名录 54 条）|
| `_batch11_candidates_raw.txt` | 70 家原始候选（公司名 + 域名）|
| `_batch11_domains.txt` | 70 个域名（MX 复核用）|
| `_batch11_检索agent任务书.md` | 4 路 agent 的自包含任务书 |
| `_batch11_A_加拿大_候选.md` / `_A_美国_` / `_B_加拿大_` / `_B_美国_` | 4 路 agent 完整产出（含「本轮剔除记录」）|
| `scripts/extract_batch11.py` | 从 4 份 md 抽取候选清单 |
| `scripts/gen_batch11_csv.py` | CSV 生成脚本 |
| `scripts/build_baseline.py` | ✅ **本批修复：新增 `load_exclusions()`，真正读取《永久排除名录》** |
| `永久排除名录.md` | ✅ **本批补登 22 家**（batch11 识破的制造商/再制造/中国货源）|
