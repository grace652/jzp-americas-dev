# ⛔ 排除记录 — 买家 374 ERTH Infrastructure Services Group（erthcorp.com）

> 采集日期：2026-10-05 ｜ 来源：batch10 名单（erthcorp.com，加拿大 ON Ingersoll）｜ 判定：**排除（公用事业本体 / 市政公用事业集团）**
> ⚠️ 本记录严格区分「已验证」与「未获取」；未找到的信息一律标注，不做推断填充。
> - 发信资格：⛔ **拦截（第 5 类：主体为公用事业本体；与 batch9 已排除的「ERTH Corp」同一实体）**
> - 邮箱档位：—（不进入写信环节）

---

## 一、判定结论（一句话）

**名单给的域 `erthcorp.com` 是「ERTH Corporation」—— 一家由九家市政股东持有的市政公用事业集团（旗下含受管制配电公司 ERTH Power），即 batch9 已排除的「ERTH Corp」（判定为公用事业本体）本身。名单所列的 "ERTH Infrastructure Services Group" 并非独立承包主体，而是该市政公用事业集团旗下的**承包事业群/分部**。⇒ 同一实体 ⇒ 排除。**

> 🔴 本排除**依据 batch9 先例**（`线索资产/名单说明-batch9.md` 第 48 行：硬性排除含「**公用事业本体**」）与作业指导 §四「若为公用事业本体则写排除记录」。

---

## 二、证据（官网业务描述原句 + 一手来源）

### 2.1 `erthcorp.com` 首页自述（一手源：官网首页）
> *"ERTH Corporation is a **diverse group of companies with origins in the utility industry. Owned by nine municipal shareholders**, ERTH has grown to be a leading provider of products and services in many industries including utility, energy retailer, municipal, commercial and industrial to name a few."*

- 首页把 **ERTH Power** 标为 *"**Your Hometown Utility**"*（即受管制配电公司 / LDC）。
- 首页新闻含 *"**ERTH (Westario) Acquisition Inc.** has applied for approval to acquire **Westario Power Inc.**"*（向安省能源局 OEB 申请收购另一家 LDC）⇒ 典型的**公用事业集团并购行为**。

### 2.2 `erthcorp.com/utility-construction-and-lighting/`（一手源：官网业务页）
> *"**ERTH Infrastructure Services Group** is raising the standard for utility construction and lighting by delivering custom, high-quality, turnkey electrical solutions… **Owned by nine municipalities and having an affiliate local distribution company, ERTH Power**, we understand first-hand the complexities and challenges that utilities, municipalities and businesses face."*

- 该页明确把 **ERTH Infrastructure Services Group** 定位为集团旗下**承包事业群**（Electrical Contracting / Pole Line / Substation Construction / Street Lighting / Traffic Signals）。
- 同页重申 *"Owned by nine municipalities, ERTH is strong and stable…"*。

### 2.3 `erthcorp.com/management-team/`（一手源：官网管理层页）
- **Chris White — President & CEO**，履历：*"played a major role in the creation of ERTH Power through the **merger of ten Ontario-based electric utilities**… became President of the **regulated utility, ERTH Power Corporation**, serving the interests of **nine municipal shareholders**"*。
- **Laurie Palmer — COO**（负责 business operations 与 **infrastructure divisions**）。
- **Graig Pettit — VP & GM, ERTH Power**（*"responsible for the day to day operation of the **regulated arm** of the ERTH group of companies"*）。
- ⇒ 管理层即为**市政公用事业集团高管**，其受管制核心是 LDC（ERTH Power）。

### 2.4 域名归属交叉（一手源：DNS）
- `erthcorp.com` MX = `erthcorp-mx1.titanhq.com` / `erthcorp-mx2.titanhq.com`
- `erthpower.com` MX = **同一组** `erthcorp-mx1.titanhq.com` / `erthcorp-mx2.titanhq.com`
- ⇒ **ERTH Corporation 与 ERTH Power（LDC）共用同一邮件基础设施** ⇒ 同一集团、同一实体族。

### 2.5 与 batch9 排除的关系
- 作业指导 §附明确：**374 ERTH Infrastructure Services Group（ON）—— 与 batch9 已排除的「ERTH Corp / Alectra Energy Solutions」可能同源，先核**。
- `线索资产/名单说明-batch9.md` 第 48 行：batch9 硬性排除类别含「**公用事业本体**」。
- 本批实测：`erthcorp.com` **就是** ERTH Corporation（市政公用事业集团），即 batch9 判定为公用事业本体的同一实体。⇒ **不是「另一家承包商」，而是「同一实体」**。

---

## 三、为什么排除（判据说明）

| # | 判据 | 事实 |
|---|---|---|
| 1 | **主体为市政公用事业集团** | ERTH Corporation 由**九家市政股东**持有；旗下含受管制 LDC（ERTH Power）；管理层为公用事业高管；有 LDC 并购行为 |
| 2 | **与 batch9 已排除实体同一** | batch9 排除「ERTH Corp」（公用事业本体）；本域 `erthcorp.com` 即该实体 |
| 3 | **名单所列 "Infrastructure Services Group" 非独立法人** | 官网将其表述为集团旗下**承包事业群**，非独立注册主体、无独立域名 |
| 4 | **与项目「公用事业本体」硬性排除一致** | 见 `名单说明-batch9.md` §硬性排除 |

> 📌 **判据边界（重要）**：该事业群**确实从事变电站建设/维护/维修（会采购变压器）**，单看业务描述像 B 类承包商；但**其法律/股权主体是市政公用事业集团**，与 batch9 排除口径一致。**故按「主体」而非「业务群」判定排除。**

---

## 四、⚠️ 人工重开选项（留痕，供决策人裁定）

> 🔴 本条为**唯一需要人工确认的点**。若决策人认为应**按「承包事业群」独立评估**（而非按集团主体排除），
> 则下列数据可直接启用，无需重挖：

- 决策人候选：**Dale Flynn — General Manager, Infrastructure Services at ERTH Corporation**
  - LinkedIn：`ca.linkedin.com/in/dale-flynn-a2052539`（第三方摘要，未直取）
  - 依据：LinkedIn 摘要 + Wiza/Lead411/ContactOut 三方 B2B 均记该职务（**均 B2B，非一手源**）
- 集团高管（若走集团口径）：**Chris White — President & CEO**（官网管理层页一手明文）
- 业务：turnkey substation construction / maintenance / repair（含 transformers），服务 utilities + ICI 客户
- 域：`erthcorp.com`（MX = titanhq）
- ⚠️ 若重开：仍须按「同一集团只发 1 家」排重（本集团已含 LDC ERTH Power、Solutions & Technologies、Energy Services 等多业务）

**决策归属**：是否重开 = **人工判定**。本子 agent 按作业指导 §四「若为公用事业本体则写排除记录」执行**排除**。

---

## 五、来源清单（URL）

- `https://www.erthcorp.com/`（首页，含 "Owned by nine municipal shareholders"、ERTH Power 收购新闻）
- `https://www.erthcorp.com/utility-construction-and-lighting/`（"ERTH Infrastructure Services Group" 业务页）
- `https://www.erthcorp.com/management-team/`（管理层：Chris White / Laurie Palmer / Graig Pettit 等）
- `https://www.erthcorp.com/electrical-contracting/`（*"you can trust that ERTH Infrastructure Services…"*）
- DNS：`dig @8.8.8.8 MX erthcorp.com` / `erthpower.com`（同一 titanhq 组）
- 内部：`线索资产/名单说明-batch9.md` 第 48 行（硬性排除含「公用事业本体」）

---

## 六、同名排除表

| 同名 | 地点 | 排除/说明理由 |
|---|---|---|
| **ERTH Corp / ERTH Corporation** | 加拿大 ON Ingersoll | 🔴 **本主体** —— 市政公用事业集团（9 家市政股东 + LDC ERTH Power），batch9 已排除（公用事业本体） |
| **ERTH Power Corporation** | 加拿大 ON | 同集团受管制 LDC（"Your Hometown Utility"）→ **同集团，不单独开发** |
| **ERTH Infrastructure Services Group** | 加拿大 ON | 同集团**承包事业群**（非独立法人）→ 随主体一并排除 |
| **ERTH Solutions & Technologies / ERTH Energy** | 加拿大 ON | 同集团其他业务线 → 同集团 |
| **Alectra Energy Solutions** | 加拿大 ON | batch9 同批排除的市政公用事业竞争臂（另一主体，非本单） |
