# 【买家 153】开发信交接单 — Steinmetz Corporation（The Steinmetz Corporation）

> 采集日期：2026-09-28 ｜ 名单来源：`线索资产/目标客户清单.csv` 序号 18（A 类 · 电气承包商/工程公司）
> 采集方：找客户环节（本环节只产出交接单，不写正文/不碰模板/不定话术）
> ⚠️ 本表严格区分「已验证」与「未获取」，未找到的信息一律标注，**不做推断填充**（H1）
> ✅ 一句话结论：**威斯康星州 Appleton 的电力工程服务公司，1977 年成立（48 年）**；
> 客户约 **200 家**，覆盖**中西部**，服务对象含 **investor-owned utilities（投资者所有制电力公司）、
> municipal utilities（市政电力公司）、大型工业、机构**；
> 官网自述 *"From **high voltage systems to low voltage systems**"*；
> 联系人 **Scott Steinmetz（President，电气工程师）** —— ⚠️ **仅第三方双源，官网无人员页**；
> 🔴 **邮箱未获取**（官网 Contact 页仅表单；且**邮件服务器直接封锁我方源 IP，SMTP 完全无法探测**）。
> ⚠️ **CSV 州省填 IL（伊利诺伊）—— 实为 WI（威斯康星），已更正。**

---

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示(如有)
Steinmetz Corporation | Scott Steinmetz | President, electrical engineer | ⚠️ 未获取 | ⛔ 无法验证（邮件服务器封锁我方源 IP）| linkedin.com/in/scott-steinmetz-a1280751（仅摘要可见）| 威斯康星州 Appleton 的电力工程服务公司，1977 年成立；客户约 200 家，覆盖中西部；服务对象含投资者所有制电力公司、市政电力公司、大型工业、机构；服务含电气工程与电力工程，自述覆盖"从高压系统到低压系统"、"从测试与维护到咨询工程"；拥有现代化设施 | 官网实抓（首页/contact-us 页）+ LinkedIn 摘要 + RocketReach + 第三方（buzzfile/dnb）+ DNS 实测 | 🔴 邮件服务器封锁我方 IP（SMTP 不可用）；⚠️ CSV 州省错误（IL→WI，已更正）；⚠️ 官网无邮箱明文、无人员页；⚠️ 具名联系人仅第三方双源
```

**发信资格：❌ 不合格**（**无可用邮箱渠道** —— 官网无邮箱明文 + SMTP 无法探测）
**邮箱档位：⚠️ 无（未获取任何邮箱）**

> 🔴 **本单依任务交接书 §4.4 判定为「疑似 + 缺口」类，不直接进写信环节。**
> 理由：**无任何可用触达邮箱**（官网仅表单 + 邮件服务器封锁）。
> ✅ **但公司业务对口度高（HV/LV + 公用事业客户）** ⇒ **建议列入「待补渠道」清单**。

---

## 二、补充信息（扩展段）

### 标准字段明细

| 项 | 内容 | 来源 |
|---|---|---|
| **公司全称** | **Steinmetz Corporation**（第三方亦称 *"The Steinmetz Corporation"*）| 官网（一手）|
| **国家 + 城市** | **美国 WI 州 Appleton（阿普尔顿）** | 官网（一手）|
| **州省** | 🔴 **WI ✅（威斯康星）** —— 🔴 **CSV 填 IL（伊利诺伊），错误，本单已更正** | 官网（一手）|
| **详细地址** | **2224 W. Pershing Street, Appleton, WI 54914**（🟢 官网明文，**第一方**）| 官网（一手）|
| **电话** | **Tel: 920-734-9699** ／ **Fax: 920-734-3569**（🟢 官网明文）| 官网（一手）|
| **邮箱** | 🔴 **未获取** —— 官网 **Contact 页仅有表单**，**未列任何邮箱** | 官网（一手）|
| **注册信息** | ⚠️ **未获取** | — |
| **成立年份** | **1977**（🟢 官网明文：*"**Since 1977** Steinmetz Corporation has been providing engineering services to **investor-owned utilities, municipal utilities, large industrials, and institutions**."*）| 官网（一手）|
| **域名** | steinmetzcorp.com（🔴 **邮件服务器封锁我方源 IP，SMTP 完全不可用**）| 探测确认 |
| **邮件网关** | 🔴 **Charter/Spectrum Business（Time Warner Cable Business）**（`mx1.biz.rr.com` / `mx2.biz.rr.com`）—— **老式 ISP 托管邮箱** | DNS MX |
| **SPF** | `v=spf1 include:_spf.twcbc.com ~all`（**~all 软失败**；`_spf.twcbc.com` = Time Warner Cable Business Class）| DNS TXT |
| **DMARC** | ⚠️ **未配置** | DNS |
| **规模** | **约 200 家客户**（官网明文 *"serves approximately **200 clients** throughout the **Midwest**"*）；⚠️ 员工数未获取 | 官网（一手）|
| **官网** | https://steinmetzcorp.com（⚠️ WordPress 站，部分子页 404）| — |

> 📌 **技术旁证**：其邮件托管在 **Charter/Spectrum Business（rr.com）** ⇒
> **属小型企业常见配置**（自建域但用 ISP 邮箱），**非企业级邮件系统**（无 M365/Google）。
> ⚠️ 且其 SPF/DMARC 配置较基础 ⇒ **提示公司规模不大、IT 投入有限**。

### ✅ 第一判断：业务对口度较高（HV/LV 全覆盖）

官网 **首页原文**（一手，逐字）：

> *"The Steinmetz Corporation serves approximately **200 clients** throughout the Midwest, specializing in
> a full range of **electrical engineering services, and electrical power engineering**."*
> *"Since 1977 Steinmetz Corporation has been providing engineering services to **investor-owned utilities,
> municipal utilities, large industrials, and institutions**."*
> *"Our professional personnel have developed expertise in all aspects of electrical power.
> **From high voltage systems to low voltage systems, from testing and maintenance services to
> consulting engineering.** Whatever your need, we've got you covered."*

🔴 **业务含义（供写信环节自行判断，本环节不定话术）**：
- ✅✅ **客户结构极优**：**investor-owned utilities + municipal utilities** ——
  **这是电力公司（公用事业）** ⇒ **变压器采购的主力客户类型**。
  （对比：本批次多数客户是承包商，而**这家直接服务公用事业**。）
- ✅ **"From high voltage systems to low voltage systems"** ⇒ **HV 能力明确**。
- ✅ **"testing and maintenance services to consulting engineering"** ⇒ **测试/维护 + 咨询**双线。
- ✅ **1977 年至今 48 年**，客户约 200 家 ⇒ **稳定经营、客户基础扎实**。
- ⚠️ **但它是「工程服务公司」，不是「设备采购方」** —— 与服务对象（公用事业）的关系是**工程咨询/服务**。
  **⇒ 采购影响力为间接（为其客户做工程服务），不得当作直接买方**（H1）。

### 联系人（含 still_here 在职核验）

| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| **Scott Steinmetz** | **President（首封主送候选）** | ⚠️ **仅第三方双源（均非官网）**：<br>① LinkedIn 标题：*"**President, electrical engineer** at Steinmetz Corporation"*<br>② RocketReach：*"**Scott Steinmetz** is the President…"* | ⚠️ 未知 | ⚠️ **未知**（LinkedIn 页存在，近期活跃度无法确认）| **低**（推测为家族企业主，⚠️ 推断）| linkedin.com/in/scott-steinmetz-a1280751（仅摘要可见）|

> 🔴 **机读结论（须谨慎）**：
> 1. **Scott Steinmetz = President，但【官网无人员页、无第一方来源】** ⇒
>    **不满足 H5（交叉验证需 ≥1 第一方）**。
>    ⇒ **职务标注为「待官网证实」**；⛔ **正文中不得强调其职称**，建议**直呼姓名**。
> 2. ⚠️ **姓氏 "Steinmetz" 与公司同名** ⇒ **疑为家族企业/创始人后代**（⚠️ **推断，非事实**）。
>    （注："Steinmetz" 亦是电气工程史上的著名人物 —— Charles Proteus Steinmetz，GE 科学家；
>    ⚠️ **无任何证据表明两者有关**，**不得在信中建立此联想**。）
> 3. ⚠️ **公司无团队页** ⇒ **无其他可确认的管理层**。
> 4. 🔴 **但即使职务成立，本单也无法触达** —— **无邮箱渠道**（见下）。

### 邮箱分档（A/B/C）

| 档 | 地址 | 依据 | 可否主送 |
|---|---|---|---|
| ⚠️ **无** | ⚠️ **未获取任何邮箱** | 官网 Contact 页**仅表单**，未列任何邮箱 | ⛔ **不可投递** |
| C | ⚠️ 任何推测地址 | 🔴 **邮件服务器直接封锁我方源 IP**（`554 … blocked`）⇒ **SMTP 完全无法探测**，**连连接都建立不了** | ⛔ **禁用**（H2）|

**🔴 邮箱验证方法与证据链（可复现）：**

```
域名 steinmetzcorp.com
MX   = 10 mx1.biz.rr.com / 10 mx2.biz.rr.com   （🔴 Charter/Spectrum Business —— 老式 ISP 托管邮箱）
SPF  = v=spf1 include:_spf.twcbc.com ~all      （Time Warner Cable Business Class）
DMARC= ⚠️ 无记录

SMTP 连接尝试：
  🔴 CONNECT-ERR SMTPConnectError:
     554 p-bc5-impin002.msg.pkvw.co.charter.net cmsmtp
     **223.64.2.43 blocked**. Please see https://www.spectrum.net/support/…
     AUP#In-1130
  ⇒ 🔴 判定：**邮件服务器在【连接阶段】即拒绝我方源 IP** ⇒
     **连 SMTP 会话都建立不了** ⇒ **完全无法探测**（属第 6 类「源 IP 被封锁」的新变体：
     前次是 Spamhaus 封在 RCPT 阶段，本次是 Charter 封在 CONNECT 阶段）。
  ⇒ ⛔ **本单无法通过 SMTP 获取任何邮箱信息。**
```

> 🔴 **重要提示**：
> 1. **本次封锁方是 Charter/Spectrum（ISP 自身），不是 Spamhaus** —— 说明**封锁来源在扩大**。
> 2. **我方源 IP `223.64.2.43` 已被多家邮件服务标记** ⇒
>    **该问题已在买家 129–152 多单中反复出现**，**是发送环节的首要阻塞项**。
> 3. ⛔ **本单无任何可用邮箱** ⇒ **必须改走其他渠道**（见「补渠道建议」）。

---

## 三、开发信建议（**仅限：收件人 / 时机 / 附件 —— 不含正文、不含主题行、不含开场句**）

> ⚠️ **本单因无可用邮箱渠道，暂不建议进入写信环节。** 本节内容仅供参考。

| 项 | 建议 | 依据 |
|---|---|---|
| **主送** | ⛔ **无可用邮箱** —— 需先补渠道 | — |
| **替代触达（重要）** | ✅ **（1）官网 Contact 表单**（唯一官网渠道）<br>✅ **（2）电话 920-734-9699**（官网明文）<br>⚠️ **（3）传真 920-734-3569**（官网明文 —— 老式企业仍可能用真）| 官网 Contact 页（一手）|
| **建议时机** | **中部时间工作日 08:00–10:00**（Appleton, WI = **America/Chicago / CT**）| — |
| **建议附件** | ① **E541626**（三相液浸 POWER 变，750–110,000 kVA / 72–121 kV）—— **其服务对象为公用事业，且官网明述 HV**<br>② **E541627**（配电变）—— 备用<br>③ 公司介绍 | ⚠️ **但须注意红线：对美国客户主推配电级** |
| **切入角度提示**（**仅提示，不代拟文案**）| ✅ **最大亮点：其客户是 investor-owned utilities 与 municipal utilities**<br>⇒ **公用事业是变压器采购的主力**（但该公司是**工程服务方**，非直接买方）| 官网首页（一手）|
| ⚠️ **定位提醒** | 🔴 **无邮箱 ⇒ 本单暂时不可执行**；且**其为工程服务方，采购影响力为间接** | 见上 §二 |
| ⛔ **禁止事项** | ① **不得推测任何邮箱**（服务器封锁，H2）；② **不得在信中提及 Charles Proteus Steinmetz**（无证据关联）；③ 对美国客户**不主动推高压主变**（红线）；④ 首封不报交期/价格 | — |

---

## 四、合规自查（H1–H7）

| 规则 | 自查结果 |
|---|---|
| **H1 不虚构** | ✅ 邮箱明确标「未获取」；职务标为「仅第三方，待官网证实」；家族企业标为推断；**明确禁止 Steinmetz 名人联想** |
| **H2 不臆造邮箱** | ✅ **明确说明 SMTP 完全不可用** ⇒ **禁止推测任何邮箱**；如实交付「无邮箱」 |
| **H3 格式校验 + ≥1 交叉来源** | 🔴 **不满足**（无邮箱可交付）⇒ 已如实标注不合格 |
| **H4 标注验证状态** | ✅ 完整记录 CONNECT 阶段封锁的原始报错文本 |
| **H5 交叉验证需 ≥1 第一方** | ⚠️ **公司层面**满足（官网第一方）；**人员层面不满足**（仅第三方）⇒ 已降级标注 |
| **H6 角色邮箱不得单独交付** | ⛔ **本单无任何邮箱** ⇒ **更无法满足 H6** ⇒ 判定不合格 |
| **H7 落盘 .md** | ✅ 本文件 |

---

## 五、给下一环节的交付说明

**🔴 本单判定：不合格（无可用邮箱渠道）→ 列入「待补渠道」清单。**

**可直接使用的成果（公司层面）：**
1. **公司公开业务事实**：威斯康星州 Appleton；**1977 年成立（48 年）**；
   **客户约 200 家，覆盖中西部**；服务对象含 **investor-owned utilities / municipal utilities /
   大型工业 / 机构**；服务含 **电气工程与电力工程**，自述 *"From high voltage systems to
   low voltage systems, from testing and maintenance services to consulting engineering"*
2. 地址 **2224 W. Pershing Street, Appleton, WI 54914**
3. 电话 **920-734-9699**／传真 **920-734-3569**
4. 可点名联系人 **Scott Steinmetz**（⚠️ 仅第三方双源，职务待官网证实）
5. 🔴 **CSV 州省已更正**：IL → **WI**

**必须知悉的风险：**
1. 🔴 **无任何可用邮箱** —— 官网仅表单 + **邮件服务器封锁我方 IP** ⇒ **本单当前不可执行**
2. 🔴 **邮件服务器在 CONNECT 阶段即封锁**（`554 … 223.64.2.43 blocked`）⇒ 连会话都建立不了
3. 🔴 **CSV 州省错误**（IL → WI）⇒ 已更正，影响时区判断（应按时区 **CT**）
4. ⚠️ **官网无人员页** ⇒ 具名联系人仅第三方来源
5. ⚠️ **业务定位是「工程服务方」，不是设备采购方** ⇒ 采购影响力为间接
6. 🔴 **域未配 DMARC** ⇒ 可被冒用，防钓鱼

**补渠道建议（供后续专项补渠道）：**
- ✅ **官网 Contact 表单**（唯一官网渠道，可靠但慢）
- ✅ **电话 920-734-9699**（官网明文，可作 B 档电话触达）
- ⚠️ **传真 920-734-3569**（老式企业仍可能使用）
- ⚠️ **换源 IP 后重试 SMTP**（若发送环节解决了 IP 封锁问题，本域即可探测）

**本环节未做（属其他环节职责）：**
- 未写正文、主题行、开场句、钩子、产品切片（→ 环节 ② 写开发信 agent）
- 未定最终发送时间与时区窗口排程（→ 环节 ③/④ 脚本）
