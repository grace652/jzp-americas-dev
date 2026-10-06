# ⛔ 排除记录 — 买家 205 · JDD Electrical Wholesale（JDD Electrical Supply）

> 判定日期：2026-09-29 ｜ 判定环节：环节① 找客户 · **⓪ 层反身排除** ｜ 结论：**⛔ 排除（永久）**
> 名单来源：目标客户清单-batch6.csv 序号 32（官网 jddelectricalwholesale.com，备注「Calgary 电气批发」）
> 一句话：表面是「Calgary 电气批发商」，实为 **「中国货源 → 北美」直营通道**（自有亚洲工厂伙伴 + **驻华采购总监** + 私标 + 直供承包商），命中 ⓪ 层第 3 类，**排除**。

---

## 一、判定依据（⓪ 层：反身排除）

### 1.1 命中类别
**第 3 类 · 「中国货源 → 北美」通道**（判据词：`Asian manufacturing` / `partner factory` / `factory-direct`）

### 1.2 官网业务描述原句（jddelectricalwholesale.com，第一方）

| # | 原句（逐字） | 指向 |
|---|---|---|
| 1 | *"We supply the EMT conduit, strut, B-material, and wire that contractors need… **Our production schedule runs on a rolling basis**, so common sizes and lengths stay on the shelf even during peak construction season."* | 自有**生产排程** |
| 2 | *"**We control quality at every stage instead of relying on a name-brand label** to do it for us. **Our full-time quality control team** checks that what leaves our doors meets CUL, CSA, and CETL standards…"* | **私标（private-label）自控质量** |
| 3 | *"Every batch is documented and traceable, so if a question ever comes up about a specific shipment, we can pull **the exact production record** within minutes."* | **生产批次记录** |
| 4 | *"**Save Up to 40% With Our Direct-to-Contractor Pricing Model** … We eliminate [the middleman] by delivering products straight to your jobsite. **That vertical integration** means you get the same quality components…"* | **垂直整合 / factory-direct** |
| 5 | *"…we sell it straight to you at **direct-to-contractor pricing. No distributor markup**…"* | 绕过分销的**直供**模式 |

### 1.3 团队页自证（jddelectricalwholesale.com/meet-the-team/，第一方）——决定性证据

| 姓名 | 职务 | 逐字自述（节选） |
|---|---|---|
| **Jonathan Peters** | **Co-Founder & Director** | *"an entrepreneur and **global supply-chain builder**… began sourcing internationally and has since **built long-term manufacturing partnerships across Asia and North America**… from **factory floor** to customer delivery."* |
| **Frank Liao** | **Director of Procurement** | *"**Based in China**, Frank leads JDD's overseas operations, overseeing **factory engagement, production coordination, quality control**, and on-the-ground supplier management… developing and maintaining JDD's **long-term supplier relationships across Asia**."* |
| Darrin Oneschuk | Co-Founder & President | *"30 years of electrical industry experience… leads sales strategy, customer relationships, and market expansion."* |
| Ivan Luna | Finance & Administration Manager | 财务行政 |

> 🔴 **关键**：本司**专设「驻华采购总监」**，职责是「工厂对接 / 生产协调 / 质量控制 / 亚洲供应商管理」——
> 即 **JDD 自己就是中国工厂在北美的那一端**。它买的就是中国货，与我方**同源同市场**，
> **没有「我方供它转卖」的空间**（它有自己的亚洲工厂伙伴）。

### 1.4 附带确认（排除时的副产品）
- **真实邮箱域 = `jddsupply.com`**（官网 contact 页明文 `info@jddsupply.com`），MX = `jddsupply-com.mail.protection.outlook.com`（M365），SPF `-all`。
  → 名单所给官网域 `jddelectricalwholesale.com` **确无 MX**（实测），邮件域是另一个 `jddsupply.com`。
- 产品线 = EMT 导管 / 刚性导管 / strut 杆件 / 桥架 / 建筑线缆 / 电气工具——**不含变压器**（无我方产品可切入的现成品类）。

---

## 二、为什么这是「排除」而不是「降级」

| 判据 | JDD 情况 |
|---|---|
| 是否制造商（NAICS 335311/335313）| 否（做导管/线缆，非变压器；且不自称变压器制造） |
| 是否 YAWEI 等竞品代理 | 否 |
| **是否「中国货源 → 北美」通道** | ✅ **是** —— 自有亚洲工厂伙伴 + 驻华采购总监 + 私标 + 直供 |
| 是否有「我方供它转卖」空间 | ❌ **无** —— 它自建中国供应链，新品类亦会向自有工厂伙伴采购 |

> 📌 与排除名录 §二 既有案例（Rionex、Crown Mountain）**同构**：
> 均为「以中国工厂为上游、在北美直销」的通道型公司。
> ⚠️ **差异说明（留痕供人工复核）**：Rionex/Crown Mountain 主营**变压器**（与我方产品完全重合）；
> JDD 主营**导管/线缆**（与我方产品**互补但不重合**）。本次判定**以「结构位置」为准**
> （驻华采购总监 + 亚洲工厂伙伴 = 供应链另一端），故仍判**排除**。
> 若人工认为「互补品类可另议」，请在本记录下方批注并移出名录——**默认维持排除**。

---

## 三、处置动作
1. ✅ 本记录落盘：`batch6_new_174plus/⛔排除205_JDD_Electrical_Wholesale_排除记录.md`
2. ✅ 已追加至 `线索资产/永久排除名录.md`
3. ⛔ **不产出交接单、不进写信环节、不发送**

---

## 四、证据 URL
- https://jddelectricalwholesale.com/ （业务原句）
- https://jddelectricalwholesale.com/meet-the-team/ （团队页，驻华采购总监自述）
- https://jddelectricalwholesale.com/contact/ （真实邮箱域 jddsupply.com）
- DNS 实测：`dig @8.8.8.8 MX jddelectricalwholesale.com` → 空；`dig @8.8.8.8 MX jddsupply.com` → `jddsupply-com.mail.protection.outlook.com`
