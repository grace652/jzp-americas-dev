# batch9 目标客户名单 · 使用说明（2026-10-02）

> 用户指令：「找今天的 50 家客户，还是经销商和承包商各 25 家」
> 参数沿用 batch6/7/8 口径：**A 电气承包商 25 + B 分销商 25**；**加拿大 25 : 美国 25**；**换新来源**。
> 起始编号 **买家 324**（batch8 止于 323）。

> **本名单只做「找客户」，不含任何正文。写信是写开发信 agent 的活。**

---

## 一、名单构成

| 类型 | 家数 | 加拿大 | 美国 |
|---|---|---|---|
| **A 电气承包商 / 工程公司** | **25** | 13 | 12 |
| **B 分销商 / 贸易商** | **25** | 12 | 13 |
| **合计** | **50** | **25** | **25** |

**⭐ 高价值档：34 / 50（68%）**（口径：官网业务描述原句出现 `substation` / `high voltage` / `transformer` / `transmission`）

### 州省分布

| 加拿大 | 家 | 美国 | 家 |
|---|---|---|---|
| ON | 7 | TX | 4 |
| QC | 6 | CO / FL / MI / NC / OH | 各 2 |
| BC / AB | 各 4 | NE / UT / TN / PA / WA / VA / AZ / AL / GA / SC / NY | 各 1 |
| NS | 2 | | |
| SK / MB | 各 1 | | |

---

## 二、🔴 搜索来源（与 batch5–8 **全部不同**）

| 批次 | A 类来源 | B 类来源 |
|---|---|---|
| batch5 | ECA Ottawa、ECAM(MB) | — |
| batch6 | ECABC(BC)、ECAA(AB) | FSG Top100、shopwholesale.ca |
| batch7 | NECA 分会、IEC 分会、ENR Top 600、州执照库、SAM.gov | NAED、AD、IMARK、EW Top 150、Hammond 名录 |
| batch8 | CMEQ(QC)、NLCA(NL)、NETA、MMUA、Centex IEC、ISNetworld | CEDA、poidata.io、electricalindustry.ca、Electrical Advertiser、EASA |
| **batch9 本批** | **CECA（全国）**、**省级采购门户（MERX / BC Bid / SEAO / Ontario Tenders）**、**PCCA**、**NUCA**、**ABC**、**AGC**、**Southeast Electric Exchange**、**RMEL**、**CanadaBuys**、**Avetta / ComplyWorks** | **NEMRA**、**MDM Top Electrical Distributors**、**NAW**、**PEARL**、**Alberta Electrical League**、**BC Electrical Association**、**EERAC**、省 SoS NAICS 423610/416110 |

> 换来源目的：**降低重复概率**。前四批的协会名录已挖过一遍。
> ⚠️ **来源池正在收窄** —— batch10 起可能需要转向「州/省采购门户逐州扫描」或「展会参展商名录」。

### 检索方法
**4 路并行 agent**：A 加拿大 / A 美国 / B 加拿大 / B 美国，每路 20 家候选（共 80 → 筛 50）。
提示词内嵌：① 产品与 UL 证书号 ② 类型定义 ③ **硬性排除**（制造商/竞品/YAWEI 代理/中国货代/终端户/公用事业本体 + 🆕「三合一」判据）④ 排除名单路径 ⑤ **要求官网业务描述原句** ⑥ 指定新来源 ⑦ 地域配额。

---

## 三、🔴 排重结果

| 项 | 值 |
|---|---|
| 基线 | **`_dedup_baseline_batch9.txt`（941 个有效关键词）** |
| 候选 | 80 家 |
| **命中基线** | **3 家** → 全部剔除（见下）|
| **命中永久排除名录** | **0 家** ✅ |
| **命中退信域名（16 个）** | **0 家** ✅ |

### 🔴🔴 本批最重要的发现：**基线构建器把「成交客户 SGE」漏掉了**（已修）

**现象**：检索 agent 把 **`Société Générale d'Électrotechnique (SGE) / Lignec`（`groupesge.ca`，QC）**
当新线索报上来，且**通过了排重**。而它 **是我方 2023-07 的已成交客户**（2000/2500/3000 kVA 美变）。

**根因**：`build_baseline.py` 的 `norm()` 后过滤 `len(k) < 4` → **3 字母的「sge」被静默丢弃**。
→ **所有 3 字母以内的公司名都不受保护**（SGE 是成交客户，属最危险的一类漏网）。

**已修（两处）**：
1. `build_baseline.py`：阈值 **4 → 3**（基线 923 → **941 词**，`sge` 已入册）
2. `check_dedup.py`：**长度 < 5 的关键词只做「全词匹配」，不做子串匹配** —— 保住短词的同时压掉误报
   （复验：`Allteck Line Contractors` 仍被 `allteck` 全词拦下；`k line` 子串仍命中）

**复验**：`Société Générale d'Électrotechnique (SGE) / Lignec` 现在**正确命中**「成交客户」来源 ✅

### 本轮剔除 3 家

| 公司 | 类型 | 剔除依据 |
|---|---|---|
| **Société Générale d'Électrotechnique (SGE) / Lignec**（QC）| A | 🔴 **我方已成交客户**（2023-07） |
| **TM3 Inc.**（ON）| A | 排重命中基线 v2「tm3」（已触达）|
| **Cache Valley Electric (CVE)**（UT）| A | 排重命中基线 v2「cve」（已触达）|

> ⚠️ **注意 CVE 这一例**：公司全名 "Cache Valley Electric" 与基线关键词 `cve` **不是字面匹配** ——
> 是**缩写 vs 全名**的形态差异。**基线只能拦「同名/近似名」，拦不住缩写**。
> 这类漏网只能靠**人工复核 agent 的「前批已见」提示**（batch8 的 agent 曾明确点名 CVE）。

---

## 四、⚠️ 按项目判例降级 / 需注意的项

### 4.1 降为备选（MX 走 Mimecast，项目有 PBL 拦截史）

| 公司 | 类型 | 说明 |
|---|---|---|
| **Hypower, Inc.**（FL）| A | `hypowerinc.com` MX = `us-smtp-inbound-2.mimecast.com` |
| **Kent Power, Inc.**（MI）| A | `kentpower.com` MX = `us-smtp-inbound-1.mimecast.com` |

→ 已由 **Lee Electrical Construction（NC）** 与 **Interstate Electrical Contractors（CO）** 补位。

### 4.2 入选但需投递前注意

| 编号 | 公司 | 风险 |
|---|---|---|
| **365** | BD Electrical（MI）| 含 *Repairs & Custom Fabrication* 与自有 BaseLine™ 母线/开关柜产品 → **属再售+轻改装**，未见绕线/总装变压器产线 ⇒ 保留；**投递前建议再确认非制造** |
| **357** | FEL（QC）| MX = `fwd1.porkbun.com`（**邮箱转发域**）→ 投递前复验可达性 |
| **359** | Groupe PSE（QC）| MX = `mail.webador.com`（建站商邮箱）→ 属弱域，投递前复验 |
| **352** | IES（ON）| MX 走 Proofpoint（`pphosted`）→ 可探测性待验 |
| **349** | Daltco / **353** Westgrid / **354** Metro Systems / **361** Lonestar / **363** Electrical Now | 官网仅给「经销商/供应」描述，**变压器专营信号弱于 ⭐ 档** → 钩子建议落在「产品线互补」而非「你们卖变压器」 |

---

## 五、🔴 本批尚未做的（下一环节的工作）

**这 50 家目前只是「公司级线索」**，与 batch8 交付时的状态相同。尚未做：

| 缺口 | 说明 |
|---|---|
| **具名决策人** | 全部 50 家均未挖人 |
| **邮箱** | 全部 50 家均未挖邮箱（只有官网域 + MX 已验证）|
| **still_here 在职核验** | 未做 |
| **⓪ 层逐家复核** | 检索 agent 已逐家读官网原文（80/80 = 100%），我另做了排重与 MX 独立复核；**未对全部 50 家做二次官网复核** |

> 🔴 **按「信息不够就不发」原则，这 50 家现在都还不能进写信环节。**

### 挖人时可优先用的 A 档来源（batch8 已验证）
1. **`cage.report/<CAGE号>`** 的 "Published business email"（batch8 命中 6 家）
2. **CMEQ 持牌企业库**（魁省，batch8 命中 2/2）
3. **行业细分协会会员名录**（TECA / NECA 各分会）
4. **官网 Careers 页** + **footer mailto（须 `curl | grep`）**
5. **省/州企业注册库**

---

## 六、⭐ 信号最强的 8 家（建议先做这批）

| 编号 | 公司 | 类型 | 地区 | 官网原文信号 |
|---|---|---|---|---|
| **360** | **CT Sales Ltd.** | B | 加拿大 NS | *"Atlantic Canada's **Power System Specialists**"*；产品线含 **Substation / Transmission / Distribution Solutions** + **Power Transformers** |
| **369** | **Southern Transformer Services** | B | 美国 AL | *"dedicated to providing comprehensive services for electrical **transformers**, including **sales**, field services and the supply of electrical parts"* |
| **353** | **Westgrid Power** | B | 加拿大 BC | *"supplies tested, warrantied **transformers** and switchgear"* + *"We **buy** retired and surplus transformers… from **substation** upgrades"* |
| **354** | **Metro Systems Ltd.** | B | 加拿大 BC | *"giant selection of new and slightly used **transformers**. Available for **purchase or rental**… Sizing from >1KVA up to **1MVA**"* |
| **351** | **Mississauga Electrical Supply** | B | 加拿大 ON | *"stocking the most comprehensive inventory of electrical connectors, **transformers**, and many other components"* |
| **331** | **Entreprise Électrique MJL** | A | 加拿大 QC | *"électricité, automatisation, **haute tension**"*；服务含 *la construction d'un **poste électrique*** |
| **333** | **EGL Construction** | A | 加拿大 QC | *"construction et réfection de **postes électriques**, lignes de **transmission** et distribution"* |
| **344** | **Lee Electrical Construction** | A | 美国 NC | *"manage all aspects of **substation construction and maintenance**"* |

---

## 七、下一步（等你确认）

1. **名单是否可用** —— 要保留 / 剔除哪些？
2. **是否按计划先做 ⭐ 高价值档**（建议先做 §六 的 8 家）
3. **§三 的基线 bug 已修**（阈值 4→3 + 短词只做全词匹配）—— 请确认这个改动方向
4. **§四 的两家 Mimecast 降级**是否认可

确认后进入「**挖决策人 + 邮箱**」环节，**起始编号 买家 324**。

---

## 附：文件清单

| 文件 | 内容 |
|---|---|
| **`目标客户清单-batch9.csv`** | **81 行**（50 入选 + 3 剔除 + 27 备选），含「高价值档」「核实状态」列 |
| `名单说明-batch9.md` | 本文件 |
| `_dedup_baseline_batch9.txt` | **941 词基线（含全部 3 字母关键词）** |
| `_batch9_candidates_raw.txt` | 80 家原始候选，供复核 |
| `scripts/build_baseline.py` | 通用基线生成器（**已修 4→3 阈值 bug**）|
| `scripts/check_dedup.py` | 排重校验器（**已修：短词只做全词匹配**）|
| `scripts/gen_batch9_csv.py` | CSV 生成脚本 |
