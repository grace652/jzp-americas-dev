# 【买家 366】开发信交接单 — P&F Supply Company（P & F Supply Co.）

> 采集日期：2026-10-02 ｜ 来源：batch9 名单（pfsupply.com，MI Grand Rapids）｜ 一句话结论：**密歇根 Grand Rapids 的家族经营 70+ 年工业电气盈余件分销商（60,000+ sq ft 库存，官网明列 Transformers 为其经营品类之一，主营新件/新盈余件/旧件，含停产与难寻件）—— 典型 B 类盈余件分销商（非制造、非竞品）；官网仅挂角色邮箱 `sales@pfsupply.com`，且该域走 Proofpoint ARS（catch-all，SMTP 永久无效）→ 仅取得角色邮箱，须点名转交具名决策人 Mike Pennell（President）= B 档。**
> ⚠️ 本表严格区分「已验证」与「未获取」；未找到的信息一律标注，不做推断填充。
> - 发信资格：✅ **通过（B 档，须点名转交）**
> - 邮箱档位：**B（角色邮箱 → 点名转交）** —— `sales@pfsupply.com` → 请转交 Mike Pennell（President）
> - ⚠️ **H6 声明**：仅取得角色邮箱 `sales@pfsupply.com`，**未取得决策人直邮**（已跑升级三步，均失败，详见「邮箱分档」段）

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示
P&F Supply Company | Mike Pennell（Michael Pennell）| **President（总裁）** | `sales@pfsupply.com`（**B 档角色邮箱**，**请点名转交 Mike Pennell**）| **已验证（作为角色邮箱，官网第一方明文）**；⚠️ **具名邮箱未找到**（本域 catch-all，SMTP 无法验证）| 个人页 `linkedin.com/in/mike-pennell-55675135`（公司页未找到）| 密歇根 Grand Rapids 的**家族经营 70+ 年工业电气盈余件分销商**；官网自述 *"family owned business for over 70 years. Originally starting as a surplus business… We handle **new, new surplus, and used** industrial electrical supplies"*；*"known for having both current as well as **obsolete and hard to find** items"*；经营品类含 **Electrical Controls / Distribution / Transformers / Busway and Bus Plugs / Circuit Breakers / Fuses / Renewal Parts**；60,000+ sq ft 库存；PEARL 会员 + Grand Rapids 商会会员 | 官网 home/about-us 实抓 + PEARL 会员名录 + LinkedIn + Buzzfile | ⚠️ 盈余件分销商（非制造）；⚠️ 官网为老式 Joomla 模板站、仅挂 `sales@`；正文不引用规模数字
```

## 二、补充信息（扩展段）

### 标准字段明细
- 国家+城市：**美国 Michigan**（Grand Rapids）
- 详细地址：**1135 Broadway Ave NW, Grand Rapids, MI 49504**（官网页脚明文 "1135 Broadway NW / Grand Rapids, MI 49504"；PEARL 名录记 "1135 Broadway Ave NW, Grand Rapids, MI 49504-4215"）
- 电话：**1.616.454.3586** / **1.888.294.3586**（官网明文）；PEARL 名录另记 **(616) 292-5746**
- LinkedIn：个人页 `linkedin.com/in/mike-pennell-55675135`（公司页未找到）
- 网站：**www.pfsupply.com**（老式 Joomla / Shape5 模板站；邮箱域 = 官网域 `pfsupply.com`）
- 成立日：官网自述 **"family owned business for over 70 years"**（**无具体年份 → 正文不写具体年份**）
- 规模：官网称 **60,000+ sq ft 库存**（一手明文）；员工数/营收未获取（**不可引用具体数字**）
- 法人主体：**P & F Supply Company, Inc.**（Buzzfile 记 "also operates under the name P & F SUPPLY COMPANY INC"）
- 执照：未获取
- 会员：**PEARL**（Professional Electrical Apparatus Recyclers League，官网明文 + PEARL 名录 "PAC Dealer Member"）+ **Grand Rapids Area Chamber of Commerce**

### 联系人（含 still_here 在职核验）
| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| **Mike Pennell（Michael Pennell，本次点名转交对象）** | 最高决策（President） | LinkedIn 现任 **PRES at P & F SUPPLY CO**；Buzzfile 记 **Contact: Michael Pennell** | 未获取 | 中：LinkedIn 现任 + Buzzfile 同期 | **中**（LinkedIn 现任 + Buzzfile 一致，但**邮箱未获取**、无近期活跃佐证） | `linkedin.com/in/mike-pennell-55675135` |

> 🔴 **一家只发 1 人**：本单仅识别出 1 位决策人 **Mike Pennell（President）**，作为点名转交对象。

### 邮箱分档（A/B/C）
- **B 档（角色邮箱，已验证）**：✅ `sales@pfsupply.com`（官网首页 / About 页第一方明文，页脚 mailto）
- ❌ **A 档（具名邮箱）：未找到**
  - **升级三步结果（H6 要求）**：
    - ① 挖职能邮箱：翻遍官网（home / about-us / featured / pages 等）**仅得 `sales@`**，**无 purchasing@ / supplier@ 等职能邮箱**
    - ② 从回信反推命名规则：无任何回信样本
    - ③ 推演 + SMTP：**本域 MX = Proofpoint ARS（`pfsupply.com.1.0001.arsmtp.com`）**，实测为 **CATCH-ALL**（随机地址 `zzz_nonexistent_probe_9987@pfsupply.com` 亦返回 250，且回执文本为 ARS 的 *"will relay to a client address"*）⇒ **SMTP 探测对本域永久无效**（渠道清单 §二十一 第 7 类失效网关），推演地址**无法验证**（按 §六 catch-all 规则，**严格禁止使用非第一方来源地址**）
  - ⇒ **结论：仅取得角色邮箱 `sales@pfsupply.com`，未取得决策人直邮。**
- **主送路径**：`sales@pfsupply.com`（**B 档，正文首句请点名转交 Mike Pennell, President**）；电话 **1.616.454.3586** / **1.888.294.3586** 并行跟进
- ⚠️ **H6 风险（已显式声明）**：**仅取得角色邮箱 `sales@pfsupply.com`，未取得决策人直邮** —— 列为本条风险。**禁止**把 `sales@` 混作「正常具名结果」蒙混过关。

### 我为什么找他
- P&F 官网 About 页**明确将 Transformers 列为其经营品类**：*"If you are looking for anything in Electrical Controls, Distribution, **Transformers**, Busway and Bus Plugs, Circuit Breakers, Fuses and Renewal Parts, feel free to contact us"* —— 这是**最直接的品类对口证据**：其本身就是变压器**买/卖**方。
- 其商业模式是 **"new, new surplus, and used"** 盈余件分销（官网 About：*"Originally starting as a surplus business, we have evolved into a company with a reputation for quality and extensive inventory… known for having both current as well as **obsolete and hard to find** items"*）—— **盈余件分销商需要持续补充「新件」货源**，正是我方作为制造商直供的切入点；且其**只做库存买卖/翻新，不做变压器制造** ⇒ **非竞品**。
- **家族经营 70+ 年**（官网明文）+ **PEARL 会员**（正规再认证体系）—— 关系型、长期导向的家族企业，**决策权集中**（President Mike Pennell），适合直接触达最高层。

### 买家类型 / 需求品类
- 买家类型：🔥 **B 工业电气盈余件分销商（家族企业，含变压器，Grand Rapids）** —— B 类贸易商
- 需求品类（带结论态）：
  - `三相液浸配电变 / 三相美变（UL E541627，45–5,000 kVA，可直供）` —— **主切口**（其明列 Transformers）
  - `单相柱上变（认证在办 E544629，条件切入）` —— 条件试探
  - `三相液浸电力变（UL E541626，72–121 kV、750–110,000 kVA，可直供）` —— 视其工业客户，条件试探
  - `干变（美国不匹配：无 UL）` —— ⛔ **钩子不落此项**，正文不提干变
  - ⚠️ 客户在**美国**：仅推液浸类（美变/电力变）
- ⚠️ **E541627/E541626 为正式 CoC；E544629 仅为 ECD 计划函 → 不可称 certified**
- ⚠️ **类目名同形异义提醒**：其官网将 Transformers 与 Busway / Circuit Breakers 并列，属**电力设备**类目（非 LED 驱动）；但**具体 kV/kVA 未列** → **首轮问规格**

### 电压·频率·认证要求
- 电压：未获取（官网未列变压器具体电压等级）→ 首轮问
- 频率：**60 Hz**（美国，产品零改造适配）
- 认证：美国市场需 **UL**；我方持 **UL E541627** / **E541626** 正式 CoC —— ⛔ 不写 `CSA Certified`，不称 E544629 为 certified

### 采购信号
- 官网 About **明列 Transformers 为经营品类** → 明确的变压器购销职能
- 商业模式含 **"new, new surplus, and used"** → **持续的买入/补货职能**
- 自述 **"obsolete and hard to find items"**（停产/难寻件）→ 需多渠道货源
- **PEARL 会员 + Grand Rapids 商会会员**（官网明文）→ 有正规行业准入体系
- **60,000+ sq ft 库存**（官网一手源）→ 规模化库存管理

### 可利用的钩子（按强度排序）
1. **官网 About 明列 `Transformers` 为经营品类**（一手源）—— 最高对口度
2. **"new, new surplus, and used" 盈余件分销模式**（官网一手源）—— 直接对准其补货口
3. **家族经营 70+ 年 + PEARL 会员**（官网一手源）—— 关系型长期伙伴角度
4. **Grand Rapids 本地仓储（1135 Broadway Ave NW）** —— 区域交付角度

### 开发信建议
- **收件人策略**：⚠️ **B 档** —— 主送 `sales@pfsupply.com`，**正文首句请点名转交 Mike Pennell（President）**；电话 **1.616.454.3586** 并行跟进
- 🔴 **域名提醒**：邮箱域 = 官网域 = **`pfsupply.com`**；⚠️ **绝不可**误写为 `pf-supply.com` / `pandfsupply.com` 等（未验证）
- 🔴 **话术红线**：**不引用员工数/营收/成立年份**；不写 `CSA Certified`；不称 E544629 为 certified；**对美国客户不谈干变**；供货记录 PDF 绝不外发
- **开场角度**：从其**官网 About 明列的 Transformers 经营品类 + 盈余件分销模式** 切入（写信 agent 决定措辞）
- **发送时段**：MI = **ET（东部时区）**，周二–周四当地上午 ≈ **北京时间 21:00–00:00**（夏令时期间）
- **送达配置**：MX = **Proofpoint ARS**（`*.arsmtp.com`）；⚠️ 该网关**不验证收件人**（catch-all 转发）→ 投递本身通常不退回，但**无法预验证**；用正规 ESP 投递，首封注意退信/送达监控
- **附件建议**：不带名录/供货记录；如需仅附 UL 证书号 + 容量区间

### ⚠️ 矛盾点与风险提示
- 🔴 **H6 未达标（核心风险）**：**仅取得角色邮箱 `sales@pfsupply.com`，未取得决策人直邮**。已跑完升级三步（职能邮箱 / 反推规则 / 推演+SMTP），**均失败**（本域为 Proofpoint ARS catch-all，SMTP 无效）。**禁止**把 `sales@` 当作具名结果。
- 🔴 **本域为 Proofpoint ARS「转发式 250」网关**：MX = `pfsupply.com.1.0001.arsmtp.com`，随机地址亦 250（回执含 *"will relay"*）⇒ **SMTP 探测对本域永久无效**（§二十一）。按 §六 规则，**严禁使用任何非第一方来源的地址**。
- ⚠️ **官网为老式 Joomla 模板站**：页面含模板示例模块（*"This is a sample module published to the sidebar_top position…"*）→ **非真实业务内容，不得引用**；页脚 "Designed by Shape5.com Joomla Templates" 为模板商，**非公司联系人**。
- ⚠️ **电话口径不一**：官网 `1.616.454.3586` vs PEARL 名录 `(616) 292-5746` → 拨打时以官网为准。
- ⚠️ **成立年份无具体值**（官网仅 "over 70 years"）→ **正文不写具体年份**。
- ⚠️ **规模/营收未获取** → **正文不引用任何数字**（含 60,000 sq ft）。
- ⚠️ **Mike Pennell 在职性「中」**：LinkedIn 现任 + Buzzfile 一致，但无近期活跃佐证 ⇒ **点名转交前建议电话确认**。

### 信息缺口清单（请勿编造）
- **Mike Pennell 的具名邮箱**：**未找到**（本域 catch-all，无法验证）
- **公司成立具体年份 / 员工数 / 营收**：未获取（**不可引用具体数字**）
- **法人注册号 / 注册日（MI LARA）**：未获取（LARA 站被 Cloudflare 拦截，未取得）
- **采购的具体变压器 kV / kVA / 品牌 / 认证要求**：首轮问
- **是否已固定中国/海外供应商 / 是否进口**：未获取（**海关数据未查**）
- **除 Mike Pennell 外的其他联系人 / 采购岗具名**：未找到
- **公司 LinkedIn 页**：未找到

### 一句话画像
密歇根 Grand Rapids 一家 **家族经营 70+ 年的工业电气盈余件分销商**（60,000+ sq ft 库存，官网**明列 Transformers 为经营品类**，主营新件/新盈余件/旧件，含停产难寻件）—— **典型 B 类盈余件分销商（非制造/非竞品）**；⚠️ 官网**仅挂角色邮箱 `sales@pfsupply.com` 且本域为 Proofpoint ARS catch-all**，**未取得决策人直邮** → **B 档，须点名转交 Mike Pennell（President）**。

### 渠道覆盖清单（L-1、L0–L7）
| 层 | 结果 | 一句话 |
|---|---|---|
| L-1 锁人 | ✅ | LinkedIn 命中 **Mike Pennell（PRES at P & F SUPPLY CO）**；Buzzfile 记 Michael Pennell |
| L0 官网 | ⚠️ | home/about-us 全抓，**仅得 `sales@`**（角色邮箱）；模板示例内容已剔除 |
| L1 政府一手 | ❌ | **MI LARA** 被 Cloudflare 拦截（未取得）；无 CAGE 记录 |
| L2 命名+DNS | ⚠️ | MX=**Proofpoint ARS**；**实测 catch-all（ARS 转发式 250）⇒ SMTP 永久无效** |
| L3 B2B 库 | ⚠️ | Buzzfile / D&B / RocketReach 有条目，**仅作旁证**（未采信其邮箱）|
| L4 社媒协会 | ✅ | **PEARL 会员名录**（PAC Dealer Member，含地址电话）+ Grand Rapids 商会会员 |
| L5 黄页同址 | ⚠️ | 未深挖 |
| L6 电话表单 | ✅ | 1.616.454.3586 / 1.888.294.3586（未拨打）|
| L7 付费 | ❌ | 未启用 |

### 同名排除表
| 同名 | 地点 | 排除理由 |
|---|---|---|
| **F&P Supply Company**（CAGE/DUNS 008452183）| — | 名称形近但**不同主体**（cage.report 同名搜索命中，非本单目标）|
| **F & P Supply** 等其他 "Supply" 类公司 | — | 须按 **1135 Broadway Ave NW, Grand Rapids MI + pfsupply.com + President Mike Pennell** 锁定主体 |
| **P&F Supply Company Inc**（Buzzfile 别名档案 `no:16307478`）| Grand Rapids, MI | **同主体**（Buzzfile 多档案），非独立客户 |
| **Mike Pennell / Michael Pennell**（其他同名个人）| — | 须按 **P & F SUPPLY CO + President + Grand Rapids MI** 锁定 |
