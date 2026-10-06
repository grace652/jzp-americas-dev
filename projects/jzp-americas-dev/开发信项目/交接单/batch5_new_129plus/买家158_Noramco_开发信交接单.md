# 【买家 158】开发信交接单 — Noramco（NoraMco / Wire & Cable Distributor）

> 采集日期：2026-09-28 ｜ 名单来源：`线索资产/目标客户清单.csv` 序号 29（B 类 · 分销商/贸易商）
> 采集方：找客户环节（本环节只产出交接单，不写正文/不碰模板/不定话术）
> ⚠️ 本表严格区分「已验证」与「未获取」，未找到的信息一律标注，**不做推断填充**（H1）
> ✅ 一句话结论：**加拿大全国性电线电缆与电气分销商，温尼伯设有分支（950 Ross Ave）；
> 🎯 **具名邮箱 `norwpg@noramco.ca`（温尼伯分支）SMTP 实证通过**（控制 250 / 随机 550）；
> ⚠️ **`info@noramco.ca` 实测 550（不存在）** —— 属**极少数「分支邮箱存在但 info@ 不存在」**的域名；
> `noramco.com` 为**另一租户**（452 4.5.3 多租户）⇒ **不得使用 .com**；
> ⓪ 反身排除判定：**分销商，非制造商 ⇒ 通过**。

---

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示(如有)
Noramco | ⛔ 未获取（仅有分支邮箱）| ⛔ 未获取 | norwpg@noramco.ca | ✅ SMTP 实证（控制 250 / 随机 550 / 候选 250）| ⛔ 未定位 | 加拿大电线电缆与电气分销商，温尼伯分支位于 950 Ross Ave；提供 Cut-To-Length、库存管理、并联敷设（Paralleling）、Kitting、定制标签、剥皮/染色/绞合、定制拉眼安装等增值服务；服务商业/工业、电信、公用事业、OEM 市场 | ECAM 会员名录（一手）+ 官网分支页（一手）+ DNS/MX + SMTP 控制地址探测 | ⚠️ 主营为电线电缆；官网未明列变压器采购
```

**发信资格：⚠️ 部分通过**（**分支业主邮箱已实证**，但**无具名联系人、无职位** ⇒ 只能发角色型分支邮箱）
**邮箱档位：B（分支角色邮箱 `norwpg@`，SMTP 实证通过）**

---

## 二、补充信息（扩展段）

### 标准字段明细

| 项 | 内容 | 来源 |
|---|---|---|
| **公司名** | **Noramco**（官网拼写；第三方偶见拼作 **Normaco**，⚠️ **疑为官网笔误**）| 官网（一手）|
| **国家 + 城市** | **加拿大 MB 省 Winnipeg（温尼伯分支）** | 官网分支页（一手）|
| **州省** | **MB ✅**（CSV 填 MB，**正确**）| — |
| **🔴 温尼伯分支地址** | **950 Ross Ave, Winnipeg, MB R3E 1M2** | 官网分支页 + ECAM（一手）|
| **电话（温尼伯）** | **204-661-8302** ／ F **204-663-3898** ／ Toll Free **800-706-9519** | ECAM（一手）|
| **邮箱（温尼伯分支）** | **`norwpg@noramco.ca`** | ECAM 名录（一手）|
| **域名** | **noramco.ca**（⚠️ **`.com` 属另一租户，禁用**）| DNS |
| **邮件网关** | **Microsoft Exchange Online**（`noramco-ca.mail.protection.outlook.com`）| DNS MX |
| **SPF** | `v=spf1 ip4:104.130.122.4 ip4:143.55.233.119 include:spf.protection.outlook.com include:343251081.spf02.hubspotemail.net include:_spf.sendergen.com -all`（**硬 fail**）| DNS TXT |
| **DMARC** | **`v=DMARC1; p=reject; rua=…uriports.com; adkim=r; aspf=r`** | DNS TXT |
| **成立年份** | ⛔ 未获取 | — |
| **规模** | 全国多分支（温尼伯为其中之一）；员工数 ⛔ 未获取 | — |
| **官网** | https://noramco.ca | — |

### 业务定位（官网一手，逐字）

官网首页（一手）：
> *"Wire & Cable Distributor — At **Normaco**（⚠️ 疑笔误，实为 Noramco）, we are proud to provide
> a wide range of **high-quality wire, cable, and electrical** …"*

官网温尼伯分支页（一手）：
> *"Winnipeg — **950 Ross Ave, Winnipeg, MB R3E 1M2**"*
> 增值服务逐字：*"**Cut-To-Length** … **Inventory Management** … **Paralleling** …
> **Kitting** … **Custom Labelling** … **Stripping / Dying / Twisting** …
> **Custom Pulling Eye Installation**"*
> *"We are always happy to answer technical questions, help locate **rare or difficult-to-find items**,
> and assist you in **sourcing the ideal products** for your application."*

ECAM 会员名录（一手）：
> *"No matter what industry you are working in—**commercial and industrial, telecom, utility, or OEM**—
> we can help you …"*

⚠️ **官网未明列变压器采购** —— 主营为**电线电缆与配套增值加工**，
**变压器属延伸品类推断**（电气分销商常规品类）。

### ⓪ 反身排除判定（本环节强制首层）

| 检查项 | 结论 |
|---|---|
| 官网是否自称 manufacture / 制造 | ❌ **无**（自称 *"Wire & Cable Distributor"*）|
| 是否有自有品牌变压器规格书 | ❌ 无 |
| 是否销售自有品牌变压器 | ❌ 无 |
| 定性 | ✅ **分销商（含电缆加工增值服务）⇒ 非制造商 ⇒ 通过 ⓪ 层** |

### 联系人（含仍_here 在职核验）

| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| ⛔ **未获取任何具名联系人** | — | — | — | — | — | — |
| （分支邮箱）| 温尼伯分支 | `norwpg@noramco.ca` | — | 🟢 邮箱 SMTP 实证 | — | — |

> 🔴 **机读结论**：
> 1. **本单核心缺口 = 人** —— 官网与 ECAM **均只列分支邮箱，未列具名人员**。
> 2. ✅ **但 `norwpg@noramco.ca` 已 SMTP 实证**（非 catch-all）⇒ **可发分支角色邮箱**，
>    属「B 档角色邮箱主送、正文点名公司/分支」的可用路径。
> 3. ⚠️ **无采购决策人具名** ⇒ 若首封无回应，需转 LinkedIn 补人。

### 邮箱分档（A/B/C）

| 档 | 地址 | 依据 | 可否主送 |
|---|---|---|---|
| A | ⛔ 未获取 | — | — |
| **B** | **`norwpg@noramco.ca`** | **ECAM 名录明文 + SMTP 控制地址协议实证（250）** | ✅ **主送**（温尼伯分支）|
| C | `info@noramco.ca` | 🔴 **实测 550（不存在）** | ⛔ **禁止使用**（H2）|
| C | `info@noramco.com` / `sales@noramco.com` | 🔴 **452 4.5.3 Recipients belong to multiple tenants**（**另一租户**）| ⛔ **禁止使用** |

**🔴 邮箱验证方法与证据链（可复现）：**

```
域名 noramco.ca
MX   = noramco-ca.mail.protection.outlook.com   （Microsoft Exchange Online）
SMTP 控制地址协议（HELO jiezougroup.com）：
  RCPT norwpg@noramco.ca      -> 250 2.1.5 Recipient OK    （控制地址 A：ECAM 明文，已知真实）
  RCPT zzq9k2x7@noramco.ca    -> 550 5.4.1 Access denied   （控制地址 B：随机地址，正确拒绝）
  RCPT info@noramco.ca        -> 550 5.4.1 Access denied   ← 【反证】info@ 不存在，非 catch-all
⇒ ✅ 控制 250 + 随机 550 ⇒ 判定【真实名册，非 catch-all】。

⚠️ 跨域误用警示（经 noramco.ca 的 MX 探测 .com 地址）：
  RCPT info@noramco.com       -> 452 4.5.3 Recipients belong to multiple tenants
  RCPT sales@noramco.com      -> 452 4.5.3 Recipients belong to multiple tenants
⇒ 🔴 判定：noramco.com 属于【另一 Microsoft 租户】，与 noramco.ca 非同一组织
   ⇒ 不得因两者同名而互推邮箱；且 .com 无法经 .ca 的 MX 探测。
```

---

## 三、开发信建议（**仅限：收件人 / 时机 / 附件 —— 不含正文、不含主题行、不含开场句**）

| 项 | 建议 | 依据 |
|---|---|---|
| **主送** | **`norwpg@noramco.ca`**（温尼伯分支）| B 档，名录一手 + SMTP 250 |
| **正文处理** | ⚠️ **无具名联系人** ⇒ 建议以**分支/公司层面**称呼，**不得虚构人名** | H1/H2 |
| **补齐路径** | ① 电话 **204-661-8302** 索取采购/分支经理邮箱<br>② LinkedIn 搜索 Noramco 员工 | 本环节渠道清单 |
| **建议时机** | **中部时间（CT）工作日 08:30–10:30**（Winnipeg = America/Winnipeg）| — |
| **建议附件** | ① UL 证书 **E541627**（三相液浸配电变 45–5,000 kVA）<br>② UL 证书 **E541626**（电力变 750–110,000 kVA）<br>③ 公司介绍 | 加拿大客户 ⇒ 配电级为主，电力级可备选 |
| **切入角度提示**（**仅提示，不代拟文案**）| ① 该公司服务 **commercial/industrial、telecom、utility、OEM** ⇒ 客户面广，**配电变是其客户配套品类**<br>② 其官网强调 **"help locate rare or difficult-to-find items"（稀缺件寻源）** ⇒ **寻源能力导向**，可突出我方直供与交期确定性<br>③ 提供 **Cut-To-Length / Kitting / Paralleling** 等电缆加工增值服务 ⇒ **对配套物料整合供货敏感** | 官网（一手）|
| ⛔ **禁止事项** | ① 不得称 certified（柱上变 E544629 仅 ECD 计划函）<br>② 不得提 YAWEI<br>③ 首封不报交期/价格<br>④ **不得使用 `info@noramco.ca`**（实测不存在）<br>⑤ 🔴 **不得使用 `noramco.com` 任何地址**（属另一租户）<br>⑥ **不得虚构联系人姓名**<br>⑦ 不得发送供货记录 PDF | — |

---

## 四、⚠️ 矛盾点与风险提示

| # | 风险 | 说明 |
|---|---|---|
| 1 | 🔴 **`noramco.com` 属另一租户** | 452 4.5.3 多租户 ⇒ **同名不同组织**，误用即退信 |
| 2 | ⚠️ **`info@noramco.ca` 不存在（550）** | 罕见：分支邮箱存在而 info@ 不存在 ⇒ 严禁惯例兜底 |
| 3 | ⚠️ **无具名联系人 / 无职位** | 仅能发分支角色邮箱，称呼需谨慎 |
| 4 | ⚠️ **官网拼写不一致** | 首页写 "Normaco"、品牌为 "Noramco" ⇒ 引用时以 Noramco 为准 |
| 5 | ⚠️ **主营非变压器** | 电线电缆 + 加工服务为主 ⇒ 变压器属品类延伸 |
| 6 | ⚠️ **成立年份未获取** | — |

---

## 五、信息缺口清单（请勿编造）

| 缺口 | 状态 |
|---|---|
| **具名联系人 / 职位** | ⛔ **未获取**（本单核心缺口）|
| **高管 / 采购决策人** | ⛔ 未获取 |
| **成立年份 / 员工数 / 注册号** | ⛔ 未获取 |
| **变压器采购证据** | ⛔ 未获取 |
| **决策人 LinkedIn** | ⛔ 未定位 |

---

## 六、一句话画像

**加拿大电线电缆与电气分销商，温尼伯分支位于 950 Ross Ave，提供 Cut-To-Length、Kitting、
Paralleling、定制拉眼等电缆加工增值服务，客户覆盖 commercial/industrial、telecom、utility、OEM。
🎯 温尼伯分支邮箱 **`norwpg@noramco.ca` 已 SMTP 实证**（控制 250 / 随机 550）；
⚠️ **`info@noramco.ca` 实测不存在（550）**；🔴 **`noramco.com` 属另一租户（452 多租户），禁用**。
⛔ **官网与行业协会名录均无具名联系人** ⇒ 只能以分支角色邮箱触达，称呼需谨慎。
⓪ 层判定：分销商，非制造商 ⇒ 通过。加拿大客户 ⇒ 配电级 E541627 为主。**

---

## 七、渠道覆盖清单

| 渠道 | 状态 |
|---|---|
| **L-1 锁人** | ⛔ **未获取任何具名联系人**（仅有分支邮箱）|
| **L0 官网** | ✅ 首页 + 温尼伯分支页抓取；拿到地址、增值服务清单；⚠️ 无邮箱无人员 |
| **L1 政府一手** | ⛔ 未查 |
| **L2 命名+DNS** | ✅ 域名存活（M365，SPF `-all`，DMARC `p=reject`）；✅ **SMTP 实证（含 .com 多租户反证）** |
| **L3 B2B 库** | 🟡 infobel 提及（未采信）|
| **L4 社媒协会** | ✅ **ECAM 会员名录**（地址 + 电话 + 邮箱）|
| **L5 黄页同址** | 🟡 infobel.ca 条目一致 |
| **L6 电话表单** | ✅ 204-661-8302 |
| **L7 付费** | ⛔ 未启用 |
