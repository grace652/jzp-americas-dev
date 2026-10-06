# 【买家 136】开发信交接单 — ABCO Supply & Service Ltd.

> 采集日期：2026-09-28 ｜ 名单来源：`线索资产/目标客户清单.csv` 序号 13（A 类 · 电气承包商/工程公司）
> 采集方：找客户环节（本环节只产出交接单，不写正文/不碰模板/不定话术）
> ⚠️ 本表严格区分「已验证」与「未获取」，未找到的信息一律标注，**不做推断填充**（H1）
> ✅ 一句话结论：**1972 年成立、温尼伯的多工种（电气/机械）承包商（51+ 年，自有 33,000 平方英尺厂房）**；
> 官网项目页明列 **Diageo 变电站升级**（*"Remove and reinstall (2) **3 MVA Transformers**"*，
> **Prime Contractor**，Gimli MB）与 **MB Hydro Bipole III Riel Station**（*"transformer drains"* 管线）；
> **联系人 Brian Cabral（General Manager）锁定，邮箱 `brian.cabral@abcosupply.com`
> 经 SMTP 控制组法验证命中（A 档）**。

---

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示(如有)
ABCO Supply & Service Ltd. | Brian Cabral | General Manager | brian.cabral@abcosupply.com | ✅ 已验证（A 档） | ⚠️ 个人页未直接取（LinkedIn 摘要可见）| 温尼伯多工种承包商，1972 年成立，51+ 年历史；自有 33,000 sq ft 总部+仓库+制造厂（含 5 吨行车）；业务含电气/仪表控制、工艺管道、机械装配、制冷、燃气、水暖；项目履历含 Diageo 变电站升级（搬迁 2×3MVA 变压器，Prime Contractor）与 MB Hydro Bipole III Riel Station | 官网实抓（首页/about-us/our-projects/Diageo 专项页）+ LinkedIn 招聘页摘要 + SMTP 控制组法 + DNS/SPF/DMARC | ⚠️ 官网无团队页、无实名邮箱；⚠️ 第三方库（openbiz）数据严重失真（地址/年份均与官网冲突）
```

**发信资格：✅ 通过**（九条闸门全过）
**邮箱档位：A（具名联系人 · 已验证 · 非 catch-all 域）**

---

## 二、补充信息（扩展段）

### 标准字段明细

| 项 | 内容 | 来源 |
|---|---|---|
| **公司全称** | **ABCO Supply & Service Ltd.**（官网用 *"ABCO Supply & Services"*）| 官网（一手）|
| **国家 + 城市** | **加拿大 MB 省 Winnipeg（温尼伯）** | 官网 Contact 页（一手）|
| **州省** | **MB ✅**（CSV 填 MB，**正确**）| 官网 |
| **详细地址** | **1346 Spruce Street, Winnipeg, MB R3E 2V7** | 官网 Contact 页（一手）|
| **电话** | **+1 (204) 633-8071** | 官网 Contact 页（一手）|
| **注册信息** | ⚠️ **未获取**（MB 省注册库未查通）| — |
| **成立年份** | **1972**（官网首页原句 *"Established in 1972 in Winnipeg, Manitoba"*；about-us 原句 *"dating back to 1972"*）| 官网（一手，两处一致✅）|
| **域名** | abcosupply.com（🔴 **非 catch-all，SMTP 探测有效**）| 探测确认 |
| **规模** | **自有 33,000 平方英尺**复合体（总部 + 仓库 + 制造厂）；制造厂有 **5 吨室内行车**<br>⚠️ 员工数未获取 | 官网 about-us（一手）|
| **营收** | ⚠️ 未获取 | — |
| **官网** | https://abcosupply.com | — |

> ⚠️ **第三方库数据失真警告**：`openbiz.ca` 显示 ABCO 地址为 *1244 Border St*、成立年份 *1985*、
> 员工 "Less 10" —— **与官网（1346 Spruce St / 1972 / 33,000 sq ft 厂房）逐项冲突**。
> **⇒ 判定 openbiz 数据不可用**，⛔ **不得引用**。**一律以官网为准**。

### 联系人（含 still_here 在职核验）

| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| **Brian Cabral** | **General Manager（总经理 · 首封主送）** | **LinkedIn 招聘页原句**（ABCO 官方发布的招聘帖署名区）：*"**Brian Cabral — General Manager at ABCO**"*<br>⚠️ RocketReach 另称其 *"Project Manager and Estimator"*（口径冲突）| ⚠️ 未知 | **高**：LinkedIn 招募帖署名为在任 GM（帖文由 ABCO 发布）| 低 | ⚠️ ca.linkedin.com/in/brian-cabral-1236b484（未直接抓取，仅摘要可见）|

> 🔴 **机读结论**：
> 1. **Brian Cabral 是本单可确认的管理联系人**，依据是 **ABCO 官网 LinkedIn 招聘帖的署名区**：
>    *"Brian Cabral — General Manager at ABCO"* —— 这是**公司自己发布的招聘信息**，
>    可视为**在任证明**（招聘是现任管理者的职责）。
> 2. ⚠️ **职称口径冲突**：LinkedIn 显示 *General Manager*，RocketReach 显示 *Project Manager and Estimator*。
>    → **采用 LinkedIn（信息较新，且出现在 ABCO 官方招聘帖语境）**；
>    ⛔ **不得在正文中强调其具体职称**（避免因口径差异出错），建议**直呼姓名**。
> 3. ⚠️ **官网无团队页、无实名邮箱、无管理层名单** —— 除 Brian Cabral 外**无其他决策人公开**。
> 4. ⚠️ **创始人/所有者姓名未获取** —— 官网仅称 *"privately owned"*，未具名。

### 邮箱分档（A/B/C）

| 档 | 地址 | 依据 | 可否主送 |
|---|---|---|---|
| **A** | **`brian.cabral@abcosupply.com`** | ①**SMTP 控制组法命中**（250，非 catch-all 已排除）<br>②**LinkedIn 招聘帖署名**确认 Brian Cabral = General Manager @ ABCO | ✅ **主送** |
| A（备选格式）| `bcabral@abcosupply.com` | 同样 SMTP 命中 250（**同人多格式**）| ⚠️ 备选，**不与主送同发** |
| B | `info@abcosupply.com` | SMTP 命中 250（已验证存在）；⚠️ 官网**未明文列出**（官网只有表单）| ⚠️ 第二轮备选 |
| C | — | 无 | — |

**🔴 邮箱验证方法与证据链（可复现）：**

```
域名 abcosupply.com
MX = abcosupply-com.mail.protection.outlook.com   （Exchange Online / M365）
SPF = v=spf1 include:spf.protection.outlook.com -all   （🔴 -all 硬失败，策略严格）
      另含 knowbe4-site-verification（安全意识培训平台）
DMARC = v=DMARC1; p=quarantine; rua=mailto:...     （⚠️ 中等严格，quarantine）

🔴 catch-all 排除测试（干净轮次）：
   随机地址  zzz_nonexistent_probe_9987@abcosupply.com  → 550  ✅
   ⇒ 判定【非 catch-all】，SMTP 探测有效

🔴 多格式命名规则探测（本域为 {first}.{last} 与 {f}{last} 并存）：
   ✅ brian.cabral@abcosupply.com  → 250  🔴 命中（{first}.{last}）
   ✅ bcabral@abcosupply.com       → 250  （{f}{last}，同人别名或并存）
   ❌ brian@abcosupply.com         → 550
   ❌ cabral@abcosupply.com        → 550（首测被 Spamhaus 干扰，不可信）

🔴 干净轮次复核（IP 黑名单解除后，三组一致）：
   控制组  info@abcosupply.com                 → ✅ 250 Recipient OK
   对照    zzz_nonexistent_probe_9987@         → ✅ 550（排除 catch-all）
   候选    brian.cabral@abcosupply.com         → ✅ 250 Recipient OK

⇒ 判定：**A 档成立**
   ① 技术验证 = SMTP 控制组法（非 catch-all + 命中 + 控制组正常）
   ② 交叉源  = LinkedIn（ABCO 官方招聘帖署名 "Brian Cabral — General Manager at ABCO"）
```

> ⚠️ **过程干扰（已排除）**：探测中途本机出口 IP `223.64.2.43` 再次触发
> **Spamhaus 拦截**（`550 5.7.1 ... blocked using Spamhaus`）。
> 按协议**控制组复核**：冷却后 `info@` 恢复 250，**且 `brian.cabral@` 在新轮次复现 250** → 结论有效。
> 🔴 **第三次印证：本机出口 IP 的 Spamhaus 问题是系统性障碍，发送环节必须先解决。**

### 我为什么找他

**这家公司的项目页，把「2 台 3 MVA 变压器」的搬迁工程写成了自己的 Prime Contractor 业绩。**

| # | 具体观察（均有官网原句出处） |
|---|---|
| 1 | 🔴 **Diageo 变电站升级项目（官网专项页原句）**：*"**Remove and reinstall (2) 3 MVA Transformers**"*<br>—— **明确给出变压器数量（2 台）与容量（3 MVA）**，是本批唯一给出具体 kVA 的客户 |
| 2 | **同项目页原句**：*"Install customer supplied 6,000 amp switchgear E-House. **Supply, Install, and design 6,000 and 3,000 amp Cable buss Systems**"*<br>—— 有 **Supply + Install + design** 三项职责 |
| 3 | 🔴 **同项目页明列 *"Prime Contractor"*** —— **不是分包，是总包**，对项目采购有主导权 |
| 4 | **MB Hydro Bipole III Riel Station 项目（官网原句）**：*"Synchronous Condenser pipe fabrication and Installation of lycol, lube oil, compressed air, hydrogen, deluge, **transformer drains**, CO2 & potable water piping systems."*<br>—— 🔴 **MB Hydro Bipole III 是曼尼托巴省最大输电工程**（±500kV HVDC） |
| 5 | **公司规模**：*"We own and operate a **33,000-square-foot complex**, housing our head office, warehouse, and fabrication facility"*；制造厂有 **5 吨室内行车** |
| 6 | **51+ 年经营（1972 起）**，官网原句 *"With over 51 years in the construction industry"* |
| 7 | **服务行业含 Utility**：*"ABCO operates across major economic sectors, including Commercial, Manufacturing, Industrial, **Utility**, Mining, and Institutional"* |
| 8 | **工会承包商**：官网客户证言区出现 *"Russ Shewchuk — **IBEW Local Union 2085**"* → 电气业务为 IBEW 工会承包 |
| 9 | **多工种一站式**：电气/仪表控制、工艺管道、机械装配（millwright）、制冷、燃气、水暖 —— 官网称 *"one-stop shop advantage"*、*"single-source management of multiple trades"* |
| 10 | **客户类型**：Diageo Canada（大型烈酒集团）、MB Hydro（省电力公司）、TransCanada Pipelines（管道）、Victoria General Hospital、加拿大政府（Centennial Flame 纪念碑） |

> 📌 **开场可用的合法事实**（措辞由写信环节定）：
> 「官网 Diageo 变电站升级项目里写明的 2 台 3 MVA 变压器搬迁（且是 Prime Contractor）」或
> 「MB Hydro Bipole III Riel Station 的 transformer drains 管线工程」
> —— **均为官网原句，只有这家成立**。

### 买家类型 / 需求品类

**买家类型：🔥 B — 多工种承包商（电气 + 机械，EPC / 施工型，纯 B 型）**
判定依据（六层过筛结果）：
- ⓪ 反身排除：**通过** —— 官网**无任何 "manufacturer / we manufacture / our factory" 字样**；
  有 fabrication facility，但按官网描述为**工艺管道/机械预制**（*"pre-fabricate many of the complex mechanical piping systems"*），
  **非变压器制造**；未发现代理任何品牌（尤其**未见 YAWEI**）
- ① 价值链：主营 = 电气 + 机械施工安装 → 价值链中间环节 ✅
- ② 类型：**B（多工种承包商）** —— 依据 *"leading multi-trade contracting and service company"*
- ③ 产品形态：**配电级美变 / 小容量电力变**（见下）
- ④ 地域：**MB 省（加拿大，权重高）** → **可谈高压 E541626** ⚠️ 但据实评估
- ⑤ 规模：自有 33,000 sq ft 厂房，全员数未知

**需求品类（带结论态 —— 加拿大客户，可谈高压）：**

```
- `三相美变 / padmount（UL E541627，45–5,000 kVA，可直供）`   ← 🔴 主谈：Diageo 项目为 3 MVA（=3000 kVA）级，正落此区间
- `三相液浸电力变（UL E541626，750–110,000 kVA，可直供）`     ← Diageo 3 MVA 亦落 E541626 下沿
- `杆上变 / 单相（UL E544629，仅 ECD Letter，非证书）`          ← 配电侧，备选
- `干变（加拿大可谈：built to CSA/IEEE，需人工确认）`           ← 备选
- `站用变 / 接地变（需人工确认具体规格）`                       ← 官网 substation 业务有联想空间
```

> 🔴 **本单的独特价值**：**Diageo 项目给了具体容量 3 MVA（3,000 kVA）**，
> 正落在我方 **E541627（45–5,000 kVA）区间内**，**是美国/加拿大配电级产品线的直接目标区间**。
> ⚠️ **但注意**：该项目原文是 *"**customer supplied** 6,000 amp switchgear"* 与 *"**Remove and reinstall** (2) 3 MVA Transformers"*
> —— **变压器是业主供货（Diageo 供），ABCO 负责拆卸重装**。
> → ⚠️ **不得据此断言「ABCO 采购变压器」**；但作为 **Prime Contractor**，其在新项目中**可能承担采购**。
>    **表述须谨慎**。

### 电压·频率·认证要求

| 项 | 内容 | 来源 |
|---|---|---|
| **频率** | **60 Hz**（加拿大）✅ 零改造适配 | 国别推定 |
| **电压** | ⚠️ **未获取具体电压等级** —— 官网项目页只给**电流**（6000 A / 3000 A Cable Bus）与**容量**（3 MVA），**未给 kV** | 官网原话 |
| **客户资质** | 服务 MB Hydro、Diageo、TransCanada Pipelines；**IBEW Local 2085** 工会承包 | 官网 |
| **认证（我方口径）** | 加拿大可写 `built to CSA/IEEE/IEC standards`；美变亮 `UL E541627`；电力变亮 `UL E541626` | 我方能力边界 |
| ⛔ **禁止写法** | `CSA Certified`／`cUL and CSA`／`SASO`／`SONCAP`；**不得写具体 kV**（3 MVA 可引用，因其为官网原文）| 红线 §二 |

> ✅ **罕见利好**：官网已给出 **3 MVA** 容量，属**客户自己披露的规格**，正文**可以引用这一事实**
> （因为它是项目描述的一部分，不是我方推断）。
> ⛔ 但 **不得补成具体 kV**（官网未写）。

### 采购信号

| # | 信号 | 强度 | 出处 |
|---|---|---|---|
| 1 | 🔴 **官网 Diageo 项目明列"2 台 3 MVA 变压器"搬迁，且为 Prime Contractor** | 🔥🔥🔥 | 官网（一手）|
| 2 | 🔴 **官网 MB Hydro Bipole III 项目**（省最大输电工程 ±500kV HVDC）| 🔥🔥🔥 | 官网（一手）|
| 3 | **官网项目页有 "Supply, Install, and design" 表述**（含供货职责）| 🔥🔥🔥 | 官网（一手）|
| 4 | **自有 33,000 sq ft 厂房 + 5 吨行车** → 有承接与预制能力 | 🔥🔥 | 官网（一手）|
| 5 | **51+ 年经营 + IBEW 工会承包** → 资质稳定 | 🔥🔥 | 官网（一手）|
| 6 | **服务行业含 Utility / Mining / Industrial** | 🔥🔥 | 官网（一手）|
| 7 | ⚠️ **Diageo 项目变压器为"customer supplied"** → 该单未体现其自采 | ⚠️ 双刃 | 官网原文 |
| 8 | ⚠️ 未发现近期**变压器采购招标**公开记录 | ⚠️ | 未查招标平台 |

> ⚠️ **信号强度：中强**。项目履历含变压器作业且为 Prime Contractor 是强信号；
> **但 Diageo 项目变压器系业主供货**，因此**不能直接推定其自采变压器**。
> → **本单的合理切入点是「配电级产品的供应商目录」，而非「你正在买变压器」。**

### 可利用的钩子（按强度排序）

| 序 | 钩子 | 强度 | 落点品类 | 是否可写 |
|---|---|---|---|---|
| 1 | **官网 Diageo 变电站升级：2 台 3 MVA 变压器搬迁，Prime Contractor** | 🔥🔥🔥 | 美变 / 小电力变 | ✅（可引用容量，不推 kV）|
| 2 | **官网 MB Hydro Bipole III Riel Station 项目** | 🔥🔥🔥 | — | ✅ |
| 3 | **官网 "Supply, Install, and design" 的自营表述** | 🔥🔥 | 美变 | ✅ |
| 4 | **1972 年创立、51+ 年、33,000 sq ft 自有厂房** | 🔥🔥 | — | ✅ |
| 5 | **IBEW Local 2085 工会承包** | 🔥 | — | ✅（来源为客户证言，可引用）|

### 开发信建议

> 📌 本段是**给写信环节的输入**，不是正文。**不含主题行、开场句、产品切片措辞**（分工铁律）。

- **收件人策略**：主送 **Brian Cabral（General Manager）** `brian.cabral@abcosupply.com`（A 档，已验证）
  - 🔴 **一家公司只发 1 人**（skill §3.0 红线）—— 官网无团队页，**无双送选项**
  - ⚠️ **同人多格式**：`bcabral@abcosupply.com` 亦命中，**但与主送同发等于重复投递** → ⛔ **不发**
  - 备选（第二轮）：`info@abcosupply.com`（B 档，已验证存在）
- **称呼**：⚠️ **建议直呼 "Brian"** —— 因其职称口径冲突（GM vs Project Manager），**避开职称更稳妥**
- **开场角度（供选择，非指定）**：可考虑从「官网 Diageo 变电站升级项目里的 2 台 3 MVA 变压器（作为 Prime Contractor）」或「MB Hydro Bipole III 项目」切入 —— **最终写法归写信环节**
- **附件建议**：不带供货记录名录（H7 红线）；可备 **UL E541627 区间说明（45–5,000 kVA）** —— **3 MVA 正落此区间**
- **发送时段**：客户在 **MB 省 = 中部时区（CT）**
  - 目标送达：**当地工作日 08:00–10:00**
  - 北京发送窗口（夏令时）：**21:00–23:00**
  - 冬令时：22:00–24:00
  - ⚠️ **周末不发**（按客户当地星期判断）
- **送达配置**：
  - 网关 = **Exchange Online / M365**
  - SPF = `v=spf1 include:spf.protection.outlook.com -all`（🔴 **`-all` 硬失败**）
  - DMARC = `p=quarantine`（⚠️ 中等严格；`rua` 指向的内部邮件地址未完整取得）
  - 🔴 **强烈提醒**：本机出口 IP **第三次**触发 Spamhaus（本单探测中）
    → **发送环节必须先解决 IP 信誉问题**
  - 建议**纯文本**（无图片签名需求）

### ⚠️ 矛盾点与风险提示

| # | 风险 | 详情 | 处置 |
|---|---|---|---|
| 1 | ⚠️ **Diageo 项目的变压器是「业主供货」** | 官网原句 *"**customer supplied** 6,000 amp switchgear"* + *"**Remove and reinstall** (2) 3 MVA Transformers"* | ⛔ **不得写成"ABCO 采购变压器"**；可用「作为 Prime Contractor 有采购话语权」的角度 |
| 2 | ⚠️ **Brian Cabral 职称口径冲突** | LinkedIn：General Manager；RocketReach：Project Manager and Estimator | **采用 LinkedIn 口径**；⚠️ **正文建议直呼姓名，避开职称** |
| 3 | ⚠️ **官网无实名邮箱、无团队页** | 官网只有表单与电话 | 邮箱经 SMTP 验证获得；⚠️ 人名来源为 LinkedIn 招聘帖 |
| 4 | 🔴 **第三方库 openbiz 数据严重失真** | 地址（1244 Border St vs 官网 1346 Spruce St）、年份（1985 vs 官网 1972）、员工数（<10 vs 有 33,000 sq ft 厂房）**逐项冲突** | ⛔ **openbiz 完全不可用，不得引用** |
| 5 | ⚠️ **员工数/规模未获取** | 官网只给厂房面积 | 列为缺口；⚠️ **不得引用 openbiz 的 "<10 人"** |
| 6 | ⚠️ **创始人/所有者姓名未获取** | 官网仅称 *"privately owned"* | 列为缺口 |
| 7 | ⚠️ **官网项目页未给电压（kV）** | 只给电流（A）与容量（MVA）| ⛔ **不得补 kV**；**3 MVA 可引用**（官网原文）|
| 8 | ⚠️ **MB 省注册号未获取** | 注册库未查通 | 列为缺口 |
| 9 | ⚠️ **DMARC 未完整取得** | 仅知 `p=quarantine` + `rua` 指向未完整显示 | 交发送环节补 |
| 10 | 🔴 **本机出口 IP 的 Spamhaus 问题（第三次）** | 本单探测中再次触发 | **发送环节必须优先解决**（直接决定投递成败）|

### 信息缺口清单（请勿编造）

> 🔴 **以下字段正文一个字都不能出现**（红线：比"不编造"更严格，连模糊表述都不行）。

| 缺失项 | 说明 |
|---|---|
| **具体电压等级（kV）** | 未获取。**不得假设**（3 MVA 可引用，因是官网原文）|
| **员工人数** | 未获取。⛔ **不得引用 openbiz 的"<10 人"** |
| **营收** | 未获取 |
| **MB 省注册号 / 注册日期** | 未获取 |
| **创始人 / 所有者姓名** | 未获取。**不得编造** |
| **Brian Cabral 任职起始年月** | 未获取。**不得推断** |
| **其他管理层名单** | 未获取（官网无团队页）|
| **变压器采购方式（自采 vs 业主供货）** | 未获取。⚠️ **Diageo 单为业主供货，不得反向推断** |
| **是否已有中国供应商** | 未查（未启用海关数据源）|
| **DMARC 完整记录** | 未完整取得 |
| **Diageo 项目的年份** | 未获取 |
| **任何未在官网列出的客户名** | 未获取。**不得编造**（Diageo / MB Hydro / TransCanada / VGH 均为官网原话，可引用）|

### 一句话画像

**1972 年成立的温尼伯多工种（电气+机械）承包商**（51+ 年、自有 33,000 sq ft 厂房、IBEW 2085 工会承包）——
官网项目页明列 **Diageo 变电站升级（2 台 3 MVA 变压器搬迁，Prime Contractor）** 与
**MB Hydro Bipole III Riel Station**（省最大 ±500kV HVDC 工程）的 transformer drains 管线；
**联系人 Brian Cabral（General Manager）锁定，邮箱 `brian.cabral@abcosupply.com` 经 SMTP 控制组法命中** ——
**人明确、信号中强、邮箱达（A 档）**，⚠️ 需注意 Diageo 项目变压器系业主供货，**不可反向推断其自采**。

### 渠道覆盖清单（L-1、L0–L7）

| 层 | 结果 | 一句话 |
|---|---|---|
| **L-1 锁人** | ⚠️ | **LinkedIn 招聘帖署名**锁定 General Manager Brian Cabral；⚠️ 官网无团队页 |
| **L0 官网全量** | ✅ | 首页 / about-us / our-projects / Diageo 专项页 / MB Hydro 专项页实抓；**官网无实名邮箱**（仅表单 + 电话）|
| **L1 政府一手** | ❌ | **MB 省注册库未查通**；⚠️ BC registry 无记录（正常，属 MB 管辖）|
| **L2 命名 + DNS** | ✅ | MX/SPF/DMARC 已取；🔴 **非 catch-all 判定**（随机 550）；**多格式探测命中**（`brian.cabral@` 与 `bcabral@` 均 250）；控制组法复核通过 |
| **L3 B2B 库** | ⚠️ | D&B / RocketReach / Placedigger / openbiz 均命中，**但 openbiz 数据严重失真**；RocketReach 职称口径冲突 |
| **L4 社媒协会** | ⚠️ | LinkedIn 个人页摘要命中；⚠️ **无公司页命中**；官网提及 IBEW 2085 |
| **L5 黄页同址** | ⚠️ | ⚠️ 第三方地址与官网冲突（已判定官方为准）|
| **L6 电话表单** | ✅ | **电话 +1 (204) 633-8071 已取**（官网）；官网表单可作兜底 |
| **L7 付费** | ❌ | 未启用 |

---

## 三、交付方自检（写单者留痕）

- [x] **第 0 步判定已做**：类型归属（B 多工种承包商）+ 判定依据 + 可对应产品形态
- [x] **第 ⓪ 层反身排除已做**：官网无 "manufacturer" 字样；fabrication facility 为管道/机械预制（非变压器）；未代理品牌（无 YAWEI）
- [x] **背调 13 步「必做 6 步」已走**：公司名 ✅ / 版权主体 ✅ / 简介历史 ✅ / 注册库 ❌（MB 未查通，已标缺口）/ 无街景（地址已取）/ LinkedIn 锁人 ✅
- [x] **排重已做**：与 `_dedup_keywords.txt`（164 词）+ `_bounce_domains.txt` + `00_buyer_master_dedup.md` 比对，**无命中**
- [x] **按公司归并**：主送 1 人，同人别名格式已明确标为「不与主送同发」
- [x] `.md` 已实际写入磁盘
- [x] 9 核心字段 + 12 扩展段齐
- [x] 「我为什么找他」为**具体观察**（10 条，均有官网原句）
- [x] 「信息缺口清单」明确列出不能写的字段（12 项）
- [x] 「需求品类」**带结论态**（含 3 MVA 落点分析）
- [x] 联系人四栏（still_here）已核
- [x] 邮箱已分 A/B/C 档，且**验证方法可复现**（含 Spamhaus 干扰排除说明）
- [x] 过完 §三 九条闸门
- [x] 未写任何邮件正文 / 主题行 / 开场句措辞（分工铁律）
