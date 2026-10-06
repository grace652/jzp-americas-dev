# 【买家 225】开发信交接单 — K-Line Maintenance & Construction Limited

> 采集日期：2026-09-30 ｜ 来源：batch7 名单（k-line.ca，ON）｜ 一句话结论：**ON Stouffville 的 1967 年创立家族承包商（K-Line Group of Companies 核心公司），官网逐字自述「substation engineering, procurement, and construction」「Large, complex transformers and switching substations」「5kV to 230kV」——与主变/美变极对口，且自述「large and established purchaser of high-voltage equipment」有采购力；但官网与所有渠道均无任何可用邮箱，SMTP 本机不可用 → 发信资格 ⛔（第 1 条：邮箱未找到）。**
> ⚠️ 本表严格区分「已验证」与「未获取」；未找到的信息一律标注，不做推断填充。
> 🔴 **本单被合格线闸门拦截（邮箱未找到）** —— 仍产出完整背调，标 `待补充`，待取得可用邮箱/走电话路径后再放行。

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示
K-Line Maintenance & Construction Limited | Allan Kellett | President, Owner | **未找到**（官网全站、招聘页、页脚均无邮箱；无联系表单）；B2B 库候选 `akellett@k-line.ca` 为格式推演，**未验证，不可主送** | **未找到** | 公司页（K-Line Group）未直取；个人页未确认 | ON Stouffville 1967 年创立的高压服务承包商（K-Line Group 旗下四公司之一），自述变电站 EPC 至 230kV、含「大型复杂变压器」；家族企业，Kellett 家族持有 | 官网 home / overview-divisions / services-substations / contact-us / careers / job-substation-foreperson 全页实抓 + DNS(MX/SPF) 实测 + ContactOut/cybo/allbiz 旁证 | 🔴 **邮箱未找到 → 闸门拦截**；集团含**绝缘子制造臂**（互补品，非竞品）；同名公司「K-Line Construction Ltd.」须排除
```

## 二、补充信息（扩展段）

### 标准字段明细
- 国家+城市：**加拿大 Ontario，Stouffville（Whitchurch–Stouffville）**
- 详细地址：**12731 Highway 48, Stouffville, ON L4A 4A7**（总部）；另设 SK（Emerald Park，5 Industrial Drive）、AB（Calgary，10341 50th St SE）办公室
- 电话：**(905) 640-2002**（总部）；传真 (905) 640-8887
- LinkedIn：K-Line Group of Companies 公司页（检索命中，未直取）；个人页未确认
- 网站：**www.k-line.ca**（**邮箱域 = 官网域 k-line.ca**，MX = `kline-ca0c.mail.protection.outlook.com` → **M365 / Exchange Online**）
- 成立日：**1967**（官网 "dating back to 1967"；创始人 **E. Glenn Kellett**）
- 规模：第三方估算 **约 208–450 人**（ContactOut 208 / 官网称 450+）；**人数为口径不一，正文绝不引用具体数字**
- 集团：**K-Line Group of Companies** —— 含 K-Line Maintenance & Construction Ltd.、K-Tek Electro-Services Ltd.、**K-Line Insulators Ltd.（绝缘子制造）**、K-Line International Ltd.
- 执照：未获取（安省 ESA / IBEW 口径未证实）

### 联系人（含 still_here 在职核验）
| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| **Allan Kellett（本次主送）** | 集团一把手 / 共同所有者 | **President, Owner**（**官网 k-line.ca/careers/ 逐字署名**："Allan Kellett — President, Owner"）| 未获取（家族二代）| 中：官网现行（2026-09 抓取）| **低**（官网明文署名，且为家族所有者）| 未找到 |
| Mark Kellett | 集团共同所有者（备选）| Owner（官网 /meet-our-team/："Mark and Allan proudly own and operate the K-Line Group"）| 未获取 | 中：官网现行 | 低 | 未找到 |

> 🔴 **一家只发 1 人**：主送 **Allan Kellett（President, Owner）**——官网一手源署名，决策权最高。
> ⚠️ **已剔除 Ken Ramnarine（前 COO）**：K-Line 官方 LinkedIn 于 **2024-01** 发布其**退休公告**（"will be retiring from K-Line at the end of the month … Happy retirement!"）→ **已离职，不得触达**。

### 邮箱分档（A/B/C）
- **A 档（具名直邮）**：**未找到**
- **B 档（角色邮箱）**：**未找到** —— 官网 `k-line.ca/contact-us/` 只有各办公室**电话**，**无邮箱、无联系表单**；`k-line.net`（绝缘子臂）的 `insulators@k-line.net` 属**另一产品线**，**不可挪用**
- 🔴 **H6 声明**：**未取得任何可用邮箱** —— 已跑「升级三步」：
  1. 挖职能邮箱：官网 Contact / Careers / Jobs 页**均无邮箱**（逐页 grep 验证）
  2. 从真实回信反推命名规则：无回信样本
  3. 免费试推演：ContactOut 称格式 `{first_initial}{last}@k-line.ca`（83.33%）→ 推得 `akellett@k-line.ca`，但**单一 B2B 源、未经任何验证**（H3：单一来源须标注"未经第二方印证"；H2：不得作主送）
  → 结论：**本单无可用邮箱，发信资格 ⛔**。
- 🔴 **SMTP 不可用**：`k-line.ca` MX = M365（`*.mail.protection.outlook.com`），本机 25 端口探测**连接超时**（本环境外发 25 端口整体不可用）。

### 我为什么找他
- K-Line 官网 **/services/substations/ 页面逐字写明**：其 Substation Division「includes nationally recognized experts in **substation engineering, procurement, and construction**」，提供「complete turnkey operations from conceptual design … material procurement, installation, testing and commissioning of **Large, complex transformers and switching substations**」，覆盖「**From 5kV to 230kV**」——**一家把「采购大型复杂变压器」写进主业的承包商，是主变/美变的一线买家**。
- 同一页面还自述「As a large and established **purchaser of high-voltage equipment** and related services, The K-Line Group of Companies has **preferred buying power**」——**明示其有集中采购职能与议价地位**。
- 且 **Allan Kellett 是家族所有者兼 President**（官网 careers 页署名），**决策链短、可直接拍板**——比大集团层层审批更适合冷触达。

### 买家类型 / 需求品类
- 买家类型：🔥🔥 **B 电气承包商（高压服务 / 变电站 EPC，含输配电、临时电力、实验室检测）**——实测画像 B 型主力
- 需求品类（带结论态）：
  - `主变 / 变电站变（UL E541626，72–121 kV、750–110,000 kVA，可直供）` —— 其变电站 EPC 至 230kV，最对口
  - `三相液浸配电变 / 三相美变（UL E541627，45–5,000 kVA，可直供）` —— 配电/临时电力场景（其临时电力自述含 transformers，120v–27,600v）
  - `单相柱上变（认证在办 E544629，条件切入）` —— 架空配网，非首推
  - `干变（加拿大实体可谈，有 CSA 项目报告，需人工确认）` —— 备选，不首推
  - ⛔ **绝缘子 / 线路器材不在我方产品线**——**不可误当同类去谈**
  - ⚠️ 客户在**加拿大**：干变按「加拿大可谈」处理；**绝不写 `CSA Certified`**

### 电压·频率·认证要求
- 电压：官网自述变电站 **5kV – 230kV**（一手源，/services/substations/）
- 频率：**60 Hz**（加拿大，产品零改造适配）
- 认证：加拿大市场按 **CSA / IEEE / IEC 标准**；我方持 **UL E541626** 与 **E541627** 正式 CoC —— ⛔ **不得写 `CSA Certified`**，只可写 `built to CSA/IEEE/IEC standards`

### 采购信号
- 官网自述「**large and established purchaser of high-voltage equipment**」「**preferred buying power**」→ **明示集中采购职能**
- 变电站业务含「**material procurement**」「equipment bidding, review, evaluation」→ 有设备招标/采购流程
- 招聘在招 **Substation Foreperson**（Stouffville），JD 含「field assembly of all types of substation equipment **including transformers**」→ 现场装变，印证变压器用量
- 家族企业 + 450+ 人 + 加拿大西部/国际多办公室 → 稳定项目流

### 可利用的钩子（按强度排序）
1. **变电站 EPC 至 230kV + 「大型复杂变压器」自述**（官网一手源）—— 主变/变电站变强相关
2. **「大型高压设备采购方 / preferred buying power」自述** —— 直击采购职能
3. **1967 年创立、家族二代持有（Kellett 家族）** —— 传承/决策链短角度
4. **Indigenous 合作：PAIR（加拿大原住民商业委员会）Bronze 认证** —— 官网专门页（ESG 角度）
5. **K-Tek 独立测试实验室 + 现场服务** —— 技术对话角度

### 开发信建议
- **收件人策略**：🔴 **本单无可用邮箱，不得直接发信**。可执行路径：
  - **电话优先**：(905) 640-2002 → 索取 Allan Kellett（President, Owner）或采购/估算对口人的**直邮**（这是本单解锁的唯一现实路径）
  - 若日后通过电话/名片拿到具名直邮 → 回填本单再放行
  - ⛔ **禁止**用推演地址 `akellett@k-line.ca` 主送（未验证）
- 🔴 **域名提醒**：邮箱域若取得，应为 **`k-line.ca`**；⚠️ **绝不可**误用 `k-line.net`（绝缘子臂域）或 `k-lineconstruction.com`（**另一家公司**）
- **开场角度**（待有邮箱后）：从其 **变电站 EPC 至 230kV + 「大型复杂变压器」** 自述切入（写信 agent 决定措辞）
- **发送时段**：ON **ET（东部时区）**，周二–周四当地上午 ≈ **北京时间 21:00–24:00**（夏令时期间）
- **送达配置**：MX = **M365（Exchange Online）**；发信域须 SPF/DKIM/DMARC 齐备；M365 对来源 IP 有主动反制，**勿反复探测**
- **附件建议**：不带名录/供货记录；如需仅附 UL 证书号 + 容量区间

### ⚠️ 矛盾点与风险提示
- 🔴 **邮箱未找到 → 合格线闸门第 1 条拦截**：官网全站无邮箱、无表单；B2B 库格式推演**未验证**，**禁止主送**。
- ⚠️ **集团含制造臂**：K-Line Insulators Ltd. **制造绝缘子**（互补品，非变压器）——**⓪ 层判定：通过**（不是我们的竞品），但**不得把绝缘子当同类去谈**。
- ⚠️ **同名公司须排除**：见下方同名排除表（K-Line Construction Ltd. 等）。
- ⚠️ **人数口径不一**（208 vs 450+）：**正文绝不引用具体数字**。
- ⚠️ **前 COO 已退休**（Ken Ramnarine，2024-01）：**不得触达**；部分第三方名录（allbiz/cybo）仍把他列为「primary contact / COO」→ **属过期数据**。
- ⚠️ **个人 LinkedIn 直链未取** → Allan Kellett 离职风险评「低」但依据仅官网署名。
- ⚠️ **M365 网关**：探测与送达均可能受限。

### 信息缺口清单（请勿编造）
- **任何可用邮箱**（具名或角色）：**未找到** ← 本单被拦截的直接原因
- Allan Kellett 的**个人 LinkedIn 直链 / 最近活跃**：未获取
- K-Line 的**员工数 / 营收**（准确口径）：未找到（口径不一，**不可引用具体数字**）
- K-Line **常用变压器容量 / 电压 / 品牌**：未获取
- **采购决策归属**（集团 vs 各公司）：未明（需电话确认）
- **ON 省注册主体全称 / 注册日**（Ontario Business Registry）：未查
- **NAICS 分类**：未获取

### 一句话画像
ON Stouffville 一家 1967 年创立、Kellett 家族持有的高压承包商——**变电站 EPC 至 230kV、官网明写「大型复杂变压器」与「大型高压设备采购方」**，对口度极高、决策链短；**但官网全站无任何邮箱、无表单，SMTP 本机不可用 → 被闸门拦截，只能先走电话 (905) 640-2002 索取直邮后再放行**。

### 渠道覆盖清单（L-1、L0–L7）
| 层 | 结果 | 一句话 |
|---|---|---|
| L-1 锁人 | ✅ | 官网 careers 页取 Allan Kellett（President, Owner）；owners Mark & Allan Kellett |
| L0 官网 | ❌ | /contact-us/ 仅电话、**无邮箱无表单**；/careers/ /jobs/ /job-*/ 逐页 grep 均无邮箱 |
| L1 政府一手 | ⚠️ | 安省注册库 / ESA 执照未查 |
| L2 命名+DNS | ⚠️ | MX=M365、SPF 含 outlook；**B2B 库格式 `{f}{last}@` 单一来源，未验证**；SMTP 本机不可用 |
| L3 B2B 库 | ⚠️ | ContactOut/cybo/allbiz 列人列格式，**含过期数据（Ramnarine）**，仅作旁证 |
| L4 社媒协会 | ⚠️ | 公司 LinkedIn 命中未直取；个人页未确认；PAIR 认证见官网 |
| L5 黄页同址 | ⚠️ | Stouffville 地址与第三方名录一致 |
| L6 电话表单 | ⚠️ | 电话 (905) 640-2002 可拨；**官网无联系表单** |
| L7 付费 | ❌ | 未启用 |

### 同名排除表
| 同名 | 地点 | 排除理由 |
|---|---|---|
| **K-Line Construction Ltd.** | 加拿大（k-lineconstruction.com）| 🔴 **另一家独立公司**（powerline/telecom/civil 施工），**与 K-Line Group 无关**，须严格区分 |
| K-Line Insulators Limited | ON Scarborough（k-line.net）| **同集团但不同公司**（绝缘子制造），邮箱域 k-line.net **不可挪用** |
| Kawasaki Kisen Kaisha（"K" LINE）| 日本 | 航运公司（kline.co.jp），完全无关 |
| Ali Kline | — | 🔴 **ContactOut 的「Ali Kline → akline@k-line.ca」为稻草人数据**（人名与公司名机械拼接），**整条作废** |
