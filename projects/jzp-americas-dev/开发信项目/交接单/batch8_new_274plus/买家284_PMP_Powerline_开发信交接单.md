# 【买家 284】开发信交接单 — PMP Powerline Construction Ltd.

> 采集日期：2026-10-01 ｜ 来源：batch8 名单（pmppowerline.ca，SK）｜ 一句话结论：**萨省 Assiniboia 的电力线路施工承包商（1991 年由四位合伙人创立，现为 Rick Moore 与 Clayton Pinfold 各持 50%），主营架空/地下电力线路的建设与维护，客户含 SaskPower、市政电力、矿业、油田、农村与变电站 —— 官网 About 页第一方点名「co-owner Clayton Pinfold」并公布其具名邮箱 `cpinfold@pmppowerline.ca`，且 SMTP RCPT 实测 250 命中 = A 档 → 可主送。**
> ⚠️ 本表严格区分「已验证」与「未获取」；未找到的信息一律标注，不做推断填充。
> ✅ **本单过 A 档**：邮箱为**具名 + 官网一手源 + SMTP 实测命中**三源，可作主送。
> ⚠️ **MX 自指向**（`0 pmppowerline.ca.`）—— 但**实测该域由 Blacksun Exim 服务器收信、RCPT 返回 250**，**投递前仍需在发送环节复验**（见风险段）。

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示
PMP Powerline Construction Ltd. | Clayton Pinfold | Co-owner / Owner-Operator（与 Rick Moore 各持 50%）| `cpinfold@pmppowerline.ca`（**A 档具名，官网 About 页一手源 + SMTP 250 命中**）| **已验证**（官网 About 页明文 `- or - cpinfold@pmppowerline.ca` + SMTP RCPT 250（控制组 250 / 随机 550 对照成立））| 未找到（公司/个人 LinkedIn 均未检索到）| 萨省 Assiniboia 的**电力线路施工承包商**（1991 年四位合伙人创立），主营**架空/地下电力线路建设与维护**，客户含 **SaskPower、市政电力、矿业（煤/钾盐）、油田、农村、变电站**；30+ 员工；ISN Networld 认证 + Heavy Construction Safety Association 会员 | 官网 home / about / contact 实抓 + BBB 档案 + DNS(MX/A/SPF) + SMTP RCPT 实测 | ⚠️ **承包商（非制造/非竞品）**；⚠️ MX 自指向需投递复验；正文不引用员工数/成立年份

## 二、补充信息（扩展段）

### 标准字段明细
- 国家+城市：**加拿大 Saskatchewan**（Assiniboia，萨省中南部）；另有 **Gull Lake** 与 **Pilot Butte** 两个卫星车间
- 详细地址：**Po Box 550, Assiniboia, Saskatchewan S0H 0B0**（官网 About/contact 页）
- 电话：**306-642-3547**；传真 **306-642-5299**
- LinkedIn：**未找到**（公司页与个人页均未检索到）
- 网站：**www.pmppowerline.ca**（邮箱域 = 官网域 `pmppowerline.ca` ✅）
- 成立日：**1991 年**（官网 About 页「started in 1991 by four partners with a combined total of 62 years experience in the Line Trade」）—— 一手源，**可引用**
- 规模：**30+ 员工**（官网 About 页自述「over 30 employees」；⚠️ **正文不引用具体数字**）
- 法人主体：**P.M.P. Powerline Construction Ltd.**（官网署名；CSV 全称 PMP Powerline Construction Ltd.）
- 执照：**ISN Networld 认证** + **Heavy Construction Safety Association** 会员（官网自述）；⚠️ 萨省企业注册号未查

### 联系人（含 still_here 在职核验）
| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| **Clayton Pinfold（本次主送）** | Co-owner（与 Rick Moore 各持 50%），Owner/Operator | 官网 About 页：「The current owner/operators of the company are **Rick Moore and Clayton Pinfold**, each owning a 50% share」 | **未获取**（公司 1991 创立，其本人任期未知）| 高：官网 About 页现行点名 + **SMTP RCPT 250 命中（邮箱在役）** + BBB 档案在列 | **低**（官网一手点名 + SMTP 命中 + BBB，三源）| 未找到 |
| Rick Moore（第二 owner，无邮箱）| Co-owner / Owner-Operator | 官网 About 页 + BBB 档案「Principal Contacts: Rick Moore, Owner/Operator」 | 未获取 | 高 | 低 | 未找到 |

> 🔴 **一家只发 1 人**：主送 **Clayton Pinfold**——**唯一有具名邮箱的 owner**（官网一手源 + SMTP 命中）。
> ⚠️ **Rick Moore 是 BBB 的 Principal Contact 但无公开邮箱** → 若 Clayton 渠道退信，可电话 **306-642-3547** 找 Rick。
> 🔴 **两位 owner 同属一家公司** → **只发 1 人，不拆成 2 个机会**。

### 邮箱分档（A/B/C）
- **A 档（具名决策人邮箱，已验证）**：✅ **`cpinfold@pmppowerline.ca`** —— 来源① **官网 About 页 mailto 明文**（`- or - cpinfold@pmppowerline.ca`，**一手源**）；来源② **SMTP RCPT 实测 250 命中**（同一轮：控制组 `pmp@` 250 / 随机地址 550 / 候选 250，**三者同时成立 ⇒ 探测有效**）。**双源（一手 + SMTP）⇒ H5 顶格达标**
- **B 档**：`pmp@pmppowerline.ca`（官网 Contact 页角色邮箱）
- **主送路径**：**`cpinfold@pmppowerline.ca`（A 档，可主送）**；辅以电话 **306-642-3547** 跟进
- ✅ **H3 说明**：邮箱来自**官网一手源 + SMTP 实测**，**非单一来源**；**已验证**。
- 🔴 **MX 实测**：`pmppowerline.ca` MX = **`0 pmppowerline.ca.`（自指向）** —— 三解析器（8.8.8.8 / 1.1.1.1 / 9.9.9.9）一致。**A 记录 `69.27.101.4`**；**实测 25 端口连通，返回 `220-cp1014.blacksun.ca ESMTP Exim 4.100.1`**（Blacksun 托管 Exim）⇒ **MX 自指但域真实收信**。SPF = `v=spf1 +mx +a +ip4:69.27.101.4 +ip4:69.27.96.200 +ip4:69.27.97.200 +include:_spf.google.com ~all`（⚠️ 含 `_spf.google.com`，但 MX 不在 Google）。
- ⚠️ **收信域可靠性**：该域由 **Blacksun（萨省 ISP）共享 Exim 服务器**托管 —— **非 Google/M365**，属**小厂自建邮局**类型 ⇒ **RCPT 探测有效**（本单已验证），但**送达信誉/容量弱于大厂** ⇒ **投递前需在发送环节复验**（见风险段）。

### 我为什么找他
- 官网首页明述 **「PMP Powerline offers maintenance and construction services for both overhead and underground power utilities. We have clients in several different lines of business including city power utilities, mining, oil well leases, rural, **substations** and Saskatchewan power utilities.」** —— **直接列出「substations（变电站）」作为业务线与客户类型** ⇒ **变电站建设/维护 = 明确的变压器采购场景**。
- 官网 About 页明述 **1991 年由四位线路行业（Line Trade）合伙人创立，客户含 SaskPower、Swift Current 市、CP 铁路、SaskTel、煤/钾盐/油田企业** ⇒ **公用事业与工业电力承包商**，属典型 B 型客户。
- **决策人 = Co-owner Clayton Pinfold（50% 持股，Owner/Operator）** —— **小企业主即采购决策口**，且**其具名邮箱经官网一手源 + SMTP 实测双证**，触达直达决策人。

### 买家类型 / 需求品类
- 买家类型：🔥 **B 电力线路施工承包商（架空/地下线路 + 变电站）**——实测画像 B 型（占 62%）
- 需求品类（带结论态）：
  - `三相液浸配电变 / 三相美变（UL E541627，45–5,000 kVA，可直供）` —— 配电线路/变电站主切口
  - `三相液浸电力变（UL E541626，72–121 kV、750–110,000 kVA，可直供）` —— 其变电站业务对口，条件试探
  - `单相柱上变（认证在办 E544629，条件切入）` —— **架空配电线路（其主业）对口**，条件切入
  - `干变（加拿大可谈，有 CSA 项目报告，需人工确认）` —— 其矿业/工业客户可能有干变需求，**备选**
  - ⚠️ 客户在**加拿大**：干变按「加拿大可谈」处理；**绝不写 `CSA Certified`**

### 电压·频率·认证要求
- 电压：官网未列具体 kV（仅「overhead and underground power utilities」）→ 具体采购 kV/kVA **首轮问**
- 频率：**60 Hz**（加拿大，产品零改造适配）
- 认证：加拿大市场按 **CSA / IEEE / IEC 标准**；我方持 **UL E541626** 与 **E541627** 正式 CoC —— ⛔ **不得写 `CSA Certified`**，只可写 `built to CSA/IEEE/IEC standards`

### 采购信号
- 官网明列 **「substations」** 为业务线/客户类型 → 变电站设备（变压器）采购职能
- 客户含 **SaskPower（省电力公司）+ 市政电力 + 矿业 + 油田** → 公用事业与工业电力设备长期需求
- **ISN Networld 认证 + Heavy Construction Safety Association 会员** → 合规运营，具备承接大项目资质
- **1991 年起运营、30+ 员工、3 个站点** → 稳定经营的本地承包商

### 可利用的钩子（按强度排序）
1. **官网明列「substations（变电站）」为业务线**（一手源）—— 与我方电力变/配电变能力对口
2. **客户含 SaskPower + 市政电力 + 矿业/油田**（一手源）—— 公用事业/工业电力场景
3. **Co-owner Clayton Pinfold 即决策口，邮箱双证** —— 冷触达直达决策人
4. **1991 年起 30+ 年的线路承包商** —— 老牌承包商，长期经营角度
5. **架空/地下线路主业** —— 单相柱上变/配电变场景

### 开发信建议
- **收件人策略**：✅ **A 档主送 `cpinfold@pmppowerline.ca`（Clayton Pinfold）**，写个性化正文；电话 **306-642-3547** 并行跟进
- 🔴 **域名提醒**：邮箱域 = 官网域 = **`pmppowerline.ca`**；⚠️ **绝不可**误写为 `pmpowerline.ca` / `pmppowerline.com` 等（未验证）
- 🔴 **话术红线**：**不引用员工数（30+）/ 不引用成立年份为卖点**；不写 `CSA Certified`
- **开场角度**：从其 **官网明列的「变电站（substations）+ SaskPower/市政电力客户」** 切入（写信 agent 决定措辞）
- **发送时段**：SK **CST（中部标准时区，全年不夏令）**，周二–周四当地上午 ≈ **北京时间 22:00–01:00**
- **送达配置**：🔴 **MX 自指向 `pmppowerline.ca`（→ Blacksun Exim `cp1014.blacksun.ca`）** —— **投递前需复验**；非 Google/M365，注意首封退信监控
- **附件建议**：不带名录/供货记录；如需仅附 UL 证书号 + 容量区间

### ⚠️ 矛盾点与风险提示
- ⚠️ **MX 自指向（重要）**：`pmppowerline.ca` 的 MX = `0 pmppowerline.ca.`（**自指**），**非标准配置** ⇒ **发送环节必须在投递前复验该域是否仍正常收信**（本单实测 25 端口 Exim 返回 220 + RCPT 250，**当前有效**，但需按批次复核）。
- ⚠️ **收信域为小厂共享 Exim 服务器（Blacksun）** —— 送达信誉/容量弱于 Google/M365 ⇒ **建议低速率、逐封投递**，避免一次性多发。
- ⚠️ **网站版权年份偏旧**（页脚「2009 & 2010」）→ 但 About 页 owner 点名 + SMTP 命中 + BBB 在列，**仍在营**；**仍建议电话复核在职**。
- ⚠️ **公司/个人 LinkedIn 均未找到** → 缺社交佐证（但 SMTP 命中已强证邮箱在役）。
- ⚠️ **两位 owner 同属一家公司** → **只发 1 人**（Clayton），**不得对 Rick Moore 另发**。
- ⚠️ **规模数据为官网自述**（30+ 人）→ **正文不引用具体数字**。

### 信息缺口清单（请勿编造）
- **Clayton Pinfold / Rick Moore 的任职时长**：未获取
- **采购的具体变压器 kV / kVA / 品牌 / 认证要求**：首轮问
- **是否已固定变压器供应商 / 是否进口**：未获取
- **萨省企业注册号 / 法人注册细节**：未查
- **员工数 / 营收的权威口径**：未获取（官网自述 30+ 人，**正文不可引用**）
- **公司/个人 LinkedIn 页**：未找到

### 一句话画像
萨省 Assiniboia 一家 **1991 年创立、30+ 人的电力线路施工承包商**（另有 Gull Lake / Pilot Butte 站点，ISN Networld 认证），主营**架空/地下电力线路的建设与维护**，客户含 **SaskPower、市政电力、矿业、油田、农村与变电站** —— **Co-owner Clayton Pinfold（50% 持股）具名邮箱 `cpinfold@pmppowerline.ca`（官网一手源 + SMTP 250 命中，A 档，可主送）**；⚠️ **MX 自指向，投递前需复验**，不引用员工数。

### 渠道覆盖清单（L-1、L0–L7）
| 层 | 结果 | 一句话 |
|---|---|---|
| L-1 锁人 | ✅ | 官网 About 页点名「current owner/operators: Rick Moore and Clayton Pinfold, each 50%」+ BBB「Principal Contacts: Rick Moore」 |
| L0 官网 | ✅ | home / about / contact 实抓；🔴 **About 页一手具名邮箱 `cpinfold@pmppowerline.ca`（A 档）** |
| L1 政府/协会一手 | ⚠️ | ISN Networld / Heavy Construction Safety Association 会员（官网自述）；萨省注册未查 |
| L2 命名+DNS | ✅ | **MX 自指向（实测 Exim 收信）**；A=69.27.101.4；SPF 含 Google + 自有 IP；**邮箱域 = 官网域** |
| L3 B2B 库 | ⚠️ | D&B / BBB 有条目，**仅旁证** |
| L4 社媒协会 | ❌ | 公司/个人 LinkedIn **未找到** |
| L5 黄页同址 | ✅ | mysask411 / topcompanies / cossd 同址在列（旁证在营）|
| L6 电话表单 | ✅ | 306-642-3547 + 传真 + 官网联系表单（未拨打）|
| L7 付费 | ❌ | 未启用 |

### 同名排除表
| 同名 | 地点 | 排除理由 |
|---|---|---|
| PMP / PMP Powerline（其他同名）| — | 须按 **SK Assiniboia + pmppowerline.ca + 电力线路施工** 锁定 |
| Clayton Pinfold / Rick Moore（其他同名个人）| — | 须按 **PMP Powerline Construction Ltd. + Owner/Operator + Assiniboia** 锁定 |
| 「PMP」项目管理缩写等 | — | 与本公司无关 |
