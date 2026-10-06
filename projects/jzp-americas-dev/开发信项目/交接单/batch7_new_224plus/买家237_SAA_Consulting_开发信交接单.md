# 【买家 237】开发信交接单 — SAA Consulting Ltd.

> 采集日期：2026-09-30 ｜ 来源：batch7 名单（saaconsulting.ca，SK）｜ 一句话结论：**萨斯卡通/里贾纳（Regina, SK）的工程咨询公司，官网首页以 "Innovative Engineering for Your Transmission Line Design" 为题，About Us 称持 APEGS 许可、团队含 Civil/Structural/Electrical/Mechanical 注册工程师、西加拿大 20+ 年设计与施工经验；官网公布角色邮箱 `info@saaconsulting.ca`（一手源）= B 档 → 但**未取得任何具名决策人**，按 §4.4 列风险。**
> ⚠️ 本表严格区分「已验证」与「未获取」；未找到的信息一律标注，不做推断填充。
> ⚠️ **本单为 B 档**：主送走角色邮箱 `info@saaconsulting.ca` + **点名转交（具体人未获取）**；🔴 **未取得具名决策人直邮**。

## 闸门（留痕）

- 发信资格：⚠️ **有条件通过**（B 档角色邮箱 → 点名转交；⚠️ **未取得具名决策人**，按 §4.4 列风险；且**业务描述存在"商业/合同咨询 vs 电气设计"口径差**，建议先电话确认其是否真做电气设计）
- 邮箱档位：**B（角色邮箱 → 点名转交）**
- 排重：与 `clients/`、`交接单/batch1–6`、`发信队列.json`、`发送日志.csv`、`退信黑名单.json`、`永久排除名录.md` 逐条比对 → **0 命中** ✅

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示
SAA Consulting Ltd. | （具名决策人未获取）| — | `info@saaconsulting.ca`（**B 档角色邮箱，官网一手源**）| **已验证（官网一手源明文；格式校验通过）** | 未找到 | Regina SK 工程咨询公司；官网首页以 "Innovative Engineering for Your Transmission Line Design" 为题；About Us 称持 APEGS 许可、团队含 Civil/Structural/Electrical/Mechanical 注册工程师、西加拿大 20+ 年设计与施工经验 | 官网 home/about-us/contact-us-1 实抓 + DNS(MX/SPF) 实测 | ⚠️ **业务口径差**（首页文案偏"战略/商业/合同咨询"，About Us 偏"注册工程师设计"）→ **须电话确认其电气设计能力**；**无具名决策人**；成立年份/人数未获取（不引用）
```

## 二、补充信息（扩展段）

### 标准字段明细
- 国家+城市：**加拿大 Saskatchewan**，Regina
- 详细地址：**3317 Green Jade Lane, Regina, SK**（官网 contact 页）
- 电话：**+1 306 535 4543**（官网）
- LinkedIn：未找到
- 网站：**saaconsulting.ca**（**邮箱域 = 官网域 saaconsulting.ca**，MX = `saaconsulting-ca.mail.protection.outlook.com`；SPF `include:secureserver.net -all`）
- 成立日：🔴 **未获取**（官网未给年份）
- 规模：⚠️ **未获取**（官网仅称团队含注册工程师、20+ 年经验）→ **不引用人数**
- 法人主体：**SAA Consulting Ltd.**
- 资质：官网称"fully licensed and authorized to practice engineering in the province of Saskatchewan"，团队为 **APEGS** 注册成员
- 业务定位：⚠️ **口径不一** —— 首页 About 文案偏"战略、商业与合同解决方案"；About Us 页偏"注册工程师（含电气）设计与施工"

### 联系人（含 still_here 在职核验）
| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| （主送对象）| — | 🔴 **未获取**（官网无团队页/具名联系人）| — | — | — | — |
| （第二具名联系人）| — | **未找到** | — | — | — | — |

> 🔴 **一家只发 1 人**：**具名决策人未获取** → 主送走角色邮箱 `info@saaconsulting.ca` + 请求转交；⚠️ **无具名直邮，按 §4.4 显式标风险**。

### 邮箱分档（A/B/C）
- **B 档（角色邮箱，官网一手源）**：✅ **`info@saaconsulting.ca`**（官网 contact 页明文）
- **A 档（具名）**：❌ **未取得**（官网未公布具名邮箱；**无样本，禁推演**）
- **主送路径**：**`info@saaconsulting.ca`（B 档）**，正文首句**请求转交给负责输电线路/变电站设计的负责人**
- ⚠️ **H3/H6 说明**：邮箱来自**官网一手源**（满足 H5）；**仅有角色邮箱，升级三步未获具名决策人** → **显式标风险**（§4.4）。
- 🔴 **SMTP 不可用**：本机 25 端口整体不可用 → 未能做 RCPT 复核，**以官网一手源为准**。

### 我为什么找他
- 官网首页**以 "Innovative Engineering for Your **Transmission Line Design**" 为标题**，且 About Us 页**逐字写明**"fully licensed and authorized to practice engineering in the province of Saskatchewan. Our team is composed of highly qualified **Civil, Structural, Electrical, and Mechanical Engineers**, all of whom are registered members of **APEGS**" —— **一家持省许可、团队含注册电气工程师的工程公司，涉输电线路设计，是输配电设备规格的潜在相关方**。
- 官网称团队有 "**over 20 years of hands-on experience** in the design and construction industry across **Western Canada**" —— **西加拿大设计与施工经验，与输电线路/变电站场景对口**。
- ⚠️ **但其首页 About 文案偏"战略/商业/合同咨询"** → **电气设计的实际承接范围须电话确认**（勿按纯设计院话术套）。

### 买家类型 / 需求品类
- 买家类型：⚠️ **B 型（工程咨询，疑偏设计/规格方）** —— **类型判定依据**：官网 About Us 明列注册电气工程师 + 输电线路设计；**主类以"工程咨询"为主**；⚠️ 首页文案偏商业/合同咨询 → **须电话确认以哪类为主**
- 需求品类（带结论态）：
  - `三相液浸电力变 / 主变（UL E541626，72–121 kV、750–110,000 kVA，可直供）` —— 其输电线路/变电站设计对口
  - `三相液浸配电变 / 三相美变（UL E541627，45–5,000 kVA，可直供）` —— 配电场景
  - `单相柱上变（认证在办 E544629，条件切入）` —— **条件切入**
  - `干变（加拿大实体可谈，有 CSA 项目报告，需人工确认）` —— 备选，不首推
  - ⚠️ 客户在**加拿大**：干变按「加拿大可谈」处理；**绝不写 `CSA Certified`**

### 电压·频率·认证要求
- 电压：🔴 **未获取**（官网仅称 "Transmission Line Design"，未给 kV）→ **正文不引用电压数字**，首轮问
- 频率：**60 Hz**（加拿大，产品零改造适配）
- 认证：加拿大市场按 **CSA / IEEE / IEC 标准**；我方持 **UL E541626** 与 **E541627** 正式 CoC —— ⛔ **不得写 `CSA Certified`**，只可写 `built to CSA/IEEE/IEC standards`

### 采购信号
- 官网 About Us 列注册电气工程师 + 输电线路设计 → **潜在规格/设计方**
- 官网称持 APEGS 省工程许可 → **合规工程实体**
- ⚠️ **未发现其自身采购变压器的证据** → 定位为**潜在渠道/规格方**，且**业务口径待确认**

### 可利用的钩子（按强度排序）
1. **"Transmission Line Design" 首页定位 + APEGS 注册电气工程师**（官网一手源）—— 最对口的身份角度
2. **西加拿大 20+ 年设计与施工经验** —— 经验角度
3. **持 Saskatchewan 省工程许可（APEGS）** —— 合规工程实体角度
> ⚠️ **钩子强度受限**：业务口径差（商业/合同 vs 电气设计）+ 无具名联系人 → **待电话确认后再定钩子**。

### 开发信建议
- **收件人策略**：**B 档 → 主送 `info@saaconsulting.ca`**，正文首句**请求转交给负责输电线路/变电站设计的负责人**；电话 **+1 306 535 4543** 并行（**建议先电话确认其电气设计业务与负责人姓名**）
- 🔴 **定位红线**：SAA 业务口径差（可能偏商业/合同咨询）→ **先确认是否做电气设计**，勿按纯设计院话术硬套
- 🔴 **话术红线**：**不引用人数/成立年份/电压数字**
- **开场角度**：从其 **输电线路设计 + APEGS 注册电气工程师** 切入（写信 agent 决定措辞）
- **发送时段**：SK = **CT（中部时区，萨省不实行夏令时）**，周二–周四当地上午 ≈ **北京时间 22:00–01:00**
- **送达配置**：MX = **Microsoft 365**（GoDaddy/secureserver 发信）；SPF `include:secureserver.net -all`；发信域须 SPF/DKIM/DMARC 齐备
- **附件建议**：不带名录/供货记录；如需仅附 UL 证书号 + 容量区间

### ⚠️ 矛盾点与风险提示
- 🔴 **无具名决策人**：官网无团队页/具名联系人 → **仅角色邮箱，按 §4.4 显式标风险**。
- ⚠️ **业务口径差**：首页 About 偏"战略/商业/合同咨询"，About Us 偏"注册工程师设计与施工" → **须电话确认其电气设计能力与承接范围**。
- ⚠️ **成立年份 / 人数 / 地址以外信息未获取** → 正文不引用。
- ⚠️ **电压未获取** → 正文不引用电压数字。
- ⚠️ **同名风险**：与 **SASA Consulting Ltd（sasaconsulting.ca）** 名称近似，**不同主体** → 勿混（见排除表）。
- ⚠️ **定位风险**：若其实际偏商业/合同咨询，按买方话术写会错位。
- ⚠️ **公司 LinkedIn 未找到** → 无法做 LinkedIn 侧核验。

### 信息缺口清单（请勿编造）
- **具名决策人（负责人/总经理/电气总工）**：**未找到**
- **公司成立年份**：未获取（**不得引用**）
- **员工数 / 营收**：未获取（**不可引用具体数字**）
- **电压等级 / 常用变压器容量 / 品牌**：未获取
- **其是否真做电气设计（vs 商业/合同咨询）**：**口径不一，须电话确认**
- **APEGS Certificate of Authorization 号 / 注册主体全称**：未查
- **其设计项目的终端业主（买方）是谁**：未获取

### 一句话画像
Regina（SK）一家工程咨询公司，**官网首页以 "Innovative Engineering for Your Transmission Line Design" 为题，About Us 称持 APEGS 许可、团队含注册电气/结构/土木/机械工程师、西加拿大 20+ 年经验** —— **官网公布角色邮箱 `info@saaconsulting.ca`（一手源）= B 档**；🔴 **未取得具名决策人**，且**业务口径差（商业/合同 vs 电气设计）须电话确认**。

### 渠道覆盖清单（L-1、L0–L7）
| 层 | 结果 | 一句话 |
|---|---|---|
| L-1 锁人 | ⛔ | 官网无团队页/具名联系人；**未取得具名决策人** |
| L0 官网 | ✅ | home / about-us / contact-us-1 全抓；**角色邮箱 `info@saaconsulting.ca` 明文（一手源）** |
| L1 政府一手 | ⚠️ | 官网称持 APEGS 省许可；APEGS 注册库未查 |
| L2 命名+DNS | ⚠️ | MX = Microsoft 365；SPF `-all`；**具名推演未采信**；SMTP 本机不可用 |
| L3 B2B 库 | ❌ | 未获有效具名线索 |
| L4 社媒协会 | ❌ | 公司 LinkedIn 未找到 |
| L5 黄页同址 | ⚠️ | Regina 3317 Green Jade Lane 见官网 |
| L6 电话表单 | ✅ | +1 306 535 4543 + 官网表单（未拨打/未提交）|
| L7 付费 | ❌ | 未启用 |

### 同名排除表
| 同名 | 地点 | 排除理由 |
|---|---|---|
| **SASA Consulting Ltd**（sasaconsulting.ca）| CA | 🔴 **名称极近，不同主体**（Saeid Sadeghi, P.Eng. 结构工程，Iowa State 1979）→ **勿混** |
| SAA Consulting（saaconsulting.co.in）| India | 猎头/领导力咨询，无关联 |
| SAA Consulting Group LLC | US | D&B 收录，不同主体 |
| Saskatchewan Association of Architects (SAA) | CA SK | 建筑师协会，非本家 |
