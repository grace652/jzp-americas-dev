# 【买家 234】开发信交接单 — PNH Engineering Ltd.

> 采集日期：2026-09-30 ｜ 来源：batch7 名单（pnhengineering.com，BC Coquitlam）｜ 一句话结论：**BC Coquitlam 的专业工程公司，做高压/中压变电站的电气与保护控制设计（含设备规格书、MV 单元变电站、BOM）；但官网（© 2021）所列唯一具名负责人 Pritam Haldar，经核已为新公司 Gridwise Engineering 的联合创始人 → 离职风险🔴 → 本单拦截。**
> ⚠️ 本表严格区分「已验证」与「未获取」；未找到的信息一律标注，不做推断填充。
> ⛔ **本单拦截**：唯一具名联系人离职风险🔴；无第二具名联系人；且公司官网陈旧（© 2021），主体状态存疑 → **发信前须电话定性**。

## 闸门（留痕）

- 发信资格：⛔ **拦截（合格线闸门第 3 条：唯一具名联系人离职风险🔴，无第二联系人改发）**；另涉**第 5 条相关**（主体状态存疑，须电话定性）
- 邮箱档位：**B（角色邮箱 `info@pnhengineering.com`）** —— 但**因联系人缺失，本单不发**
- 排重：与 `clients/`、`交接单/batch1–6`、`发信队列.json`、`发送日志.csv`、`退信黑名单.json`、`永久排除名录.md` 逐条比对 → **0 命中** ✅
- 🔴 **拦截处置**：仍建线索池条目，标 `待补充`；**绝不为了凑数量而放行**。

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示
PNH Engineering Ltd. | （无有效具名联系人）| — | `info@pnhengineering.com`（**B 档角色邮箱，官网一手源**）| **已验证（官网一手源明文；格式校验通过）** | 未找到 | BC Coquitlam 专业工程公司，做 HV/MV 变电站电气与保护控制设计（含设备规格书、MV 单元变电站、BOM），兼做建筑制图；官网 © 2021 陈旧 | 官网 home/why-choose-us/substation-electrical-design 实抓 + LinkedIn（Pritam Haldar 现任别处）+ Gridwise Engineering 团队页 + DNS(MX/SPF) 实测 | 🔴 **唯一具名负责人已离职（现为 Gridwise 联合创始人）→ 不得发**；⚠️ 公司网站陈旧，主体是否仍经营**存疑，须电话定性**
```

## 二、补充信息（扩展段）

### 标准字段明细
- 国家+城市：**加拿大 British Columbia**，Coquitlam
- 详细地址：🔴 **官网未公布实体门牌地址**（仅称 Coquitlam, BC）
- 电话：**+1-778-558-3294**（官网页脚）
- LinkedIn：公司页未找到；个人页未确认
- 网站：**pnhengineering.com**（WordPress；**邮箱域 = 官网域 pnhengineering.com**，MX = **Microsoft 365** `pnhengineering-com.mail.protection.outlook.com`）
- 成立日：🔴 **未获取**（官网页脚 © 2021 PNH Engineering Ltd.）
- 规模：⚠️ **未获取**（官网仅称 "Our principal has more than 20 years"）→ **不引用人数**
- 法人主体：**PNH Engineering Ltd.**（官网页脚署名）
- 业务定位：**专业工程公司 / 设计咨询（specifier）**

### 联系人（含 still_here 在职核验）
| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| **Pritam Haldar（官网所列 Principal）** | Principal（官网口径）| 官网 why-choose-us："Our principal, Pritam Haldar, has more than 23 years of experience…" | 未获取 | ⚠️ **LinkedIn 现任 "Partner at Gridwise Engineering"**；Gridwise 团队页记其为 **co-founder**（"Pritam is a co-founder of Gridwise Engineering"）| **🔴 高**（现任别处）→ **不得发** | `ca.linkedin.com/in/pritam-haldar-p-eng-ceng-14462a22` ✅（现职 Gridwise）|
| （第二具名联系人）| — | **未找到** | — | — | — | — |

> 🔴 **一家只发 1 人 + 唯一人已离职**：官网唯一具名负责人 Pritam Haldar 现为 **Gridwise Engineering 联合创始人**（其 LinkedIn 与 Gridwise 官网团队页双证）→ **本单无可发对象**，**拦截**。

### 邮箱分档（A/B/C）
- **B 档（角色邮箱，官网一手源）**：✅ **`info@pnhengineering.com`**（官网页脚明文）
- **A 档（具名）**：❌ **未取得**（官网未公布具名邮箱；`pritam@` 等**无样本，禁推演**）
- **主送路径**：⛔ **本单不发**（唯一具名联系人已离职，无第二联系人）
- ⚠️ **H6 说明**：仅角色邮箱，且「升级三步」未获具名决策人 → **显式标风险**（见下）。
- 🔴 **SMTP 不可用**：本机 25 端口整体不可用 → 未能做 RCPT 复核。

### 我为什么找他
- 官网 **Substation Electrical Design** 页逐字列出交付物含 "**Equipment specifications**"、"**Medium voltage unit substations**"、"**Material lists**"、"**Bill of materials for estimate support**" —— **一家为 HV/MV 变电站出设备规格书与 BOM 的工程公司，是变压器规格的制定方**（渠道价值）。
- 官网称其经验含 "**Greenfield / Brownfield substation**"、"**Asset replacement**（circuit breakers, disconnect switches, VTs/CVTs, protection relays…）" —— **资产更换场景明确，与变压器更换相关**。
- ⚠️ 但其**核心负责人已转往新公司**，上述能力的**现承接主体存疑**。

### 买家类型 / 需求品类
- 买家类型：🔥 **B 型（工程/设计咨询，规格制定方 / specifier）**——⚠️ **非终端采购方**
- 需求品类（带结论态）：
  - `三相液浸配电变 / 三相美变（UL E541627，45–5,000 kVA，可直供）` —— 其 MV 单元变电站场景对口
  - `三相液浸电力变 / 主变（UL E541626，72–121 kV、750–110,000 kVA，可直供）` —— 变电站场景，条件试探
  - `变电站小主变 SF 系列（36–48 kV，ECD 计划函，条件切入）` —— **条件切入**
  - `干变（加拿大实体可谈，有 CSA 项目报告，需人工确认）` —— 备选，不首推
  - ⚠️ 客户在**加拿大**：干变按「加拿大可谈」处理；**绝不写 `CSA Certified`**

### 电压·频率·认证要求
- 电压：官网称 "high voltage switching stations and substations, medium voltage unit substations"；🔴 **具体 kV 未获取** → **正文不引用电压数字**
- 频率：**60 Hz**（加拿大，产品零改造适配）
- 认证：加拿大市场按 **CSA / IEEE / IEC 标准**；我方持 **UL E541626** 与 **E541627** 正式 CoC —— ⛔ **不得写 `CSA Certified`**，只可写 `built to CSA/IEEE/IEC standards`

### 采购信号
- 官网列 **"Equipment specifications"** 与 **"Bill of materials"** → **规格制定方，可影响选型**
- 官网列 **Asset replacement（CB/开关/继电器等）** → 资产更换场景
- ⚠️ **未发现其自身采购变压器的证据** → 定位为**渠道/规格方**

### 可利用的钩子（按强度排序）
1. **变电站设备规格书 + BOM 交付**（官网一手源）—— 进入规格/合格供方角度
2. **Greenfield/Brownfield + Asset replacement** —— 资产更换场景角度
3. **GIS（气体绝缘开关设备）经验** —— 高压设备场景角度
> ⚠️ **上述钩子均因「主体/联系人存疑」暂缓使用**，待电话定性后再启用。

### 开发信建议
- **收件人策略**：⛔ **本单不发**。**先电话 +1-778-558-3294 定性**：(1) 公司是否仍在经营；(2) 现负责人是谁、是否仍做变电站设计。**定性通过后**再补具名联系人并重开本单。
- 🔴 **定位红线**：PNH 为**设计咨询方**（非买方）→ 话术应定位"进入其设备规格/合格供方"
- 🔴 **话术红线**：**不引用人数/成立年份/电压数字**；**不提 Pritam Haldar**（已离职，勿踩雷）
- **发送时段**：BC = **PT（太平洋时区）**，周二–周四当地上午 ≈ **北京时间 23:00–02:00**（夏令时期间）
- **送达配置**：MX = **Microsoft 365**；SPF 齐备；发信域须 SPF/DKIM/DMARC 齐备
- **附件建议**：不带名录/供货记录；如需仅附 UL 证书号 + 容量区间

### ⚠️ 矛盾点与风险提示
- 🔴 **唯一具名负责人已离职**：Pritam Haldar 现为 **Gridwise Engineering 联合创始人**（LinkedIn + Gridwise 团队页双证）→ **不得发**（闸门第 3 条）。
- 🔴 **公司主体状态存疑**：官网 © 2021 陈旧、无实体地址、负责人转往新公司 → **疑公司已停业或休眠，须电话定性**（闸门第 5 条相关）。
- ⚠️ **无第二具名联系人** → 无法改发第二人。
- ⚠️ **成立年份 / 人数 / 地址未获取** → 正文均不得引用。
- ⚠️ **电压未获取** → 正文不引用电压数字。
- ⚠️ **H6**：仅角色邮箱，升级三步未获具名决策人 → **显式标风险**。

### 信息缺口清单（请勿编造）
- **公司是否仍在经营**：**存疑，须电话定性**（官网 © 2021 + 负责人已离职）
- **现负责人 / 具名联系人**：**未找到**（官网所列 Pritam Haldar 已离职）
- **实体地址**：官网未公布
- **成立年份 / 员工数 / 营收**：未获取（**不可引用具体数字**）
- **电压等级 / 常用变压器容量 / 品牌**：未获取
- **BC 省 EGBC 工程许可 / 注册主体全称**：未查
- **Pritam Haldar 离职的确切时间与去向**：仅知现任 Gridwise（时间未获取）

### 一句话画像
BC Coquitlam 一家专业工程公司（HV/MV 变电站电气与保护控制设计，出设备规格书与 BOM）——⛔ **官网所列唯一具名负责人 Pritam Haldar 现为 Gridwise Engineering 联合创始人，离职风险🔴，且公司网站陈旧（©2021）、主体状态存疑 → 本单拦截，须先电话定性**。

### 渠道覆盖清单（L-1、L0–L7）
| 层 | 结果 | 一句话 |
|---|---|---|
| L-1 锁人 | ⛔ | 官网所列唯一负责人已离职；**无第二具名联系人** |
| L0 官网 | ✅ | home / why-choose-us / substation-electrical-design 全抓；**角色邮箱 `info@pnhengineering.com` 明文（一手源）** |
| L1 政府一手 | ❌ | EGBC 注册库未查；无注册主体信息 |
| L2 命名+DNS | ⚠️ | MX = Microsoft 365；SPF 齐备；**具名推演未采信**；SMTP 本机不可用 |
| L3 B2B 库 | ⚠️ | D&B / 目录仅作旁证 |
| L4 社媒协会 | ⚠️ | Pritam Haldar 个人页显示现职别处（离职证据）；无公司页 |
| L5 黄页同址 | ❌ | 无实体地址可核 |
| L6 电话表单 | ✅ | +1-778-558-3294 + 官网联系（**未拨打 → 建议先电话定性**）|
| L7 付费 | ❌ | 未启用 |

### 同名排除表
| 同名 | 地点 | 排除理由 |
|---|---|---|
| **Gridwise Engineering** | CA | 🔴 **非同名，但为负责人现所属新公司** → 若日后开发，注意与 PNH 区分 |
| PNH Limited / pnh.ca | CA | 不同主体（pnh.ca 为另一站，勿混）|
| PNH Engineering（其他同名）| — | 未发现同域名其他主体 |
| Pritam Haldar（70+ 同名 LinkedIn）| — | 须按 PNH/Gridwise + P.Eng CEng 锁定 |
