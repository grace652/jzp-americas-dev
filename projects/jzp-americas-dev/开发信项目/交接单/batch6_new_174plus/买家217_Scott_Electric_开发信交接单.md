# 【买家 217】开发信交接单 — Scott Electric Company

> 采集日期：2026-09-29 / 来源：batch6 名单（第 44 行，CSV 州省 PA、备注「宾州电气供应（Greensburg PA）」）/ 一句话结论：**宾州 Greensburg 的 1946 年创立、全美最大独立电气分销商之一**（分支覆盖 PA/NY/MD）；⓪ 层通过（NAICS **423610** 批发，官网/Chamber 自述 "wholesale electrical distributor"，无制造自述）；🔴 **CSV 域名有误** —— `scottelectric.com` 实为**旧金山电气承包商 Edward W. Scott Electric Co.**（另一家），真站与邮箱域均为 **`scottelectricusa.com`**（对非美 IP 地域封锁）；**决策人锁定 President Samuel Z. Scott（PA 州务卿注册一手源确认）**，邮箱 `sscott@scottelectricusa.com`（第三方单一来源，**待验证**）；公司另有采购岗（Ryan Kelly / William D.）但**无邮箱**。

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示(如有)
Scott Electric Company | Samuel Z. Scott（主送） | President / Secretary / Treasurer | sscott@scottelectricusa.com（AllBiz/PeopleSmart 单一来源，未经第二方印证） | 待验证（单一来源；命名规则 {f}{last}@ 与 sscott@ 自洽） | 公司 linkedin.com/company/scott-electric-company；个人页未确认 | PA Greensburg，1946 创立，全美最大独立电气分销商之一，分支 PA/NY/MD，24h 应急 panel shop，SAM.gov 政府供应商 | PA 州务卿注册(pennsylvaniadb 镜像) + AllBiz + Westmoreland Chamber + LinkedIn + govtribe + DNS | 🔴 CSV 域名 scottelectric.com 非本司；真站 scottelectricusa.com（地域封锁）；邮箱单一来源，未第二方印证；SMTP 探测被源 IP 拦截
```

## 二、补充信息（扩展段）

### 标准字段明细
- 国家+城市：美国 Pennsylvania，Greensburg（总部，ET 时区）；分支覆盖 **PA / NY / MD**
- 详细地址：1000 S Main St, Greensburg, PA 15601（PA 州注册 Principal Address + 官网一致）
- 电话：(800) 442-8045 / (724) 837-9530 / (724) 261-5159（Westmoreland Chamber）；传真 (724) 834-6380
- 网站：**scottelectricusa.com**（🔴 对非美 IP 返回 "Access Denied … outside our supported regions"）；🔴 **`scottelectric.com` = Edward W. Scott Electric Co.（旧金山电气承包商，另一实体）**
- **邮箱域**：`scottelectricusa.com`（MX = `east/west.smtp.mx.exch070.serverdata.net` = **Intermedia**；SPF 含 intermedia / constantcontact / sendgrid，`~all`）
- 成立日：**口径矛盾** ⚠️ —— 官网/AllBiz 业务描述记 **1946**；PA 州务卿**公司注册**日 **1957-08-12**（公司号 321218）→ 建议取「1946 年创立」表述
- 规模：241 人（AllBiz）/ 178（ContactOut）/ 229（LeadIQ）；营收 $25–75M（AllBiz）；Seamless 另估 501–1,000 人 / $500M（**明显偏离，不采信**）
- NAICS：**423610**（primary，naicslist / siccode）；SIC 5063（AllBiz 另标 238210 承包商码，非制造）
- 州注册：**Scott Electric Company，PA 公司号 321218，状态 Active**，Incorporated 1957-08-12（一手源）
- 社媒：linkedin.com/company/scott-electric-company
- 州省核实：**CSV = PA ｜ 实测 = PA（Greensburg）** —— 一致

### 联系人（含 still_here 在职核验）
| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| **Samuel Z. Scott**（主送） | 老板 / 家族主事人 | President / Secretary / Treasurer | 未获取（家族企业） | 高：**PA 州务卿注册在任（Active）+ AllBiz 主联系人** | 低 | 未确认 |
| Joseph Z Diastolfo | 高管（备选） | Vice President | 未获取 | 中：PA 州务卿注册在列 | 低 | 未找到 |
| Ryan Kelly | 采购（职能更对口） | Purchasing | 未获取 | 中：LinkedIn 现职 | 低 | linkedin.com/in/ryan-kelly-14500214a |
| William D. | 采购（姓名缩写） | Purchasing Agent | 未获取 | 中：LinkedIn 现职 | 低 | linkedin.com/in/william-d-46754a145 |
| Cris Stout | 销售（非采购） | Executive Sales Manager | 未获取 | 中：Westmoreland Chamber 名录 | 低 | 未找到 |
| Tracey O'Baker | 人事（非采购） | Senior HR Generalist | 未获取 | 中：Westmoreland Chamber 名录 | 低 | 未找到 |

> 🔴 一家只发 1 人：**主送 Samuel Z. Scott（President）**。
> **理由与取舍（如实记录）**：按优先级「采购岗 > 老板」，Ryan Kelly / William D. 的**职能更对口**，但二人**均无任何可获取邮箱**（且 William D. 姓名被 LinkedIn 缩写）；而 Samuel Z. Scott 是**PA 州务卿注册一手源确认**的家族主事人（President/Secretary/Treasurer 三职一身），且有唯一可得的邮箱。**本单以「可触达性」压过「职能对口度」**，故选 President，并把采购岗列为备选。
> 备选（同公司不重复发）：Joseph Z Diastolfo（VP）、Ryan Kelly / William D.（Purchasing）。

### 邮箱分档（A/B/C）
- **A 档（具名）**：`sscott@scottelectricusa.com`（AllBiz，来源 PeopleSmart）—— **单一第三方来源，未经第二方印证** ⇒ 状态 **待验证**，**不可直接作主送**（H3/H4）。
  - 自洽性：命名规则 **`{f}{last}@scottelectricusa.com`**（`sscott@` = s + scott），与域名格式一致。
- **B 档（角色，第三方来源）**：`support@scottelectricusa.com`（AllBiz 角色邮箱）—— 同属单一来源，**待验证**。
- **主推路径**：电话 **(800) 442-8045** / **(724) 837-9530**，**点名转交 Samuel Z. Scott, President**；或官网 `scottelectricusa.com/contactus` 分支联系人（需美 IP）
- 🔴 **H6 声明**：**未取得经第二方印证的具名直邮**。已跑「升级三步」：
  1. 挖职能邮箱：官网 `contactus` 页仅给分支导航 + 电话 800-442-8045，**无第一方邮箱明文**（且站点对非美 IP 地域封锁）
  2. 从真实样本反推命名规则：**无第一方样本**；`sscott@` 来自第三方库，且与其格式自洽
  3. 免费试推演：未额外推演（避免 H2 风险）
  → 结论：**`sscott@` 为「待验证」候选（单一来源）**，已如实标注为风险；**主送建议电话点名转交**。
- 🔴 **SMTP 探测结论（未采信）**：对 `scottelectricusa.com`（Intermedia / serverdata）跑控制地址协议，**控制地址 `support@` 与随机地址均返回 `554 5.7.1 … blocked using pbl.spamhaus.org`（源 IP 223.64.3.115）** ⇒ 属**源 IP 级拦截**，**本轮探测整体作废**，不据此判任何地址存在/不存在。

### 我为什么找他
- Scott Electric 是 **1946 年创立、全美最大独立电气分销商之一**（分支覆盖 PA/NY/MD，官网自述「Meeting the needs of electrical contractors since 1946」），**仍是家族企业**——PA 州务卿注册显示 **Samuel Z. Scott 一人身兼 President / Secretary / Treasurer**，Joseph Z Diastolfo 任 VP（**一手政府源**，非第三方库）。
- 对**家族型独立分销商**而言，**新供应商准入常由家族主事人拍板**；且本公司有明确采购职能（在招 **Buyer**：SimplyHired/Glassdoor「prepare purchase orders, transfer material between warehouses, and be responsible for finding **new items to add**」）→ 新供应商对接是其采购部日常工作。
- 品类对应：官网自述「best known for providing construction projects with **lighting, gear, and electrical supplies**」+ **24 小时应急 panel shop** → 有 **gear（开关/配电）与项目配套**采购场景。

### 买家类型 / 需求品类
- 买家类型：**A 分销商**（批发电气分销；服务电气承包商、政府机构、市政、零售；含零售照明 showroom + 24h panel shop + 自有车队次日达）
- 需求品类（带结论态）：
  - `三相美变（UL E541627，可直供）` —— gear 品类 + 项目配套
  - `单相柱上变（认证在办 E544629，条件切入）` —— 非首推
  - ⚠️ 美国客户：**不谈干变**（无 UL 不匹配）

### 电压·频率·认证要求
- 电压：未获取
- 频率：**60 Hz**（美国）
- 认证：我方 UL **E541627** 正式 CoC，适配美国

### 采购信号
- **在招 Buyer**（SimplyHired / Glassdoor：「prepare purchase orders, transfer material between warehouses, and be responsible for finding **new items to add**」）→ **主动扩品/找新供应商**（强信号）
- 已有 **Purchasing 团队**（LinkedIn 见 Ryan Kelly / William D.）→ 采购职能常设
- **24 小时应急 panel shop** + 自有车队次日达 → 有备货与项目响应能力
- **SAM.gov 政府供应商**（govtribe：「Scott Electric Co is an electrical distributor and supply store」）+ 服务政府/市政 → 政府采购资质

### 可利用的钩子（按强度排序）
1. **在招 Buyer + 「finding new items to add」**（扩品信号）—— 最自然的供应商切入角度
2. **gear 品类 + 24h panel shop**（官网明文）—— 与配电变压器对口
3. **1946 年创立、近 80 年家族独立**—— 稳健传承角度
4. **PA/NY/MD 三州分支 + 服务政府/市政**—— 区域覆盖角度

### 开发信建议
- **收件人策略**：`sscott@scottelectricusa.com` 为**单一来源待验证** ⇒ 建议**电话 (800) 442-8045 / (724) 837-9530 点名转交 Samuel Z. Scott, President**；若走邮箱，正文首句明确请求转交，并**先做小批投递观察退信**（H3/H4）
- 🔴 **域名提醒（务必照做）**：邮箱域为 **`scottelectricusa.com`**；**绝不可**发到 `scottelectric.com`（那是**旧金山 Edward W. Scott Electric Co.**，另一家公司）
- **开场角度**：从其**在招 Buyer / 扩品信号 + gear 品类**切入（写信 agent 决定措辞）
- **发送时段**：宾州 **ET**，周二–周四当地上午 = **北京时间 21:00–23:00**（夏令时期间）
- **送达配置**：MX = **Intermedia（serverdata.net）**；SPF `~all`（软失败）；发信域须 SPF/DKIM/DMARC 齐备；纯文本
- **附件建议**：不带名录/供货记录；如需仅附 UL 证书号 + 容量区间

### ⚠️ 矛盾点与风险提示
- 🔴 **CSV 域名错误（严重）**：`scottelectric.com` **= Edward W. Scott Electric Co.（旧金山电气承包商）**，与本司**完全无关** ⇒ 真站/收信域均为 **`scottelectricusa.com`**，发信务必核对。
- 🔴 **站点地域封锁**：`scottelectricusa.com` 对**非美 IP 返回 Access Denied** ⇒ 无法抓第一方邮箱，也**不宜在正文引用官网细节**。
- 🔴 **邮箱单一来源未印证**：`sscott@scottelectricusa.com` 来自 AllBiz/PeopleSmart（**第三方**，且 AllBiz 页最后更新 2024-08）⇒ **待验证**，作主送有退信风险。
- 🔴 **SMTP 探测失效**：`scottelectricusa.com` 对来源 IP 返回 **Spamhaus PBL 554** ⇒ 无法用 RCPT 验证。
- ⚠️ **成立年份口径矛盾**（业务描述 1946 vs 州注册 1957）⇒ 建议用「1946 年创立」，或**回避年份**。
- ⚠️ **规模数据分歧大**（178–241 人 vs Seamless 501–1,000 人/$500M）⇒ **正文勿引用具体数字**。
- ⚠️ **主送人职能取舍**：President 非采购岗（采购岗 Ryan Kelly / William D. 无邮箱）⇒ 已在联系人段如实标注。

### 信息缺口清单（请勿编造）
- Samuel Z. Scott 的**已验证具名邮箱**：**未找到**（`sscott@` 仅单一第三方来源）
- **第一方角色邮箱**（官网明文）：未找到（站点地域封锁）
- Samuel Z. Scott 的**个人 LinkedIn 直链 / 任职时长**：未获取
- **采购负责人（Purchasing Manager / Director）姓名**：未找到（仅见 Purchasing Agent / Purchasing）
- Ryan Kelly / William D. 的**邮箱与全名**：未找到（William D. 姓名被 LinkedIn 缩写）
- 公司**员工数 / 营收**（一手源口径）：口径分歧，未定
- 公司**常用变压器容量 / 电压 / 品牌**：未获取
- **24h panel shop 的业务范围**（是否含自制 panel/gear 组装）：未核实

### 一句话画像
宾州 Greensburg 一家 1946 年创立、近 80 年的**家族独立电气分销商**（PA/NY/MD 三州、gear + panel shop）—— **CSV 给的域名根本是另一家公司**（真站是 scottelectricusa.com，还对非美 IP 封锁）；家族主事人 Samuel Z. Scott 已由**州务卿一手源**确认为 President，但邮箱只有单一第三方来源，**主送建议电话点名转交**。

### 渠道覆盖清单（L-1、L0–L7）
| 层 | 结果 | 一句话 |
|---|---|---|
| L-1 锁人 | ✅ | PA 州务卿注册锁 President Samuel Z. Scott（+ VP Diastolfo）；LinkedIn 锁 2 名 Purchasing |
| L0 官网 | ⚠️ | `scottelectricusa.com` **地域封锁（非美 IP Access Denied）** ⇒ 未取第一方邮箱；`scottelectric.com` 属另一家公司 |
| L1 政府一手 | ✅ | **PA 州务卿注册（公司号 321218，Active，President/VP）** + SAM.gov/govtribe 政府供应商 |
| L2 命名+DNS | ✅ | MX=Intermedia；`{f}{last}@` 与 `sscott@` 自洽；SMTP 探测被 Spamhaus PBL 拦截（作废） |
| L3 B2B 库 | ⚠️ | AllBiz/ContactOut/LeadIQ/RocketReach 给职务与邮箱（**单一来源，未印证，H5**） |
| L4 社媒协会 | ⚠️ | 公司 LinkedIn 页 + Westmoreland Chamber 名录（联系人 2 名，非采购） |
| L5 黄页同址 | ⚠️ | Greensburg 1000 S Main St 多源一致 |
| L6 电话表单 | ✅ | (800) 442-8045 / (724) 837-9530 + 官网 contactus（未拨打/未提交） |
| L7 付费 | ❌ | 未启用 |
