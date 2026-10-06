# 【买家 155】开发信交接单 — Trotter & Morton Group of Companies（TMGOC）

> 采集日期：2026-09-28 ｜ 名单来源：`线索资产/目标客户清单.csv` 序号 25（A 类 · 电气承包商/工程公司）
> 采集方：找客户环节（本环节只产出交接单，不写正文/不碰模板/不定话术）
> ⚠️ 本表严格区分「已验证」与「未获取」，未找到的信息一律标注，**不做推断填充**（H1）
> ✅ 一句话结论：**卡尔加里的多工种建筑服务集团，1927 年成立（98 年）**；
> 🔴 **旗下 9 家子公司**，含 **Centec Electric & Controls**（工业电气）、**Draw Energy**（电气与仪表）、
> **Fred Welsh**（机电）、**Bow River Paving**、**Rambler Fabrication**、**Whaler**（油气总包）；
> 业务覆盖 **加美 6 城**（Vancouver / Calgary / Winnipeg / Kelowna / Seattle / San Antonio / Wilsonville）；
> **2026 年加拿大最佳管理公司白金会员**；
> 🔴 **两个具名邮箱 SMTP 三点对照干净命中（A 档）**：
> **`dryan@tmlgroup.com`（David Ryan, CEO）**／**`cmaclellan@tmlgroup.com`（Craig Maclellan, COO）**；
> 团队页另有 CFO **Steve Salt**。
> ⚠️ **变压器信号弱**：官网无任何变压器/高压表述。

---

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示(如有)
Trotter & Morton Group of Companies | David Ryan（CEO）／ Craig Maclellan（COO，电气背景更对口）| CEO ／ Chief Operating Officer | dryan@tmlgroup.com ／ cmaclellan@tmlgroup.com | ✅ 已验证（A 档 · SMTP 控制组法三点对照，两个具名邮箱均命中）| ⚠️ 未获取（LinkedIn 个人页仅摘要）| 卡尔加里多工种建筑服务集团，1927 年起家于水暖，现覆盖加美 6 城；旗下 9 家子公司（含 Centec Electric & Controls / Draw Energy / Fred Welsh / Bow River Paving / Rambler / Whaler / Industrial Contracting / Building Technologies / Facility Services）；业务含商业/机构/市政建筑、工业（含油气）机电总承包、设施服务（LINC Service）、沥青、制造；2026 加拿大最佳管理公司白金会员；累计 2000+ 项目、110 万工时 | 官网实抓（首页/our-company/leadership/contact-us 页）+ LinkedIn（Craig Maclellan 2026-05 活跃帖）+ DNS/SMTP 控制组法多格式探测 | ⚠️ 变压器信号弱（无高压/变压器表述）；⚠️ 集团结构复杂（9 子公司，采购可能分散）；⚠️ 邮箱域为 tmlgroup.com（非官网域 trotterandmorton.com）
```

**发信资格：✅ 通过**（具名联系人 + 已验证邮箱 + 企业规模明确）
**邮箱档位：A（具名联系人 · SMTP 已验证 · 非 catch-all 域）**

---

## 二、补充信息（扩展段）

### 标准字段明细

| 项 | 内容 | 来源 |
|---|---|---|
| **公司全称** | **Trotter & Morton Group of Companies**（简称 **TMGOC**，官网自用；亦见 *"TML Group"* 品牌）| 官网（一手）|
| **国家 + 城市** | 🇨🇦 **加拿大 AB 省 Calgary（卡尔加里）** —— 总部；另在 **Vancouver / Winnipeg / Kelowna（加）** 与 **Seattle / San Antonio / Wilsonville / Eugene / Lacey / Longview（美）** 设点 | 官网 Contact 页（一手）|
| **州省** | **AB ✅**（CSV 填 AB，**正确**）| 官网 |
| **详细地址** | **5723 1 Street SE, Calgary, AB T2H 1H9**（🟢 官网 Contact 页明文，**Corporate Mailing Address 与 Main Office 一致**）| 官网（一手）|
| **电话** | **403-255-7535** ／ **403-640-0767**（传真或第二线路，🟢 官网明文）| 官网（一手）|
| **邮箱** | 🟢 **官网 Contact 页明文列出多个部门/子公司邮箱**（域为 **`tmlgroup.com`**，**非官网域**）：<br>`t_m@tmlgroup.com`（主邮箱）／ `whaler@`／`dispatch@`／`rambler@`／`solar@`／`tmic@`（温尼伯工业）／`vanservice@`／`vanmechestimating@` | 官网（一手）|
| **注册信息** | ⚠️ **未获取** | — |
| **成立年份** | **1927**（🟢 官网首页明文：*"Bringing Buildings to Life **Since 1927**"*；*"In **1927**, Trotter & Morton began its journey as a **plumbing and heating company**"*）| 官网（一手）|
| **域名** | 🔴 **两个域**：<br>① `trotterandmorton.com`（**官网域**）<br>② **`tmlgroup.com`（邮箱域 —— 官网 Contact 页所列邮箱所在）** | 实测确认 |
| **邮件网关** | **Proofpoint Essentials**（`mx1-us1.ppe-hosted.com` / `mx2-us1.ppe-hosted.com`）| DNS MX |
| **SPF** | `v=spf1 include:sendgrid.net a:dispatch-us.ppe-hosted.com -all`（**-all 硬失败**；含 SendGrid）| DNS TXT |
| **DMARC** | 🔴 **`v=DMARC1; p=reject; adkim=s; aspf=s;`** —— **最严格配置**（拒收 + **严格对齐**）| DNS TXT |
| **企业荣誉** | **2026 加拿大最佳管理公司白金会员**（Canada's Best Managed Companies Platinum）；**2025 亦为白金会员** | 官网（一手）|
| **规模** | **累计 2,000+ 项目（2020 年）**；**110 万工时**；**100+ 客户 / 1,000+ 项目**（官网首页）；设施服务 2020 年 **32 万工时**、**15M 平方英尺**、**10,000+ 客户**、**1,800+ 服务协议**；⚠️ 员工总数未获取 | 官网（一手）|
| **官网** | https://trotterandmorton.com | — |

> 📌 **集团结构**（官网首页「Our Group of Companies」原文，一手，9 家）：
> **Bow River Paving**（沥青，1991）/ **Trotter & Morton Building Technologies**（电气/数据/安防/机械/钣金）/
> **Facility Services** / **Industrial Contracting** / **Rambler Fabrication**（管道制造与焊接）/
> **Whaler Industrial Contracting**（油气总包，15 年）/ **Centec Electric & Controls**（**工业电气，Brandon MB，2000 年起，ISO 9001:2015**）/
> **Fred Welsh Mechanical**（Coquitlam BC 机械）/ **Draw Energy**（**电气与仪表，卡尔加里，20+ 年**）

### ⚠️ 第一判断：业务对口度偏弱（须如实标注）

官网**通篇未见**「变压器」「变电站」「高压」表述。其自我定位为：

> *"Bringing Buildings to Life Since 1927"*；*"From the initial planning stages to ongoing maintenance,
> we've got the whole building covered."*（官网首页，一手）

四大业务板块（官网首页，一手）：
> *Commercial（商业/机构/市政建筑、沥青、太阳能）/ Industrial（**general, mechanical and electrical
> construction and maintenance services as well as civil projects for the oil and gas industry in Western Canada**）/
> Facility Services（LINC Service 品牌）/ 集团子公司*

🔴 **业务含义（供写信环节自行判断，本环节不定话术）**：
- ⚠️ **无变压器/高压证据** ⇒ **不得推断其采购变压器**（H1）。
- ✅ **但三个正向信号**：
  1. **Industrial 板块明述 "mechanical and **electrical** construction"**，服务**油气行业**（Western Canada）
     —— 油气项目有配电与备用电源需求。
  2. **子公司 Centec Electric & Controls**（工业电气，ISO 9001:2015）与 **Draw Energy**（电气与仪表）
     ⇒ **集团内有专业电气实体**，可能对接电气设备。
  3. **Fred Welsh** 的服务范围含 *"covering **electrical**, plumbing and refrigeration systems"*。
- ⚠️ **集团结构复杂（9 家子公司，跨加美 6 城）** ⇒ **采购可能分散在各子公司**，
  **总部层面（CEO/COO）未必直接管电气设备采购**。
- ⚠️ **⇒ 归入「可能触及但未明示」类**。

### 联系人（含 still_here 在职核验）

官网 **Leadership 页**（一手，逐字）：

| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| **Craig Maclellan** | 🔴 **Chief Operating Officer（首选 —— 电气背景最对口）** | 🟢 **官网明文**：*"**Craig Maclellan** — **Chief Operating Officer**"*；描述逐字：*"As Chief Operating Officer, Craig is responsible for **the construction operations** of the Trotter & Morton Group of Companies. Craig has been with the company **since 2009**, beginning his journey as an **Electrical Project Manager / Estimator**. … he provides leadership to several of Trotter & Morton's business units including **Electrical**, Mechanical, Bow River Paving, Industrial Services, Rambler, and Whaler. Prior to joining Trotter & Morton, Craig spent **12 years with Raffin Electric**…"* | **2009 至今（16 年）**；电气行业经验更长 | ✅ **高**：**LinkedIn 2026-05 发帖**（关于公司获 2026 白金奖）；官网领导层页在列 | **低**（COO 级，16 年司龄）| ca.linkedin.com/in/craig-maclellan-b5a49692（仅摘要）|
| **David Ryan** | **CEO（业主级备选）** | 🟢 **官网明文**：*"**David Ryan** — **CEO**"*；描述逐字：*"provides executive oversight to all operating divisions. He has been with Trotter and Morton for **over 25 years**…"*；*"holds a Bachelor of Arts Degree from the University of Calgary, as well as a **Red Seal ticket**… as a **Journeyman Steam Fitter / Gas Fitter**"* | **25 年+** | **高**：官网领导层页在列 | **低**（CEO 级，25 年司龄）| ca.linkedin.com/in/david-ryan-09116a65（仅摘要）|
| **Steve Salt** | **Chief Financial Officer** | 🟢 官网明文；*"has been with the company **since 2009**… Prior to joining, Steve spent 5 years with **PricewaterhouseCoopers** in Calgary"*；负责 HR/IT/Admin 共享服务 | 2009 至今（16 年）| 高：官网领导层页在列 | ⚠️ 未知 | ⚠️ 未获取 |

> 🔴 **机读结论**：
> 1. 🔴 **Craig Maclellan（COO）是首选** —— 理由：
>    ① **官网明文其"起点是 Electrical Project Manager / Estimator"**（**电气专业背景**）；
>    ② **负责集团施工运营 + 分管 Electrical、Industrial Services 等业务单元**；
>    ③ **前 Raffin Electric 12 年**（电气行业深厚）；
>    ④ **2026-05 LinkedIn 发帖活跃**（**在职确认，近期活跃度最高**）。
>    **⇒ 他的职能比 CEO 更接近电气设备采购决策。**
> 2. ✅ **David Ryan（CEO）为业主级备选**，25 年司龄。
> 3. ✅ **三人都满足 H5**（官网 Leadership 页第一方明文）。
> 4. ⚠️ **官网未列采购负责人** ⇒ 采购可能由各子公司自理。

### 邮箱分档（A/B/C）

| 档 | 地址 | 依据 | 可否主送 |
|---|---|---|---|
| **A** | **`cmaclellan@tmlgroup.com`** | ① **SMTP 控制组法三点对照命中**：随机 550 / `t_m@` 250 / `cmaclellan@` 250<br>② 官网 Leadership 页确认 *Craig Maclellan = COO*（**电气背景**）<br>③ **命名规则 `{firstinitial}{last}@` 已双向印证** | ✅ **首选主送** |
| **A** | **`dryan@tmlgroup.com`** | ① **SMTP 控制组法三点对照命中**（同轮同规则）<br>② 官网确认 *David Ryan = CEO* | ✅ **备选主送** |
| B | `t_m@tmlgroup.com` | 🟢 **官网明文**（主邮箱）；✅ SMTP 命中 250 | ⚠️ 第二轮备选 |
| C | `s.salt@` / `steve.salt@` 等 CFO 格式 | ⚠️ **未测**（本轮未测 CFO 格式）⇒ **不可用** | ⛔ 禁用（H2）|

**🔴 邮箱验证方法与证据链（可复现）：**

```
域名 tmlgroup.com（邮箱域 —— 官网 Contact 页所列）
MX   = 10 mx1-us1.ppe-hosted.com / 10 mx2-us1.ppe-hosted.com   （Proofpoint Essentials）
SPF  = v=spf1 include:sendgrid.net a:dispatch-us.ppe-hosted.com -all
DMARC= 🔴 v=DMARC1; p=reject; adkim=s; aspf=s;   （最严格：拒收 + 严格对齐）

SMTP RCPT 探测（控制组协议 + 多格式并行）：
  550 5.1.1  zzz_nonexistent_probe_9987@tmlgroup.com   ← 🔴 随机 550 ⇒ 【非 catch-all】✅
  250 2.1.5  t_m@tmlgroup.com                          ← 🟢 控制组起点 250（官网明文）⇒ 来源未被封 ✅
  ---- David Ryan (CEO) ----
  550  david.ryan@tmlgroup.com                         ← 排除 {first}.{last}@
  250  dryan@tmlgroup.com                              ← 🎯 命中
  ---- Craig Maclellan (COO) ----
  550  craig.maclellan@tmlgroup.com                    ← 排除 {first}.{last}@
  250  cmaclellan@tmlgroup.com                         ← 🎯 命中
  ---- 其他 ----
  550  info@tmlgroup.com                               ← 无此地址
  550  s.salt@tmlgroup.com                             ← （CFO 该格式不存在）
  550  info@trotterandmorton.com                       ← ⚠️ 官网域【不承载邮件】

⇒ 🎯 【命名规则确证为 `{initial}{last}@`】（两个不同的人都符合 ⇒ 规则可靠）
   ⇒ 三点对照齐备 ⇒ A 档成立，【两个具名邮箱均命中】。
```

> ⚠️ **重要提示**：
> 1. **邮箱域是 `tmlgroup.com`，不是官网域 `trotterandmorton.com`**
>    ⇒ **`@trotterandmorton.com` 的任何地址都不可用**（该域无 MX，探测返回 550）。
> 2. 🔴 **该域 DMARC = `p=reject; adkim=s; aspf=s`（最严格 + 严格对齐）**
>    ⇒ **我方发信必须确保 SPF/DKIM 完全合规，否则会被直接拒收**
>    —— **发送环节须特别注意**（本单为本批次 DMARC 最严格的域之一，与买家 149 Shermco 同级）。

---

## 三、开发信建议（**仅限：收件人 / 时机 / 附件 —— 不含正文、不含主题行、不含开场句**）

> 依分工铁律：**措辞/钩子/产品切片/主题行全部归环节 ②（写开发信 agent）**。本节只给**收件人与时机**层面的建议。

| 项 | 建议 | 依据 |
|---|---|---|
| **首选主送** | **`cmaclellan@tmlgroup.com`**（Craig Maclellan，COO）—— **电气背景最对口 + 2026-05 仍活跃** | 见上 §二 |
| **备选主送** | `dryan@tmlgroup.com`（David Ryan，CEO）| 业主级，25 年司龄 |
| **抄送** | ⛔ **不建议首封抄送**（避免高管之间显得乱发）| — |
| **第二触达** | 电话 **403-255-7535** | 官网明文（一手）|
| **建议时机** | **山地时间工作日 08:00–10:00**（Calgary = **America/Edmonton / MT**）| 承包商上午处理事务 |
| **建议附件** | ① **E541627**（三相配电变，45–5,000 kVA）—— 主推<br>② **E541626**（POWER 变）—— 备用（官网无高压证据）<br>③ 公司介绍 | 属「可能触及但未明示」类 ⇒ 配电级起步 |
| **切入角度提示**（**仅提示，不代拟文案**）| ① 🔴 **Craig Maclellan 的公开履历**：**Electrical Project Manager/Estimator 出身** + **分管 Electrical 业务单元** ⇒ **技术对接口**<br>② 集团 **Industrial 板块服务油气行业**（Western Canada）+ 子公司 **Centec Electric & Controls**（工业电气）/ **Draw Energy**（电气与仪表）⇒ 电气实体 | 官网 Leadership 页 + 首页（一手）|
| ⚠️ **定位提醒** | 🔴 **业务对口度弱**（官网无变压器/高压表述）+ **集团采购可能分散**（9 家子公司）<br>⇒ 归入「宽泛触达」 | 见上 §二 |
| 🔴 **发送前置检查** | **该域 DMARC = p=reject + adkim=s + aspf=s（最严）** ⇒ **必须确保我方 SPF/DKIM 合规** | DNS 实测 |
| ⛔ **禁止事项** | ① **勿投 `@trotterandmorton.com`**（该域收不了信）；② 不得称其「做变压器/高压」（无表述，H1）；③ 首封不报交期/价格（红线）；④ 不得推测 CFO 邮箱（未测）| — |

---

## 四、合规自查（H1–H7）

| 规则 | 自查结果 |
|---|---|
| **H1 不虚构** | ✅ 注册信息「未获取」；规模数据逐条标来源与年份；明确标注「变压器信号弱」；**明确指出集团采购可能分散** |
| **H2 不臆造邮箱** | ✅ 两个具名邮箱**均经 SMTP 实测**；**明确禁用未测的 CFO 格式**；**明确指出官网域不可收信** |
| **H3 格式校验 + ≥1 交叉来源** | ✅ 格式合法 + 官网职务 + SMTP 命中（**三重来源**）|
| **H4 标注验证状态** | ✅ 完整给出探测矩阵；**命名规则由两个不同人双向印证** |
| **H5 交叉验证需 ≥1 第一方** | ✅ **第一方 = 官网 Leadership 页**（CEO/CFO/COO 三人明文 + 职务描述）|
| **H6 角色邮箱不得单独交付** | ✅ 主送为**具名邮箱**（两个 A 档）|
| **H7 落盘 .md** | ✅ 本文件 |

---

## 五、给下一环节的交付说明

**可直接使用的成果：**
1. 🔴 **首选联系人 Craig Maclellan（COO）** —— **电气背景最对口**（Electrical PM/Estimator 出身、分管 Electrical 业务单元、
   前 Raffin Electric 12 年、2026-05 LinkedIn 活跃）
   + 邮箱 **`cmaclellan@tmlgroup.com`**（✅ SMTP 三点对照验证）
2. 备选 **David Ryan（CEO）** + 邮箱 **`dryan@tmlgroup.com`**（✅ SMTP 三点对照验证）
3. 第三人 **Steve Salt（CFO）**（⚠️ 邮箱未测）
4. **公司公开业务事实**：卡尔加里多工种建筑服务集团；**1927 年成立（98 年）**；
   **9 家子公司**（Bow River Paving / Building Technologies / Facility Services / Industrial Contracting /
   Rambler / Whaler / **Centec Electric & Controls** / **Fred Welsh** / **Draw Energy**）；
   业务覆盖**加美 6 城**；**2026 加拿大最佳管理公司白金会员**；累计 2,000+ 项目
5. 地址 **5723 1 Street SE, Calgary, AB T2H 1H9** + 电话 **403-255-7535**

**必须知悉的风险：**
1. 🔴 **邮箱域是 `tmlgroup.com`，不是官网域 `trotterandmorton.com`** ⇒ **勿投官网域**
2. 🔴 **该域 DMARC = `p=reject; adkim=s; aspf=s`（最严）** ⇒ **发信须确保 SPF/DKIM 合规**，否则被拒
3. ⚠️ **业务对口度弱**（官网无变压器/高压表述）
4. ⚠️ **集团结构复杂（9 家子公司，加美 6 城）** ⇒ 采购可能分散，总部未必直管电气设备采购
5. ⚠️ 附注：同一邮箱域 `tmlgroup.com` 亦用于其子品牌（TML Group），**带外发信注意署名主体**

**本环节未做（属其他环节职责）：**
- 未写正文、主题行、开场句、钩子、产品切片（→ 环节 ② 写开发信 agent）
- 未定最终发送时间与时区窗口排程（→ 环节 ③/④ 脚本）
