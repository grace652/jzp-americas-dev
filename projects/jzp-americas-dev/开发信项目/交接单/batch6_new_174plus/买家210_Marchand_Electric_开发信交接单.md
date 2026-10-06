# 【买家 210】开发信交接单 — Marchand Electric（Marchand Electrical Company Limited）⛔ 已停业 / 破产管理

> 采集日期：2026-09-29 / 来源：batch6 名单（序号 37，标注「⚠️ 疑 Shopify 站」）
> **一句话结论：⛔ 该公司已于 2026 年进入破产管理（receivership），库存于 2026-08-18 全部拍卖清盘。名单给的 `marchandelectric.com` 是一个已下线的 Shopify 店铺（"This store is unavailable"）。本单不进入写信环节，已追加至《永久排除名录》。**

---

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示(如有)
Marchand Electric（法定主体：Marchand Electrical Company Limited） | —— 不适用（公司已停业） | —— | —— | 未找到（不适用） | —— | 加拿大安大略渥太华 1892 年创立的照明/电气零售批发商，134 年历史，2026 年进入破产管理，2026-08-18 库存清盘拍卖，官网域已成下线 Shopify 店 | Ottawa Business Journal / ottown.ca / MNP Ltd. 破产管理卷宗 / Infinity Assets 拍卖公告 / DNS 实测 | 🔴 **公司已停业 ⇒ 闸门第 5 条拦截，禁止触达**
```

---

## 二、补充信息（扩展段）

### 标准字段明细
- 国家+城市：**加拿大**。⚠️ **州省修正**：CSV 原值 `QC`，实测主体总部在 **Ontario（渥太华 Ottawa）**，在 **Quebec（Gatineau）设分支**（140 Bd Gréber, Gatineau QC J8T 6H5）⇒ **CSV 的 QC 只对应其 Gatineau 分支，主体是 ON**
- 详细地址：Gatineau 分支 140 Boulevard Gréber, Gatineau, QC J8T 6H5（第三方名录）
- 电话：819-561-0185（Gatineau 分支，第三方名录）
- LinkedIn：公司帖 `linkedin.com/posts/scotty-morris-25305b2bb_...activity-7490418614471401472-IYwz`（2026-08-04）
- 网站：`marchandelectric.com` ⇒ **已下线**（HTTP 返回 "This store is unavailable"）
- 成立日：**1892**（OBJ 原文 "founded in 1892"，经营 **134 年**）
- 规模：未获取（清盘前）
- 营收：未获取
- NAICS：未获取

### 停业证据链（🔴 三条独立来源）

| # | 来源 | 原文 / 事实 | 日期 |
|---|---|---|---|
| 1 | **Ottawa Business Journal**（obj.ca） | *"Marchand Electric, founded in 1892, **went into receivership** earlier this year, and its remaining stock will be sold at …"* | 2026-08-13 |
| 2 | **MNP Ltd. 破产管理卷宗**（mnpdebt.ca） | 案卷目录名 `receivership/**marchand-electrical-company-limited**`；*"Chapman sworn on February 27, 2026 … the consent of **MNP Ltd.**, dated January 27, 2026, **to act as receiver** …"* | 2026-07-10（order） |
| 3 | **Infinity Assets 拍卖公告**（infinityassets.com） | 标的 `marchand-electric.pdf` / `marchand-electric.html`；**"CLOSES: Tuesday August 18th, 10AM EST"**；**"Removal – All Items by Tuesday August 25th"** | 2026-08-13 |
| 4 | **ottown.ca**（媒体转载 OBJ） | *"Ottawa is closing the book on one of its longest-running businesses this week, as the entire stock of Marchand Electric goes up for auction after an incredible **134 years** in operation."*（1,200+ 件库存，含吊灯等照明器材） | 2026-08-14 |
| 5 | **LinkedIn 帖**（2026-08-04） | *"**After 134 years in business, Marchand Electric has closed its doors.** On August 18, the company will be sold at auction."* | 2026-08-04 |

### 「疑 Shopify 站」的核实结论（任务书点名项）

| 检查项 | 实测 | 判读 |
|---|---|---|
| `dig @8.8.8.8 A marchandelectric.com` | **23.227.38.65** | ✅ 确认是 **Shopify** 的 IP（任务书预判正确） |
| HTTP 访问 | 返回 **"This store is unavailable — Something went wrong. What happened? This store is unavailable"** | 🔴 **店铺已下线**，非在运营的公司主体站 |
| `dig @8.8.8.8 MX marchandelectric.com` | `mx1–mx4.mtaroutes.com`（优先级 10/20/30/40） | ⚠️ 域**仍配置邮件路由**，但这**只说明域名尚未过期**，**不代表公司在营**（清盘后域名常残留） |
| 主体域核实结果 | **找不到任何在运营的公司主体域** | 🔴 **如实标注：公司主体站已不存在** |

> 🔴 **结论**：任务书要求的「核实真实主体域」——**核实结果是：不存在**。`marchandelectric.com` 是该公司遗留域名，现托管一个**已下线的 Shopify 店**；Gatineau 分支曾用此域（chamberofcommerce 名录记载其 URL 即 `http://www.marchandelectric.com/`）。公司本体已清盘。

### 联系人（含 still_here 在职核验）

| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| —— 不适用 —— | —— | 公司已停业，无在职决策人 | —— | —— | 🔴 **N/A** | —— |

> 🔴 **不挖人、不找邮箱**：公司已停业，任何「在职核验」都无意义。**禁止**为凑数去挖已离职人员或残留邮箱。

### 邮箱分档（A/B/C）

- **A 档**：未找到（公司已停业，不作挖掘）
- **B 档**：无
- **C 档**：无
- **H6 声明**：**不适用** —— 非「仅角色邮箱」情形，而是**主体已消灭**。

### 我为什么找他

> 🔴 **不适用** —— 本单为**排除单**，不进入写信环节，无需开场观察。

### 买家类型 / 需求品类

- 买家类型：**（历史）A 分销/零售商 —— 照明器材与电气用品**（Gatineau 名录归类为 "lighting store"；拍卖清单含大量照明器材）。⓪ 层：非制造商 ✅
- 需求品类：**不适用**（公司已停业，无采购行为）

### 电压·频率·认证要求

- 不适用（无在营主体）

### 采购信号

- 🔴 **负向信号**：破产管理（2026-01 委任 MNP Ltd. 为接管人）→ 资产清盘（2026-08-18 拍卖）→ 公司关闭。**无任何采购可能。**

### 可利用的钩子（按强度排序）

- 🔴 **无**（不进入写信环节）

### 开发信建议

> ⛔ **不发信。** 公司已停业。本单**不得进入写信环节**，**不得进入任何发送队列**。

### ⚠️ 矛盾点与风险提示

1. 🔴 **CSV 州省错误**：CSV 原值 `QC`，实测**主体在 ON（渥太华）**，QC（Gatineau）只是分支 —— 见渠道清单 §十二/§二十六「每单必核州省」。
2. 🔴 **CSV 域名是遗留域名**：`marchandelectric.com` 现为**下线 Shopify 店**，非公司主体站。**任何按此域拼写的邮箱都不可投递/无意义。**
3. ⚠️ **MX 记录会误导**：该域仍有 `mtaroutes.com` MX，容易被误判为「公司在营、可投递」。**MX 存在 ≠ 公司存在** —— 这条建议沉淀进 skill。
4. ⚠️ **同名风险**：魁北克另有 `marchandenergie.com`（Marchand Énergie）与 `marchand…`（Marchand Entrepreneur Électricien Ltée），**均为不同主体**，勿混为一谈。本单主体为 **Marchand Electrical Company Limited（渥太华，1892）**。

### 信息缺口清单（请勿编造）

- ❌ 清盘前员工数 / 营收 / NAICS —— 未获取（且**已无意义**）
- ❌ 是否有其他关联法人仍在经营 —— 未查（**若要复活此线索，须先确认是否存在独立主体，不得凭感觉拆**）
- ❌ 破产管理卷宗全文细节 —— 仅取到索引与摘要（PDF 未逐页解析）

### 一句话画像

1892 年开在渥太华、撑了 134 年的照明电气老店，2026 年 1 月被接管、8 月清仓拍卖——名单给的那个 Shopify 域名，是它留下的空壳。

### 渠道覆盖清单（L-1、L0–L7）

| 层 | 结果 | 一句话 |
|---|---|---|
| L-1 锁人 | ⛔ | 不做（公司已停业） |
| L0 官网 | ❌ | `marchandelectric.com` = 下线 Shopify 店（"This store is unavailable"） |
| L1 政府一手 | ✅ | MNP Ltd. 破产管理卷宗（法院 order）+ OBJ/ottown 报道 |
| L2 命名+DNS | ⚠️ | A=Shopify IP 23.227.38.65；MX=mtaroutes（**残留路由，不代表在营**） |
| L3 B2B 库 | ⚠️ | 第三方名录（chamberofcommerce / findstorenearme）仅证历史存在 |
| L4 社媒协会 | ✅ | LinkedIn 关闭公告帖（2026-08-04） |
| L5 黄页同址 | ⚠️ | 仅 Gatineau 分支历史地址 |
| L6 电话表单 | ❌ | 不做 |
| L7 付费 API | ❌ | 未启用 |

---

## 三、发信资格闸门

- **发信资格**：⛔ **拦截（第 5 条：公司已停业 / 破产管理清盘）**
- **邮箱档位**：**未找到（不适用）**
- **处置**：
  1. ⛔ **不进入写信环节、不进入发送队列**
  2. ✅ 已追加至 `线索资产/永久排除名录.md`（§五 其他已判定不可做）
  3. ✅ 本文件保留为**详细证据档**（对应名录的「速查索引 ↔ 详细证据」双层结构）
