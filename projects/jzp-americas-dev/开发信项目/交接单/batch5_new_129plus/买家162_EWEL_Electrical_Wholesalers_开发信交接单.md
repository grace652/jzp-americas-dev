# 【买家 162】开发信交接单 — EWEL Electrical Wholesalers Edmonton

> 采集日期：2026-09-28 ｜ 名单来源：`线索资产/目标客户清单.csv` 序号 33（B 类 · 分销商/贸易商）
> 采集方：找客户环节（本环节只产出交接单，不写正文/不碰模板/不定话术）
> ⚠️ 本表严格区分「已验证」与「未获取」，未找到的信息一律标注，**不做推断填充**（H1）
> ✅ 一句话结论：**埃德蒙顿（Edmonton）本地电气批发商（EWEL = Electrical Wholesalers Edmonton），
> 服务住宅/机构/工业三大板块，自 1988 年起为 Alberta Electrical Alliance 会员；
> 🎯 **具名/角色邮箱 `sales@ewel.ca` SMTP 实证通过**（控制随机 550 / `info@` 550）；
> ⚠️ **`info@ewel.ca` 与 `orders@ewel.ca` 实测均 550（不存在）** ⇒ 仅 `sales@` 一条可用；
> 公司至今**未定位任何具名联系人**；
> ⓪ 反身排除判定：**批发分销商，非制造商 ⇒ 通过**。

---

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示(如有)
EWEL (Electrical Wholesalers Edmonton) | ⛔ 未获取 | ⛔ 未获取 | sales@ewel.ca | ✅ SMTP 实证（随机 550 / info@ 550 / sales@ 250）| ⛔ 未定位 | 加拿大 AB 省 Edmonton（埃德蒙顿）本地电气批发商，主址 11604 186 Street NW；服务 residential / institutional / industrial 三大板块；自 1988 年起为 Alberta Electrical Alliance 会员；产品线覆盖配电设备（Distribution Equipment）、工业控制与自动化、线缆、照明、导管与配件、数据通信等；仅向 AB 省内发货 | 官网首页/Contact 页（一手）+ Alberta Electrical Alliance（一手）+ DNS/MX + SMTP 控制地址探测 | ⚠️ 官网邮箱经 Cloudflare 混淆，未直接读出；⚠️ 未明列变压器采购；仅限 AB 省内发货
```

**发信资格：🟡 部分通过**（**有可用角色邮箱 `sales@ewel.ca` 且实证**，但**无具名联系人**）
**邮箱档位：B（角色邮箱 `sales@`，SMTP 实证通过）**

---

## 二、补充信息（扩展段）

### 标准字段明细

| 项 | 内容 | 来源 |
|---|---|---|
| **公司全称** | **EWEL (Electrical Wholesalers Edmonton)** | 官网（一手）|
| **国家 + 城市** | **加拿大 AB 省 Edmonton（埃德蒙顿）** | 官网 Contact 页（一手）|
| **州省** | **AB ✅**（CSV 填 AB，**正确**）| — |
| **详细地址** | **11604 186 Street NW, Edmonton, AB T5S 0C4** | 官网 Contact 页（一手）|
| **电话** | **780.451.2311**（官网 `tel:` 实证）；另有 **780.701.3482**（仅见于链接，未见于正文）| 官网（一手）|
| **邮箱** | **`sales@ewel.ca`**（SMTP 实证 250）；⚠️ 官网邮箱经 **Cloudflare 混淆**未直接读出 | SMTP + 官网（一手）|
| **域名** | **ewel.ca** | — |
| **邮件网关** | **Microsoft Exchange Online**（`ewel-ca.mail.protection.outlook.com`）| DNS MX |
| **SPF / DMARC** | DMARC **`p=quarantine`**（含 uriports.com 报告）| DNS TXT |
| **成立年份** | ⚠️ **官网未明示**；自 **1988 年**起为 Alberta Electrical Alliance 会员 | 官网（一手）|
| **规模** | ⛔ 员工数未获取；官网另有 `/store-locations`（多店，未逐一取）| — |
| **官网** | https://www.ewel.ca | — |
| **🚚 销售范围** | 🔴 **官网明示 *"We ship within Alberta only."*** | 官网（一手）|

### 业务定位（官网一手，逐字）

官网页脚（一手）：
> *"**EWEL is an Edmonton operated electrical wholesaler** serving **residential, institutional,
> and industrial** sectors."*
> *"Proud Member of **Alberta Electrical Alliance** since **1988**"*
> *"🔴 **We ship within Alberta only.**"*

官网产品目录分类（一手，逐字）：
> *Alarms & Signalling; Fuses & Accessories; Connectors & Fittings; Conduits & Fittings;
> Conduit & Cable Accessories; **Distribution Equipment**; Electrical Boxes; Electrical Enclosures;
> Electrical Tools & Hardware; Heating & Ventilation; **Industrial Control & Automation**;
> Industrial Supply; Lighting; Raceway / Cable Tray / Channel Strut; Wire & Cable;
> Data Communication and Networking; Wiring Devices & Telecom; Safety.*

✅ **品类验证**：官网产品线含 **"Distribution Equipment"（配电设备）** ⇒ **配电变属其常规品类范畴内**。

⚠️ 官网 Contact 页**未列任何具名人员**。

### ⓪ 反身排除判定（本环节强制首层）

| 检查项 | 结论 |
|---|---|
| 官网是否自称 manufacture / 制造 | ❌ **无**（自称 *"electrical wholesaler"*）|
| 是否有自有品牌变压器规格书 | ❌ 无 |
| 是否销售自有品牌变压器 | ❌ 无 |
| 定性 | ✅ **电气批发分销商 ⇒ 非制造商 ⇒ 通过 ⓪ 层** |

### 联系人（含仍_here 在职核验）

| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| ⛔ **未获取任何具名联系人** | — | — | — | — | — | — |

> 🔴 **机读结论**：本单**核心缺口 = 人**。官网 Contact 页**无具名人员**，
> 邮箱经 Cloudflare 混淆。⇒ 需经电话 **780.451.2311** 或 LinkedIn 补人。

### 邮箱分档（A/B/C）

| 档 | 地址 | 依据 | 可否主送 |
|---|---|---|---|
| A | ⛔ 未获取 | — | — |
| **B** | **`sales@ewel.ca`** | **SMTP 控制地址协议实证（250）；随机地址 550** | ✅ **主送**（⚠️ 无具名人，以角色称呼）|
| C | `info@ewel.ca` | 🔴 **实测 550（不存在）** | ⛔ **禁止使用**（H2）|
| C | `orders@ewel.ca` | 🔴 **实测 550（不存在）** | ⛔ **禁止使用**（H2）|

**🔴 邮箱验证方法与证据链（可复现）：**

```
域名 ewel.ca
MX   = ewel-ca.mail.protection.outlook.com   （Microsoft Exchange Online）
SMTP 控制地址协议（HELO jiezougroup.com）：
  RCPT zzq9k2x7@ewel.ca   -> 550 5.4.1 Access denied   （控制地址：随机地址，正确拒绝）
  RCPT info@ewel.ca       -> 550 5.4.1 Access denied   ← 【反证】info@ 不存在
  RCPT orders@ewel.ca     -> 550 5.4.1 Access denied   ← 【反证】orders@ 不存在
  RCPT sales@ewel.ca      -> 250 2.1.5 Recipient OK    （候选：命中）
⇒ ✅ 随机 550 + 候选 250 ⇒ 判定【真实名册，非 catch-all】。
   ⚠️ 但注意：本域【未取得官网明确列出的「控制地址 A」】
   （官网邮箱被 Cloudflare 混淆）⇒ 控制协议中「控制 A」一栏缺失。
   已用「随机 550 + 两处反证 550」替代，判别力仍成立。
```

---

## 三、开发信建议（**仅限：收件人 / 时机 / 附件 —— 不含正文、不含主题行、不含开场句**）

| 项 | 建议 | 依据 |
|---|---|---|
| **主送** | **`sales@ewel.ca`** | B 档唯一可用地址，SMTP 实证 |
| **正文处理** | ⚠️ **无具名联系人** ⇒ 建议以**公司/销售部门层面**称呼，**不得虚构人名** | H1/H2 |
| **补齐路径** | ① 电话 **780.451.2311** 索取采购/经理姓名<br>② 官网 `/store-locations` 查各店负责人<br>③ LinkedIn 搜 EWEL 员工 | 本环节渠道清单 |
| **建议时机** | **山地时间（MT）工作日 08:30–10:30**（Edmonton = America/Edmonton）| — |
| **建议附件** | ① UL 证书 **E541627**（三相液浸配电变 45–5,000 kVA）<br>② 公司介绍<br>🟡 E541626（电力变）可备选 | 加拿大客户 ⇒ 配电级为主 |
| **切入角度提示**（**仅提示，不代拟文案**）| ① 该司产品线含 **"Distribution Equipment"** 与 **"Industrial Control & Automation"** ⇒ **配电变在其品类范围内**<br>② 服务 **residential / institutional / industrial** 三板块 ⇒ **客群广、走量为主**<br>③ 1988 年起为 **Alberta Electrical Alliance 会员** ⇒ **老牌本地渠道，重视稳定供货**<br>④ 🔴 **仅向 AB 省内发货** ⇒ 若我方货物需入其仓，须走**其自有进口/清关**路径，**物流环节需提前确认** | 官网（一手）|
| ⛔ **禁止事项** | ① 不得称 certified（柱上变 E544629 仅 ECD 计划函）<br>② 不得提 YAWEI<br>③ 首封不报交期/价格<br>④ **不得使用 `info@ewel.ca` / `orders@ewel.ca`**（实测均不存在）<br>⑤ **不得虚构联系人姓名**<br>⑥ **不得声称该公司自产变压器**<br>⑦ 不得发送供货记录 PDF | — |

---

## 四、⚠️ 矛盾点与风险提示

| # | 风险 | 说明 |
|---|---|---|
| 1 | 🔴 **仅向 AB 省内发货** | 官网逐字 *"We ship within Alberta only"* ⇒ **若我方以「寄样/寄资料」方式触达，物流路径受限** |
| 2 | ⚠️ **`info@` 与 `orders@` 均不存在（550）** | 多家公司惯例有 info@/orders@，本域没有 ⇒ 勿套用 |
| 3 | ⚠️ **无具名联系人** | 官网 Contact 页无人员 |
| 4 | ⚠️ **官网邮箱 Cloudflare 混淆** | 无法读出官网明文邮箱 ⇒ 未能建立「控制地址 A」 |
| 5 | ⚠️ **成立年份未明示** | 仅有 1988 年行业协会会员起始年 |
| 6 | ⚠️ **未定位多店架构** | 官网有 `/store-locations`，未逐一抓取 |

---

## 五、信息缺口清单（请勿编造）

| 缺口 | 状态 |
|---|---|
| **具名联系人 / 职位** | ⛔ **未获取**（本单核心缺口）|
| **官网明文邮箱** | ⛔ 未读出（Cloudflare 混淆）|
| **成立年份 / 员工数 / 注册号** | ⛔ 未获取 |
| **分店清单** | 🟡 官网有页面，未抓取 |
| **变压器采购证据** | ⛔ 未获取（品类含 Distribution Equipment，属推断）|
| **决策人 LinkedIn** | ⛔ 未定位 |

---

## 六、一句话画像

**埃德蒙顿本地电气批发商（EWEL = Electrical Wholesalers Edmonton），主址 11604 186 Street NW，
服务住宅/机构/工业三大板块，产品线含 Distribution Equipment 与工业控制自动化，
自 1988 年起为 Alberta Electrical Alliance 会员，⚠️ **仅向 AB 省内发货**。
🎯 角色邮箱 **`sales@ewel.ca` 已 SMTP 实证**（随机 550 / `info@` 550 / `sales@` 250）；
🔴 **`info@ewel.ca` 与 `orders@ewel.ca` 实测均不存在**。
⚠️ **官网 Contact 页无具名人员、邮箱经 Cloudflare 混淆** ⇒ 需先经电话（780.451.2311）补人。
⓪ 层判定：电气批发分销商，非制造商 ⇒ 通过。加拿大客户 ⇒ 配电级 E541627 为主。**

---

## 七、渠道覆盖清单

| 渠道 | 状态 |
|---|---|
| **L-1 锁人** | ⛔ **未获取任何具名联系人** |
| **L0 官网** | ✅ 首页 + Contact 页抓取；拿到地址、电话、品类、发货范围；⚠️ 邮箱混淆、无人员 |
| **L1 政府一手** | ⛔ 未查 |
| **L2 命名+DNS** | ✅ 域名存活（M365，DMARC `p=quarantine`）；✅ **SMTP 实证（含 info@/orders@ 双反证）** |
| **L3 B2B 库** | 🟡 firmania.ca / alberta-local.ca / infobel.ca（未采信）|
| **L4 社媒协会** | ✅ **Alberta Electrical Alliance**（1988 起会员）|
| **L5 黄页同址** | 🟡 多处目录条目一致（11604 186 St NW）|
| **L6 电话表单** | ✅ 780.451.2311 |
| **L7 付费** | ⛔ 未启用 |
