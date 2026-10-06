# 【买家 215】开发信交接单 — Green Mountain Electric Supply, Inc.（GMES）

> 采集日期：2026-09-29 / 来源：batch6 名单（第 42 行，CSV 州省 VT、备注「佛蒙特电气供应（Colchester VT）」）/ 一句话结论：**佛蒙特 Colchester 的三代家族电气批发商（34 网点、AD 联盟成员，东北区域）**，⓪ 层通过（NAICS 423610 / SIC 5063，官网自称 "wholesale electrical supplies"，无制造自述）；🔴 **CSV 域名有误** —— `greenmountainelectric.com` 返回 401（非公开站），真站与邮箱域均为 **`gmes.com`**；**采购一把手 Adam Cross（Purchasing Manager）被公司官方 LinkedIn 帖两度点名**，第一方明文 `support@gmes.com` 可点名转交；具名邮箱 `adamc@gmes.com` 为规则推演（**待验证**）。

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示(如有)
Green Mountain Electric Supply, Inc. (GMES) | Adam Cross（主送）/ Nate Laber（备选） | Purchasing Manager / President & CEO（Co-Owner） | 推演：adamc@gmes.com（待验证）；B 档：support@gmes.com（官网第一方明文）/ 电话 (802) 338-9336 点名转交 | A 档具名：待验证；B 档角色：已验证（官网明文） | 公司 linkedin.com/company/green-mountain-electric-supply；个人 linkedin.com/in/adam-cross-79b0b2124 | VT Colchester 总部，三代家族（创始人 Earl Laber，孙 Nate Laber 现任 CEO），34 网点，AD（Affiliated Distributors）联盟成员，批发电气/HVAC/照明/数据 | 官网(gmes.com) + 公司 LinkedIn 帖×2 + MDM Top Distributors + LeadIQ/RocketReach + archive.org + DNS | 🔴 官网域为 gmes.com（CSV 给的 greenmountainelectric.com 非公开站）；具名邮箱为规则推演，**不得作主送**；成立年份口径矛盾
```

## 二、补充信息（扩展段）

### 标准字段明细
- 国家+城市：美国 Vermont，Colchester（总部，ET 时区）；服务美国东北部
- 详细地址：356 Rathe Road, Colchester, VT 05446（官网 Contact 页明文）
- 电话：**(802) 338-9336**（官网 Contact 页明文）
- 网站：**gmes.com**（Magento 商城；A=Fastly 151.101.x）；🔴 `greenmountainelectric.com` 返回 **HTTP 401**（需授权，疑内部/客户门户，**非公开站、非邮箱域**）
- **邮箱域**：`gmes.com`（MX = `gmes-com.mail.protection.outlook.com` = **Microsoft 365**；SPF 含 outlook / sendgrid / createsend / billtrust，`-all`）
- 成立日：**口径矛盾** ⚠️ —— 官网 /about-us 记「1970 年改名 Green Mountain Electric Supply」；AllBiz 记 1977；MailBat 记 1953；官网 /locations 写「over 70 years」→ **不作单一采信**
- 规模：**34 网点**（MDM 2026 电气/数据/安全 排名第 33）；51–200 人（MailBat）
- NAICS：**423610**（Electrical Apparatus & Equipment… Merchant Wholesalers，naicslist primary）；SIC 5063
- 社媒：linkedin.com/company/green-mountain-electric-supply（另有 FB/IG/X/YouTube）
- 联盟/集团：**AD（Affiliated Distributors）成员**（公司 LinkedIn 帖）
- 州省核实：**CSV = VT ｜ 实测 = VT（Colchester）** —— 一致
- ⚠️ 同名实体：纽约 Fredonia 另有 "Green Mountain Electric Supply, Inc."（buzzfile 收录）—— 需与 VT 主体区分

### 联系人（含 still_here 在职核验）
| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| **Adam Cross**（主送） | **采购一把手** | Purchasing Manager | 未获取（至少 2023 起） | 高：**公司 LinkedIn 帖 2023-11 与 2024-05 两度点名**；个人 LinkedIn 有 2024 获奖帖 | 低 | linkedin.com/in/adam-cross-79b0b2124 |
| Nate Laber | 老板 / CEO（备选） | President & CEO / Co-Owner | 三代家族（创始人之孙） | 中：MDM 2026 + anglera 专题 + ContactOut | 低 | 未找到 |
| Gregg Laber | 家族二代（背景） | （父辈） | — | 低 | — | 未找到 |
| Kim Herron | 市场经理（非采购） | Marketing Manager | 未获取 | 中：公司 LinkedIn 帖 | 低 | 未找到 |

> 🔴 一家只发 1 人：**主送 Adam Cross（Purchasing Manager）** —— 采购岗优先于 President，且其职务由**公司自身 LinkedIn 帖**两度公开点名（第一方社媒）。
> 备选（同公司不重复发）：Nate Laber（President & CEO）。

### 邮箱分档（A/B/C）
- **A 档（具名）**：**无已验证具名邮箱**。推演 `adamc@gmes.com`（依 LeadIQ「FirstL@gmes.com」/ RocketReach「[first][last_initial]」规则）→ 状态 **待验证**，**不可作主送**。
- **B 档（角色，官网第一方明文）**：**`support@gmes.com`**（官网 /contact 页脚 "Email: support@gmes.com"，经 archive.org 存档页取证）
- **主推路径（B 档）**：电话 **(802) 338-9336** 或 `support@gmes.com`，**点名转交 Adam Cross, Purchasing Manager**；正文首句明确请求转交
- 🔴 **H6 声明**：**具名决策人直邮未取得**（仅规则推演）。已跑「升级三步」：
  1. 挖职能邮箱：官网未见 `Purchasing@` / `Supplier@` 类；仅 `support@gmes.com`
  2. 从真实样本反推命名规则：无回信样本（命名规则来自第三方库）
  3. 免费试推演：`adamc@gmes.com`（**推演，未验证**）
  → 结论：**可交付 B 档 + 一个「待验证」A 档候选**，已如实标注为风险。
- ⚠️ **SMTP 探测未跑**：`gmes.com` MX = Microsoft 365，且**本机源 IP 已被同批 Intermedia/M365 网关以 Spamhaus PBL 拦截**（见买家 214/217）⇒ 按渠道清单预判**不可探测，未浪费轮次**。

### 我为什么找他
- GMES 是 **1970 年起（家族三代）扎根佛蒙特、34 网点、AD 联盟成员**的东北电气批发商，官网自述「electrical distributor serving **contractor, industrial, and municipal** markets」+「wholesale electrical supplies」—— 明确的分销商定位，采购职能是其核心。
- **Adam Cross 的采购职务是公司自己公开的**：GMES 官方 LinkedIn 帖 2023-11 原文「…**Adam Cross – Purchasing Manager**, and Jeremy…」，2024-05 帖「GMES Marketing Manager Kim Herron and **Purchasing Manager Adam Cross** recently participated in AD MAX」→ **第一方社媒两度点名**，是公开可见、可核实的采购负责人。
- 品类对应：官网产品线含 **"Distribution Equipment"**（配电设备）+ 解决方案含 **VMI / Gear Design / EV Chargers** → 有配电设备与项目配套采购场景。

### 买家类型 / 需求品类
- 买家类型：**A 分销商**（批发电气 / HVAC / 照明 / 数据；承包商 + 工业 + 市政三类客户）
- 需求品类（带结论态）：
  - `三相美变（UL E541627，可直供）` —— Distribution Equipment 品类
  - `单相柱上变（认证在办 E544629，条件切入）` —— 市政/农网场景，非首推
  - ⚠️ 美国客户：**不谈干变**（无 UL 不匹配）

### 电压·频率·认证要求
- 电压：未获取
- 频率：**60 Hz**（美国）
- 认证：我方 UL **E541627** 正式 CoC，适配美国

### 采购信号
- **34 网点**（MDM 2026 排名第 33）+ 区域并购扩张（anglera 专题称其「Quiet Roll-Up of the Northeast」）→ 备货与整合需求
- **AD（Affiliated Distributors）联盟成员** + 参加 **AD MAX** 会议 → 有联盟集中采购/供应商对接机制
- 解决方案含 **VMI（供应商管理库存）/ Gear Design / EV Chargers** → 主动的供应链协同与配电设备设计场景
- Magento 电商 + 报价表单（Get a Quote）→ 报价驱动型采购

### 可利用的钩子（按强度排序）
1. **AD 联盟 + AD MAX 参与**（Adam Cross 本人参加）—— 联盟采购/供应商对接的自然入口
2. **34 网点 + 东北区域并购扩张**—— 供应链扩张角度
3. **Distribution Equipment 品类 + Gear Design 解决方案**—— 配电变压器直接对口
4. **三代家族 50 年 + 佛蒙特本土**—— 稳健传承角度

### 开发信建议
- **收件人策略**：**不要**盲发推演地址 `adamc@gmes.com`（**待验证**，触 H2/H4）；走 **B 档** —— 电话 **(802) 338-9336** 或 `support@gmes.com`，**点名转交 Adam Cross, Purchasing Manager**；正文首句明确请求转交
- 🔴 **域名提醒（务必照做）**：邮箱域为 **`gmes.com`**；**绝不可**发到 `greenmountainelectric.com`（该域返回 401，非收信域）
- **开场角度**：从其 **AD 联盟采购体系 + Distribution Equipment 品类**切入（写信 agent 决定措辞）
- **发送时段**：佛蒙特 **ET**，周二–周四当地上午 = **北京时间 21:00–23:00**（夏令时期间）
- **送达配置**：MX = **Microsoft 365**；SPF `-all`；发信域须 SPF/DKIM/DMARC 齐备；纯文本
- **附件建议**：不带名录/供货记录；如需仅附 UL 证书号 + 容量区间

### ⚠️ 矛盾点与风险提示
- 🔴 **CSV 域名错误**：`greenmountainelectric.com` **返回 HTTP 401**（需授权），**非公开站、非邮箱域**；真站与收信域均为 **`gmes.com`** ⇒ 发信务必用 `gmes.com`。
- 🔴 **具名邮箱未验证**：`adamc@gmes.com` 系**命名规则推演**（规则来自第三方库，非第一方样本）⇒ **不得作主送**。
- ⚠️ **成立年份口径矛盾**（官网 1970 改名 / AllBiz 1977 / MailBat 1953 / 官网 "over 70 years"）⇒ **正文勿提成立年份**。
- ⚠️ **同名实体**：纽约 Fredonia 另有同名公司 ⇒ 本单锁定 **VT Colchester 主体**。
- ⚠️ **公司规模数据来自第三方**（51–200 人），**未获一手源印证**，正文勿引用具体数字。
- ⚠️ Adam Cross **任职时长未获取**（仅知至少 2023 起）。

### 信息缺口清单（请勿编造）
- Adam Cross 的**已验证具名邮箱**：**未找到**（仅推演）
- Adam Cross 的**任职时长 / 精确头衔演变**：未获取
- Nate Laber 的**个人页 / 直接联系方式**：未找到
- 公司**准确成立年份**：口径矛盾，未定
- 公司**员工数 / 营收**（一手源口径）：未找到
- 公司**常用变压器容量 / 电压 / 品牌**：未获取
- **VT 州注册主体全称 / 注册日**：未查
- 采购**决策归属**（Adam Cross 是否统管全 34 网点采购）：未明

### 一句话画像
佛蒙特一家三代家族经营、34 网点、AD 联盟成员的东北电气批发商 —— **CSV 给的域名是错的（真站是 gmes.com）**；**采购经理 Adam Cross 被公司官方 LinkedIn 两度点名**，但官网只放表单 + `support@gmes.com`，具名地址只能推演，**主送走第一方角色邮箱 / 电话点名转交**。

### 渠道覆盖清单（L-1、L0–L7）
| 层 | 结果 | 一句话 |
|---|---|---|
| L-1 锁人 | ✅ | 公司 LinkedIn 帖两度点名 Purchasing Manager Adam Cross；MDM 给 President Nate Laber |
| L0 官网 | ✅ | /contact + /about-us + /locations（经 archive.org 取证第一方 `support@gmes.com`） |
| L1 政府一手 | ⚠️ | 未查 VT 州注册库 |
| L2 命名+DNS | ✅ | MX=M365；命名规则来自第三方库（FirstL@）；SMTP 预判失效未跑 |
| L3 B2B 库 | ⚠️ | LeadIQ/RocketReach/ContactOut 给格式与职务（**互证不算印证，H5**） |
| L4 社媒协会 | ✅ | 公司 LinkedIn 帖（第一方点名）+ AD 联盟 |
| L5 黄页同址 | ⚠️ | Colchester VT 地址一致 |
| L6 电话表单 | ✅ | (802) 338-9336 + 官网表单（未拨打/未提交） |
| L7 付费 | ❌ | 未启用 |
