# 【买家 192】开发信交接单 — Penco Electrical Contractors, Inc.（GA）

> 采集日期：2026-09-29 / 来源：batch6 名单（CSV 序 19）/ 一句话结论：**⓪ 层通过（商业/工业电气承包商，非制造商）**；官网页给出**完整团队含 Purchasing Agent**，但**未取得任何具名直邮**（域走 Proofpoint，SMTP 控制地址即被拒）；**降级为 B 档：电话点名转交 David Wallace（Purchasing Agent）**。

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示(如有)
Penco Electrical Contractors, Inc.（GA Morrow，覆盖东南 6 州） | David Wallace | Purchasing Agent（采购员） | 未找到（B档：770.960.7223 点名转交） | 未找到 | linkedin.com/company/penco-electrical-contractors | 1983 年创立于 Atlanta 的家族电气承包商，Division 16&17 全包（商业/机构/工业/高层/医疗），GDOT+Atlanta FBE/SBE 认证，覆盖 GA/AL/FL/NC/SC/TN | 官网页（团队/联系/About）+ 州执照 + B2B 库（仅旁证）| 🔴 无具名直邮；⚠️ 商业承包商→干变需求不匹配风险
```

## 二、补充信息（扩展段）

### ⓪ 层反身排除（🔴 已完成，结论：不排除）
- **判定**：✅ **电气承包商（服务/安装方）**，**非制造商/竞品代理/中国货源通道**。
- **证据原句（官网一手）**：
  - 首页："Your Trusted **Atlanta Electrical Contractor**… Delivering… **electrical solutions** for commercial, institutional, and industrial clients"
  - 首页："**Electrical Construction & Project Services** — Turnkey electrical services for new construction, renovations, and tenant improvements"
  - About："We handle every phase of **Division 16 & 17 electrical work**—commercial, industrial, institutional."
- **判据对照**：全文**无** `we manufacture` / `our factory`；动作词为 `install / service / maintain / construct`（安全信号）。**保留**。
- **NAICS**：238210（电气承包，推断）→ 承包商，非 335311/335313。

### 标准字段明细
- 国家+城市：美国 Georgia，Morrow（Atlanta 都会区）
- 详细地址：1087 Citizens Parkway, Morrow, GA 30260
- 电话：**770.960.7223**（官网一手）；Fax 770.960.7232
- LinkedIn：公司 linkedin.com/company/penco-electrical-contractors
- 网站：**www.pencoelectric.com**（站点用 www 前缀；域 pencoelectric.com）
- 成立日：**1983**（官网自述，"42 years"/"since 1983"）
- 规模：小微（ContactOut 记 ~10 员工口径；官网 500+ 商业项目）
- 营收：未获取
- NAICS：238210（推断）
- 资质：**Georgia DOT & City of Atlanta 认证 FBE & SBE Contractor**；GA/AL/FL/NC/SC/TN 六州持牌

### 联系人（含 still_here 在职核验）
| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| **David Wallace（主送点名）** | **采购** | **Purchasing Agent**（官网页） | 长（Penco LinkedIn 有"Work Anniversary David Wallace"帖） | 中：官网页在列 + LinkedIn 周年帖 | 低–中 | linkedin.com/in/david-wallace-795481198 |
| Kristen Williams（备选） | 最高层 | CEO（第二代 owner） | 多年 | 高：LinkedIn 个人页活跃 | 低 | linkedin.com/in/kristenatpenco |
| Bill Bledsoe | 最高层 | President（创始人 William T. Bledsoe 家族） | 多年 | 中 | 低 | — |
| Jerry Kirkman | 运营 | COO | — | — | — | — |
| Paul Kitchens | 报价 | Estimator | — | — | — | — |
| Glenn Claxton | 仓储 | Warehouse Manager | — | — | — | — |

> ⚠️ **团队来源**：官网页 `pencoelectric.com/about/`（**一手**，16 人全名单，含职务）。

### 邮箱分档（A/B/C）
- **A档（具名）**：**无**（官网页零邮箱；仅表单）
- **B档（电话，主送）**：**770.960.7223** → 点名转交 **David Wallace（Purchasing Agent）**
- **C档（推断邮箱，🔴 不可主送）**：`dwallace@pencoelectric.com` —— 仅由 B2B 库口径推演（RocketReach/Prospeo/PeopleSmart 一致称格式为 **`{first initial}{last}@pencoelectric.com`**，例 `jdoe@`），**未经任何一手源印证，格式校验为「待验证」**。
- **H6 声明**：⚠️ **仅取得角色入口（电话/表单），未取得决策人直邮。** 升级三步执行情况：
  - ① 挖职能邮箱：官网页 Contact/About **无任何邮箱**（仅表单）→ 未获
  - ② 从回信反推命名规则：无回信样本 → 停
  - ③ 免费推演：**不做**（无一手源，推演地址不可主送；见 H2/H4）
  - ⇒ **如实记录：未取得具名直邮，列为风险。**

### 我为什么找他
- Penco 是 **1983 年起家的家族商业电气承包商**，官网页**主动公开了完整团队名单**，其中 **David Wallace 的职务是 Purchasing Agent** —— 在一家约十人规模的公司里，**Purchasing Agent 就是采购决策/执行人**，比找 CEO 更对口。
- 该公司做 **Division 16&17 全包（含 Service & Maintenance / 改造 retrofit）** —— **改造/运维会带出变压器替换需求**，是"从改造项目切入"的对话对象。

### 买家类型 / 需求品类
- 买家类型：🔥 **A 承包商（商业/机构/工业电气承包，含改造与运维）**
- 需求品类（带结论态，**美国客户不谈干变**）：
  - `三相美变（UL E541627，可直供）` — 其商业项目配电侧
  - `单相柱上变（认证在办，条件切入）` — 条件型
  - 🔴 **重点风险**：商业/机构建筑（办公、医疗、高层）的变压器**多为室内干式变**，而我方 **`干变（美国不匹配：无 UL）`** ⇒ **不可推**。本单**须先电话确认其变压器需求是"液浸美变"还是"干变"**，否则钩子会挂空。
  - ⛔ `干变（美国不匹配：无 UL）` — **不推**

### 电压·频率·认证要求
- 频率：60 Hz（美国）→ 零改造适配
- 电压：商业配电（480V/277V 二次侧 + 中压进线），具体未获取
- 认证：美国要 **UL**（我方仅液浸类 E541626/E541627）；**干式变无 UL → 不匹配**
- 网关：MX = `mx1/mx2-us1.ppe-hosted.com`（**Proofpoint**）；SPF 含 `~all` 软失败

### 采购信号
- 官网明确 "**Service & Maintenance**… repairs, **retrofits**, routine maintenance" → 改造/替换需求持续
- 承接 **500+ 商业项目**（自述）→ 项目量稳定
- 家族企业二代接班（Kristen Williams 任 CEO）→ 决策链短
- 官网"Generator Sales（Kohler）" → 已有设备销售/采购习惯（**非变压器，但证明其会做设备采购**）

### 可利用的钩子（按强度排序）
1. **改造/运维项目里的配电变替换** —— 与其 Service & Maintenance 线直接相关（**但须先确认是液浸而非干变**）
2. 42 年家族企业 + 500+ 商业项目 → 长期合作叙事
3. 六州持牌 → 区域交付能力

### 开发信建议
- 收件人：🔴 **先电话 770.960.7223，点名转交 David Wallace（Purchasing Agent）**，问出他的直邮后再发信
- 抬头/称呼：待拿到直邮后具名；若走电话，先请前台转 Purchasing
- 收件人策略：**B 档点名转交**（H6 已声明未取得具名直邮）；**不要**把推演地址 `dwallace@pencoelectric.com` 当主送（H2/H4）
- 发送时段：美国 Eastern Time（GA）周二–周四上午 = 北京时间约 21–23 点
- 送达配置：**Proofpoint** 网关 + SPF `~all`；建议纯文本、单发；发件域三件套须齐
- 附件：不带名录/供货记录 PDF
- ⚠️ **电话脚本要点（只问不推销）**：① 你们项目里用的是**液浸美变还是干式变**？② 变压器采购归谁？③ 能否给 Purchasing 的邮箱？

### ⚠️ 矛盾点与风险提示
- 🔴 **无具名直邮**：官网页仅表单 + 电话；SMTP 探测**整体作废**（见下）→ 本单**只能 B 档（电话点名）**，**不可直接发信**。
- 🔴 **SMTP 不可用（已实测）**：`pencoelectric.com` MX = Proofpoint（ppe-hosted）；控制地址 `info@pencoelectric.com` 返回 **550** ⇒ **本轮探测整体作废**，**绝不能据此判定任何候选邮箱「不存在」**（§十六/§二十七）。未反复重试。
- ⚠️ **干变不匹配风险（最高业务风险）**：商业/机构建筑多要**干式变**，我方**无 UL** ⇒ **推干变会自曝短板**。**必须先电话确认品类**。
- ⚠️ **同名公司干扰**：搜索出现 **"Penco Electric & Generators"（IL，`info@pencoelectricinc.com`，847 区号）** —— **完全不同的公司**，勿混用其邮箱。
- ⚠️ **David Wallace 职务冲突**：官网页（一手）记 **Purchasing Agent**；LinkedIn 却记 **Service Electrician** ⇒ 以官网为准，但**入职/在岗状态需电话核**（`still_here` 未完全闭环）。

### 信息缺口清单（请勿编造）
- **具名直邮**：未找到（勿用 `dwallace@pencoelectric.com` 当主送）
- **David Wallace 的准确在岗职务**（Purchasing Agent vs Service Electrician）：**未证实** → 电话核
- **其项目变压器是液浸还是干式**：**未获取**（🔴 决定本单是否值得发）
- 公司**营收 / 常用变压器容量与品牌 / 现有供应商**：未获取
- **采购决策是否就在 David Wallace**：未证实

### 一句话画像
Atlanta 42 年家族商业电气承包商——官网页把 **Purchasing Agent David Wallace** 明明白白列出来，但**零邮箱**；先打电话确认"你们要的是液浸美变还是干变"，再决定要不要发。

### 渠道覆盖清单（L-1、L0–L7）
| 层 | 结果 | 一句话 |
|---|---|---|
| L-1 锁人 | ✅ | 官网页 16 人全名单，含 Purchasing Agent |
| L0 官网 | ⚠️ | 拿到电话/地址/团队，但**邮箱为零**（仅表单）|
| L1 政府一手 | ⚠️ | FMCSA DOT 3074889 存在（officer 需登录）；GA 执照 |
| L2 命名+DNS | ⚠️ | 域=Proofpoint，SMTP 控制地址 550 → 探测作废 |
| L3 B2B库 | ⚠️ | 仅推演格式（旁证，不作印证）|
| L4 社媒协会 | ✅ | LinkedIn 公司页 + CEO 个人页 |
| L5 黄页同址 | ✅ | 1087 Citizens Pkwy 多源交叉 |
| L6 电话表单 | ✅ | 770.960.7223（**本单主路径**，未拨打）|
| L7 付费 | ❌ | 未启用 |
