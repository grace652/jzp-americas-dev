# 【买家 291】开发信交接单 — M. J. Electric, LLC

> 采集日期：2026-10-01 ｜ 来源：batch8 名单（mjelectric.com，MI Iron Mountain）｜ 一句话结论：**密歇根 Iron Mountain 的多专业电气总承包商**（60 余年历史；transmission / substation / distribution / renewable / power / industrial / instrumentation / civil-foundation；**Quanta Services（NYSE:PWR）旗下**）—— 明确的「电气施工总承包」服务商（非制造、非竞品、非中国货源通道）；**采购一把手 Kory Pontbriand（Director of Purchasing）具名邮箱 `kpontbriand@mjelectric.com` 经 SMTP 控制地址法实测命中，且同域第二条命中 `tnagy@`（CEO）⇒ 命名规则 `{f}{last}@` 获规则级确认 = A 档 → 可主送。**
> ⚠️ 本表严格区分「已验证」与「未获取」；未找到的信息一律标注，不做推断填充。
> ✅ **本单过 A 档**：邮箱为**具名 + 采购一把手职能 + SMTP 双点实证（规则级确认）**，可作主送。

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示
M. J. Electric, LLC | Kory Pontbriand | **Director of Purchasing（采购总监）** | `kpontbriand@mjelectric.com`（**A 档具名**）| **已验证**（SMTP RCPT 实测 250：控制地址 `info@` 250 + 随机地址 550 + 对照组 550；**同域 `tnagy@`（CEO Tom Nagy）亦 250 ⇒ 命名规则 `{f}{last}@` 规则级确认**；LinkedIn 现职「Director of Purchasing at MJ Electric」）| 公司 LinkedIn `linkedin.com/company/mj-electric`；个人页 `linkedin.com/in/kory-pontbriand-67553040` | 密歇根 Iron Mountain 的多专业电气总承包商（60 余年）；业务含 transmission / substation / distribution / renewable / power / industrial / instrumentation / civil-foundation；**Quanta Services 旗下**；全美 20+ 区域与部门办公室 | 官网 home / leadership / contact-us / services 实抓 + LinkedIn 个人页 + jooble 招聘信息 + DNS(MX/SPF) 与 SMTP 实测 | ⚠️ **大型集团（Quanta）成员公司，采购权可能上移**；正文不引用人数/营收
```

## 二、补充信息（扩展段）

### 标准字段明细
- 国家+城市：**美国 Michigan**（Iron Mountain，Upper Peninsula，总部）
- 详细地址：**200 West Frank Pipp Drive, PO Box 686, Iron Mountain, MI 49801-1419**（Corporate Office，官网 contact 页明文）
- 电话：**906.774.8000**（Corporate Office）；另有 20+ 区域/部门办公室直线（Midwest 630.613.3476、Eastern 610.562.7570 等）
- LinkedIn：公司页 `linkedin.com/company/mj-electric`；个人页 `linkedin.com/in/kory-pontbriand-67553040`
- 网站：**www.mjelectric.com**（邮箱域 = 官网域 `mjelectric.com` ✅ 一致）
- 成立日：官网称「For more than six decades」（**>60 年**）→ 具体年份未获取
- 规模：未获取（**不可引用**）
- 法人主体：**M. J. Electric, LLC**；**母公司 = Quanta Services, Inc.（NYSE:PWR）**（官网首页原文 "a Quanta Services company"）
- 执照：未获取

### 联系人（含 still_here 在职核验）
| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| **Kory Pontbriand（本次主送）** | **采购总监**（Director of Purchasing）| LinkedIn 现职 **Director of Purchasing at MJ Electric**；工作经历含 M. J. Electric, LLC | 未获取 | 未获取（无近期活跃证据）| **低**（LinkedIn 现职 + **SMTP 250 实测命中**双源）| `linkedin.com/in/kory-pontbriand-67553040` |
| Hunter Buechel, MBA | Purchasing Agent（采购专员）| LinkedIn 记 **Purchasing Agent at M.J. Electric** | 未获取 | 未获取 | 中（单一来源）| `linkedin.com/in/hunter-buechel-mba-3304a0250` |
| Tom Nagy | CEO | 官网 leadership 页明文 **Tom Nagy, CHIEF EXECUTIVE OFFICER** | 未获取 | 官网现行 | 低 | 官网 leadership 页 |

> 🔴 **一家只发 1 人**：主送 **Kory Pontbriand（Director of Purchasing）** —— 采购一把手，职能最对口，邮箱已 SMTP 实证。
> ⚠️ **同域多人（Hunter Buechel 等）= 排重对象，不另发**。
> ⚠️ 公司 leadership 页列有 21 位高管（Tom Nagy CEO / Paul Randby COO / Jennifer Zimmerman CFO 等），**均无公开邮箱**，不作主送。

### 邮箱分档（A/B/C）
- **A 档（具名决策人邮箱，已验证）**：✅ **`kpontbriand@mjelectric.com`**
  - 实证：`python3 邮箱验证.py mjelectric.com kory.pontbriand@mjelectric.com kpontbriand@mjelectric.com pontbriand@mjelectric.com`
    - 控制地址 `info@mjelectric.com` → **250**（本轮可信）
    - 随机地址 `zzz_nonexistent_probe_9987@` → **550**（非 catch-all）
    - 对照组 `john.smith@ / jane.doe@ / bob.jones@` → **全 550**
    - 候选 `kpontbriand@` → **250 命中**；`kory.pontbriand@` → 550；`pontbriand@` → 550
  - **规则级确认**（第二轮）：控制 `info@` 250 + 随机 550 + **`tnagy@mjelectric.com`（CEO Tom Nagy）→ 250** + `jzimmerman@` → 550
  - ⇒ 本域命名规则 = **`{first-initial}{last}@`**，且**两条独立命中**（CEO + 采购总监）互为印证
- **B 档**：官网未公布角色邮箱（contact 页只有地址与电话）→ **无 B 档**
- **主送路径**：**`kpontbriand@mjelectric.com`（A 档，可主送）**；并行电话 **906.774.8000** 转 Purchasing
- ⚠️ **H3/H5 说明**：邮箱为 **SMTP 控制地址法实测命中（技术实证）+ 规则级二次确认 + LinkedIn 具名现职**。**一手源**为官网 leadership 页确认其采购/管理层架构、官网 contact 页确认企业身份。

### 我为什么找他
- 官网首页明写其为 **"a multi-faceted ELECTRICAL CONTRACTOR"**，业务覆盖 **transmission / substation / distribution / renewable energy / power / industrial / instrumentation / civil-foundation** —— **以「采购设备 → 施工交付」为商业模式**，与我方「制造商直供」定位直接对口（**且非制造方**）。
- 官网 projects 板块列出 **"Beecher 345 kV Energized Line"、"Meyer Substation & Foundations"、"Heartland Divide Wind"** —— **变电站与输变电项目是其核心交付物**，**主变/配电变需求与其业务高度重合**。
- **Kory Pontbriand 的职能就是采购**（LinkedIn 明写 Director of Purchasing，所在地 Iron Mountain = 总部）—— **决策人即采购接口**；同司另有 Purchasing Agent 岗位，说明**采购职能成建制**。

### 买家类型 / 需求品类
- 买家类型：🔥 **B 电气总承包商（EPC / 施工）**（实测画像 B 型主力）
- 需求品类（带结论态）：
  - `三相液浸电力变（UL E541626，72–121 kV、750–110,000 kVA，可直供）` —— 其 345kV 线路 / 变电站业务对口，**主切口**
  - `三相液浸配电变 / 三相美变（UL E541627，45–5,000 kVA，可直供）` —— 其 distribution / substation 业务对口
  - `主变（产能可覆盖，UL 区间外，需人工确认）` —— 其业务上限高，**如涉 500kV 级须人工确认**
  - `单相柱上变（认证在办 E544629，条件切入）` —— 其 distribution 业务对口，**条件切入**
  - ⛔ 对美国客户**不谈干变**

### 电压·频率·认证要求
- 电压：官网项目含 **345 kV** 线路；业务覆盖 transmission / substation / distribution → **具体采购等级首轮问**
- 频率：**60 Hz**（美国，产品零改造适配）
- 认证：美国市场须 **UL**；我方持 **UL E541626 / E541627** 正式 CoC（**UL Product iQ 可核验编号**）——⛔ 不得写 `CSA Certified`
- ⚠️ **集团准入**：Quanta 有供应商准入门槛（安全/质量/EDI/账期），**须评估**（写入风险）

### 采购信号
- 官网 leadership 页**设独立采购管理层**（Director of Purchasing）+ 招聘 Purchasing Agent → **采购职能成建制且在招**
- **在招「Supply Chain / Procurement / Buyer / Purchaser」岗位**（Iron Mountain）→ **采购团队在扩张**
- 项目组合含 **345kV 线路 + Substation & Foundations** → 变电站设备持续需求
- 全美 **20+ 区域/部门办公室** → 采购体量大
- **Quanta Services 旗下**（NYSE:PWR）→ 采购量极大但**准入流程长**

### 可利用的钩子（按强度排序）
1. **其业务核心是 345kV 线路 + 变电站交付**（官网 projects 一手源）—— 产品对口度最高
2. **采购一把手 Kory Pontbriand 的职能就是采购**（LinkedIn + SMTP 实证）—— 决策人即入口
3. **采购团队在招人扩张**（jooble 招聘）—— 时机好
4. **全美 20+ 办公室、体量大** —— 长期供应角度
5. ⚠️ **Quanta 集团** → 若走集团路径，注意供应商准入与 BABA 类条款

### 开发信建议
- **收件人策略**：✅ **A 档主送 `kpontbriand@mjelectric.com`（Kory Pontbriand，采购总监）**，写个性化正文；电话 **906.774.8000** 并行跟进
- 🔴 **域名提醒**：邮箱域 = 官网域 = **`mjelectric.com`**；⚠️ **绝不可**误写为 `quantaservices.com`（母公司域）或 `mjx.com` / `mjd.com` 等子公司简称域
- 🔴 **话术红线**：**不引用人数/营收**；不写 `CSA Certified`；**首封不报交期/价格**
- **开场角度**：从其 **345kV 线路 / 变电站项目组合 + 采购团队扩张** 切入（写信 agent 决定措辞）
- **发送时段**：MI Iron Mountain **ET（东部时区）**，周二–周四当地上午 ≈ **北京时间 21:00–00:00**（夏令时期间）
- **送达配置**：MX = **Microsoft 365**（`mjelectric-com.mail.protection.outlook.com`）；SPF = `include:_u.mjelectric.com._spf.smart.ondmarc.com -all`（**硬失败 `-all`，较严格**；DMARC 托管于 OnDMARC）→ 注意首封退信监控
- **附件建议**：不带名录/供货记录；如需仅附 UL 证书号 + 容量区间

### ⚠️ 矛盾点与风险提示
- ⚠️ **大型集团成员公司降级**（照 `渠道状态清单.md` §三十）：**Quanta Services（NYSE:PWR）** 下辖 300+ 运营公司，**采购权可能上移集团/区域层**，且有**合格供应商准入门槛** → 冷邮件直接开单概率受限，**定为「长期培育型 / 集团采购敲门型」**；**但本司保留了独立的 Director of Purchasing 岗位**，说明**基层采购权仍在**，是本单相对乐观的依据。
- ⚠️ **`mjelectric.com` 与 `dashiell.com` A 记录同 IP**（`141.193.213.20/21`）→ 同属 Quanta 的站点托管（**非同一公司**，仅佐证集团归属）。
- ⚠️ **Kory Pontbriand 无近期活跃证据** → 任职时长未获取；但 **SMTP 250 命中 + LinkedIn 现职**双源支撑 still_here。
- ⚠️ **SPF 硬失败（`-all`）** → 送达较严格，注意首封退信监控。
- ⚠️ **员工数/营收未获取** → **正文不引用任何数字**。
- ⚠️ **SMTP 探测纪律**：本域共跑 **两轮**（均带控制地址），未继续重复，避免触发 M365 反制拉黑。

### 信息缺口清单（请勿编造）
- **采购的具体变压器 kV / kVA / 品牌 / 认证要求**：首轮问
- **Kory Pontbriand 在本司任职时长 / 最近活跃**：未获取
- **是否已固定变压器供应商 / 是否直接进口**：未获取
- **公司员工数 / 营收**：未获取（**不可引用具体数字**）
- **B 档角色邮箱（`info@` 等）**：官网未公布，**未获取**（注：`info@mjelectric.com` 经 SMTP 实测 **250 存在**，但**未见于官网明文**，仅作控制地址使用，**不作交付**）
- **公司成立确切年份**：仅知「>60 年」
- **Quanta 集团供应商准入的具体要求（BABA / 安全审计 / EDI）**：未获取
- **主变/500kV 级需求**：其项目含 345kV，**上限未获取**

### 一句话画像
密歇根 Iron Mountain 一家 **60 余年的多专业电气总承包商**（**Quanta Services 旗下**，全美 20+ 办公室，核心交付含 345kV 线路与变电站）；**采购一把手 Kory Pontbriand（Director of Purchasing）具名邮箱 `kpontbriand@mjelectric.com` 经 SMTP 控制地址法实测命中，且同域 CEO 邮箱亦命中 ⇒ 命名规则 `{f}{last}@` 规则级确认（A 档，可主送）** —— 是 B 型 EPC 客户中采购入口最清晰的一家。

### 渠道覆盖清单（L-1、L0–L7）
| 层 | 结果 | 一句话 |
|---|---|---|
| L-1 锁人 | ✅ | LinkedIn 命中 **Kory Pontbriand（Director of Purchasing）**；官网 leadership 页列 21 位高管（无邮箱）|
| L0 官网 | ⚠️ | home / leadership / contact-us / services 全抓；**官网无任何明文邮箱**（仅地址 + 电话）|
| L1 政府一手 | ⚠️ | 未查联邦/州登记库（Quanta 集团主体，POC 不公开）|
| L2 命名+DNS | ✅ | 命名规则实测 = **`{f}{last}@`**（**双点命中：CEO `tnagy@` + 采购总监 `kpontbriand@`**）；MX=M365；SPF `-all` |
| L3 B2B 库 | ⚠️ | 未依赖 B2B 库（本项目 A 档来自 SMTP 实证）|
| L4 社媒协会 | ✅ | LinkedIn 个人页现职（Kory Pontbriand）；公司页有 |
| L5 黄页同址 | ⚠️ | 官网 contact 页已给全 20+ 办公室地址 |
| L6 电话表单 | ✅ | 906.774.8000（Corporate）+ 各区域直线（未拨打）|
| L7 付费 | ❌ | 未启用 |

### 同名排除表
| 同名 | 地点 | 排除理由 |
|---|---|---|
| **MJ Drilling / MJ Excavating / MJ Civil / MJ Industrial / MJ West / MJ East**（mjd / mjx / pci 等子品牌）| 全美 | **同集团内部部门/子公司**（官网 leadership 页列其 President），**非独立客户**，不另发 |
| Quanta Services 其他运营公司 | 全美 | **同集团**（含买家 288 Dashiell），**非本单客户** |
| 其他含 "MJ Electric" / "M.J. Electric" 的实体 | — | 须按 **`mjelectric.com` + Iron Mountain, MI + Quanta** 锁定 |
| "MJ Electric"（其他州同名小型电气承包商）| — | 🔴 通用名，**必须按州/域锁主体**，勿按公司名取域 |
