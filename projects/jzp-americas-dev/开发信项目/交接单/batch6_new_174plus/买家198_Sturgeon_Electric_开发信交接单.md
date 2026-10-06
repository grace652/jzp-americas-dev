# 【买家 198】开发信交接单 — Sturgeon Electric Company, Inc.

> 采集日期：2026-09-29 / 来源：batch6 名单（第 25 行，CSV 州省 CO、备注「SPF -all、无 MX」）/ 一句话结论：**科罗拉多 Henderson 的百年西部基础设施承包商（1912 年创立，MYR Group 旗下 15 家子公司之一）**，官网公开完整 Leadership；**邮箱域确认在母集团 `myrgroup.com`（该域为 catch-all，具名邮箱不可验证）→ B 档：角色邮箱/表单点名转交 President T&D（Eric Lauriha）**。

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示(如有)
Sturgeon Electric Company, Inc. | Eric Lauriha | President, Sturgeon Electric（Transmission & Distribution）/ Group VP, T&D West, MYR Group | 未找到具名直邮（域 catch-all）；B 档：info-sturgeon@myrgroup.com / 官网表单 / 电话 303.286.8000 点名转交 | 未找到（A 档）；B 档角色邮箱为官网明文 | 公司页 linkedin.com/company/sturgeon-electric-company（未直取）；个人页未确认 | CO Henderson，1912 创立，MYR Group（Nasdaq: MYRG）子公司，西部输电/工商业/新能源电气施工，百年老牌 | 官网 /leadership/ + /about/ + MYR Group /contact/ + /contact/vendors/ + DNS | 🔴 官网域无 MX（勿发）；邮箱域=myrgroup.com 且为 catch-all（禁推演具名）
```

## 二、补充信息（扩展段）

### 标准字段明细
- 国家+城市：美国 Colorado，Henderson（丹佛都会区）
- 详细地址：Henderson, CO 80640（12150 E 112th Ave，MYR Group 联系页列 Sturgeon Electric 地址）；母集团总部 12121 Grant St, Suite #610, Thornton, CO 80241
- 电话：**303.286.8000**（MYR Group 总机，Sturgeon Electric 共用）；分支：Phoenix, AZ — T&D 480.940.1986 / C&I 480.894.0221
- LinkedIn：公司页 linkedin.com/company/sturgeon-electric-company（检索命中，未直取）；**个人页未确认**
- 网站：sturgeonelectric.com（**A=162.223.226.36，NS=dnsmadeeasy，无 MX，SPF `-all`**）
- **真实邮箱域**：`myrgroup.com`（MX=Proofpoint `mxa-00498d01.gslb.pphosted.com`；A=162.223.226.36，与官网域**同 IP** → 同属 MYR Group 基础设施）
- 成立日：**1912**（官网 "Since 1912"）
- 规模：未找到（母集团 MYR Group 为 Nasdaq 上市公司 MYRG，旗下 **15 家**电气承包商）
- 营收：未找到（可用母集团财报，但子公司口径未获取）
- 母集团：**MYR Group Inc.**（Nasdaq: MYRG），官网 myrgroup.com
- 州省核实：**CSV = CO ｜ 实测 = CO（Henderson）** —— **一致，无需修正**

### 联系人（含 still_here 在职核验）
| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| Eric Lauriha | **T&D 一把手（本次主送）** | President, Sturgeon Electric（T&D）/ Group VP, T&D West, MYR Group | 2013 起任 district manager，2022 起 regional VP，2023 起 group VP，**2025 起 President**（累计 17+ 年） | 中：官网 /leadership/ 在列（2026-09 抓取） | 低 | 未找到 |
| Don Egan | C&I 一把手 / 母集团 COO（备选） | President, Sturgeon Electric（C&I）/ SVP & COO, C&I, MYR Group | 1991 入职 Sturgeon，2020 起 Sturgeon C&I President，2023 起 MYR SVP&COO | 中：官网 /leadership/ 在列 | 低 | 未找到 |
| Matt Patterson | RVP, T&D（Phoenix/Denver 线运营，备选） | Regional Vice President, T&D | 2006 入职，2022 district manager，2024-12 起 RVP | 中：官网在列 | 低 | 未找到 |

> 🔴 一家只发 1 人：**主送 Eric Lauriha（President, Sturgeon Electric T&D）**——输电/配电业务与变压器品类最对口，且为分部一把手。
> 备选（同公司不重复发）：Don Egan（C&I President / MYR COO）、Matt Patterson（RVP T&D）。

### 邮箱分档（A/B/C）
- **A 档（具名）**：**未找到** —— 官网 Leadership 页只列姓名+职务，**无具名邮箱**
- **B 档（角色，官网明文，first-party）**：`info-sturgeon@myrgroup.com`（MYR Group 官方 Contact 页明列，标注为 "Sturgeon Electric locations"）
- **主推路径（B 档）**：官网 Contact 表单（myrgroup.com/contact/）/ 电话 **303.286.8000** / **Vendor Program 表单**（myrgroup.com/contact/vendors/）→ 点名转交 **Eric Lauriha, President, Sturgeon Electric T&D**
- 🔴 **H6 声明**：**仅取得角色邮箱（且属集团层级），未取得决策人直邮** —— 已跑「升级三步」：
  1. 挖职能邮箱：官网仅见 `info-sturgeon@myrgroup.com` 与 `info@myrgroup.com`，**未见** `Purchasing@`/`Supplier@` 类
  2. 从真实回信反推命名规则：无回信样本
  3. 免费试推演：**域 `myrgroup.com` 为 catch-all，推演地址无法验证 → 依 §六 严格禁止使用非第一方来源地址，停止推演**
  → 结论：**本单只能走 B 档**，已如实标注为风险。
- 🔴 **catch-all 判定证据**：控制地址 `info-sturgeon@myrgroup.com` = 250（官网明文，真实）｜随机地址 `zzz_nonexistent_probe_9987@myrgroup.com` = **250** ⇒ **该域 catch-all，SMTP 探测永久无效**。LeadIQ/NeverBounce 给出的 `FLast@myrgroup.com` 格式（如 elauriha@）**属 B2B 库且 catch-all 下无法证伪** ⇒ **不得作主送**（H2/H5/H6）。

### 我为什么找他
- Sturgeon 官网 **/leadership/ 页把 T&D 与 C&I 两条业务线的一把手全公开**，其中 **Eric Lauriha 是 Transmission & Distribution 线的 President**——一家自 1912 年起做「**electrical transmission**」、且隶属全美最大输电承包商集团之一的公司，**输电/配电线一把手**正是变压器这类设备采购的**决策入口**；他的履历还显示其**从 Arizona district 做起、把该区做成 Sturgeon T&D 西部最大区之一**，说明是业务实权人物而非挂名。
- 业务与其职责直接对应：官网自述 "one of the largest and most complex **electrical transmission** … projects"——**输电 = 主变/变电站变的主场**。

### 买家类型 / 需求品类
- 买家类型：🔥🔥 **B 电气承包商（西部基础设施，输电 + 工商业 + 新能源，百年、集团型）**——实测画像 B 型主力（集团采购层）
- 需求品类（带结论态）：
  - `主变 / 变电站变（UL E541626，750–110,000 kVA，可直供）` —— 其输电/变电站业务最对口，项目制主谈
  - `三相美变（UL E541627，45–5,000 kVA，可直供）` —— 配电/工商业场景
  - `单相柱上变（认证在办 E544629，条件切入）` —— 配网线路，非首推
  - ⚠️ 美国客户：**不谈干变**（无 UL 不匹配）

### 电压·频率·认证要求
- 电压：未获取（输电业务典型 115/230/345 kV 级，**未证实**）
- 频率：**60 Hz**（美国）
- 认证：我方 UL **E541626（750–110,000 kVA）** 与 **E541627** 正式 CoC，适配美国

### 采购信号
- 官网设 **Vendor Program（供应商多元化计划）** + 母集团 myrgroup.com/contact/vendors/ 有 **"Apply Now" 供应商申请表单** → **明确、公开的供应商准入入口**（强信号）
- 业务含 "**electrical transmission**"、"renewable energy"（如 Raptor Ridge Solar Field）、"commercial & industrial" → 多场景用变
- **母集团 Nasdaq 上市（MYRG）**、旗下 15 家承包商、集中采购/车队资源 → 集团级采购体系
- 百年老牌（1912）+ 西部多州运营 → 稳定项目流

### 可利用的钩子（按强度排序）
1. **Vendor Program / 供应商准入表单**（官网公开入口）—— 最合规、最自然的切入路径
2. **输电（transmission）业务 + 变电站项目**（如 Utah State Penitentiary 输电项目）—— 主变强相关
3. **1912 年创立、百年西部基础设施**—— 稳健传承角度
4. **MYR Group（Nasdaq: MYRG）旗下、15 家承包商协同**—— 集团背书
5. **新能源转型**（官网 "clean energy transformation"）—— 时效性角度

### 开发信建议
- **收件人策略**：**不要**盲发 `elauriha@myrgroup.com` 一类具名地址（catch-all，无法验证，触 H2/H6）；走 **B 档**——优先 **MYR Group Vendor Program 表单**（myrgroup.com/contact/vendors/，最契合供应商身份），或 `info-sturgeon@myrgroup.com` / 电话 303.286.8000，**点名转交 Eric Lauriha, President, Sturgeon Electric T&D**；正文首句明确请求转交
- 🔴 **域名提醒（务必照做）**：**绝不可**把收件地址写成 `@sturgeonelectric.com`（该域**无 MX**，必退信）；邮箱域为 **`myrgroup.com`**
- **开场角度**：从其 **输电/变电站业务 + 公开 Vendor Program** 切入（写信 agent 决定措辞）
- **发送时段**：科罗拉多 **MT**，周二–周四当地上午 = **北京时间 22:00–01:00**（夏令时期间）；美山区夏令时 3–11 月
- **送达配置**：MX = **Proofpoint（pphosted）**，SPF `-all`（含多段 ip4 与 pphosted include）；发信域须 SPF/DKIM/DMARC 齐备；**Proofpoint 可能对未授权来源不透露目录，勿反复探测**
- **附件建议**：不带名录/供货记录；如需仅附 UL 证书号 + 容量区间

### ⚠️ 矛盾点与风险提示
- 🔴 **官网域无 MX（硬故障）**：`sturgeonelectric.com` **无 MX 且 SPF `-all`** ⇒ 发到官网域**必退**；真实邮箱域为 `myrgroup.com`（与官网域同 IP，属同集团基础设施）。
- 🔴 **邮箱域 catch-all**：`myrgroup.com` 对任意地址返回 250 ⇒ 具名邮箱**不可验证**；`FLast@myrgroup.com` 类格式**严禁作主送**。
- ⚠️ **集团采购层**：Sturgeon 为 MYR Group 子公司，**采购权可能在集团/区域层**（MYR 设 COO、Group VP 等跨公司统筹）→ 按「集团采购敲门型 / 长期培育」处理，冷邮件直接开单概率低于独立承包商。
- ⚠. **公司名易混**：与 Sturgeon（姓氏）/ 其他 "Sturgeon" 实体注意区分；本单为 **Sturgeon Electric Company, Inc.（MYR Group 子公司，CO Henderson）**。
- ⚠️ 官网 Leadership 页 **Josh Barber（VP, Colorado C&I）标 "COMING SOON!"** → 该页在更新中，个别条目可能变动。
- ⚠️ 个人 LinkedIn 直链未取 → Eric Lauriha 离职风险评为「低」但**非零**（依据仅官网在列）。

### 信息缺口清单（请勿编造）
- Eric Lauriha 的**具名邮箱**：未找到（域 catch-all，无法验证）
- 个人 **LinkedIn 直链 / 最近活跃**：未获取
- Sturgeon 的**员工数 / 营收**（子公司口径）：未找到
- 公司**常用变压器容量 / 电压 / 品牌**：未获取
- **采购决策归属**（Sturgeon 分部 vs MYR 集团）：未明（需电话/Vendor 流程确认）
- **CO 州注册主体全称 / 注册日**（CO SOS）：未查
- **邮箱域与官网域不一致**（同 IP 但域不同）的正式说明：未获取

### 一句话画像
科罗拉多一家 1912 年创立、隶属 Nasdaq 上市集团 MYR Group 的西部输电承包商——官网域根本收不了信，真正的邮箱域在母集团 `myrgroup.com`，且该域 catch-all；**对口度极高（输电/变电站一把手已锁定），但具名直邮不可验证，只能走集团 Vendor Program / 角色邮箱点名转交**。

### 渠道覆盖清单（L-1、L0–L7）
| 层 | 结果 | 一句话 |
|---|---|---|
| L-1 锁人 | ✅ | 官网 /leadership/ 取 T&D 与 C&I 两条线一把手（Eric Lauriha / Don Egan） |
| L0 官网 | ✅ | /leadership/ + /about/ + /contact/vendor-program/ 全取；无具名邮箱 |
| L1 政府一手 | ⚠️ | 未查 CO SOS；MYR Group 为 Nasdaq 上市公司（SEC 文件可查，未取） |
| L2 命名+DNS | ✅ | 官网域无 MX；邮箱域 myrgroup.com 有 MX 但 catch-all → 探测无效，禁止推演 |
| L3 B2B 库 | ⚠️ | LeadIQ/NeverBounce 给 FLast 格式（互证不算，H5；catch-all 下不可证伪） |
| L4 社媒协会 | ⚠️ | 公司 LinkedIn 页命中未直取；个人页未确认 |
| L5 黄页同址 | ⚠️ | Henderson CO 地址与母集团联系页一致 |
| L6 电话表单 | ✅ | 303.286.8000 + 官网/Vendor 表单（未拨打/未提交） |
| L7 付费 | ❌ | 未启用 |
