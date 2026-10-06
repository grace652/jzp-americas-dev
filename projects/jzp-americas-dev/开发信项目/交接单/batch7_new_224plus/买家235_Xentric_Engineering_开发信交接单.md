# 【买家 235】开发信交接单 — Xentric Engineering Ltd.

> 采集日期：2026-09-30 ｜ 来源：batch7 名单（xentric.ca，AB）｜ 一句话结论：**加拿大西部（Langley BC / Calgary AB / Canmore AB）的多学科工程咨询公司，做公用事业接入、69–500kV 输电线路设计、高压变电站与配电系统；官网明示 "Engineering, Procure, Construct, Manage" 理念，强调业主直接参与材料采购；官网公布角色邮箱 `info@xentric.ca`（一手源）= B 档 → 点名转交总裁。**
> ⚠️ 本表严格区分「已验证」与「未获取」；未找到的信息一律标注，不做推断填充。
> ⚠️ **本单为 B 档**：主送走角色邮箱 `info@xentric.ca` + 点名转交；⚠️ 具名总裁**姓名存在来源冲突**，须电话确认。

## 闸门（留痕）

- 发信资格：⚠️ **有条件通过**（B 档角色邮箱 → 点名转交；**总裁姓名存在来源冲突** + **邮箱为单一渲染来源（curl 被 WAF 拦截）** → 建议发信前电话 604-200-7183 一并确认总裁姓名与 `info@xentric.ca` 有效性）
- 邮箱档位：**B（角色邮箱 → 点名转交）**
- 排重：与 `clients/`、`交接单/batch1–6`、`发信队列.json`、`发送日志.csv`、`退信黑名单.json`、`永久排除名录.md` 逐条比对 → **0 命中** ✅

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示
Xentric Engineering Ltd. | Chris Wood, PhD, P.Eng., PE（⚠️ 姓名存冲突，见下）| President（LinkedIn 个人页 "About" 记 "President of Xentric Engineering Ltd"）| `info@xentric.ca`（**B 档角色邮箱**）| **官网一手源（经渲染解析）；⚠️ 单一来源，未获第二方印证** —— curl 直取被 WAF 拦截（返回 0 字节），未能二次抓原文 → **建议电话 604-200-7183 复核** | 公司 LinkedIn `linkedin.com/company/xentric-engineering-ltd`（未直取）；个人页 `ca.linkedin.com/in/chris-wood-phd-peng-pe-178817165` | 加拿大西部多学科工程咨询公司，做公用事业接入 / 69–500kV 输电线路设计 / 高压变电站 / 配电系统 / 可再生与电信；EPCM 理念（业主直采）；注册工程师覆盖 BC/AB/SK 及部分美国州 | 官网 home/contact-us 实抓 + LinkedIn（个人页）+ prospeo（邮箱格式/规模）+ Crunchbase + DNS(MX/SPF) 实测 | ⚠️ **总裁姓名来源冲突**（Chris Wood vs Chris Peng）→ 须电话确认；**成立年份口径冲突**（官网 ©2022 vs 第三方 2022）→ 正文不提年份；员工数为第三方口径（不引用）
```

## 二、补充信息（扩展段）

### 标准字段明细
- 国家+城市：**加拿大**（BC Langley / AB Calgary / AB Canmore；总部称"Western Canada"）
- 详细地址（页脚）：**Unit #103B, 1205 Bow Valley Trail, Canmore, AB T1W 1P5**
- 电话：**604-200-7183**
- LinkedIn：公司页 `linkedin.com/company/xentric-engineering-ltd` ✅（未直取）；个人页 `ca.linkedin.com/in/chris-wood-phd-peng-pe-178817165`
- 网站：**xentric.ca**（WordPress；**邮箱域 = 官网域 xentric.ca**，MX = `mailstream-*.mxrecord.io` + Microsoft 365 双路）
- 成立日：⚠️ 官网页脚 © 2022；第三方记 founded **2022** → **口径一致但仅为页脚/第三方，正文不提年份**
- 规模：⚠️ 第三方记 **21–50 人**（prospeo）→ **不引用人数**
- 法人主体：**Xentric Engineering Ltd.**（官网 "privately owned independent engineering firm"）
- 注册足迹：官网称工程师主要注册于 **BC / AB / SK**，另有部分注册于美国若干州

### 联系人（含 still_here 在职核验）
| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| **Chris Wood, PhD, P.Eng., PE（主送对象，存疑）** | President | LinkedIn 个人页 "About"："Chris Wood is the President of Xentric Engineering Ltd" | 未获取 | 未获取 | **中**（⚠️ **来源冲突**：Aeroleads 记其 "**previously** worked as President at Xentric"；RocketReach 另记总裁为 "**Chris Peng**"）→ **须电话确认** | `ca.linkedin.com/in/chris-wood-phd-peng-pe-178817165` ✅ |
| Matt Morgan | 员工（职务未获取）| LinkedIn 记 "Experience: Xentric Engineering Ltd."（Canmore）| 未获取 | 未获取 | 中（仅第三方）| `ca.linkedin.com/in/matt-j-morgan` |
| Gracie Zhang | Telecom Engineer | RocketReach 记 "Telecom Engineer @ Xentric Engineering Ltd." | 未获取 | 未获取 | 中（仅第三方）| 未确认 |

> 🔴 **一家只发 1 人**：主送对象拟为 **Chris Wood（President）**，但**姓名/在职存在冲突** → **正文可泛称 "the President" 或先电话确认**；其余员工**不据此另发**。

### 邮箱分档（A/B/C）
- **B 档（角色邮箱）**：✅ **`info@xentric.ca`**（官网页脚；⚠️ 经渲染解析取得，**curl 直取被 WAF 拦截**，未获第二方印证 → 建议电话 604-200-7183 复核）
- **A 档（具名）**：❌ **未取得**（官网未公布具名邮箱）；⚠️ 第三方记邮箱格式为 **`{firstname}{lastname}@xentric.ca`（86.1%）**，但**推演邮箱不得作主送**（H2/H4）
- **主送路径**：**`info@xentric.ca`（B 档）**，正文首句**请求转交给负责输电线路/变电站设计的负责人（President）**
- ⚠️ **H3/H6 说明**：邮箱来自**官网一手源**（满足 H5）；**仅有角色邮箱** → 已跑「升级三步」，**未获具名决策人直邮** → **显式标风险**。
- 🔴 **SMTP 不可用**：本机 25 端口整体不可用 → 未能做 RCPT 复核，**以官网一手源为准**。

### 我为什么找他
- 官网**逐字写明**其 **Power System Equipment** 服务含 "**Detailed Specifications**"、"**Factory Acceptance Tests**"、"**Erection & Commissioning**" —— **一家为电力设备出详细规格、并参与出厂验收与安装调试的工程公司，是变压器规格与验收的直接相关方**（渠道价值高：进其规格 = 进其项目）。
- 官网明确其交付链 "from the conceptual stage, through to feasibility and front-end engineering design, detailed design, **procurement**, construction, commissioning, energization" —— **明确含 procurement 环节**。
- 官网 "**Engineering, Procure, Construct, Manage**" 理念下强调 "**the Owner is involved directly in the procurement of material and contractors**" —— **其模式重视业主直采，制造商有机会直接进入选型**。
- 官网 **Transmission Design 覆盖 69 kV to 500 kV** + **High-Voltage Substations / Power System Studies / Protection & Control** —— **覆盖我方主变区间（72–121 kV）**。

### 买家类型 / 需求品类
- 买家类型：🔥 **B 型（工程咨询 / EPCM，规格与采购参与方）**——⚠️ **偏规格/设计方**，非纯终端买方
- 需求品类（带结论态）：
  - `三相液浸电力变 / 主变（UL E541626，72–121 kV、750–110,000 kVA，可直供）` —— 其 69–121kV 输电/变电站设计区间**直接对口**
  - `三相液浸配电变 / 三相美变（UL E541627，45–5,000 kVA，可直供）` —— 配电场景
  - `≥500kV 级主变（产能可覆盖，UL 区间外，需人工确认）` —— 其设计上探至 500kV，**超出我方 UL 覆盖区间，需人工确认**
  - `干变（加拿大实体可谈，有 CSA 项目报告，需人工确认）` —— 备选，不首推
  - ⚠️ 客户在**加拿大**：干变按「加拿大可谈」处理；**绝不写 `CSA Certified`**

### 电压·频率·认证要求
- 电压：其设计覆盖 **69 kV – 500 kV**（官网一手源）；🔴 **具体项目 kV 未获取** → **正文不引用具体项目电压**
- 频率：**60 Hz**（加拿大，产品零改造适配）
- 认证：加拿大市场按 **CSA / IEEE / IEC 标准**；我方持 **UL E541626** 与 **E541627** 正式 CoC —— ⛔ **不得写 `CSA Certified`**，只可写 `built to CSA/IEEE/IEC standards`

### 采购信号
- 官网列 **"Detailed Specifications" + "Factory Acceptance Tests"** → **规格与验收参与方，可影响选型**
- 官网交付链**明确含 procurement** → 采购参与
- 官网 EPCM 理念强调**业主直采材料** → 制造商有机会直入选型
- **注册工程师覆盖 BC/AB/SK + 部分美国州** → 跨区项目

### 可利用的钩子（按强度排序）
1. **Power System Equipment：Detailed Specifications + Factory Acceptance Tests**（官网一手源）—— 最对口的规格/验收角度
2. **69–500kV 输电线路 + 高压变电站设计** —— 覆盖我方主变区间
3. **EPCM 理念 + 业主直采材料** —— 制造商直入选型角度
4. **Renewable Energy（Solar/Wind/DER）** —— 可再生配套变压器角度
5. **三地办公（Langley/Calgary/Canmore）** —— 跨区触达角度

### 开发信建议
- **收件人策略**：**B 档 → 主送 `info@xentric.ca`**，正文首句**请求转交给负责输电线路/变电站设计的负责人（President）**；电话 **604-200-7183** 并行（**建议先确认总裁姓名**）
- 🔴 **姓名冲突处理**：总裁姓名来源冲突（Chris Wood vs Chris Peng）→ **正文可泛称 "the President" 或先电话确认**，⛔ **不擅写具体姓名**
- 🔴 **话术红线**：**不引用人数**（第三方口径）；**不提成立年份**；**不引用具体项目电压**
- **开场角度**：从其 **设备详细规格 + 出厂验收（FAT）** 参与切入（写信 agent 决定措辞）
- **发送时段**：AB = **MT（山地时区）**，周二–周四当地上午 ≈ **北京时间 22:00–01:00**（夏令时期间）
- **送达配置**：MX = mxrecord.io（邮件安全网关）+ Microsoft 365；SPF `-all`（严格）；发信域须 SPF/DKIM/DMARC 齐备
- **附件建议**：不带名录/供货记录；如需仅附 UL 证书号 + 容量区间 + 技术标准（IEEE C57.12）

### ⚠️ 矛盾点与风险提示
- ⚠️ **总裁姓名来源冲突**：LinkedIn "About" 称 **Chris Wood** 为 President；Aeroleads 记其 "**previously**"；RocketReach 另记 **Chris Peng** 为 President/CEO → **须电话确认，正文不擅写姓名**。
- ⚠️ **B 档角色邮箱 + 无具名直邮** → 必须点名转交（§4.4 / H6）。
- ⚠️ **成立年份仅页脚/第三方（2022）** → **正文不提年份**。
- ⚠️ **人数为第三方口径（21–50）** → **正文不引用人数**。
- ⚠️ **定位**：偏**工程咨询/规格方** → 话术应定位"进入其设备规格"，不宜直接报价成交。
- ⚠️ **电压仅知设计区间（69–500kV）** → 正文不引用具体项目电压。
- ⚠️ **邮箱格式推演（{firstname}{lastname}@）来自第三方** → **不得作主送**（H2/H4）。

### 信息缺口清单（请勿编造）
- **总裁的确切姓名**（Chris Wood vs Chris Peng）：**存疑，须电话确认**
- **具名决策人直邮**：**未取得**（仅有角色邮箱；推演不得主送）
- **Chris Wood 的任职时长 / 最近活跃 / 是否仍在任**：未获取
- **成立年份 / 员工数 / 营收**：未获取或仅第三方（**不可引用具体数字**）
- **具体项目电压 / 常用变压器容量 / 品牌**：未获取
- **AB/BC 省注册主体全称 / 工程许可号**：未查
- **是否自持 EPC 施工能力（还是仅咨询）**：未确认

### 一句话画像
加拿大西部（Langley/Calgary/Canmore）一家**多学科工程咨询公司**（公用事业接入 / 69–500kV 输电线路 / 高压变电站 / 配电 / 可再生与电信），**官网明示设备详细规格、出厂验收（FAT）与 EPCM 业主直采理念** —— **官网公布角色邮箱 `info@xentric.ca`（一手源）= B 档，点名转交总裁**；⚠️ 总裁**姓名来源冲突**、无具名直邮 → 建议先电话 604-200-7183 确认。

### 渠道覆盖清单（L-1、L0–L7）
| 层 | 结果 | 一句话 |
|---|---|---|
| L-1 锁人 | ⚠️ | 第三方记总裁为 Chris Wood（**冲突**：另有 Chris Peng）；**官网无具名** |
| L0 官网 | ✅ | home / contact-us 全抓；**角色邮箱 `info@xentric.ca` 明文（一手源）** |
| L1 政府一手 | ⚠️ | 官网称工程师注册 BC/AB/SK + 部分美国州；注册库未查 |
| L2 命名+DNS | ⚠️ | MX = mxrecord.io + Microsoft 365；SPF `-all`；**具名推演未采信**；SMTP 本机不可用 |
| L3 B2B 库 | ⚠️ | prospeo（邮箱格式）/ Crunchbase / RocketReach / Aeroleads 仅作旁证 |
| L4 社媒协会 | ⚠️ | 公司 LinkedIn + 个人页（Chris Wood）命中未直取；官网链 EGBC |
| L5 黄页同址 | ⚠️ | Canmore 1205 Bow Valley Trail 为页脚地址 |
| L6 电话表单 | ✅ | 604-200-7183 + 官网联系表单（未拨打/未提交）|
| L7 付费 | ❌ | 未启用 |

### 同名排除表
| 同名 | 地点 | 排除理由 |
|---|---|---|
| Xentric（其他同名）| — | 未发现同域名其他主体 |
| Chris Wood vs Chris Peng | CA | 🔴 **同一职位的两个姓名口径** → 须电话确认，交人工判 |
| Xentric 类似名（Xentrik 等）| 多地 | 不同主体 |
