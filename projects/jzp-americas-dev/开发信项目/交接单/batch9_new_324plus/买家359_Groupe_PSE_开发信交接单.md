# 【买家 359】开发信交接单 — Groupe PSE Distribution Électrique

> 采集日期：2026-10-02 ｜ 来源：batch9 名单（groupepse.ca，QC Laval）｜ 一句话结论：**拉瓦尔 2023 年注册的小微（1–5 人）电气用品分销/项目商（官网 "Vente de matériel électrique" + 项目管理 + 配送），非制造/非竞品 —— 可留；但公开渠道**未能锁定任何具名决策人**，官网/JSON-LD 仅挂角色邮箱 `info@groupepse.com`，H6 升级三步全部失败 → ⛔ 拦截（仅角色邮箱 + 无具名决策人），须先电话补人。**
> ⚠️ 本表严格区分「已验证」与「未获取」；未找到的信息一律标注，不做推断填充。
> - 发信资格：⛔ **拦截（H6：仅取得角色邮箱 `info@groupepse.com`，未取得决策人直邮；且无具名决策人可核 still_here）**
> - 邮箱档位：**B（角色邮箱 `info@groupepse.com`）** ｜ 具名决策人：**未找到**

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示
Groupe PSE Distribution Électrique（法人：GROUPE PSE DISTRIBUTION INC. / GROUP PSE DISTRIBUTION INC.）| **未找到** | **未找到** | `info@groupepse.com`（**B 档角色邮箱**）| **已验证（一手明文）**；SMTP 未复核 | Facebook 页 "groupe pse distribution"（官网 footer 链接，未取内容）| 魁省 Laval 的**电气用品分销 + 项目管理 + 技术支持 + 配送**商：官网 "Vente de matériel électrique"（住宅/商业/工业）、"Gestion de Projets"、"Conseils et support technique"、"Livraison rapide à travers tout le Canada"；2023-12 注册，小微（1–5 人）| 官网 home/contact/services 实抓（含 Webador JSON-LD）+ QC REQ（opengovca/b2bhint）+ infobel/cybo/canadanear 检索 | ⚠️ 分销/项目商（非制造）；🔴 **官网域与邮箱域不一致（见双域声明）**；⚠️ 站点为 Webador 建站商托管；⚠️ 未取得具名决策人；正文不引用人数/营收/年份
```

## 二、补充信息（扩展段）

### 标准字段明细
- 国家+城市：**加拿大 Québec**（Laval）
- 详细地址：**3479 Boul. Cartier Ouest, Laval, QC H7V 3T4**（官网 footer + REQ 一致）
- 电话：**514-443-1272**（官网 footer / JSON-LD；⚠️ 同址另有 "PSE Électrique Inc."）
- 邮箱域：🔴 **`groupepse.com`（≠ 官网域 `groupepse.ca`）** —— 见「双域声明」
- 网站：**www.groupepse.ca**（Webador 建站商托管）
- 成立日：**2023-12-04**（REQ 注册；incorporation 2023-12-02）
- 规模：**Micro，员工 "De 1 à 5"**（REQ 一手；infobel 记 2 人）→ **正文不引用具体数字**
- 法人主体：**GROUPE PSE DISTRIBUTION INC.**（REQ NEQ **1179327482**；状态 "Immatriculée"；法律形式 = Société par actions）
- 经营范围（REQ 一手）：**4499 - Autres services relatifs à la construction** + **5749 - Autres types de commerce de machines, matériel et fournitures électriques et électroniques**
- 执照：未获取

### 🔴 双域声明（务必）
| 项 | 域 | 说明 |
|---|---|---|
| **官网域** | `groupepse.ca` | MX = **`mail.webador.com`**（**Webador 建站商邮箱，弱域**）—— ⚠️ **不宜作收件域** |
| **收件域（实际邮箱域）** | **`groupepse.com`** | 官网明文 + JSON-LD 的 `info@groupepse.com`；MX = **`groupepse-com.mail.protection.outlook.com`（Microsoft 365）** → **真实收信域** |
> ⇒ **投递一律用 `groupepse.com`**，**绝不可**发到 `groupepse.ca`（建站商弱域）。

### 联系人（含 still_here 在职核验）
| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| **（未找到具名决策人）** | — | — | — | — | — | — |

> 🔴 **未能锁定任何具名决策人** —— 已穷尽：官网（无团队/关于人页）、REQ/opengovca/b2bhint（**未公开董事/股东**）、infobel/cybo/canadanear（仅地址电话）、LinkedIn（**命中的 "Groupe PSE" 均为法国实体，非本案**）、Facebook（仅页面名，未取内容）。
> 🔴 **H6 声明**：**仅取得角色邮箱 `info@groupepse.com`，未取得决策人直邮；且无具名决策人可作「点名转交」对象** → 按 H6 显式列为风险，**不得直接交付发信**。

### 邮箱分档（A/B/C）
- **B 档（角色邮箱）**：`info@groupepse.com`（官网 Contact 页 + JSON-LD `"email"` 明文，一手）—— ⚠️ 背后无人
- **A 档**：❌ 未取得
- **SMTP 复核**：❌ **未跑**（**无具名候选可测**；且无控制地址样本外的意义）。⚠️ `groupepse.com` MX = M365，如需复核须先有具名候选。
- **H6「升级三步」执行记录**：
  1. **挖职能邮箱**：官网 contact/services 全翻，**仅 `info@groupepse.com`**（无 `purchasing@`/`achats@`/`ventes@`）→ ❌
  2. **从回信反推命名规则**：**无回信样本** → ❌
  3. **推演**：**无第一方命名样本 + 无具名决策人** → 推演地址（如 `pse@` / `info2@`）**一律不得采信**（H2/H4）→ ❌
- **结论**：**仅角色邮箱，未取得决策人直邮，且无具名决策人** → **H6 拦截**。
- **补人路径（交接给人工）**：电话 **514-443-1272** 直接询问负责人姓名/邮箱；或经 Facebook 页 "groupe pse distribution" 私信。

### 我为什么找他
- 官网自述 **"Vente de matériel électrique"**（住宅/商业/工业）+ **"Gestion de Projets"** + **"Livraison rapide à travers tout le Canada"** —— **电气用品分销 + 项目供货**职能明确，属 B 类渠道商。
- 官网自述提供 **"produits sur mesure adaptés aux besoins de chaque client"（定制订单）** 与 **"solutions d'énergie renouvelable / éclairage LED"** → 有**定制/寻源**诉求，可能接受新供应商。
- REQ 经营范围含 **"commerce de machines, matériel et fournitures électriques"**（电气设备与器材贸易）→ 一手印证其**分销**属性。
- ⚠️ 但**无具名决策人**，本单**无法完成个性化开场**（「我为什么找他」只能落到公司层面，**不足以支撑非群发信**）。

### 买家类型 / 需求品类
- 买家类型：**B 电气用品分销 + 项目供货商（住宅/商业/工业，LV）** —— 实测画像 B 类（**小微，采购量未知**）
- 需求品类（带结论态）：
  - `三相液浸配电变 / 三相美变（UL E541627，45–5,000 kVA，可直供）` —— **条件切口**（官网未突出变压器专营，属通用电气分销）
  - `单相柱上变（认证在办 E544629，条件切入）` —— 未定位，**条件试探**
  - `干变（加拿大可谈，有 CSA 项目报告，需人工确认）` —— 须人工确认
  - ⚠️ **未定位其是否经营变压器**（官网为通用电气用品描述）→ 若无法确认，按 `（未定位，需电话确认）` 处理
  - ⚠️ 客户在**加拿大**：可谈液浸类为主
- ⚠️ **E541627/E541626 为正式 CoC；E544629 仅为 ECD 计划函 → 不可称 certified**

### 电压·频率·认证要求
- 电压：未获取 → **首轮问**
- 频率：**60 Hz**（加拿大，产品零改造适配）
- 认证：加拿大市场需 **CSA/IEEE 标准符合性**；我方持 **UL E541626/E541627** 正式 CoC，可写 `built to CSA/IEEE/IEC standards` —— ⛔ 不写 `CSA Certified`

### 采购信号
- 官网 **"commandes personnalisables"（可定制订单）** → 有寻源/定制需求
- 官网 **"Livraison express pour les commandes dépassant 2000 $ CAD"** → 有**小额多频**采购特征（**量级偏小**）
- REQ 经营范围含电气设备**贸易** → 分销职能一手印证
- ⚠️ 公司**2023-12 才注册、1–5 人** → **体量极小、供应链尚未成熟**，也可能是**机会**（新公司无固定供应商）

### 可利用的钩子（按强度排序）
1. **REQ 一手经营范围含「电气设备与器材贸易」** —— 印证分销属性
2. **官网 "commandes personnalisables"（定制订单）** —— 寻源诉求
3. **新公司（2023-12）→ 供应链可能尚未固化** —— 早期进入角度
4. ⚠️ **无具名决策人 → 钩子无法落到个人，仅供电话补人后使用**

### 开发信建议
- **收件人策略**：⛔ **暂不发信** —— **无具名决策人 + 仅角色邮箱**（H6 拦截）。**先电话 514-443-1272 补人**（问负责人姓名 + 直邮），补到具名决策人后再写个性化信。
- 🔴 **双域提醒（务必）**：**官网域 = `groupepse.ca`（MX = Webador 建站商弱域，不可收信）**；**收件域 = `groupepse.com`（MX = Microsoft 365，真实收信）** → 若日后发送，**一律用 `groupepse.com`**
- 🔴 **话术红线**：**不引用人数/营收/年份**；不写 `CSA Certified`；不称 E544629 为 certified；供货记录 PDF 绝不外发
- **发送时段**：QC = **ET（东部时区）**，周二–周四当地上午 ≈ **北京时间 21:00–00:00**（夏令时期间）；⚠️ **法语区** → 正文语言建议法语优先（写信 agent 决定）
- **送达配置**：收件域 MX = **Microsoft 365**；⚠️ 但**当前不发**（H6）
- **附件建议**：不带名录/供货记录

### ⚠️ 矛盾点与风险提示
- 🔴 **H6 拦截**：仅角色邮箱 + **无具名决策人** → 本单**不具备发信资格**，须先电话补人。
- 🔴 **双域陷阱**：官网域 `groupepse.ca` 的 MX 是 **Webador 建站商**（`mail.webador.com`），**不是真实收信域**；真实邮箱域是 **`groupepse.com`（M365）**。⚠️ 若按官网域发信**必退**。
- ⚠️ **Webador 建站模板污染**：官网源码含 `support@webador.com`（**建站商客服邮箱**）→ **必须剔除**，不得当作联系人。
- ⚠️ **同址多实体**：同址 3479 Bd Cartier O 另有 **"PSE Électrique Inc."**（canadanear 记）→ 疑似关联主体，**关系未获取**，不臆测；须按 **NEQ 1179327482 + groupepse.com** 锁定。
- ⚠️ **LinkedIn 同名陷阱**：搜 "Groupe PSE" 命中大量**法国实体**（Rodolphe F.、David Perrelle 等）→ **与本案无关**，不得采信。
- ⚠️ **公司极新（2023-12）+ 极小微（1–5 人）** → 采购量、供应链成熟度均未知；**正文不引用任何数字**。
- ⚠️ **规模/营收未获取** → **正文不引用任何数字**。

### 信息缺口清单（请勿编造）
- **具名决策人姓名 / 职务 / 邮箱**：**未找到**（**本单最大缺口**）
- **是否实际经营变压器**：未获取（官网为通用电气描述）
- **员工数 / 营收**：未获取（**不可引用具体数字**）
- **董事 / 股东**：未获取（REQ 未公开）
- **采购的具体变压器 kV / kVA / 品牌 / 认证要求**：未获取
- **是否已固定中国/海外供应商 / 是否进口**：未获取（**海关数据未查**）
- **与 "PSE Électrique Inc." 的关系**：未获取
- **Facebook 页内容**：未获取（仅链接）

### 一句话画像
魁省 Laval 一家 **2023 年底注册、1–5 人的小微电气用品分销/项目商（Groupe PSE Distribution）**，官网为**通用电气用品 + 项目管理 + 配送**描述，REQ 经营范围含「电气设备与器材贸易」 —— **可留的 B 类分销商**；⚠️ **但公开渠道未能锁定任何具名决策人**，仅挂角色邮箱 `info@groupepse.com`（且**官网域 `groupepse.ca` 为 Webador 弱域、真实收件域是 `groupepse.com`**），H6 升级三步全败 → ⛔ **拦截，须先电话 514-443-1272 补人**。

### 渠道覆盖清单（L-1、L0–L7）
| 层 | 结果 | 一句话 |
|---|---|---|
| L-1 锁人 | ❌ | 官网无团队页；REQ 未公开董事；LinkedIn 命中均为法国同名实体 → **未找到具名决策人** |
| L0 官网 | ✅ | home/contact/services 实抓；获 `info@groupepse.com`（角色）+ 业务描述 + 电话/地址 |
| L1 政府一手 | ✅ | **QC REQ（NEQ 1179327482）**：注册日 2023-12-04、经营范围、员工数 1–5、地址；**未公开董事** |
| L2 命名+DNS | ⚠️ | 官网域 MX=Webador（弱域）；**收件域 groupepse.com MX=M365**；**未跑 SMTP（无具名候选）** |
| L3 B2B 库 | ⚠️ | Crunchbase 有条目，**仅作旁证** |
| L4 社媒协会 | ❌ | LinkedIn 命中均为法国同名实体；Facebook 页仅链接 |
| L5 黄页同址 | ⚠️ | infobel / cybo / canadanear 仅地址电话，**无具名联系人** |
| L6 电话表单 | ✅ | **514-443-1272（补人唯一路径，未拨打）** |
| L7 付费 | ❌ | 未启用 |

### 同名排除表
| 同名 | 地点 | 排除理由 |
|---|---|---|
| **Groupe PSE（法国实体）** | France（Rouen 等）| 🔴 **完全不同的公司**（LinkedIn 命中 Rodolphe F. / David Perrelle 等）→ 与本案无关 |
| **Philippine Stock Exchange (PSE)** | 菲律宾 | 缩写同形，**完全无关** |
| **Puget Sound Energy (PSE)** | 美国 WA | 缩写同形，**完全无关** |
| **PSE Électrique Inc.** | Laval, QC（**同址** 3479 Bd Cartier O）| ⚠️ **疑似关联主体**（同址），关系未获取 → 须按 **NEQ 1179327482 + groupepse.com** 锁定 |
| **Groupe PS Électrique Inc.** | Laval, QC（4410 boul. Sainte-Rose）| ⚠️ 名称近似、**不同地址/不同主体** → 排除 |
| **Jose Collado - grupo pse srl** | Argentina | 名称近似，**完全无关** |
