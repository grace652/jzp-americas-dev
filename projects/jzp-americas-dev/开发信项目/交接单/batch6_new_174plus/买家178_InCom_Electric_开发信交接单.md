# 【买家 178】开发信交接单 — InCom Electric Corp.

> 采集日期：2026-09-29 / 来源：batch6 名单（目标客户清单-batch6.csv 序 5）/ 一句话结论：Calgary 工业与商业电气承包商（2007 创立，Co-Founder 家族/合伙人体制，COR+CFAA 认证），President & Co-Founder Dustin Owens 具名邮箱 `dowens@incomelectric.com` 经 SMTP 实测命中（250，并以其兄弟 `towens@` 印证命名规则），A 档可直接主送。

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示(如有)
InCom Electric Corp. | Dustin Owens | President & Co-Founder | dowens@incomelectric.com | 已验证（SMTP 250 命中 + 命名规则印证 + 官网/ LinkedIn 职务） | linkedin.com/in/dustin-owens-206b98148；公司页 linkedin.com/company/incom-electric-corp | 2007 创立于 Calgary，工业/商业/市政/废水/油气电气承包 + 生命安全系统，21 员工（峰值 125），最大合同 $4M+，COR+CFAA 认证 | 官网 About(Leadership Team)/Contact + LinkedIn ×4 + RocketReach + ContactOut + SMTP 探测 + DNS | 邮箱域=官网域；MX=Google Workspace；SPF `~all`（软策略，注意送达）
```

## 二、补充信息（扩展段）

### 标准字段明细
- 国家+城市：加拿大 Alberta — Calgary
- 详细地址：
  - 官网页脚：5740 Burbank Crescent SE, Calgary, AB T2H 1Z6
  - 目录另载：4301G – 9 Street SE, Calgary, AB T2G 3C8（ContactOut）——**两址并存，需电话确认**
- 电话：403-455-6515（官网页脚明文）
- 邮箱（角色）：sales@incomelectric.com（官网 About 页 "GET IN TOUCH" 链接明文）
- LinkedIn：Dustin Owens `linkedin.com/in/dustin-owens-206b98148`；Todd Owens `linkedin.com/in/todd-owens-5050937b`；Todd Sumner `linkedin.com/in/todd-sumner-62135714a`；Tony Sutton `linkedin.com/in/tony-sutton-2b1b7b148`；Warren Immerkar `linkedin.com/in/warren-immerkar-29038814a`；公司 `linkedin.com/company/incom-electric-corp`
- 网站：incomelectric.com（Wix 建站）
- 成立日：2007（官网 About "InCom was founded in 2007"；页脚 "InCom_EST 2007"）
- 规模：21 名员工（ContactOut）；官网自述 "Manpower peak: 125"
- 营收：未获取（官网自述 "Largest contract: +$4M"）
- NAICS：未获取
- 认证：**COR（Certificate of Recognition）**、**CFAA（Canadian Fire Alarm Association）**（官网 About 明文）
- 里程碑（官网自述）：Largest contract +$4M / Manpower peak 125 / Gain ownership of Head Office

### 联系人（含 still_here 在职核验）

| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| **Dustin Owens**（主送） | 公司最高决策 / 创始人 | President & Co-Founder | 2007 创立至今（19 年） | 官网 Leadership Team 页在列（含本人自述）；LinkedIn 现职 "President at InCom Electric Corp"；RocketReach 现职一致 | 低 | ca.linkedin.com/in/dustin-owens-206b98148 |
| Todd Owens | 创始人（备选，不发） | Co-Founder | 2007 创立至今 | 官网 Leadership Team 页在列；LinkedIn 现职 | 低 | linkedin.com/in/todd-owens-5050937b |
| Todd Sumner | 副总裁兼施工经理（备选，不发） | Vice President & Co-Founder | 2007 创立至今 | 官网 Leadership Team 页在列；LinkedIn 现职 | 低 | ca.linkedin.com/in/todd-sumner-62135714a |
| Tony Sutton | 服务协调（备选，不发） | Service Coordinator | 9 年 | 官网 Leadership Team 页在列 | 低 | ca.linkedin.com/in/tony-sutton-2b1b7b148 |
| Warren Immerkar | 估料（备选，不发） | Estimator | 8 年 | 官网 Leadership Team 页在列 | 低 | ca.linkedin.com/in/warren-immerkar-29038814a |

> 说明：官网有完整 **Leadership Team** 页（第一方）。按选人优先级，估料岗（Warren Immerkar, Estimator）最贴近采购/规格对接，但为**非决策的支撑岗**；**President & Co-Founder Dustin Owens** 为最终决策人且邮件实测可达 → 定为**主送 1 人**。其余 4 人**不并发发送**（一家只发 1 人）。

### 邮箱分档（A/B/C）
- **A 档（具名，主送）**：`dowens@incomelectric.com` — Dustin Owens（President & Co-Founder）
  - **SMTP 实测**（MX = `aspmx.l.google.com`，Google Workspace）：
    ```
    250  sales@incomelectric.com             ← 控制地址（官网明文，真实）✅
    550  zzz_nonexistent_probe_9987@...      ← 随机地址 550 ⇒ 非 catch-all ✅
    550  zzz_random_ab12@incomelectric.com   ← 随机 550（第二轮复测一致）✅
    550  john.smith@incomelectric.com        ← 对照组 550 ✅
    550  dustin@incomelectric.com            ← {firstname}@ 不成立
    550  dustin.owens@incomelectric.com      ← {first}.{last}@ 不成立
    550  d.owens@incomelectric.com           ← {f}.{last}@ 不成立
    550  owens@incomelectric.com             ← {last}@ 不成立
    250  dowens@incomelectric.com            ← ⭐ 候选命中
    250  towens@incomelectric.com            ← ⭐ 其兄 Todd Owens 命中 ⇒ 印证命名规则 = {f}{last}@
    ```
    控制 250 + 随机 550 + 对照 550 + 候选 250 → **四条件同时成立，探测可信**；且 **`towens@` 同步命中**，**独立印证了本域命名规则为 `{首字母}{姓}@`**（Todd Owens 亦为 Owens 姓），使 `dowens@` 的归属判定更稳。
  - 交叉印证：官网 Leadership Team 页具名 President & Co-Founder + LinkedIn 现职 + RocketReach 现职 → 人名/职务三方一致。
  - 验证状态：**已验证**。
- **B 档（角色邮箱）**：`sales@incomelectric.com`（官网明文，SMTP 250）—— 作点名转交入口或备选。
- **C 档**：无。
- **H6 声明**：不适用（已取得具名决策人邮箱）。

### 我为什么找他
- 官网 About 页有完整 **"OUR LEADERSHIP TEAM"**（第一方），Dustin Owens 的条目写明 *"I am proud to be a founder of InCom… My prized project is a design/build modular building for a remote water treatment plant in Northern Alberta. From creating the initial design, through construction, **helicopter transport**, and commissioning"* —— 一个能描述"直升机吊运预制模块到偏远水处理厂"的创始人，说明其项目覆盖偏远/工业场景，**配电设备为必备物料**。
- 且他是 "InCom's **special projects expert**"（Master Electrician），官网列出的项目含 **Bonnybrook Wastewater Treatment Plant、YYC Glycol Recycling Facility、Stewart Creek Lift Station** 等市政/工业设施 —— 这类项目必然涉及中低压配电与变压器，是可落地的开场观察。

### 买家类型 / 需求品类
- 买家类型：🔥 **B 型 —— 电气承包商**（工业/商业/市政），非制造商、非分销商
- 需求品类（带结论态）：
  - `三相美变（UL E541627，可直供）` —— 工业/市政设施（废水处理、提升泵站、厂房）配电主谈品类
  - `单相柱上变（认证在办，条件切入）` —— 偏远/临时场景可条件提及
  - `主变（产能可覆盖，UL 区间外，需人工确认）` —— 若涉较大容量工业配电，需人工确认
- ⛔ 不推：干变对美客户不谈（本案为加拿大客户，如被问可谈 built-to-CSA，但非首选）

### 电压·频率·认证要求
- 电压：未获取（官网未公开常做电压等级；项目含废水厂、泵站、冷库设计建造，推定中低压，**需电话确认**）
- 频率：60 Hz（加拿大）
- 认证：项目执行 CSA/加拿大电气规范；公司持 **COR** 与 **CFAA**（消防报警，非产品认证）

### 采购信号
- **多行业覆盖**（工业/商业/市政/废水/油气/食品饮料）+ **设计-建造（design-build）能力** → 项目型采购，变压器为直接物料
- **模块化/撬装（modular & skid construction）** → 预制配电单元，标准化采购倾向强
- **增长轨迹**：Manpower peak 125、最大合同 +$4M、自购总部（"Gain ownership of Head Office"）→ 扩张中
- **官网明确列 "Estimator" 岗位**（Warren Immerkar）→ 有专职估料/报价职能，说明其有规范化的采购/报价流程

### 可利用的钩子（按强度排序）
1. **设计-建造 + 模块化/撬装（modular & skid construction）** —— 预制配电单元直接消耗变压器（最强，可指名）
2. **废水/市政/泵站项目**（Bonnybrook WWTP、Stewart Creek Lift Station）—— 基础设施配电场景
3. **President 本人自述的"直升机吊运预制模块"招牌项目** —— 极具辨识度的"我读过你的故事"开场素材
4. **自购总部 + 峰值人力 125 + $4M 合同** —— 稳健成长型买家，适合长线

### 开发信建议
- **收件人策略**：主送 `dowens@incomelectric.com`（Dustin Owens，President & Co-Founder，A 档）。**一家只发 1 人**，不并发 Todd Owens / Todd Sumner / Warren Immerkar。
- **送达配置**：MX = Google Workspace；SPF = `v=spf1 include:_spf.google.com ~all`（**软策略 `~all`**）→ 我方发件域须自建 SPF/DKIM/DMARC 三件套（尤其 DMARC），避免被 Gmail 侧降权；纯文本优先。
- **发送时段**：卡尔加里（MT，UTC-7/-6）周二–周四 上午 09:00–11:00 ≈ 北京时间 次日 00:00–02:00（夏令时）。
- **附件建议**：首封不带供货名录/PDF；可提及 UL 证书号与容量区间。
- **备注**：邮箱域 = 官网域（incomelectric.com），无需换域。

### ⚠️ 矛盾点与风险提示
- ⚠️ **两个地址并存**（5740 Burbank Crescent SE vs 4301G – 9 Street SE）→ 寄样/上门前须电话确认实际经营地。
- ⚠️ **同名主体**：检索 "InCom" 会命中 IT/咨询类公司（如 InCom 其他实体）—— 本案主体为 **Calgary 的 InCom Electric Corp.**（incomelectric.com），勿混。
- ⚠️ **规模口径不一**：ContactOut 称 21 员工，官网自述峰值 125 → **勿在信中引用人数**。
- ⚠️ 首封红线：不写交期数字、不写价格词、不提 CSA Certified / SASO / SONCAP / YAWEI。

### 信息缺口清单（请勿编造）
- **常用变压器容量、电压等级、品牌**：未获取（需电话确认）
- 公司**年营收 / NAICS**：未获取
- **实际经营地址**（两址并存）：需电话确认
- **Dustin Owens 的任职起止精确日期**：未获取（仅知 2007 创立至今）
- **采购/供应商对接人的专门岗位**：官网仅见 Estimator（Warren Immerkar），**是否有专职 Purchasing 未明**
- **联系邮箱以外的直接电话/手机**：未获取（仅有公司总机 403-455-6515）

### 一句话画像
Calgary 一家从废水厂、泵站到冷库设计建造通吃的工业电气承包商（2007，COR+CFAA，还自购了总部）——创始人 Dustin Owens 的 `dowens@` 直邮实测可达，且规则已被其兄弟的邮箱印证。

### 渠道覆盖清单（L-1、L0–L7）
| 层 | 结果 | 一句话 |
|---|---|---|
| L-1 锁人 | ✅ | 官网 Leadership Team 页第一方锁定 5 人；President Dustin Owens 定为主送 |
| L0 官网 | ✅ | About(Leadership Team)/服务/项目/认证全取；页脚 sales@ + 电话 + 地址 |
| L1 政府一手 | ⚠️ | 未查 AB 注册库；ContactOut 给出第二地址 |
| L2 命名+DNS | ✅ | MX=Google Workspace；**四条件成立 + towens@ 印证 {f}{last}@ ⇒ dowens@ 实测命中** |
| L3 B2B 库 | ⚠️ | RocketReach / ContactOut 现职旁证（不作印证主力） |
| L4 社媒协会 | ✅ | LinkedIn 公司页 + 5 名成员个人页（官网直接给出） |
| L5 黄页同址 | ⚠️ | cylex 等目录给出地址；两址不一致待确认 |
| L6 电话表单 | ✅ | 403-455-6515 + 官网表单（未拨打） |
| L7 付费 | ❌ | 未启用 |

---

- 发信资格：✅ 通过（核心字段齐、still_here 四栏齐、有「我为什么找他」与缺口清单）
- 邮箱档位：**A（具名，SMTP 实测命中 + 命名规则独立印证）**
- ⓪ 层反身排除：**PASS** —— 官网自述 *"InCom Electric Corp. is an **industrial and commercial electrical contractor**"*，*"We undertake construction and service projects of all scopes and sizes"*；服务为 Full service electrical contracting / Life safety systems / Electrical service，**无任何制造、工厂、OEM 或代理变压器品牌（含 YAWEI）表述** ⇒ **承包商客户，非竞品**。
