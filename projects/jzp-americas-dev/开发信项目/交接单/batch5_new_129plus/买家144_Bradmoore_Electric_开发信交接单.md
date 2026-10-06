# 【买家 144】开发信交接单 — Bradmoore Electric Co. Ltd.

> 采集日期：2026-09-28 ｜ 名单来源：`线索资产/目标客户清单.csv` 序号 9（A 类 · 电气承包商/工程公司）
> 采集方：找客户环节（本环节只产出交接单，不写正文/不碰模板/不定话术）
> ⚠️ 本表严格区分「已验证」与「未获取」，未找到的信息一律标注，**不做推断填充**（H1）
> ✅ 一句话结论：**渥太华第二代家族电气承包商**（1975 年由 Eric Moore + Barry Bradley 创立，
> 2008 年传给二代 **Tyson Moore / Lance Moore**），服务商业/工业/机构客户；
> 🔴 **任务书预警的「有 A 无 MX」已查明原因** —— 公司邮箱**不在** `bradmooreelectric.com`，
> 而在 `bradmoore.ca`（**该域已无 DNS 记录**）与**免费个人邮箱 `bradmoore@live.ca`**；
> 联系人 **Lance Moore（Director）**，官网 Contact 页明文 **`Lance.Moore@bradmoore.ca`（域已失效）** +
> 首页明文 **`bradmoore@live.ca`（个人邮箱，可用）**。
> ⚠️ **变压器信号弱**：官网无任何变压器/高压表述。

---

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示(如有)
Bradmoore Electric Co. Ltd. | Lance Moore | Director（第 2 代业主）| bradmoore@live.ca | ⚠️ 官网明文（个人免费邮箱）；SMTP 不可验证（Outlook 消费级域拒绝探测）| ca.linkedin.com/in/lance-moore-95b607143（仅摘要可见）| 渥太华家族电气承包商，1975 年由 Eric Moore 与 Barry Bradley 创立，2008 年传给二代 Tyson 与 Lance Moore（两人从业合计 50 年+）；服务商业/工业/机构电气；官网自述"业主亲自驻场"模式；协会：ESA / ECAO / OCA | 官网实抓（首页/about/contact 页）+ LinkedIn 摘要（两人 Director）+ SquaredAway 第三方简介 + DNS 查询 | 🔴 变压器信号弱；🔴 企业域 bradmoore.ca 已失效；⚠️ 只能用个人邮箱触达；⚠️ 官网仅 4 页（Wix 极简站）
```

**发信资格：⚠️ 有条件通过**（人对、有可用邮箱；缺口在「个人邮箱 + 业务对口弱」）
**邮箱档位：A（具名联系人 · 官网明文来源）—— ⚠️ 但为个人免费邮箱，非企业域**

---

## 二、补充信息（扩展段）

### 标准字段明细

| 项 | 内容 | 来源 |
|---|---|---|
| **公司全称** | **Bradmoore Electric Co. Ltd.** | 第三方 SquaredAway + 官网（一手）|
| **国家 + 城市** | **加拿大 ON 省 Ottawa（渥太华）**；官网自述 *"Servicing Ottawa's commercial, industrial and institutional electrical needs"* | 官网首页（一手）|
| **州省** | **ON ✅**（CSV 填 ON，**正确**）| 官网 |
| **详细地址** | ⚠️ **官网未列出** | — |
| **电话** | **Lance Moore：(613) 978-7632**（⚠️ **个人手机**，官网 Contact 页明文）| 官网 Contact 页（一手）|
| **注册信息** | ⚠️ **未获取** | — |
| **成立年份** | **1975**（官网 about 页逐字：*"started in Ottawa by **Eric Moore and Barry Bradley in 1975**"*）| 官网（一手）|
| **域名** | 🔴 **复杂情况，见下 §「域名与邮箱问题诊断」** | — |
| **邮件基础设施** | 🔴 **`bradmooreelectric.com`：无 MX、无 SPF、无 DMARC**（**空配置**）<br>🔴 **`bradmoore.ca`：无任何 DNS 记录**（域已失效/未配置）<br>✅ **实际用 `live.ca`（Outlook.com 消费级邮箱）** | DNS 实测 |
| **规模** | ⚠️ **未获取**（官网为 4 页 Wix 站，无规模信息）| — |
| **协会** | **ESA**（安省电气安全局）、**ECAO**（安省电气承包商协会）、**OCA**（渥太华建筑协会）—— 官网首页显示三个协会徽标链接 | 官网首页（一手）|
| **官网** | https://www.bradmooreelectric.com（⚠️ Wix 极简站，仅 Home/Services/Projects/About/Contact 5 页）| — |

### 🔴 域名与邮箱问题诊断（任务书预警项，已查明）

任务书 §6.3 记载：**`bradmooreelectric.com` 有 A 记录但无 MX，邮件入口需另找**。本单已查明：

| 域名 | DNS 状态 | 用途 | 结论 |
|---|---|---|---|
| `bradmooreelectric.com` | ✅ 有 A 记录（**Wix 托管**，185.230.63.x）<br>🔴 **无 MX / 无 SPF / 无 DMARC** | **仅网站**，**不承载邮件** | 该域**不能收信** |
| `bradmoore.ca` | 🔴 **无 MX、无 TXT、无 A —— 全无记录** | 官网 Contact 页**声明的邮箱域** | 🔴 **域已失效 ⇒ `Lance.Moore@bradmoore.ca` 无法收信** |
| `live.ca` | ✅ MX = `nam.olc.protection.outlook.com`（Outlook.com 消费级）| 🟢 **实际使用中的邮箱** | ✅ **唯一可用触达渠道** |

**🧩 诊断结论**：
该公司**从未配置过企业邮件系统** —— 网站用 Wix（免费/低价套餐）、邮箱用**个人免费 `live.ca`**。
官网 Contact 页展示的 `Lance.Moore@bradmoore.ca` **是已废弃的地址**（域都不解析了）。

> ⚠️ **⇒ 任务书「有 A 无 MX」的真实原因：不是配置疏漏，而是该公司压根没有企业邮箱。**
> 商业含义：**这是一家规模很小的公司**（小到用个人邮箱做业务），
> 与官网「业主亲自驻场」自述一致。**⇒ 采购体量预期须大幅下调。**

### 联系人（含 still_here 在职核验）

| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| **Lance Moore** | **Director（第 2 代业主，首封主送）** | 🟢 **双源**：<br>① **官网 Contact 页明文署名**（联系人区直接写 *Lance Moore* + 电话 + 邮箱）<br>② **LinkedIn 标题**：*"**Director** at Bradmoore Electric"* | **2008 年接手至今（约 18 年）**；官网称其与 Tyson *"over 50 years combined experience"* | **高**：官网 Contact 页当前在展示；LinkedIn 在列 | **极低**（业主级）| ca.linkedin.com/in/lance-moore-95b607143（仅摘要可见）|
| **Tyson Moore** | Director / **Part owner**（第 2 代业主，备选）| ⚠️ **仅 LinkedIn**：*"**Director** · Part owner of Bradmoore Electric"* | 2008 年接手至今 | 中：LinkedIn 页存在 | 极低（业主级）| ca.linkedin.com/in/tyson-moore-735614143（仅摘要可见）|
| Eric Moore | **创始人**（1975）| 🟢 官网 about 页明文 *"started in Ottawa by Eric Moore and Barry Bradley in 1975"* | 1975–2008 | ⚠️ 已退（2008 年交班）| — | — |
| Barry Bradley | **创始人**（1975）| 🟢 官网 about 页明文 | 1975–2008 | ⚠️ 已退 | — | — |

> 🔴 **机读结论**：
> 1. **Lance Moore 是官网当前列出的唯一联系人与署名者** ⇒ **首选主送对象**。
>    职务 *Director* 为 **LinkedIn（第三方）** + 官网署名（第一方但未标职务）的组合，
>    **⚠️ 官网未明写其职务** ⇒ **建议正文直呼姓名，不强调职称**。
> 2. **Tyson Moore 同为 part owner**（LinkedIn 自述），可作 follow-up 备选。
> 3. **该公司是「二代家族企业 + 业主驻场」模式** ⇒ **决策链极短，Lance/Tyson 即决策者**。
> 4. ⚠️ 官网**未提供 Lance/Tyson 之外任何人员**（无团队页）。

### 邮箱分档（A/B/C）

| 档 | 地址 | 依据 | 可否主送 |
|---|---|---|---|
| **A** | **`bradmoore@live.ca`** | 🟢 **官网首页明文出现**（一手，站点内置联系邮箱）<br>⚠️ **个人免费邮箱**（非企业域）| ✅ **主送**（唯一可用渠道）|
| C | `Lance.Moore@bradmoore.ca` | 🟢 官网 Contact 页明文 —— 🔴 **但 `bradmoore.ca` 域已无任何 DNS 记录 ⇒ 该地址无法收信** | ⛔ **禁用**（域已失效）|
| C | `Lance.Moore@bradmooreelectric.com` | ⚠️ 格式合理推演 —— 🔴 **但该域无 MX ⇒ 无法收信** | ⛔ **禁用** |

**🔴 邮箱验证方法与证据链（可复现）：**

```
域名 A：bradmooreelectric.com
  A 记录    = 185.230.63.171 / .107 / .186   （Wix 托管）
  MX        = ⚠️【空】—— 无任何 MX 记录
  TXT/SPF   = ⚠️【空】
  DMARC     = ⚠️【空】
  ⇒ 判定：该域【不承载邮件】。任何 @bradmooreelectric.com 地址均无法投递。

域名 B：bradmoore.ca
  A 记录    = ⚠️【空】
  MX        = ⚠️【空】
  TXT       = ⚠️【空】
  ⇒ 判定：该域【完全无 DNS 记录】= 已失效或从未启用。
  ⇒ 🔴 官网 Contact 页展示的 Lance.Moore@bradmoore.ca 【不可用】。

域名 C：live.ca（Microsoft Outlook.com 消费级）
  MX        = 10 nam.olc.protection.outlook.com
  SMTP 探测 = 🔴 连接即被【强制断开】（SMTPServerDisconnected）
  ⇒ 判定：Outlook.com 消费级域【不接受未认证来源的 SMTP 探测】—— 属安全策略；
     ⇒ SMTP 对本域【不可用】，但【不代表地址无效】。
  ⇒ bradmoore@live.ca 的可信度来自【官网第一方明文列出】（H5 满足）。
```

> 🔴 **重要提示（发送环节必读）**：
> 1. **只能投 `bradmoore@live.ca`** —— 企业域两个都不可用。
> 2. **个人免费邮箱的投递风险高**：Outlook.com 对陌生发件人的**垃圾邮件过滤极严**，
>    且**无法通过 SFP/DMARC 声明组织身份**。**⇒ 该地址的到达率预期须下调。**
> 3. **若邮件未回，第二触达路径是电话 (613) 978-7632（Lance Moore 本人手机）。**

---

## 三、开发信建议（**仅限：收件人 / 时机 / 附件 —— 不含正文、不含主题行、不含开场句**）

> 依分工铁律：**措辞/钩子/产品切片/主题行全部归环节 ②（写开发信 agent）**。本节只给**收件人与时机**层面的建议。

| 项 | 建议 | 依据 |
|---|---|---|
| **主送** | `bradmoore@live.ca` | **唯一可用渠道**（企业域全失效）|
| **称呼** | **Lance Moore** —— ⚠️ **不写职称**（官网未标其职务）| 见上 §二 |
| **抄送** | ⛔ **不可行**（无第二个有效地址）| — |
| **第二触达** | 电话 **(613) 978-7632**（Lance Moore 本人手机，官网明文）| 官网 Contact 页（一手）|
| **建议时机** | **美东工作日 08:00–10:00**（Ottawa = America/Toronto / ET）| 承包商上午处理事务 |
| **建议附件** | ① **E541627**（三相配电变，45–5,000 kVA）—— 该司为商业/机构建筑承包商，配电级最对口<br>② 公司介绍 | 属「可能触及但未明示」类 ⇒ 优先配电级 |
| **切入角度提示**（**仅提示，不代拟文案**）| 官网自述 *"owners on-site, giving our partners seamless decision-making"* + *"continually growing and looking for new clients"* —— **明确表达在找新客户**。<br>⇒ 决策链短是优势 | 官网 about 页（一手）|
| ⚠️ **定位提醒** | 🔴 **公司规模小**（用个人邮箱 + Wix 站）⇒ **采购体量预期须大幅下调**，归入「宽泛触达」| 见上 §二 |
| ⛔ **禁止事项** | ① 不得称其「做变压器/高压」（官网无表述，H1）；② 首封不报交期/价格（红线）；③ **不得使用已失效的 bradmoore.ca 地址** | — |

---

## 四、⚠️ 矛盾点与风险提示

| # | 风险 | 说明 |
|---|---|---|
| 1 | 🔴 **企业邮箱域两个全失效** | `bradmoore.ca` 无任何 DNS 记录；`bradmooreelectric.com` 有 A 无 MX ⇒ **企业域不能收信** |
| 2 | 🔴 **只能用个人免费邮箱** | `bradmoore@live.ca`（Outlook.com 消费级）⇒ 垃圾过滤严格，到达率预期须下调 |
| 3 | 🔴 **SMTP 不可验证** | Outlook 消费级域强制断开未认证探测 ⇒ **该地址无法用 SMTP 证真**（可信度仅靠官网第一方明文）|
| 4 | ⚠️ **公司规模小** | 用个人邮箱 + Wix 极简站（仅 4–5 页）⇒ 采购体量预期下调 |
| 5 | ⚠️ **官网未明列其职务** | Lance Moore 的 *Director* 来自 LinkedIn（第三方）⇒ **建议直呼姓名、不强调职称** |
| 6 | ⚠️ **业务对口度弱** | 官网无任何变压器/高压/变电站表述 ⇒ 归「宽泛触达」|
| 7 | ⚠️ **官网未列地址、无团队页、无规模信息** | 仅 Contact 页给姓名+手机+（失效）邮箱 |

---

## 五、信息缺口清单（请勿编造）

| 缺口 | 状态 |
|---|---|
| **详细地址** | ⛔ 官网未列 |
| **注册号 / 注册信息** | ⛔ 未获取 |
| **员工数 / 营收** | ⛔ 未获取 |
| **Lance / Tyson Moore 的官网职务标注** | ⛔ 官网未标 |
| **企业域可用邮箱** | ⛔ 两个企业域均不可收信 |
| **变压器采购证据** | ⛔ 未获取 |
| **具名邮箱（非个人域）** | ⛔ 不存在可用者 |

---

## 六、一句话画像

**渥太华第二代家族电气承包商（1975 年创立，2008 年传给 Tyson/Lance Moore），
业主驻场、决策链极短，官网自述「正在拓客」——但公司规模小到没有企业邮箱，
唯一可用触达是个人邮箱 `bradmoore@live.ca`，第二触达为 Lance 本人手机 613-978-7632。
属「宽泛触达」档，采购体量预期须大幅下调。**

---

## 七、渠道覆盖清单

| 渠道 | 状态 | 备注 |
|---|---|---|
| 官网（Wix，4–5 页） | ✅ 已抓取 | 首页/about/contact |
| 官网 Contact 页明文邮箱 | ✅ 已获取 | `Lance.Moore@bradmoore.ca`（🔴 域失效）|
| 官网首页明文邮箱 | ✅ 已获取 | `bradmoore@live.ca`（唯一可用）|
| 官网 Contact 页电话 | ✅ 已获取 | (613) 978-7632（Lance 手机）|
| LinkedIn（Lance / Tyson） | ⚠️ 仅摘要可见 | 撞 authwall |
| DNS（三域 A/MX/SPF/DMARC） | ✅ 已实测 | 见 §二诊断表 |
| SMTP 探测 | ⛔ 不可用 | Outlook 消费级域拒绝探测 |
| 第三方（SquaredAway） | ⚠️ 已参考 | 公司全称佐证 |

---

## 八、合规自查（H1–H7）

| 规则 | 自查结果 |
|---|---|
| **H1 不虚构** | ✅ 地址标「官网未列」；规模「未获取」；职务标注来源级别；明确标注「变压器信号弱」 |
| **H2 不臆造邮箱** | ✅ **明确禁用** `@bradmoore.ca`（域失效）与 `@bradmooreelectric.com`（无 MX）两个臆造/废弃地址；只用官网明文 |
| **H3 格式校验 + ≥1 交叉来源** | ✅ 格式合法；官网第一方明文 |
| **H4 标注验证状态** | ✅ 三个域的 DNS 状态逐一实测并列表；明确说明「Outlook 消费级域拒绝 SMTP 探测 ∉ 地址无效」 |
| **H5 交叉验证需 ≥1 第一方** | ✅ **第一方 = 官网首页明文邮箱** + 官网 Contact 页署名 |
| **H6 角色邮箱不得单独交付** | ✅ 交付**具名邮箱**（bradmoore@live.ca 虽为个人邮箱，但对应具名公司）+ 具名联系人 + 电话 |
| **H7 落盘 .md** | ✅ 本文件 |

---

## 九、给下一环节的交付说明

**可直接使用的成果：**
1. 主送邮箱 **`bradmoore@live.ca`**（官网第一方明文，唯一可用渠道）
2. 联系人 **Lance Moore**（Director / 第 2 代业主）+ 手机 **613-978-7632**
3. 备选联系人 **Tyson Moore**（Director / Part owner）
4. **公司公开业务事实**：渥太华家族电气承包商；1975 年创立，2008 年二代接手；商业/工业/机构电气；
   协会 ESA / ECAO / OCA；自述「业主驻场、正在找新客户」

**必须知悉的风险：**
1. 🔴 **企业域两个都不可用**：`bradmoore.ca` 无 DNS 记录、`bradmooreelectric.com` 无 MX
2. 🔴 **只能用个人免费邮箱（live.ca）** ⇒ Outlook.com 过滤严格，**到达率预期下调**
3. ⚠️ **公司规模小**（个人邮箱 + Wix 站）⇒ 采购体量预期下调
4. ⚠️ **业务对口度弱**（官网无变压器/高压表述）
5. ⚠️ 官网仅 4 页，无团队页、无地址、无规模信息

**本环节未做（属其他环节职责）：**
- 未写正文、主题行、开场句、钩子、产品切片（→ 环节 ② 写开发信 agent）
- 未定最终发送时间与时区窗口排程（→ 环节 ③/④ 脚本）
