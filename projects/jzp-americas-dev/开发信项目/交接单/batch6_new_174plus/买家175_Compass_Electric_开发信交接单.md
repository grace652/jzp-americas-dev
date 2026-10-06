# 【买家 175】开发信交接单 — Compass Electric Ltd.

> 采集日期：2026-09-29 / 来源：batch6 名单（目标客户清单-batch6.csv 序 2）/ 一句话结论：温哥华岛（Victoria/Langford）市政与商业电气承包商（2011 创立，62 人规模），Director Brian Banner 具名邮箱 `brian@compasselectric.net` 经 SMTP 实测命中（250），A 档可直接主送。

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示(如有)
Compass Electric Ltd. | Brian Banner | Director（创始人） | brian@compasselectric.net | 已验证（SMTP 250 命中 + LinkedIn + 媒体报道三方） | linkedin.com/in/brian-banner-98099a93；公司页 linkedin.com/company/compass-electric-vi | 2011 年创立于 Victoria，62 名电工/学徒/办公人员，服务南温哥华岛住宅/商业/市政；Generac 供应商+安装商；街灯/临时供电/照明改造/太阳能/EV 充电/消防报警 | 官网 About+Contact 页 + LinkedIn + Business Examiner 报道 + SMTP 探测 + DNS | 邮箱域=官网域；MX=Proofpoint(ppe-hosted)；SPF 含 ppe-hosted + M365，`-all` 硬策略
```

## 二、补充信息（扩展段）

### 标准字段明细
- 国家+城市：加拿大 British Columbia — Victoria / Langford（南温哥华岛）
- 详细地址：110 – 1039 Langford Parkway, Victoria, BC V9B 0A5（cybo / cylex 目录）
- 电话：1-250-800-2169（官网 Contact 页明文）
- LinkedIn：个人 `ca.linkedin.com/in/brian-banner-98099a93`；公司 `ca.linkedin.com/company/compass-electric-vi`
- 网站：compasselectric.net
- 成立日：2011（Business Examiner 2021-03-31 报道原文 "Compass Electric was founded in 2011"）
- 规模：62 名电工、学徒与办公人员（Business Examiner 2021 报道口径；当前规模未获取）
- 营收：未获取
- NAICS：未获取
- 官网关联：与 Generac（发电机）、Gemstone Lights（户外照明）、Financeit（融资）有合作/推荐关系
- 官网列名协会：About 页 "Associations" 段自述 "aligned with industry leading organisations"（**未列具体协会名**）

### 联系人（含 still_here 在职核验）

| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| **Brian Banner**（主送） | 公司最高决策 / 创始人 | Director | 2011 创立至今（14+ 年） | LinkedIn 个人页现职 "Director - Compass Electric Ltd."；Business Examiner 2021 报道其为 Director；官网 About 页引述其本人表述 | 低 | ca.linkedin.com/in/brian-banner-98099a93 |
| Melissa Reay | 员工（备选，不发） | 未标注 | 未获取 | LinkedIn 显示 Experience: Compass Electric Ltd.（Victoria） | 未获取 | ca.linkedin.com/in/melissa-reay-b3417523a |

> 说明：官网无 Team/Leadership 页，仅 About 页无具名。经 LinkedIn 检索锁定 **Director Brian Banner**（创始人），并以 2021 年媒体报道交叉确认职务。按优先级落到 **老板/Owner** 层。

### 邮箱分档（A/B/C）
- **A 档（具名，主送）**：`brian@compasselectric.net` — Brian Banner（Director）
  - **SMTP 实测**（MX = `mx1-us1.ppe-hosted.com`，Proofpoint）：
    ```
    250  info@compasselectric.net          ← 控制地址（官网可推定为真）
    550  zzz_nonexistent_probe_9987@...    ← 随机地址 550 ⇒ 非 catch-all ✅
    550  john@compasselectric.net          ← 对照组 550 ✅
    550  sales@compasselectric.net         ← 对照组 550 ✅
    550  melissa@compasselectric.net       ← 对照 550（员工名无邮箱）
    250  brian@compasselectric.net         ← ⭐ 候选命中
    ```
    控制 250 + 随机 550 + 对照 550 + 候选 250 → **四条件同时成立，探测可信**。
  - 交叉印证：LinkedIn 现职 Director + Business Examiner 报道 Director → 人名/职务一致；域内唯一 "brian"。
  - 验证状态：**已验证**。
- **B 档（角色邮箱）**：`info@compasselectric.net`（SMTP 250，域内真实）—— 作点名转交入口或备选。
- **C 档**：无。
- **H6 声明**：不适用（已取得具名决策人邮箱）。

### 我为什么找他
- 官网 About 页**只有一段"我们是一站式电气承包商"的泛述、无具名团队**，但 Business Examiner 2021 的专访点名 *"Director **Brian Banner**, a hands-on leader"*，且该报道**直接引述他的原话**（"Our first large project was the BC Ambulance Dispatch Facility in Langford…"）—— 说明他是这家公司的对外代表与决策人。
- 其官网在运/已完成项目含 **Tesla Victoria、BC Ambulance Dispatch、Sooke Regional Library、多栋公寓与商业体**，并专营 **Street Lighting（市政/商业）** 与 **Temporary Power（含 distribution panels）** —— 临时供电的配电箱/变压器场景是可落地的开场观察。

### 买家类型 / 需求品类
- 买家类型：🔥 **B 型 —— 电气承包商**（住宅+商业+市政），非制造商、非分销商
- 需求品类（带结论态）：
  - `三相美变（UL E541627，可直供）` —— 商业/市政项目配电、临时供电配电箱配套
  - `单相柱上变（认证在办，条件切入）` —— 街灯/户外配电场景可条件提及
- ⛔ 不推：干变对美客户不谈（本案为加拿大客户，如被问可谈 built-to-CSA，但非首选）

### 电压·频率·认证要求
- 电压：未获取（官网未公开；服务含临时供电 distribution panels，推定中低压，**需电话确认**）
- 频率：60 Hz（加拿大）
- 认证：项目执行 CSA/加拿大电气规范；公司自述 "access to the best suppliers and manufacturers"（采购方视角，非制造方）

### 采购信号
- 专营 **Street Lighting（市政/商业）** 与 **Temporary Power** → 配电箱/变压器为项目必备物料
- 官网 About 自述 "continued business development plans in the works and numerous upcoming projects on its calendar… anticipates growing its clientele" → **扩张信号**
- 62 人规模 + 服务多类项目 → 常态采购
- 与 Generac 有供应商/安装商合作 → 已习惯与设备供应商建立供货关系（对"新增设备供应商"接受度较高）

### 可利用的钩子（按强度排序）
1. **Temporary Power + Street Lighting 专营** —— 直接对应配电箱/变压器场景（最强，可指名）
2. **BC Ambulance Dispatch Facility（2013 首个大项目）** —— 媒体报道中他亲口讲的招牌项目，可作"我读过你的故事"的开场
3. **官网自述扩张中（business development plans / upcoming projects）** —— 切入新供应商的时机
4. **Generac 合作经验** —— 说明其已有设备供应商协作惯例

### 开发信建议
- **收件人策略**：主送 `brian@compasselectric.net`（Brian Banner，Director，A 档）。**一家只发 1 人**。
- **送达配置**：MX = Proofpoint（`ppe-hosted.com`）+ 后端 M365；SPF 为 `include:_spf-us.ppe-hosted.com include:spf.protection.outlook.com -all`（硬策略）→ **必须用合规发件域 + SPF/DKIM/DMARC 三件套**；纯文本优先。
- **发送时段**：维多利亚（PT，UTC-8/-7）周二–周四 上午 09:00–11:00 ≈ 北京时间 次日 01:00–03:00（夏令时）。
- **附件建议**：首封不带供货名录/PDF；可提及 UL 证书号与容量区间。
- **备注**：邮箱域 = 官网域（compasselectric.net），无需换域。

### ⚠️ 矛盾点与风险提示
- ⚠️ **官网 About 无具名团队、无 Team 页** → 人名全部来自 LinkedIn + 2021 年媒体；**任职信息以 2021 年为基准**，虽 LinkedIn 显示现职，仍建议发送前留意是否有变动。
- ⚠️ **公司规模为 2021 年口径（62 人）**，当前规模未获取，勿在信中引用具体人数。
- ⚠️ 公司名 "Compass Electric" 在北美多处重名（如美国 Compass Electric）—— 本案主体为 **BC Victoria 的 Compass Electric Ltd.**（域 compasselectric.net），勿混。
- ⚠️ 首封红线：不写交期数字、不写价格词、不提 CSA Certified / SASO / SONCAP / YAWEI。

### 信息缺口清单（请勿编造）
- Brian Banner 的**任职起止精确日期**：未获取
- 公司**当前规模 / 年营收 / NAICS**：未获取
- **常用变压器容量、电压等级、品牌**：未获取（需电话确认）
- **采购/估料对接人**：官网未公开，未找到
- **官网所列协会的具体名称**：官网只写 "Associations" 未列名，未获取
- Brian Banner 的**个人邮箱以外的联系方式**：未获取

### 一句话画像
温哥华岛的一站式电气承包商（2011，62 人），靠街灯与临时供电吃饭，创始人 Brian Banner 亲自在 LinkedIn 上挂着 Director 头衔——`brian@` 直邮实测可达。

### 渠道覆盖清单（L-1、L0–L7）
| 层 | 结果 | 一句话 |
|---|---|---|
| L-1 锁人 | ✅ | LinkedIn 锁定 Director Brian Banner + 2021 媒体报道交叉 |
| L0 官网 | ✅ | About/Contact/服务/项目全取；**无 Team 页、无具名邮箱** |
| L1 政府一手 | ⚠️ | 未查 BC 注册库；cybo/cylex 目录给出地址 |
| L2 命名+DNS | ✅ | MX=Proofpoint；**SMTP 四条件成立，brian@ 实测 250** |
| L3 B2B 库 | ⚠️ | D&B/Crunchbase 有公司档案（未取具名邮箱） |
| L4 社媒协会 | ✅ | LinkedIn 个人页 + 公司页；Business Examiner 报道 |
| L5 黄页同址 | ✅ | cybo / cylex 地址交叉（1039 Langford Parkway） |
| L6 电话表单 | ✅ | 1-250-800-2169 + 官网表单（未拨打） |
| L7 付费 | ❌ | 未启用 |

---

- 发信资格：✅ 通过（核心字段齐、still_here 四栏齐、有「我为什么找他」与缺口清单）
- 邮箱档位：**A（具名，SMTP 实测命中 + 三方交叉）**
- ⓪ 层反身排除：**PASS** —— 官网自述 *"We consider ourselves to be a **one-stop electrical contractor**, with access to the best suppliers and manufacturers in the industry"*（"manufacturers" 出现在**其采购来源**语境，非自称制造）；服务为安装/施工/服务类（街灯、临时供电、发电机安装、照明改造、太阳能、EV 充电、消防报警）⇒ **承包商客户，非竞品**。
