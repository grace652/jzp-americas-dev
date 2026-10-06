# 【买家 147】开发信交接单 — Earl Carr Electric Canada Ltd.（ECECL）

> 采集日期：2026-09-28 ｜ 名单来源：`线索资产/目标客户清单.csv` 序号 12（A 类 · 电气承包商/工程公司）
> 采集方：找客户环节（本环节只产出交接单，不写正文/不碰模板/不定话术）
> ⚠️ 本表严格区分「已验证」与「未获取」，未找到的信息一律标注，**不做推断填充**（H1）
> ✅ 一句话结论：**渥太华东部 Carp 的商业/工业电气承包商，1978 年成立（47 年）**；
> 客户含 **PWGSC（联邦工程部）、DND、渥太华医院、Carleton 大学、渥太华大学、Loblaws、OCDSB、ZIBI**；
> 能力含 **"new line construction"（新建线路）** 与 **"emergency power restoration"（应急供电恢复）**；
> 曾 **3 次获 R.H. (Hugh) Carroll 安全奖**（2001/2009/2010）；
> 联系人 **Doug Vandemheen**（⚠️ **官网标 Director of Construction / LinkedIn 标 Owner，职务冲突**）；
> 🎯 邮箱 **`reception@ececl.ca` —— SMTP 控制组法三点对照命中（B 档，域非 catch-all）**。
> 🔴 **官网存在被注入的赌博外链** —— 疑似被挂马，**发送与回信均须警惕**。

---

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示(如有)
Earl Carr Electric Canada Ltd. | Doug Vandemheen | ⚠️ Director of Construction（官网）/ Owner（LinkedIn）—— 口径冲突 | reception@ececl.ca | ✅ 已验证存在（SMTP 三点对照，非 catch-all）；⚠️ 角色邮箱 | ca.linkedin.com/in/doug-vandemheen-05b25b26（仅摘要可见）| 渥太华东部 Carp 的电气承包商，1978 年成立（40+ 年）；服务商业/工业客户；能力含配电、火警、照明、维护、**新建线路施工**、**应急供电恢复**、design-build、按标/单价/成本加成计费；客户含 PWGSC、DND、渥太华医院、Carleton 大学、渥太华大学、Loblaws Properties、OCDSB、CRC、ZIBI；曾 3 次获 R.H. Carroll 安全奖 | 官网实抓（首页/company-overview/our-team/contact 页）+ LinkedIn 摘要 + 第三方 allbiz + DNS/SMTP 控制组法 | 🔴 官网被注入赌博外链（疑似挂马）；⚠️ 职务口径冲突；⚠️ 变压器信号弱；⚠️ 三个域并存
```

**发信资格：⚠️ 有条件通过**（有具名联系人 + 邮箱已 SMTP 验证；缺口在「职称冲突 + 业务对口弱 + 官网安全风险」）
**邮箱档位：B（角色邮箱 · 官网明文 · SMTP 三点对照已验证）**

---

## 二、补充信息（扩展段）

### 标准字段明细

| 项 | 内容 | 来源 |
|---|---|---|
| **公司全称** | **Earl Carr Electric Canada Ltd.**（简称 **ECECL**，官网自用）| 官网（一手）|
| **国家 + 城市** | **加拿大 ON 省 Carp（卡普，渥太华西部郊区）** | 官网 Contact 页（一手）|
| **州省** | **ON ✅**（CSV 填 ON，**正确**；任务书称 "Ottawa"，实际**注册地在 Carp**）| 官网 |
| **详细地址** | **120 Walgreen Road (Unit 3), Carp, ON K0A 1L0**（🟢 **官网首页明文**，**第一方**）| 官网（一手）|
| **电话** | **613.831.9179**（🟢 官网 Contact 页明文）| 官网（一手）|
| **注册信息** | ⚠️ **未获取** | — |
| **成立年份** | **1978**（🟢 官网首页明文：*"providing electrical solutions for commercial and industrial customers **since 1978**"*；company-overview 页重复 *"since 1978"*；并称 *"over 40 years of experience"*）| 官网（一手，两处一致✅）|
| **域名** | 🔴 **三个域并存**：<br>① `earlcarrelectriccanada.com`（**网站域**）—— 🔴 **Proofpoint ARS 网关，"转发式 250"**<br>② **`ececl.ca`（邮箱域）** —— ✅ **M365，非 catch-all，SMTP 有效**<br>③ （`ececl` 为其官方简称）| 实测确认 |
| **邮件网关** | `earlcarrelectriccanada.com`：**Proofpoint ARS**（`earlcarrelectriccanada.com.1.0001.arsmtp.com`）<br>`ececl.ca`：**Microsoft 365**（`ececl-ca.mail.protection.outlook.com`）| DNS MX |
| **SPF** | `earlcarrelectriccanada.com`：`v=spf1 include:spf.protection.outlook.com -all`（**-all 硬失败**）<br>`ececl.ca`：`v=spf1 include:**edgepilot.com** -all`（**-all 硬失败**，用第三方邮件平台）| DNS TXT |
| **DMARC** | ⚠️ **两域均未配置** | DNS |
| **规模** | ⚠️ **未获取**（官网团队页列 3 人）| — |
| **荣誉** | **R.H. (Hugh) Carroll 安全奖** 三次：**2001 / 2009 / 2010**（官网明文）| 官网（一手）|
| **客户** | **PWGSC**（联邦公共工程）、**DND**、**The Ottawa Hospital**、**CRC**、**Carleton University**、**University of Ottawa**、**Loblaws Properties**、**OCDSB**、**ZIBI (Windmill Dream)** | 官网（一手）|
| **官网** | https://earlcarrelectriccanada.com | — |

### 🔴🔴 重大安全发现：官网被注入赌博外链（疑似挂马）

在抓取官网 **首页/company-overview 页**时，发现**正文中夹入两段与业务完全无关的赌博站点推广文案与外链**：

```
"Picking a UK casino brand often comes down to how fast payouts clear, the depth of live games
 and bonus terms that read plainly. … A name appearing repeatedly across review roundups is
 [rhino casino](https://rhinocasinouk.com/en-gb/) for its broad game range and steady live tables. …"

"Newcomers often compare welcome packages and wagering terms before committing real funds anywhere
 online. Spending time on [karamba casino](https://karambacasino-uk.com/en-gb/) shows a tidy lobby …"

[janusz casino](https://janusz-casino24.pl/)
[janusz kasyno](https://polskie-januszcasino.pl/)
[beep beep casino pl](https://beepbeepcasino4.pl/)
```

**判读**：
- 🔴 这是**典型的 WordPress / CMS 被注入外链（link injection / SEO 挂马）**特征 ——
  **注入内容直接插在正文段落之间**，是**网站已被入侵的强信号**（比买家 138 ETAC 的页脚隐藏链接更严重）。
- ⚠️ **不构成排除理由**（该公司本身仍是合格目标），但**必须写入本单并提示发送环节**：
  1. **该域可能已被入侵** ⇒ **往来邮件存在被第三方截取或仿冒的风险**；
  2. **若对方回信，须留意发信源真实性**（尤其涉及链接、附件、付款信息时）；
  3. 可作**同名公司的识别指纹**。
- ⛔ **本环节未点击、未访问任何该等链接。**

> 📌 已同步记录至 skill `渠道状态清单.md` §七「网站被注入外链 = 线索可信度指纹」。

### ⚠️ 第一判断：业务对口度偏弱（须如实标注）

官网**通篇未见**「变压器」「变电站」「高压」表述。其自我定位为：

> *"a leading electrical contractor in **Eastern Ontario** providing electrical solutions for
> **commercial and industrial** customers since 1978"*（官网首页，一手）

官网业务描述（company-overview 页，一手，逐字）：
> *"Distribution, Fire Alarm Systems, Lighting and maintenance projects are all in a day's work…"*
> *"We also provide **design-build services** and can operate on a **bid, unit price, or cost-plus basis**"*
> *"Whether it is **emergency power restoration** or **new line construction** the value of ECECL's expertise cannot be underestimated."*

🔴 **业务含义（供写信环节自行判断，本环节不定话术）**：
- ✅ **两个正面信号**：
  1. ***"new line construction"***（新建线路施工）—— **可能触及配电线路与设备**
  2. ***"emergency power restoration"***（应急供电恢复）—— **可能触及变压器抢修/替换**
- ⚠️ **但均为泛化表述，无具体电压等级或设备名称** ⇒ **不得推断其采购变压器**（H1）。
- ✅ **客户强度高**：PWGSC / DND / 渥太华医院 / 两所大学 / Loblaws ⇒ **项目来源稳定且体量可观**。
- ⚠️ **⇒ 归入「可能触及但未明示」类**（与买家 141/142/146 同档）。

### 联系人（含 still_here 在职核验）

| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| **Doug Vandemheen** | **首封主送** | 🔴 **口径冲突**：<br>① **官网 Our Team 页明文**：*"Doug Vandemheen — **Director of Construction**"*（🟢 第一方）<br>② **LinkedIn 标题**：*"**Owner**, Earl Carr Electric Canada Ltd"*（第三方）| **1978 年入行至今（47 年）**；官网称 *"Doug has been in the industry **since 1978**… completed his apprenticeship training in Western Canada primarily in the **oil and gas sector**… moved back to Ottawa"* | **高**：官网团队页在列 + LinkedIn 在列 | **低**（Owner 级）| ca.linkedin.com/in/doug-vandemheen-05b25b26（仅摘要可见）|
| Janelle Vandemheen | **Operations** | 🟢 官网 Our Team 页明文 *"OPERATIONS"*；*"joined in **2012**… In **2016**, she moved into the role of Operations"* | 2012 至今（13 年）| 高：官网在列 | ⚠️ 未知 | ⚠️ 未获取 |
| Laura Scott | **Project Coordinator** | 🟢 官网 Our Team 页明文；*"joined… in **2003**… In **2004**, she moved into the role…"* | 2003 至今（22 年）| 高：官网在列 | ⚠️ 未知 | ⚠️ 未获取 |
| Jacques Gauthier | ⚠️ **仅第三方**（allbiz 称其为 "primary contact"）| ⚠️ 官网**无此人** | ⚠️ 未知 | ⚠️ 未知 | ⚠️ 未知 | ⚠️ 第三方 |

> 🔴 **机读结论**：
> 1. 🔴 **Doug Vandemheen 职务存在冲突**：**官网写 Director of Construction，LinkedIn 写 Owner**。
>    **处置**：**官网为第一方，优先采信「Director of Construction」**；
>    但 **LinkedIn 的「Owner」亦可能为真**（官网未否定其所有权）。
>    ⇒ **⛔ 正文中不得强调其具体职称**，**建议直呼姓名**（H4/H6）。
> 2. ✅ **Vandemheen 姓氏出现两次**（Doug + Janelle）⇒ **疑为家族企业**（⚠️ 推断，非事实）。
>    且两职衔为「Construction Director」+「Operations」⇒ **两人构成运营核心**。
> 3. 🔴 **注意一处细节**：官网团队页**未列出任何"President"或"Owner"头衔** ——
>    与 LinkedIn 称 Doug 为 Owner 形成对照。**⇒ 该司领导层头衔体系不清晰。**
> 4. ⚠️ **Jacques Gauthier**（第三方 allbiz 称 primary contact）**官网无此人** ⇒ **不采信**（可能为过时数据）。

### 邮箱分档（A/B/C）

| 档 | 地址 | 依据 | 可否主送 |
|---|---|---|---|
| **B** | **`reception@ececl.ca`** | 🟢 **官网 Contact 页明文**（一手）；✅ **SMTP 控制组法三点对照命中**（随机 550 / 候选 250，**域非 catch-all**）| ✅ **主送** |
| C | `@earlcarrelectriccanada.com` 任何地址 | 🔴 **Proofpoint ARS 网关"转发式 250"** —— 探测返回 *"will relay to a client address"*，**不区分真假** | ⛔ **禁用**（无法验证 + 未获明文地址）|
| A | ⚠️ **未获取**（无具名邮箱）| — | — |

**🔴 邮箱验证方法与证据链（可复现）：**

```
域名 A：earlcarrelectriccanada.com（网站域）
  MX   = 10 earlcarrelectriccanada.com.1.0001.arsmtp.com
         20 earlcarrelectriccanada.com.2.0001.arsmtp.com
         （🔴 Proofpoint ARS —— 邮件安全网关）
  SPF  = v=spf1 include:spf.protection.outlook.com -all
  DMARC= ⚠️ 无

  探测：
    250  zzz_nonexistent_probe_9987@earlcarrelectriccanada.com
         :: "…will relay to a client address"
    250  info@earlcarrelectriccanada.com
         :: "…will relay to a client address"
  ⇒ 🔴 判定：Proofpoint ARS 属【"转发式 250"】—— 对【任何】收件人一律回 250 后转发给客户服务器，
     【完全不透露目录信息】⇒ 探测【无效】。属「令 SMTP 失效」的第 ④ 类新变体。

域名 B：ececl.ca（邮箱域 —— 官网 Contact 页所列）
  MX   = 10 ececl-ca.mx1.arsmtp.com
         20 ececl-ca.mx2.arsmtp.com
  SPF  = v=spf1 include:edgepilot.com -all
  DMARC= ⚠️ 无
  ⚠️ 注：MX 指向 ARS，但【实际 RCPT 响应来自 M365】⇒ 探测有效。

  探测：
    550 5.4.1  zzz_nonexistent_probe_9987@ececl.ca   ← 🔴 随机 550 ⇒ 【非 catch-all】✅
    250 2.1.5  reception@ececl.ca                     ← 🎯 命中
  ⇒ ✅ 三点对照齐备（随机 550 + 候选 250 + 官网明文）⇒ B 档成立。
```

> 🔴 **重要提示**：
> 1. **必须投 `ececl.ca`**，**不要投 `earlcarrelectriccanada.com`**
>    （后者是网站域，且被 ARS 反垃圾网关挡在前面，未验证地址风险高）。
> 2. **域 `ececl.ca` 使用 `edgepilot.com` 作为 SPF 发送平台** ⇒ 可能是外发邮件服务。

### ⚠️ 新增网关行为模式（已在 skill 记录）

🔴 **本单发现第 5 种「令 SMTP 探测失效」的网关行为：Proofpoint ARS 的「转发式 250」**

| 行为 | 表现 | 判据 |
|---|---|---|
| **转发式 250** | 对**任何**收件人（含随机地址）一律回 **250 + "will relay to a client address"** | 回执文本含 **"will relay"** ⇒ 该网关**不验证收件人**，只负责转发 ⇒ **探测无效** |

**⇒ 规程：见到 "will relay" 字样 ⇒ 立即判定该域 SMTP 不可用，改走其他渠道。**

---

## 三、开发信建议（**仅限：收件人 / 时机 / 附件 —— 不含正文、不含主题行、不含开场句**）

> 依分工铁律：**措辞/钩子/产品切片/主题行全部归环节 ②（写开发信 agent）**。本节只给**收件人与时机**层面的建议。

| 项 | 建议 | 依据 |
|---|---|---|
| **主送** | **`reception@ececl.ca`** | SMTP 三点对照命中；⚠️ 角色邮箱 |
| **⚠️ 勿投** | `@earlcarrelectriccanada.com` | 🔴 该域被 ARS 网关拦住，且未验证地址 |
| **称呼** | ⚠️ 若正文需称呼人：用 **Doug Vandemheen**，**不写职称**（官网与 LinkedIn 口径冲突）| 见上 §二 |
| **抄送** | ⛔ **不建议** | — |
| **第二触达** | 电话 **613.831.9179** | 官网 Contact 页明文（一手）|
| **建议时机** | **美东工作日 08:00–10:00**（Carp/Ottawa = America/Toronto / ET）| 承包商上午处理事务 |
| **建议附件** | ① **E541627**（三相配电变，45–5,000 kVA）—— 该司为商业/工业承包商，配电级最对口<br>② **E541626**（POWER 变）—— ⚠️ 仅在其「应急供电恢复」场景明确涉及主变时使用<br>③ 公司介绍 | 属「可能触及但未明示」类 ⇒ 优先配电级 |
| **切入角度提示**（**仅提示，不代拟文案**）| ① 官网明列 *"**emergency power restoration**"* 与 *"**new line construction**"* ⇒ **两个最可能触及变压器的场景**<br>② 客户含 **PWGSC / DND / 医院 / 大学** ⇒ **联邦与机构项目渠道** | 官网 company-overview 页（一手）|
| 🔴 **安全提示** | **官网疑似被挂马** ⇒ **若对方回信，须核验发信源真实性**（见上 §二）| 实测 |
| ⛔ **禁止事项** | ① 不得称其「做变压器/高压」（官网无表述，H1）；② **不得向 earlcarrelectriccanada.com 投递**；③ 首封不报交期/价格（红线）| — |

---

## 四、⚠️ 矛盾点与风险提示

| # | 风险 | 说明 |
|---|---|---|
| 1 | 🔴 **官网疑似被挂马** | 正文被注入赌博外链（rhino/karamba/janusz/beep beep casino）⇒ 回信须核验发信源真实性 |
| 2 | 🔴 **网站域被 Proofpoint ARS 拦住** | `earlcarrelectriccanada.com` 探测「转发式 250」⇒ **不可投递，须投 `ececl.ca`** |
| 3 | ⚠️ **Doug Vandemheen 职务口径冲突** | 官网 *Director of Construction* vs LinkedIn *Owner* ⇒ 正文勿强调职称，直呼姓名 |
| 4 | ⚠️ **主送为角色邮箱** | H6：已附具名联系人 + 电话作为第二触达 ⇒ 满足「B 档电话+点名」|
| 5 | ⚠️ **业务对口度弱** | 官网无变压器/高压表述；仅 "new line construction" / "emergency power restoration" 两处泛化触点 |
| 6 | 🔴 **两域均未配 DMARC** | 可被冒用 ⇒ 防钓鱼 |
| 7 | ⚠️ **三域并存易混淆** | `earlcarrelectriccanada.com`（网站）/ `ececl.ca`（邮箱）/ `ececl`（简称）|
| 8 | ⚠️ **官网无 President/Owner 头衔** | 团队页仅 Director of Construction / Operations / Project Coordinator ⇒ 领导层头衔体系不清晰 |

---

## 五、信息缺口清单（请勿编造）

| 缺口 | 状态 |
|---|---|
| **具名邮箱** | ⛔ 未获取 |
| **注册号 / 注册信息** | ⛔ 未获取 |
| **员工数 / 营收** | ⛔ 未获取（团队页仅列 3 人）|
| **官方 President/Owner 头衔** | ⛔ 官网未列 |
| **变压器 / 高压项目证据** | ⛔ 未获取 |
| **Jacques Gauthier（第三方所列）** | ⚠️ 官网无此人 ⇒ 不采信 |
| **公司 LinkedIn 页** | ⛔ 未定位 |

---

## 六、一句话画像

**渥太华西部 Carp 的商业/工业电气承包商，1978 年成立（47 年），客户含 PWGSC、DND、
渥太华医院、Carleton 与渥太华两所大学、Loblaws——联邦与机构项目渠道稳固；
曾 3 次获 R.H. Carroll 安全奖。邮箱 `reception@ececl.ca` 经 SMTP 三点对照实证有效，
可点名 Doug Vandemheen（⚠️ 职称口径冲突）。⚠️ 官网疑似被挂马，回信须核验发信源。**

---

## 七、渠道覆盖清单

| 渠道 | 状态 | 备注 |
|---|---|---|
| 官网（首页/company-overview/our-team/contact） | ✅ 已抓取 | 一手 |
| 官网首页明文（地址/电话/成立年份） | ✅ 已获取 | 120 Walgreen Road Unit 3, Carp, ON K0A 1L0 / 613.831.9179 |
| 官网 Our Team 页 | ✅ 已抓取 | Doug Vandemheen / Janelle Vandemheen / Laura Scott |
| 官网 client 列表 | ✅ 已抓取 | PWGSC/DND/医院/两校/Loblaws/OCDSB/ZIBI |
| LinkedIn 个人页（Doug Vandemheen） | ⚠️ 仅摘要可见 | 撞 authwall |
| DNS（两域 MX/SPF/DMARC） | ✅ 已实测 | Proofpoint ARS + M365 |
| SMTP 探测（控制组协议） | ⚠️ 部分有效 | `ececl.ca` 随机 550 / reception@ 250；ARS 域无效 |
| 第三方（allbiz） | ⚠️ 已参考 | Jacques Gauthier（不采信）|

---

## 八、合规自查（H1–H7）

| 规则 | 自查结果 |
|---|---|
| **H1 不虚构** | ✅ 注册信息标「未获取」；规模「未获取」；**职务冲突如实双向标注**；明确「不得推断其采购变压器」；家族企业标为推断 |
| **H2 不臆造邮箱** | ✅ 只用官网明文 `reception@ececl.ca`；**明确禁用 ARS 域任何地址** |
| **H3 格式校验 + ≥1 交叉来源** | ✅ 格式合法 + 官网明文 + SMTP 三点对照 |
| **H4 标注验证状态** | ✅ 完整给出两域探测矩阵；**职务冲突按「官网优先 + 禁止强调职称」处置** |
| **H5 交叉验证需 ≥1 第一方** | ✅ **第一方 = 官网 Our Team 页**（Doug Vandemheen + Director of Construction）|
| **H6 角色邮箱不得单独交付** | ✅ 已附**具名联系人（Doug Vandemheen）+ 电话** 作为第二触达 ⇒ 满足「B 档电话+点名」|
| **H7 落盘 .md** | ✅ 本文件 |

---

## 九、给下一环节的交付说明

**可直接使用的成果：**
1. 主送邮箱 **`reception@ececl.ca`**（SMTP 三点对照已验证）+ 电话 **613.831.9179**
2. 可点名联系人 **Doug Vandemheen**（⚠️ 职称口径冲突，**勿在正文强调**）
3. **公司公开业务事实**：Carp（渥太华西郊）电气承包商；1978 年成立（47 年）；商业/工业电气；
   **能力含 "new line construction" 与 "emergency power restoration"**、design-build、配电/火警/照明/维护；
   **3 次获 R.H. Carroll 安全奖**（2001/2009/2010）；
   客户含 **PWGSC / DND / 渥太华医院 / Carleton 大学 / 渥太华大学 / Loblaws / OCDSB / ZIBI**
4. 团队另两人：**Janelle Vandemheen（Operations）**、**Laura Scott（Project Coordinator）**
5. 地址 **120 Walgreen Road (Unit 3), Carp, ON K0A 1L0**

**必须知悉的风险：**
1. 🔴 **官网疑似被挂马**（正文被注入赌博外链）⇒ **回信须核验发信源真实性**
2. 🔴 **必须投 `ececl.ca`，勿投 `earlcarrelectriccanada.com`**（后者被 ARS 反垃圾网关拦）
3. ⚠️ **Doug Vandemheen 职务口径冲突**（官网 Director of Construction vs LinkedIn Owner）
4. ⚠️ **业务对口度弱**（官网无变压器/高压表述）
5. 🔴 **两域均未配 DMARC** ⇒ 可被冒用，防钓鱼
6. ⚠️ 三域并存（earlcarrelectriccanada.com / ececl.ca），易混淆

**本环节未做（属其他环节职责）：**
- 未写正文、主题行、开场句、钩子、产品切片（→ 环节 ② 写开发信 agent）
- 未定最终发送时间与时区窗口排程（→ 环节 ③/④ 脚本）
