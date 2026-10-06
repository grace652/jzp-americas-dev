# 【买家 214】开发信交接单 — Dulles Electric Supply Corp.

> 采集日期：2026-09-29 / 来源：batch6 名单（第 41 行，CSV 州省 VA、备注「弗吉尼亚电气供应（Sterling VA）」）/ 一句话结论：**弗吉尼亚 Sterling 的 1985 年家族电气分销商（照明 showroom + 电气供应柜台 + 商业项目部）**，⓪ 层通过（NAICS 全为批发类，无制造自述）；**采购一把手 Ryland Edwards（Director of Purchasing）已锁**，且官网第一方明文邮箱 **GMilotte@dulleselectric.com** 确认了 `FLast@` 命名规则 → 可推演 `REdwards@dulleselectric.com`（**待验证**，不可作主送），主送走 B 档：电话 703-450-5700 / 第一方 `weborders@dulleselectric.com` 点名转交。

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示(如有)
Dulles Electric Supply Corp. | Ryland Edwards（主送）/ John Milotte（备选） | Director of Purchasing / General Manager | 推演：REdwards@dulleselectric.com（待验证）；B 档：weborders@dulleselectric.com（第一方明文）/ 电话 703-450-5700 点名转交 | A 档具名：待验证（命名规则经第一方样本确认）；B 档角色：已验证（官网明文） | 公司 linkedin.com/company/dulles-electric-supply-corp；个人 linkedin.com/in/ryland-edwards | VA Sterling，1985 创立，照明 showroom 1.2 万尺 + 电气供应柜台 5 千尺 + 商业项目部（含 switchgear），51–200 人 | 官网 /pages/about-us + /pages/meet-the-team + /pages/de-design-group + /pages/credit-application + SAM.gov(GovCB) + LinkedIn/Wiza/RocketReach + DNS | 🔴 具名邮箱为「命名规则推演」，**不得作主送**；SMTP 探测失效（源 IP 被 Spamhaus PBL 拦截）；双域名并存（dulleselectric.com / dulleselectricsupply.com）
```

## 二、补充信息（扩展段）

### 标准字段明细
- 国家+城市：美国 Virginia，Sterling（Washington DC 都会区，ET 时区）
- 详细地址：22570 Shaw Rd Ste 150, Sterling, VA 20166（SAM.gov 登记地址）；官网显示 22570 Shaw Road, Sterling, VA 20166
- 电话：**703-450-5700**（官网主号）；571-323-7952（SAM.gov POC 线）；Supply Counter 西语专线 703-928-3408 / 703-906-2300；DE Design Group 571-323-7954
- 网站：**dulleselectric.com**（Shopify，A=23.227.38.65）；另有 **dulleselectricsupply.com**（企业购/目录站）+ catalog.dulleselectric.com（同一实体，MX 同为 serverdata exch029）
- **邮箱域**：`dulleselectric.com`（MX = `east/west.smtp.mx.exch029.serverdata.net` = **Intermedia**；SPF 含 intermedia / mailgun / constantcontact / protection.outlook.com，`-all`）
- 成立日：1985（官网 "since 1985"；SAM.gov Year Established 1985 —— 一致）
- 规模：51–200 人（Seamless 估算）；营收约 $5M+（Seamless 粗估，**未经一手源印证**）
- NAICS：**423390 / 423610 / 423690 / 423840 / 423850 / 423990**（SAM.gov，全为批发类）
- 社媒：linkedin.com/company/dulles-electric-supply-corp
- 州省核实：**CSV = VA ｜ 实测 = VA（Sterling）** —— 一致，无需修正

### 联系人（含 still_here 在职核验）
| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| **Ryland Edwards**（主送） | **采购一把手** | Director of Purchasing | 未获取 | 中：LinkedIn 现职描述「Direct all activities related to purchasing and inventory management across a multi-location supply network」 | 低（三源同期：LinkedIn / Wiza / RocketReach） | linkedin.com/in/ryland-edwards |
| John Milotte | 总经理（备选） | General Manager | 未获取 | 中：LinkedIn / RocketReach / AllBiz 三源 | 低 | linkedin.com/in/john-milotte-24142248 |
| Gloria Milotte | 事业部经理（DE Design Group，照明设计） | Division Manager | 未获取 | 高：**官网 de-design-group 页在列 + 第一方邮箱明文** | 低 | 未找到 |
| Kevin Fitzpatrick | 首席照明设计师（非采购） | Lead Lighting Designer | 未获取 | 高：官网在列 | 低 | 未找到 |

> 🔴 一家只发 1 人：**主送 Ryland Edwards（Director of Purchasing）** —— 采购岗优先于 GM/老板，且公司有商业项目部（switchgear/配电设备采购场景）。
> 备选（同公司不重复发）：John Milotte（General Manager）。

### 邮箱分档（A/B/C）
- **A 档（具名）**：**无已验证具名邮箱**。推演 `REdwards@dulleselectric.com`（依第一方样本 `GMilotte@` 确认的 `FLast@` 规则）→ 状态 **待验证**，**不可作主送**。
- **B 档（角色，官网第一方明文）**：
  - `weborders@dulleselectric.com`（全站页脚，官网明文）
  - `credit@dulleselectric.com`（/pages/credit-application 明文）
  - `GMilotte@dulleselectric.com`（/pages/de-design-group 明文，对应 **Gloria Milotte**，非采购岗）
- **主推路径（B 档）**：电话 **703-450-5700** 或 `weborders@dulleselectric.com`，**点名转交 Ryland Edwards, Director of Purchasing**；正文首句明确请求转交。
- 🔴 **H6 声明**：**具名决策人直邮未取得**（仅命名规则推演）。已跑「升级三步」：
  1. 挖职能邮箱：官网未见 `Purchasing@` / `Supplier@` 类；仅 `weborders@` / `credit@`
  2. 从真实样本反推命名规则：**成功** —— 官网第一方明文 `GMilotte@dulleselectric.com`（Gloria Milotte）= `{FirstInitial}{Last}@`
  3. 免费试推演：`REdwards@dulleselectric.com`（**推演，未验证**）
  → 结论：**可交付 B 档 + 一个「待验证」A 档候选**，已如实标注为风险。
- 🔴 **SMTP 探测结论（未采信）**：对 `dulleselectric.com`（Intermedia / serverdata）跑控制地址协议，**控制地址 `info@` 与随机地址均返回 `554 5.7.1 … blocked using pbl.spamhaus.org`（源 IP 223.64.3.115）** ⇒ 属**源 IP 级拦截**（渠道清单 §十五/§二十四类），**本轮探测整体作废**，不据此判任何地址存在/不存在。

### 我为什么找他
- Dulles 官网 "Meet The Team" 页**只列姓名不列职务**（Stephen Miller / Nizar Halabi / Ashton Dove / Will Kelley / Bharat Patel / Alaina Poindexter / Sharon Howard-Denny / Amanda Miller / Kyle Davis），但 **LinkedIn / Wiza / RocketReach 三源同期指向 Ryland Edwards 为 Director of Purchasing**，其自述职责原文「Direct all activities related to purchasing and inventory management across a multi-location supply network」—— 正是「多分店备货型」变压器采购的决策入口。
- 业务与品类直接对应：官网 /pages/commercial-department 明说「our commercial sales department can provide pricing for project bids of any size, or we can help with your specifications for your **commercial lighting and switchgear** needs」；/pages/about-us 亦写「From commercial or industrial lighting to **switch gear** we can provide it all」→ **有 switchgear / 配电设备的项目采购场景**。
- 命名规则可落地：官网第一方明文 `GMilotte@dulleselectric.com`（Gloria Milotte，Division Manager）**确证了 `FLast@dulleselectric.com` 规则**，使推演地址具备依据（非凭空拼写）。

### 买家类型 / 需求品类
- 买家类型：**A 分销商**（照明 showroom + 电气供应柜台 + 商业项目部；主营零售/承包商/商业项目）
- 需求品类（带结论态）：
  - `三相美变（UL E541627，可直供）` —— 商业项目部 switchgear / 配电场景
  - `单相柱上变（认证在办 E544629，条件切入）` —— 非首推
  - ⚠️ 美国客户：**不谈干变**（无 UL 不匹配）

### 电压·频率·认证要求
- 电压：未获取
- 频率：**60 Hz**（美国）
- 认证：我方 UL **E541627** 正式 CoC，适配美国

### 采购信号
- **商业项目部**公开承接「project bids of any size」+ switchgear 规格协助 → 项目制采购入口
- 自述「multi-location supply network」→ 多分店备货体系
- 线上目录站（dulleselectricsupply.com / catalog.dulleselectric.com）→ 有 SKU 管理/备货职能
- 1985 至今持续经营（40 年），SAM.gov 政府供应商登记（可投政府标）

### 可利用的钩子（按强度排序）
1. **商业项目部 + switchgear 品类**（官网明文）—— 与配电变压器最直接对口
2. **照明 + 电气双线、1.7 万尺门店**（showroom 1.2 万尺 + 供应柜台 5 千尺）—— 规模与专业度角度
3. **1985 年至今 40 年、DC 都会区老牌**—— 稳健传承角度
4. **多分店备货网络（multi-location supply network）**—— 供应链协同角度

### 开发信建议
- **收件人策略**：**不要**盲发推演地址 `REdwards@dulleselectric.com`（**待验证**，触 H2/H4）；走 **B 档** —— 电话 **703-450-5700** 或 `weborders@dulleselectric.com`，**点名转交 Ryland Edwards, Director of Purchasing**；正文首句明确请求转交
- 🔴 **域名提醒（务必照做）**：邮箱域为 **`dulleselectric.com`**（MX 在 serverdata/Intermedia）；**勿**写成 `dulleselectricsupply.com`（虽同一实体，但收信域以 `dulleselectric.com` 为准）
- **开场角度**：从其**商业项目部 switchgear 品类**切入（写信 agent 决定措辞）
- **发送时段**：华盛顿 **ET**，周二–周四当地上午 = **北京时间 21:00–23:00**（夏令时期间）
- **送达配置**：MX = **Intermedia（serverdata.net）**；SPF `-all` 硬；发信域须 SPF/DKIM/DMARC 齐备；纯文本
- **附件建议**：不带名录/供货记录；如需仅附 UL 证书号 + 容量区间

### ⚠️ 矛盾点与风险提示
- 🔴 **具名邮箱未验证**：`REdwards@dulleselectric.com` 系**命名规则推演**（规则由第一方样本 `GMilotte@` 确认，但该地址本身未经第二方印证）⇒ **不得作主送**。
- 🔴 **SMTP 探测失效**：`dulleselectric.com` 对来源 IP 返回 **Spamhaus PBL 554** ⇒ 无法用 RCPT 验证任何地址，**不要反复重试**。
- ⚠️ **双域名并存**：`dulleselectric.com`（Shopify 主站）与 `dulleselectricsupply.com`（企业购站，A=AWS）为**同一实体**（MX 同为 `exch029.serverdata.net`）—— 发信以 `dulleselectric.com` 为准。
- ⚠️ **规模数据仅第三方估算**（51–200 人 / ~$5M），**未获一手源印证**，正文勿引用具体数字。
- ⚠️ **Meet The Team 页无职务**：9 个姓名均无 title，无法从官网核验其职能（Ryland Edwards 的采购职务来自 LinkedIn/Wiza/RocketReach，非官网）。
- ⚠️ 公司名易混：与 **Dulles Electric & Supply Corp**（同一实体对外用名）注意区分写法。

### 信息缺口清单（请勿编造）
- Ryland Edwards 的**已验证具名邮箱**：**未找到**（仅推演）
- Ryland Edwards / John Milotte 的**任职时长**：未获取
- 公司**员工数 / 营收**（一手源口径）：未找到（第三方估算不可引用）
- 公司**常用变压器容量 / 电压 / 品牌**：未获取
- **VA 州注册主体全称 / 注册日**（VA SCC）：未查
- 采购**决策归属**（Ryland Edwards 是否独立决策 vs 需 GM John Milotte 会签）：未明
- **商业项目部负责人姓名**：未找到

### 一句话画像
DC 都会区一家 1985 年创立的家族电气分销商（照明 showroom + 供应柜台 + 商业项目部，含 switchgear）——**采购一把手 Ryland Edwards 已锁定，命名规则也由官网第一方邮箱 `GMilotte@` 确证**，但具名地址只能推演、SMTP 又被源 IP 拦截，**主送只能走电话 / 第一方角色邮箱点名转交**。

### 渠道覆盖清单（L-1、L0–L7）
| 层 | 结果 | 一句话 |
|---|---|---|
| L-1 锁人 | ✅ | LinkedIn/Wiza/RocketReach 三源锁 Director of Purchasing（Ryland Edwards）+ GM（John Milotte） |
| L0 官网 | ✅ | about / meet-the-team / de-design-group / credit-application / supply-counter 全抓；取到 3 个第一方明文邮箱 |
| L1 政府一手 | ✅ | SAM.gov 供应商档案（NAICS 全批发类 + POC 电话；无邮箱） |
| L2 命名+DNS | ✅ | `FLast@` 规则经第一方样本确认；MX=Intermedia；SMTP 探测被 Spamhaus PBL 拦截（作废） |
| L3 B2B 库 | ⚠️ | LeadIQ/Wiza/RocketReach 佐证职务（**互证不算印证，H5**） |
| L4 社媒协会 | ⚠️ | 公司 LinkedIn 页命中未直取；个人页经 WebSearch 摘要 |
| L5 黄页同址 | ⚠️ | Sterling VA 地址与 SAM.gov 登记一致 |
| L6 电话表单 | ✅ | 703-450-5700 + 官网表单（未拨打/未提交） |
| L7 付费 | ❌ | 未启用 |
