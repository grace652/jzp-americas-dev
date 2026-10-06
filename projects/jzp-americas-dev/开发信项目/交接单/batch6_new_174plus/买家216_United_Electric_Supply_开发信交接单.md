# 【买家 216】开发信交接单 — United Electric Supply Co., Inc.

> 采集日期：2026-09-29 / 来源：batch6 名单（第 43 行，CSV 州省 DE、备注「特拉华电气供应（New Castle DE）」）/ 一句话结论：**特拉华 New Castle 的 1965 年创立、100% 员工持股（ESOP）的中大西洋电气分销商**（300+ 人、7 大品类含 gear & control，网点覆盖 DE/PA/MD/北 VA/NJ）；⓪ 层通过（NAICS 423610 批发 + 官网自述 "general-line distributor"；SAM 另登记 335xxx 制造业码但**非 335311/335313**，判为投标广度自报）；**采购一把手 Dave Wilson（Director of Purchasing，2026-01 升任）已锁**，具名邮箱 `dwilson@unitedelectric.com` 为规则推演（**待验证**）→ 主送走 B 档：电话 (302) 322-3333 点名转交。

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示(如有)
United Electric Supply Co., Inc. | Dave Wilson（主送）/ Tony Buonocore（备选） | Director of Purchasing / President & CEO | 推演：dwilson@unitedelectric.com（待验证）；B 档：电话 (302) 322-3333 / (800) 322-3374 点名转交 | A 档具名：待验证；B 档角色邮箱：**未找到**（官网被 Cloudflare 拦，未取到第一方邮箱） | 公司 linkedin.com/company/unitedelectricsupply；个人页未确认 | DE New Castle，1965 创立，100% ESOP 员工持股，300+ 人，7 大品类（含 gear & control），网点 DE/PA/MD/北VA/NJ，SAM.gov 含 PSC 6120 变压器 | 官网 /aboutus + tED Magazine×2(2026-01/2026-03) + MDM + Datanyze + SAM.gov(GovCB) + DNS | 🔴 具名邮箱为规则推演，**不得作主送**；官网被 Cloudflare 拦未取到第一方邮箱；SAM 自报制造业 NAICS（需辨）
```

## 二、补充信息（扩展段）

### 标准字段明细
- 国家+城市：美国 Delaware，New Castle（总部；对外亦称 Wilmington，ET 时区）
- 详细地址：10 Bellecor Dr, New Castle, DE 19720（SAM.gov / 官网一致）
- 电话：**(302) 322-3333**（SAM.gov）；**(800) 322-3374**（24 小时应急，官网）；(302) 322-7662（Datanyze）
- 网站：**unitedelectric.com**（Cloudflare 保护；A=104.18.x Cloudflare）
- **邮箱域**：`unitedelectric.com`（MX = `unitedelectric-com.mail.protection.outlook.com` = **Microsoft 365**；SPF 含 outlook / exclaimer / amazonses / emailcampaigns / createsend / sendgrid + `ip4:50.235.120.26`，`-all`）
- 成立日：**1965**（官网 /aboutus 原文 "founded in 1965"；SAM.gov Year Established 1965 —— 一致）
- 规模：**300+ 人**（官网）；380（ContactOut）/ 500（Datanyze/Kona）⚠️ 口径不一；营收 **$300M+**（官网）/ $105.6M（Kona）⚠️ 口径矛盾
- 网点：Regional Service Centers（New Castle DE、Culpeper VA）+ 分支覆盖 **DE / PA / MD / 北 Virginia / NJ**
- NAICS：**423610**（primary，批发）+ 444190；⚠️ SAM.gov 另登记 **335122 / 335129 / 335312 / 335314 / 335999**（制造业码）
- **PSC 6120 = "Transformers: distribution & power station"**（SAM.gov）→ 确证政府供变电设备
- 集团归属：**独立，100% 员工持股（ESOP）**（1995 员工收购），**非** Sonepar/USESI/WESCO/Rexel 成员；2024 并购 **Kovalsky-Carr**（Rochester NY）为子公司
- 社媒：linkedin.com/company/unitedelectricsupply
- 州省核实：**CSV = DE ｜ 实测 = DE（New Castle）** —— 一致

### 联系人（含 still_here 在职核验）
| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| **Dave Wilson**（主送） | **采购一把手** | Director of Purchasing | 2018 入职 Buyer → 2020 Manager → **2026-01 升 Director** | 高：**tED Magazine 2026-03 官方公告 + tedmag.com 2026-01-14 + Datanyze 三源** | 低 | 未确认（Datanyze 列 "David Wilson, Director, Purchasing"） |
| Tony Buonocore | CEO（备选） | President & CEO（2026-05 起，接替退休的 George Vorwick） | 2018 随 Westway 并入 United，2025 起 President | 高：tED/electricalmarketing 2026 公告 | 低 | 未找到 |
| Greg Sundberg | EVP Sales（备选） | Executive VP, Sales（2026-05） | 20+ 年 | 中：tED 2026-05 | 低 | 未找到 |
| Lindsey Cropper | CHRO（非采购） | Chief Human Resources Officer | 2016 入职 | 中：tED 2026-01 | 低 | 未找到 |

> 🔴 一家只发 1 人：**主送 Dave Wilson（Director of Purchasing）** —— 采购一把手，2026 年 1 月刚升任（新供应商窗口）。
> 备选（同公司不重复发）：Tony Buonocore（President & CEO）、Greg Sundberg（EVP Sales）。

### 邮箱分档（A/B/C）
- **A 档（具名）**：**无已验证具名邮箱**。推演 `dwilson@unitedelectric.com`（依 Datanyze 首格式「first initials + last, `JSmith@unitedelectric.com`」+ LeadIQ「FLast@」+ ContactOut「{first_initial}{last}@」）→ 状态 **待验证**，**不可作主送**。
- **B 档（角色）**：**未找到第一方明文** —— 官网 `unitedelectric.com` 被 Cloudflare 拦（HTTP 403），未取到 `info@` / `sales@` 等。
- **主推路径**：电话 **(302) 322-3333** / **(800) 322-3374**，**点名转交 Dave Wilson, Director of Purchasing**；正文首句明确请求转交
- 🔴 **H6 声明**：**既未取得具名直邮、也未取得第一方角色邮箱**。已跑「升级三步」：
  1. 挖职能邮箱：官网被 Cloudflare 拦，**未取到任何第一方邮箱**
  2. 从真实样本反推命名规则：无回信样本（命名规则来自第三方库）
  3. 免费试推演：`dwilson@unitedelectric.com`（**推演，未验证**）
  → 结论：**本单唯一可靠入口是电话点名转交**，具名邮箱仅为「待验证」候选，已如实标注为风险。
- ⚠️ **SMTP 探测未跑**：MX = Microsoft 365，且本机源 IP 已被同批网关以 Spamhaus PBL 拦截 ⇒ 预判**不可探测，未浪费轮次**。

### 我为什么找他
- United 是 **1965 年创立、100% ESOP 员工持股**的中大西洋电气分销商（300+ 人，7 大品类含 **gear and control**），且**从未被 Sonepar/WESCO/Rexel/PE 收购** —— 是罕见的「独立 + 员工持股」主体，采购决策留在公司内部。
- **Dave Wilson 的采购职务由行业官方媒体三源公开确认**：tED Magazine（2026-03 纸质版 + 官网 2026-01-14）原文「**Dave Wilson is now director of purchasing.** He joined United in 2018 as a buyer and was promoted to manager in 2020」——**2026 年 1 月刚升任**，是稳定在职、且处于**新岗位建立供应商关系窗口期**的采购一把手。
- 品类直接对应：其 **SAM.gov 政府供应商档案含 PSC 6120 "Transformers: distribution & power station"** → **确证有配电/电力变压器的采购与供货场景**（不是推测）。

### 买家类型 / 需求品类
- 买家类型：**A 分销商**（独立、100% ESOP；工业自动化 / 照明 / 线缆管件 / gear & control / 数据通信 / 机电 / 能源方案 七大品类）
- 需求品类（带结论态）：
  - `三相美变（UL E541627，45–5,000 kVA，可直供）` —— 配电场景
  - `主变 / 变电站变（UL E541626，750–110,000 kVA，可直供）` —— 对应 PSC 6120 "power station" 变压器
  - `单相柱上变（认证在办 E544629，条件切入）` —— 非首推
  - ⚠️ 美国客户：**不谈干变**（无 UL 不匹配）

### 电压·频率·认证要求
- 电压：未获取（PSC 6120 覆盖 distribution + power station 两档）
- 频率：**60 Hz**（美国）
- 认证：我方 UL **E541626 / E541627** 正式 CoC，适配美国

### 采购信号
- **PSC 6120「Transformers: distribution & power station」**（SAM.gov）→ 已具备变压器政府供货资质与场景
- **2026-01 采购部升格为 Director 级**（Dave Wilson）+ 2026-05 新 CEO 上任 → **组织调整期 = 新供应商窗口**
- **ESOP + 并购扩张**（2024 并入 Kovalsky-Carr，保留独立品牌）→ 多品牌采购协同
- 7 大品类含 **gear and control** + 官网强调 "engineering expertise / hands-on product testing" → 项目配套采购

### 可利用的钩子（按强度排序）
1. **PSC 6120 变压器政府供货资质**（SAM.gov）—— 与配电/电力变最直接对口
2. **2026-01 采购部升格 + 2026-05 新 CEO**（组织调整期）—— 新供应商窗口
3. **100% ESOP 员工持股 + 独立（未被巨头收购）**—— 长期合作、决策留在内部
4. **ESOP 并购模式（Kovalsky-Carr 保留独立品牌）**—— 多品牌采购协同角度

### 开发信建议
- **收件人策略**：**不要**盲发推演地址 `dwilson@unitedelectric.com`（**待验证**，触 H2/H4）；本单**无第一方角色邮箱可用** ⇒ 走 **电话 (302) 322-3333 / (800) 322-3374 点名转交 Dave Wilson, Director of Purchasing**（或官网 Contact 表单）
- 🔴 **域名提醒**：邮箱域为 **`unitedelectric.com`**；⚠️ 勿与加州 **unitedelectricchino.com**、**ueonline.com（United Electric Controls）**、**unitedelec.com** 等**同名不同实体**混淆
- **开场角度**：从其 **PSC 6120 变压器供货资质 + gear & control 品类**切入（写信 agent 决定措辞）
- **发送时段**：特拉华 **ET**，周二–周四当地上午 = **北京时间 21:00–23:00**（夏令时期间）
- **送达配置**：MX = **Microsoft 365**；SPF `-all`；发信域须 SPF/DKIM/DMARC 齐备；纯文本
- **附件建议**：不带名录/供货记录；如需仅附 UL 证书号 + 容量区间

### ⚠️ 矛盾点与风险提示
- 🔴 **既无具名验证邮箱、也无第一方角色邮箱**：`dwilson@unitedelectric.com` 系**命名规则推演**；官网被 Cloudflare 拦，未取到 `info@` ⇒ **唯一可靠入口是电话**。
- ⚠️ **SAM.gov 自报制造业 NAICS**：档案含 335122/335129/335312/335314/335999（制造业码）—— **非 335311/335313（变压器/开关柜制造）**，且官网无任何制造自述（自述为 "general-line distributor"）⇒ 判定为**分销商为投标广度自报的分类**，**不构成 ⓪ 层排除**；但**该码需人工复核**（是否另有 panel/gear 组装业务）。
- ⚠️ **规模数据口径矛盾**：员工 300+（官网）/380/500；营收 $300M+（官网）/$105.6M（Kona）⇒ **正文勿引用具体数字**。
- ⚠️ **集团归属澄清**：United **不是** Sonepar/USESI 成员（独立 ESOP）；但其子公司 **Kovalsky-Carr** 为独立品牌 ⇒ 若开发 KC 需另开单据。
- ⚠️ **同名实体极多**（unitedelectricchino / ueonline / unitedelec）⇒ 发信前务必核对域名为 `unitedelectric.com`。

### 信息缺口清单（请勿编造）
- Dave Wilson 的**已验证具名邮箱**：**未找到**（仅推演）
- **第一方角色邮箱**（info@ / sales@）：未找到（官网 Cloudflare 拦截）
- Dave Wilson 的**个人 LinkedIn 直链 / 最近活跃**：未获取
- 公司**员工数 / 营收**（一手源口径）：口径矛盾，未定
- 公司**常用变压器容量 / 电压 / 品牌**：未获取（仅知 PSC 6120 品类）
- **DE 州注册主体全称 / 注册日**：未查
- SAM 制造业 NAICS 对应的**实际业务**（是否 panel/gear 组装）：未核实
- 采购**决策归属**（Dave Wilson vs 各 RSC 分部）：未明

### 一句话画像
特拉华一家 1965 年创立、**100% 员工持股、从未被巨头收购**的中大西洋电气分销商 —— **采购一把手 Dave Wilson 由 tED Magazine 官方公告确认、2026 年 1 月刚升任**，SAM 档案还带着 PSC 6120 变压器供货资质；对口度极高，但**官网被 Cloudflare 拦、无任何第一方邮箱**，只能靠电话点名转交。

### 渠道覆盖清单（L-1、L0–L7）
| 层 | 结果 | 一句话 |
|---|---|---|
| L-1 锁人 | ✅ | tED Magazine（行业官方媒体）三源锁 Director of Purchasing Dave Wilson |
| L0 官网 | ⚠️ | /aboutus 正文可读（搜索快照），但直抓被 **Cloudflare 403** ⇒ 未取到第一方邮箱 |
| L1 政府一手 | ✅ | SAM.gov 档案（NAICS + **PSC 6120 变压器** + 电话；无邮箱） |
| L2 命名+DNS | ✅ | MX=M365；命名规则来自第三方库（FLast@）；SMTP 预判失效未跑 |
| L3 B2B 库 | ⚠️ | Datanyze/LeadIQ/ContactOut/RocketReach 给格式与职务（**互证不算印证，H5**） |
| L4 社媒协会 | ⚠️ | 公司 LinkedIn 页命中；个人页未确认 |
| L5 黄页同址 | ⚠️ | New Castle DE 地址一致 |
| L6 电话表单 | ✅ | (302) 322-3333 / (800) 322-3374 + 官网表单（未拨打/未提交） |
| L7 付费 | ❌ | 未启用 |
