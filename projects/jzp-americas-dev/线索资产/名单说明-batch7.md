# batch7 目标客户名单 · 使用说明（2026-09-30）

> 用户指令：「今天的 50 家开始找」
> 参数经确认 = **同 batch6**：A 电气承包商 25 + B 分销商 25；**加拿大 25 : 美国 25**
> 优先级经确认 = **先做 ⭐ 高价值档**
> 来源经确认 = **换新来源**（避开 batch5/6 用过的 ECABC / ECAA / FSG Top100 / shopwholesale）

> **本名单只做「找客户」，不含任何正文。写信是写开发信 agent 的活。**

---

## 一、名单构成

| 类型 | 家数 | 加拿大 | 美国 |
|---|---|---|---|
| **A 电气承包商 / 工程公司** | **25** | 14 | 11 |
| **B 分销商 / 贸易商** | **25** | 11 | 14 |
| **合计** | **50** | **25** | **25** |

### 州省分布

| 州省 | A | B | 小计 |
|---|---|---|---|
| 加拿大 BC | 6 | 2 | 8 |
| 加拿大 ON | 3 | 3 | 6 |
| 加拿大 AB | 4 | 2 | 6 |
| 加拿大 QC | 1 | 3 | 4 |
| 加拿大 MB / SK | 2 | 0 | 2 |
| 美国 TX | 2 | 2 | 4 |
| 美国 FL | 2 | 2 | 4 |
| 美国 MN | 1 | 2 | 3 |
| 美国 AZ / MI | 1 / 0 | 1 / 1 | 4 |
| 美国 其他（NM / WI / CO / GA / PA / NY / DE / SD / ID / IL） | 3 | 5 | 8 |

---

## 二、🔴 搜索来源（与 batch5 / batch6 **完全不同**）

| 类型 | batch5 用过 | batch6 用过 | **batch7 本批** |
|---|---|---|---|
| A 承包商 | ECA Ottawa、ECAM(MB) | ECABC(BC)、ECAA(AB) | **NECA 分会**、**IEC 分会**、**ENR Top 600**、**州执照库**、**SAM.gov**、定向检索 |
| B 分销商 | — | FSG Top100、shopwholesale.ca | **NAED**、**AD**、**IMARK Group**、**Electrical Wholesaling Top 150**、**Hammond 分销商名录**、定向检索 |

> 换来源的目的：**降低重复概率**。上两批的协会名录已挖过一遍。

---

## 三、🔴 排重结果

| 项 | 值 |
|---|---|
| 基线 | `_dedup_keywords_v2.txt`（**398 个有效关键词**，≥4 字符）|
| 本批候选 | 57 家（A 26 + B 31）|
| **命中基线** | **0 家** ✅ |
| **命中永久排除名录** | **0 家** ✅ |
| **命中退信域名（13 个）** | **0 家** ✅ |
| **命中成交客户（17 家）** | ⚠️ **1 家** → 已剔（见下）|

### 🔴 本轮发现基线的一个**真实缺陷**（重要，建议修）

**405 关键词基线里不包含 16 家已成交客户。**

实测：**`Black & McDonald Limited`**（2024-07 成交：6MVA BESS + 20kVA 单相柱上 + 5000kVA 箱变）
**顺利通过了排重**，被检索 agent 当作新候选报上来。原因：

| 基线覆盖来源 | 是否含成交客户 |
|---|---|
| `clients/`（已触达） | ❌ 不含 |
| `交接单/batch1–5`（已建档） | ❌ 不含 |
| `成交客户类型总结.md` 的 16 家外部客户 | ❌ **完全没进基线** |

**这是最危险的一类漏网**：把**已成交客户**当新客户去发冷邮件，
轻则尴尬，重则损害既有客户关系。

**本轮处置**：排重时**额外比对 16 家成交客户 + 1 家我方代理（POWER ELECTRONICS）**，
命中即剔 → Black & McDonald 已剔除。

> ⚠️ **建议**：把 16 家成交客户正式并入 `_dedup_keywords_v2.txt`（→ 414 词），
> 否则**下一批还会再犯**。本轮只在脚本里做了临时比对，**没有改基线文件**（等用户点头）。

---

## 四、✅ 已核实的部分

| 项 | 状态 |
|---|---|
| 排重（398 词基线） | ✅ 0 命中 |
| **成交客户比对（17 家）** | ⚠️ **1 命中** → 已剔 |
| 永久排除名录（45 家） | ✅ 0 命中 |
| 退信域名（13 个） | ✅ 0 命中 |
| **域名 MX 解析** | ✅ **53/57 有 MX**；4 家无 MX → 已剔 |
| 业务类型（⓪ 层反身排除）| ⚠️ **仅按官网业务描述初筛**，未逐家进官网读原文复核 —— 见 §六 |

---

## 五、⚠️ 被剔与转备选的 7 家（诚实标注）

### 剔除 4 家

| 公司 | 类型 | 问题 |
|---|---|---|
| **Black & McDonald Limited**（ON） | A | 🔴 **已成交客户**（2024-07）|
| **Western Line Builders**（NV） | A | **无 MX 记录**（8.8.8.8 与 1.1.1.1 均返回空）→ 收不了信 |
| **Cayer Transformateurs**（QC） | B | 同上 |
| **Helberg Power Supply**（NY） | B | 同上 |

### 转备选 3 家（信号弱，非不合格）

| 公司 | 类型 | 原因 |
|---|---|---|
| **Gross Electric Supply**（OH） | B | 官网只写 `medium voltage products`，**无 transformer 明示** |
| **Chancellor Inc.**（MS） | B | 官网只写 `electrical distribution`，无变压器信号 |
| **Nesco Electric**（MS） | B | 官网只写 `electrical supplier since 1965`，无变压器信号 |

> 若入选的 50 家挖人时掉得多，可启用这 3 家补位，不必再跑一轮搜集。

---

## 六、🔴 本批尚未做的（下一环节的工作）

**这 50 家目前只是「公司级线索」**，与 batch6 交付时的状态相同。尚未做：

| 缺口 | 说明 |
|---|---|
| **⓪ 层反身排除的逐家确认** | 已按官网业务描述初筛，但**未逐家进官网读原文**确认非制造商 / 非竞品 / 非 YAWEI 代理 |
| **具名决策人** | 全部 50 家均未挖人 |
| **邮箱** | 全部 50 家均未挖邮箱（只有官网域）|
| **still_here 在职核验** | 未做 |

> 🔴 **按「信息不够就不发」原则，这 50 家现在都还不能进写信环节。**

---

## 七、⭐ 高价值档（41 / 50 家）

筛选口径：官网业务描述里明确出现 `substation` / `high voltage` / `transformer`。

**41/50 命中** —— 本批质量明显高于 batch6（batch6 是 50 家里约 10 家 ⭐）。

### 信号最强的 7 家（建议先做这批）

| 公司 | 类型 | 地区 | 官网原文信号 |
|---|---|---|---|
| **K-Line Maintenance & Construction** | A | 加拿大 ON | `substation engineering, procurement, and construction`；`Large, complex transformers`；`5kV to 230kV` |
| **Western Pacific Enterprises** | A | 加拿大 BC | `high-voltage substations, switching stations, GIS`；`5kV to 500kV` |
| **Southeast Power Corporation** | A | 美国 FL | `complete turnkey substation construction`；`up to 500kV` |
| **Surplec** | B | 加拿大 QC | `largest inventory of high-voltage transformers and apparatus in Canada` |
| **Transformer Exchange / Transformer Network** | B | 美国 MI / SD | 专营 `power & substation transformers` 买卖租修 |
| **MegaGrid Supply** | B | 美国 FL | `emergency power transformers`、`grid infrastructure solutions` |
| **Lizco Sales & Rentals** | B | 加拿大 ON | `three phase transformers in 75…5000 KVA`；`pad mount transformers` |

---

## 八、下一步（等你确认）

**你说「先找到，我确定之后再进入写信环节」，所以现在停在等你确认。**

请你看完后告诉我：

1. **名单是否可用** —— 要保留 / 剔除哪些？
2. **是否按计划先做 ⭐ 高价值档**（建议先做上表 7 家信号最强的）
3. **§三 的基线缺陷**是否要我把 16 家成交客户**正式并入 `_dedup_keywords_v2.txt`**（推荐做，防下批再犯）

---

## 附：文件清单

| 文件 | 内容 |
|---|---|
| **`目标客户清单-batch7.csv`** | ⭐ **57 行结构化名单**（含「高价值档」「核实状态」列）|
| `名单说明-batch7.md` | 本文件 |
| `_dedup_keywords_v2.txt` | 398 词基线（⚠️ **未含成交客户**，见 §三）|
| `永久排除名录.md` | 已判定不可做的公司 |
| `_bounce_domains.txt` | 退信域名 |
| `成交客户类型总结.md` | **16 家成交客户**（本轮临时比对用，建议并入基线）|
