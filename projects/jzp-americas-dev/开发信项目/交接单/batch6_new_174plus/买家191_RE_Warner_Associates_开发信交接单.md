# 【买家 191】开发信交接单 — R.E. Warner & Associates（OH，现属 ISG）

> 采集日期：2026-09-29 / 来源：batch6 名单（CSV 序 18）/ 一句话结论：**⓪ 层通过（设计工程公司，非制造商）**；但 🔴 **公司已于 2026-06 并入 ISG Inc，邮箱域应为 `isginc.com` 而非官网 `rewarner.com`**；锁定 **Frank H. Johnson Jr., PE（VP, Energy）**，邮箱一手源 `Frank.Johnson@ISGInc.com`。

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示(如有)
R.E. Warner & Associates（现 ISG Inc.，OH Cleveland） | Frank H. Johnson Jr., PE | Vice President, Energy（ISG） | Frank.Johnson@ISGInc.com | 已验证（ISG 官网一手源） | linkedin.com/in/frank-h-johnson-jr-pe-a88bb015 | 1951 年创立的 Cleveland 多专业工程/建筑/测绘公司，电力/公用工程（变电站+输配电）设计；2026-06 并入 ISG Inc（75 年 legacy），成为其 Energy BU 主力 | ISG 官网 Energy BU 页 + ISG people 页 + R.E. Warner 官网 + ISG 收购新闻 | 🔴 邮箱域(isginc.com) ≠ 官网域(rewarner.com)；⚠️ 设计工程公司，采购权存疑
```

## 二、补充信息（扩展段）

### ⓪ 层反身排除（🔴 已完成，结论：不排除）
- **判定**：✅ **咨询设计工程公司**（engineering/architecture/surveying），**非制造商/竞品代理/中国货源通道**。
- **证据原句（官网一手）**：
  - 首页："R.E. Warner is a trusted **consulting engineering and design partner**… Our portfolio includes **substation, distribution, and transmission engineering** for electric utilities"
  - 首页："we offer **multi-discipline engineering services**… **Electrical engineering for utilities, power, lighting, and communications**"
  - About："Since our founding in **1951**, R.E. Warner has been a trusted **consulting engineering and design partner**"
- **判据对照**：全文**无** `we manufacture` / `our factory`；动作词为 `engineer / design / consult / survey`（设计方，非生产方）。**保留**。
- ⚠️ 注意：官网有一节 "**Manufacturing & Industrial**" —— 读全文后确认是**"为制造业客户做厂建设计"**（*"end-to-end design solutions for advanced manufacturing environments"*），**不是自己制造设备**（符合 §二十三）。

### 标准字段明细
- 国家+城市：美国 Ohio，Cleveland 地区（North Olmsted）
- 详细地址：ISG Cleveland = Great Northern Corp. Center, 25000 Country Club Boulevard, Suite 340, North Olmsted, OH 44070
- 电话：**440.835.9400**（ISG Cleveland 总机，一手）
- LinkedIn：个人 linkedin.com/in/frank-h-johnson-jr-pe-a88bb015（Frank）；公司 rewarner.com 与 isginc.com
- 网站：**rewarner.com**（现为 ISG 子品牌页；NS 为 Cloudflare）→ 主体 isginc.com
- 成立日：**1951**（官网自述，2026 = 75 周年）
- 规模：ISG 为大型多专业 A&E 公司（原 R.E. Warner 约百人级，第三方口径）
- 营收：未获取
- NAICS：541330（工程服务，推断）
- 归属：**2026-06-01 ISG Inc 收购 R.E. Warner**（ISG 官网新闻稿 + 新闻转载）

### 联系人（含 still_here 在职核验）
| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| **Frank H. Johnson Jr., PE（主送）** | **电力/公用工程负责人** | Vice President, Energy（ISG）；R.E. Warner 时期任 Director of PM → VP | 多年（2025-05 已列 R.E. Warner 领导层） | 高：2026-06 在 LinkedIn 亲自发帖谈 R.E. Warner 并入 ISG | 低 | isginc.com/people/frank-johnson；linkedin.com/in/frank-h-johnson-jr-pe-a88bb015 |
| Ted Beltavski, PE（备选） | 原最高层（现转型） | Executive Advisor / Employee Owner（ISG）；原 R.E. Warner **President & CEO** | 20+ 年 | 高：ISG people 页在列 | 低（但角色已转顾问） | isginc.com/people/ted-beltavski；linkedin.com/in/ted-beltavski-5b708712 |
| Michael Sousaris | 项目执行 | Project Executive（Energy BU） | — | — | — | isginc.com Energy BU 页 |
| Steve Burton, PMP | 项目管理 | Senior Project Manager（Energy BU） | — | — | — | isginc.com Energy BU 页 |

### 邮箱分档（A/B/C）
- **A档（具名，主送）**：`Frank.Johnson@ISGInc.com` —— **ISG 官网 Energy Business Unit 页一手明文**（格式 `{First}.{Last}@ISGInc.com`），**已验证**。
- **A档（备选）**：`Ted.Beltavski@ISGInc.com` —— ISG people 页一手明文。
- **B档（角色）**：`contactus@rewarner.com`（R.E. Warner Contact 页一手）；ISG 通用联系为表单。
- 命名规则：**`{First}.{Last}@ISGInc.com`**（首字母大写，ISG 官网多人一致）。
- H6 声明：不适用（已取得具名邮箱）。
- ⚠️ 未能跑 SMTP 复核：`isginc.com` MX = M365（`isginc-com.mail.protection.outlook.com`），**未测**（避免与其它 M365 域同批探测触发源 IP 拉黑）；A 档依据为**官网一手明文**，不依赖 SMTP。

### 我为什么找他
- Frank Johnson 是 **R.E. Warner 自己的领导层**（2025-05 公司领导层更新公告点名，任 Director of PM → VP），并入 ISG 后**继续主管 Energy 业务单元（VP, Energy）** —— 即**电力/变电站业务的现任负责人**，比已转"顾问"的原 CEO Ted Beltavski 更贴当前业务。
- 该公司**专做"electric utilities 的变电站 + 输配电工程"** —— 这类设计院是**变压器规格的制定者（spec engineer）**，是"提前进入项目规格书"的对话对象。

### 买家类型 / 需求品类
- 买家类型：🔥 **A 工程公司（电力/公用工程设计与变电站工程；spec 制定方）**
- 需求品类（带结论态，**美国客户不谈干变**）：
  - `三相美变（UL E541627，可直供）` — 配电侧变电站设计关联
  - `主变/变电站变（UL E541626，可直供，72–121 kV）` — 输电/变电站设计关联
  - `500kV 级主变（产能可覆盖，UL 区间外，需人工确认）` — 其项目涉及电网现代化，属机会型
  - ⛔ `干变（美国不匹配：无 UL）` — **不推**
- ⚠️ **定位提醒**：作为**设计方**，他们**不直接采购**变压器，但**决定规格/品牌入围**。钩子应落在"**供你们在规格书里写进/推荐我方产品**"，而非"卖给你们"。

### 电压·频率·认证要求
- 频率：60 Hz（美国）→ 零改造适配
- 电压：变电站 + 输配电（utility 级）；含 MV/HV
- 认证：美国要 **UL**（我方 E541626 / E541627）；表述用 `UL certified, tested to IEEE C57.12 and ANSI standards`，**不写 CSA/SASO/SONCAP**
- 网关：MX = `isginc-com.mail.protection.outlook.com`（M365）；SPF 含 `-all` **硬失败** → 发件域自查

### 采购信号
- **2026-06 并入 ISG** → 整合期，供应商/规格体系可能重审
- ISG **Energy BU 在招 "Senior Physical Substation Engineer"**（高电压输配电设计）→ 电力业务扩张
- R.E. Warner 承接 **"Transmission and Distribution Substation Improvements"**、**"Electrical Substation Design Improvements"**（官网 portfolio）→ 持续变电站设计项目
- 连续 5 年 Northeast Ohio Top Workplace + 2026 NorthCoast 99 → 业务稳定

### 可利用的钩子（按强度排序）
1. **并入 ISG 后的能源业务扩张** —— 新东家 + 在招变电站工程师，正是规格体系重审窗口
2. **R.E. Warner 75 年 legacy + 变电站设计专长** —— 开场可点名其"Transmission & Distribution Substation Improvements"项目
3. 我方 **UL E541626/E541627 覆盖配电变到 121kV 电力变** → 可对接其变电站设计的产品选型

### 开发信建议
- 收件人：**A 档直发 `Frank.Johnson@ISGInc.com`**（ISG Energy BU VP，官网一手）
- 🔴 **务必用 `isginc.com` 域**，**切勿**按官网 `rewarner.com` 臆造收件人（H2/§八）
- 抬头/称呼：Frank（具名，PE）
- 收件人策略：若 Frank 无回应，改发 `Ted.Beltavski@ISGInc.com`（原 R.E. Warner CEO，现 Executive Advisor）—— 但**一家只发 1 人**
- 发送时段：美国 Eastern Time（OH）周二–周四上午 = 北京时间约 21–23 点
- 送达配置：M365 收信 + SPF `-all` 硬失败 → 发件域三件套（SPF/DKIM/DMARC）必须齐；建议纯文本、单发
- 附件：不带名录/供货记录 PDF

### ⚠️ 矛盾点与风险提示
- 🔴 **域名陷阱（最高优先）**：官网域 `rewarner.com`，**邮箱域是 `isginc.com`** —— 按官网域拼写收件地址会**发错/退信**。已在「开发信建议」显式提醒。
- 🔴 **主体已变更**：公司**已于 2026-06 并入 ISG**，抬头应写 **"R.E. Warner & Associates, now part of ISG"**（官网口径），勿仍以独立公司身份称呼。
- ⚠️ **价值链位置偏弱**：**设计工程公司 ≠ 采购方**。他们**制定规格**但**不直接下单**。若目标是"卖设备"，这家应定为**规格影响型 / 长期培育型**，而非首批成交对象。**这是本单最大的定位风险，写信环节务必知情。**
- ⚠️ **Ted Beltavski 角色**：已从 President/CEO 转为 **Executive Advisor**（半退居二线）→ 不作主送。
- ⚠️ **收购后采购是否上收 ISG**：未证实。

### 信息缺口清单（请勿编造）
- Frank Johnson 的**任职时长 / 是否仍在 Energy BU 一线**：未获取
- **R.E. Warner 是否自行采购变压器**（vs 客户/公用事业方采购）：**未证实** —— 🔴 关键缺口
- 公司**营收 / 常用变压器容量与品牌**：未获取
- **并入 ISG 后采购是否上收**：未证实
- Frank Johnson 的**直邮是否仍在用**（isginc.com 一手明文，未跑 SMTP）：未复核

### 一句话画像
Cleveland 75 年历史的变电站设计院——**2026-06 刚并入 ISG，电力业务由 VP Frank Johnson 主管**；它不是买家，是**规格制定方**，切入点是"让我们的 UL 液浸变进你们的变电站规格书"。

### 渠道覆盖清单（L-1、L0–L7）
| 层 | 结果 | 一句话 |
|---|---|---|
| L-1 锁人 | ✅ | Energy BU VP + 原 CEO + 项目执行/PM 四人锁 |
| L0 官网 | ✅ | ISG Energy BU 页 + people 页拿到具名邮箱（一手）|
| L1 政府一手 | ⚠️ | 收购新闻稿（ISG 官网）；公司注册未查 |
| L2 命名+DNS | ✅ | `{First}.{Last}@ISGInc.com` 规则（多人一致）；域=isginc.com |
| L3 B2B库 | ⚠️ | LinkedIn 现职旁证 |
| L4 社媒协会 | ✅ | LinkedIn 个人页 + 政府/媒体收购报道 |
| L5 黄页同址 | ✅ | ISG Cleveland 地址交叉 |
| L6 电话表单 | ✅ | 440.835.9400（未拨打）|
| L7 付费 | ❌ | 未启用 |
