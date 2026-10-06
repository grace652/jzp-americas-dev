# 【买家 204】开发信交接单 — Alberta Breaker & Supply Co. Ltd.（Northern Breaker Group）

> 采集日期：2026-09-29 / 来源：batch6 名单（目标客户清单-batch6.csv 序号 31）/ 一句话结论：Calgary 独立电气批发商（2001 成立，5 万+ SKU，含 Delta/REX 变压器线），⓪ 层判定为**分销商 PASS**；属 Northern Breaker Group（采购权可能上移），已 SMTP 验证两条具名邮箱，主送走 President。
> 闸门输出：`发信资格：✅ 通过 ｜ 邮箱档位：A（具名已验证，don@ / aaron@）`
> ⚠️ 唯一未决项：**角色口径冲突**（见「矛盾点与风险」）——官网团队页把 Don Haynes 列为 Counter Sales，LinkedIn×2 + RocketReach 列为 President。

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示(如有)
Alberta Breaker & Supply Co. Ltd.（Northern Breaker Group 旗下） | Don (Donald) Haynes | President（LinkedIn×2+RocketReach；官网团队页另列为 Counter Sales） | don@albertabreaker.net | 已验证（SMTP RCPT 250，控制地址协议通过） | LinkedIn 个人页未取（第三方快照：ca.linkedin.com/in/donald-haynes-66a71514b / -31787b345）；公司页 northernbreakergroup.ca | Calgary 独立电气批发商，2001 由 Gordon Haynes 创立，5 万+ SKU（新/旧/停产断路器为主），代理 Delta / REX 变压器线，属 Northern Breaker Group（Calgary+Edmonton+Vancouver 三仓） | 官网 albertabreaker.net（业务原句）+ northernbreakergroup.ca（集团页）+ SMTP 探测 + LinkedIn/RocketReach | 集团采购权或上移；无采购专职岗；President 头衔口径冲突（见风险段）
```

## 二、补充信息（扩展段）

### 标准字段明细
- 国家+城市：加拿大 Alberta，Calgary（SE）
- 详细地址：5734 Burbank Crescent SE, Calgary, AB T2H 1Z6（官网明文；Google Maps CID 6970617663715778679）
- 电话：403-520-0014（Calgary 主）；Edmonton 780-758-6122；Vancouver 604-283-6336
- 营业：周一–周五 7:00–16:30（MST，UTC-7，夏令时 MDT UTC-6）
- 网站：albertabreaker.net（品牌站）→ 集团站 northernbreakergroup.ca
- 集团：**Northern Breaker Group**（母公司品牌）
  - Calgary：Alberta Breaker & Supply（本家，2001 起）
  - Edmonton：National Breaker & Supply Ltd.（sales@nationalbreaker.ca）
  - Vancouver/Surrey BC：CPM Electrical Sales（cpmelectricalsales@gmail.com）
- 成立：2001（Gordon Haynes 创立；其 56 年电气行业经验，前 Westburne / Gescan / Nedco / GE）
- 规模：单仓批发 + 全国邮寄；「50,000+ products」；未见营收公开
- NAICS：**未取得官方码**（cybo/linkcentre 归类为「电器用品店/Electrical systems」——零售批发，非制造；本单 ⓪ 层以官网业务原句为准，判为分销商）

### 联系人（含 still_here 在职核验）
| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| **Don (Donald) Haynes** | 决策层（拟主送） | President（第三方×3）/ Counter Sales（官网） | 未获取 | 中：LinkedIn 资料在位；官网团队页在列 | ⚠️ 中（口径冲突，见风险） | ca.linkedin.com/in/donald-haynes-66a71514b（快照） |
| Aaron Bell | 分支运营负责人（备选，已验邮箱） | Branch Manager | 未获取（官网称 20+ 年经验） | 中：官网集团页在列（近期更新） | ⚠️ 中（Signalhire 另有「Retired」记录，疑数据串号） | 未取（官网集团页有简介，无个人页） |
| Gordon Haynes | 创始人/最高（无邮箱） | CEO & Founder | 2001 至今 | 高：集团页明确「He leads… national expansion」 | 低 | 未取 |
| Willy Muckersie | 仓/停产件专家 | Warehouse & Obsolete Parts Specialist | 20+ 年 | 中 | 低 | — |
| Dean Ropchan | 电机控制 | Motor Control Specialist | 25 年 | 中 | 低 | — |
| Tim Davis | 自动化/电机控制部门 | Automation & Motor Control Division Lead | 1987 至今 | 中 | 低 | — |

> 🔴 **本单只发 1 人**：拟主送 **Don (Donald) Haynes**；Aaron Bell 为同域备选（同公司，不并列发送）。

### 邮箱分档（A/B/C）
- **A 档（具名，已验证）**：
  - `don@albertabreaker.net` — 对应 Don (Donald) Haynes（President）。**SMTP RCPT 250**，同轮控制地址 `sales@albertabreaker.net` = 250、随机地址 550、对照组 550 → 探测有效、非 catch-all（Google Workspace）。
  - `aaron@albertabreaker.net` — 对应 Aaron Bell（Branch Manager）。同协议 250 命中。**本域命名规则 = `{firstname}@`**（`aaron@` 命中；`gordon@`/`gordon.haynes@`/`ghaynes@` 均 550 → 创始人 Gordon 该域无邮箱）。
- **B 档（角色）**：`sales@albertabreaker.net`（官网 mailto 明文，一手）——备用点名转交入口。
- **C 档**：`cpmelectricalsales@gmail.com`（Vancouver 分部，免费邮箱，非本单）。
- H6 声明：**不适用**——已取得具名决策人邮箱（A 档），非仅角色邮箱。

### 我为什么找他
- 官网业务原句 **"Alberta Breaker & Supply is one of the leading electrical wholesalers in Calgary. We stock over 50,000 products…"**，且明列 **REX（isolation units, step-up/step-down）** 与 **Delta Transformers** 两条变压器品牌线——即**已在其货架上卖变压器**，不是潜在而是现成的变压器转售商。
- 其货架**高度依赖"新/旧/停产"断路器与 legacy 配电设备**（官网原句："legacy systems still running across Southern Alberta"、"new, used, and obsolete breakers"）→ 对**按规格定制、交期可控**的变压器有真实需求缺口。

### 买家类型 / 需求品类
- 买家类型：🔥 **A 分销商**（独立电气批发商；断路器/电机控制/变压器/熔断器/面板/箱体全线）
- 需求品类（带结论态）：
  - `三相美变（UL E541627，可直供）` — 主推：其货架已有 Delta/REX 变压器线，规格替换空间明确
  - `单相柱上变（认证在办，条件切入）` — Alberta 农业/能源/油田场景的柱上配电
  - `主变/变电站变（产能可覆盖，UL 区间外，需人工确认）` — 工业项目制，次优先
  - ⚠️ 不谈干变于美国客户（此处为加拿大客户，干变可谈 `built to CSA 标准`，但非本单主推）

### 电压·频率·认证要求
- 电压：未获取（Alberta 工商业常见 600V/480V/347V 配电 + 单相 240/120V）
- 频率：**60 Hz**（加拿大）
- 认证：加拿大市场 → `cUL / built to CSA 标准`；美变亮 **UL E541627**

### 采购信号
- 独立家族批发商（非集团统采）→ 单点决策链短，Calgary 分支可自主采购
- 官网明示「Net payment terms and purchase history for qualified Calgary contractor accounts」→ 有对公采购与账期流程
- 集团三仓（Calgary/Edmonton/Vancouver）→ 单一供应商可一次覆盖三仓需求
- 货架含 REX / Delta 变压器 → 现成品类，非新品类教育成本

### 可利用的钩子（按强度排序）
1. **「我已看到你们 Calgary 仓卖 REX 与 Delta 变压器」**（官网明文品类）——最具体的非群发证据
2. **legacy/停产件定位**——"new, used, and obsolete" → 我方**按规格定制 + 交期可控**可补其定制缺口
3. **集团三仓扩张**——Gordon Haynes「leads the Northern Breaker Group's national expansion」→ 供应网络扩容窗口
4. **UL E541627 三相液浸配电变**——直接对应其变压器货架

### 开发信建议（不写正文/主题/话术）
- **收件人策略**：主送 `don@albertabreaker.net`（Don/Donald Haynes，President）；若退信或身份冲突 → 转 `aaron@albertabreaker.net`（Aaron Bell，Branch Manager）；再兜底 `sales@albertabreaker.net` 点名转交。
- **发送时段**：Calgary 为 **MST（UTC-7）**，建议当地周二–周四上午 8–10 点（≈北京时间 23:00–01:00）。
- **送达配置**：`albertabreaker.net` MX = **Google Workspace**（`smtp.google.com`），SPF `~all`（软失败，无硬拒）；**未检测到 DMARC 硬策略**（建议发送前补一次 TXT 复核）；纯文本、无附件名录。
- **附件建议**：不带名录；如需附，仅 UL 证书号 + 容量区间（勿外发供货记录 PDF）。

### ⚠️ 矛盾点与风险提示
- 🔴 **角色口径冲突（本单最大不确定）**：官网团队页（第一方，近期更新）把 **"Don Haynes"** 列为 **Counter Sales**（持牌 master electrician，9 年现场 + 9 年在 Alberta Breaker）；而 LinkedIn（两个档案）+ RocketReach 均称 **Donald Haynes = President of Alberta Breaker & Supply Co Ltd**。二者**可能同名不同人**（家族企业常见父子同名/同姓），也可能是官网团队页仅描述 Calgary 分支岗位。→ **don@ 邮箱本身经 SMTP 验证真实存在**，但收件人到底是 President 还是 Counter Sales 未定，**写信时避免在正文里强指其职务**。
- ⚠️ **集团归属**：属 Northern Breaker Group → 采购权**可能上移**至集团层（Gordon Haynes 主导全国扩张）。若首轮无回应，可上探 `northernbreakergroup.ca`（Google Workspace）或集团电话。
- ⚠️ **Aaron Bell「Retired」疑云**：Signalhire 记录显示 "Retired at Alberta Breaker"，邮箱为 `a********l@sonepardis.ca`（Sonepar 域）——与本司域不符，**疑为数据串号**；但官网集团页仍列其为 Branch Manager。→ 若改用 aaron@ 主送，先电话核实。
- ⚠️ **NAICS 未取得**：本单 ⓪ 层以官网业务原句判定（"leading electrical wholesalers"、"We stock"），非官方码；如需硬证据可补查加拿大注册库。
- ⚠️ 官网团队页简介为**营销文案口吻**（人名+职能机械感较强），**人名真实性以 SMTP 命中为准**（don@ / aaron@ 均 250）。

### 信息缺口清单（请勿编造）
- Don/Donald Haynes 的**确切职务**（President vs Counter Sales）：未定，勿在信中武断称呼
- **采购专职岗**：未找到（小微家族批发商，疑由老板/分支经理兼）
- **营收 / 员工数 / 成立注册号**：未获取
- **官方 NAICS 码**：未取得
- **常用变压器容量段/电压等级**：未获取
- **个人 LinkedIn 直链**：未取（仅第三方快照）
- **Gordon Haynes（创始人）邮箱**：该域 SMTP 多格式均 550，未找到

### 一句话画像
Calgary 家族电气批发商（2001，5 万 SKU，卖 REX/Delta 变压器），属三仓的 Northern Breaker Group——主送 President 级 don@，但头衔口径待核。

### 渠道覆盖清单（L-1、L0–L7）
| 层 | 结果 | 一句话 |
|---|---|---|
| L-1 锁人 | ✅ | 官网团队页 6 人全取（含 CEO/Founder、Branch Manager）+ LinkedIn 补 President 头衔 |
| L0 官网 | ✅ | 业务原句 + 品类 + 三仓 + mailto（sales@ 一手）全取 |
| L1 政府一手 | ❌ | 未查加拿大注册库（时间约束） |
| L2 命名+DNS | ✅ | Google Workspace MX + SPF ~all；SMTP 命中 2 条具名，反推规则 `{firstname}@` |
| L3 B2B 库 | ⚠️ | Prospeo（`{first}`）与 RocketReach（`{first}.{last}`）冲突；仅作旁证 |
| L4 社媒协会 | ⚠️ | LinkedIn 仅第三方快照；未走协会名录 |
| L5 黄页同址 | ⚠️ | cybo/linkcentre 同址旁证 |
| L6 电话表单 | ✅ | 403-520-0014（官网一手，未拨打） |
| L7 付费 | ❌ | 未启用 |
