# 【买家 285】开发信交接单 — Noble Electric Ltd.

> 采集日期：2026-10-01 ｜ 来源：batch8 名单（noble-electric.ca，MB）｜ 一句话结论：**曼省 St Andrews（大温尼伯区）的全牌照电气承包商，服务矿业（Hudbay）、市政、工业、商业与住宅，自述「fully certified for high voltage」，业务含水/污水处理系统、HVAC、自动化、结构化布线、医疗电气 —— 典型 B 型承包商；业主为持牌电工 Duane Noble（温尼伯市政府执照 Active，2026-09-24 复核）—— ⚠️ 但官网仅有表单、无任何邮箱，外部登记库/协会名录亦无具名邮箱，且该域走 Google Workspace（SMTP 反枚举，无法验证）⇒ 邮箱「未找到」，发信资格 ⛔ 拦截。**
> ⚠️ 本表严格区分「已验证」与「未获取」；未找到的信息一律标注，不做推断填充。
> ⛔ **本单未过发信资格闸门**：**邮箱未找到** → **拦截（第 1 条）**；**拦截 ≠ 消失**，标 `待补充`。

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示
Noble Electric Ltd. | Duane Noble | 业主 / 持牌电工（Owner-Operator，公司名含其姓氏）| 🔴 **未找到** | **未找到** | 未找到 | 曼省 St Andrews（大温尼伯）的全牌照电气承包商，服务**矿业（Hudbay）/市政/工业/商业/住宅**；业务含电气项目管理、系统设计安装、水/污水处理系统、HVAC、自动化与系统控制、结构化布线（Cat5/6/光纤）、电气升级与维修、医院医疗电气；自述「fully certified for high voltage, high-places」 | 官网 home / contact-us / projects / blogs 实抓 + TradesVerified（温尼伯市政府执照）+ D&B + 多家本地名录 + DNS(MX/A) + SMTP 实测 | ⚠️ **承包商（非制造/非竞品）**；⛔ **无邮箱**；正文不引用员工数/成立年份

## 二、补充信息（扩展段）

### 标准字段明细
- 国家+城市：**加拿大 Manitoba**（办公地 **St Andrews**，即大温尼伯区东北的 RM of St Andrews；⚠️ **CSV 原值写「Winnipeg」，实测办公地在 St Andrews**，已修正；其官网自述「Electrical Contractor in Winnipeg」）
- 详细地址：**11 Chizick Drive, St Andrews, MB R1A 2A5**（官网 Contact 页 + 多家名录一致）
- 电话：**1 (204) 687-0475**（周一–周五 8:00–17:00）
- LinkedIn：**未找到**（公司页与个人页均未检索到）
- 网站：**www.noble-electric.ca**（⚠️ **该域与 BC 省 Whistler 的同名「Noble Electric」（nobleelectric.ca）不是同一家公司**）
- 成立日：**未获取**
- 规模：**未获取**（**正文不引用任何数字**）
- 法人主体：**Noble Electric Ltd.**（官网署名）
- 执照：✅ **City of Winnipeg Licensed Contractor（Electrical, License Type A）** —— 经 TradesVerified 转引市政府数据，**状态 Active，最近复核 2026-09-24**（政府一手源转引）

### 联系人（含 still_here 在职核验）
| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| **Duane Noble（建议目标，但无邮箱）** | 业主 / 持牌电工（Owner-Operator）| TradesVerified：**「Noble, Duane of Noble Electric Ltd. — Licensed Electrician」**（License Type A，政府验证）；公司名含其姓氏 | **未获取** | 高：**市政府执照 Active，2026-09-24 复核** | **低**（政府执照现役）| 未找到 |

> 🔴 **一家只发 1 人**：**Duane Noble** 是唯一可识别的决策人（持牌电工 + 公司同姓）。
> ⛔ **但其邮箱未找到** → **本单无合格主送对象**，标 `待补充`。
> ⚠️ 未发现其他具名人员公开线索。

### 邮箱分档（A/B/C）
- **A 档（具名决策人邮箱，已验证）**：❌ **未找到**
- **B 档（角色邮箱）**：❌ **未找到**（官网 **只有联系表单**，未公布任何 `info@`/`sales@`）
- **C 档**：❌ 未找到
- **主送路径**：⛔ **无** —— **建议走电话 1 (204) 687-0475 / 官网表单**取得邮箱后回填。
- 🔴 **H6 说明**：**连角色邮箱都未取得**（非「仅角色邮箱」）⇒ **显式写明「未取得任何邮箱（含角色邮箱），未取得决策人直邮」**，列为本条风险。
- 🔴 **MX 实测**：`noble-electric.ca` MX = **Google Workspace**（`aspmx.l.google.com` + `alt1–4.aspmx.l.google.com`）→ **域真实存在且收信**。
- 🔴 **SMTP 实测无效**：向 `aspmx.l.google.com` 发 RCPT，**控制组、随机地址、候选地址全部返回 `250 2.1.5 OK`** ⇒ **Google Workspace 反枚举，RCPT 探测对本域完全无效** ⇒ **不得据 SMTP 断言任何地址存在**（H2）。

### 我为什么找他
- 官网自述 **「We install, repair and upgrade electrical systems at any scale, and are trusted by partners in the mining industry, municipalities and commercial & residential construction」**，并列 **「Fully certified for high voltage, high-places」** —— **高压电气能力 + 矿业/市政客户** ⇒ **变电站与配电设备采购场景**，典型 B 型承包商。
- 官网博客《The Ultimate Guide to Industrial Electrical Services in Manitoba》明述 **「High-Voltage Systems: Our high-voltage specialists design systems that manage electrical loads efficiently, crucial for industrial machinery」**，并提及 **CSA C22.1-21 合规、电弧闪风险评估、SCADA 改造、Teck90 电缆** ⇒ **具备高压工业电气系统设计与实施能力**，与我方变压器应用场景对口。
- **决策人 = 业主 Duane Noble（持牌电工，公司同姓）** —— 小企业主即决策口。

### 买家类型 / 需求品类
- 买家类型：🔥 **B 电气承包商（工业/矿业/市政，高压能力）**——实测画像 B 型（占 62%）
- 需求品类（带结论态）：
  - `三相液浸配电变 / 三相美变（UL E541627，45–5,000 kVA，可直供）` —— 工业/商业配电主切口
  - `三相液浸电力变（UL E541626，72–121 kV、750–110,000 kVA，可直供）` —— 其高压/矿业业务对口，条件试探
  - `单相柱上变（认证在办 E544629，条件切入）` —— 若涉及配电线路，条件切入
  - `干变（加拿大可谈，有 CSA 项目报告，需人工确认）` —— 其医院/商业客户可能有干变需求，**备选**
  - ⚠️ 客户在**加拿大**：干变按「加拿大可谈」处理；**绝不写 `CSA Certified`**

### 电压·频率·认证要求
- 电压：官网未列具体 kV（仅「high voltage / high-places」+ 博客提及工业高压系统）→ 具体采购 kV/kVA **首轮问**
- 频率：**60 Hz**（加拿大，产品零改造适配）
- 认证：加拿大市场按 **CSA / IEEE / IEC 标准**；我方持 **UL E541626** 与 **E541627** 正式 CoC —— ⛔ **不得写 `CSA Certified`**，只可写 `built to CSA/IEEE/IEC standards`
- ⚠️ **注意**：官网博客称其自身「adhering to CSA standards, such as CSA C22.1-21」—— 这是**其施工合规标准**，**不是我方认证**，勿混淆。

### 采购信号
- 官网自述 **高压电气能力 + 矿业（Hudbay）/市政/工业客户** → 高压设备采购职能
- 业务含 **水/污水处理系统、HVAC、自动化与系统控制、SCADA 改造、医疗电气** → 电气设备与控制系统长期需求
- **市政府 Electrical License Type A（Active，2026-09 复核）** → 合规在营
- 官网项目含 **Northland Ford 电气与结构化布线、Chicken Chef 餐饮、Hudbay 矿、Humboldt 学校、Aspen Grove** 等 → 稳定的本地项目流

### 可利用的钩子（按强度排序）
1. **官网自述「高压电气能力 + 矿业/市政客户」**（一手源）—— 与我方变压器能力对口
2. **官网博客明列工业高压系统设计 + CSA C22.1 合规 + SCADA 改造**（一手源）—— 技术能力强对口信号
3. **业主 Duane Noble 即决策口（持牌电工）** —— 冷触达直达决策人
4. **矿业客户（Hudbay）+ 市政项目** —— 工业电力场景
5. ⚠️ **但无邮箱** → 钩子暂无法落地，需先取得联系方式

### 开发信建议
- **收件人策略**：⛔ **无合格主送邮箱** —— **建议先电话 1 (204) 687-0475 / 官网表单索取邮箱**，取得后再回填本单
- 🔴 **域名提醒**：官网域 = **`noble-electric.ca`**；⚠️ **绝不可**误写为 **`nobleelectric.ca`**（那是 **BC 省 Whistler 的同名不同公司**）
- 🔴 **话术红线**：**不引用员工数/成立年份**；不写 `CSA Certified`（勿把对方的 CSA C22.1 施工标准当作我方认证）
- **开场角度**：若触达，从其 **官网自述的「高压电气 + 矿业/市政」** 切入（写信 agent 决定措辞）
- **发送时段**：MB **CST（中部标准时区，全年不夏令）**，周二–周四当地上午 ≈ **北京时间 22:00–01:00**
- **送达配置**：MX = **Google Workspace**；⚠️ 送达风险低（大厂），但**邮箱未知**
- **附件建议**：不带名录/供货记录

### ⚠️ 矛盾点与风险提示
- 🔴 **无邮箱（最重要）**：官网**只有联系表单**；外部登记库（市政府执照 / D&B / 本地名录）**均无邮箱**；该域走 **Google Workspace，SMTP 反枚举不可验证** ⇒ **邮箱「未找到」**，**不得推演填充**（H2）。
- 🔴 **同名公司陷阱**：BC 省 Whistler 有一家 **Noble Electric（nobleelectric.ca）**，联系人 Stephen Brawn / Steve Noble —— **与本单无关，切勿混用其邮箱**。
- ⚠️ **CSV 城市值有误**：CSV 写 Winnipeg，实测办公地 **St Andrews**（RM of St Andrews，大温尼伯区）。
- ⚠️ **成立年份/规模未获取** → **正文不引用任何数字**。
- ⚠️ **公司/个人 LinkedIn 未找到** → 缺社交佐证。
- ⚠️ **官网为营销代理维护**（作者 slug 为 `agopalansupport-websitepro-hosting` / `joshsicamarketing-com`）→ 站点内容偏营销口径，**技术细节以官网自述为准**。

### 信息缺口清单（请勿编造）
- 🔴 **邮箱（含角色邮箱）**：**未找到** —— 本单最大缺口
- **Duane Noble 的任职时长**：未获取
- **成立年份 / 员工数 / 营收**：未获取（**不可引用具体数字**）
- **采购的具体变压器 kV / kVA / 品牌 / 认证要求**：未获取
- **是否已固定变压器供应商 / 是否进口**：未获取
- **公司/个人 LinkedIn**：未找到
- **官网办公地 vs CSV 城市**：已修正为 St Andrews

### 一句话画像
曼省 St Andrews（大温尼伯）一家 **全牌照电气承包商**（City of Winnipeg Electrical License Type A，Active），自述**具备高压电气能力**，服务**矿业（Hudbay）/市政/工业/商业/住宅**，业务含电气项目管理、系统设计安装、水/污水处理、HVAC、自动化与 SCADA、结构化布线、医疗电气 —— **业主 Duane Noble 是持牌电工即决策口**，🔴 **但官网仅有表单、全渠道无邮箱，且域走 Google Workspace 无法 SMTP 验证 ⇒ 邮箱未找到，发信资格拦截（第 1 条），标 `待补充`。**

### 渠道覆盖清单（L-1、L0–L7）
| 层 | 结果 | 一句话 |
|---|---|---|
| L-1 锁人 | ✅ | TradesVerified（转引 City of Winnipeg 执照）：Duane Noble, Licensed Electrician, Noble Electric Ltd. |
| L0 官网 | ⚠️ | home / contact-us / projects / blogs 实抓；**仅有联系表单，无任何邮箱、无 Team 页** |
| L1 政府/协会一手 | ⚠️ | 市政府 Electrical License Type A（Active，2026-09 复核）—— **有执照、无邮箱** |
| L2 命名+DNS | ⚠️ | MX=**Google Workspace**；**SMTP 反枚举（全部 250）⇒ 无法验证任何地址** |
| L3 B2B 库 | ⚠️ | D&B / chamberofcommerce / infobel / cylex 有条目，**均无邮箱** |
| L4 社媒协会 | ❌ | 公司/个人 LinkedIn **未找到**；WCA 名录无邮箱字段 |
| L5 黄页同址 | ⚠️ | chamberofcommerce / renogiants / mapquest 同址在列（旁证在营）|
| L6 电话表单 | ✅ | **1 (204) 687-0475** + 官网联系表单 ← **当前唯一可用触达路径** |
| L7 付费 | ❌ | 未启用 |

### 同名排除表
| 同名 | 地点 | 排除理由 |
|---|---|---|
| 🔴 **Noble Electric（nobleelectric.ca）** | **BC Whistler** | **完全不同公司**（联系人 Stephen Brawn / Steve Noble，做高端住宅电气）—— **切勿混用** |
| Noble Electricals（noblelites.com）| 美国/印度 | LED 照明制造商，**无关** |
| Noble Construction Corp. | SK Esterhazy | 矿业/机械总包，**无关** |
| Noble（noble.ca）| ON London | 电子元件制造商，**无关** |
| Duane Noble（其他同名）| — | 须按 **Noble Electric Ltd. + St Andrews MB + 持牌电工** 锁定 |
