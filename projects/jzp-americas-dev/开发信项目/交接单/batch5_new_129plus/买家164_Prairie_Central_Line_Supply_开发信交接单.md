# 【买家 164】开发信交接单 — Prairie Central Line Supply Ltd.（PCLS）

> 采集日期：2026-09-28 ｜ 名单来源：`线索资产/目标客户清单.csv` 序号 35（B 类 · 分销商/贸易商）
> 采集方：找客户环节（本环节只产出交接单，不写正文/不碰模板/不定话术）
> ⚠️ 本表严格区分「已验证」与「未获取」，未找到的信息一律标注，**不做推断填充**（H1）
> ✅ 一句话结论：**1988 年创立、专门服务曼省与萨省电力与电信行业的杆线与带电作业物资供应商；
> 🎯 **具名/角色邮箱 `hmcnicolljr@pclsupply.mb.ca` SMTP 实证通过**
> （控制 250 / 随机 550 / `info@` + `sales@` 均 250）；
> 🔴 **邮箱域名存在「双域」现象**：具名邮箱用 **`pclsupply.mb.ca`**，而角色邮箱用 **`pclsupply.ca`**
> ⇒ **典型「一封一域」陷阱，不得混用**；
> ⓪ 反身排除判定：**电力/电信物资分销商，非制造商 ⇒ 通过**。

---

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示(如有)
Prairie Central Line Supply Ltd. | H. McNicoll Jr.（缩写）| ⛔ 职位未获取 | hmcnicolljr@pclsupply.mb.ca | ✅ SMTP 实证（控制 250 / 随机 550 / 候选 250）| ⛔ 未定位 | 加拿大曼尼托巴省温尼伯的电力与电信行业物资供应商，1988 年创立；主营带电作业工具、杆线五金、导线配件、安全服装等；客户以电力公用事业与电信行业为主，兼服务承包商 | 官网（一手）+ ECAM 会员名录（一手）+ DNS/MX + SMTP 控制地址探测 | ⚠️ 主营为杆线/带电作业物资，非变压器主品类；官网未见变压器采购声明
```

**发信资格：✅ 通过**（具名邮箱 SMTP 实证；⚠️ 职位未获取）
**邮箱档位：A（具名个人邮箱 SMTP 实证）+ B（`info@` / `sales@` 实证）**

---

## 二、补充信息（扩展段）

### 标准字段明细

| 项 | 内容 | 来源 |
|---|---|---|
| **公司全称** | **Prairie Central Line Supply Ltd.**（简称 **PCLS**）| 官网（一手）|
| **国家 + 城市** | **加拿大 MB 省 Winnipeg（温尼伯）** | 官网 Contact 页（一手）|
| **州省** | **MB ✅**（CSV 填 MB，**正确**）| — |
| **详细地址** | **583 Plinguet St, Winnipeg, MB R2J 0G3** | 官网 Contact 页 + ECAM（一手）|
| **电话** | **(204) 633-1804** ／ Toll Free **1-800-701-4441** ／ F **(204) 633-1183** | 官网 Contact 页（一手）|
| **邮箱（具名）** | **`hmcnicolljr@pclsupply.mb.ca`** | ECAM 名录（一手）|
| **邮箱（角色）** | `info@pclsupply.ca` / `sales@pclsupply.ca`（**均 SMTP 250**）| SMTP 实证 |
| **🔴 邮箱域名（双域）** | **具名 → `pclsupply.mb.ca`** ／ **角色 → `pclsupply.ca`** | ECAM + SMTP |
| **网站域名** | **pclsupply.ca** | 官网 |
| **邮件网关（两域同）** | **Microsoft Exchange Online**（`pclsupply-ca.mail.protection.outlook.com` / `pclsupply-mb-ca.mail...`）| DNS MX |
| **DMARC** | **`v=DMARC1; p=reject`**（pclsupply.ca）| DNS TXT |
| **成立年份** | **1988 年**（官网逐字 *"Established in 1988"*）| 官网（一手）|
| **规模** | ⛔ 员工数未获取 | — |
| **官网** | https://www.pclsupply.ca/ | — |

### 业务定位（官网一手，逐字）

官网首页（一手）：
> *"**Established in 1988** to service the **Power and Telecommunications Industry in Manitoba
> and Saskatchewan**, Prairie Central line Supply Ltd. offers a broad range of electrical
> and safety related items. From **hot line tools & pole line hardware, to wire accessories,
> safety clothing**, and much more, PCLS is here to supply the needs of our customers.
> We also carry stock **exclusively devoted for contractors**."*
> *"Our mission is to provide quality service to our valued customers based on our core values of
> **honesty, integrity and dedication**."*

官网 Contact 页（一手）：
> *"Prairie Central Line Supply Ltd. **Winnipeg** — **583 Plinguet St, Winnipeg, MB R2J0G3**
> Phone: (204) 633-1804 or 1-800-701-4441 — Fax: (204) 633-1183"*

⚠️ **官网未明列变压器采购** —— 主营为**带电作业工具 / 杆线五金 / 导线配件 / 安全服装**，
**变压器属延伸品类推断**（电力公用事业客户常同时采购变压器）。

### ⓪ 反身排除判定（本环节强制首层）

| 检查项 | 结论 |
|---|---|
| 官网是否自称 manufacture / 制造 | ❌ **无**（自称 *"here to supply the needs"* / *"carry stock"*）|
| 是否有自有品牌变压器规格书 | ❌ 无 |
| 是否销售自有品牌变压器 | ❌ 无 |
| 定性 | ✅ **电力/电信物资分销商 ⇒ 非制造商 ⇒ 通过 ⓪ 层** |

### 联系人（含仍_here 在职核验）

| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| **H. McNicoll Jr.**（缩写，全名未获取）| **首封主送（具名）** | ⛔ **职位未获取** | ⚠️ 未知 | 🟢 中：名录在列 + 邮箱 SMTP 实证 | ⚠️ 未知 | ⛔ 未定位 |

> 🔴 **机读结论**：
> 1. **`hmcnicolljr@pclsupply.mb.ca` 是 ECAM 名录列出的具名邮箱，SMTP 实证通过**。
>    ⚠️ 但邮箱名用**缩写**（`hmcnicolljr` = H. McNicoll Jr.）⇒ **全名与职位均未获取**。
> 2. ⚠️ **该司为家族型老牌企业（1988 年）**，McNicoll 姓名缩写带「Jr.」⇒ 可能为**第二代/家族成员**，
>    **若如此则职级可能较高**（但**未获证实，不得推断**）。
> 3. ✅ **有 `info@` / `sales@` 兜底**（均实证 250）。

### 邮箱分档（A/B/C）

| 档 | 地址 | 依据 | 可否主送 |
|---|---|---|---|
| **A** | **`hmcnicolljr@pclsupply.mb.ca`** | **ECAM 名录明文 + SMTP 控制地址协议实证（250）** | ✅ **主送**（⚠️ 全名/职位未知）|
| **B** | `info@pclsupply.ca` / `sales@pclsupply.ca` | **SMTP 实证（均 250）** | ✅ 兜底主送 |
| C | `hmcnicolljr@pclsupply.ca` | 🔴 **实测 550（不存在于 .ca）** | ⛔ **禁止使用** |

**🔴 邮箱验证方法与证据链（可复现）：**

```
域名 pclsupply.ca  （另有 pclsupply.mb.ca，两者 MX 均指向 Microsoft Exchange Online）
SMTP 控制地址协议（HELO jiezougroup.com，经 pclsupply-ca 的 MX）：
  RCPT hmcnicolljr@pclsupply.mb.ca -> 250 2.1.5 Recipient OK   （控制地址 A：ECAM 明文，已知真实）
  RCPT zzq9k2x7@pclsupply.ca       -> 550 5.4.1 Access denied  （控制地址 B：随机地址，正确拒绝）
  RCPT info@pclsupply.ca           -> 250 2.1.5 Recipient OK
  RCPT sales@pclsupply.ca          -> 250 2.1.5 Recipient OK
  RCPT hmcnicolljr@pclsupply.ca    -> 550 5.4.1 Access denied  ← 【跨域反证】
⇒ ✅ 控制 250 + 随机 550 ⇒ 判定【真实名册，非 catch-all】。

🔴 【双域结论】（本单最重要发现）：
   · 具名邮箱只存在于 `pclsupply.mb.ca`（.ca 上 550）
   · 角色邮箱存在于 `pclsupply.ca`（.mb.ca 未测角色）
   ⇒ 判定：该组织同时运营两个域，【具名与角色分属不同域】，【不得跨域套用命名规则】。
```

---

## 三、开发信建议（**仅限：收件人 / 时机 / 附件 —— 不含正文、不含主题行、不含开场句**）

| 项 | 建议 | 依据 |
|---|---|---|
| **主送** | **`hmcnicolljr@pclsupply.mb.ca`**（点名 H. McNicoll Jr.）| A 档具名实证；⚠️ **注意域名是 `.mb.ca` 不是 `.ca`** |
| **兜底** | `info@pclsupply.ca` / `sales@pclsupply.ca`（均实证）| B 档 |
| **补齐路径** | 电话 **(204) 633-1804** 确认 McNicoll 全名与职位 | 本环节渠道清单 |
| **建议时机** | **中部时间（CT）工作日 08:30–10:30**（Winnipeg = America/Winnipeg）| — |
| **建议附件** | ① UL 证书 **E541627**（三相液浸配电变 45–5,000 kVA）<br>② UL 证书 **E541626**（电力变 750–110,000 kVA）<br>③ 公司介绍 | 加拿大客户 + 电力公用事业渠道 ⇒ **配电级为主，电力级可备选** |
| **切入角度提示**（**仅提示，不代拟文案**）| ① 该司**明确服务 Power & Telecommunications Industry**，覆盖 **MB + SK 两省** ⇒ **客户即电力公用事业单位，是配电变的终端使用方**<br>② 其主营为**带电作业工具与杆线五金** ⇒ **配电变是其客户配套品类，互补性明确**<br>③ 1988 年创立、**"honesty, integrity and dedication"** 为对外核心价值 ⇒ **关系导向、看重长期承诺**<br>④ 官网提及 *"stock exclusively devoted for contractors"* ⇒ **有承包商专属库存机制** ⇒ 对**供货稳定性**敏感 | 官网（一手）|
| ⛔ **禁止事项** | ① 不得称 certified（柱上变 E544629 仅 ECD 计划函）<br>② 不得提 YAWEI<br>③ 首封不报交期/价格<br>④ 🔴 **不得把具名邮箱写成 `pclsupply.ca`**（实测不存在）<br>⑤ **不得虚构 McNicoll 的全名或职位**（H1）<br>⑥ 不得发送供货记录 PDF | — |

---

## 四、⚠️ 矛盾点与风险提示

| # | 风险 | 说明 |
|---|---|---|
| 1 | 🔴 **双域陷阱** | 具名用 `pclsupply.mb.ca`、角色用 `pclsupply.ca` ⇒ **跨域套用即退信** |
| 2 | ⚠️ **具名人全名与职位未知** | 仅缩写 `hmcnicolljr` ⇒ 正式称呼有风险 |
| 3 | ⚠️ **主营非变压器** | 带电作业工具/杆线五金为主 ⇒ 变压器属品类延伸 |
| 4 | ⚠️ **DMARC `p=reject`（严格）** | 我方若以此域代发需极谨慎（但正常直发无影响）|
| 5 | ⚠️ **成立年份一手但规模未获取** | — |
| 6 | ⚠️ **「Jr.」提示家族企业，但职级未证实** | **不得推断其为负责人** |

---

## 五、信息缺口清单（请勿编造）

| 缺口 | 状态 |
|---|---|
| **McNicoll 的全名与职位** | ⛔ **未获取** |
| **高管 / 采购决策人** | ⛔ 未获取 |
| **员工数 / 注册号** | ⛔ 未获取 |
| **变压器采购证据** | ⛔ 未获取 |
| **决策人 LinkedIn** | ⛔ 未定位 |

---

## 六、一句话画像

**1988 年创立、专门服务曼尼托巴与萨斯喀彻温两省「电力与电信行业」的杆线与带电作业物资供应商
（583 Plinguet St, Winnipeg），主营带电作业工具、杆线五金、导线配件、安全服装，
另有承包商专属库存。客户即电力公用事业单位 ⇒ **配电变的终端使用场景明确**。
🎯 **具名邮箱 `hmcnicolljr@pclsupply.mb.ca` 已 SMTP 实证**（⚠️ 全名/职位未知）；
`info@pclsupply.ca` / `sales@pclsupply.ca` 亦均实证。
🔴 **关键陷阱：具名邮箱在 `pclsupply.mb.ca`，角色邮箱在 `pclsupply.ca` —— 双域并存，不得混用**
（`hmcnicolljr@pclsupply.ca` 实测 550）。
⓪ 层判定：电力/电信物资分销商，非制造商 ⇒ 通过。加拿大客户 ⇒ 配电级 E541627 为主。**

---

## 七、渠道覆盖清单

| 渠道 | 状态 |
|---|---|
| **L-1 锁人** | 🟡 **H. McNicoll Jr.（职位未知）** —— 名录一手 + 邮箱实证；⛔ 无高管明列 |
| **L0 官网** | ✅ 首页 + Contact 页抓取；拿到 1988 年、业务定位、地址、双电话；⛔ 无具名人员页 |
| **L1 政府一手** | ⛔ 未查 |
| **L2 命名+DNS** | ✅ **双域解析**（pclsupply.ca + pclsupply.mb.ca，均 M365）；✅ **SMTP 实证（含跨域反证）** |
| **L3 B2B 库** | 🟡 canada.chamberofcommerce.com / allbiz.ca（未采信）|
| **L4 社媒协会** | ✅ **ECAM 会员名录**（地址 + 邮箱）|
| **L5 黄页同址** | 🟡 firmania.ca 条目一致（583 Plinguet St）|
| **L6 电话表单** | ✅ (204) 633-1804 / 1-800-701-4441 |
| **L7 付费** | ⛔ 未启用 |
