# 【买家 242】开发信交接单 — RMS Energy Co., LLC

> 采集日期：2026-09-30 ｜ 来源：batch7 名单（rmsenergy.com，MN Little Falls）｜ 一句话结论：**明尼苏达 Little Falls 的全国性电力基础设施服务商（NETA 认证），官网自述 "one-stop resource for substation construction, maintenance, and upgrades"、"From bus systems to substations"；官网 About 公布完整高管团队（President & CEO Justin Johnson 等 16 人）；但官网仅设联系表单、**未公布任何对口角色邮箱**，具名邮箱仅有**推演** → ⛔ **按闸门第 1 条拦截（邮箱未验证）**，建议先电话/表单确认对口人。**
> ⚠️ 本表严格区分「已验证」与「未获取」；未找到的信息一律标注，不做推断填充。
> ⛔ **本单为拦截单**：主送邮箱未验证 → **不得直接发**；建议先电话 **+1 (320) …** 或官网表单确认采购/供应链对口人。

## 闸门（留痕）

- 发信资格：⛔ **拦截（第 1 条：具名邮箱未验证；仅有的角色邮箱 `careers@rmsenergy.com` 为招聘专用、非采购对口）**
- 邮箱档位：**C（需电话确认）** —— 唯一公开角色邮箱为招聘邮箱，**不可作销售主送**；具名 `jjohnson@` 为推演
- 排重：与 `clients/`、`交接单/batch1–6`、`发信队列.json`、`发送日志.csv`、`退信黑名单.json`、`永久排除名录.md`、`_dedup_keywords_v2.txt`、成交客户（16 家）逐条比对 → **0 命中** ✅
- 🔴 **拦截 ≠ 消失**：本家仍在线索池保留，标 `待补充`，待电话确认对口邮箱后再进写信环节。

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示
RMS Energy Co., LLC | Justin Johnson | President & CEO（官网 About 页明列）| ⛔ **未获取对口邮箱**（官网仅表单；唯一公开角色邮箱 `careers@rmsenergy.com` 为招聘专用；具名 `jjohnson@rmsenergy.com` 为**推演，待验证**）| **未找到（对口）** / `careers@rmsenergy.com` = 官网一手源但**招聘用途** | 公司 LinkedIn `linkedin.com/company/rms-energy`（命中未直取）；个人页未获取 | 明尼苏达 Little Falls 全国性电力基础设施服务商；NETA 认证；官网自述 "one-stop resource for substation construction, maintenance, and upgrades"、"From bus systems to substations"；设三大事业部（ERS 电气可靠性 / ESS 工程方案 / 设备方案）；服务 utility/industrial/renewables/data center/government | 官网 home / About / substation-solutions / contact / join-our-team 实抓 + LinkedIn（公司页）+ seamless/contactout 邮箱格式 + DNS(MX/SPF/DMARC) 实测 | ⚠️ **官网无对口角色邮箱** → 主送受阻；**具名推演不可主送**；第三方人数（352）不引用；⓪ 层需确认其 Equipment/Engineered Solutions 事业部**是否自制设备**（须排除竞品/贴牌可能）
```

## 二、补充信息（扩展段）

### 标准字段明细
- 国家+城市：**美国 Minnesota**，Little Falls（主办公室）；官网列 22+ 处网点（含 **Sacramento, CA 变压器场 / Transformer Yard**、Dallas TX、Memphis TN、Charlotte NC 等）
- 详细地址：**15396 183rd Street, Little Falls, MN 56345**（官网 + findglocal + MapQuest 一致）
- 电话：**未获取**（官网 contact 页仅表单，无公开电话）→ **须电话确认**（可用 D&B / 地图侧号码）
- LinkedIn：公司页 `linkedin.com/company/rms-energy`（命中未直取）；个人页未获取
- 网站：**rmsenergy.com**（**邮箱域 = 官网域 rmsenergy.com**；MX = **FireEye/Mimecast** `*.us.email.fireeyecloud.com`；SPF `include:spf.protection.outlook.com include:transmail.net include:_spf.intacct.com include:zcsend.net include:spf.smtp2go.com -all`；**DMARC `p=reject`，rua=mailto:nmurphy@rmsenergy.com**）
- 成立日：🔴 **未获取**（官网未给年份；About 页最早提及 "Justin Johnson joined RMS Energy in 2016"，非成立年）→ **正文不提年份**
- 规模：⚠️ 第三方记 352 人（ContactOut）/ 30 人（ContactOut 另一页）→ **口径悬殊，不引用人数**
- 法人主体：**RMS Energy Co., LLC**
- 资质：官网自述 **NETA accredited**（电力测试认证）

### 联系人（含 still_here 在职核验）
| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| **Justin Johnson（理论主送对象）** | 公司最高负责人 | **官网 About 页明列 "President & CEO"** | 未获取（官网自述 2016 加入 RMS）| 官网 About 现行（2026-09 抓取）| **低**（官网一手源明列）| 未找到 |
| Kyle Wattenbarger | President, Equipment Solutions（**设备事业部**，变压器相关）| 官网 About 页 | 未获取 | 未获取 | **中**（单源官网）| 未找到 |
| Brian O'Neil | President, Engineered Solutions（ESS）| 官网 About 页 | 未获取 | 未获取 | **中**（单源官网）| 未找到 |
| Ike Ratliff | President, Electrical Reliability Solutions（ERS）| 官网 About 页 | 未获取 | 未获取 | **中**（单源官网）| 未找到 |

> 🔴 **一家只发 1 人**：若邮箱可得，主送对象 = **Justin Johnson（President & CEO）**（官网一手源）。
> ⚠️ **但本单邮箱未验证 → 主送受阻**；且对变压器采购，**Kyle Wattenbarger（Equipment Solutions）或供应链口可能更对口** → 电话确认后再定主送对象。

### 邮箱分档（A/B/C）
- **A 档（具名）**：❌ **未取得**。`jjohnson@rmsenergy.com` 为**推演**（格式 `[f][last]`，seamless 记 86%；且 DNS DMARC 记录公布 `nmurphy@rmsenergy.com` 佐证该格式）→ **无一手源明文，不作主送**
- **B 档（角色邮箱）**：⚠️ **`careers@rmsenergy.com`**（官网 join-our-team 页一手源）——**但为招聘专用**，**非采购/销售对口** → **不宜作销售主送**
- **C 档（需电话确认）**：⛔ **本单适用** —— 官网仅表单、无对口角色邮箱 → **先电话确认对口人与其邮箱**
- **主送路径（待确认后启用）**：电话 + 官网 contact 表单（Inquiry Type 选 "Request for Quotes"）→ 请求转交 President & CEO 或 Equipment Solutions 负责人
- ⚠️ **H2/H4/H6 说明**：⛔ **绝不编造邮箱**；具名仅推演 → **不主送**；仅角色邮箱为招聘用途 → **按 §4.4 显式标风险**。
- 🔴 **SMTP 不可用**：`rmsenergy.com` MX = FireEye/Mimecast；本机 25 端口整体不可用 → 未能做 RCPT 复核。

### 我为什么找他
- 官网 **substation-solutions 页逐字写明** "RMS Energy is your **one-stop resource for substation construction, maintenance, and upgrades**. Our experienced crews are trained in all aspects of substation work"，且首页称 "**From bus systems to substations, we deliver end-to-end power solutions**" —— **一家做变电站建设/维护/升级、并含 bus systems 的服务商，是配变/主变的直接使用方与相关方**。
- 官网 About 页**设独立 "Equipment Solutions" 事业部（Kyle Wattenbarger 任 President）**，且网点含 **Sacramento, CA 的 Transformer Yard** —— **变压器是其设备事业部的核心资产类型**。
- 官网自述 **NETA accredited** + 服务 **utility / data center / renewables / government** 客户 —— **高门槛、合规导向的 B 端客户群**。

### 买家类型 / 需求品类
- 买家类型：🔥 **B 电气承包商 / 电力服务商（全国性，中型偏大，NETA 认证）**——实测画像 B 型
- ⚠️ **类型判定依据 + 第 ⓪ 层说明**：官网业务描述为 **services / construction / engineered solutions**（非 manufacturer）→ **非我方竞品**；**但其 "Engineered Solutions" 与 "Equipment Solutions" 事业部是否自制/贴牌设备，须电话确认排除**（若自制变压器则涉竞品，须剔除）。
- 需求品类（带结论态）：
  - `三相液浸电力变 / 主变（UL E541626，72–121 kV、750–110,000 kVA，可直供）` —— 其变电站主业对口，**首推方向**
  - `三相液浸配电变 / 三相美变（UL E541627，45–5,000 kVA，可直供）` —— 配电场景
  - `单相柱上变（认证在办 E544629，条件切入）` —— 配网场景，**条件切入**
  - `干变（美国不匹配：无 UL）` —— ❌ **不推**，**钩子绝不挂干变**
  - ⚠️ 客户在**美国**：60 Hz；认证须 **UL**

### 电压·频率·认证要求
- 电压：🔴 **未获取**（官网未给 kV）→ **正文不引用电压数字**，首轮问
- 频率：**60 Hz**（美国，产品零改造适配）
- 认证：美国市场须 **UL**；我方持 **UL E541626** 与 **E541627** 正式 CoC —— 可写 `UL listed (E541627 / E541626)`；⛔ **不得写 `CSA Certified` / `SASO` / `SONCAP`**

### 采购信号
- 官网自述 **substation construction / maintenance / upgrades** + **bus systems** → 变电站设备采购与更换场景
- 独立 **Equipment Solutions 事业部 + Sacramento Transformer Yard** → **变压器资产管理与采购职能明确**
- **NETA 认证 + 服务 utility / data center / government** → 合规采购流程、持续招标
- 22+ 网点、全国服务 → **多站点设备需求**

### 可利用的钩子（按强度排序）
1. **官网自述 "one-stop resource for substation construction, maintenance, and upgrades" + "From bus systems to substations"**（一手源）—— 最对口的能力角度
2. **独立 Equipment Solutions 事业部 + Sacramento Transformer Yard** —— 变压器资产角度
3. **NETA 认证 + utility/data center 客户群** —— 合规/高端客户角度
4. **22+ 网点全国服务** —— 规模与多站点角度
> ⚠️ **钩子强度受限于邮箱缺口**：**待电话确认对口人后再定钩子与主送**。

### 开发信建议
- **收件人策略**：⛔ **本单暂不可发** —— 邮箱未验证。**先电话/官网表单（Inquiry Type: Request for Quotes）确认采购或 Equipment Solutions 对口人及其邮箱**，再启用主送
- 🔴 **话术红线**：**不引用人数/营收/成立年份**；**不臆测其事业部自制设备的能力**（须先确认非竞品）
- **开场角度**：从其 **substation construction/maintenance + Equipment Solutions/Transformer Yard** 切入（写信 agent 决定措辞，**须待邮箱确认后**）
- **发送时段**：MN = **CT（中部时区）**，周二–周四当地上午 ≈ **北京时间 22:00–01:00**（夏令时期间）
- **送达配置**：MX = **FireEye/Mimecast**；SPF 多源 `-all`；**DMARC `p=reject`（对方收信严格）**；发信域须 SPF/DKIM/DMARC 齐备
- **附件建议**：不带名录/供货记录；如需仅附 UL 证书号 + 容量区间

### ⚠️ 矛盾点与风险提示
- ⛔ **邮箱未验证（主风险）**：官网无对口角色邮箱；具名 `jjohnson@` 为推演 → **按闸门第 1 条拦截**。
- ⚠️ **唯一公开角色邮箱为招聘用途**（`careers@rmsenergy.com`）→ **不宜作销售主送**。
- ⚠️ **第 ⓪ 层待确认**：**Engineered Solutions / Equipment Solutions 事业部是否自制/贴牌设备**（若自制变压器则涉竞品）→ **须电话确认**。
- ⚠️ **成立年份未获取** → **正文不提年份**。
- ⚠️ **人数口径悬殊**（352 vs 30，均第三方）→ **不引用人数**。
- ⚠️ **电压未获取** → 正文不引用电压数字。
- ⚠️ **公司电话未获取**（官网仅表单）→ 须从 D&B / 地图侧补号码。
- ⚠️ **DMARC `p=reject`** → 对方邮件系统严格；首封须确保我方 SPF/DKIM 对齐，否则易被拒。
- ⚠️ **名称易混**：`rms.energy`（菲律宾）、`rmsenergy.com.au`（澳洲）、`rmsie.com`（RMS 工程）→ **不同主体**（见排除表）。

### 信息缺口清单（请勿编造）
- **对口角色邮箱 / 具名直邮**：**未获取**（`jjohnson@` 为推演，**不得作主送**）
- Justin Johnson 的**个人 LinkedIn / 任职时长 / 最近活跃**：未获取
- **公司电话**：未获取（官网仅表单）
- **成立年份**：未获取（**不得引用**）
- **员工数 / 营收**：未获取（口径悬殊，**不可引用具体数字**）
- **电压等级 / 常用变压器容量 / 品牌**：未获取
- **其 Equipment/Engineered Solutions 事业部是否自制设备**：**待确认（涉 ⓪ 层竞品判定）**
- **采购 / 供应链对口人**：未获取

### 一句话画像
明尼苏达 Little Falls 一家全国性电力基础设施服务商（**官网自述 "one-stop resource for substation construction, maintenance, and upgrades"、NETA 认证、设独立 Equipment Solutions 事业部与 Sacramento 变压器场**）—— ⛔ **但官网无对口角色邮箱，具名仅推演 → 按闸门第 1 条拦截**；须先电话/表单确认采购或设备事业部对口人，再进写信环节。

### 渠道覆盖清单（L-1、L0–L7）
| 层 | 结果 | 一句话 |
|---|---|---|
| L-1 锁人 | ✅ | 官网 About 页公布完整高管团队，锁定 President & CEO Justin Johnson + Equipment Solutions 负责人 |
| L0 官网 | ⚠️ | home / About / substation-solutions / contact / join-our-team 全抓；**仅表单 + 招聘邮箱，无对口角色邮箱** |
| L1 政府一手 | ⚠️ | 未查（可查 MN 州务卿 / SAM.gov 补对口人）|
| L2 命名+DNS | ⚠️ | MX = FireEye/Mimecast；SPF 多源 `-all`；**DMARC `p=reject`，rua 佐证 `[f][last]` 格式**；**具名推演未采信**；SMTP 本机不可用 |
| L3 B2B 库 | ⚠️ | seamless/contactout 记邮箱格式与人数，**仅作旁证** |
| L4 社媒协会 | ⚠️ | 公司 LinkedIn 命中未直取；个人页未获取 |
| L5 黄页同址 | ⚠️ | Little Falls 15396 183rd St 见官网 + 地图一致 |
| L6 电话表单 | ⚠️ | 官网表单（Request for Quotes）+ **电话未获取**（未拨打/未提交）|
| L7 付费 | ❌ | 未启用 |

### 同名排除表
| 同名 | 地点 | 排除理由 |
|---|---|---|
| **RMS Energy**（rms.energy）| 菲律宾 Taguig | 🔴 **不同主体**（Utility Management）→ 勿混 |
| **RMS Energy**（rmsenergy.com.au）| 澳大利亚 | 🔴 **不同主体**（澳洲能源服务）→ 勿混 |
| **RMS**（rmsie.com）| US | 🔴 **不同主体**（RMS 工程，substations）→ 勿混 |
| RMS Energy Co., LLC（本家）| MN Little Falls | **同一主体**（本家）|
