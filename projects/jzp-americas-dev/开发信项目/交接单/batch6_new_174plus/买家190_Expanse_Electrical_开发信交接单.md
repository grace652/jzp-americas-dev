# 【买家 190】开发信交接单 — Expanse Electrical Co.（OK/TX）

> 采集日期：2026-09-29 / 来源：batch6 名单（CSV 序 17）/ 一句话结论：**⓪ 层通过（EPC，非变压器制造商）**；锁定 **John Sutton（Supply Chain Manager）**，`john.sutton@expanseelectrical.com` 经 **SMTP RCPT 250 实证**，A 档可主送。

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示(如有)
Expanse Electrical Co.（EPC，输电+变电站 ≤345kV） | John Sutton | Supply Chain Manager（供应链/采购） | john.sutton@expanseelectrical.com | 已验证（SMTP RCPT 250 + Wiza 旁证） | linkedin.com/company/expanse-electrical-company | 70+ 年历史的电气/电力/自动化 EPC，输电+变电站 turnkey ≤345kV，含 Power Transformer Services；14 州持牌；2026-01 被 MidCentral Energy Partners 收购 | 官网 About/Contact + SMTP 实证 + Wiza/RocketReach/LeadIQ + 收购新闻 | 邮箱域=官网域（同为 expanseelectrical.com）；⚠️ 官网自述"UL Control Panel Manufacturer"（造控制柜，非变压器）；CSV 州省应更正
```

## 二、补充信息（扩展段）

### ⓪ 层反身排除（🔴 已完成，结论：不排除）
- **判定**：✅ **EPC 承包商**，**非变压器制造商/竞品代理/中国货源通道**。
- **证据原句（官网一手）**：
  - 首页："**Transmission & Substation Services** — Turnkey power delivery construction and maintenance services for power systems **up to 345kV**"
  - 首页："**Power Transformer Services** — Oil processing, inspection, maintenance and repair services to maximize the life of your transformers"
  - About："We serve as a **single-source provider** throughout a system's entire lifecycle… from engineering design and site preparation to energization"
  - About（Licenses）：14 州电气承包商执照（TX/OK/LA/AR/NM/CO/UT/WY/MT/ND/NE/AZ/VA/AL）
- **⚠️ 唯一需标注项**：About 页写 "**Certified UL Control Panel Manufacturer**（UL 508A / UL 698 / UL HazLoc）" —— 这是**制造控制柜/控制盘**，**不是变压器**，与我方产品线**不重合**（符合 §二十三：读全文判断，`Manufacturer` 出现在**不同品类**上）。**保留**，但写进风险段提示写信环节勿混淆。
- **判据对照**：全文**无** 变压器 `we manufacture` / `our factory` / `OEM 自称`；变压器相关动词为 `install / test / repair / service`（安全信号）。

### 标准字段明细
- 国家+城市：美国 **Oklahoma City, OK（总部）**；Texas 网点 Deer Park（Houston）/ Andrews / Gardendale；NM Carlsbad；ND Williston
  - 🔴 **CSV 州省修正**：CSV 记 `TX`，**实测总部在 OK（Oklahoma City）**，TX 为其网点之一。建议改为 `OK/TX`。
- 详细地址（总部）：914 N. Broadway Ave., Suite 230, Oklahoma City, OK 73102
- 电话：Houston/Deer Park (832) 399.0054；Andrews (432) 523.3530；Carlsbad (575) 885.8658；Williston (701) 774.1094
- LinkedIn：公司 linkedin.com/company/expanse-electrical-company
- 网站：expanseelectrical.com（WordPress；NS 为 Microsoft）
- 成立日：品牌口径 "more than 70 years"（沿革含多家并入公司）
- 规模：~145–206 人（RocketReach 145 / LeadIQ 206，第三方口径，**正文勿引用具体数字**）
- 营收：未获取
- NAICS：238210（电气承包，推断）
- 归属：**2026-01 被 MidCentral Energy Partners 收购**（EINPresswire 新闻稿）

### 联系人（含 still_here 在职核验）
| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| **John Sutton（主送）** | **采购/供应链** | Supply Chain Manager | 未获取 | 中：Wiza/RocketReach 现职=Expanse；基于 Houston TX | 低–中 | wiza.co/d/expanse-energy-solutions/7a23/john-sutton |
| Jerrit Coward（备选） | 最高层 | CEO & Chairman of the Board | 多年（创始人级） | 高：多源同期提及（Wiza/CIENCE/LinkedIn） | 低 | linkedin.com/in/jerrit-coward-9a048750 |
| Olivia Garcia | HR | Human Resources Manager | — | — | — | rocketreach 管理层 |

### 邮箱分档（A/B/C）
- **A档（具名，主送）**：`john.sutton@expanseelectrical.com` —— **已验证**：SMTP RCPT **250**（控制地址 `info@` 250 + 随机地址 550 + 对照组全 550），且 Wiza 显示格式 `j*****@expans***.com` 与之一致。
- **A档（备选）**：`jerrit.coward@expanseelectrical.com` —— SMTP RCPT **250**。
- 命名规则（本域实证）：**`{first}.{last}@`**（`jsutton@` 与 `jcoward@` 均 550，排除 `{f}{last}`）。
- H6 声明：不适用（已取得具名邮箱）。
- ⚠️ 仅**实测返回 250 的这两个具体地址**可用；**不得据 `{first}.{last}` 规则推导其他高管邮箱**（H2）。

### 我为什么找他
- 该公司**设有 Procurement Manager 岗位**（tealhq 招聘帖："lead strategic purchasing for critical **Substation projects**"），且管理层名单里 **John Sutton 挂 Supply Chain Manager** —— 即**采购/供应链岗**，比找 CEO 更对口。
- 其业务是 **EPC + 输电/变电站 turnkey ≤345kV**，**变压器是项目 BOM 里的核心采购项**；配合其 "Power Transformer Services" 线，说明他们**既装新机也管旧机**，我方既是新机来源也是替换来源。

### 买家类型 / 需求品类
- 买家类型：🔥 **A EPC（输电+变电站，≤345kV，含变压器服务）**
- 需求品类（带结论态，**美国客户不谈干变**）：
  - `主变/变电站变（三相液浸电力变 UL E541626，可直供，HV 72–121 kV / 750–110,000 kVA）` — 与其 ≤345kV 项目最贴合
  - `三相美变（UL E541627，可直供）` — 配电侧
  - `500kV 级主变（产能可覆盖，UL 区间外，需人工确认）` — 其能力上限 345kV，500kV 属机会型，**需人工确认**
  - ⛔ `干变（美国不匹配：无 UL）` — **不推**

### 电压·频率·认证要求
- 频率：60 Hz（美国）→ 零改造适配
- 电压：输电/变电站 **≤345kV**（官网自述）；配电侧常规
- 认证：美国要 **UL**（我方 E541626 / E541627 可直供）；对客户用 `UL certified, tested to IEEE C57.12 and ANSI standards`，**不写 CSA/SASO/SONCAP**
- 网关：MX = `expanseelectrical-com.mail.protection.outlook.com`（**M365 / Exchange Online**，SMTP 探测**有效**，见实证）

### 采购信号
- **设有 Procurement Manager 岗**（明确写 "critical Substation projects"）→ 采购职能制度化、对变压器有持续需求
- **2026-01 被 MidCentral Energy Partners 收购** → 整合期常见**供应商重审窗口**
- **新设 Power Services Division**（官网新闻）→ 变压器服务线扩张
- **承接 Fervo Energy 地热项目的高压 EPC**（官网新闻）→ 高压变电设备采购
- 官网："Our **warehouses are fully stocked** and ready to serve… 24 hours a day" → 有备货习惯

### 可利用的钩子（按强度排序）
1. **Substation / 345kV 项目的主变与配电变供货** —— 与其 Procurement Manager 的职责描述逐字对应
2. **MidCentral 收购后的供应商整合窗口** —— 新东家常重审采购
3. 新设 Power Services Division → 既有新机采购、也有旧机替换
4. 14 州持牌 + 多网点 → 全国交付能力匹配

### 开发信建议
- 收件人：**A 档直发 `john.sutton@expanseelectrical.com`**（Supply Chain Manager，SMTP 已验证）
- 备选：若 John Sutton 无回应，改发 `jerrit.coward@expanseelectrical.com`（CEO，已验证）—— ⚠️ 但**同一家公司只发 1 人**，勿同时发
- 抬头/称呼：John（具名）
- 发送时段：美国 Central Time（OKC）周二–周四上午 = 北京时间约 22–24 点
- 送达配置：**M365（Exchange Online）** 收信；建议纯文本、单发、控制频率，避免触发 Spamhaus 源 IP 拉黑；发件域三件套须齐
- 附件：不带名录/供货记录 PDF；可附 UL 编号说明

### ⚠️ 矛盾点与风险提示
- 🔴 **CSV 州省错误**：CSV 记 `TX`，**实测总部在 OK（Oklahoma City）**，TX 为网点 → 已在标准字段修正。
- ⚠️ **"UL Control Panel Manufacturer" 字样**：官网自称制造 **UL 508A 控制柜**（**非变压器**）。**不构成排除**，但写信环节**勿与我方产品混淆**，也不要主动提"你们也制造"。
- ⚠️ **集团收购**：2026-01 起属 **MidCentral Energy Partners** → 采购权可能向集团上收（参考 §三十 集团成员降级），列为**需观察项**。
- ⚠️ **员工数口径不一**（145 vs 206）：**正文绝不引用具体数字**。
- ⚠️ **John Sutton 任职时长未获取** → 无法判断是否新入职；开场避免"恭喜加入"类措辞。

### 信息缺口清单（请勿编造）
- John Sutton 的**任职时长 / 具体采购权限范围**：未获取
- 公司**营收 / 常用变压器容量与品牌 / 现有供应商**：未获取
- **MidCentral 收购后采购是否上收**：未证实
- **Jerrit Coward 是否仍任 CEO**（收购后管理层可能变动）：未证实
- 采购是否走**集团集中采购**：未证实

### 一句话画像
70 年历史的 OK/TX 高压 EPC——**输电+变电站 ≤345kV turnkey，专门设了 Procurement Manager 管"变电站项目战略采购"**，刚被 MidCentral 收购、正在整合，是主变/配电变最对口的对话对象。

### 渠道覆盖清单（L-1、L0–L7）
| 层 | 结果 | 一句话 |
|---|---|---|
| L-1 锁人 | ✅ | 供应链岗 John Sutton + CEO Jerrit Coward 双锁 |
| L0 官网 | ✅ | About/Contact 拿到总部/网点/持牌/认证（邮箱为表单） |
| L1 政府一手 | ⚠️ | 州持牌号已在官网列出（14 州）；收购新闻稿 |
| L2 命名+DNS | ✅ | 命名规则 `{first}.{last}@` 实证；M365 域探测有效 |
| L3 B2B库 | ✅ | Wiza/RocketReach/LeadIQ/CIENCE（旁证 + 与 SMTP 互证）|
| L4 社媒协会 | ✅ | LinkedIn 公司页；Schneider/Rockwell 联盟 |
| L5 黄页同址 | ⚠️ | 多网点交叉 |
| L6 电话表单 | ✅ | 各网点电话（未拨打）|
| L7 付费 | ❌ | 未启用 |
