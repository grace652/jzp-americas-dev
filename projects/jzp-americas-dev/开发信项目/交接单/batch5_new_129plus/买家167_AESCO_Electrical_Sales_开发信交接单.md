# 【买家 167】开发信交接单 — AESCO Electrical Sales（Atlantic Canada）

> 采集日期：2026-09-28 ｜ 名单来源：`线索资产/目标客户清单.csv` 序号 38（B 类 · 分销商/贸易商）
> 采集方：找客户环节（本环节只产出交接单，不写正文/不碰模板/不定话术）
> ⚠️ 本表严格区分「已验证」与「未获取」，未找到的信息一律标注，**不做推断填充**（H1）
> ✅ 一句话结论：**加拿大大西洋省份（Atlantic Canada）的高中压电力变压器与开关柜
> 「制造商代表 + 分销商」—— 🎯 **本批次「产品定位最精准」的目标**（官网逐字：
> *"providing **High and Medium Voltage Power Transformers**, Switchgear…"*）；
> 🔴 **但其邮件网关（IONOS/1and1）以 rDNS 为由拒绝我方源 IP** ⇒
> **本轮 SMTP 探测失败**，邮箱**无法实证**，**只能依官网/名录定档**；
> ⓪ 反身排除判定：**制造商代表 + 分销商，非制造商 ⇒ 通过**。

---

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示(如有)
AESCO Electrical Sales（AESCO）| ⛔ 未获取 | ⛔ 未获取 | ⛔ 未获取（官网仅列电话/传真，无邮箱）| 🔴 SMTP 探测失败（网关拒绝源 IP）| ⛔ 未定位 | 加拿大大西洋省份的高中压电力变压器、开关柜等电力设备「制造商代表 + 分销商」；地址 20 Greenwich Drive, Dartmouth, Nova Scotia；服务 Atlantic Canada 区域 | 官网首页/Contact 页（一手）+ DNS/MX + SMTP（失败，记录为设备级阻断） | 🔴 邮箱未获取；⚠️ SMTP 网关以 rDNS 为由拒绝探测源
```

**发信资格：⛔ 待补**（**产品定位极精准**，但**缺邮箱、缺具名联系人** ⇒ 需补）
**邮箱档位：⛔ 未获取**

---

## 二、补充信息（扩展段）

### 标准字段明细

| 项 | 内容 | 来源 |
|---|---|---|
| **公司名** | **AESCO Electrical Sales**（品牌 **AESCO**；关联名 **Aesco Associates Limited**）| 官网 + 411.ca（一手/三方）|
| **国家 + 城市** | **加拿大 NS 省 Dartmouth（达特茅斯）** | 官网 Contact 页（一手）|
| **州省** | **NB（CSV 口径：新不伦瑞克）** ⚠️ **地址实为 NS（新斯科舍）Dartmouth** | 官网（一手）|
| **详细地址** | **20 Greenwich Drive, Dartmouth, Nova Scotia, Canada B2V 2L9** | 官网 Contact 页（一手）|
| **电话** | **902 434 3101** | 官网 Contact 页（一手）|
| **传真** | **902 434 3101**（⚠️ 官网电话与传真**同号**，疑为录入问题）| 官网（一手）|
| **邮箱** | ⛔ **官网未列任何邮箱** | — |
| **域名** | **aesco.ca** | — |
| **邮件网关** | 🔴 **IONOS / 1&1（`mx00.1and1.com` / `mx01.1and1.com`）** | DNS MX |
| **SPF / DMARC** | ⚠️ 未解析到有效值 | — |
| **成立年份** | ⛔ 未获取 | — |
| **覆盖区域** | **Atlantic Canada（大西洋省份）** | 官网（一手）|

### 业务定位（官网一手，逐字）⭐

官网首页（一手）：
> *"AESCO is a **Manufacturers Representative and Distributor** providing
> **High and Medium Voltage Power Transformers, Switchgear**, …"*
> *"We Are **Manufacturer's Representatives** — We Are **Manufacturer's Distributors** —
> We Constantly Strive To Be Our Customers **EASIEST Place to Do Business**"*

官网 Contact 页（一手）：
> *"Always feel free to contact AESCO for any questions on our products or if you are looking for
> **representation in the Atlantic Canada Area**"*
> *"**20 Greenwich Drive, Dartmouth, Nova Scotia, Canada B2V 2L9** — Tel: 902 434 3101 —
> Fax: 902 434 3101"*

⭐ **品类验证（本批次最强）**：官网**直接以「High and Medium Voltage Power Transformers」
作为首项业务描述** ⇒ **与我方高压/中压变压器产品线高度吻合**。

### 🔴 ⓪ 反身排除判定（本环节强制首层）

| 检查项 | 结论 |
|---|---|
| 官网是否自称 manufacture / 制造 | ❌ **无**（自称 *"Manufacturers Representative and Distributor"*）|
| 是否有自有品牌变压器规格书 | ❌ 无 |
| 是否销售自有品牌变压器 | ❌ 无（代理他人品牌）|
| **是否构成「代理冲突」** | ⚠️ **是 —— 它是「制造商代表」，本质即代理** |
| **代理哪些变压器品牌** | ⛔ **未获取**（官网产品/品牌页路径 404，未取得代理清单）|
| 定性 | ✅ **不排除（非制造商）**；🔴 **但必须核查其已代理的变压器品牌** —— 这决定是否存在渠道冲突 |

> 📌 **机读结论（关键）**：
> 1. **AESCO 的业务描述与本项目产品线呈现「近乎逐字级吻合」**
>    （*"High and Medium Voltage Power Transformers"*）⇒ **靶向性极强**。
> 2. 🔴 **但它是 manufacturers representative（代理商）** ⇒ **开发前必须确认它代理的变压器品牌**，
>    否则可能构成「撬已有代理」。
> 3. ⚠️ **本单未能取得其品牌代理清单**（官网 `/products` 路径返回 404）⇒ **列为关键待补项**。

### 联系人（含仍_here 在职核验）

| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| ⛔ **未获取任何具名联系人** | — | — | — | — | — | — |

### 邮箱分档（A/B/C）

| 档 | 地址 | 依据 | 可否主送 |
|---|---|---|---|
| A | ⛔ 未获取 | — | — |
| B | ⛔ 未获取 | — | — |
| C | `info@aesco.ca` 等 | ⚠️ **纯推测，且探测失败无法验证** | ⛔ **禁止使用**（H2）|

**🔴 邮箱验证状态（本单特殊：探测被目标网关阻断）：**

```
域名 aesco.ca
MX   = mx00.1and1.com / mx01.1and1.com   （IONOS / 1&1）
SMTP 控制地址协议（HELO jiezougroup.com）：
  CONNECT-ERR  SMTPConnectError (554)
  b'perfora.net (mxeueus011) Nemesis ESMTP Service not available / No SMTP service /
    Invalid DNS PTR resource record / … i=ip&v=223.64.2.43&r=1M1r4W-…'
⇒ 🔴 【网关级阻断】：该 MX 以【源 IP 无有效 rDNS（PTR）】为由，在 SMTP 握手前即返回 554
   ⇒ 连【控制地址】都无法投递 ⇒ 【探测能力为 0】。
⇒ ⛔ 依 H2/H4：本域【未做成功探测】，不得推断或标注任何邮箱为「已验证」。
⚠️ 该阻断为【对探测源 IP 的策略】，【不代表我方正常发信会被拒】
   （正式发信的源 IP 与 rDNS 不同）—— 但接入前需评估。
```

---

## 三、开发信建议（**仅限：收件人 / 时机 / 附件 —— 不含正文、不含主题行、不含开场句**）

| 项 | 建议 | 依据 |
|---|---|---|
| **主送** | ⛔ **暂不可发信** —— 缺邮箱 + 缺联系人 | — |
| **补齐路径（首选）** | 🔴 **电话 902 434 3101**，需索取：<br>① 变压器产品线负责人姓名与邮箱<br>② **其已代理的变压器品牌清单**（🔴 决定是否渠道冲突）| 本环节渠道清单 |
| **补齐路径（次选）** | 补抓官网 `/products` 或品牌页（原路径 404，需从首页导航重试）| — |
| **建议时机** | **大西洋时间（AT）工作日 08:30–10:30**（Dartmouth = America/Halifax）| — |
| **建议附件** | ① UL 证书 **E541627**（三相液浸配电变 45–5,000 kVA）<br>② UL 证书 **E541626**（电力变 750–110,000 kVA）<br>③ 公司介绍 | 🎯 **该司明示经营 High & Medium Voltage 变压器 ⇒ E541626 + E541627 双证均对口** |
| **切入角度提示**（**仅提示，不代拟文案**）| ① 🎯 该司**产品定位与本项目近乎逐字吻合**（*"High and Medium Voltage Power Transformers"*）⇒ **靶向性最强**<br>② 其定位为 **manufacturers representative + distributor** ⇒ **熟悉与制造商建立代理/分销关系**，**是「潜在区域代理」思路的天然对象**<br>③ 覆盖 **Atlantic Canada（NB/NS/PE/NL 四省）** ⇒ **区域独家潜力**<br>④ 🔴 **前置动作必不可少**：确认其**现有变压器代理线**，避免「撬代理」 | 官网（一手）|
| ⛔ **禁止事项** | ① 不得称 certified（柱上变 E544629 仅 ECD 计划函）<br>② 不得提 YAWEI<br>③ 首封不报交期/价格<br>④ **不得虚构联系人或邮箱**（H1/H2）<br>⑤ 🔴 **不得在未核实其代理线前贸然开发**<br>⑥ **不得声称 AESCO 是制造商**<br>⑦ 不得发送供货记录 PDF | — |

---

## 四、⚠️ 矛盾点与风险提示

| # | 风险 | 说明 |
|---|---|---|
| 1 | 🔴 **SMTP 网关以 rDNS 为由完全阻断探测** | 连控制地址都无法投递 ⇒ **邮箱不可实证** |
| 2 | 🔴 **代理冲突风险** | 它是 manufacturers representative（代理商）⇒ **必须核查其已有变压器代理线** |
| 3 | ⚠️ **官网未列任何邮箱** | 仅电话与传真 |
| 4 | ⚠️ **电话与传真同号（902 434 3101）** | 疑为官网录入问题，**致电时注意** |
| 5 | ⚠️ **CSV 省份（NB）与官网地址（NS）不一致** | 官网明示 Dartmouth, **Nova Scotia** ⇒ **建议更正 CSV 为 NS** |
| 6 | ⚠️ **无具名联系人** | 官网全站未见人员 |
| 7 | ⚠️ **产品页路径 404** | 品牌代理清单未取得 |

---

## 五、信息缺口清单（请勿编造）

| 缺口 | 状态 |
|---|---|
| **其代理的变压器品牌清单** | 🔴 **未获取（决定是否渠道冲突的关键）** |
| **具名联系人 / 职位** | ⛔ **未获取** |
| **任何邮箱地址** | ⛔ **未获取** |
| **成立年份 / 员工数 / 注册号** | ⛔ 未获取 |
| **SPF / DMARC** | ⛔ 未解析到 |

---

## 六、一句话画像

**加拿大大西洋省份的高中压电力变压器与开关柜「制造商代表 + 分销商」，
地址 20 Greenwich Drive, Dartmouth, **Nova Scotia** B2V 2L9，电话 902 434 3101。
🎯 **其官网业务描述（*"providing High and Medium Voltage Power Transformers, Switchgear"*）
与本项目产品线近乎逐字吻合 —— 是本批次「产品定位最精准」的目标。**
✅ 其自述 "*We Are Manufacturer's Representatives / Distributors*" ⇒
**是「潜在区域代理」思路的天然对象，可覆盖 Atlantic Canada 四省**。
🔴 **两处阻断**：① 邮件网关（IONOS）以**源 IP 无 rDNS** 为由在握手前返回 554 ⇒ **本轮 SMTP 探测完全失败，邮箱无法实证**；
② **官网未列任何邮箱、无具名联系人**。
⚠️ **开发前置动作**：必须先核实其**已代理的变压器品牌**，避免「撬代理」。
⓪ 层判定：制造商代表 + 分销商，非制造商 ⇒ 通过。**

---

## 七、渠道覆盖清单

| 渠道 | 状态 |
|---|---|
| **L-1 锁人** | ⛔ **未获取任何具名联系人** |
| **L0 官网** | ✅ 首页 + Contact 页抓取；拿到地址、电话、业务定位；⛔ 无邮箱、无人员；⚠️ `/products` 404 |
| **L1 政府一手** | ⛔ 未查 |
| **L2 命名+DNS** | ✅ 域名存活（IONOS/1&1 MX）；🔴 **SMTP 被 rDNS 策略阻断，探测失败** |
| **L3 B2B 库** | 🟡 411.ca（关联名 Aesco Associates Limited）；🟡 trademo.com（未采信）|
| **L4 社媒协会** | ⛔ 未定位 |
| **L5 黄页同址** | 🟡 411.ca 条目（Dartmouth, NS）|
| **L6 电话表单** | ✅ 902 434 3101（**唯一可用触点**）|
| **L7 付费** | ⛔ 未启用 |
