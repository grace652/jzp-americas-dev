# 【买家 179】开发信交接单 — Allied Projects Ltd.

> 采集日期：2026-09-29 / 来源：batch6 名单（A 电气承包商，AB 工业+可再生）/ 一句话结论：**卡尔加里 design-build 全服务电气承包商（1996，员工持股），⓪ 层通过；锁到 VP Operations Jason Lane（官网团队页+LinkedIn 双源），但只拿到官网投标角色邮箱 `estimating@`，具名直邮未找到（域走 Proofpoint ARS，SMTP 探测无效）。**

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示(如有)
Allied Projects Ltd. | Jason Lane | Vice President, Operations | estimating@alliedprojects.ca（B档·点名转交）| 已验证（官网明文角色邮箱）；具名直邮未找到 | linkedin.com/in/jason-lane-9b152367 | 卡尔加里，1996 年 Mike Brunner 创立，2008 年转员工持股；商业/市政基建/机构/轻工业 design-build 电气承包，~80 人 | 官网（首页/团队页/Contact）+ LinkedIn + ECAA 前会长佐证 | 邮箱域=官网域（一致）；MX=Proofpoint ARS，SMTP 探测无效；仅角色邮箱，须点名转交
```

## 二、补充信息（扩展段）

### 标准字段明细
- 国家+城市：加拿大 Alberta，Calgary（卡尔加里）
- 详细地址：7017 Farrell Road SE, Calgary, AB T2H 0T3
- 电话：403-543-4530；传真 403-543-4540
- 网站：alliedprojects.ca
- 邮箱域：alliedprojects.ca（与官网域一致）｜ MX：`alliedprojects-ca.mx1/mx2.arsmtp.com`（Proofpoint ARS 网关）
- 成立日：1996 年（官网团队页：Mike Brunner 于 1996 年创立）；2008 年转为**员工持股公司（employee-owned）**
- 规模：~78–80 人（RocketReach 78 / CompanyListing 80，第三方，未回源）
- 营收：未获取
- NAICS：未获取（未回源核对）

### 联系人（含 still_here 在职核验）
| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| **Jason Lane**（主送点名） | 运营负责人（设备选型/采购实际决策层） | Vice President, Operations | 未获取（具体起止未公开） | LinkedIn 现职"Vice President, Operations at Allied Projects Ltd"；官网团队页在列 | 低（官网团队页 + LinkedIn 双源均现任） | linkedin.com/in/jason-lane-9b152367 |
| Brian Reed（备选） | 商务/项目开发 | Vice President, Business Development | 未获取 | LinkedIn 现职在列；官网团队页在列 | 低 | linkedin.com/in/brian-reed-34315a31 |
| Michael Brunner | 创始人（2012 年已移交日常经营） | Founder | 1996 年创立 | 官网团队页在列 | 低（但不负责日常采购） | 未取（官网团队页有传） |
| Arpad Bencsik | 报价（Senior Estimator） | Senior Estimator | 未获取 | 仅 LinkedIn 目录页命中，未经个人页确认 | ⚠️ 未核 | linkedin.com/pub/dir/Arpad/Bencsik（**目录页，非个人页**） |

### 邮箱分档（A/B/C）
- **A档（具名决策人直邮）**：**未找到**（官网 Contact 只放 `estimating@`；个人邮箱零公开）
- **B档（角色邮箱，主送）**：`estimating@alliedprojects.ca` —— 官网 Contact 页明文，且**语义对口**（"For Bid Invitations, please email us here"），是供应商报价/投标的正规入口 → **主送 + 正文点名转交 Jason Lane（VP Operations）**
- **C档**：无
- **H6 声明（强制）**：**仅取得角色邮箱 `estimating@`，未取得决策人直邮。** 升级三步：① 职能邮箱 —— 官网只有 `estimating@` 一个，无 `purchasing@` / `suppliers@`；② 回信样本 —— 无（未触达，拿不到签名反推命名规则）；③ 推演 —— **无样本，停推演**（H2）。⇒ 列为本条风险。

### 我为什么找他
- 官网 Contact 页把 **`estimating@` 直接开放为投标邮箱**（原文 "For Bid Invitations, please email us here"）—— 说明 Allied 的报价/采购入口**对外透明**，供应商可直接触达；且其自述为 **design-build**（设计-建造）承包商，**变压器由其自行选型采购**，是真实的设备采购方。
- 另一层具体观察：Allied **2008 年转为员工持股公司（ESOP）**、创始人 Mike Brunner 曾任 **2006 年阿尔伯塔电气承包商协会（ECAA）会长** —— 这两条都是"我研究过你"的硬证据，不是套话。

### 买家类型 / 需求品类
- 买家类型：**A 电气承包商（design-build，全服务多元化；商业/市政基建/机构/轻工业）**
- 需求品类（带结论态）：
  - `三相美变（UL E541627，可直供）` —— 商业/机构/轻工业配电主谈
  - `干变（加拿大可谈，built to CSA 标准）` —— 楼宇/机构项目常用
  - `主变（产能可覆盖，UL 区间外，需人工确认）` —— 如有较大工业项目
  - 说明：承包商属**项目制采购**，规格随项目走；首轮宜先问"当前项目常用容量段"，而非硬推单一品类。

### 电压·频率·认证要求
- 频率：60 Hz（加拿大）
- 电压：低压 120/208/240/347/480/600 V；中压 4.16 / 13.8 / 25 kV（承包商项目常见段）
- 认证：加拿大 **CSA / cUL** 体系；我方 E541627 含 **CUL 75–3,000 kVA** 覆盖

### 采购信号
- **design-build 模式** ⇒ 承包商自行选型采购设备（非纯安装）
- Contact 页**公开投标邮箱** ⇒ 供应商入口开放
- **员工持股（ESOP，2008）** ⇒ 决策偏长期、重质量与员工利益，非纯低价导向
- 官网自述"Alberta's Largest Full Service Diversified Electrical Contractors" ⇒ 规模与项目体量支撑变压器需求

### 可利用的钩子（按强度排序）
1. **design-build + 公开投标邮箱** —— 供应商直接切入的正规入口（最强，且具体）
2. **员工持股公司（ESOP 2008）** —— 差异化角度（长期主义/共同利益）
3. **创始人 Mike Brunner 曾任 2006 年 ECAA 会长** —— 行业资历点，显示对方懂行
4. **1996 年创立、2026 年满 30 年** —— 时间点祝贺角度
5. 商业/市政基建/机构/轻工业的多元化项目组合 —— 对应用品切片

### 开发信建议
- **收件人策略**：主送 `estimating@alliedprojects.ca`，**正文首句请求转交给 Jason Lane（VP Operations）**（B档唯一合法用法：点名转交）。**不另发 Brian Reed / Brunner**（一家只发 1 人）。
- **发送时段**：卡尔加里（Mountain Time，9 月为 MDT=UTC-6）周二–周四上午 → **北京时间约 23:00–01:00**（北京=UTC+8，时差 14 小时）。
- **送达配置**：域走 **Proofpoint ARS 网关**（MX=`*.arsmtp.com`）⇒ **纯文本、少链接、无附件**，SPF/DKIM/DMARC 三件套须齐；**本域 SMTP 探测无效，不要据此判地址不存在**。
- **附件建议**：不带公司名录；如带，只带 UL 证书号（E541627）与容量区间。
- ⚠️ **不要写**：交期数字、价格词、`CSA Certified` / `SASO` / `SONCAP` / `YAWEI`。

### ⚠️ 矛盾点与风险提示
- **邮箱域 = 官网域**（alliedprojects.ca），一致 ✅ —— 但**只有角色邮箱**，无具名直邮（H6 风险，已在邮箱分档显式声明）。
- **MX 为 Proofpoint ARS**（`*.arsmtp.com`）：已知该网关对 RCPT 返回"转发式 250"（任何地址都 250）⇒ **SMTP 探测整体无效**，不得用探测结论判具名邮箱是否存在。
- Arpad Bencsik 仅命中 **LinkedIn 目录页**（非个人页），未采信为决策人。
- 官网标注 "© 2026 Allied Projects Ltd."，站点活跃；未见 link injection / 赌博外链。
- **同名风险**：存在另一家 `alliedprojectservices.ca`（Allied Project Services Ltd，地址 4304 Brentwood Green NW）—— **与本单不是同一主体**，勿混。

### 信息缺口清单（请勿编造）
- **Jason Lane 具名直邮**：未找到（禁止用 `jason.lane@` / `jlane@` 推演作主送）
- Jason Lane **任职起止时长**：未获取
- 公司**营收 / 员工精确数**：未回源（仅第三方 78–80 人）
- **NAICS / 州注册档案**：未查
- **常用变压器容量段 / 现有品牌**：未获取（首轮电话/回信确认）
- 采购是否集中在 estimating 岗：未明
- 个人 LinkedIn 直链：Brian Reed / Brunner 未取（仅团队页文字）

### 一句话画像
卡尔加里 30 年的 design-build 员工持股电气承包商 —— 投标邮箱对外开着门，先写 `estimating@` 请他们转给管运营的 VP Jason Lane。

### 渠道覆盖清单（L-1、L0–L7）
| 层 | 结果 | 一句话 |
|---|---|---|
| L-1 锁人 | ✅ | 官网团队页 7 人 + LinkedIn 双源，锁定 VP Operations Jason Lane |
| L0 官网 | ✅ | 首页/团队页/Contact 全取；邮箱仅 `estimating@` |
| L1 政府一手 | ⚠️ | 未查省注册；ECAA 会长（2006）为行业佐证 |
| L2 命名+DNS | ⚠️ | MX=Proofpoint ARS（探测无效）；无样本停推演 |
| L3 B2B库 | ⚠️ | RocketReach/CompanyListing 仅作规模旁证（未采信邮箱） |
| L4 社媒协会 | ✅ | LinkedIn 个人页 + 公司页；ECAA 关联 |
| L5 黄页同址 | ⚠️ | allbiz/companylisting 同址佐证；已辨同名 alliedprojectservices.ca |
| L6 电话表单 | ✅ | 403-543-4530 + Contact 表单（未拨打） |
| L7 付费 | ❌ | 未启用 |
