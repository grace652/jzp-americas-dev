# ⛔ 排除记录 — Rionex Energy

> 采集日期：2026-09-28 ｜ 名单来源：`线索资产/目标客户清单.csv` 序号 43（CSV 标注 **B 类 · 分销商/贸易商**）
> 采集方：找客户环节（本环节只产出交接单/排除记录，不写正文/不碰模板/不定话术）
> ⚠️ 本表严格区分「已验证」与「未获取」，未找到的信息一律标注，**不做推断填充**（H1）
> 🔴 **结论：排除（六层过筛 ⓪「反身排除」命中）。Rionex Energy 是江苏正来电气（JIANGSU ZHENGLAI ELECTRIC CO. LTD）在美国的独家授权分销通道 —— 与 JIEZOU 同为中国产能 → 北美市场，构成直接渠道竞争。**
> **⇒ 不进写信环节，无交接单，仅留此排除记录归档。**
> **批次**：batch5_new_129plus（第六批 · 美国 B 类） ｜ **官网**：`rionexenergy.com`

---

## 一、排除理由（一句话）

**Rionex Energy 不生产变压器，而是「江苏正来电气」在美国市场的授权分销商（authorized U.S. distributor）—— 其全部 4 个 UL 档案均签发于同一家中国工厂。这是我方在中国产能端 → 北美市场的**同赛道通道**，不是可开发的潜在客户。**
**⇒ 向其发开发信 = 向竞争对手推销同类货源。**

---

## 二、决定性证据：UL 证书签发对象（第一手官方文件）

**取证方式**：直接下载 Rionex 官网自行公开的 4 份 UL Certificate of Compliance PDF（`rionexenergy.com/documents/*.pdf`），用 `pypdf` 提取「Issued to」字段。

| UL 档案 | 产品 | **签发对象（Issued to）** | 签发日期 |
|---|---|---|---|
| **E526441**（UL-US-2563976-1） | 三相液浸美变 45–4,000 kVA，≤24.94 kV | 🔴 **JIANGSU ZHENGLAI ELECTRIC CO. LTD**<br>229 Huanghai Avenue West, Hai'An, Jiangsu 226600, **China** | 2025-04-21 |
| **E539752**（UL-US-2581703-0） | 干式通用变（UL 1561），SG 系列 | 🔴 **同上** | 2025-08-25 |
| **E545481**（UL-US-2591855-0） | 中压干式配电变（UL 1562），SGLB 系列 30–3,000 kVA | 🔴 **同上** | 2025-11-10 |
| **E538000**（UL-US-2588083-0） | UL 认可绝缘系统 | 🔴 **同上** | 2025-10-17 |

> 🔴 **4 份证书的签发对象全部是「JIANGSU ZHENGLAI ELECTRIC CO. LTD」（江苏正来电气有限公司），地址为中国江苏海安。**
> 证书签发人为 **David Piecuch, UL Mark Certification Program Owner**（UL LLC），**文件本身即为官方一手证据**。

**⇒ 结论：Rionex Energy 所售变压器的 UL 认证持有方 = 一家中国工厂。Rionex 只是该工厂在美国的销售通道。**

---

## 三、官网自述（逐字引用，与 UL 证据互相印证）

来源：`rionexenergy.com/en/about`

> *"Rionex Energy is the **authorized United States distributor for a UL-audited transformer manufacturing partner**."*
> *"**Authorized distribution** —— Full written authorization from the manufacturer for the U.S. market, **not gray-market or broker inventory**."*
> *"**Factory-direct** —— Quotes come straight from **factory production planning**, so pricing and lead times hold up after the PO."*
> *"As the **authorized U.S. distributor** we quote straight from **factory production slots**: no extra middle layer, no marked-up broker stock."*（首页）

来源：`rionexenergy.com` 首页

> *"See where your equipment is built. **Climate-controlled winding rooms, vacuum pressure impregnation, CNAS-accredited routine testing**, and a shielded partial-discharge test room."*
> *"**Factory acceptance tests**, third-party inspection, and ANSI/IEEE/CSA compliance support."*

> 上述「partner factory / 生产排期 / 绕线车间 / CNAS 实验室」**均属其中国合作工厂，Rionex 自身无制造资产**。
> 官网**未披露**任何自有工厂、员工规模、公司历史、创始人。

---

## 四、与我方竞争关系的判定

| 维度 | Rionex Energy | JIEZOU（我方） | 关系 |
|---|---|---|---|
| 货源端 | **中国**（江苏正来电气，Jiangsu Zhenglai） | 中国自有工厂 | 🔴 **同一货源端** |
| 目标市场 | **美国**（Houston, TX） | **北美**（美/加） | 🔴 **同一目标市场** |
| 商业模式 | 「**中国工厂 → 美国**」**独家授权分销** | 工厂直销北美 | 🔴 **同赛道** |
| 产品 | 美变 45–4,000 kVA · 中压干变 30–3,000 kVA · 变电站变 · 电抗器/滤波 | E541627 配电变 · E541626 电力变 | ⚠️ **液浸美变段高度重叠** |
| 认证话术 | *"UL file numbers you can verify"* · *"E526441, E539752, E545481"* | 持有 UL 正式 CoC | 🔴 **同一套合规语言** |

### 🔴 与 Crown Mountain 的**关键同构**

| 公司 | 本质 | 结论 |
|---|---|---|
| ⛔ **Crown Mountain Solutions**（CSV 45） | 「中国供应链 → 北美」的采买代理 | **排除** |
| ⛔ **Rionex Energy**（CSV 43） | 「中国工厂（江苏正来）→ 美国」的**独家授权分销** | **排除** |

> **两者是同一类：中国产能的北美出口通道。**
> 区别仅在于：Crown Mountain 是**多工厂采买代理**，Rionex 是**单一工厂独家分销**。
> ⇒ **判据统一**：**凡「以中国供应链为核心卖点、面向北美市场销售变压器」者，一律排除**（因其存在理由与我方完全重合，无谈判空间）。

### 与「保留类」的分界（复习判据）

| 类型 | 例 | 处理 | 理由 |
|---|---|---|---|
| 代理**特定品牌**（非中国源） | Jebco（代理 Hammond PS）、AESCO | ⚠️ 保留 | 我方产品**可替代/补充其代理线** → 有谈判空间 |
| 本身就是「中国源 → 北美」通道 | **Crown Mountain、Rionex** | 🔴 **排除** | 与我方**同源同市场**，无谈判空间 |

---

## 五、附带发现（不予采用，仅记录）

- ⚠️ **Rionex 官网存在中文版**（`rionexenergy.com/zh/products`，页面可见中文描述如「死面（dead-front）结构，环网或辐射式进线」）—— **进一步佐证其中国背景**（团队/供应链为中文母语）。
- ⚠️ **公司实体信息极度不透明**：官网无创始人、无团队页、无公司历史、无员工规模、无注册信息；仅公示 **`support@rionexenergy.com`** 与 **"Houston, TX, USA"**。
- ⚠️ 搜索未找到其任何**第三方公司档案**（Bizapedia / LinkedIn / D&B 等均无有效记录）—— 公司**成立时间与法人未获取**。
- ⚠️ ⚠️ **重要区分**：`ionexenergy.com`（**Ionex Energy**，电动两轮车换电业务）与本案 **`rionexenergy.com`（Rionex）** **完全不同**，勿混淆。
- ⚠️ 另有 `houstontransformer.com`（Houston Transformer Company）、`Texas Transformers and Equipment, LLC` 等**无关同名类实体**，勿混。

---

## 六、附：DNS / SMTP 记录（存档）

| 项 | 值 |
|---|---|
| MX | `0 rionexenergy-com.mail.protection.outlook.com`（Microsoft 365） |
| SPF | `v=spf1 include:secureserver.net -all`（**硬失败**） |
| DMARC | `v=DMARC1; p=quarantine; adkim=r; aspf=r; rua=mailto:dmarc_rua@onsecureserver.net` |

**SMTP 探测结果（2026-09-28）**：

```
MX=rionexenergy-com.mail.protection.outlook.com
  550  info@rionexenergy.com      :: 5.4.1 Recipient address rejected: Access denied.
  550  sales@rionexenergy.com     :: 5.4.1 Recipient address rejected: Access denied.
  550  zzq9k2x7@rionexenergy.com  :: 5.4.1 Recipient address rejected: Access denied.  ← 🔴 随机对照亦 550
```

> 🔴 **随机对照地址亦 550** ⇒ 属 skill《渠道状态清单》**第 (h) 类：同域全 550 但对照未达 250 ⇒ 内部目录不披露**。
> ⚠️ **不可据此判断「地址不存在」** —— **仅表示该域不对外部披露目录**。
> （因已排除，DNS/SMTP 仅作存档，不影响结论。）

---

## 七、CSV 原始记录

```
43,B 分销商/贸易商,Rionex Energy,Rionex Energy,美国,,分销商,UL-listed padmount + substation 变压器,rionexenergy.com
```

> **建议**：
> ① CSV 第 43 行「细分属性」由 `分销商` 修正为 **`⛔中国工厂（江苏正来电气）北美独家分销（同业竞争，排除）`**；
> ② 「州省」列补 **`TX`**（Houston, TX）；
> ③ 备注建议补：**UL 档案 E526441 / E539752 / E545481 / E538000 均签发给 JIANGSU ZHENGLAI ELECTRIC CO. LTD（中国江苏海安）**。

---

## 八、方法论沉淀建议（供更新 skill）

**建议新增「⓪ 层排除」子判据 —— 「查 UL 档案持有人」：**

> 当一家公司自称 *"authorized distributor"* / *"factory-direct"* / *"partner factory"*，但**未自证制造能力**时：
> **应直接调取其公开的 UL Certificate of Compliance，核对「Issued to」字段的实体名与国别。**
> - 若签发对象为**中国工厂** → 判定为**「中国源 → 北美」通道 ⇒ 排除**
> - 若签发对象为**欧美工厂** → 可作**普通分销商**评估（保留）
>
> **本案即为该判据的首次实战应用，且一举定案。**
> （Rionex 自行公开全部 4 份证书 PDF，使其真实身份**自我暴露** —— 这是此类公司常见的**过度自证反成破绽**。）

---

*排查：砚舟 · 2026-09-28 · batch5_new_129plus · CSV 43 · ⓪层排除*
