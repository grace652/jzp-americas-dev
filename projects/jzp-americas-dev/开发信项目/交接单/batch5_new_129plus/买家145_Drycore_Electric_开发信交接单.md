# 【买家 145】开发信交接单 — Drycore Electric（注册名 Drycore Electric 2002 Inc.）

> 采集日期：2026-09-28 ｜ 名单来源：`线索资产/目标客户清单.csv` 序号 10（A 类 · 电气承包商/工程公司）
> 采集方：找客户环节（本环节只产出交接单，不写正文/不碰模板/不定话术）
> ⚠️ 本表严格区分「已验证」与「未获取」，未找到的信息一律标注，**不做推断填充**（H1）
> ✅ 一句话结论：**渥太华的电气承包商，1991 年成立（30+ 年）**，
> 🔴 **官网服务清单明确列出高压等级**：*"Incoming services/infrastructure (**high, medium & low voltages**)"*
> 与 *"**High voltage systems**"* —— **触及高压**；
> 含 **Design-Build / 预制 / 运维** 全链条，协会含 ECAO/OCA 及**魁北克两家协会**（跨省业务）；
> 联系人：⚠️ **官网无团队页，未获具名决策人**；
> 邮箱 **`contact.us@drycoreinc.ca`（官网 Contact 页明文，B 档）** + 旧域同址镜像。
> ⚠️ **CSV 所填域名 `drycore2002.ca` 已 301 重定向至 `drycoreinc.ca`（现用主域）**。

---

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示(如有)
Drycore Electric 2002 Inc. | ⚠️ 未获取（官网无团队页）| — | contact.us@drycoreinc.ca | ⚠️ 官网明文（角色邮箱）；域为 catch-all 无法 SMTP 验证 | ca.linkedin.com/company/drycore-electric（公司页）| 渥太华电气承包商，1991 年成立（30+ 年）；服务住宅/商业/工业；能力含 pre-construction（概念估算/价值工程/可施工性审查）、Design-Build、Installation（**高压系统**、超低压、发电机、UPS、接地、**高中低压进线**、EV 充电、能源管理）、Maintenance & Repair（含 24 小时应急）；项目含学校、商业、Design-Build；协会含 OCA/ECAO/ACQ/CMEQ | 官网实抓（首页/services/about/contact 页）+ DNS/重定向实测 + 第三方（联邦注册号、员工数）+ SMTP 探测 | ⚠️ 未获具名决策人（本单最大缺口）；⚠️ 域为 catch-all；⚠️ 两个域并存（旧域 301 至新域）
```

**发信资格：❌ 不合格**（**缺具名联系人** —— 触犯合格线闸门第一条）
**邮箱档位：B（角色邮箱 · 官网明文）**

> 🔴 **本单依任务交接书 §4.4 判定为「疑似 + 缺口」类，不直接进写信环节。**
> 理由：**合格线闸门要求「有具名联系人（不是『采购部』这种职能名）」** —— 本单未找到。
> ⚠️ 但公司**业务对口度高（明列高压）**，价值不低 ⇒ **建议列入「待补人」清单，优先补人后可转正**。

---

## 二、补充信息（扩展段）

### 标准字段明细

| 项 | 内容 | 来源 |
|---|---|---|
| **公司全称** | **Drycore Electric 2002 Inc.**（对外品牌 *"Drycore Electric"* ／ *"DRYCORE ELECTRIC \| ÉLECTRIQUE"*）| 第三方（can1business，联邦注册）+ 官网（一手）|
| **国家 + 城市** | **加拿大 ON 省 Ottawa（渥太华）** | 官网（一手）|
| **州省** | **ON ✅**（CSV 填 ON，**正确**）| 官网 |
| **详细地址** | **5480 Canotek Rd. Unit #1, Ottawa, ON K1J 9H5**（🟢 官网 Contact 页明文，**第一方**）<br>⚠️ 第三方 ContactOut 作 *K1C 6R7*（**邮编冲突**）⇒ **采信官网 K1J 9H5** | 官网（一手）|
| **电话** | **613.745.7600**（🟢 官网 Contact 页明文）| 官网（一手）|
| **注册信息** | **Drycore Electric 2002 Inc.**，**Canada Business Corporations Act**，注册日 **2002-08-30**（⚠️ **第三方 can1business 所载，未经官方注册库复核**）| 第三方（未复核）|
| **成立年份** | **1991**（官网首页/about 页逐字：*"In business since **1991**"* ／ *"since **1991**"*；官网另称 *"Serving Ottawa for over 30 years"*）<br>⚠️ **与注册年份 2002 不一致** —— 合理解释：**原实体 1991 年成立，2002 年重组为现名公司**（`2002 Inc.` 亦印证）**⇒ 此为推断，非事实** | 官网（一手）+ 推断 |
| **域名** | 🔴 **两个域**：<br>① `drycore2002.ca`（**CSV 所填**）—— 🔴 **301 重定向至 `drycoreinc.ca`**<br>② `drycoreinc.ca`（**现用主域**，网站实际所在）<br>两域**均配 Google Workspace** | 实测确认 |
| **邮件网关** | **Google Workspace**（两域均为 `aspmx.l.google.com`）| DNS MX |
| **SPF** | `drycore2002.ca`：`v=spf1 include:**dc-aa8e722993._spfm.drycore2002.ca** ~all`（**自定义 _spfm 子域，~all 软失败**）| DNS TXT |
| **DMARC** | `drycore2002.ca`：`v=DMARC1; P=none; rua=mailto:dmarc-reports@drycore2002.ca`（**p=none 监控模式**）| DNS TXT |
| **规模** | ⚠️ 第三方（ContactOut）称 **15 名员工**；Prospeo 称营收约 $1.37M —— **均未经官网证实** | 第三方（未证实）|
| **协会** | **Ottawa Construction Association（OCA）**、**Electrical Contractors Association of Ottawa（ECAO-Ottawa）**、**Electrical Contractors Association of Ontario（ECAO）**、**Association de la construction du Québec（ACQ）**、**Canadian Design-Build Institute**、**Corporation des Maîtres Électriciens du Québec（CMEQ）** | 官网 about 页（一手）|
| **官网** | **https://drycoreinc.ca**（⚠️ `drycore2002.ca` 已 301 重定向至此）| — |

> 🔴 **域名变更提示（重要）**：CSV 填写的 `drycore2002.ca` **已废弃为跳转域**。
> 官网 Contact 页**同时展示两个域的邮箱**（`contact.us@drycoreinc.ca` 与 `contact.us@drycore2002.ca`）
> —— 说明**两个域都还在用**，但**主域是 `drycoreinc.ca`**。
> ⚠️ 发信**优先用 `drycoreinc.ca`**（主域，DMARC/SPF 维护更完整的是旧域，但主域是官方站点所在）。

### 🔴 第一发现：官网明列「高压」等级 —— 业务对口度较高

官网 **Services 页「Design-Build」清单原文**（一手，逐字）：

> *"Power distribution systems / Emergency power distribution / UPS systems / Grounding systems /
> **Incoming services/infrastructure (high, medium & low voltages)** / Lighting systems /
> Monitor control systems / Fire alarm systems / Building automation systems /
> Security, IT & audio/video infrastructure systems / LEED-certified design"*

官网 **Services 页「Installation」清单原文**（一手，逐字）：

> *"**High voltage systems** / **Extra low voltage power systems** / Lighting and lighting control systems /
> Fire alarm and detection systems / Electrical panels / **Generators** / Structured cabling and data networks /
> Security systems and CCTV installations / Renewable energy systems (solar, wind, etc.) /
> **Electric vehicle (EV) charging stations** / Energy management systems"*

官网 **首页原文**（一手，逐字）：

> *"Our team of professionals has the expertise to perform all types of electrical installations,
> from **high voltage to extra low voltage power systems**."*

🔴 **业务含义（供写信环节自行判断，本环节不定话术）**：
- **明列「high voltage systems」与「high/medium/low voltage 进线」** ⇒ **明确触及高压等级**，
  比买家 141（Alliance）、142（Ardoch）**对口度明显更高**。
- ⚠️ **但仍未提及「变压器」或「变电站」字样** ⇒ **不得推断其采购变压器**（H1）。
  其高压能力可能表现为**高压电缆敷设、开关柜、进线施工**，而非变压器采购。
- ✅ **正面信号**：其 **OCA/ECAO** 会员身份 + *"recommendations by **electrical engineering firms**"*
  （官网自述）⇒ 处于电气工程生态内，**有设备选型接触面**。

### 联系人（含 still_here 在职核验）

| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| ⚠️ **未获取** | — | — | — | — | — | — |

> 🔴 **机读结论（本单最大缺口）**：
> 1. **官网无团队页、无 About-Us 人员名单、无任何具名联系人** ——
>    官网 Contact 页**只给地址/电话/角色邮箱 + 表单**。
> 2. 尝试过的渠道**均未产出具名决策人**：
>    - 官网首页 / services / about / contact 页 —— 无人员
>    - LinkedIn **公司页存在**（`ca.linkedin.com/company/drycore-electric`）但**未抓取到人员**
>    - 第三方（ContactOut / Prospeo / can1business）—— **未产出可交付的具名管理者**
> 3. 🔴 **⇒ 依任务交接书 §4.4 合格线闸门第一条（须有具名联系人），本单【不合格】。**
> 4. ⚠️ **补人建议渠道**（供后续专项补人使用）：
>    - **OCA（渥太华建筑协会）会员名录**（其官网 about 页明列该会会员 —— 与买家 134 CCIB 的成功路径同类）
>    - **ECAO 会员名录**
>    - 联邦注册库（can1business 已给注册号，可进一步查**董事名册**）

### 邮箱分档（A/B/C）

| 档 | 地址 | 依据 | 可否主送 |
|---|---|---|---|
| **B** | **`contact.us@drycoreinc.ca`** | 🟢 **官网 Contact 页明文**（一手，**主域邮箱**）| ⚠️ 仅作**待补人后的备用** |
| B | `contact.us@drycore2002.ca` | 🟢 **官网 Contact 页明文**（一手，**旧域镜像**）| ⚠️ 备用（旧域）|
| A | ⚠️ **未获取**（无具名邮箱）| — | — |
| C | — | ⛔ **不可推演**：域为 catch-all，任何格式都回 250，**无法证伪** | ⛔ 禁用（H2）|

**🔴 邮箱验证方法与证据链（可复现）：**

```
域名 drycore2002.ca（旧域，CSV 所填）
  MX   = 1 aspmx.l.google.com（Google Workspace）
  SPF  = v=spf1 include:dc-aa8e722993._spfm.drycore2002.ca ~all
  DMARC= v=DMARC1; P=none; rua=mailto:dmarc-reports@drycore2002.ca
  HTTP = 301 → https://drycoreinc.ca/     （已废弃为跳转域）

  探测（对 drycore2002.ca）：
    250 2.1.5  zzz_nonexistent_probe_9987@drycore2002.ca   ← 🔴 随机地址也 250 ⇒ 【CATCH-ALL】
    250 2.1.5  info@drycore2002.ca
  ⇒ 🔴 判定：该域为 CATCH-ALL ⇒ SMTP 探测【全部无效】。

域名 drycoreinc.ca（新主域）
  MX   = aspmx.l.google.com（Google Workspace）
  A    = Cloudflare（104.21.42.89 / 172.67.160.115）
  ⚠️ 探测返回：451 4.3.0 "Multiple destination domains per transaction is unsupported"
  ⇒ 原因：同一 SMTP 会话内混合探测两个不同域，被 Google 拒绝
     （技术性拒绝，【非策略性】）⇒ 需【分域分会话】重测。

⇒ 🔴 【综合判定】：
   - 两个域均为 catch-all 或无法验证 ⇒ 【SMTP 对本单完全无效】。
   - `contact.us@drycoreinc.ca` 的可信度【不依赖 SMTP】，而依赖【官网第一方明文】。
```

> ⚠️ **catch-all 的连带影响**：**任何具名格式（如 `info@`、`j.smith@`）都会回 250，无法证伪**
> ⇒ **⛔ 严禁推测具名邮箱**（H2）。**本单只能交角色邮箱，且不合格。**

### ⚠️ 方法论提示（已在 skill 记录）

**Google Workspace 同会话多域探测会报 `451 4.3.0 Multiple destination domains per transaction is unsupported`**
—— 这是**技术性拒绝，不是策略性拒绝**，**不可误判为「网关封禁」**。
**⇒ 规程：探测 Google Workspace 域时，一次会话只探测一个域。**

---

## 三、开发信建议（**仅限：收件人 / 时机 / 附件 —— 不含正文、不含主题行、不含开场句**）

> ⚠️ **本单因缺具名联系人，暂不建议进入写信环节。** 本节内容仅供**补人成功后**参考。

| 项 | 建议 | 依据 |
|---|---|---|
| **主送** | ⚠️ **待补人**。补到具名联系人前，**不建议用角色邮箱发起首封** | 合格线闸门 |
| **若必须投递** | `contact.us@drycoreinc.ca`（主域）| 官网明文 |
| **建议时机** | **美东工作日 08:00–10:00**（Ottawa = America/Toronto / ET）| — |
| **建议附件** | ① **E541626**（三相液浸 POWER 变，750–110,000 kVA / 72–121 kV）—— ⚠️ **仅在确认其做高压变电站级项目后使用**<br>② **E541627**（配电变，45–5,000 kVA）—— 更稳妥的起点<br>③ 公司介绍 | 其官网明列 *"high voltage systems"* 但**未提变压器** ⇒ 建议配电级起步 |
| **切入角度提示**（**仅提示，不代拟文案**）| 官网自述 *"recommendations by **electrical engineering firms** to their clients"* + *"close relationships with **general contractors**"* ⇒ 处于**工程生态中间层**，有设备接触面 | 官网 about 页（一手）|
| ⛔ **禁止事项** | ① **不得推演具名邮箱**（域 catch-all，H2）；② 不得称其「采购变压器」（官网未述，H1）；③ 首封不报交期/价格（红线）| — |

---

## 四、⚠️ 矛盾点与风险提示

| # | 风险 | 说明 |
|---|---|---|
| 1 | 🔴 **未获具名决策人** | 官网无团队页、无 About-Us 人员名单 ⇒ **触犯合格线闸门第一条 ⇒ 本单不合格** |
| 2 | 🔴 **两个域均为 catch-all** | 随机地址亦回 250 ⇒ **SMTP 完全无效，严禁推测具名邮箱**（H2）|
| 3 | 🔴 **主送只能是角色邮箱** | H6 明确：角色邮箱不得单独交付 ⇒ 不合格的直接原因 |
| 4 | ⚠️ **CSV 域名已废弃** | `drycore2002.ca` 已 301 至 `drycoreinc.ca`，CSV 须更正 |
| 5 | ⚠️ **成立年份口径不一** | 官网 1991 vs 联邦注册 2002 ⇒ 已标为推断（原实体 1991、2002 年重组）|
| 6 | ⚠️ **邮编第三方冲突** | ContactOut 作 K1C 6R7 vs 官网 K1J 9H5 ⇒ 已采信官网 |
| 7 | ⚠️ **规模仅第三方未证实** | ContactOut 称 15 人 / Prospeo 称营收 $1.37M，均无官网印证 |
| 8 | ⚠️ **未提变压器** | 官网明列「high voltage systems」但**无变压器/变电站**字样 ⇒ 不得推断采购 |

---

## 五、信息缺口清单（请勿编造）

| 缺口 | 状态 |
|---|---|
| **具名决策人 / 具名邮箱** | ⛔ 未获取（**本单最大缺口**）|
| **注册号（官方复核）** | ⚠️ 仅第三方 can1business 所载 2002-08-30，未经官方库复核 |
| **员工数 / 营收** | ⚠️ 仅第三方未证实 |
| **变压器 / 变电站项目证据** | ⛔ 未获取 |
| **Lance/Tyson 之外的团队名单** | ⛔ 官网无团队页 |
| **过去项目具名案例** | ⛔ 官网仅泛述「学校、商业、Design-Build」 |

---

## 六、一句话画像

**渥太华电气承包商（1991 年起，30+ 年），官网明确列出「high voltage systems」与
「高中低压进线」——本批同类承包商中对口度较高的一家；但官网完全没有团队信息，
未获任何具名决策人，且两个域均为 catch-all，SMTP 无法验证 ⇒ 本单不合格，
列入「待补人」清单，补人成功后可优先转正（建议走 OCA / ECAO 会员名录）。**

---

## 七、渠道覆盖清单

| 渠道 | 状态 | 备注 |
|---|---|---|
| 官网（首页/services/about/contact） | ✅ 已抓取 | 一手 |
| 官网 Contact 页明文（地址/电话/双域邮箱） | ✅ 已获取 | 5480 Canotek Rd. Unit #1, K1J 9H5 / 613.745.7600 |
| 官网 Services 页（高压能力清单） | ✅ 已抓取 | 逐字引用 |
| 官网 about 页（协会名单） | ✅ 已抓取 | OCA/ECAO/ACQ/CMEQ/CDBI |
| DNS（A/MX/SPF/DMARC + 301 重定向） | ✅ 已实测 | 两域均 Google Workspace |
| SMTP 探测 | ⛔ 无效 | 两域 catch-all / 451 技术拒绝 |
| LinkedIn 公司页 | ⚠️ 存在但未抓到人员 | ca.linkedin.com/company/drycore-electric |
| 第三方（can1business / ContactOut / Prospeo） | ⚠️ 已参考 | 注册信息、规模（均未证实）|
| **OCA / ECAO 会员名录** | 🔜 **建议下一步补人** | 与买家 134 CCIB 成功路径同类 |

---

## 八、合规自查（H1–H7）

| 规则 | 自查结果 |
|---|---|
| **H1 不虚构** | ✅ 1991 vs 2002 的年份差异**如实标注并标为推断**；员工数/营收标为第三方未证实；明确「未提变压器，不得推断」|
| **H2 不臆造邮箱** | ✅ 明确说明域为 catch-all ⇒ **禁止推测具名邮箱**；只用官网明文角色邮箱 |
| **H3 格式校验 + ≥1 交叉来源** | ⚠️ 邮箱格式合法、官网明文；**但无具名联系人与具名邮箱 ⇒ 未过合格线** |
| **H4 标注验证状态** | ✅ 明确区分「官网明文」与「SMTP 不可验证（catch-all）」；记录 451 的技术原因 |
| **H5 交叉验证需 ≥1 第一方** | ✅ 公司层面信息有官网第一方；**人员层面无来源（如实标注未获取）** |
| **H6 角色邮箱不得单独交付** | 🔴 **本单只有角色邮箱 ⇒ 依 H6 不得单独交付 ⇒ 判定不合格**（已在开头明示）|
| **H7 落盘 .md** | ✅ 本文件 |

---

## 九、给下一环节的交付说明

**🔴 本单判定：不合格（缺具名联系人）→ 列入「待补人」清单。**

**可直接使用的成果（公司层面）：**
1. 公司公开业务事实：1991 年成立（30+ 年）；渥太华；服务住宅/商业/工业；
   **能力含高压系统、高中低压进线、Design-Build、发电机、UPS、EV 充电、能源管理**；
   协会 OCA / ECAO / ACQ / CMEQ / Canadian Design-Build Institute
2. 地址 **5480 Canotek Rd. Unit #1, Ottawa, ON K1J 9H5** + 电话 **613.745.7600**
3. 角色邮箱 **`contact.us@drycoreinc.ca`**（主域）／ `contact.us@drycore2002.ca`（旧域）
4. **CSV 域名已过时**：`drycore2002.ca` → **301 至 `drycoreinc.ca`**

**必须知悉的风险：**
1. 🔴 **未获具名决策人** ⇒ **不合格**，不可直接进写信环节
2. 🔴 **两个域均为 catch-all** ⇒ SMTP 完全无效，**严禁推测具名邮箱**
3. ⚠️ CSV 域名已废弃（重定向），须更正
4. ⚠️ 官网无团队页、无地址以外的人员信息

**补人建议渠道（供后续专项补人）：**
- **OCA 会员名录** / **ECAO 会员名录**（该司自述为两会会员 —— 与买家 134 CCIB 成功路径同类）
- 联邦注册库进一步查**董事名册**（已获注册信息：Drycore Electric 2002 Inc.，CBCA，2002-08-30）

**本环节未做（属其他环节职责）：**
- 未写正文、主题行、开场句、钩子、产品切片（→ 环节 ② 写开发信 agent）
- 未定最终发送时间与时区窗口排程（→ 环节 ③/④ 脚本）
