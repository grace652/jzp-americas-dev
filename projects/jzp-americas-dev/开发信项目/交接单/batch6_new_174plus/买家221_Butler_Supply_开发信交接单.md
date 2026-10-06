# 【买家 221】开发信交接单 — Butler Supply Inc.（Fenton / St. Louis, MO）

> 采集日期：2026-09-29 / 来源：batch6 名单（目标客户清单-batch6.csv 序 48，MO 分销商）/ 一句话结论：圣路易斯地区最大独立电气+管道分销商（1941 创立，女性持股 WBE，30+ 分支），⓪层 PASS（电气/管道批发，非制造商）；区域副总裁 Randy Kunkel 具名邮箱由**官网分支页 + IEC 圣路易斯协会名录 + SMTP 250 三重印证**（A 档）；原采购总监 Russ Braunseis 疑似已离职。

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示(如有)
Butler Supply Inc. | Randy Kunkel | Regional Vice President（区域副总裁） | rkunkel@butlersupply.com | 已验证（官网分支页明文 + IEC St. Louis 协会名录 + SMTP RCPT 250 三重印证） | linkedin.com/in/randy-kunkel-a2739042｜linkedin.com/company/butler-supply | 1941 年创立于 St. Louis MO；100% 女性持股、全国认证 WBE；电气 + 管道 + 通信 + 工具/安全多品类批发分销；30+ 分支（MO/IL/KY/TN/AR 等），约 145 人；圣路易斯地区最大独立分销商 | 官网 butlersupply.com（分支页 + 招聘页）+ IEC St. Louis 会员名录 + LinkedIn（个人页 + 公司晋升帖）+ Wiza/ContactOut 旁证 + SMTP 探测 | 邮箱域=官网域；MX=Microsoft 365；本机对该域 SMTP 有效（sales@ 250 + 随机 550 对照通过） |
```

## 二、补充信息（扩展段）

### 标准字段明细
- 国家+城市：美国 Missouri — Fenton（公司总部，St. Louis 都会区）；门店覆盖 St. Louis 城区 + MO/IL/KY/TN/AR 等 30+ 分支
- 详细地址：965 Horan Drive, Fenton, MO 63026（总部，官网 Contact 页原话）；2141 January Ave, St. Louis, MO 63110（St. Louis 城门店）
- 电话：(636) 349-9000（总部，官网/协会一致）；Fax (636) 680-1144
- LinkedIn：个人 `linkedin.com/in/randy-kunkel-a2739042`；公司页 `linkedin.com/company/butler-supply`
- 网站：butlersupply.com
- 成立日：**1941**（engproducts / united-local 一致，"founded in St. Louis, MO in 1941"）
- 规模：约 145 人（LeadIQ 145 / RocketReach 144 / ContactOut 127）；**30+ 分支**（官网 "30 branch locations"，2025 分支表列 32）
- 营收：未获取
- NAICS：**423610（电气批发）/ 423720（管道批发）** —— 官网与协会均标 "Electrical & Plumbing Distributor" ⇒ **分销，非制造**
- 股权/属性：**100% 女性持股、管理、控制**，全国认证 **WBE**（united-local 原话）

### 联系人（含 still_here 在职核验）
| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| **Randy Kunkel**（主送） | 区域管理 / 公司对外登记联系人 | Regional Vice President（原 Manager） | LinkedIn 标 Manager；公司帖宣布晋升 Regional VP；**至少 2018 起**（allpeople 标 2018–2023） | LinkedIn 现职 "MANAGER at Butler Supply"（Jefferson County）；官网 Fenton 分支页列其邮箱；IEC 圣路易斯名录列其为公司 Contact | 低 | linkedin.com/in/randy-kunkel-a2739042 |
| John Duda | 公司最高决策（备选，不发） | Chairman & CEO | 未获取 | RocketReach / Wiza / LinkedIn（john-duda-99b995b2）现职 | 低 | linkedin.com/in/john-duda-99b995b2 |
| Russ Braunseis | 原采购总监（**已离职，勿发**） | 原 Director of Purchasing/PEPPER | allpeople：2012–2022 | Wiza（2026-06）仍标现职，但**与 SMTP / 年限证据冲突** | 🔴 **高（疑离职）** | 未取 |

> 选人说明：本单**采购总监岗疑似空缺/换人**（见矛盾点），故按优先级下沉 —— **Randy Kunkel 是唯一同时具备「具名 + 在职 + 第一方邮箱」的高级管理触点**（区域副总裁 + 官网登记联系人），定为主送。John Duda（Chairman & CEO）为备选，**不并发发送**（一家只发 1 人）。

### 邮箱分档（A/B/C）
- **A 档（具名，主送）**：`rkunkel@butlersupply.com` — Randy Kunkel（Regional Vice President）
  - 来源 1（一手）：官网分支页 `butlersupply.com/locations/fenton/` 明文列 "EMAIL: rkunkel@butlersupply.com"
  - 来源 2（一手/协会）：**IEC（Independent Electrical Contractors）Greater St. Louis 会员名录**列 "Contact: Randy Kunkel / Email: rkunkel@butlersupply.com"
  - 来源 3（实证）：SMTP RCPT **250**；同轮控制 `sales@butlersupply.com` = **250**、随机地址 `zzz_nope_x@` = **550**（非 catch-all）⇒ 探测可信。
  - 命名规则实证：本域为 `{first_initial}{last}@`（rkunkel@ 250）。
- **B 档（角色邮箱，采购入口）**：`sales@butlersupply.com`（250）/ `purchasing@butlersupply.com`（**250，SMTP 实证存在**）—— 仅作点名转交或备选。
- **C 档**：无。
- **H6 声明**：不适用（已取得具名高级管理邮箱）。

### 我为什么找他
- **Randy Kunkel 是 Butler Supply 对外登记的公司联系人**（IEC 圣路易斯协会名录 Contact 一栏）且被公司公开晋升为 **Regional Vice President**（LinkedIn 公司帖）—— 说明他是**公司层面可对外的决策触点**，不是随机抓的高管。
- Butler 是 **WBE 女性持股 + 30+ 分支 + 电气与管道双品类**的圣路易斯最大独立分销商；官网在招 **Director of Gear & Lighting / VP of Lighting / Director of Industrial Sales / Panel Shop Technician**（2026-09 招聘页）—— 正在**扩张 gear（配电类）与工业品类**，正是配电变压器可切入的窗口。

### 买家类型 / 需求品类
- 买家类型：🔥🔥 **A 型 —— 电气 + 管道分销商**（圣路易斯地区最大独立分销商，30+ 分支，NAICS 423610/423720）
- 需求品类（带结论态）：
  - `三相美变（UL E541627，可直供）` —— 工业/商业配电与 gear 品类主谈
  - `单相柱上变（认证在办，条件切入）` —— 仅户外/临时供电场景条件性提及
  - ⛔ 不推：**干变（美国不匹配：无 UL）** —— 对美国客户一律不谈干变
- ⚠️ 注意：Butler 招聘含 **Panel Shop Technician**（Paducah）⇒ 其有**配电柜组装**增值能力（属分销商常见 panel shop，**非变压器制造**），不影响 ⓪ 层判定。

### 电压·频率·认证要求
- 电压：未获取（**需电话确认**）
- 频率：**60 Hz**（美国）
- 认证：美国市场需 **UL**；我方三相液浸配电变持 UL **E541627**
- ⚠️ 附加：Butler 为 **WBE 认证企业**，其采购/供应商流程可能含多元化供应商（diversity supplier）考量，**可作切入话术角度之一**（非首封必谈）

### 采购信号
- 2026-09 招聘页密集在招：**Director of Gear & Lighting（Fenton + Lee's Summit 两处）/ VP of Lighting / Director of Industrial Sales / Project Manager-Quotations Specialist** → **品类扩张期**，正补强 gear/照明/工业线
- 30+ 分支 + 总部 Fenton 集中配送 → 备货型分销商
- 官网自述支持 "Order Online, by Email, Over the Phone, or Via Text" → 线上化成熟，采购/供应链有系统支撑
- 2025 年收购扩张（Christopher Reese 帖：Butler 2025 初扩张区域版图）→ 整合期常有供应商重审窗口

### 可利用的钩子（按强度排序）
1. **在招 Director of Gear & Lighting / VP of Lighting（2026-09）**（最强，时效性最高）→ 说明 gear/配电品类正在扩张，新增变压器供应线时机契合
2. **WBE 女性持股 + 圣路易斯最大独立分销商** → 合规与规模对等，可谈供货资质
3. **30+ 分支 + 电气/管道双品类** → 单点成交可辐射多州
4. **2025 区域扩张 + 整合期** → 供应商重审窗口

### 开发信建议
- **收件人策略**：主送 `rkunkel@butlersupply.com`（Randy Kunkel，Regional Vice President，A 档）。**一家只发 1 人**，不并发 John Duda。若需直对采购职能，可用 B 档 `purchasing@butlersupply.com` 点名转交（但**优先发具名**）。
- **送达配置**：邮箱域 = 官网域（butlersupply.com），无需换域；MX = Microsoft 365 → 走正规 ESP/合规发件域，SPF/DKIM/DMARC 三件套齐，纯文本优先。
- **发送时段**：圣路易斯（CT，UTC-6/-5）周二–周四 上午 09:00–11:00 ≈ 北京时间 22:00–24:00（夏令时 23:00–01:00）。
- **附件建议**：首封不带供货名录/PDF；可提及 UL 证书号与容量区间。
- ⛔ 首封红线：不写交期数字、不写价格词、不提 CSA Certified / SASO / SONCAP / YAWEI、不谈干变。

### ⚠️ 矛盾点与风险提示
- 🔴 **原采购总监 Russ Braunseis 疑似已离职**：Wiza（2026-06）标其现职 "Director of Purchasing/PEPPER"，但 **SMTP 实测 `rbraunseis@butlersupply.com` = 550**（本域命名规则为 `{f}{last}@`，若其在职应为 550 之外的命中），且 allpeople 标其 "2012–2022"。⇒ **不采用其为收件人**，并建议电话确认采购职能现任归属。
- ⚠️ `russb@butlersupply.com` SMTP = 250（存在），但**无法确认该地址属于 Russ Braunseis**（本域规则为 `{f}{last}`，`russb` 不符）→ **不采用**，避免张冠李戴。
- ⚠️ **同名主体陷阱**：另有 **Butler Supply Group（BSG，PA/FL，butlersupplygroup.com）**、**The Butler Corporation（清洁用品，shop.butlersystem.com）**、**butlersupplies.com** —— **均非本案**。本案唯一指向 **MO Fenton 的 Butler Supply Inc.（butlersupply.com）**。
- ⚠️ 官网 butlersupply.com 与分支 PDF **被 Cloudflare 拦截**（403），分支名录未能全量抓取 → 分支级联系人覆盖不完整。
- ⚠️ Randy Kunkel 的**现任职务口径不一**（LinkedIn 标 "MANAGER"，公司帖称晋升 "Regional Vice President"）→ 写信时**用职务泛称或直接称其名**，避免头衔写错。

### 信息缺口清单（请勿编造）
- **现任采购负责人姓名/邮箱**：未找到（原总监 Russ Braunseis 疑离职）
- Randy Kunkel 的**任职起止精确日期 / 晋升时间**：未获取
- Butler 的**常用变压器容量 / 电压等级 / 现有品牌**：未获取（需电话确认）
- **年营收 / 精确员工数**：未获取
- **分支全量联系人名录**：未获取（官网分支 PDF 被 Cloudflare 拦）
- **邮箱可投递性**：SMTP 250 已实证存在；实际送达仍受 M365 网关策略影响

### 一句话画像
圣路易斯 1941 年创立、女性持股 WBE 的电气+管道最大独立分销商（30+ 分支），2026 年正在补强 gear/照明/工业品类；区域副总裁 Randy Kunkel 的邮箱由官网+协会+SMTP 三重坐实，是当前最稳的具名触点。

### 渠道覆盖清单（L-1、L0–L7）
| 层 | 结果 | 一句话 |
|---|---|---|
| L-1 锁人 | ✅ | 锁到 Randy Kunkel（区域 VP，官网+协会登记联系人）+ CEO/President 备选 |
| L0 官网 | ⚠️ | 分支页产出 `rkunkel@butlersupply.com`（一手明文）；**Corporate Directory / 分支 PDF 被 Cloudflare 拦** |
| L1 政府一手 | ⚠️ | NAICS 423610/423720 经第三方库核；MO SOS 未查 |
| L2 命名+DNS | ✅ | MX=M365；SMTP 有效（sales@/purchasing@ 250 + 随机 550）；实证 `{f}{last}@` 规则 |
| L3 B2B 库 | ⚠️ | Wiza / ContactOut / RocketReach / LeadIQ 旁证（不作印证主力） |
| L4 社媒协会 | ✅ | **IEC St. Louis 会员名录**（一手协会登记）+ LinkedIn 个人页/公司晋升帖 |
| L5 黄页同址 | ✅ | superpages / mapquest / united-local 同址交叉 |
| L6 电话表单 | ✅ | 总部 (636) 349-9000 + 表单（未拨打） |
| L7 付费 | ❌ | 未启用 |

---

- 发信资格：✅ 通过（核心字段齐、still_here 四栏齐、有「我为什么找他」与缺口清单）
- 邮箱档位：**A（具名，官网明文 + 协会名录 + SMTP 250 三重印证）**
- ⓪ 层反身排除：**PASS** —— 官网/协会自述 *"Electrical & Plumbing Distributor"* / *"Wholesale Distributor"*，NAICS 423610/423720 ⇒ **分销商**；招聘含 Panel Shop Technician（配电柜组装，属分销增值，**非变压器制造**），无 `we manufacture` / `our factory` / 变压器 `OEM` 表述，**无代理 YAWEI 等禁用品牌** ⇒ 分销商客户，非竞品。
