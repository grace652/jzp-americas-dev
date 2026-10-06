# 【买家 139】开发信交接单 — Hertz Engineering Inc.

> 采集日期：2026-09-28 ｜ 名单来源：`线索资产/目标客户清单.csv` 序号 1（A 类 · 电气承包商/工程公司）
> 采集方：找客户环节（本环节只产出交接单，不写正文/不碰模板/不定话术）
> ⚠️ 本表严格区分「已验证」与「未获取」，未找到的信息一律标注，**不做推断填充**（H1）
> ✅ 一句话结论：**温哥华的电气工程咨询 + 现场服务公司（HV/MV 变电站设计专营）**；
> 🔴 **官网明文自述替客户「选型并采购电力变压器」**（*"specify and procure big pieces of equipment such as
> **power transformers**, circuit breakers and switchgear"*）—— **本批次采购影响力信号最强的一家**；
> ⚠️ **但公司规模仅约 2 人**（RocketReach），须注意其项目体量与决策链；
> 联系人 **Hasan Humayun（Director, P.Eng, PMP）**；邮箱 **`contact@hertzengineering.ca`（官网第一方，B 档）**。

---

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示(如有)
Hertz Engineering Inc. | Hasan Humayun | Director (P.Eng, PMP) | contact@hertzengineering.ca | ✅ 官网第一方明文（角色邮箱）| ca.linkedin.com/in/hasanhumayun（⚠️ 撞 authwall，仅摘要可见）| 温哥华电气工程咨询+现场服务公司；专营 HV/MV 变电站设计（布局/开关柜/接地网/防雷/设备选型）；提供继保与控制设计、电力系统研究、项目管理（含**物料采购**）、设备测试与验收（FAT/SAT）；官网明文替客户选型并采购电力变压器/断路器/开关柜 | 官网实抓（首页/hv-mv-substation-design-services/material-procurement 页）+ RocketReach（Director 职务）+ LinkedIn 摘要 + DNS/SPF/SMTP 控制组法 | ⚠️ 规模极小（约 2 人）；⚠️ 域为未认证来源统一拒绝，SMTP 不可用；⚠️ 无实名邮箱
```

**发信资格：⚠️ 有条件通过**（人对、业务对口、有可用邮箱；缺口在「邮箱为角色邮箱 + 规模小」）
**邮箱档位：B（角色邮箱 · 官网第一方来源 · 非猜测）**

---

## 二、补充信息（扩展段）

### 标准字段明细

| 项 | 内容 | 来源 |
|---|---|---|
| **公司全称** | **Hertz Engineering Inc.** | 官网（一手）|
| **国家 + 城市** | **加拿大 BC 省 Vancouver（温哥华）**；官网自述 *"based in Vancouver, Canada"* | 官网首页（一手）|
| **州省** | **BC ✅**（CSV 填 BC，**正确**）| 官网 |
| **详细地址** | **Suite 700 - 838 West Hastings Street, Vancouver, BC V6C 1C8**（⚠️ 第三方黄页 firmania 所载，**官网未明列地址**）| 第三方（未复核）|
| **电话** | **778-238-8521**（⚠️ 从官网页面源码中提取，**官网页面上未直接展示**）| 官网源码 |
| **注册信息** | ⚠️ **未获取** | — |
| **成立年份** | ⚠️ **未获取**（官网未标注）| — |
| **域名** | hertzengineering.ca（🔴 **未认证来源统一 451，SMTP 探测不可用**）| 探测确认 |
| **邮件网关** | **Microsoft 365 / Exchange Online**（`hertzengineering-ca.mail.protection.outlook.com`）| DNS MX |
| **SPF** | `v=spf1 include:spf.protection.outlook.com -all`（**-all 硬失败**，策略严格）| DNS TXT |
| **DMARC** | ⚠️ **未配置**（`_dmarc.hertzengineering.ca` 无记录）| DNS |
| **网站技术** | **Wix 建站**（源码含 wixpress.com sentry 上报端点）；无独立 Team/About 页 | 源码 |
| **规模** | ⚠️ **约 2 名员工**（RocketReach 自报 "employs 2 employees"）—— **微型公司**，**未经官网证实** | 第三方 |
| **官网** | https://www.hertzengineering.ca | — |

### 🔴 第一发现：官网明文「替客户选型并采购变压器」——采购影响力强

官网 **Material Procurement 页原文**（一手，逐字）：

> *"Hertz Engineering will work with our clients for their material procurement needs. … We work with vendors as client representatives to **specify and procure big pieces of equipment such as power transformers, circuit breakers and switchgear**. Through our **network of approved vendors**, clients can feel comfortable that they are getting the best materials for their projects and on schedule."*

其自述采购流程（一手，逐字）：
> 1. Identify Requirements. 2. **Vendor selection.** 3. **Negotiation and contracting.** 4. Service delivery and performance monitoring. 5. Renewal/contract closure.

官网 **HV/MV Substation Design 页原文**（一手，逐字）：

> *"designing transmission and distribution substations for various utilities and industries"*；服务含
> *"Substation Layout Design / Switchgear Layout Design / Ground Grid Design / Lightning Shield Design /
> **Substation Equipment Specifications and Selection**"*

🔴 **业务含义（供写信环节自行判断，本环节不定话术）**：
- 该公司**以「客户代表」身份替业主选供应商、谈合同、下采购单** —— 属**渠道型影响力节点**，
  而非终端自用采购方。**⇒ 这是本批次 10+ 家中唯一明确写出「procure power transformers」的公司。**
- ⚠️ **但它是顾问角色，不是出资方**：最终采购决策与付款在**其客户（业主/公用事业）**手里。
  **⇒ 不得把它当作最终买方来写**（H1）。

### 联系人（含 still_here 在职核验）

| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| **Hasan Humayun, P.Eng, PMP** | **Director（首封主送）** | ⚠️ **双源一致但均非官网**：<br>① LinkedIn 标题：*"**Director** with expertise in Project …"*<br>② RocketReach：*"currently a **Director** at Hertz Engineering Inc."*；并称其为该公司 management team 成员 | ⚠️ 未知 | **中**：LinkedIn 页存在；2026-01 有 Hertz 招聘帖关联其名 | ⚠️ 未知 | ca.linkedin.com/in/hasanhumayun（⚠️ **撞 authwall，仅摘要可见**）|

> 🔴 **机读结论**：
> 1. **Hasan Humayun 是本单唯一可确认的管理联系人**，职务 *Director*（LinkedIn + RocketReach 两源一致）。
> 2. ⚠️ **但两源均为第三方，官网无团队页、无署名的管理层信息** ⇒ **不满足 H5「交叉验证需 ≥1 第一方来源」**
>    ⇒ **职务标注为「待官网证实」**，且 **⛔ 正文中不得强调其具体职称**，建议**直呼姓名**。
> 3. ⚠️ **公司规模仅约 2 人**（第三方）—— 若属实，则决策链极短（本人即决策者），
>    但也意味着**单项目体量有限**。**该规模数据未经官网证实，仅作风险提示**。
> 4. ⚠️ **无其他公开管理层**（官网无团队页）。

### 邮箱分档（A/B/C）

| 档 | 地址 | 依据 | 可否主送 |
|---|---|---|---|
| **B** | **`contact@hertzengineering.ca`** | **官网源码中明文出现**（一手）；⚠️ 页面正文未直接展示，属**站点内置联系邮箱** | ✅ **可主送**（B 档，角色邮箱）|
| A | ⚠️ **未获取**（无实名邮箱）| 域 SMTP 不可用 + 官网无实名邮箱 | — |
| C | `h.humayun@` / `hasan@` / `hhumayun@` 等 | ⚠️ **全部未验证** —— 域为「未认证来源统一拒绝」，**任何地址都测不出真假** | ⛔ **禁用**（H2）|

**🔴 邮箱验证方法与证据链（可复现）：**

```
域名 hertzengineering.ca
MX   = hertzengineering-ca.mail.protection.outlook.com   （M365 / Exchange Online）
SPF  = v=spf1 include:spf.protection.outlook.com -all    （-all 硬失败）
DMARC= ⚠️ 无记录

SMTP RCPT 探测：
  451 4.4.4  zzz_nonexistent_probe_9987@hertzengineering.ca
  451 4.4.4  info@hertzengineering.ca
  ⇒ 原文： "4.4.4 Mail received as unauthenticated, incoming to a recipient domain
            configured in a host..."（消息截断）
⇒ 🔴 判定：该租户配置为【对未认证来源统一拒绝】—— 4xx 临时拒绝，未透露任何目录信息。
   ⇒ 随机地址与候选地址【返回同一结果】⇒ 探测【完全无效】。
   ⇒ 属「网关行为令 SMTP 失效」的第 ② 类（对未授权来源统一拒）。
   【本单】不依赖 SMTP：contact@ 的可信度来自【官网第一方源码明文】。
```

> ⚠️ **连带影响**：**任何 `hasan@` / `h.humayun@` 类地址都无法被验证或证伪** ⇒
> **⛔ 严禁推测具名邮箱**（H2）。本单**只能以 B 档角色邮箱投递**。

### ⚠️ 联系方式冲突：Hertz 有「极简站」特征

官网为 **Wix 极简站**：无 About/Team/Contact 独立页（均为 404），首页即全部内容。
**⇒ 该公司对外披露极少 → 这也是「约 2 人」判断的间接佐证。**

---

## 三、开发信建议（**仅限：收件人 / 时机 / 附件 —— 不含正文、不含主题行、不含开场句**）

> 依分工铁律：**措辞/钩子/产品切片/主题行全部归环节 ②（写开发信 agent）**。本节只给**收件人与时机**层面的建议。

| 项 | 建议 | 依据 |
|---|---|---|
| **主送** | `contact@hertzengineering.ca` | 官网第一方，B 档；⚠️ 具名邮箱无法验证 |
| **称呼** | ⚠️ 若正文需称呼人：用 **Hasan Humayun**，**不写职称**（职务仅第三方来源）| 见上 §二 |
| **抄送** | ⛔ **不建议**（无第二个可靠地址）| — |
| **建议时机** | **美西工作日 09:00–11:00**（Vancouver = America/Vancouver / PT）| 工程咨询公司上午处理事务 |
| **建议附件** | ① **E541626**（三相液浸 POWER 变，750–110,000 kVA / 72–121 kV）—— **对应其变电站设计与设备选型业务**<br>② **E541627**（配电变，45–5,000 kVA）—— 备用<br>③ 公司介绍 | 选型类客户对**证书与规格**敏感度最高 |
| **切入角度提示**（**仅提示，不代拟文案**）| 官网自述 *"network of approved vendors"* + *"Vendor selection"* —— **该公司已有一套「合格供应商库」**。<br>⇒ 目标应是**进入其 vendor list**，而非直接谈单 | 官网 material-procurement 页（一手）|
| ⚠️ **定位提醒** | 该公司是**客户代表/顾问**，**不是出资买方** —— 材料应面向「**作为供应商资格**」而非「报价成交」| 见上 §二 |
| ⛔ **禁止事项** | ① 不得假设其为最终买方；② 不得因其「procure power transformers」就报价格/交期（红线：首封不报交期/价格）；③ 不得提其规模 | — |

---

## 四、合规自查（H1–H7）

| 规则 | 自查结果 |
|---|---|
| **H1 不虚构** | ✅ 地址标为「第三方未复核」；员工数标为「第三方未证实」；职务标注「待官网证实」；电话标注「取自源码，页面未直接展示」 |
| **H2 不臆造邮箱** | ✅ **只用官网源码明文的 `contact@`**；`hasan@` 类**已明确禁用**并说明域不可验证的原因 |
| **H3 格式校验 + ≥1 交叉来源** | ⚠️ 邮箱格式合法；**但具名邮箱无来源**，故只交 B 档角色邮箱（如实标注）|
| **H4 标注验证状态** | ✅ 明确写「官网第一方来源（非 SMTP 验证，因域 451）」；**未混称已验证** |
| **H5 交叉验证需 ≥1 第一方** | ⚠️ **职务信息不满足**（两源均第三方）→ **已降级标注，并禁止在正文强调职称** |
| **H6 角色邮箱不得单独交付** | ✅ **本单在交接单中明确标注 B 档 + 说明原因**，并给出电话作为第二触达路径（见下）|
| **H7 落盘 .md** | ✅ 本文件 |

> 📌 **关于 H6 的处置说明**：H6 要求「角色邮箱不得**单独**交付」。本单已附
> **第二触达路径**：电话 **778-238-8521** + 具名联系人 **Hasan Humayun（Director）** 可点名。
> ⇒ **满足「B 档电话 + 点名」的合格线**（任务交接书 §4.4）。

---

## 五、给下一环节的交付说明

**可直接使用的成果：**
1. 主送邮箱 **`contact@hertzengineering.ca`**（官网第一方，B 档）+ 第二触达 电话 **778-238-8521**
2. 可点名联系人 **Hasan Humayun**（Director, P.Eng, PMP）—— ⚠️ 职称勿在正文强调
3. **公司公开业务事实**：温哥华 HV/MV 变电站设计专营；替客户**选型并采购变压器/断路器/开关柜**；
   有 *"network of approved vendors"*；服务含 FAT/SAT 验收测试、继保设计、电力系统研究

**必须知悉的风险：**
1. 🔴 **它是顾问/客户代表，不是出资买方** —— 目标是进入其合格供应商库
2. ⚠️ **具名邮箱无法验证**（域对未认证来源统一 451）⇒ 无法预验证，也不可推测
3. ⚠️ **规模约 2 人**（第三方，未证实）⇒ 单项目体量可能有限
4. ⚠️ 公司无独立 About/Team 页，对外披露极少
5. 🔴 **域未配 DMARC** ⇒ 该域可被冒用，**若收到该域来信需谨慎核验**（防钓鱼）

**本环节未做（属其他环节职责）：**
- 未写正文、主题行、开场句、钩子、产品切片（→ 环节 ② 写开发信 agent）
- 未定最终发送时间与时区窗口排程（→ 环节 ③/④ 脚本）
