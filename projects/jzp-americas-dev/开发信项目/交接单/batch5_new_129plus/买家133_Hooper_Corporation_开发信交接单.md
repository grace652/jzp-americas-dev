# 【买家 133】开发信交接单 — Hooper Corporation

> 采集日期：2026-09-28 ｜ 名单来源：`线索资产/目标客户清单.csv` 序号 17（A 类 · 电气承包商/工程公司）
> 采集方：找客户环节（本环节只产出交接单，不写正文/不碰模板/不定话术）
> ⚠️ 本表严格区分「已验证」与「未获取」，未找到的信息一律标注，**不做推断填充**（H1）
> 🟡 一句话结论：**1913 年成立、威斯康星州 DeForest 的全服务电力/机械承包商**（100+ 年历史，
> 5 个区域办公室，1800+ 台设备），**Electric Power Division 明列"Substation Department"**，
> 官网自述完成过 **345kV 与 500kV 输电线**；**领导层 9 人名单全部一手可查**
> （President Steve Lindley / SVP Electric Power Jake Davie / **VP – Substation Bruce Cram**）；
> 🔴 **但全站仅暴露 `DOT@`（交通安全口）与 `DMARC_Logs@`（技术口）两个角色邮箱，
> 无通用邮箱、无实名邮箱；邮件网关对未授权来源不透露真实目录** →
> **本单判定为「人明确、信号极强、但邮箱不达」**。

---

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示(如有)
Hooper Corporation | Bruce Cram（首选·变电站口）/ Jake Davie（备选·电力事业口） | VP Electric Power Division – Substation / SVP Electric Power Division | ⚠️ 未获取实名邮箱（官网仅 DOT@hoopercorp.com） | ⚠️ 无法验证（网关对未授权来源不透露目录） | https://cw.linkedin.com/company/hooper-corporation | 威斯康星州 DeForest 的全服务电力/机械承包商，1913 年成立；电力事业部下设 Substation Department 专营高压变电站建设/改造/维护；官网自述完成 345kV/500kV 线路；5 个区域办公室（WI/CO/FL/OH）+ 7 名高管公开 | 官网全站实抓（leadership / electric-power-division / press / contact）+ wisbusiness 官方新闻稿 + LinkedIn 公司页 + DNS/DMARC 分析 | ⚠️ **DMARC p=reject（最严格）**，投递合规要求高；⚠️ **无实名邮箱，投递需指定人**；⚠️ 第三方库（AllBiz）称 President 为 "David Orr"，**与官网冲突，以官网为准**
```

**发信资格：⚠️ 条件性通过（邮箱档位不足）**
**邮箱档位：B（角色邮箱 `DOT@hoopercorp.com` 为唯一公开地址，且属交通安全口，B2B 开发不适用）**

> 🔴 **本单与 131（Trueline）同型的交付缺陷**：人名、职位、业务证据**全部一手可查且极强**，
> **但邮箱拿不到**。区别在于：
> - 131 失效原因 = 域名 **catch-all**（一律 250）
> - 133 失效原因 = 网关 **对未授权来源不透露目录**（控制组返回 451，随机地址返回 550，
>   无法建立「真地址 → 250」的基准）

---

## 二、补充信息（扩展段）

### 标准字段明细

| 项 | 内容 | 来源 |
|---|---|---|
| **公司全称** | **Hooper Corporation** | 官网 / 新闻稿（双源✅）|
| **国家 + 城市** | **美国 WI 州 DeForest**（总部；另有 5 个区域办公室）| 官网 Contact 页（一手）|
| **州省** | **WI ✅**（CSV 填 WI，**正确**）| 官网 |
| **详细地址** | **6450 Pederson Crossing Boulevard, DeForest, Wisconsin 53532-1613**（总部）<br>制造厂：6400 Pederson Crossing Boulevard（同街区）| 官网 Contact 页（一手）|
| **电话** | **(608) 249-0451**（总部）；**24h 电力应急 (877) 630-7554** | 官网（一手）|
| **注册信息** | ⚠️ **未获取**（美国为州级注册，未查 WI DFI 备案）| — |
| **成立年份** | **1913**（官网 *"Since 1913"*；LinkedIn *"Headquartered in Madison, Wis., since 1913"*；新闻稿 *"headquartered in Wisconsin since 1913"*）| ✅ **三源一致** |
| **域名** | hoopercorp.com（🔴 注意：**不是** hooper.com）| 官网 |
| **规模** | **5 个区域办公室**；**1,800+ 车辆与设备**（官网 Electric Power Division 页原句 *"an inventory of more than 1,800 vehicles and equipment"*）；官网称数百个项目 | 官网（一手）|
| **营收** | ⚠️ 未获取（未查私有公司财务）| — |
| **官网** | https://www.hoopercorp.com | — |

> 📌 **区域办公室（官网 Contact 页完整列出）**：
> - **中西部区**：Rothschild, WI（1630 County Road XX）｜Wauwatosa, WI（11020 W Plank Court, Suite F）
> - **俄亥俄河谷区**：Marietta, OH（103 Industry Road）
> - **东南区**：Davie, FL（6900 Southwest 21 Court, Suite 5）
> - **西区**：Commerce City, CO（4475 E. 74th Avenue, Suite 100）
> → **官网自述**：*"geographic reach from the Rocky Mountains to Florida"*

### 联系人（含 still_here 在职核验）

| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| **Bruce Cram** | **VP Electric Power Division – Substation（🔴 首选·变压器最对口）** | 官网 Leadership 页明列「Vice President Electric Power Division – Substation」；个人页写「Vice President / Substation and Underground Electric Construction Department Head」 | **15 年**（个人页原句 *"15 years of experience with onsite project management of both Substation and Underground Electric"*，页面日期 2019）| 中：官网个人页在列（2019 版）| 低 | ✅ https://www.hoopercorp.com/leadership/bruce-cram/ |
| **Jake Davie** | **SVP Electric Power Division（备选·整部门负责人）** | 官网 Leadership 页明列「Senior Vice President Electric Power Division」；新闻稿（2022-01-11）确认晋升 | **2005 年入职**（个人页原句 *"has been with Hooper Corporation since 2005"*）→ **约 21 年** | **高**：官网在列；2026-09 被 The Daily Reporter 列为 Wisconsin AEC 350 上榜领导 | 低 | ✅ https://www.hoopercorp.com/leadership/jake-davie/ |
| **Steve Lindley** | President（第三备选·公司级） | 官网 Leadership 页明列「President」；个人页写「President of Hooper Corporation」 | **26+ 年**（个人页原句 *"more than 26 years of experience"*）| 高：官网在列；2022 新闻稿由其发言 | 低 | ✅ https://www.hoopercorp.com/leadership/steve-lindley/ |
| **Damon Arsenault** | VP Electric Power Division – Transmission & Distribution | 官网 Leadership 页明列 | 2021-02 入职（新闻稿）| ⚠️ 个人页 **404**（官网无）| 低 | ❌ 官网无 |
| **Robert Hoffer** | Chief Financial Officer | 官网 Leadership 页明列 | **2008 年入职**（个人页原句）→ 约 18 年 | 中 | 低 | ✅ https://www.hoopercorp.com/leadership/robert-hoffer/ |
| **Mike Anderson** | Vice President Safety | 官网 Leadership 页明列 | ⚠️ 未知 | ⚠️ 未知 | 低 | ❌ 官网无 |
| **Brad Werlein** | SVP Mechanical Division | 官网 Leadership 页明列 | ⚠️ 未知 | ⚠️ 未知 | 低 | ❌ 官网无 |
| **Brian Schultz** | SVP Mechanical Division – Operations | 官网 Leadership 页明列 | ⚠️ 未知 | ⚠️ 未知 | 低 | ❌ 官网无 |
| **Rob Weise** | VP Mechanical Division – HVAC | 官网 Leadership 页明列 | ⚠️ 未知 | ⚠️ 未知 | 低 | ❌ 官网无 |

> 🔴 **机读结论**：
> 1. **领导层 9 人**全部来自**官网 Leadership 页（一手）**，其中 4 人有个人详情页。
> 2. **首选收件人应为 Bruce Cram（VP – Substation）** —— 其职权**直接覆盖变电站**，
>    而变压器安装在 substation 部门的业务范围内。
> 3. **次选 Jake Davie（SVP Electric Power Division）** —— 新闻稿（2022-01-11）明确
>    *"oversee all areas of the Electric Power Division including distribution and transmission, **substation**, line clearance, and emergency storm response"*
>    → **substation 在其管辖内**，是 Bruce 的上级。
> 4. ⚠️ **个人页日期为 2019-09-03**，页面内容可能滞后（例：Jake Davie 个人页仍写
>    "Overhead Line Department Head"，而其现职已是 SVP）→ **职称以 Leadership 主页为准**。
> 5. ⚠️ **Damon Arsenault 个人页 404**，说明官网并非所有领导都有详情页。
> 6. ⚠️ **第三方库冲突**：AllBiz 称 "David Orr (President)"，**与官网 Steve Lindley 冲突**。
>    → **判定 AllBiz 数据陈旧**（Hooper 2021 年统一公司名、2022 年领导层变动）。
>    **一律以官网为准**。

### 邮箱分档（A/B/C）

| 档 | 地址 | 依据 | 可否主送 |
|---|---|---|---|
| A | ⚠️ **无** | 未取得任何实名邮箱 | ❌ |
| B | **`DOT@hoopercorp.com`** | 官网 Contact 页明列（一手）| ⛔ **不适用** —— 这是**交通安全（Dept. of Transportation）对接邮箱**，非商务口。按 H6，**角色邮箱单独不可交付**，且此角色与开发信主题完全不符 |
| B | `DMARC_Logs@hoopercorp.com` | **DMARC 记录明列**（`rua=mailto:DMARC_Logs@hoopercorp.com`）| ⛔ **绝不可用** —— 这是**邮件安全日志邮箱**，发商务信属严重错配 |
| C | — | 无 | — |

**🔴 邮箱验证方法与证据链（可复现 —— 本单结论是「无法验证」）：**

```
域名 hoopercorp.com
MX = mx1~mx4.mtaroutes.com   （第三方邮件安全网关 MTA Routes，后端接 Office 365）
SPF = 未取到标准 v=spf1 记录（TXT 仅有验证串）
DMARC = v=DMARC1; p=reject; rua=mailto:DMARC_Logs@hoopercorp.com; fo=1
        🔴 p=reject 为最严格策略

🔴 SMTP RCPT 探测过程（2026-09-28 实测）：
   ① 直连 MX 探测 → 全部 451 "4.4.62 Mail sent to the wrong Office 365 region"
      → 区域路由问题，探测无效
   ② 改逐台 MX 单发 → 得到 550 "no mailbox by that name is currently available"
      → 但对以下地址【全部】返回同一 550：
          zzz_nonexistent_probe_9987@（随机）
          info@ / contact@ / sales@ / careers@（常见角色邮箱）
          steve.lindley@ / slindley@ / jake.davie@ / bruce.cram@（实名候选）
   ③ 控制组（已知存在的 DMARC_Logs@）→ 451 "not yet authorized to deliver mail from <ian@jiezougroup.com>"
      🔴 关键：控制组被【授权门槛】挡住，无法建立「真地址 → 250」基准
   ④ 连续探测后连接被切断（"Too many failed recipients"）→ 触发速率限制

⇒ 判定：**该网关对未授权来源不透露真实目录**
   在 451 未授权的条件下，所有 550 "no mailbox" 都【不可信】——
   既可能是地址不存在，也可能是网关对未授权来源的统一回应
⇒ ⛔ **本单无法通过 SMTP 判定任何邮箱真伪**
```

> 🔴 **必须向写信/发送环节交代清楚**：
> 1. **`hoopercorp.com` 是 `p=reject` 的严格域**，且网关（mtaroutes）设授权门槛。
>    我方 IP 在**未获授权**状态下**探测不到目录**。
> 2. 我**没有**、也**无法**确认任何实名邮箱。**任何候选地址（如 `bruce.cram@`）都属推测，不得使用**（H2）。
> 3. ⚠️ 注意区分：**探测"被拒"≠"邮箱不存在"**。这与 132（Mott 域统一 550 拒绝）机理不同，
>    但结论一样 —— **本域 SMTP 探测不可用作交付依据**。

### 我为什么找他

**这是一家把「变电站」写进部门建制的百年承包商，且官网自述做过 345kV/500kV 线路。**

| # | 具体观察（均有官网/新闻稿原句出处） |
|---|---|
| 1 | **官网 Electric Power Division 页原句**：*"Hooper Corporation's **Substation Department** specializes in **high voltage substation construction, modifications, and maintenance**"* —— **独立部门建制** |
| 2 | **官网 Business Units 页原句**：*"a geographic reach from the Rocky Mountains to Florida"*，且 *"our regional offices located in Wisconsin, Colorado, Florida, Michigan and Ohio have collectively completed hundreds of successful projects, including significant **345kV and 500kV lines** throughout the United States."* |
| 3 | **官网 About 页原句**：*"Hooper's areas of expertise include ... as well as **the construction of substations** and **high-voltage transmission and distribution lines**."* |
| 4 | **LinkedIn 公司帖文（2025-03）项目实录**：*"First, Hooper crews **disassembled a spare transformer at the Hazel Creek Substation** and carefully prepared it for transport."* —— 🔴 **变压器现场作业的直接证据** |
| 5 | **24h 全国电力应急响应**：*"24-Hour Electric Power Emergency Storm Response (Nationwide): (877) 630-7554"* —— 抢修场景 = 存量设备更换需求 |
| 6 | **百年历史 + 持续扩张**：1913 年成立；2021 年统一公司名 + 启用在 DeForest 的新总部与预制厂（Daily Reporter / WMTV 报道）；2026-05 新开 Rothschild 办公室 |
| 7 | **领导层持续获行业表彰**：The Daily Reporter 的 Wisconsin AEC 350（2026-09 有五位 Hooper 领导上榜）、CFO of the Year（2025）、Senior Project Manager of the Year（2025） |
| 8 | **Jake Davie 的职权含 substation**（2022 新闻稿原句，见上）；**Bruce Cram 直接管 Substation 部门**（官网）|
| 9 | 官网自述员工 *"top-rated in **design, engineering, project management**, and skilled trades"* → **有设计/工程能力**，可能参与设备规格制定 |

> 📌 **开场可用的合法事实**（措辞由写信环节定）：
> 「Hazel Creek 变电站的备用变压器拆解运输」或「Substation Department 专营高压变电站建设改造」
> —— **均为官网/LinkedIn 原句，只有这家成立**。

### 买家类型 / 需求品类

**买家类型：🔥 B — 全服务电力/机械承包商（EPC / 施工型，纯 B 型）**
判定依据（六层过筛结果）：
- ⓪ 反身排除：**通过** —— 官网**无任何 "manufacturer / we manufacture / our factory" 字样**；不做设备制造（有 Fabrication Facility，但按官网描述为**管道/机械预制**，非变压器）；未发现代理任何品牌（尤其**未见 YAWEI**）
- ① 价值链：主营 = 输配电线路 + 变电站 + 机械 → 价值链中间环节 ✅
- ② 类型：**B（全服务承包商）** —— 依据 *"full-service electric, power and mechanical contractor"*
- ③ 产品形态：**变电站变 / 电力变**（见下）
- ④ 地域：**美国 WI（美国市场 → 主推配电级）** ⚠️ 见下方定位说明
- ⑤ 规模：**大**（5 区域办公室、1800+ 设备、百年企业）

**🔴 美国市场产品定位（重要）**：
根据我方业务事实 —— **美国市场无高压主变销售先例，主推配电级（E541627）**。

**需求品类（带结论态 —— 美国客户，主推配电级）：**

```
- `三相美变 / padmount（UL E541627，45–5,000 kVA，可直供）`   ← 🔴 主谈：美国市场主推配电级
- `三相液浸电力变（UL E541626，750–110,000 kVA，可直供）`     ← ⚠️ 若其变电站项目需中压电力变，可试探性提及（但美国无先例，不作为主打）
- `杆上变 / 单相（UL E544629，仅 ECD Letter，非证书）`          ← 配电侧，备选
- `干变（美国可谈：built to UL/ANSI/IEEE，需人工确认）`         ← 备选，不首推
```

> ⚠️ **矛盾提示**：官网自述完成 **345kV/500kV 线路**（超高压），但这**是线路施工能力，不是变压器采购规格**。
> 且 **345/500kV 级主变远超我方能力边界（E541626 上限 110,000 kVA / 121kV）**。
> → ⛔ **绝不因其做 500kV 线路就推高压主变** —— 线路施工与变压器采购是两码事。
> → 主打**配电级 E541627**，落点在变电站的**中低压侧设备**与配网场景。

### 电压·频率·认证要求

| 项 | 内容 | 来源 |
|---|---|---|
| **频率** | **60 Hz**（美国）✅ 零改造适配 | 国别推定 |
| **电压** | 官网自述完成 **345kV / 500kV 线路**（⚠️ 线路能力，非变压器规格）| 官网原话 |
| **客户资质** | 服务公用事业（website 提 "utility sector"）；NECA 会员（Jake Davie 任 NECA Government Affairs Committee 成员）| 官网个人页 |
| **认证（我方口径）** | 美国：美变亮 `UL E541627`；电力变亮 `UL E541626`；可写 `built to ANSI/IEEE standards` | 我方能力边界 |
| ⛔ **禁止写法** | `CSA Certified`／`cUL and CSA`／`SASO`／`SONCAP`；**不得写变压器具体 kV/kVA** | 红线 §二 |

> 🔴 **345kV/500kV 是「线路施工能力」，出自官网 Electric Power Division 页。**
> 正文**可以引用其线路能力**（原话），但 ⛔ **不得据此推断变压器规格，
> 更不得据此推高压主变**（我方美国无高压先例 + 超出能力边界）。

### 采购信号

| # | 信号 | 强度 | 出处 |
|---|---|---|---|
| 1 | **官网 Substation Department 独立建制**，专营高压变电站建设/改造/维护 | 🔥🔥🔥 | 官网（一手）|
| 2 | **LinkedIn 项目实录：Hazel Creek 变电站备用变压器拆解运输**（2025-03）| 🔥🔥🔥 | LinkedIn 公司帖（一手发布）|
| 3 | **24h 全国电力应急响应** → 抢修更换频次高 | 🔥🔥🔥 | 官网（一手）|
| 4 | **持续扩张**：2021 新总部/预制厂、2026-05 新开 Rothschild 办公室 | 🔥🔥 | 新闻报道（多源）|
| 5 | **百年企业（1913）+ 5 区域办公室 + 1800+ 设备** → 采购体量大 | 🔥🔥 | 官网（一手）|
| 6 | 领导层频繁获行业奖（Wisconsin AEC 350 2026-09 五人上榜）→ 行业活跃度高 | 🔥 | 官网 Press 页 |
| 7 | ⚠️ 未发现近期**变压器采购招标**公开记录 | ⚠️ | 未查招标平台 |

> ✅ **信号强度：极强**。这是本批**业务对口度最高**的公司之一
> —— 有独立变电站部门、有变压器现场作业实录、有全国应急响应。
> 🔴 **但邮箱不可达，这是本单唯一也是致命的短板。**

### 可利用的钩子（按强度排序）

| 序 | 钩子 | 强度 | 落点品类 | 是否可写 |
|---|---|---|---|---|
| 1 | **LinkedIn 项目实录：Hazel Creek 变电站备用变压器拆解运输** | 🔥🔥🔥 | 配电变 / padmount | ✅ |
| 2 | **官网 Substation Department 独立建制** | 🔥🔥🔥 | 配电变 | ✅ |
| 3 | **24h 全国电力应急风暴响应** —— 抢修需要快速供货 | 🔥🔥🔥 | 配电变 | ✅ |
| 4 | **1913 年成立 100+ 年历史 + 持续扩张** | 🔥🔥 | — | ✅ |
| 5 | **官网自述完成 345kV/500kV 线路** | 🔥 | — | ⚠️ 可引用，但**不得据此推高压主变** |
| 6 | NECA 会员（Jake Davie 在政府事务委员会） | 🔥 | — | ⚠️ 来源是个人页，引用需谨慎 |

### 开发信建议

> 📌 本段是**给写信环节的输入**，不是正文。**不含主题行、开场句、产品切片措辞**（分工铁律）。

- **收件人策略**：🔴 **本单无任何实名邮箱**，唯一公开地址是 `DOT@hoopercorp.com`（**不适用**）
  - **首选对象（人）**：**Bruce Cram（VP – Substation）** —— 职权直接覆盖变电站，最对口
  - **次选对象（人）**：**Jake Davie（SVP Electric Power Division）** —— 其上级，管辖含 substation
  - **第三备选**：Steve Lindley（President）
  - 🔴 **一家公司只发 1 人**（skill §3.0 红线）
  - ⛔ **严禁使用**：`DOT@hoopercorp.com`（交通安全口）、`DMARC_Logs@`（安全日志口）、
    以及任何推测格式（`bruce.cram@` / `bcram@` / `jdayvie@`）
- **称呼**：待邮箱获取后确定（人已明确）
- **开场角度（供选择，非指定）**：可考虑从「Hazel Creek 变电站的变压器拆解运输」或「Substation Department 独立建制」切入 —— **最终写法归写信环节**
- **附件建议**：不带供货记录名录（H7 红线）；可备 **UL E541627 区间说明（45–5,000 kVA）**
- **发送时段**：客户在 **WI 州 = 中部时区（CT）**
  - 目标送达：**当地工作日 08:00–10:00**
  - 北京发送窗口（夏令时）：**21:00–23:00**
  - 冬令时：22:00–24:00
  - ⚠️ **周末不发**（按客户当地星期判断）
- **送达配置**：
  - 网关 = **mtaroutes.com**（第三方安全网关，后端 Office 365）
  - 🔴 **DMARC = `p=reject`（最严格策略）** → **我方发信域名必须 SPF + DKIM + DMARC 全部配置正确，
    否则会被直接拒收**。这是本单**最高优先级的技术要求**
  - 🔴 网关设**授权门槛**（未授权来源返回 451）→ 说明其**反垃圾策略严格**，
    首次接触建议**纯文本、无附件、无图片、无跟踪像素**
  - ⚠️ 本单**未取到标准 v=spf1 记录**（TXT 仅有验证串），建议发送环节复核

### ⚠️ 矛盾点与风险提示

| # | 风险 | 详情 | 处置 |
|---|---|---|---|
| 1 | 🔴🔴 **无实名邮箱（本单最大缺陷）** | 全渠道（官网全站 / 新闻稿 / 个人页 / DMARC）**仅有 `DOT@` 与 `DMARC_Logs@` 两个角色邮箱，均不适用**；网关不透露目录 | **本单按「信息不够不发」精神，定级为「草稿级可写、发送前须补人」**。若写信环节认为无可送地址，**本单应退回** |
| 2 | 🔴 **DMARC p=reject** | 最严格策略，投递合规要求极高 | **发送环节必须确保我方 SPF/DKIM/DMARC 齐全**；否则直接被拒 |
| 3 | 🔴 **不得推高压主变** | 官网自述 345kV/500kV **线路**能力，易诱发误推高压主变 | ⛔ **美国市场主推 E541627 配电级**；345/500kV 远超我方能力边界（E541626 上限 121kV） |
| 4 | ⚠️ **第三方库与官网冲突** | AllBiz 称 President 为 "David Orr" | **以官网 Steve Lindley 为准**；⛔ 不得引用 AllBiz |
| 5 | ⚠️ **领导个人页日期滞后** | 个人页均标注 2019-09-03（Jake Davie 页仍写旧职）| **职称以 Leadership 主页为准** |
| 6 | ⚠️ **Damon Arsenault 个人页 404** | 官网并非所有领导都有详情页 | 不影响收件人选择 |
| 7 | ⚠️ **注册信息未获取** | 美国州级注册未查（WI DFI）| 列为缺口 |
| 8 | ⚠️ **SPF 标准记录未取到** | TXT 仅有域名验证串 | 交发送环节复核 |
| 9 | ⚠️ **规模/营收未获取** | 无第三方财务数据 | 列为缺口 |

### 信息缺口清单（请勿编造）

> 🔴 **以下字段正文一个字都不能出现**（红线：比"不编造"更严格，连模糊表述都不行）。

| 缺失项 | 说明 |
|---|---|
| **实名邮箱（任何高管）** | 🔴 **本单核心缺口**。未获取 |
| **注册号 / 注册日期** | 未获取（未查 WI DFI）|
| **员工人数 / 营收** | 未获取。**不得假设** |
| **变压器侧电压等级** | 未获取。只用官网**线路**能力原话 |
| **常用变压器容量段（kVA）** | 未获取。**不得假设** |
| **变压器采购方式** | 未获取（总部集中 vs 区域分散，未知）|
| **是否已有中国供应商** | 未查（未启用海关数据源）|
| **SPF 标准记录** | 未取到 |
| **Bruce Cram / Jake Davie 的任职起始年月** | Jake Davie 为 2005 年（已知）；**Bruce Cram 仅有"15 年经验"表述，起始年月未知** |
| **Mike Anderson / Brad Werlein / Brian Schultz / Rob Weise 履历** | 未获取（官网无个人页）|
| **公司 LinkedIn 具体数据（员工数等）** | 未取 |
| **任何未在官网列出的客户名** | 未获取。**不得编造**（Hazel Creek / 345kV / 500kV 均为官网原话，可引用）|

### 一句话画像

**1913 年成立的威斯康星州 DeForest 全服务电力/机械承包商**（5 区域办公室、1800+ 设备，
Electric Power Division 下设独立 Substation Department，官网自述做过 345kV/500kV 线路，
LinkedIn 有 Hazel Creek 变电站备用变压器拆解实录）；
**领导层 9 人全部一手可查（首选 VP – Substation Bruce Cram）**，
🔴 **但官网只暴露两个不适用角色邮箱（`DOT@` / `DMARC_Logs@`），网关对未授权来源不透露目录，
且 DMARC 为最严格的 p=reject** —— **「人明确、信号极强、邮箱不达」**。

### 渠道覆盖清单（L-1、L0–L7）

| 层 | 结果 | 一句话 |
|---|---|---|
| **L-1 锁人** | ✅ | 🔴 **官网 Leadership 页 9 人完整名单**（一手），其中 4 人有个人详情页含履历 |
| **L0 官网全量** | ✅ | 主页 / leadership / electric-power-division / about-us / contact-us / press / careers + 4 个人页实抓；**仅有 2 个不适用角色邮箱** |
| **L1 政府一手** | ❌ | **未查**（美国 WI DFI 州级注册未取）|
| **L2 命名 + DNS** | ⚠️ | MX/SPF/DMARC 全取；🔴 **DMARC p=reject**；🔴 **网关授权门槛导致 SMTP 探测不可用**（已用控制组证明）|
| **L3 B2B 库** | ⚠️ | AllBiz / ContactOut / Wiza / PeopleSmart 均命中，**但数据陈旧或需付费**；⚠️ **AllBiz 的 President 与官网冲突** |
| **L4 社媒协会** | ✅ | LinkedIn 公司页命中（cw.linkedin.com/company/hooper-corporation）；NECA 会员线索（个人页）；The Daily Reporter 多次报道 |
| **L5 黄页同址** | ✅ | 地址完整（总部 + 5 区域办公室）；AllBiz 列表亦命中 |
| **L6 电话表单** | ✅ | **总部电话 (608) 249-0451 已取**；官网有 General Inquiry / Project Inquiry 表单 → **表单可作 B 档兜底** |
| **L7 付费** | ❌ | 未启用 |

> 🔴 **建议的补人路径（交给用户/下一环节）**：
> 1. **电话 (608) 249-0451 直接问 Electric Power Division 采购/商务对接邮箱** —— 成本最低、命中率最高
> 2. **官网 Project Inquiry 表单** —— 可作为 B 档兜底（但会流入销售池）
> 3. ⚠️ 因 DMARC p=reject 且网关设门槛，**不建议盲发推测地址**（会损害我方域名信誉）

---

## 三、交付方自检（写单者留痕）

- [x] **第 0 步判定已做**：类型归属（B 全服务承包商）+ 判定依据 + 可对应产品形态
- [x] **第 ⓪ 层反身排除已做**：官网无 "manufacturer" 字样；Fabrication Facility 非变压器制造；未代理品牌（无 YAWEI）
- [x] **背调 13 步「必做 6 步」已走**：公司名 ✅ / 版权主体 ✅（© 2024 Hooper Corporation）/ 简介历史 ✅ / 注册库 ⚠️（美国州级未查，已标缺口）/ 无街景（地址已取）/ LinkedIn 公司页 ✅ + 官网 Leadership 锁人 ✅
- [x] **排重已做**：与 `_dedup_keywords.txt`（164 词）+ `_bounce_domains.txt` + `00_buyer_master_dedup.md` 比对，**无命中**
- [x] **按公司归并**：无实名邮箱，**已明确禁用两个不适用角色邮箱与所有推测格式**
- [x] `.md` 已实际写入磁盘
- [x] 9 核心字段 + 12 扩展段齐
- [x] 「我为什么找他」为**具体观察**（9 条，均有官网/新闻稿/LinkedIn 原句）
- [x] 「信息缺口清单」明确列出不能写的字段（12 项）
- [x] 「需求品类」**带结论态**（含美国市场定位说明）
- [x] 联系人四栏（still_here）已核
- [x] 邮箱已分 A/B/C 档，**验证方法可复现（并诚实说明"无法验证"）**
- [x] 过完 §三 九条闸门 —— ⚠️ **邮箱档位一条为「条件性通过」，故整体标为条件性通过**
- [x] 未写任何邮件正文 / 主题行 / 开场句措辞（分工铁律）
