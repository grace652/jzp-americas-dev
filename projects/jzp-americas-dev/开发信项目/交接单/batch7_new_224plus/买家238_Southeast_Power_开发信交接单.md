# 【买家 238】开发信交接单 — Southeast Power Corporation

> 采集日期：2026-09-30 ｜ 来源：batch7 名单（southeastpower.com，FL Titusville）｜ 一句话结论：**佛州 Titusville 的电力输配 / 变电站施工承包商，官网自述 "complete turnkey substation construction"、输电线路 46kV–500kV，为 PCA（Power Corporation of America）全资子公司（最终母公司 Goldfield Corp，NYSE: GV）；官网页脚公布角色邮箱 `info@southeastpower.com`（一手源）= B 档 → 点名转交 President Jason M. Spivey。**
> ⚠️ 本表严格区分「已验证」与「未获取」；未找到的信息一律标注，不做推断填充。
> ⚠️ **本单为 B 档**：主送走角色邮箱 `info@southeastpower.com` + 点名转交；具名直邮 `jspivey@` 为**推演（无一手源明文，不作主送）**。

## 闸门（留痕）

- 发信资格：✅ **通过**（B 档角色邮箱 → 点名转交 Jason M. Spivey）
- 邮箱档位：**B（角色邮箱 → 点名转交）**
- 排重：与 `clients/`、`交接单/batch1–6`、`发信队列.json`、`发送日志.csv`、`退信黑名单.json`、`永久排除名录.md`、`_dedup_keywords_v2.txt`、成交客户（16 家）逐条比对 → **0 命中** ✅

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示
Southeast Power Corporation | Jason M. Spivey | President（theorg 现任 org chart + 官网 about 提及 Mr. Spivey）| `info@southeastpower.com`（**B 档角色邮箱，官网页脚一手源**）| **已验证（官网一手源明文；格式校验通过）** | 公司 LinkedIn `linkedin.com/company/southeast-power-corporation`（未直取）| 佛州 Titusville 电力输配/变电站施工承包商；官网自述 "complete turnkey substation construction"；输电线路 46kV–500kV；为 PCA（Power Corporation of America）全资子公司；服务东南部+中大西洋+德州 | 官网 home/projects/contact-us 实抓 + theorg org chart + CAGE.report(SAM.gov/DLA 一手) + leadiq/contactout/rocketreach 邮箱格式 + DNS(MX/SPF) 实测 | ⚠️ 属**上市母公司 Goldfield Corp（NYSE: GV）旗下 PCA 子公司** → 决策链可能长、或集团集中采购；具名直邮 `jspivey@` 为**推演（不作主送）**；第三方员工数（160+）不引用
```

## 二、补充信息（扩展段）

### 标准字段明细
- 国家+城市：**美国 Florida**，Titusville（公司总部）；另有分公司 **Spartanburg, SC** 与 **Bastrop, TX**
- 详细地址：**1805 Hammock Rd, Titusville, FL 32796**（SAM.gov/CAGE 一手源 + 官网）
- 电话：**321-268-0540**（官网）；**321-724-1700**（CAGE/DLA 一手源）
- LinkedIn：公司页 `linkedin.com/company/southeast-power-corporation`（未直取）；个人页未找到
- 网站：**www.southeastpower.com**（**邮箱域 = 官网域 southeastpower.com**；MX = **Barracuda ESS** `d191196a/b.ess.barracudanetworks.com`；SPF `include:spf.protection.outlook.com include:spf.ess.barracudanetworks.com include:_spf.psm.knowbe4.com -all`；DMARC 未取到）
- 成立日：🔴 **口径冲突**（CAGE 记 established 1995-08-29；SAM legacy 记 business started 1950；SAM public 记 business started 1983）→ **正文不提年份**
- 规模：⚠️ 第三方口径 160–500 人（rocketreach 162；theorg 201–500）→ **不引用人数**
- 法人主体：**Southeast Power Corporation**；母公司 **PCA（Power Corporation of America）**；最终母公司 **Goldfield Corporation（NYSE: GV）**
- 资质：**SAM.gov 注册**（UEI `YQN2KJM54EC9`，CAGE `04AM7`，Active）；NAICS `237130` / `221121`

### 联系人（含 still_here 在职核验）
| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| **Jason M. Spivey（本次主送对象）** | 公司最高负责人 | theorg org chart 记 "President"；官网 about 页提及 "In 2015, Mr. Spivey joined Southeast Power Corporation, a wholly owned subsidiary of PCA, as a Project Manager" | **未获取**（据官网自述 2015 入职，任职约 10 年+）| 官网 about 现行（2026-09 抓取）+ theorg 现行 | **低**（官网 about 提及 + theorg 现任，双源）| 未找到 |
| Todd Davis | Vice President, Western Division | theorg org chart | 未获取 | 未获取 | **中**（单源第三方）| 未找到 |
| Brian Tilton / Jack Moore / Jeff Slaybaugh / John White / Tate Johnston | Vice President（多辖区）| theorg org chart | 未获取 | 未获取 | **中**（单源第三方）| 未找到 |

> 🔴 **一家只发 1 人**：主送对象 = **Jason M. Spivey（President）**——官网 about 提及 + theorg 现任双源。
> ⚠️ 其余 VP 均为**单源第三方（theorg）**，未确指 → **不据此另发**。

### 邮箱分档（A/B/C）
- **B 档（角色邮箱，官网一手源）**：✅ **`info@southeastpower.com`**（官网页脚明文）
- **A 档候选（推演，不作主送）**：`jspivey@southeastpower.com` —— 邮箱格式 `FLast@` / `[f][last]`（leadiq / rocketreach / contactout **三库一致**），但**无一手源明文** → **待验证，不作主送**
- **主送路径**：**`info@southeastpower.com`（B 档）**，正文首句**请求转交 Jason M. Spivey（President）**；电话 **321-268-0540** 并行
- ⚠️ **H3/H5 说明**：主送邮箱来自**官网一手源**（满足 H5）。具名 `jspivey@` 仅第三方库推演，**未获一手源印证 → 标"待验证"，不主送**。
- ⚠️ **另有一条一手源邮箱但不采用**：CAGE 记录公布 `swherry@goldfieldcorp.com`（NSPA NCAGE 一手源）—— 经核，**Stephen R. Wherry 为母公司 Goldfield Corp 的 CFO**（SEC 8-K），**非本主体对口人 → 不采用**。
- 🔴 **SMTP 不可用**：本机 25 端口整体不可用 → 未能做 RCPT 复核，**以官网一手源为准**。

### 我为什么找他
- 官网**首页逐字写明** "Southeast Power Corporation provides power utility companies with an effective electrical construction contractor"，且 "engaged in the **construction and maintenance of power transmission and distribution lines, substations**…"，并在 "Our Experience Includes" **明列 "Turnkey substation construction and maintenance"** 与 **"Power transmission line construction and maintenance ranging from 46kV to 500kV"** —— **一家自述做「交钥匙变电站建设」、输电做到 500kV 的承包商，是配变/主变的直接使用方与规格相关方**。
- 其**分公司覆盖 Titusville FL / Spartanburg SC / Bastrop TX**，服务东南部+中大西洋+德州 —— **多辖区持续作业，设备更换需求连续**。
- 官网**设 Careers 入口**（"continually looking for exceptional professionals to join our team"）→ **规模持续运营中，非萎缩**。

### 买家类型 / 需求品类
- 买家类型：🔥 **B 电气承包商（电力输配 / 变电站 EPC，中型，PCA 集团子公司）**——实测画像 B 型
- 需求品类（带结论态）：
  - `三相液浸电力变 / 主变（UL E541626，72–121 kV、750–110,000 kVA，可直供）` —— 其输电/变电站主业对口，**首推方向**
  - `三相液浸配电变 / 三相美变（UL E541627，45–5,000 kVA，可直供）` —— 配电场景，条件试探
  - `单相柱上变（认证在办 E544629，条件切入）` —— 配网场景，**条件切入**
  - `干变（美国不匹配：无 UL）` —— ❌ **不推**，**钩子绝不挂干变**
  - ⚠️ 客户在**美国**：60 Hz；认证须 **UL**

### 电压·频率·认证要求
- 电压：官网自述**输电 46kV–500kV、配电 <46kV**（一手源）→ **可引用该区间**，但**不引用具体项目容量**
- 频率：**60 Hz**（美国，产品零改造适配）
- 认证：美国市场须 **UL**；我方持 **UL E541626** 与 **E541627** 正式 CoC —— 可写 `UL listed (E541627 / E541626)`；⛔ **不得写 `CSA Certified` / `SASO` / `SONCAP`**

### 采购信号
- 官网自述 **"Turnkey substation construction"** → 含**设备采购 + 安装**职能
- **覆盖 FL / SC / TX 三辖区、多州作业** → 持续更换需求
- **SAM.gov 注册**（政府/公用事业客户）→ 有投标与合规采购流程

### 可利用的钩子（按强度排序）
1. **官网自述 "complete turnkey substation construction" + 输电 46kV–500kV**（一手源）—— 最对口的能力角度
2. **三辖区（FL / SC / TX）多州作业** —— 区域覆盖角度
3. **官网 Careers 持续招聘** —— 运营中角度
4. **SAM.gov 政府注册** —— 合规/公用事业客户角度

### 开发信建议
- **收件人策略**：**B 档 → 主送 `info@southeastpower.com`**，正文首句**请求转交 President Jason M. Spivey**；电话 **321-268-0540** 并行
- 🔴 **话术红线**：属**上市集团（Goldfield/PCA）子公司** → **不引用人数/营收/成立年份**；**不暗示集团层级关系**
- **开场角度**：从其 **turnkey substation construction + 46kV–500kV 输电区间** 切入（写信 agent 决定措辞）
- **发送时段**：FL Titusville = **ET（东部时区）**，周二–周四当地上午 ≈ **北京时间 21:00–00:00**（夏令时期间）
- **送达配置**：MX = **Barracuda ESS**；SPF `-all`（**硬拒绝，发信域须严格对齐 SPF/DKIM**）；DMARC 未取到
- **附件建议**：不带名录/供货记录；如需仅附 UL 证书号 + 容量区间

### ⚠️ 矛盾点与风险提示
- ⚠️ **具名直邮 `jspivey@` 为推演**（三库一致但无一手源明文）→ **不主送**，仅列 A 档候选。
- ⚠️ **成立年份口径冲突**（1950 / 1983 / 1995）→ **正文不提年份**。
- ⚠️ **第三方员工数（162 / 201–500）** → **不引用人数**。
- ⚠️ **集团背景**：Goldfield Corp（NYSE: GV）→ PCA → Southeast Power → **决策链可能长，采购或集中**；正文不臆测其采购权限。
- ⚠️ **CAGE 一手邮箱 `swherry@goldfieldcorp.com` 属母公司 CFO** → **非本主体对口人，不采用**（勿误发）。
- ⚠️ **名称易混**：**Southeast Power Technology（上海）** 为**制造商**，**不同主体** → 勿混（见排除表）。
- ⚠️ **DMARC 未取到** → 送达风险中等，注意首封退信监控。
- ⚠️ **个人 LinkedIn 未找到** → 无法做社媒侧 still_here 复核。

### 信息缺口清单（请勿编造）
- **Jason M. Spivey 的具名直邮**：未获取（`jspivey@` 为推演，**不得作主送**）
- Jason M. Spivey 的**个人 LinkedIn / 任职时长 / 最近活跃**：未获取
- **成立年份**：口径冲突，**不得引用**
- **员工数 / 营收**：未获取（**不可引用具体数字**）
- **常用变压器容量 / kV 等级 / 现有品牌**：未获取
- **采购决策链（是否集团集中采购）**：未获取
- **变压器采购对口人（采购 / 工程口）**：未获取

### 一句话画像
佛州 Titusville 一家电力输配 / 变电站施工承包商（**官网自述 "complete turnkey substation construction"、输电 46kV–500kV**，PCA 集团子公司，服务东南部+中大西洋+德州）——**官网页脚公布角色邮箱 `info@southeastpower.com`（一手源）= B 档，点名转交 President Jason M. Spivey**；⚠️ 属上市集团子公司，决策链可能长，且具名直邮仅有推演。

### 渠道覆盖清单（L-1、L0–L7）
| 层 | 结果 | 一句话 |
|---|---|---|
| L-1 锁人 | ✅ | theorg org chart 锁定 President Jason M. Spivey；官网 about 佐证 |
| L0 官网 | ✅ | home / projects / contact-us 全抓；**角色邮箱 `info@southeastpower.com` 明文（B 档一手源）** |
| L1 政府一手 | ✅ | **CAGE.report（SAM.gov/DLA）取 UEI/CAGE/地址/电话 + 公布邮箱**（母公司 CFO，不采用）|
| L2 命名+DNS | ⚠️ | MX = Barracuda ESS；SPF `-all`；**具名推演未采信**；SMTP 本机不可用 |
| L3 B2B 库 | ⚠️ | leadiq/contactout/rocketreach 邮箱格式三库一致（仅作推演佐证）|
| L4 社媒协会 | ⚠️ | 公司 LinkedIn 命中未直取；个人页未找到 |
| L5 黄页同址 | ⚠️ | Titusville 1805 Hammock Rd 见官网 + CAGE 一致 |
| L6 电话表单 | ✅ | 321-268-0540 + 官网表单（未拨打/未提交）|
| L7 付费 | ❌ | 未启用 |

### 同名排除表
| 同名 | 地点 | 排除理由 |
|---|---|---|
| **Southeast Power Technology Development Co., Ltd.**（southeastpowertech.com）| 上海 | 🔴 **电力设备制造商，不同主体**（中国厂商）→ 勿混 |
| Southeast Power Corp（其他州）| US | 无关联 |
| Goldfield Corporation（NYSE: GV）| US | **最终母公司**（非本主体；`swherry@goldfieldcorp.com` 为母公司 CFO）|
| PCA（Power Corporation of America）| US | **直接母公司**（非本主体）|
