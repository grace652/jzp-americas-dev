# 【买家 174】开发信交接单 — Sasco Contractors Ltd.

> 采集日期：2026-09-29 / 来源：batch6 名单（目标客户清单-batch6.csv 序 1）/ 一句话结论：BC 最大电气承包商之一（1985 创立，200+ 人，Burnaby/Kamloops/Langford 三办公室），"A" Licensed 全服务电气与通信承包；总统 Craig Paquin 具名邮箱见企业自撰文档明文（A 档），但本机 SMTP 因 SpamTitan 网关 Spamhaus PBL 拦截无法复核。

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示(如有)
Sasco Contractors Ltd. | Craig Paquin | President（兼 Principal） | cpaquin@sascocontractors.com | 已验证（企业自撰文档明文 + B2B 旁证；SMTP 因网关拦截未复核） | linkedin.com/company/sasco-contractors（个人页直链未取，见缺口） | 1985 创立，BC 全服务电气与通信承包商，200+ 人，Burnaby 总部 + Kamloops + Vancouver Island(Langford)，COR 认证 15+ 年，数据中心/配电升级/HVAC 电气化项目 | 官网 Leadership 页 + 官网 Contact 页 + 企业自撰赞助商简介 PDF + RocketReach 旁证 + City of Burnaby 执照库(opengovca) + DNS | 邮箱域=官网域；邮件走 SpamTitan 网关，后端 M365 且 RestrictDomainsToIPAddresses → 送达须走正规 ESP
```

## 二、补充信息（扩展段）

### 标准字段明细
- 国家+城市：加拿大 British Columbia — Burnaby（大温总部）+ Kamloops（内陆）+ Langford（温哥华岛）
- 详细地址：
  - Burnaby 总部：114 – 3060 Norland Avenue, Burnaby, BC V5B 3A6
  - Kamloops：961C Laval Crescent, Kamloops, BC V2C 5P4
  - Vancouver Island（Langford）：101 – 2785 Leigh Road
- 电话：604.299.1640（Burnaby）/ 250.828.0605（Kamloops）/ 250.940.4000（Langford）；Fax 604.299.1688
- LinkedIn：公司页 `linkedin.com/company/sasco-contractors`（另 `sg.linkedin.com/company/sasco-contractors`）
- 网站：sascocontractors.com
- 成立日：1985（官网自述 "Family owned and growing for 40 years"）
- 规模：200+ 人（官网 Leadership 页 "employing more than 200 people"）
- 营收：未获取
- NAICS：未获取（BC 市政执照分类为 "Electrical Contractor" / "Contractor's Shop and Yard"）
- 资质：COR Certified by WorkSafeBC（15+ 年，"one of the first electrical contractors in the province to receive certification"）；官网自述 `"A" Licensed full-service electrical contractor`
- 执照（一手源）：City of Burnaby 营业执照 **#00150411**，Trade Name `SASCO`，Account Name `SASCO CONTRACTORS LTD`，类型 Contractor's Shop and Yard，2026-01-01 至 2026-12-31，状态 **APPROVED**（opengovca 镜像）

### 联系人（含 still_here 在职核验）

| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| **Craig Paquin**（主送） | 公司最高决策 / 对外联络人 | President（兼 Principal） | President 13 年；行业 23 年 | 官网 Leadership 页在列；RocketReach 现职 "President, Principal at Sasco Contractors"（Burnaby, BC） | 低 | 未取（个人 LinkedIn 直链未获取，见缺口） |
| Reid Hockin | 运营一把手（备选，不发） | VP – General Manager（Principal） | 2000 年入职；2022 起任 VP-GM | 官网 Leadership 页在列；RocketReach 现职 | 低 | 未取 |
| Jeff Bedry | 现场运营 | VP Field Operations（Principal） | 1992 年起（30+ 年） | 官网 Leadership 页在列 | 低 | 未取 |
| Amanda Koning | 财务与行政 | VP Finance & Administration（CPA/CPHR） | 未获取 | 官网 Leadership 页在列 | 低 | 未取 |
| Chris Findlater | 业务发展 | VP Business Development | 2021 年加入（30+ 年行业） | 官网 Leadership 页在列 | 低 | 未取 |

> 说明：Sasco 官网无 Procurement / Purchasing 岗位公开。按选人优先级（采购岗 > 国际销售 > 品类经理 > 老板/Owner > 普通顾问）落到 **老板/Owner** 层 → 选 President Craig Paquin。Reid Hockin（VP-GM，管全盘运营）为备选，**不并发发送**（一家只发 1 人）。

### 邮箱分档（A/B/C）
- **A 档（具名，主送）**：`cpaquin@sascocontractors.com` — Craig Paquin（President）
  - 来源 1（一手文档明文）：企业自撰赞助商简介 PDF，原文 *"If you want to get in touch with us, please email **Craig Paquin at cpaquin@sascocontractors.com** for more information."*（golfgroupmanager 托管的赛事赞助商手册，内容由 Sasco 自撰）
  - 来源 2（旁证，B2B）：RocketReach 个人页显示 Craig Paquin 现任 President/Principal at Sasco Contractors
  - 验证状态：**已验证（文档明文 + 旁证）**；🔴 **SMTP 未能复核** —— 该域 MX = `activeco-mx1/2.titanhq.com`（SpamTitan 网关），对本机来源 IP 返回 `554 5.7.1 ... blocked using zen.spamhaus.org; Listed by PBL`；直连后端 `sascocontractors-com.mail.protection.outlook.com` 返回 `550 5.7.51 TenantInboundAttribution`（租户设了 partner connector / RestrictDomainsToIPAddresses）。**网关拦截 ≠ 地址不存在**，不据此判否。
- **B 档（角色邮箱）**：`info@sascocontractors.com`（Burnaby 总部）/ `kamloops@sascocontractors.com` / `vanisle@sascocontractors.com` —— 官网 Contact 页明文（一手源）。仅作点名转交入口或备选。
- **C 档**：无。
- **H6 声明**：不适用（已取得具名决策人邮箱，非仅角色邮箱）。

### 我为什么找他
- 官网 Leadership 页明确 Craig Paquin 是 **President**，且企业自撰的对外简介里**留的就是他的邮箱**作为业务咨询入口 —— 说明他是这家 200+ 人承包商的**对外决策触点**，不是随机挑的高管。
- 他 "oversaw the growth and evolution of a 10-person company into a multi-disciplined, full-service electrical contractor employing more than 200 people"，且官网在运项目含 **Data Centre / Distribution Upgrades / HVAC Electrification** —— 这三类都直接消耗配电变压器，是可落地的开场观察。

### 买家类型 / 需求品类
- 买家类型：🔥 **B 型 —— 电气承包商（EPC/施工方）**，非制造商、非分销商（⓪ 层判定见下）
- 需求品类（带结论态）：
  - `三相美变（UL E541627，可直供）` —— 数据中心/商业楼宇配电升级、配电室改造的主谈品类
  - `单相柱上变（认证在办，条件切入）` —— 若涉户外/临时供电场景，仅条件性提及
- ⛔ 不推：干变（对美客户不谈；对加客户如被问可谈 built-to-CSA，但不作首选钩子）

### 电压·频率·认证要求
- 电压：未获取（官网未公开常做电压等级；其项目含数据中心与配电升级，推定中低压配电，**需电话确认**）
- 频率：60 Hz（加拿大）
- 认证：项目执行标准为 CSA/加拿大电气规范体系；Sasco 自身持 WorkSafeBC COR 安全认证（非产品认证）

### 采购信号
- 三办公室（Burnaby / Kamloops / Langford）+ 200+ 人 → 项目型采购频次高，配电设备为常态消耗
- 在运项目类型：Data Centre、Distribution Upgrades、HVAC Electrification、Energy Efficiency → 变压器为直接物料
- 官网设 `services-request` 入口 → 有规范化接单流程，非纯手工作坊
- 家族企业 + 40 年 + 明确 succession（Hank→Brian→Craig + 4 位 principal）→ 决策链稳定、关系导向（"relationship-based contractor"）

### 可利用的钩子（按强度排序）
1. **官网在运项目类型**：Data Centre / Distribution Upgrades / HVAC Electrification —— 直接对应配电变压器用量（最强，可指名）
2. **"A" Licensed + COR 15 年 + 200+ 人**：合规与规模匹配，可谈供货资质对等
3. **家族 40 年 + relationship-based**：关系导向型买家，适合长线培育
4. **三地办公室覆盖 BC 全域**：单点成交可辐射内陆与温哥华岛

### 开发信建议
- **收件人策略**：主送 `cpaquin@sascocontractors.com`（Craig Paquin，President，A 档）。**一家只发 1 人**，不并发 Reid Hockin。
- **送达配置**：🔴 该域经 SpamTitan 网关 + 后端 M365（RestrictDomainsToIPAddresses）→ **必须走正规 ESP/合规发件域**，SPF/DKIM/DMARC 三件套齐；**纯文本优先**，避免营销化模板触发网关拦截。首封后关注退信与灰名单延迟（SpamTitan 有 greylisting 特征）。
- **发送时段**：温哥华（PT，UTC-8/-7）周二–周四 上午 09:00–11:00 ≈ 北京时间 次日 01:00–03:00（夏令时）。
- **附件建议**：首封不带供货名录/PDF；可提及 UL 证书号与容量区间（不带附件）。
- **备注**：邮箱域 = 官网域（sascocontractors.com），无需换域。

### ⚠️ 矛盾点与风险提示
- 🔴 **SMTP 无法复核**（SpamTitan 网关 Spamhaus PBL 拦本机 IP + M365 租户 RestrictDomainsToIPAddresses）→ `cpaquin@` 的**可投递性未实测**，仅凭文档明文 + 旁证采信；发送前建议先用正规 ESP 做一次小规模投递观察退信。
- ⚠️ **同名主体陷阱**：检索 "SASCO" 会命中另一家 **SASCO（linkedin.com/company/sasco，招聘 Electrical Estimators）** 及 RocketReach "SASCO Management Team（Glen Kucera / Clayton Tanaka）" —— **均非本案主体**，本案主体是 BC 的 **Sasco Contractors Ltd.**，勿混。
- ⚠️ 官网 Contact 页出现 "A" Licensed 与 `A` 加引号写法，属其自述资质表述，引用时照原文，勿改写成我方认证。
- ⚠️ 首封红线：不写交期数字、不写价格词、不提 CSA Certified / SASO / SONCAP / YAWEI。

### 信息缺口清单（请勿编造）
- Craig Paquin 的**个人 LinkedIn 直链**：未获取（仅有 RocketReach 与公司页）
- Craig Paquin 的**任职起止精确日期**：未获取（仅"13 年任 President"）
- Sasco 的**常用变压器容量/品牌/电压等级**：未获取（需电话确认）
- Sasco 的**年营收 / NAICS 代码**：未获取
- **采购/估料对接人**（Estimator / Purchasing）：官网未公开；LinkedIn 检索到 Project Manager/Estimator 岗位（如 Claudio Canosa、Gabe Robles），但**均为第三方快照、未经在职核验，不采用**
- **邮箱可投递性**：未实测（网关拦截）

### 一句话画像
BC 最大电气承包商之一（1985，200+ 人，三地办公）的总统 Craig Paquin 亲自挂在对外咨询邮箱上——数据中心与配电升级项目在跑，是配电变压器的常态消耗方。

### 渠道覆盖清单（L-1、L0–L7）
| 层 | 结果 | 一句话 |
|---|---|---|
| L-1 锁人 | ✅ | 官网 Leadership 页 5 人全锁；President Craig Paquin 定为主送 |
| L0 官网 | ✅ | Leadership + Contact（info@/kamloops@/vanisle@）+ 业务/项目/历史全取 |
| L1 政府一手 | ✅ | City of Burnaby 执照 #00150411 APPROVED（opengovca 镜像）；MRAS 加拿大注册库可查 |
| L2 命名+DNS | ⚠️ | MX=SpamTitan 网关→后端 M365(RestrictDomainsToIPAddresses)；无样本故不推演命名规则 |
| L3 B2B 库 | ⚠️ | RocketReach 现职旁证（不作印证主力） |
| L4 社媒协会 | ✅ | LinkedIn 公司页；ECABC 名录有 Sasco (Kamloops) 条目（未含具名邮箱） |
| L5 黄页同址 | ✅ | opengovca 同址交叉（3060 Norland Ave #114） |
| L6 电话表单 | ✅ | 三地电话 + services-request 表单（未拨打） |
| L7 付费 | ❌ | 未启用 |

---

- 发信资格：✅ 通过（核心字段齐、still_here 四栏齐、有「我为什么找他」与缺口清单）
- 邮箱档位：**A（具名，文档明文；可投递性未实测）**
- ⓪ 层反身排除：**PASS** —— 官网自述 *"full-service electrical contractor"* / *"the proud sector leader in electrical project delivery"*，服务为 Construction & Upgrades / Service & Maintenance / Fire Alarm / Datacomms，**无任何制造、工厂、OEM 或代理变压器品牌（含 YAWEI）表述** ⇒ 承包商客户，非竞品。
