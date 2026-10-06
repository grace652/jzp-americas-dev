# 【买家 160】开发信交接单 — Jebco Agencies Inc.（电气制造商代表）

> 采集日期：2026-09-28 ｜ 名单来源：`线索资产/目标客户清单.csv` 序号 31（B 类 · 分销商/贸易商）
> 采集方：找客户环节（本环节只产出交接单，不写正文/不碰模板/不定话术）
> ⚠️ 本表严格区分「已验证」与「未获取」，未找到的信息一律标注，**不做推断填充**（H1）
> ✅ 一句话结论：**加拿大中西部（Winnipeg / Regina / Saskatoon 三点）电气制造商代表机构（rep firm），
> 1991 年创立；代理 Legrand/Starline、nVent、Littelfuse、Hammond Power Solutions、Weidmüller 等品牌；
> 🎯 从 ECAM 名录取得**具名邮箱 `dkelly@jebcoagencies.com`**；
> 🔴 **但 `jebcoagencies.com` 实测为 catch-all（随机地址亦 250）⇒ SMTP 探测在此域失效**；
> ⓪ 反身排除判定：**制造商代表（rep firm）—— 性质上是「代理」，⚠️ 需重点核查是否构成代理冲突 ⇒ 见 §二⓪**。

---

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示(如有)
Jebco Agencies Inc. | D Kelly（姓氏未获取）| ⛔ 职位未获取 | dkelly@jebcoagencies.com | 🔴 SMTP 不可判（域为 catch-all，随机亦 250）| ca.linkedin.com/company/jebco-agencies-inc | 加拿大中西部电气制造商代表机构（rep firm），1991 年创立；办公室位于 Winnipeg MB、Regina SK、Saskatoon SK；代理 Legrand/Starline、nVent（Erico/Eriflex/Hoffman/Caddy/ILSCO）、Littelfuse、Hammond Power Solutions、Weidmüller、Service Wire、Power Bus Way 等 25+ 品牌 | ECAM 会员名录（一手）+ 官网（一手）+ LinkedIn（三方）+ DNS/MX + SMTP 探测 | 🔴 制造商代表性质＝代理关系，需核验是否代理变压器品类
```

**发信资格：⚠️ 待核**（人已取得，**但邮箱 SMTP 不可判** + **代理冲突风险** ⇒ 需先做 H4 状态标注与 ⓪ 层复核）
**邮箱档位：C（域为 catch-all，无法通过 SMTP 提升档位）**

---

## 二、补充信息（扩展段）

### 标准字段明细

| 项 | 内容 | 来源 |
|---|---|---|
| **公司全称** | **Jebco Agencies Inc.**（品牌 **Jebco Agencies**）| 官网 + ECAM（一手）|
| **国家 + 城市** | **加拿大 MB 省 Winnipeg（总部）** | 官网（一手）|
| **州省** | **SK（CSV 口径，本单覆盖 Winnipeg MB / Regina SK / Saskatoon SK 三点）** | 官网（一手）|
| **详细地址（ECAM 登记）** | **4-3603 Kochar Avenue, Saskatoon, SK S7P 0B8** | ECAM（一手）|
| **电话** | **204-786-2604**（ECAM 口径，温尼伯线）| ECAM（一手）|
| **邮箱（具名）** | **`dkelly@jebcoagencies.com`** | ECAM 名录（一手）|
| **域名** | **jebcoagencies.com** | — |
| **邮件网关** | **Microsoft Exchange Online**（`jebcoagencies-com.mail.protection.outlook.com`）| DNS MX |
| **SPF** | `v=spf1 include:spf.protection.outlook.com -all` | DNS TXT |
| **DMARC** | ⚠️ 未解析到 | — |
| **成立年份** | **1991 年**（第三方 cybo.com 述）| 第三方（非一手，标注）|
| **规模** | 3 个办公室（Winnipeg / Regina / Saskatoon）| 官网（一手）|

### 业务定位（官网一手，逐字）

> *"Jebco Agencies is an **electrical manufacturers representative firm**,
> with offices in **Winnipeg, Regina and Saskatoon**"*
> *"Jebco Agencies Inc. is the leading electrical manufacturers rep firm covering the
> **Midwest region of Canada**, with offices in Winnipeg, Regina and Saskatoon."*
> 官网 `Our Manufacturers` 页载明代理品牌（25+），逐字可见：
> **Legrand / Starline、Liteline、Littelfuse、Meltric、nVent（Erico / Eriflex / Hoffman / Caddy / ILSCO）、
> Power Bus Way、Service Wire、Swivelpole、Weidmüller、Anamet、Chemelex、Eiko、Federal Signal、
> GlenDimplex Americas、Hammond Power Solutions、Intermatic、Kidde、LED Roadway Lighting、
> Wiremold、Pass & Seymour、Connectrac** 等。
> ✅ 官网新闻：*"**Jebco is now representing Power Bus Way** — Power Bus Way is a leading North American
> specialist in **Cable Bus** power…"*

### 🔴 ⓪ 反身排除判定（本环节强制首层）

| 检查项 | 结论 |
|---|---|
| 官网是否自称 manufacture / 制造 | ❌ **无**（自称 *"manufacturers representative firm"*）|
| 是否有自有品牌变压器规格书 | ❌ 无 |
| 是否销售自有品牌变压器 | ❌ 无 |
| **⚠️ 是否为「代理」性质** | 🔴 **是 —— 这是 rep firm（制造商代表），本质即「代理」** |
| 定性 | ⚠️ **需重点核查**：rep firm 代理他人品牌，**不生产**，本身**不是制造商同业**；<br>但 **rep firm 通常有「排他代理区域」约定** ⇒ **若其已代理某变压器品牌，则构成渠道冲突** |
| 🎯 处置 | ✅ **不排除（非制造商）**，但 🔴 **必须在首封前核验其是否已代理变压器类品牌**；<br>若已代理，则**应视为潜在竞争对手的渠道**，需评估后再决定是否开发 |

> 📌 **机读结论（关键）**：
> 1. **rep firm ≠ 制造商的竞争对手**（它不生产），因此**不触发 H1 排除**。
> 2. 🔴 **但 rep firm 的商业模式就是「替制造商卖货」** ⇒ **若它已代理某个变压器品牌，
>    我方直接开发会被视为「撬代理」。这是本单最大风险。**
> 3. ✅ **积极面**：官网代理清单中**列有 `Hammond Power Solutions`（变压器/电抗器制造商）**
>    ⇒ 🔴 **强烈提示该 rep firm 已涉足变压器品类代理** ⇒ **本单开发价值需下调**。

### 联系人（含仍_here 在职核验）

| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| **D Kelly**（姓氏未获取）| **首封候选（具名）** | ⛔ **职位未获取** | ⚠️ 未知 | 🟡 中：ECAM 名录在列；⚠️ 邮箱无法 SMTP 验证 | ⚠️ 未知 | ⛔ 未定位 |

> 🔴 **机读结论**：人已取得（`dkelly@`），**但①职位未知 ②邮箱 SMTP 不可判（catch-all）
> ③公司性质存在代理冲突风险** ⇒ **三处硬伤，本单建议列为「低优先 / 待核」**。

### 邮箱分档（A/B/C）

| 档 | 地址 | 依据 | 可否主送 |
|---|---|---|---|
| A | ⛔ 未获取 | — | — |
| B | `info@jebcoagencies.com` / `sales@` / `winnipeg@` / `regina@` / `saskatoon@` | ⚠️ **全部 250，但域为 catch-all ⇒ 无法区分真假** | ⚠️ 仅兜底 |
| **C** | **`dkelly@jebcoagencies.com`** | **ECAM 名录明文（一手）**，但 **SMTP 不可判（catch-all）** | ⚠️ **可用但状态标注「未验证」** |

**🔴 邮箱验证方法与证据链（可复现）：**

```
域名 jebcoagencies.com
MX   = jebcoagencies-com.mail.protection.outlook.com   （Microsoft Exchange Online）
SMTP 控制地址协议（HELO jiezougroup.com）：
  RCPT info@jebcoagencies.com       -> 250 2.1.5 Recipient OK
  RCPT zzq9k2x7@jebcoagencies.com   -> 250 2.1.5 Recipient OK   🔴【随机地址亦 250】
  RCPT sales@jebcoagencies.com      -> 250 2.1.5 Recipient OK
  RCPT winnipeg@jebcoagencies.com   -> 250 2.1.5 Recipient OK
  RCPT regina@jebcoagencies.com     -> 250 2.1.5 Recipient OK
  RCPT saskatoon@jebcoagencies.com  -> 250 2.1.5 Recipient OK
⇒ 🔴 【catch-all 判定】：随机地址返回 250 ⇒ 本域【无判别能力】。
   SMTP 探测在本域【完全失效】，不得据此判定任何地址真实存在。
⇒ ⚠️ 依 H4：`dkelly@jebcoagencies.com` 只能标注为【来源：ECAM 名录（一手）；
   邮箱验证状态：SMTP 不可判（域为 catch-all）】，不得标注「已验证」。
```

---

## 三、开发信建议（**仅限：收件人 / 时机 / 附件 —— 不含正文、不含主题行、不含开场句**）

| 项 | 建议 | 依据 |
|---|---|---|
| **主送** | ⚠️ **建议暂缓**，先完成 ⓪ 层代理冲突核验 | 见 §二 ⓪ 层 |
| **若继续** | `dkelly@jebcoagencies.com`（点名 D Kelly）| ECAM 一手；⚠️ 状态为「SMTP 不可判」 |
| **核验动作** | ① 查该 rep firm **是否已代理变压器品牌**（网站已列 **Hammond Power Solutions**）<br>② 电话 **204-786-2604** 询问代理线范围 | 🔴 关键前置动作 |
| **建议时机** | （核验后）中部时间（CT）工作日 08:30–10:30 | — |
| **建议附件** | ⚠️ 暂不建议附 UL 证书 —— **需先解除代理冲突疑虑** | — |
| **切入角度提示**（**仅提示，不代拟文案**）| ① 该公司为 **rep firm（制造商代表）** ⇒ 若我方希望进入加拿大中西部渠道，**rep firm 是标准通路**<br>② 但 🔴 **前提是它尚未代理同类变压器品牌**（官网已列 Hammond Power Solutions，需核实）<br>③ 覆盖 **MB + SK 两省** ⇒ **区域渠道价值高** | 官网（一手）|
| ⛔ **禁止事项** | ① 不得称 certified（柱上变 E544629 仅 ECD 计划函）<br>② 不得提 YAWEI<br>③ 首封不报交期/价格<br>④ **不得虚构 D Kelly 的姓氏或职位**<br>⑤ **不得声称其邮箱「已验证」**（H4，域为 catch-all）<br>⑥ 🔴 **不得在未核实代理线前贸然开发**（渠道冲突风险）<br>⑦ 不得发送供货记录 PDF | — |

---

## 四、⚠️ 矛盾点与风险提示

| # | 风险 | 说明 |
|---|---|---|
| 1 | 🔴 **代理冲突风险（最大风险）** | rep firm 本质为「代理」；官网已代理 **Hammond Power Solutions**（变压器制造商）⇒ 可能已占位 |
| 2 | 🔴 **域名 catch-all，SMTP 探测失效** | 随机地址亦 250 ⇒ **无法验证任何邮箱真假**（H4 标注「不可判」）|
| 3 | ⚠️ **具名人姓氏与职位未知** | 正式称呼有风险 |
| 4 | ⚠️ **成立年份来自三方** | 「1991 年」出自 cybo.com，非工商一手 |
| 5 | ⚠️ **DMARC 未解析到** | 反钓鱼策略不明 |
| 6 | ⚠️ **主营为代理销售，非采购** | rep firm 是「替供应商卖」而非「替客户买」⇒ 与我方商业模式可能重叠而非互补 |

---

## 五、信息缺口清单（请勿编造）

| 缺口 | 状态 |
|---|---|
| **是否已代理变压器品牌** | 🔴 **未核实（本单最关键前置）** |
| **D Kelly 的姓氏与职位** | ⛔ **未获取** |
| **邮箱真实性** | ⛔ **不可判**（域为 catch-all）|
| **成立年份（一手）/ 员工数 / 注册号** | ⛔ 未获取 |
| **决策人 LinkedIn** | ⛔ 未定位 |

---

## 六、一句话画像

**加拿大中西部电气制造商代表机构（rep firm，1991 年创立），办公室位于 Winnipeg MB / Regina SK /
Saskatoon SK 三点，代理 Legrand/Starline、nVent、Littelfuse、**Hammond Power Solutions**、
Weidmüller、Service Wire、Power Bus Way 等 25+ 品牌。
从 ECAM 名录取得具名邮箱 `dkelly@jebcoagencies.com`（⚠️ 职位未知）。
🔴 **两处硬伤**：① 域名 `jebcoagencies.com` 为 **catch-all** ⇒ SMTP 探测完全失效，邮箱真实性不可判；
② 该公司为 **rep firm（性质即代理）**，且**官网代理清单已含 Hammond Power Solutions（变压器制造商）**
⇒ **存在渠道代理冲突风险**。
⓪ 层判定：非制造商 ⇒ 不触发排除；**但需先核实其变压器代理线后再决定是否开发**。**

---

## 七、渠道覆盖清单

| 渠道 | 状态 |
|---|---|
| **L-1 锁人** | 🟡 **D Kelly（职位未知）** —— ECAM 一手；⛔ 无高管 |
| **L0 官网** | ✅ 首页 + About + Manufacturers 抓取；拿到 3 办公室与 25+ 代理品牌 |
| **L1 政府一手** | ⛔ 未查 |
| **L2 命名+DNS** | ✅ 域名存活（M365，SPF `-all`）；🔴 **SMTP 实测 catch-all，探测失效** |
| **L3 B2B 库** | 🟡 cybo.com（成立年份来源，三方）|
| **L4 社媒协会** | ✅ **ECAM 会员名录**；✅ LinkedIn 公司页 |
| **L5 黄页同址** | 🟡 多处目录条目 |
| **L6 电话表单** | ✅ 204-786-2604 |
| **L7 付费** | ⛔ 未启用 |
