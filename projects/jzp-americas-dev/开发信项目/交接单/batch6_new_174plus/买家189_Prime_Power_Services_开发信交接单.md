# 【买家 189】开发信交接单 — Prime Power Services（TX）

> 采集日期：2026-09-29 / 来源：batch6 名单（CSV 序 16）/ 一句话结论：**⓪ 层已确认是「变电站+高压服务商」（做变压器检修/测试，不是制造商）**，官网页脚自公示具名邮箱 `lvillarreal@primepower.services`（一手源），A 档可主送。

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示(如有)
Prime Power Services（TX/OK，变电站+高压服务商） | Luis Villarreal | 站点公示联系人（职务未确认，疑 owner/principal） | lvillarreal@primepower.services | 已验证（官网页脚一手源） | linkedin.com/in/luis-villarreal-053b2562 | 德州/俄克拉何马变电站建设+变压器检修/测试/场务，20+ 年，24h 应急；服务 GE/ABB/Siemens/Cooper/Howard/Pennsylvania/Waukesha 全系 OEM | 官网 JSON-LD+页脚明文邮箱 + LinkedIn + AllBiz/D&B + Texas SOS | 邮箱域=官网域（同为 primepower.services）；职务未确认；MX 走 Proofpoint
```

## 二、补充信息（扩展段）

### ⓪ 层反身排除（🔴 已完成，结论：不排除）
- **判定**：✅ **服务商/承包商**，**非制造商、非竞品代理、非中国货源通道**。
- **证据原句（官网一手）**：
  - 首页："Prime Power Services **delivers substation construction, transformer repair, testing, and field services** across Texas and Oklahoma."
  - 首页："Trusted Across Every Major OEM — Prime Power Services **installs, tests, and repairs** substation equipment **from the industry's leading manufacturers**."
  - 检修页："Our certified technicians and field engineers handle **diagnostics, oil testing, gasket and bushing replacement, LTC overhauls, and complete rebuilds**…"
  - 检修页 FAQ："What OEMs do you work on? All major manufacturers — GE, ABB, Siemens, Cooper, Howard, Pennsylvania, Waukesha, and more."
- **判据对照**：全文**无** `we manufacture` / `our factory` / `OEM 自称`；出现的是 `install / test / repair / service / rebuild`（安全信号）。**「为制造商的产品提供检修」≠ 制造商**（符合 §二十三 反向陷阱）。
- **NAICS**：General Electrical Contractor / Building Equipment Contractors（AllBiz/D&B）→ 承包商，非 335311/335313。

### 标准字段明细
- 国家+城市：美国 Texas（服务覆盖 TX+OK 全境：Houston/Dallas/Fort Worth/Austin/San Antonio/El Paso/Corpus Christi/Lubbock/Amarillo + OKC/Tulsa）
- 详细地址：Brownsville, TX（Cameron County）。Texas SOS 登记名 **YOUR PRIME POWER SERVICES LLC**，注册办公址 2158 Johnson St, Brownsville, TX 78521；第三方名录另记 5420 Southmost Rd, Brownsville, TX 78521（两址并存，取用时以电话核对）
- 电话：(832) 908-1748（官网一手）
- LinkedIn：个人 linkedin.com/in/luis-villarreal-053b2562（"Substation Services"，现属 Prime Power Services / E4A Solutions）
- 网站：primepower.services（GoDaddy NS）
- 成立日：Texas SOS 注册 2018-09-20（状态 Active/Reinstated，2024-11-04）
- 规模：小微（LLC，无公开员工数/营收）
- 营收：未获取
- NAICS：238210 / 238290（电气承包 / 建筑设备承包，第三方口径）

### 联系人（含 still_here 在职核验）
| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| Luis Villarreal | 站点公示联系人（疑 owner/principal） | 未标注职务（AllBiz 记 "primary contact"） | 未获取 | 中：LinkedIn 现职=Prime Power Services；官网将其列为唯一邮箱 | 中（小微、职务未确认） | linkedin.com/in/luis-villarreal-053b2562 |

### 邮箱分档（A/B/C）
- **A档（具名，主送）**：`lvillarreal@primepower.services` —— **官网一手**（JSON-LD `"email": "lvillarreal@primepower.services"` + 页脚 `<p>Email: lvillarreal@primepower.services</p>`），格式与域名一致，**已验证**。
- **B档（角色/电话兜底）**：(832) 908-1748 电话点名转交 Luis Villarreal。
- H6 声明：不适用（已取得具名邮箱）。
- ⚠️ 未能跑 SMTP 复核：`primepower.services` MX 走 **Proofpoint（mx1/mx2-us1.ppe-hosted.com）**，控制地址 `info@primepower.services` 返回 **550 → 本轮探测作废**（网关拒未授权来源），**不得据此判定任何地址不存在**。A 档依据为**官网一手明文**，不依赖 SMTP。

### 我为什么找他
- 官网把 `lvillarreal@primepower.services` 作为**唯一公开邮箱**挂在页脚/结构化数据里 —— 在一家小微高压服务商，这通常就是老板本人；且他的 LinkedIn 现职正是 Prime Power Services 的 Substation Services。
- 该公司主营 **transformer repair / upgrades & expansions / substation installation**，即**明确会采购/更换变压器**（不是只会"设计"），切入点是"你们的检修/改造项目里，替换机组从哪来"。

### 买家类型 / 需求品类
- 买家类型：🔥 **A 承包商（变电站+高压，含变压器检修/测试）**
- 需求品类（带结论态，**美国客户不谈干变**）：
  - `三相美变（UL E541627，可直供）` — 其检修/改造涉及 pad-mount 替换
  - `三相液浸电力变/主变（UL E541626，可直供，72–121 kV）` — 其"Power transformer repair / LTC overhaul"对应的站级/输电级机组
  - `单相柱上变（认证在办，条件切入）` — 其服务覆盖 small low-voltage pad mounts
  - ⛔ `干变（美国不匹配：无 UL）` — **不推**

### 电压·频率·认证要求
- 频率：60 Hz（美国）→ 产品零改造适配
- 电压：配电 15/25 kV 级 pad-mount；站级/输电级 power transformer（其服务面含 transmission-class）
- 认证：美国要 **UL**（我方 E541627 / E541626 可直供）；对客户表述用 `UL certified, tested to IEEE C57.12 and ANSI standards`，**不写 CSA/SASO/SONCAP**

### 采购信号
- 官网明确承接 **"Transformer upgrades & expansions"** 与 **"New substation construction"** → 直接产生**替换变压器**需求
- 服务全系 OEM（GE/ABB/Siemens/Cooper/Howard/Pennsylvania/Waukesha）→ **懂规格、能直接对话技术参数**，非门外汉
- 20+ 年 + 24h 应急 → 存量设备老化，替换/改造持续发生
- 站点在招 field technicians/engineers → 业务扩张中

### 可利用的钩子（按强度排序）
1. **"你们的 transformer repair / upgrade 项目里，替换机组从哪采购"** —— 最贴合其主业
2. **全系 OEM 检修** → 我方作为**新增替换货源**（非替代其检修能力，是补它的整机缺口）
3. 20+ 年 + TX/OK 全境 + 24h 应急 → 交付可靠性的对话基础（**首封不报交期/价格**）

### 开发信建议
- 收件人：**A 档直发 `lvillarreal@primepower.services`**（官网一手，无需转交）
- 收件人策略：若首封无回应，改走电话 (832) 908-1748 点名 Luis Villarreal
- 抬头/称呼：Luis（具名）
- 发送时段：美国 Central Time（TX）周二–周四上午 = 北京时间约 22–24 点（夏令时）
- 送达配置：MX 走 **Proofpoint（ppe-hosted）**，SPF 含 `~all` 软失败 + 未见 DMARC 强制 → 建议纯文本、单发、避免链接堆叠；发件域三件套（SPF/DKIM/DMARC）须齐
- 附件：不带任何名录/供货记录 PDF；如需资质，仅可附 UL 编号说明

### ⚠️ 矛盾点与风险提示
- 🔴 **主体名不一致**：Texas SOS 登记为 **YOUR PRIME POWER SERVICES LLC**（Tax ID 32068423584），第三方名录写作 "Prime Power Services LLC" —— 疑同一主体（dba），但**未证实**；发信前建议电话核对抬头。
- ⚠️ **职务未确认**：Luis Villarreal 的 title 未见一手标注（官网只给邮箱、AllBiz 只给 "primary contact"）→ 开场避免直接称 "Owner/President"，可用中性称呼。
- ⚠️ **地址两版**：2158 Johnson St vs 5420 Southmost Rd（均 Brownsville）—— 寄样前必须电话确认。
- ⚠️ **同城同名干扰**：Brownsville 有多位 "Luis Villarreal"（另一 LinkedIn 现属 State of Texas）→ 认人时以"公司=Prime Power Services"为准。
- ⚠️ **域名形态**：官网用 `.services`（非 .com），**邮箱域与官网域一致**（同为 primepower.services），非陷阱。

### 信息缺口清单（请勿编造）
- Luis Villarreal 的**准确职务**：未获取（勿写 Owner/President）
- 公司**员工数 / 营收 / 常用变压器容量与品牌**：未获取
- **SMTP 复核**：不可用（Proofpoint 网关，控制地址 550）
- **采购决策是否就在 Luis 本人**：未证实
- **E4A Solutions 与本主体的关系**（LinkedIn 同时挂靠）：未获取

### 一句话画像
Brownsville 起家的 TX/OK 高压服务商——**做变电站建设 + 全系 OEM 变压器检修/改造**，官网把老板邮箱直接挂出来，是"替换机组从哪买"最直接的对话对象。

### 渠道覆盖清单（L-1、L0–L7）
| 层 | 结果 | 一句话 |
|---|---|---|
| L-1 锁人 | ⚠️ | 拿到站点公示联系人 Luis Villarreal（职务未确认） |
| L0 官网 | ✅ | 页脚/JSON-LD 拿到具名邮箱（一手）+ 服务原文 |
| L1 政府一手 | ✅ | Texas SOS 记录（YOUR PRIME POWER SERVICES LLC，Active）|
| L2 命名+DNS | ⚠️ | 邮箱域=官网域；Proofpoint 网关，SMTP 不可用 |
| L3 B2B库 | ⚠️ | AllBiz/D&B/Buzzfile 旁证（仅旁证）|
| L4 社媒协会 | ✅ | LinkedIn 现职核验 |
| L5 黄页同址 | ⚠️ | 两版地址并存 |
| L6 电话表单 | ✅ | (832) 908-1748（未拨打）|
| L7 付费 | ❌ | 未启用 |
