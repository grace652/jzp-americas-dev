# 【买家 246】开发信交接单 — Ward Electric Company, Inc.

> 采集日期：2026-09-30 ｜ 来源：batch7 名单（wardelectriccompany.com，US CO，A 电气承包商）｜ 一句话结论：**科罗拉多 Longmont 的家族型全服务电气承包商（2005 年由 Ward 家族创立，现由 Matt Ward 任 President、Mark Ward 任 CEO），官网首页逐字写明 "Power Lines — Whether it's transmission or distribution, we have the experience to provide turnkey solutions" 与 "Substations — We can build it from the ground up or provide turnkey substation solutions"，业务含输电（345kV→34.5kV）、配电、变电站、可再生；官网 Contact 页公布部门角色邮箱 `bids@wardelectriccompany.com` / `office@wardelectriccompany.com`（一手源）= B 档 → 点名转交 Director of Estimating/PM Jacob Prinz（备选 President Matt Ward）。**
> ⚠️ 本表严格区分「已验证」与「未获取」；未找到的信息一律标注，不做推断填充。
> ⚠️ **本单为 B 档**：主送走角色邮箱 `bids@wardelectriccompany.com` + 点名转交；具名直邮未取得（无邮箱命名样本，**禁推演**）。

## 闸门（留痕）

- 发信资格：✅ **通过**（B 档角色邮箱 → 点名转交 Jacob Prinz, Director of Estimating/Project Management）
- 邮箱档位：**B（角色邮箱 → 点名转交）**
- 排重：与 `clients/`、`交接单/batch1–7`、`发信队列.json`、`发送日志.csv`、`退信黑名单.json`、`永久排除名录.md`、`_dedup_keywords.txt` 逐条比对 → **0 命中** ✅
- ⓪ 层（反身排除）：**通过**——官网自述为 **full-service electrical contractor（全服务电气承包商）**，业务是施工/维护，**非变压器制造商、非 YAWEI 代理、非中国货源通道**

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示
Ward Electric Company, Inc.（Ward Electric）| Jacob Prinz（主转交）；Matt Ward（备选）| Director of Estimating / Project Management（主）；President（备选）| `bids@wardelectriccompany.com`（**B 档角色邮箱，官网一手源**）| **已验证（官网 Contact 页明文一手源；格式校验通过）** | 公司 LinkedIn 未直取；个人页：Matt Ward `linkedin.com/in/matt-ward-22521b45`（经搜索快照）| 科罗拉多 Longmont 家族型全服务电气承包商（2005 年创立，Matt/Mark Ward 2012 年从父母手中收购），第二处位于 Iowa Sioux City；业务含**输配电线路（345kV→34.5kV）turnkey、变电站 ground-up/turnkey、可再生（风光）、住宅/C&I**；官网称已成全国性承包商 | 官网 home / contact / our-team / our-history 实抓 + DNS(MX/SPF) 实测 + LinkedIn（搜索快照）+ ColoradoBiz（旁证）| ⚠️ **存在仿冒/错拼域名 `wardelectricompanyinc.com`（少一个 c）→ 绝不投递**；⚠️ 主转交对象 Jacob Prinz 为 **2026 年新入职** → 宜用"欢迎/新职"角度或改转 Matt Ward；⚠️ 不引用人数/营收
```

## 二、补充信息（扩展段）

### 标准字段明细
- 国家+城市：**美国 Colorado**，Longmont（总部）；第二处 **Iowa**，Sioux City
- 详细地址：**9586 E. I-25 Frontage Rd., Suite B, Longmont, CO 80504**（官网 Contact 页）；Iowa：**2505 Correctionville Rd., Sioux City, IA 51106**
- 电话：**(303) 682-0066**（CO，工作日 7:00–15:00 MT）；**(712) 271-2600**（IA）
- LinkedIn：公司页未直取；个人页 `linkedin.com/in/matt-ward-22521b45`（搜索快照，**未直取**）
- 网站：**wardelectriccompany.com**（**邮箱域 = 官网域 wardelectriccompany.com**，MX = **Microsoft 365** `wardelectriccompany-com.mail.protection.outlook.com`；SPF = `spf.protection.outlook.com` + `spf-us.emailsignatures365.com`）
- 成立日：**2005-02-27**（官网 our-history：由 Mike & Joyce Ward 创立；2012 年 Matt/Mark 收购）——**多源一致**
- 规模：⚠️ 未获取（第三方口径不一 → **不引用**）
- 法人主体：**Ward Electric Company, Inc.**（官网页脚署名）
- 执照/资质：官网称有 **DOT** 部门（含司机档案）→ 车队运营；CO/IA 承包商执照号未查

### 联系人（含 still_here 在职核验）
| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| **Jacob Prinz（主转交对象）** | Director of Estimating / Project Management | **官网 Our Team 页原话**："He joined the Ward Electric team in **2026** as the Director of Estimating and Project Management" | **< 1 年（2026 新入职）** | 官网 Our Team 页现行（2026 抓取）| **中**（**新入职**——宜走"欢迎/新职"角度；单一官网来源）| 未找到 |
| **Matt Ward（备选）** | President（兼 majority owner）| **官网 Our Team 页原话**："Matt became Ward Electric's President in the spring of **2020**… Matt and his brother, Mark, became majority owners… in 2012"；LinkedIn 现任 "President at Ward Electric Company inc." | **≥ 5 年（2020 起任 President；2006 起在公司）** | 官网 Our Team 页现行 + LinkedIn 现任 | **低**（**官网原话 + LinkedIn + owner 身份**三源；家族 owner 型）| `linkedin.com/in/matt-ward-22521b45`（经搜索快照，**未直取**）|
| Mark Ward | Chief Executive Officer（兼 majority owner）| 官网 Our Team 页原话（2012 起 CEO）| ≥ 13 年 | 官网现行 | 低 | 未找到 |
| Mike Sellke | Chief Operating Officer | 官网 Our Team 页原话（2024 年中升 COO）| — | 官网现行 | 低 | 未找到 |

> 🔴 **一家只发 1 人**：**主转交 = Jacob Prinz（Director of Estimating / PM）**——**估价/项目管理为变压器采购与报价的对口职能**；⚠️ 但其 **2026 年新入职**，**宜走"欢迎/新职"角度**，或**改转 President Matt Ward（owner，最稳）**。**二选一，不得同时发。**

### 邮箱分档（A/B/C）
- **B 档（角色邮箱，官网一手源）**：✅ **`bids@wardelectriccompany.com`**（官网 Contact 页明文；"Bids & Business Development — Questions about proposals, partnerships, **products or services**"）——**最对口**；另 `office@`（General）、`ap@`（Accounts Payable）、`hr@`、`payroll@`、`driverdocs@` 均为官网明文
- **A 档（具名）**：❌ **未取得**（官网**未公布具名邮箱**；**无命名规则样本 → 禁推演** `matt@` / `jprinz@` 等）
- **主送路径**：**`bids@wardelectriccompany.com`（B 档）**，正文首句**请求转交 Jacob Prinz（Director of Estimating / PM）**（或 Matt Ward, President）
- ⚠️ **H3 说明**：邮箱来自**官网一手源（Contact 页明文）** → 满足 H5；已标来源。
- 🔴 **SMTP 不可用**：本机 25 端口整体不可用 → 未能做 RCPT 复核，**以官网一手源为准**。

### 我为什么找他
- 官网首页**逐字写明**："**Power Lines** — Whether it's **transmission or distribution**, we have the experience to provide **turnkey solutions** for jobs of all sizes" 与 "**Substations** — We can **build it from the ground up** or provide **turnkey substation solutions**" —— **一家做输配电与变电站 turnkey 的承包商，是主变/配变的直接使用方**。
- 官网 Our Team 页**逐字写明** Luke Johnson（GM–Xcel Energy）"has extensive experience from **345kV down to 34.5kV**, including lattice towers… For distribution, he has worked with steel, wood and laminate lines of all voltages" —— **明确覆盖 345kV 至 34.5kV 的输配电施工，电压区间与我方 E541626（72–121 kV）重叠**。
- 官网首页列 **Renewables（Solar and wind experience, routing power from generation to end-user）** —— **风光并网场景需升压/箱变类设备**。
- 官网称 "Ward Expands, Adds **Second Iowa Location**" + ColoradoBiz 报道其"grows into **national contractor**" —— **业务扩张期，采购需求上升**。

### 买家类型 / 需求品类
- 买家类型：🔥 **B 型 电气承包商（输配电 + 变电站，家族型，扩张期）**——实测画像 B 型
- 需求品类（带结论态）：
  - `三相液浸配电变 / 三相美变（UL E541627，45–5,000 kVA，可直供）` —— 配电与二次服务场景，**最可能切口**
  - `三相液浸电力变（UL E541626，72–121 kV、750–110,000 kVA，可直供）` —— 其变电站/输电（345kV→34.5kV）区间对口，条件试探
  - `单相柱上变（E544629 为 ECD 计划函、非证书，条件切入）` —— 配网场景，**条件切入，绝不说 certified**
  - `变电站小主变 SF 系列（36–48 kV，ECD 计划函，条件切入）` —— 变电站场景，**条件切入**
  - `干变（美国不匹配：无 UL）` —— ⛔ **显式标注，不推、不挂钩子**

### 电压·频率·认证要求
- 电压：⚠️ **部分获取**（官网仅就 Luke Johnson 个人经验称 "345kV down to 34.5kV"；**公司级常用电压未获取**）→ **正文不引用具体电压数字**，首轮问
- 频率：**60 Hz**（美国，产品零改造适配）
- 认证：美国市场按 **UL / IEEE C57.12 / ANSI 标准**；我方持 **UL E541626** 与 **E541627** 正式 CoC —— ⛔ **不得写 `CSA Certified` / `SASO` / `SONCAP`**；干变无 UL，**对美绝不谈干变**

### 采购信号
- 官网设 **"Bids & Business Development" 专用邮箱 `bids@`**，说明 "proposals, partnerships, **products or services**" → **有正式对外采购/投标入口**
- Our Team 页设 **Director of Estimating / Project Management** 岗 → **估价与采购职能明确存在**
- 业务含 **输配电 turnkey + 变电站 turnkey + 可再生** → 变压器为项目关键设备
- **扩张中**（新增 Iowa 点、全国化）→ 采购量级上升

### 可利用的钩子（按强度排序）
1. **"Substations — build it from the ground up or provide turnkey substation solutions"**（官网一手源）—— 变电站角度，最直接
2. **"Power Lines — transmission or distribution… turnkey solutions"**（官网一手源）—— 输配电角度
3. **345kV→34.5kV 输电经验**（官网 Luke Johnson 简介，一手源）—— 电压区间与我方重叠
4. **Renewables（solar & wind，routing power from generation to end-user）** —— 风光并网升压角度
5. **扩张期（新增 Iowa 点 / 全国化）** —— 供货与交期角度（⚠️ 首封不报交期）

### 开发信建议
- **收件人策略**：✅ **B 档主送 `bids@wardelectriccompany.com`**，正文首句**请求转交 Jacob Prinz（Director of Estimating / PM）**；⚠️ 若走"新职/欢迎"角度不宜，则**改转 Matt Ward（President）**。电话 **(303) 682-0066** 并行核实。
- 🔴 **域名提醒**：邮箱域 = 官网域 = **`wardelectriccompany.com`**；🔴 **绝不投递 `wardelectricompanyinc.com`（少一个 c 的错拼域名，疑仿冒）**
- 🔴 **话术红线**：**不引用人数/营收/电压具体数字**；⚠️ Jacob Prinz 为**新入职**，不宜用"资深/长期合作"类话术；⛔ 不谈干变；⛔ 不写 `CSA Certified`/`SASO`/`SONCAP`
- **开场角度**：从其 **变电站 turnkey + 输配电（345kV→34.5kV）** 切入（写信 agent 决定措辞）
- **发送时段**：CO **MT（山地时区）**，周二–周四当地上午 ≈ **北京时间 23:00–02:00**（夏令时期间）
- **送达配置**：MX = **Microsoft 365**，SPF = `spf.protection.outlook.com` + `spf-us.emailsignatures365.com`；发信域须 SPF/DKIM/DMARC 齐备
- **附件建议**：不带名录/供货记录；如需仅附 UL 证书号 + 容量区间

### ⚠️ 矛盾点与风险提示
- 🔴 **仿冒/错拼域名**：搜索命中 **`wardelectricompanyinc.com`**（拼写少一个 "c"）承载 "Ward Family… JoyforWard Foundation" 等内容 —— **疑仿冒/typo 域名或历史域名** → **绝不向其投递**；本家以 **`wardelectriccompany.com`** 为准。
- ⚠️ **主转交对象为新入职**：Jacob Prinz **2026 年入职** → 若走常规"合作/供货"角度，建议**改转 Matt Ward（President）**；或用"欢迎/新职"角度。
- ⚠️ **具名邮箱无样本** → **禁推演**（`matt@` / `jprinz@` 一律不写）。
- ⚠️ **公司级常用电压未获取** → **正文不引用电压数字**（仅 Luke Johnson 个人经验含 345kV→34.5kV，属个人资历，非公司采购规格）。
- ⚠️ **规模口径不一** → **不引用人数/营收**。
- ⚠️ **本机 SMTP 25 端口不可用** → 无法 RCPT 复核。
- ⚠️ **`hr@` 明示"Unsolicited resumes… may not be reviewed"** → 非招聘事务勿投 `hr@`。

### 信息缺口清单（请勿编造）
- **具名决策人邮箱**：**未获取**（无样本，**禁推演**）
- **公司级常用变压器电压等级 / 容量 / 品牌**：未获取（**首轮问**）
- **采购负责人姓名**（是否另有 Procurement 岗）：未获取
- **员工数 / 营收**：未获取（**不得引用具体数字**）
- **CO / IA 承包商执照号**：未查
- **Jacob Prinz 的任职起始确切月份 / 最近活跃**：未获取
- **第二具名联系人个人页**：未找到（仅 Matt Ward 有搜索快照）
- **`wardelectricompanyinc.com` 与本家的关系**：未查（**不投递**）

### 一句话画像
科罗拉多 Longmont 的**家族型全服务电气承包商（2005 创立，Ward 家族二代经营）**——首页明列 **Power Lines（输配电 turnkey）** 与 **Substations（ground-up / turnkey）**，覆盖 345kV→34.5kV，另有 Iowa Sioux City 点、处扩张期；**官网 Contact 页公布部门角色邮箱 `bids@wardelectriccompany.com`（一手源）= B 档，点名转交 Director of Estimating/PM Jacob Prinz（备选 President Matt Ward）**。

### 渠道覆盖清单（L-1、L0–L7）
| 层 | 结果 | 一句话 |
|---|---|---|
| L-1 锁人 | ✅ | 官网 Our Team 页具名 7 人；主转交 Jacob Prinz（Estimating/PM），备选 Matt Ward（President/owner）|
| L0 官网 | ✅ | home / contact / our-team / our-history 全抓；**6 个部门角色邮箱明文（B 档一手源）** |
| L1 政府一手 | ⚠️ | 官网含 DOT 部门；CO/IA 执照库未命中/未查 |
| L2 命名+DNS | ⚠️ | MX=Microsoft 365；SPF outlook+emailsignatures365；**无具名样本 → 禁推演**；SMTP 本机不可用 |
| L3 B2B 库 | ⚠️ | AllBiz / LeadIQ / Prospeo —— **仅作旁证** |
| L4 社媒协会 | ⚠️ | Matt Ward 个人页经搜索快照（未直取）；无公司页 |
| L5 黄页同址 | ✅ | 9586 E. I-25 Frontage Rd, Longmont CO —— 官网 / 目录一致 |
| L6 电话表单 | ✅ | (303) 682-0066（CO）/ (712) 271-2600（IA）+ 官网部门表单（未拨打/未提交）|
| L7 付费 | ❌ | 未启用 |

### 同名排除表
| 同名 | 地点 | 排除理由 |
|---|---|---|
| **`wardelectricompanyinc.com`**（拼写少一 c）| — | 🔴 **疑仿冒/typo 域名** → **绝不投递**；本家以 `wardelectriccompany.com` 为准 |
| **Ward Electric**（其他州同名）| 多地 | 与 Longmont CO + Sioux City IA 主体无关；须按官网域排除 |
| **Mark Ward（AllBiz 记 primary contact）** | Longmont, CO | ⚠️ 与 CEO **Mark Ward** 同名；AllBiz 为第三方口径，**以官网 Our Team 为准**（Matt=President，Mark=CEO）|
| **Matt Ward**（其他同名个人）| — | 须按 Ward Electric + Longmont CO 锁定 |
