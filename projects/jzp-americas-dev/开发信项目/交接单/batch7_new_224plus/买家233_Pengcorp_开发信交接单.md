# 【买家 233】开发信交接单 — Pengcorp Ltd.（Pengcorp Engineering）

> 采集日期：2026-09-30 ｜ 来源：batch7 名单（pengcorp.ca，AB Calgary）｜ 一句话结论：**卡尔加里的工业技术/电气工程服务公司，设有独立「Electrical & Substations」事业部，官网明列对变电站的「design, maintenance, inspection, and procurement services」，能力清单含 Power Transformers 与 Procurement & Purchasing；官网公布角色邮箱 `inquiries@pengcorp.ca`（一手源）= B 档 → 点名转交 Director Fernando Rangel。**
> ⚠️ 本表严格区分「已验证」与「未获取」；未找到的信息一律标注，不做推断填充。
> ⚠️ **本单为 B 档**：主送走角色邮箱 `inquiries@pengcorp.ca` + 点名转交；具名直邮仅有第三方库来源（**待验证，不作主送**）。

## 闸门（留痕）

- 发信资格：✅ **通过**（B 档角色邮箱 → 点名转交 Fernando Rangel）
- 邮箱档位：**B（角色邮箱 → 点名转交）**
- 排重：与 `clients/`、`交接单/batch1–6`、`发信队列.json`、`发送日志.csv`、`退信黑名单.json`、`永久排除名录.md` 逐条比对 → **0 命中** ✅

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示
Pengcorp Ltd.（Pengcorp Engineering）| Fernando Rangel | Director, Industrial Operations Services（LinkedIn 现任 + Wiza + RocketReach 多源）| `inquiries@pengcorp.ca`（**B 档角色邮箱，官网一手源**）| **已验证（官网一手源明文；格式校验通过）** | 公司 LinkedIn `linkedin.com/company/pengcorp-ltd`；Facebook `facebook.com/pengcorpltd`（未直取）| 卡尔加里工业技术/电气工程服务公司；设 Electrical & Substations 事业部（T&D / 变电站 / 地下电缆 / 矿山电缆），官网明列变电站 design/maintenance/inspection/**procurement**，能力含 **Power Transformers** 与 **Procurement & Purchasing**；另设自动化、OT 网络安全、数据可视化、人力解决方案 | 官网 home/about-us/services 与 electrical-substations 子页实抓 + LinkedIn（Fernando Rangel）+ Wiza/RocketReach + DNS(MX/SPF) 实测 | ⚠️ 业务面宽（含人力/IT）→ 话术应聚焦**变电站/变压器**；**具名直邮仅第三方库来源（待验证）**；员工数为第三方口径（不引用）
```

## 二、补充信息（扩展段）

### 标准字段明细
- 国家+城市：**加拿大 Alberta**，Calgary
- 详细地址：**8th Floor Unit 835, 401 9 Ave SW, Calgary, AB T2P 3C5**（官网页脚）
- 电话：**+1 (844) 570-7364**（官网页脚）
- LinkedIn：公司页 `linkedin.com/company/pengcorp-ltd` ✅（未直取）
- 网站：**www.pengcorp.ca**（**邮箱域 = 官网域 pengcorp.ca**，MX = **Microsoft 365** `pengcorp-ca.mail.protection.outlook.com`）
- 成立日：🔴 **未获取**（官网/about 未给年份）
- 规模：⚠️ 第三方记 ~24 人（SignalHire 口径，未证实）→ **不引用人数**
- 法人主体：Pengcorp Ltd.
- 业务定位：**工业技术集成 + 工程咨询服务**（含独立 Electrical & Substations 事业部）

### 联系人（含 still_here 在职核验）
| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| **Fernando Rangel（主送对象）** | Director, Industrial Operations Services | LinkedIn "Director, Industrial Operations Services at Pengcorp" + Wiza "Fernando works at Pengcorp Ltd. as Director" + RocketReach "Director of Operations at Pengcorp Ltd." | 未获取 | LinkedIn 现任（未取到最近日期）| **中**（多源一致，但均为第三方库/社媒，非官网一手源）| `ca.linkedin.com/in/fernando-rangel-36781232`（⚠️ 另有一同名页 `-488807131`，须按 Calgary+Pengcorp 锁定）|

> 🔴 **一家只发 1 人**：主送对象 = **Fernando Rangel（Director, Industrial Operations Services）**。
> ⚠️ **同名风险**：LinkedIn 上存在两个 "Fernando Rangel" 页（`-36781232` 与 `-488807131`）→ **须按 Calgary + Pengcorp 锁定**，勿混。

### 邮箱分档（A/B/C）
- **B 档（角色邮箱，官网一手源）**：✅ **`inquiries@pengcorp.ca`**（官网页脚明文）
- **A 档候选（具名，第三方库）**：`fernando@pengcorp.ca`（**来源为 ContactOut 等 B2B 库，非官网一手源 → 待验证，不作主送**）
- **主送路径**：**`inquiries@pengcorp.ca`（B 档）**，正文首句**请求转交 Fernando Rangel（Director, Industrial Operations Services）**
- ⚠️ **H3/H5 说明**：主送邮箱来自**官网一手源**（满足 H5）。具名 `fernando@` 仅第三方库来源，**未获一手源印证 → 标"待验证"，不主送**。
- 🔴 **SMTP 不可用**：本机 25 端口整体不可用 → 未能做 RCPT 复核，**以官网一手源为准**。

### 我为什么找他
- 官网 **Electrical Substations 子页逐字写明** "Pengcorp provides high-level expertise in **design, maintenance, inspection, and procurement services for electrical substations**"，且能力清单**明列 "Power Transformers" 与 "Procurement & Purchasing"** —— **一家把变压器写进能力清单、并明确做采购的变电站服务商，是配变/主变的直接相关方**。
- 官网 **Electrical & Substations** 事业部含 **Transmission & Distribution / Underground Cable / Mining Cable** —— **工业与矿业现场设备使用方**（阿尔伯塔矿业/油气场景）。
- 官网称其服务覆盖 **North and South America**，团队为 "consortium of highly dedicated and talented engineers" —— **跨区项目触达**（谈资角度，勿夸大）。

### 买家类型 / 需求品类
- 买家类型：🔥 **B 型（工业电气工程服务 / 变电站服务商，含采购职能）**——实测画像 B 型；⚠️ 业务面宽（含人力/IT），**话术聚焦变电站/变压器**
- 需求品类（带结论态）：
  - `三相液浸配电变 / 三相美变（UL E541627，45–5,000 kVA，可直供）` —— 其变电站/配电场景，最可能切口
  - `三相液浸电力变 / 主变（UL E541626，72–121 kV、750–110,000 kVA，可直供）` —— 变电站场景，条件试探
  - `单相柱上变（认证在办 E544629，条件切入）` —— **条件切入**
  - `干变（加拿大实体可谈，有 CSA 项目报告，需人工确认）` —— 备选，不首推
  - ⚠️ 客户在**加拿大**：干变按「加拿大可谈」处理；**绝不写 `CSA Certified`**

### 电压·频率·认证要求
- 电压：🔴 **未获取**（官网未给具体 kV）→ **正文不引用电压数字**，首轮问
- 频率：**60 Hz**（加拿大，产品零改造适配）
- 认证：加拿大市场按 **CSA / IEEE / IEC 标准**；我方持 **UL E541626** 与 **E541627** 正式 CoC —— ⛔ **不得写 `CSA Certified`**，只可写 `built to CSA/IEEE/IEC standards`

### 采购信号
- 官网明列变电站 **"procurement services"** + 能力清单含 **"Procurement & Purchasing"** → **有采购职能**
- 能力清单**明列 "Power Transformers"** → **变压器直接相关**
- 业务含 **T&D / 地下电缆 / 矿山电缆** → 工业/矿业现场设备使用方
- **Microsoft 365 邮箱** → 企业级 IT

### 可利用的钩子（按强度排序）
1. **官网明列 Power Transformers + 变电站 procurement**（官网一手源）—— 最对口的身份角度
2. **Electrical & Substations 独立事业部（T&D/地下/矿山电缆）** —— 工业/矿业现场角度
3. **服务覆盖南北美** —— 跨区触达角度
4. **Microsoft 365 企业邮箱** —— 企业级对接角度

### 开发信建议
- **收件人策略**：**B 档 → 主送 `inquiries@pengcorp.ca`**，正文首句**请求转交 Fernando Rangel（Director, Industrial Operations Services）**；电话 **+1 (844) 570-7364** 并行跟进
- 🔴 **话术红线**：**不引用人数**（第三方口径）；**不引用电压数字**；**不提成立年份**（未获取）；业务面宽 → **聚焦变电站/变压器**，勿泛谈
- **开场角度**：从其 **变电站 procurement + 能力清单含 Power Transformers** 切入（写信 agent 决定措辞）
- **发送时段**：AB = **MT（山地时区）**，周二–周四当地上午 ≈ **北京时间 22:00–01:00**（夏令时期间）
- **送达配置**：MX = **Microsoft 365**；SPF 齐备；发信域须 SPF/DKIM/DMARC 齐备
- **附件建议**：不带名录/供货记录；如需仅附 UL 证书号 + 容量区间

### ⚠️ 矛盾点与风险提示
- ⚠️ **具名邮箱仅第三方库来源**（`fernando@pengcorp.ca` 来自 ContactOut 等）→ **待验证，不作主送**；主送走角色邮箱。
- ⚠️ **具名联系人职务为第三方口径**（LinkedIn/Wiza/RocketReach）→ 正文称 "Fernando" 即可，**不擅称 CEO/President**。
- ⚠️ **同名风险**：LinkedIn 两个 "Fernando Rangel" 页 → 须按 Calgary + Pengcorp 锁定。
- ⚠️ **成立年份未获取** → **正文不提年份**。
- ⚠️ **人数为第三方口径** → **正文不引用人数**。
- ⚠️ **业务面宽**（含人力/IT/数据）→ **话术必须聚焦变电站/变压器**，否则显得不了解其主业。
- ⚠️ **电压未获取** → 正文不引用电压数字。
- ⚠️ **RocketReach 将行业记为 "Automation Machinery Manufacturing"** —— 系第三方分类，**非制造商**，勿据此误判（⓪ 层已核实其官网为服务/工程）。

### 信息缺口清单（请勿编造）
- **Fernando Rangel 的任职时长 / 最近活跃日期**：未获取
- **具名决策人直邮**：**未取得一手源**（`fernando@` 仅第三方库，待验证）
- **公司创始人 / 总经理 / 成立年份**：未找到
- **电压等级 / 常用变压器容量 / 品牌**：未获取
- **员工数 / 营收**：未获取（**不可引用具体数字**）
- **阿尔伯塔省注册主体全称 / 执照**：未查
- **其采购是自用还是代客（EPC）**：未确认

### 一句话画像
卡尔加里一家**工业技术/电气工程服务公司**，设独立 Electrical & Substations 事业部，**官网明列变电站 design/maintenance/inspection/procurement，能力清单含 Power Transformers 与 Procurement & Purchasing** —— **官网公布角色邮箱 `inquiries@pengcorp.ca`（一手源）= B 档，点名转交 Director Fernando Rangel**；⚠️ 具名直邮仅第三方库来源（待验证），业务面宽需聚焦变电站/变压器。

### 渠道覆盖清单（L-1、L0–L7）
| 层 | 结果 | 一句话 |
|---|---|---|
| L-1 锁人 | ⚠️ | 第三方多源锁定 Fernando Rangel（Director）；**官网无具名** |
| L0 官网 | ✅ | home / about-us / services / electrical-substations 全抓；**角色邮箱 `inquiries@pengcorp.ca` 明文（一手源）** |
| L1 政府一手 | ⚠️ | 阿尔伯塔注册库未查；D&B 仅作旁证 |
| L2 命名+DNS | ⚠️ | MX = Microsoft 365；SPF 齐备；**具名推演未采信**；SMTP 本机不可用 |
| L3 B2B 库 | ⚠️ | ContactOut / Wiza / RocketReach 提供具名线索（**仅作旁证，未作主送**）|
| L4 社媒协会 | ⚠️ | 公司 LinkedIn/Facebook 命中未直取；Fernando 个人页存在（同名两页）|
| L5 黄页同址 | ⚠️ | Calgary 401 9 Ave SW 与 AllBiz 一致 |
| L6 电话表单 | ✅ | +1 (844) 570-7364 + 官网联系（未拨打/未提交）|
| L7 付费 | ❌ | 未启用 |

### 同名排除表
| 同名 | 地点 | 排除理由 |
|---|---|---|
| Pengcorp（其他同名）| — | 未发现同域名其他主体 |
| Fernando Rangel（两个 LinkedIn 页）| Calgary | 🔴 **疑同一人两页** → 须按 Calgary + Pengcorp 锁定，交人工判 |
| Peng Corp / Peng Engineering 类似名 | 多地 | 不同主体 |
