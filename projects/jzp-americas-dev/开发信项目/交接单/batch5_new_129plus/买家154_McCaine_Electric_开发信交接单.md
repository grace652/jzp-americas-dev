# 【买家 154】开发信交接单 — McCaine Electric Ltd.（Canem Group 成员）

> 采集日期：2026-09-28 ｜ 名单来源：`线索资产/目标客户清单.csv` 序号 21（A 类 · 电气承包商/工程公司）
> 采集方：找客户环节（本环节只产出交接单，不写正文/不碰模板/不定话术）
> ⚠️ 本表严格区分「已验证」与「未获取」，未找到的信息一律标注，**不做推断填充**（H1）
> ✅ 一句话结论：**温尼伯的老牌电气承包商，1918 年成立（107 年），1942 年注册**；
> 自述为 **"Manitoba 与西北安大略最大的独立电气承包商"**；
> 服务工业/机构/商业客户，含 **IGF 球场、温尼伯警察总部、RBC 会展中心、曼尼托巴大学、
> St. Boniface 医院心脏护理中心、Trans Canada Pipelines**；
> 🔴 **2011 年被 Canem 集团收购**（全国性电气承包商，**10 个办公室、900+ 员工**）；
> 联系人：⚠️ **John Schubert（President）—— 但疑已离任**（LinkedIn 显示其现属 Osprey Capital）；
> 邮箱 **`mccaine@mccaine.com`（行业协会名录明文，B 档）**；
> 🔴 **域 SMTP 对未授权来源不透露目录 ⇒ 探测无效**（第 ③ 类网关行为）。

---

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示(如有)
McCaine Electric Ltd. | ⚠️ 未确认（原 President John Schubert 疑已离任）| — | mccaine@mccaine.com | ⚠️ 行业协会名录明文；🔴 域 SMTP 探测无效（不透露目录）| ⚠️ 未获取 | 温尼伯老牌电气承包商，1918 年成立、1942 年注册；自述"Manitoba 与西北安大略最大的独立电气承包商"；服务工业/机构/商业；能力含电气安装/维护/服务、design-build、结构化布线、安防、智慧建筑、能源管理；项目含 IGF 球场、温尼伯警察总部、RBC 会展中心、曼尼托巴大学、St. Boniface 医院、Trans Canada Pipelines；2011 年被 Canem 集团（10 办公室/900+ 员工）收购 | 官网 + 行业协会资料（Safety Services Manitoba / Business Elite Canada）+ LinkedIn（John Schubert）+ 第三方（companylisting/PitchBook）+ DNS/SMTP 探测 | 🔴 集团采购绑定风险（Canem 900 人集团）；⚠️ 具名联系人疑已离任；⚠️ 域名 SMTP 探测无效
```

**发信资格：❌ 不合格**（**无具名在职联系人** —— 唯一线索已疑离任）
**邮箱档位：B（角色邮箱 · 行业协会名录明文）**

> 🔴 **本单依任务交接书 §4.4 判定为「疑似 + 缺口」类，不直接进写信环节。**
> 理由：**未获可确认的在职具名联系人**（John Schubert 已疑离任）。
> ⚠️ 另须标注：**Canem 集团采购绑定风险**。

---

## 二、补充信息（扩展段）

### 标准字段明细

| 项 | 内容 | 来源 |
|---|---|---|
| **公司全称** | **McCaine Electric Ltd.** | 行业资料（一手业务名录）|
| **国家 + 城市** | **加拿大 MB 省 Winnipeg（温尼伯）** | 行业资料（一手）|
| **州省** | **MB ✅**（CSV 填 MB，**正确**）| — |
| **详细地址** | **106 Lowson Crescent, Winnipeg, MB R3P 2H8**（🟢 行业名录明文；⚠️ **官网未验证到，官网抓取失败**）| 行业名录 |
| **电话** | **204-786-2435**；Toll Free **1-877-786-2435**；Fax **204-783-2180**（🟢 行业名录明文）| 行业名录 |
| **邮箱** | **`mccaine@mccaine.com`**（🟢 行业协会资料明文；⚠️ **非具名邮箱**）| 行业名录 |
| **注册信息** | **incorporated 1942**（行业资料明文 *"**Incorporated in 1942**"*）；1918 年成立 | 行业资料 |
| **成立年份** | **1918**（行业资料明文 *"established in Winnipeg following the First World War in **1918**"*；2018 年庆祝 **100 周年**）<br>⚠️ 注意：**1918 年成立 / 1942 年注册**，两个年份均需如实标注 | 行业资料 |
| **域名** | 🔴 **`mccaine.com`（邮件域）**；**`mccaine.ca` 无 MX**（不承载邮件）| 实测确认 |
| **邮件网关** | **Microsoft 365**（`mccaine-com.mail.protection.outlook.com`）+ ⚠️ **Azure 多租户配置**（TXT 含 base64 `YXp1cmVfY29tbW9u` = **"azure_common"**）| DNS |
| **SPF** | ⚠️ **未在 TXT 中检出标准 SPF 记录**（TXT 返回多条验证记录，未见 v=spf1）| DNS TXT |
| **DMARC** | `v=DMARC1; p=quarantine`（⚠️ 中等严格）| DNS |
| **归属** | 🔴 **Canem Group 成员**（**2011 年被收购**）—— Canem 为全国性电气承包商，**10 个办公室、900+ 员工** | 行业资料 + Canem 官网 |
| **规模** | ⚠️ 第三方称 **115 名员工**（companylisting.ca）；行业资料称 2011 年被收购后 *"growing McCaine to **over 250 field electricians**"*；⚠️ **两个数字口径不同**（可能为不同时点）| 第三方（未证实）|
| **协会** | **WCA、EAM、CCA、BOMA**（行业资料明文）| 行业资料 |
| **官网** | http://www.mccaine.com（⚠️ **本环节多次抓取失败/超时，未能直接读取官网内容**）| — |

> ⚠️ **数据来源限制说明**：**本单官网 `mccaine.com` 在本环节多次抓取失败**
> （WebFetch 报错 + curl 经代理超时）。**⇒ 公司信息主要来自行业资料与第三方**，
> **已如实标注来源级别**（H1/H5）。

### 🔴 第一发现：归属 Canem 集团 —— 集团采购绑定风险

🔴 **关键事实**（行业资料 + Canem 官网，逐字）：

> *"In **2011, McCaine was purchased by **Canem**, a national electrical contracting firm,
> growing McCaine to over 250 field electricians."*
> *"Today, McCaine serves many clients across the province and, **as part of Canem**,
> offers services from Ontario to BC, averaging in revenue **excess of $250 million nationally**."*（行业资料）
> Canem 官网：*"With **10 offices across Canada** and a workforce of **more than 900 people**,
> Canem operates in a diverse cross-section of public and…"*（Canem 官网，一手）

🔴 **业务含义（供写信环节自行判断，本环节不定话术）**：
- 🔴 **McCaine 是 Canem 集团的地区成员，不是独立公司** ⇒
  **采购决策可能受集团层面管控**（与买家 137 RIES 归属 NuVolt 的情形同类）。
- ⚠️ **集团规模大**（10 办公室 / 900+ 员工 / 年营收 $250M+）⇒
  **大概率有集团级采购体系** ⇒ **单点触达 McCaine 未必能推动采购决策**。
- ✅ **但集团是「电气承包商」，不含变压器制造业务** ⇒ **⓪ 层不排除**
  （与买家 138 ETAC、143 Trinity Power 的「同业制造/销售」性质不同）。
- ⚠️ **⇒ 结论：可开发，但必须标注「集团采购绑定」风险，建议以「进入 Canem 集团供应商体系」为目标。**

### ⚠️ 第二判断：业务对口度偏弱（须如实标注）

行业资料描述其业务（逐字）：
> *"provides **electrical installation, maintenance and services** to a large number of clients in the
> **industrial, institutional and commercial** markets."*
> *"Primarily serving clients in need of commercial, light industrial, institutional **electrical, data and
> security services**."*
> *"McCaine's strongest sector is **commercial** with the **security group growing rapidly**."*

🔴 **业务含义**：
- ⚠️ **未见「变压器」「变电站」「高压」任何表述** ⇒ **不得推断其采购变压器**（H1）。
- 其**最强领域是商业电气与安防**（structured cabling / security），**非电力工程**。
- ✅ **但项目体量大**：IGF 球场、警察总部、RBC 会展中心、大学、医院 ⇒ **大型机构项目**。
- ⚠️ **⇒ 归入「可能触及但未明示」类**，且**因集团采购绑定，优先级应下调**。

### 联系人（含 still_here 在职核验）

| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| ⚠️ **John Schubert**（**疑已离任**）| 原 President | 🔴 **口径与时效冲突**：<br>① 行业资料逐字：*"**John Schubert, President, McCaine Electric Ltd. and Vice President, Business Development, Canem Group of Companies**"*（⚠️ **该资料为 2014 年前后**）<br>② **LinkedIn 自述**：*"I **was** President of McCaine Electric Ltd. since 1979…"*（**过去式**）<br>③ **Osprey Capital Partners 页面**：*"John Schubert **currently served as** President of McCaine Electric Ltd."*（⚠️ 措辞模糊，实为其投资机构履历）| **1979–约 2016**（LinkedIn 自述 *"since 1979"*；另据 Business Elite *"Frank and John stayed on during the transition for **three and five years**"* ⇒ **约 2016 年离任**）| 🔴 **低**（LinkedIn 现职为 Osprey Capital Partners）| 🔴 **高（已离任）** | ca.linkedin.com/in/john-schubert-ba-mba-p-gsc-aaa25126（仅摘要可见）|
| Jason Rice | **Safety Coordinator** | ⚠️ **仅行业资料提及**（*"Jason Rice, McCaine's **Safety Coordinator**"*）；⚠️ **职能为安全，与采购无关** | ⚠️ 未知 | ⚠️ 未知 | ⚠️ 未知 | ⚠️ 未获取 |

> 🔴 **机读结论（本单最大缺口）**：
> 1. 🔴 **John Schubert 已疑离任**：
>    - 行业资料（约 2014 年）称其为 **President of McCaine + VP Business Development of Canem Group**；
>    - 但 **LinkedIn 自述用过去式**（*"I **was** President… since 1979"*）；
>    - **Osprey Capital Partners**（其现属投资机构）页面措辞为 *"currently served as"*（模糊）。
>    - Business Elite 资料称 **2011 年被收购后 John 留任 5 年** ⇒ **约 2016 年离任**。
>    ⇒ **判定：John Schubert 已离任，不得作为收件人交付**（违反 still_here 要求）。
> 2. 🔴 **未找到 McCaine 现任负责人**：官网抓取失败 + 行业资料均为旧数据
>    ⇒ **未能确认任何在职具名联系人** ⇒ **依 §4.4 判定不合格。**
> 3. ⚠️ **Jason Rice（Safety Coordinator）职能与采购无关** ⇒ 不适用。
> 4. ⚠️ **公司归属 Canem 集团后，管理层可能已集团化**（Canem 派驻）⇒ 建议从 **Canem 集团层面**找人。

### 邮箱分档（A/B/C）

| 档 | 地址 | 依据 | 可否主送 |
|---|---|---|---|
| **B** | **`mccaine@mccaine.com`** | 🟢 **行业协会资料明文**（非官网）；⚠️ **角色邮箱** | ⚠️ 仅备用（无具名联系人）|
| A | ⚠️ **未获取** | — | — |
| C | 任何推测格式 | 🔴 **域 SMTP 对未授权来源不透露目录**（连 `info@` 都 550）⇒ **探测无效，无法证伪** | ⛔ **禁用**（H2）|

**🔴 邮箱验证方法与证据链（可复现）：**

```
域名 mccaine.com（邮件域）
MX   = mccaine-com.mail.protection.outlook.com   （M365 + Azure 多租户）
TXT  = 含 base64 `YXp1cmVfY29tbW9u` = "azure_common"（多租户标识）
SPF  = ⚠️ 未检出标准 SPF 记录
DMARC= v=DMARC1; p=quarantine

SMTP RCPT 探测（控制组协议 —— 关键诊断）：
  ---- 第 1 轮 ----
  550 5.4.1  zzz_nonexistent_probe_9987@mccaine.com   ← 随机 550
  550 5.4.1  info@mccaine.com                         ← 🔴 连 info@ 也 550 ⇒ 异常！
  ⇒ ⚠️ 疑似「源 IP 被封」或「网关策略」—— 触发对照实验。

  ---- 对照组（用已知可用域验证源 IP）----
  250 2.1.5  info@martechelectrical.com               ← 🟢 对照组 250
  ⇒ ✅ 【源 IP 未被封】—— 排除第 6 类（IP 封锁）。

  ---- 第 2 轮（追加 .ca 域测试）----
  550 5.4.1  zzz_nonexistent_probe_9987@mccaine.com   ← 仍 550
  550 5.4.1  info@mccaine.com                         ← 仍 550
  452 4.5.3  info@mccaine.ca   :: "Recipients belong to multiple tenants"  ← ⚠️ 关键线索！
  ⇒ 452 提示「多租户」，但 `mccaine.ca` **无 MX 记录**（不承载邮件）

⇒ 🔴 【综合判定】：**该域对未授权来源【不透露目录】—— 连 `info@` 都返回 550**
   （而对照组证明源 IP 正常）⇒ 属第 ③ 类网关行为「不透露目录 + 授权闸门」。
   ⇒ ⛔ **SMTP 对 mccaine.com 探测无效。**
   ⇒ `mccaine@mccaine.com` 的可信度【不依赖 SMTP】，而依赖【行业协会资料明文】。
```

> ⚠️ **连带影响**：**任何具名格式都无法验证或证伪** ⇒ **⛔ 严禁推测**（H2）。

---

## 三、开发信建议（**仅限：收件人 / 时机 / 附件 —— 不含正文、不含主题行、不含开场句**）

> ⚠️ **本单因缺具名在职联系人，暂不建议进入写信环节。** 本节内容仅供参考。

| 项 | 建议 | 依据 |
|---|---|---|
| **主送** | ⚠️ **待补人**；若必须投，用 `mccaine@mccaine.com` | 合格线闸门 |
| **⛔ 禁用** | 不要投 John Schubert（**已疑离任**）| LinkedIn + 行业资料 |
| **第二触达** | 电话 **204-786-2435**／Toll Free **1-877-786-2435** | 行业名录 |
| **建议时机** | **中部时间工作日 08:00–10:00**（Winnipeg = **America/Winnipeg / CT**）| — |
| **建议附件** | ① **E541627**（配电变）—— 主推（其最强领域为商业电气）<br>② 公司介绍 | 属「可能触及但未明示」类 |
| **切入角度提示**（**仅提示，不代拟文案**）| ⚠️ **建议优先考虑从 Canem 集团层面切入**（900 人集团，有集团采购体系）<br>其项目含 **IGF 球场 / 警察总部 / RBC 会展中心 / 医院 / 大学**（大型机构）| 行业资料（一手）|
| ⚠️ **定位提醒** | 🔴 **① 无具名在职联系人 ② Canem 集团采购绑定 ③ 业务对口弱** ⇒ **建议降优先级** | 见上 §二 |
| ⛔ **禁止事项** | ① **不得推测具名邮箱**（域不透露目录，H2）；② **不得投递已离任的 John Schubert**；③ 不得称其「做变压器/高压」（无表述，H1）；④ 首封不报交期/价格 | — |

---

## 四、合规自查（H1–H7）

| 规则 | 自查结果 |
|---|---|
| **H1 不虚构** | ✅ **明确说明官网抓取失败、信息主要来自行业资料**；1918/1942 两个年份均如实标注；员工数两个口径并列；**明确标注 John Schubert 疑已离任** |
| **H2 不臆造邮箱** | ✅ 明确说明域不透露目录 ⇒ **探测无效** ⇒ **禁止推测**；只用行业资料明文 |
| **H3 格式校验 + ≥1 交叉来源** | ⚠️ 邮箱格式合法；**但无具名在职联系人 ⇒ 未过合格线** |
| **H4 标注验证状态** | ✅ **完成 still_here 核验并发现 John Schubert 疑已离任**（本单最重要合规动作）；记录对照组诊断过程 |
| **H5 交叉验证需 ≥1 第一方** | ⚠️ **官网抓取失败** ⇒ 公司信息依赖行业资料（第三方业务名录）；**人员层面无第一方** ⇒ 如实标注 |
| **H6 角色邮箱不得单独交付** | 🔴 **本单只有角色邮箱 ⇒ 依 H6 不得单独交付 ⇒ 判定不合格**（已在开头明示）|
| **H7 落盘 .md** | ✅ 本文件 |

---

## 五、给下一环节的交付说明

**🔴 本单判定：不合格（无具名在职联系人 + 集团采购绑定）→ 建议降优先级。**

**可直接使用的成果（公司层面）：**
1. **公司公开业务事实**：温尼伯；**1918 年成立（107 年）/ 1942 年注册**；
   自述 *"Manitoba 与西北安大略最大的独立电气承包商"*；
   服务工业/机构/商业；能力含电气安装/维护、design-build、结构化布线、安防、智慧建筑；
   项目含 **IGF 球场、温尼伯警察总部、RBC 会展中心、曼尼托巴大学、St. Boniface 医院、Trans Canada Pipelines**；
   协会 WCA / EAM / CCA / BOMA
2. 地址 **106 Lowson Crescent, Winnipeg, MB R3P 2H8** + 电话 **204-786-2435**
3. 邮箱 **`mccaine@mccaine.com`**（行业协会资料明文）
4. 🔴 **归属 Canem 集团**（2011 年收购；Canem = 全国性，**10 办公室 / 900+ 员工 / 年营收 $250M+**）

**必须知悉的风险：**
1. 🔴 **无具名在职联系人** —— 原 President John Schubert **已疑离任**（约 2016 年）
2. 🔴 **Canem 集团采购绑定** ⇒ 采购决策可能受集团管控（与买家 137 RIES 同类）
3. ⚠️ **官网 `mccaine.com` 本环节多次抓取失败** ⇒ 信息主要依赖行业资料（时效存疑）
4. ⚠️ **业务对口度弱**（最强领域为商业电气与安防，非电力工程）
5. 🔴 **域对未授权来源不透露目录** ⇒ SMTP 探测无效
6. ⚠️ **SPF 记录异常**（TXT 中未检出标准 v=spf1）

**补人建议渠道（供后续专项补人）：**
- 🔴 **优先从 Canem 集团层面找人**（`canem.com`，集团有采购体系，比单点触达 McCaine 更有效）
- ⚠️ 官网 `mccaine.com` 需在网络条件改善后重试抓取
- ⚠️ 行业协会（EAM = Electrical Association of Manitoba）会员名录（⚠️ **须做 still_here 核验**，参见买家 150 教训）

**本环节未做（属其他环节职责）：**
- 未写正文、主题行、开场句、钩子、产品切片（→ 环节 ② 写开发信 agent）
- 未定最终发送时间与时区窗口排程（→ 环节 ③/④ 脚本）
