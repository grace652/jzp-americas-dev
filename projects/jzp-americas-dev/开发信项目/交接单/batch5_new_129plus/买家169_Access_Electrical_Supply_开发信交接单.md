# 买家 169 — Access Electrical Supply Ltd. 开发信交接单

> **批次**：batch5_new_129plus（第六批 · 加拿大 B 类分销商）
> **CSV 序号**：48
> **买家编号**：169
> **建档日期**：2026-09-28
> **结论**：✅ **合格（可写）** —— 5 名具名第一方人员 + 5 个第一方邮箱；但 ⚠️ **域名 catch-all，SMTP 不可验证**，邮箱证据等级为 **B（第一方官网公示）**

---

## 一、身份与定性（六层过筛）

| 层级 | 结论 |
|---|---|
| ⓪ 反身排除 | ✅ **PASS** —— 独立电气分销商 / 批发商，非制造商、非竞品、非制造代表 |
| ① 类型匹配 | ✅ **B 类 分销商/贸易商** —— 「Electrical Supply」「Distributors' Solution」自我定位 |
| ② 地域 | ✅ 加拿大 · MB（总部）+ ON（分公司） |
| ③ 业务相关性 | ✅ 明确销售 transformers（见 §三） |
| ④ 规模 | ⚠️ 小微 —— 2023-07-20 成立，**3 年**，2 个实体分支 |
| ⑤ 可达性 | ⚠️ 邮箱可达（catch-all 必达），**但不可验证** |
| ⑥ 决策人 | ✅ 已获 5 名具名人员（含 Owner） |

### ⓪ 层判定依据（逐条）

1. **非制造商**：官网 `/about` 自述为 *"a trendsetting Electrical Supply shop"*、*"a business made up of innovators and forward-thinkers"*；`/products` 全为**转售品类**（boxes、fittings、devices、fuses、switches、circuit breakers、transformers、LED、NMD90/AC90/RW90 电缆）。**无任何制造设施、产线、工厂描述。**
2. **非竞品**：`/about` 文本中 *"becoming early adopters of the latest manufacturing techniques and technologies"* 系**营销套话**（Wix 模板通用文案），与其零制造资产的实体事实矛盾。**不作为制造证据**，与 Shermco「Manufacturing 页面名 ≠ 制造商」同类处理。
3. **非制造代表（rep firm）**：官网**未列任何代理品牌清单**，未出现 "manufacturers representative" / "agency" 字样。与 Jebco（代理 Hammond Power Solutions）、AESCO（明示 rep）**性质不同**，**无渠道冲突标记**。
4. **非我方代理/据点**：地址非 `1243 N Roseburg Ct, Visalia, CA 93291`；名称与 POWER ELECTRONICS 无关。

---

## 二、公司基本档案

| 字段 | 值 | 来源 |
|---|---|---|
| 公司全称 | Access Electrical Supply Ltd. | 官网 / BBB |
| 联邦公司号 | **15215307** | Corporations Canada（经 opengovca / federalcorporation.ca 索引） |
| 注册地址（法定） | 2200-201 Portage Avenue, Winnipeg MB R3B 3L3 | Corporations Canada |
| 成立 / 注册日期 | **2023-07-20** | BBB + Corporations Canada（双源一致） |
| 实体类型 | Corporation（联邦） | BBB |
| 经营年限 | **3 年**（BBB 自 2025-10 建档，2026-01-01 起 BBB 认证，评级 **A+**） | BBB |
| 官网 | `accesselectricalsupply.ca` | — |
| 建站平台 | **Wix**（`parastorage.com` 资源、`filesusr.com` 静态域） | 技术指纹 |
| 总部地址 | **1338 Clifton Street, Winnipeg, MB R3E 2V2** | 官网 / BBB（双源一致） |
| 总部电话 | **204-975-1446** / **431-788-5152** | 官网 Winnipeg 页 + BBB |
| 多伦多分公司 | **2779 Herald Road, Sharon, ON L0G 1V0** · **705-881-1961** | 官网 Toronto 页 |
| 待开分支 | Edmonton（Opening Soon）、Calgary（Coming Soon）、Saskatoon（Coming Soon）、Vancouver/BC（Opening Soon，但已给出 BC 联系人） | 官网 branchlocations |
| 营业时间 | 周一–周五 08:00–17:00 | 官网 |
| 业务类别（BBB） | Electric Equipment Manufacturers · Electrical · Light Fixture Parts · Non-Electric Wire and Cable | BBB |

> ⚠️ **BBB 将其归类为 "Electric Equipment Manufacturers" —— 这是 BBB 的分类目录标签，非制造事实。** 已在 §一 ⓪ 层排除。

---

## 三、产品与业务定位（钩子素材 · 逐字引用）

### 3.1 官网原文（`/`）

> *"Access Electrical Supply — Electrical Distributors' Solution"*
> *"Our promise to you is that we provide cost saving solutions that transform your business. We envision a Canada where electrical solutions are not only reliable but also sustainable. By offering a comprehensive range of products from leading manufacturers, we aim to play a pivotal role in the growth and success of projects, both large and small, that shape the landscape of our nation."*
> *"Every item sold at Access Electrical undergoes rigorous testing and meets or exceeds industry standards."*

### 3.2 产品线（`/products` 逐字）

> *"Our electrical equipment sales service offers a comprehensive range of high-quality products, including **electrical boxes, fittings, devices, fuses, switches, circuit breakers, transformers, and more**. We provide reliable and efficient solutions to meet the diverse needs of our customers."*
> *"We provide different specifications of **NMD90, AC90, RW90** and other different cable products."*
> *"We offer a wide selection of energy-efficient **LED lights, fixtures, and accessories** for residential, commercial, and industrial applications."*

### 3.3 定位解读（供写信环节参考，**不代写正文**）

| 观察 | 说明 |
|---|---|
| ✅ **transformers 明确在售** | 官网产品线第一段即列出 `transformers`，属**在盘品类**，切入点成立 |
| ⚠️ **未列变压器规格/品牌** | 未出现 kVA 区间、未列变压器品牌（Schneider/Square D/Eaton/Hammond 等均未出现）→ **规格匹配度未知，首封宜先确认其在盘变压器的容量段与来源** |
| ⚠️ **偏「配货型」分销商** | 主营 wire/cable/boxes/devices/breakers/lighting，「transformers」排在断路器之后，**属长尾品类而非主营** |
| ⚠️ **规模极小、成立仅 3 年** | 单次采购量预期低；Edmonton/Calgary/Saskatoon 均"Coming Soon"，**尚在铺网点阶段** |
| ✅ **加拿大本地身份** | 明确 *"a Canada where electrical solutions…"*，**CSA/IEEE 标准体系可直接套用** |
| ⚠️ **"from leading manufacturers"** | 暗示其货源为品牌制造厂/一级代理，**我方属「非品牌替代货源」定位**，需以价格/交期/认证切入 |

---

## 四、决策人清单（★ 核心产出）

**来源**：全部来自**公司自有官网分公司页面**（Winnipeg 页 / Toronto 页 / BC 页）—— 属**第一方公示**，为最高可信级别来源（H5 满足）。

| # | 姓名 | 岗位/角色 | 邮箱 | 所在 | 证据 | 等级 |
|---|---|---|---|---|---|---|
| 1 | **Danny Lao** | **Owner（业主）** | `Danny@accesselectricalsupply.ca` | Winnipeg, MB | ①BBB *"Business Management: Danny Lao, Owner"*；②BBB *"Principal Contacts: Danny Lao, Owner"*；③官网 Winnipeg 页员工名录 | **★★★ 三源** |
| 2 | **Jon Buccini** | Electrical / Lighting Sales Specialist（销售） | `Jonb@accesselectricalsupply.ca` | Winnipeg, MB | ①官网 Winnipeg 页；②LinkedIn `ca.linkedin.com/in/jon-buccini-851709114`（电力/照明销售方向） | **★★ 双源** |
| 3 | **Nicholas Goresky** | 员工（岗位未公示） | `Nick@accesselectricalsupply.ca` | Winnipeg, MB | ①官网 Winnipeg 页 | **★ 单源（第一方）** |
| 4 | **Scott Rawson** | **Toronto / Ontario 分支负责人** | `Scotty@accesselectricalsupply.ca` | Sharon, ON | ①官网 Toronto 页员工名录（该页仅列 2 人，Scott 列首位） | **★ 单源（第一方）** |
| 5 | **Lisa Rawson** | 员工（与 Scott 同址，疑家族成员） | `Lisa@accesselectricalsupply.ca` | Sharon, ON | ①官网 Toronto 页 | **★ 单源（第一方）** |
| 6 | **Mark**（姓未公示） | **BC 分支负责人** | `Mark@accesselectricalsupply.ca` | BC（地址 TBD） | ①官网 Vancouver 页；电话 +1 (236) 889-4416 | **★ 单源（第一方）** |
| — | （通用） | 一般咨询 | `Requests@accesselectricalsupply.ca` | — | 官网 Vancouver 页 | 角色邮箱 |
| — | （通用） | 总部 | `info@accesselectricalsupply.ca` | Winnipeg | 官网全站页脚 | **C/B 级角色邮箱** |

### 4.1 关键人物深挖

**Danny Lao — Owner**（最高优先级）
- 三重来源确认：BBB「Business Management」+ BBB「Principal Contacts」+ 官网员工名录
- BBB 档案显示其为**唯一 Principal Contact 与唯一 Customer Contact**，即**单人决策结构**
- ⚠️ 存在同名干扰：LinkedIn 另有 `Danny lao — EECOL Electric`（`ca.linkedin.com/in/danny-lao-ab66ba39`）。EECOL 为加拿大大型电气分销商，与本公司 2023 年成立的时间线**不能排除「EECOL 出身、自立门户」的职业路径**，但**无法证实为同一人**，**不做推断**。
- 官网 Winnipeg 页邮箱前缀为 `Danny@`（非 `d.lao@`），**属老板直用名式邮箱**。

**Scott Rawson / Lisa Rawson — Toronto 分支**（第二优先级）
- 官网 Toronto 页标题为 *"Nourishing Electrical Contractors!"*，联系人仅列 Scott 与 Lisa 二人，**共用 Rawson 姓氏**，**强提示家族经营**。
- `Scotty@` 为昵称式前缀（非 `s.rawson@`），与 Winnipeg 的 `Danny@` 同类，**均为「名式」前缀** → 印证该域名**内部命名规则为 `{FirstName}@`**。

**命名规则推断（重要）**
> 本公司邮箱规则 = **`{FirstName}@accesselectricalsupply.ca`**（首字母大写或小写均可，多数在官网写作首字母大写）
> 佐证：`Danny@`、`Jonb@`（Jon B.）、`Nick@`、`Scotty@`、`Lisa@`、`Mark@`
> ⚠️ **`Jonb@` 是唯一例外**，为 `{First}{LastInitial}@` → 规则非绝对，**不可外推新建地址**（H2：绝不杜撰邮箱）。

---

## 五、邮箱验证（SMTP 三点式探测）

### 5.1 DNS 记录

| 项 | 值 |
|---|---|
| MX | `0 accesselectricalsupply-ca.mail.protection.outlook.com`（**Microsoft 365 / Exchange Online**） |
| SPF | `v=spf1 include:spf.protection.outlook.com -all`（**硬失败**） |
| DMARC | **无记录**（查询 `_dmarc.accesselectricalsupply.ca` 返回空） |
| 域名 A | `185.230.63.107`（Wix 托管） |

### 5.2 探测结果（2026-09-28 实测）

**探测协议**：`MAIL FROM: ian@jiezougroup.com` → 逐地址 `RCPT TO` → **随机对照地址必须 550 方可采信**

```
EHLO ok: SIZE=157286400
MAIL FROM: 250 2.1.0 Sender OK
──────────────────────────────────────────────────────────────
  250  info@accesselectricalsupply.ca          :: 2.1.5 Recipient OK
  250  Danny@accesselectricalsupply.ca         :: 2.1.5 Recipient OK
  250  Jonb@accesselectricalsupply.ca          :: 2.1.5 Recipient OK
  250  Nick@accesselectricalsupply.ca          :: 2.1.5 Recipient OK
  250  Scotty@accesselectricalsupply.ca        :: 2.1.5 Recipient OK
  250  Lisa@accesselectricalsupply.ca          :: 2.1.5 Recipient OK
  250  Mark@accesselectricalsupply.ca          :: 2.1.5 Recipient OK
  250  Requests@accesselectricalsupply.ca      :: 2.1.5 Recipient OK
──────────────────────────────────────────────────────────────
  250  ds4976um4l@accesselectricalsupply.ca    :: 2.1.5 Recipient OK   ← 🔴 随机对照
  250  h61dy6beed@accesselectricalsupply.ca    :: 2.1.5 Recipient OK   ← 🔴 随机对照
```

### 5.3 判定

| 项 | 结论 |
|---|---|
| 服务类型 | **全域 catch-all**（catch-all）—— 两个随机地址均返回 250 |
| 三点式采信条件 | ❌ **不成立**（需 对照 250 + 随机 550 + 候选 250） |
| **SMTP 通道结论** | 🔴 **完全失效 —— 无法用 SMTP 验证任何地址存在性** |
| **邮箱证据等级** | **B 级（第一方官网公示）** —— 非 A 级（A 级需 SMTP 实证） |
| 投递可行性 | ✅ **可达性高** —— catch-all 意味着**发什么都会进**，`Danny@` 等公示地址**必达** |
| 风险 | ⚠️ **不可验证 ≠ 不可用**。5 个具名地址均抄自官网原文，**存在即投递成功**；但**若官网地址为笔误或已停用，无 SMTP 兜底可发现** → **首封后须按退信监控确认** |

> **本档性质**：`catch-all` 属 skill《渠道状态清单》**第 (a) 类 Void**（与 Jebco、Beaver Electrical 同类）。
> 但**与 Jebco/Beaver 的关键差异**：本案**已在第一方官网直接读到具名邮箱**，因此**无需依赖 SMTP 猜测**，B 级证据足以交付。

---

## 六、六层过筛汇总与交付判定

| 检查项 | 状态 | 说明 |
|---|---|---|
| H1 不杜撰事实 | ✅ | 所有引用均标注来源 |
| H2 不杜撰邮箱 | ✅ | 5 个邮箱**全部抄自官网原文**，无一个按规则生成 |
| H3 邮箱格式校验 + ≥1 交叉源 | ⚠️ 部分 | 格式合法；`Danny@` 有 BBB + 官网**双源**；其余 4 人**仅官网单源**（但属第一方） |
| H4 标注验证状态 | ✅ | 已明示 **B 级 / catch-all / SMTP 失效** |
| H5 交叉验证 ≥1 第一方 | ✅ | **官网（第一方）** 提供全部 5 人 + 5 邮箱 |
| H6 角色邮箱不可单独交付 | ✅ | 本案**有具名个人邮箱**，未依赖 `info@` |
| H7 落盘 `.md` | ✅ | 本文件 |

### ✅ 最终判定：**合格（可写）** —— 进写信环节

**理由**：满足「具名决策人（Danny Lao, Owner）+ 具名邮箱（第一方官网公示）」双要件。catch-all 只影响**验证手段**，不影响**交付资格**（邮箱来自第一方公示，非猜测）。

---

## 七、开发信建议（**仅建议，不代写正文**）

> 🔴 **本节遵守分工铁律**：只给「收件人 / 时机 / 素材锚点 / 附件」建议。
> **不做**：措辞、钩子句、主题行、开场句、正文——全部归环节 ② 写开发信 agent。

| 项 | 建议 |
|---|---|
| **首选收件人** | **Danny Lao**（Owner）· `Danny@accesselectricalsupply.ca` —— 单人决策，直击 |
| **次选收件人** | **Scott Rawson**（Toronto/ON 负责人）· `Scotty@accesselectricalsupply.ca` |
| **CC / 备用** | `info@accesselectricalsupply.ca`（总部页脚公示） |
| **可写素材锚点** | ①官网在售 `transformers`；②NMD90/AC90/RW90 电缆 + 配电盘/断路器主营 → **配电级产品盘**；③「distributors' solution」自我定位；④正在铺分支（Edmonton/Calgary/Saskatoon/Vancouver 均待开）→ **备货/铺货诉求** |
| **产品切片** | **`E541627`**（三相液浸配电变，UL 45–5,000 kVA / CUL 75–3,000 kVA，**正式 CoC**）—— 与其配电级产品盘匹配 |
| 🚫 **不得提** | ❌ 高压主变 / `E541626`（对美不谈，本案在加拿大可谈但**与其业务盘不匹配**，不建议）；❌ `E544629` 柱上变说 "certified"；❌ 干式变（加拿大可谈但需谨慎）；❌ `CSA Certified` / `SASO` / `SONCAP`；❌ 品牌 `YAWEI`；❌ 首封报交期与价格；❌ 附供货记录 PDF |
| **附件建议** | 首封**不加附件**；待其回复确认「在盘变压器容量段」后再定向发对应 CoC |
| **时机** | 常规工作日（MB 为 Central Time，CST/UTC-6）。⚠️ 其营业时间 08:00–17:00 → 宜其**上午**送达 |

---

## 八、待补与风险

| # | 项目 | 说明 |
|---|---|---|
| 1 | ⚠️ **catch-all 无法验证** | SMTP 通道失效；`Danny@` 等地址依赖官网公示，需**首封后按退信确认** |
| 2 | ⚠️ **Nicholas Goresky 岗位未知** | 官网未公示其职务，仅列为联系人 |
| 3 | ⚠️ **Mark 姓氏未知** | BC 页仅写 "Mark"，无全名 |
| 4 | ⚠️ **规模风险** | 成立仅 3 年、2 个实体分支、多个网点"Coming Soon" → **单次采购量可能极小**，宜作**长期培育型**线索而非短期冲量 |
| 5 | ⚠️ **在盘变压器规格未知** | 官网未列 kVA 区间与品牌，需回复后确认 |
| 6 | ⚠️ **BBB 分类误导** | BBB 标签为 "Electric Equipment Manufacturers"，**已排除，勿被误导** |
| 7 | ⚠️ **DMARC 缺失** | 无 DMARC 记录 → 其**自有发信**不受保护；与我方发信无关，仅作记录 |

---

## 九、数据溯源

| 事实 | 来源 | 可信度 |
|---|---|---|
| 公司全称 / 地址 / 电话 | 官网 `accesselectricalsupply.ca`（首页、`/winnipeg`、`/toronto`、`/branchlocations`） | 第一方 · 高 |
| 成立日期 / 公司号 / 实体类型 | BBB Business Profile + Corporations Canada（#15215307） | 双源 · 高 |
| **Danny Lao = Owner** | BBB（Business Management + Principal Contacts 双处） + 官网员工名录 | **三源 · 极高** |
| Jon Buccini 岗位 | 官网 Winnipeg 页 + LinkedIn | 双源 · 中高 |
| Scott/Lisa Rawson、Nicholas Goresky、Mark | 官网分公司页 | 第一方 · 高 |
| 邮箱 5 个 | 官网 Winnipeg/Toronto/Vancouver 页 **逐字抄录** | 第一方 · 高 |
| MX / SPF / 域名 A | 本机 `dig`（@8.8.8.8） | 实测 · 高 |
| SMTP 探测 | 本机 smtplib 直连 M365（`ian@jiezougroup.com` 发信） | 实测 · 高 |
| 法定注册地址 201 Portage Ave | Corporations Canada | 官方 · 高 |

### ⛔ 已剔除的不可信来源（重要）

| 来源 | 问题 | 处置 |
|---|---|---|
| **`lbmsales.com/showcase/manitoba/access-electrical-supply`** | 🔴 **内容系模板批量生成** —— 出现 "John Access"（岗位 "Electrical Counter Lead"）、"Dave Electrical"、电话 `(204) 555-0131`（**555 为虚构号段**）、及 "James Hardie siding / ZIP System / Simpson Strong-Tie / framing lumber"（**建材品牌，与电气批发商无关**） | **整页作废，零采用** |

> **教训（建议入 skill）**：目录聚合站（LBM Sales 之类「Showcase / Spotlight」页）存在 **AI 批量填充的稻草人数据**。识别特征：**人名与公司名/岗位机械拼接**（"John Access"）、**555 电话**、**产品品类与公司主业矛盾**。此类来源**一律不得进入交接单**。

---

## 附：CSV 原始记录

```
48,B 分销商/贸易商,Access Electrical Supply Ltd.,Access Electrical,加拿大,ON,分销商,加拿大电气产品供应分销商,accesselectricalsupply.ca
```

> **修正记录**：CSV 仅记 `ON`（因 Toronto 分支），实际**总部在 MB（Winnipeg）**，ON 为分公司。
> 建议 CSV「州省」列补注为 **`MB/ON`**，或保持 `ON` 但于交接单内明示双省结构。

---

*建档：砚舟 · 2026-09-28 · batch5_new_129plus · 买家 169 / CSV 48*
