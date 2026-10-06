# 【买家 213】开发信交接单 — Wholesale Electric Supply Co., Inc.（Texarkana, TX）

> 采集日期：2026-09-29 / 来源：batch6 名单（序号 40，标注「德克萨斯电气批发（Texarkana）」）
> **一句话结论：🔴 名单给的域名 `wholesaleelectric.com` 指向的是另一家公司（Houston 的 Wholesale Electric Supply Company of Houston, Inc. / `wes-hou.com`，1949 年 Rutland 家族创立）。按备注「Texarkana」锁定的正确主体是 `netwes.com` 的 Wholesale Electric Supply Co., Inc.（1947 年 Amos McCulloch 创立）。人已锁到采购一把手 David Dowd（VP of Purchasing），其直邮 `david.dowd@netwes.com` 已 SMTP 三重校验实证命中 —— 本单 A 档通过。**

---

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示(如有)
Wholesale Electric Supply Co., Inc.（Texarkana, TX） | David Dowd | Vice President of Purchasing（采购副总裁） | david.dowd@netwes.com | ✅ 已验证（SMTP RCPT 250，控制地址 + 随机地址 + 对照组三重校验通过） | linkedin.com/in/david-dowd-501a7737 ／ 公司 linkedin.com/company/wholesale-electric-supply-co.-inc | 美国德州 Texarkana，1947 年 Amos McCulloch 创立的电气分销商，70+ 分支覆盖 TX/AR/KS/LA/OK/MO，约 265 人，面向住宅/商业/工业 | 官网 netwes.com（About/Locations/门户页一手）+ LinkedIn 个人页 + allbiz 名录 + SMTP 实证 | 🔴 **同名异体高风险**：`wholesaleelectric.com` 属 Houston 另一家同名公司（`wes-hou.com`），**发信域必须是 `netwes.com`**；官网被 403 拦截，部分字段经第三方取得
```

---

## 二、补充信息（扩展段）

### 标准字段明细
- 国家+城市：美国 **Texas**，Texarkana（总部，德州-阿肯色州界城市）
- 详细地址：**1400 Waterall St, Texarkana, TX 75501**（AllBiz 一手登载）；另有 **803 S Robison Rd, Texarkana, TX 75501**（ContactOut/CIENCE）—— **两址并存，疑为办公+仓储**（**须电话确认实际收件地**）
- 电话：**903-794-3404**（主）；另 903-794-6033、479-646-2000；Fax 501-372-5154
- 邮箱（一手）：**`websupport@netwes.com`**（官网 myaccount 门户页明文，附分机 20061）；`info@netwes.com`（第三方名录）
- LinkedIn：个人 `linkedin.com/in/david-dowd-501a7737`；公司 `linkedin.com/company/wholesale-electric-supply-co.-inc`（2,855 followers，slogan **"Yes, We Can!"**）
- 网站：**`netwes.com`**（⚠️ 本机直抓返回 **403 Forbidden**，含 Googlebot UA 亦被拒 ⇒ 走搜索索引 + 第三方名录）
- 成立日：**1947**。官网 About 标题 *"About Us | **Since 1947**"*；AllBiz：*"Wholesale Electric Supply Co is located in Texarkana, Texas, and was founded in **1947**."*；第三方沿革：*"**Amos McCulloch** founded Wholesale Electric Supply in 1947 in Texarkana, Texas. He and his wife **Carolyn** …"*
- 规模：约 **265 人**（ContactOut）；营收 **$25M–75M**（AllBiz，第三方估算，**正文绝不引用**）
- NAICS：未获取（ISIC 46 / 4752 由 AllBiz 登载，**非 NAICS 一手**）
- 分支网络：**官网自述 PDF 原句** *"We currently have **more than 70 branches** across **Texas, Arkansas, Kansas, Louisiana, Oklahoma, Missouri** and …"*（官网 `WES_Line Sheet.pdf`）；第三方 poidata 记 70 处
- 业务描述原句（官网首页）：*"An electrical supply **distributor** for residential, commercial & industrial with locations across Texas, Arkansas, Louisiana, Oklahoma, …"*；Locations 页：*"Wholesale Electric Supply is a leading **electrical distribution & supplier** in Bowie county and surrounding areas."*
- 组织：**Amos McCulloch Jr — President**（AllBiz 登载，邮箱 `amosm@netwes.com`）
- 其他具名员工（AllBiz 登载，**仅作旁证，未核**）：Martha Whiteman、Kurt Blumfelder、Tracy Tucker、Sabrina Fleming、Rick Spann、Russ Frey、Brandon Gilbey、Doug Graves、Steve Shoup

### 🔴 同名异体核实（任务书未点名，但这是本单最大陷阱）

| | **本单主体（✅ 采用）** | **同名的另一家（❌ 不用）** |
|---|---|---|
| 公司全称 | Wholesale Electric Supply Co., Inc. | Wholesale Electric Supply Company **of Houston**, Inc. |
| 域名 | **`netwes.com`** | **`wholesaleelectric.com`** → 跳转 `wes-hou.com` |
| 城市 | **Texarkana, TX** | Houston, TX |
| 创立 | **1947**，创始人 **Amos McCulloch** | **1949**，创始人 **Clyde & Marjorie Rutland** |
| 规模 | 70+ 分支、265 人、$25M–75M | 13 美国 + 5 国际网点 |
| 域名归属实测 | `netwes.com` A=52.1.23.37 / 34.194.151.116，MX=**Google Workspace** | `wholesaleelectric.com` A=34.174.154.35，MX=`weshou-com0i.mail.protection.outlook.com`（M365） |

> 🔴 **判定依据**：名单**备注明确写「Texarkana」**，且两家的创立年份、创始人、域名互不相干 ⇒ **按备注锁定 Texarkana 主体（`netwes.com`）**。
> ⚠️ **但名单的「官网」栏填的是 `wholesaleelectric.com`（Houston 家）** —— **两者冲突，已按备注裁决，并在下方「矛盾点」显式留痕**。若用户本意是 Houston 那家，需另开一单（其线索：`wes-hou.com/founders/`、`wes-hou.com/personnel/greg-hall/`）。

### 联系人（含 still_here 在职核验）

| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| **David Dowd** | 采购一把手（主送） | **Vice President of Purchasing** | 未获取 | **高**：LinkedIn 现职自述 *"I'm the **Vice President of Purchasing** for Wholesale Electric Supply, where I lead …"*；Salesflow 独立收录其档案，地点标 **Texarkana, Texas** | **低** | linkedin.com/in/david-dowd-501a7737 |
| Amos McCulloch Jr | President（不作首收件） | President | 未获取（创始人之后第二代） | 中：AllBiz 名录登载为 primary contact | 低 | —— |

> 🔴 **still_here 说明**：David Dowd 的**现职公司与地点**由 **LinkedIn 个人页**（现职 = Wholesale Electric Supply，地点 = Texarkana, Texas）+ **Salesflow 独立档案**（Director Of Purchasing, Wholesale Electric Supply **Texarkana**）**双源确认**，且**地点与目标主体一致** ⇒ 排除了「同名异体」误判。**离职风险低**。
> ⚠️ **头衔口径**：LinkedIn 自述 **VP of Purchasing**；Salesflow 标 **Director of Purchasing** ⇒ **以本人在 LinkedIn 的自述头衔为准**（更权威、更新）。

### 邮箱分档（A/B/C）

- **A 档（具名决策人，已验证）**：
  - **`david.dowd@netwes.com`** —— **David Dowd（VP of Purchasing）**
    - 探测：控制地址 `websupport@netwes.com`（官网一手明文）= **250** ✅ ／ 随机地址 `zzz_nonexistent_probe_9987@` = **550** ✅（非 catch-all）／ 对照组 `john.smith@` / `jane.doe@` / `bob.jones@` 全部 **550** ✅ ／ 候选 `david.dowd@netwes.com` = **250** ✅
    - 同轮排除：`ddowd@` 550、`dowd@` 550、`daviddowd@` 550 ⇒ **命名规则实证 = `{first}.{last}@`**
    - ⚠️ 注意本域**并非单一规则**：President 的地址是 `amosm@netwes.com`（`{first}{last-initial}` 形态）⇒ **不要用规则去推别人，只有实测 250 的那个地址可用**（H2）
- **B 档（角色邮箱）**：`websupport@netwes.com`（官网一手，门户支持）；`info@netwes.com`（第三方）—— 备用入口，**不作主送**
- **C 档**：无
- **H6 声明**：**不适用** —— 已取得具名决策人 A 档直邮并实证，非「仅角色邮箱」情形。

> 🔴 **邮箱域 = 官网域**：`netwes.com`（一致）。⚠️ **绝不要按 `wholesaleelectric.com` 拼收件地址**（那是 Houston 那家的域）。

### 我为什么找他

- **他是这家公司的采购一把手，且本人公开自述**：LinkedIn 现职原文 *"I'm the **Vice President of Purchasing** for Wholesale Electric Supply, where I lead …"*，Salesflow 独立档案标其地点为 **Texarkana, Texas** —— **地点与主体完全咬合，排除了同名误判**。这是本批里**唯一一个「职务 + 地点 + 公司」三要素都能对齐的采购一把手**。
- **他的公司是一家 70+ 分支的区域分销商，且总部在 1947 年就落在 Texarkana**：官网自述 PDF 原句 *"We currently have **more than 70 branches** across **Texas, Arkansas, Kansas, Louisiana, Oklahoma, Missouri** …"*。**70 个分支 = 集中采购 + 分散配送的极致形态**，正是「一供多配 / 帮它把库存周转做轻」叙事的天然标的。
- **它自述服务 residential / commercial / industrial 三端**，总部所在 Bowie county 的电力合作社与市政电力都在其覆盖带内 ⇒ **配电变与柱上变有真实落点**。

### 买家类型 / 需求品类

- 买家类型：**A 分销商（区域全品类电气批发，70+ 分支）** —— 判定依据：官网自述 *"electrical supply **distributor** for residential, commercial & industrial"* / *"leading **electrical distribution & supplier**"* ⇒ **⓪ 层通过（非制造商）**
- 需求品类（带结论态）：
  - `三相美变（UL E541627，可直供）` —— 主推
  - `单相柱上变（E544629 仅 ECD 计划函、非证书 ⇒ 条件切入）` —— 其覆盖区含德州东部/阿肯色农村电力合作社带；措辞只能用 *"the project is already underway / in progress"*，**绝不说 certified、绝不出示 ECD Letter 充作证书**
  - `油浸配电变 S11/S13/S20（可直供）`
  - `主变/变电站变（产能可覆盖，UL 区间外，需人工确认）` —— 探询项
- ⚠️ 美国客户：品类只谈**液浸类**（我方 UL 覆盖范围），**不引入其他变压器形态**。
- ⚠️ **未获取其变压器品类是否在架** ⇒ 首封宜落在「贵司 70+ 分支的配电变备货逻辑」，而非直接报价。

### 电压·频率·认证要求

- 电压：未获取（德州配电级常见 12.47/13.8/24.9 kV；**未从一手源取得，勿在信中写具体 kV**）
- 频率：**60 Hz**（美国）⇒ 产品零改造适配
- 认证：美国市场 → **UL**（`UL E541627` 三相液浸配电变，45–5,000 kVA，**正式 CoC**，UL Product iQ 可核验）
- ⛔ 绝不写 `CSA Certified` / `SASO` / `SONCAP`

### 采购信号

1. **70+ 分支 / 6 州覆盖**（TX/AR/KS/LA/OK/MO）⇒ **集中采购体量**，是「一供多配」叙事的硬支撑
2. **1947 年至今的独立家族/本地企业**（创始人 Amos McCulloch，现 President 为 Amos McCulloch Jr）⇒ **非集团成员，决策链短**，不是集团采购降级类型
3. **官网自述服务 residential / commercial / industrial 三端** ⇒ 配电变品类有终端落点
4. **官网设在线账户门户 + APP**（`netwes.com/myaccount`，iTunes 上有其 App）⇒ 数字化程度不低，对供应商 EDI/数据对接有接受度
5. **总部在 Bowie county（德州-阿肯色州界）** ⇒ 覆盖德州东部与阿肯色农村电力合作社带

### 可利用的钩子（按强度排序）

1. **⭐ 70+ 分支的库存延伸逻辑**：集中采购 + 分散配送 ⇒ 最对口的产品叙事
2. **⭐ 1947 年、创始家族仍在位**（Amos McCulloch → Amos McCulloch Jr）：长期主义供应商偏好
3. **"Yes, We Can!" 服务文化**（官网/LinkedIn slogan）：可作呼应点
4. **三端客户结构（住宅/商业/工业）**：容量段跨度大，适合整条配电变线
5. **跨 6 州的州界地理**：德州东部 + 阿肯色/路易斯安那农村电网

### 开发信建议

- **收件人策略**：**主送 `david.dowd@netwes.com`（David Dowd，VP of Purchasing）** —— A 档已验证，可写个性化正文。
  - ⚠️ **一家只发 1 人**：主送 David Dowd。Amos McCulloch Jr（President）**仅作后续升级对象，不另发一封**。
- **语言**：英语。
- **发送时段**：Texarkana TX = **CT（UTC-5，夏令时）**。CT 周二–周四 **09:00–11:00** ⇒ **北京时间 22:00–24:00**。
- **送达配置**：`netwes.com` MX = **Google Workspace**（`aspmx.l.google.com` 等 5 条）。Google Workspace 对 SMTP RCPT 探测**无 M365 那类源 IP 反制**（本轮探测干净通过）。发信仍须 SPF/DKIM/DMARC 三件套齐；首封纯文本、低链接密度。
- **🔴 收件域提醒**：**务必用 `netwes.com`**，⛔ **不要用 `wholesaleelectric.com`**（那会投到 Houston 同名公司）。
- **附件建议**：首封不带 PDF；仅文字说明 UL 号与容量区间。供货记录 PDF **绝不外发**。

### ⚠️ 矛盾点与风险提示

1. 🔴 **名单域名与备注冲突（本单最重要）**：名单「官网」栏 = `wholesaleelectric.com`（**Houston 同名公司**），备注 = **Texarkana**。本单**按备注锁定 `netwes.com`**。**若用户本意是 Houston 那家，本单需作废重开**（Houston 家线索：`wes-hou.com/founders/`、`wes-hou.com/personnel/greg-hall/`、创始人 Clyde & Marjorie Rutland、1949 年、13 美国 + 5 国际网点）。
2. 🔴 **同名公司极多**：除上述两家，第三方库还有 "Wholesale **Electrical** Supply"（`prospeo.io`）等近似主体 ⇒ **任何收件地址都必须先验域名，不能靠公司名匹配**。
3. ⚠️ **官网 403 拦截**：`netwes.com` 对本机 IP（含 Googlebot UA）一律返回 **403 Forbidden**；`web.archive.org` 对该站亦取不到 ⇒ About/Line Sheet 内容**经搜索索引与第三方名录取得**，`websupport@netwes.com` 为官网页面索引中的一手明文。**未硬闯，按规程换渠道。**
4. ⚠️ **两个地址并存**：1400 Waterall St 与 803 S Robison Rd ⇒ **寄样前须电话确认**（事故 E：租赁点/多址风险）。
5. ⚠️ **员工数/营收为第三方估算**（265 人 / $25M–75M）⇒ **正文绝不引用具体数字**。
6. ⚠️ **命名规则非单一**：本域同时存在 `{first}.{last}@`（david.dowd，实证）与 `{first}{last-initial}@`（amosm）⇒ **只可用实测 250 的地址**。

### 信息缺口清单（请勿编造）

- ❌ **NAICS 代码 / 年营收一手数据** —— 未取到
- ❌ **德州州务卿注册信息**（注册号、注册人）—— 未查
- ❌ 常用**变压器容量段 / 现有变压器供应商品牌** —— 未获取
- ❌ **采购部规模与分工**（Dowd 之下是否还有品类买手）—— 未获取
- ❌ 是否有**中国供应商** —— 未获取（海关数据未查）
- ❌ **David Dowd 的任职起始年月** —— 未获取
- ❌ 实际**收件/收货地址**（1400 Waterall vs 803 S Robison 两址并存）—— 未确认
- ❌ 个人 LinkedIn **直链最近活跃时间** —— 未取（本机不可直抓，仅摘要）

### 一句话画像

1947 年 Amos McCulloch 在德州-阿肯色州界开的电气铺子，如今 70+ 分支铺满六个州、还挂着 "Yes, We Can!" 的招牌；采购副总裁 David Dowd 的邮箱就在 `netwes.com` 上——**注意别发到 Houston 那家同名公司去**。

### 渠道覆盖清单（L-1、L0–L7）

| 层 | 结果 | 一句话 |
|---|---|---|
| L-1 锁人 | ✅ | 采购副总裁（LinkedIn 自述 + 地点对齐）+ President 全锁 |
| L0 官网 | ⚠️ | `websupport@netwes.com` 一手明文（经索引）；**直抓 403，Line Sheet PDF 亦取不到** |
| L1 政府一手 | ❌ | 德州州务卿 / 州采购门户未查 |
| L2 命名+DNS | ✅ | MX=**Google Workspace**；探测**干净有效**；规则 `{first}.{last}@` **实证命中**（同域另有 `{first}{l}@` 形态，勿外推） |
| L3 B2B 库 | ⚠️ | AllBiz / ContactOut / RocketReach / Salesflow 旁证（**仅旁证，不作印证**） |
| L4 社媒协会 | ✅ | LinkedIn 个人页（自述头衔 + 地点）+ 公司页 |
| L5 黄页同址 | ✅ | YellowPages / ChamberOfCommerce / ProcessRegister 多址交叉（**两址并存已标注**） |
| L6 电话表单 | ✅ | 903-794-3404 + 官网表单（未拨打） |
| L7 付费 API | ❌ | 未启用 |

---

## 三、发信资格闸门

- **发信资格**：✅ **通过**
- **邮箱档位**：**A（具名决策人 David Dowd，SMTP 已验证）**
- **闸门逐条**：① 邮箱已验证 ✅ ｜ ② 不在拒联名单 ✅ ｜ ③ 离职风险低 + still_here 四栏齐 ✅ ｜ ④ 档位非 C ✅ ｜ ⑤ 公司正常经营 ✅ ｜ ⑥ 「我为什么找他」已写 ✅ ｜ ⑦ 信息缺口清单已写 ✅ ｜ ⑧ 需求品类带结论态 ✅ ｜ ⑨ 该公司仅发 1 人 ✅
- **发送前置（🔴 必做）**：**收件域必须是 `netwes.com`**；**发信前先电话 903-794-3404 确认目标主体确实是 Texarkana 这家**（防同名异体误投 Houston 家）。
