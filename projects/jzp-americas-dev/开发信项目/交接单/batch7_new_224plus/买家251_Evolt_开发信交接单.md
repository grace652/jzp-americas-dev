# 【买家 251】开发信交接单 — Evolt（Evolt Electrical Supply）

> 采集日期：2026-09-30 ｜ 来源：batch7 名单（evolt.ca，BC）｜ 一句话结论：**BC Burnaby + AB Edmonton 的 100% 加拿大本土电气批发商（1998 年起，Lite-scape Lighting Inc 旗下），官网自述 "specialized supplier of lighting, switchgear, circuit protection, panels, breakers, landscape lighting" —— 明确的分销商（非制造/非竞品）；官网只公布角色邮箱 `team@e-volt.ca` / `customer@evoltsupply.com` = B 档 → 点名转交。⚠️ 产品重心在照明/开关柜/配电盘，液浸变对口度偏低。**
> ⚠️ 本表严格区分「已验证」与「未获取」；未找到的信息一律标注，不做推断填充。
> ⚠️ **本单过 B 档**，但**品类对口度偏低（低优先级）**：邮箱为角色邮箱，须点名转交。

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示
Evolt（Evolt Electrical Supply，Lite-scape Lighting Inc 旗下）| David Hinbest（拟转交，第三方）/ Jaret Larson | President（第三方口径）| `team@e-volt.ca`、`customer@evoltsupply.com`（**B 档角色邮箱**，官网一手源）| **已验证（角色邮箱）**；具名邮箱**未获取** | 公司 LinkedIn 未找到；个人页 `ca.linkedin.com/in/jaret-larson-evolt` | BC Burnaby + AB Edmonton 的 100% 加拿大本土电气批发商（1998 年起）；产品含照明、开关柜、线路保护、配电盘、断路器、景观照明；以 e-commerce 平台为主 | 官网 home / faq / Electrician_TradePro 实抓 + 官网 blog + LinkedIn 个人页 + Datanyze/Kona（旁证）+ DNS(MX/SPF) 实测 | ⚠️ 分销商（非制造）；**产品重心照明/开关柜，液浸变对口度低**；微企，禁用"行业领先/大集团"话术
```

## 二、补充信息（扩展段）

### 标准字段明细
- 国家+城市：**加拿大 British Columbia**（Burnaby）+ **Alberta**（Edmonton）
- 详细地址：**5608 Goring St #6, Burnaby, BC V5B 3A3**（Datanyze，**第三方口径**）；另有 Edmonton 仓
- 电话：**1-888-739-3555**（官网）；(604) 428-9898（Datanyze 第三方）
- LinkedIn：公司页未找到；个人页 `ca.linkedin.com/in/jaret-larson-evolt`
- 网站：**www.evolt.ca**；另有 `blog.evolt.ca`（邮箱域 = `e-volt.ca` 与 `evoltsupply.com`，**多域并存**）
- 成立日：**1998 年**（官网自述"story began in 1998 as Lite-scape Lighting"）
- 规模：未获取（第三方 Datanyze 记 14 人 / Kona 记 $1.2M，**均为第三方估算，正文不得引用**）
- 法人主体：**Lite-scape Lighting Inc.**（官网自述 Evolt.ca 为其一 division）；品牌 **Evolt Electrical Supply**
- 执照：未获取

### 联系人（含 still_here 在职核验）
| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| **Jaret Larson（拟转交）** | 管理/日常运营（"management of day-to-day…"）| LinkedIn 个人页现任，就职 **Evolt.ca（Lite-scape Lighting Inc 旗下）** | 未获取 | 高：LinkedIn 现任 + 官网 blog 署名文章（2025）| **中**（LinkedIn 单一来源）| `ca.linkedin.com/in/jaret-larson-evolt` |
| David Hinbest | President（第三方口径）| Datanyze 记 **President**，**未在官网证实** | 未获取 | 低 | **中**（仅第三方单一来源）| 未找到 |

> 🔴 **一家只发 1 人**：拟转交 **Jaret Larson**（LinkedIn 现任 + 官网 blog 署名，双源较实）。
> ⚠️ "David Hinbest President" 仅第三方单一来源，**不据此称职务**。

### 邮箱分档（A/B/C）
- **A 档**：未获取
- **B 档（角色邮箱，官网一手源）**：`team@e-volt.ca`（产品咨询）、`customer@evoltsupply.com`（客户/批量）—— 均抓自官网 faq 页明文；格式校验通过
- **主送路径**：**B 档点名转交** —— 正文首句请求转交 **Jaret Larson**
- ⚠️ **H6 升级三步**：① 官网无 `purchasing@` / `supplier@` 线索；② 无真实回信样本可反推；③ 推演（`david@e-volt.ca` 等，Datanyze 记格式 `first@e-volt.ca`）**无一手源，不做**。
  → **三步全失败：本单仅取得角色邮箱，未取得决策人直邮，列为风险。**
- 🔴 **SMTP 不可用**：`evolt.ca` MX = `x-shops.com`（电商平台自建邮）；本机 25 端口外发整体不可用 → 未能做 RCPT 复核，**以官网一手源为准**。
- ⚠️ **多域风险**：官网同时出现 `evolt.ca` / `e-volt.ca` / `evoltsupply.com` → **发信前须确认哪个域是有效收件域**。

### 我为什么找他
- Evolt 官网自述 **"a specialized supplier of lighting, switchgear, circuit protection, panels, breakers, landscape lighting, and electrical products"** —— 明确含 **switchgear**（开关柜）与**配电类**产品，**属电气分销商（非制造）**。
- 其 **100% 加拿大本土 + "Made-in-Canada brands"** 定位（官网 blog 逐条列 Axite/Bel/Code Electric 等加拿大制造品牌）——**但正因如此，其对外来品牌接受度可能偏低**，须以"补充品类/规格缺口"切入。
- 官网 **"multiple brand offerings and commercial items not available at other wholesalers"** + **"Project pricing / Make an Offer"** ——**有补充品牌与项目配货的机制**。

> ⚠️ **诚实提示**：Evolt 的产品重心是**照明 + 开关柜 + 配电盘 + 断路器**（e-commerce 通货品），**官网未见 power transformer / 液浸变产品线**。→ **品类对口度低，列为低优先级**；若开发，钩子只能落在 **switchgear / 配电类** 的**规格缺口与替代供应**上，**不可硬推液浸变**。

### 买家类型 / 需求品类
- 买家类型：**A 电气批发分销商（e-commerce 为主，BC+AB）**——实测画像 A 型
- 需求品类（带结论态）：
  - `三相液浸配电变（UL E541627，45–5,000 kVA，可直供）` —— **官网未见该品类，仅条件试探，不作首推**
  - `干变（加拿大可谈，有 CSA 项目报告，需人工确认）` —— 其配电/开关柜客户场景可能有干变需求，**条件试探**
  - `开关柜 / 配电盘相关配套（OLTC 等，配套可直供）` —— 与其 switchgear 主业相关，**条件切入**
  - ⚠️ **不推**：液浸变作为首推（官网无该品类，硬推易显群发）；**绝不写 `CSA Certified`**
  - ⚠️ 客户在**加拿大**：干变按「加拿大可谈」处理

### 电压·频率·认证要求
- 电压：**未获取**（官网以 600 V 级产品为主，未见中高压变压器规格）→ 首轮问
- 频率：**60 Hz**（加拿大，产品零改造适配）
- 认证：加拿大市场按 **CSA / IEEE / IEC 标准**；我方持 **UL E541626** 与 **E541627** 正式 CoC —— ⛔ **不得写 `CSA Certified`**，只可写 `built to CSA/IEEE/standards`
- ⚠️ 官网自述其品牌为 **"Trusted CSA-approved brands"** → 其采购决策**高度看重 CSA**，而我方**无 CSA 证书** → **这是本家最大硬伤，须在信中主动说明"built to CSA/IEEE/IEC standards"而非"certified"**

### 采购信号
- 官网 **"Order millions of products… multiple brand offerings"** → 有品牌引入机制
- **"Project pricing / bundle discounts / Make an Offer"** → 项目配货
- **e-commerce + 1500+ 制造商直发** → 供应链开放
- ⚠️ 但**未见变压器采购信号** → 采购信号弱

### 可利用的钩子（按强度排序）
1. **官网自述含 switchgear / circuit protection / panels**（一手源）—— 配电类配套角度
2. **"commercial items not available at other wholesalers"** —— 补充品牌角度
3. **BC+AB 双仓 + 1500+ 制造商直发** —— 供应链角度
4. ⚠️ **液浸变对口度低** → **不作钩子**

### 开发信建议
- **收件人策略**：⚠️ **B 档点名转交** —— 发 `team@e-volt.ca`（或 `customer@evoltsupply.com`），首句请求转交 **Jaret Larson**；电话 **1-888-739-3555** 并行跟进
- 🔴 **域名提醒**：⚠️ 官网多域并存（`evolt.ca` / `e-volt.ca` / `evoltsupply.com`）→ **发信前确认有效收件域**
- 🔴 **话术红线**：微企 → **禁用"行业领先/大集团"话术**；**不引用人数/营收/成立年份**；**不写 `CSA Certified`**
- 🔴 **品类红线**：**不把钩子挂在液浸变上**（官网无该品类）；如需开发，落在 **switchgear/配电类规格缺口**
- **发送时段**：BC **PT（太平洋时区）**，周二–周四当地上午 ≈ **北京时间 00:00–03:00**（夏令时期间）
- **送达配置**：MX = `x-shops.com`；SPF = `…-all`（硬失败）
- **附件建议**：不带名录/供货记录

### ⚠️ 矛盾点与风险提示
- 🔴 **品类对口度低**：官网产品线**无 power transformer / 液浸变** → **本家列为低优先级**；硬推液浸变易显群发。
- 🔴 **CSA 硬伤**：其自述"Trusted CSA-approved brands" → 我方无 CSA 证书 → **信里必须回避"certified"，改技术标准语**。
- ⚠️ **仅角色邮箱**（H6 三步失败）→ **不可当 A 档主送**。
- ⚠️ **多域并存**（evolt.ca / e-volt.ca / evoltsupply.com）→ 收件域须确认。
- ⚠️ **David Hinbest 职务**仅第三方单一来源 → **不据此称 President**。
- ⚠️ **规模/成立年**：官网自述 1998；第三方营收/人数**不引用**。
- ⚠️ **微企话术红线**。

### 信息缺口清单（请勿编造）
- **具名决策人邮箱**：**未获取**
- **采购/Purchasing 岗姓名**：**未获取**
- **是否经营 power transformer / 液浸变**：**未获取（官网未见）**
- **有效收件域**（evolt.ca vs e-volt.ca vs evoltsupply.com）：**未确认**
- **员工数 / 营收**：未获取（**不可引用具体数字**）
- **公司 LinkedIn 页 / 注册主体全称**：未找到
- **常用变压器 kV / kVA**：未获取（首轮问）
- **Jaret Larson / David Hinbest 的任职时长**：未获取

### 一句话画像
BC Burnaby + AB Edmonton 的 **100% 加拿大本土电气批发商（1998 年起）**，产品重心在**照明 / 开关柜 / 配电盘 / 断路器**（e-commerce 通货品）——⚠️ **官网未见 power transformer 产品线，液浸变对口度低，列为低优先级**；⚠️ 仅有角色邮箱 `team@e-volt.ca`，须**点名转交 Jaret Larson**，且其高度看重 **CSA**（我方无 CSA 证书，须改技术标准语）。

### 渠道覆盖清单（L-1、L0–L7）
| 层 | 结果 | 一句话 |
|---|---|---|
| L-1 锁人 | ⚠️ | LinkedIn 现任 Jaret Larson；David Hinbest 仅第三方 |
| L0 官网 | ✅ | home / faq / TradePro 全抓；**角色邮箱 `team@e-volt.ca` / `customer@evoltsupply.com` 明文（B 档）** |
| L1 政府一手 | ❌ | 未查联邦注册库 |
| L2 命名+DNS | ⚠️ | MX=x-shops.com；SPF 硬失败；SMTP 本机不可用；**多域并存** |
| L3 B2B 库 | ⚠️ | Datanyze/Kona 有条目，**仅作旁证** |
| L4 社媒协会 | ⚠️ | 个人页命中；**公司页未找到** |
| L5 黄页同址 | ⚠️ | Burnaby 地址为第三方口径 |
| L6 电话表单 | ✅ | 1-888-739-3555 + 在线 chat（未拨打）|
| L7 付费 | ❌ | 未启用 |

### 同名排除表
| 同名 | 地点 | 排除理由 |
|---|---|---|
| Dongguan Evolt Electronics（中国东莞）| CN | 🔴 **LED 照明/控制系统制造商**，与 BC 批发商**不同主体** |
| e-Volt / E-Volt Electrical（美国等）| US | 不同主体，须按 **Burnaby BC + evolt.ca** 锁定 |
| Evolt（其他行业同名）| — | 须按 **Lite-scape Lighting Inc 旗下 + 电气批发** 锁定 |
