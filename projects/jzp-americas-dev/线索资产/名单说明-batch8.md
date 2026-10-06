# batch8 目标客户名单 · 使用说明（2026-10-01）

> 用户指令：「开始找今天的 50 家客户」
> 参数沿用 **batch6 / batch7 口径**：A 电气承包商 25 + B 分销商 25；**加拿大 25 : 美国 25**；**换新来源**。
> 起始编号 **买家 274**（batch7 止于 273）。

> **本名单只做「找客户」，不含任何正文。写信是写开发信 agent 的活。**

---

## 一、名单构成

| 类型 | 家数 | 加拿大 | 美国 |
|---|---|---|---|
| **A 电气承包商 / 工程公司** | **25** | 13 | 12 |
| **B 分销商 / 贸易商** | **25** | 12 | 13 |
| **合计** | **50** | **25** | **25** |

**⭐ 高价值档：44 / 50（88%）** —— 明显高于 batch7（41/50 = 82%）与 batch6（约 10/50）。
筛选口径：官网业务描述原句里出现 `substation` / `high voltage` / `transformer` / `transmission`。

### 州省分布

| 加拿大 | 家 | 美国 | 家 |
|---|---|---|---|
| ON | 7 | TX | 4 |
| QC | 6 | PA | 4 |
| BC | 4 | FL | 3 |
| AB | 4 | MI / OH / WA | 各 2 |
| NS | 2 | MN / SC / AL / IL / WI / AZ / CA / ID | 各 1 |
| SK / MB | 各 1 | | |

---

## 二、🔴 搜索来源（与 batch5 / 6 / 7 **全部不同**）

| 批次 | A 类来源 | B 类来源 |
|---|---|---|
| batch5 | ECA Ottawa、ECAM(MB) | — |
| batch6 | ECABC(BC)、ECAA(AB) | FSG Top100、shopwholesale.ca |
| batch7 | NECA 分会、IEC 分会、ENR Top 600、州执照库、SAM.gov | NAED、AD、IMARK、EW Top 150、Hammond 名录 |
| **batch8 本批** | **CMEQ(QC)**、**NLCA(NL)**、**NETA**、**MMUA**、**Centex IEC**、ISNetworld、定向检索 | **CEDA 生态**、**poidata.io 省域批发商报告**、**electricalindustry.ca 本土分销商名单**、**Electrical Advertiser 变压器经销商名录**、**EASA 生态**、定向检索 |

> 换来源目的：**降低重复概率**。前几批的协会名录已挖过一遍。

### 检索方法（供下批复用）
**4 路并行 agent**：A 加拿大 / A 美国 / B 加拿大 / B 美国，每路 20 家候选（共 80 家 → 筛 50 家）。
每个 agent 的提示词**内嵌**：① 我方产品与 UL 证书号 ② 类型定义 ③ **硬性排除**（制造商/竞品/YAWEI 代理/中国货代/终端户/公用事业本体）④ 排除名单路径 ⑤ **要求每家给出「官网业务描述原句」** ⑥ 指定新来源 ⑦ 地域配额。

---

## 三、🔴 排重结果

| 项 | 值 |
|---|---|
| 基线 | **`_dedup_baseline_batch8.txt`（695 个有效关键词）** —— **本批新建** |
| 候选 | 80 家 |
| **命中基线** | **1 家** → Allteck（`k line` 短词**假阳性**，非真重复）|
| **命中永久排除名录** | **0 家** ✅ |
| **命中退信域名（16 个）** | **0 家** ✅ |

### 🔴 本批**已修** batch7 遗留的基线缺陷

batch7 发现「**405 词基线不含 16 家成交客户**」，导致已成交的 Black & McDonald 被当新线索报上来。
本批**已根治** —— 新建 `_dedup_baseline_batch8.txt`，合并四类来源：

| 来源 | 词数 |
|---|---|
| `_dedup_keywords_v2.txt`（已触达 + 已建档 batch1–5） | 398 |
| batch6 名单（50 家） | 127 |
| batch7 名单（50 家） | 155 |
| **成交客户 16 家 + 我方代理 POWER ELECTRONICS** | **15** |
| **去重后合计** | **695** |

> ⚠️ **未修改** `_dedup_keywords_v2.txt`（保持原样，等用户点头后再正式合并）。
> 生成脚本：`scripts/build_baseline_batch8.py`；校验脚本：`scripts/check_dedup.py`（已收紧子串规则）。

---

## 四、⛔ 本轮剔除（2 家，均已取证）

| 公司 | 类型 | 排除依据（官网原句） |
|---|---|---|
| **IronCore Global Resources Inc.**（BC · Vancouver） | B | 官网自称 *"Transformer Solution Provider and **Distributor**"*，却同时写 *"**Strong production capacity** and organized supply support"*、*"Our transformer **design team**"*；产品跨度 **750kV/720MVA 电力变** 到 **HDPE 管材**（自称 *"A second product line"*）；**无自有工厂地址**。⇒ **典型「中国货源→北美」通道**，与 Rionex / Crown Mountain / JDD 判例同型 |
| **Choice Electrical Supply Co.**（SK · Regina） | B | 官网自述 *"Choice Electrical Supply is **a division of Guillevin**"*，而 `guillevin` **已在排重基线内** ⇒ **同集团主体重复**（非独立法人）|

> 📌 **建议登记进 `线索资产/永久排除名录.md`**（本轮未改该文件，等用户确认）。

---

## 五、⚠️ 入选但需注意的 4 家（诚实标注）

| 编号 | 公司 | 风险点 | 处置 |
|---|---|---|---|
| **307** | SIB Électrique（QC） | 官网有 *"Nous **fabriquons** sur mesure"* 服务线 | ✅ **保留** —— 核实为**开关柜 / 控制柜（CCM / répartiteurs / centres de distribution）**装配，**与变压器互补不重合**，符合名录 §1.2「产品线互补⇒保留」 |
| **308** | Ligne STE（QC） | **跨类**：既做变压器销售/租赁，也做线路施工 | ⚠️ **保留，归 B 类**（以变压器销售/租赁为主）。**供应商来源待核** —— 挖人时需确认其是否已有中国供应商 |
| **309** | Location Power（QC） | 邮件域为 **`powerrentals.ca`**（非官网域） | ⚠️ **保留**，投递时收件域用 `powerrentals.ca` |
| **306** | Deep Electrical Supply（AB） | 原选 Bernie's Electric 因 **MX 走 Mimecast**（项目有 PBL 拦截史）降为备选，由其补位 | ✅ 已替补，Google MX |

### 另有 3 家 MX 为**自指向 / 转发域**，投递前需复验
`pmppowerline.ca`（MX 自指）｜`edisonelectricalsurplus.com`（MX 自指）｜`transconofmichigan.com`（`_dc-mx.…` 转发域）

---

## 六、🔴 本批尚未做的（下一环节的工作）

**这 50 家目前只是「公司级线索」**，与 batch7 交付时的状态相同。尚未做：

| 缺口 | 说明 |
|---|---|
| **具名决策人** | 全部 50 家均未挖人 |
| **邮箱** | 全部 50 家均未挖邮箱（只有官网域 + MX 已验证）|
| **still_here 在职核验** | 未做 |
| **⓪ 层逐家官网复核** | 检索 agent 已逐家读官网原文（80/80 = 100%），**我另做了高风险项抽查**（IronCore / SIB / Ligne STE）；但**未对全部 50 家做二次独立复核** |

> 🔴 **按「信息不够就不发」原则，这 50 家现在都还不能进写信环节。**

### 好消息：本批质量高，A 档挖人有更好抓手
batch7 的经验：**小微/家族企业官网只挂 `info@`，想要 A 档必须离开官网**。
本批 **B 类里有 13 家是「变压器专营经销商 / 二手翻新商」** —— 这类公司
**决策人极少（往往 owner 直接管采购）、且常主动公开联系人**，A 档命中率预期高于前几批。

---

## 七、⭐ 信号最强的 8 家（建议先做这批）

| 编号 | 公司 | 类型 | 地区 | 官网原文信号 |
|---|---|---|---|---|
| **318** | **Belyea Company** | B | 美国 PA | *"outdoor **oil filled substation-type**, compartmentalized **padmount** (NEMA 3R)… 100 KVA through 100,000 KVA"* —— **本批最对口，与 E541627 区间几乎重合** |
| **311** | **Transformers, Now!** | B | 美国 TX | *"1kVA **pole mounts** to 40/50mVA **substations**"*；且明示 *"we **don't** directly remanufacture"* |
| **276** | **Site Plus Electrical** | A | 加拿大 ON | *"one South Western Ontario's largest **transformer installation** service providers"* |
| **308** | **Ligne STE** | B | 加拿大 QC | 明确 **sur socle（美变）/ sur poteau（柱上变）/ à l'huile（油浸）** 销售+租赁 |
| **303** | **AC Nelson Electrical** | B | 加拿大 BC | *"Our inventory includes… **transformers**, switchgear, panels…"* |
| **283** | **CIMA+** | A | 加拿大 QC | *"over 40 years… **substation design and construction**… low-voltage to **735 kV**"* |
| **292** | **SCS Transmission Services** | A | 美国 SC | *"substation construction to **transformer assembly and maintenance**"* |
| **295** | **Wright's Electric** | A | 美国 PA | *"specialized… **High Voltage** electrical contractor"*；服务含 *"Sub-Station Construction"* 与 *"**Transformer Maintenance & Replacement**"* |

---

## 八、下一步（等你确认）

请你看完后告诉我：

1. **名单是否可用** —— 要保留 / 剔除哪些？
2. **是否按计划先做 ⭐ 高价值档**（建议先做 §七 的 8 家）
3. **§四 的 2 家剔除**（IronCore / Choice）是否要正式登记进 `永久排除名录.md`
4. **§三 的基线缺陷**是否要把 16 家成交客户**正式并入 `_dedup_keywords_v2.txt`**（推荐做，防下批再犯）

确认后进入「**挖决策人 + 邮箱**」环节，**起始编号 买家 274**。

---

## 附：文件清单

| 文件 | 内容 |
|---|---|
| **`目标客户清单-batch8.csv`** | **80 行**（50 家入选 + 2 家剔除 + 28 家备选），含「高价值档」「核实状态」列 |
| `名单说明-batch8.md` | 本文件 |
| `_dedup_baseline_batch8.txt` | **695 词基线（本批新建，含成交客户）** |
| `_batch8_candidates_raw.txt` | 80 家原始候选（公司名 + 域），供复核 |
| `scripts/build_baseline_batch8.py` | 基线生成脚本 |
| `scripts/check_dedup.py` | 排重校验脚本（含短词假阳性说明）|
| `scripts/gen_batch8_csv.py` | CSV 生成脚本 |
| `永久排除名录.md` | 已判定不可做的公司（⚠️ 本批新增 2 家待登记）|
| `_bounce_domains.txt` / `退信黑名单.json` | 退信域名（16 个）|
