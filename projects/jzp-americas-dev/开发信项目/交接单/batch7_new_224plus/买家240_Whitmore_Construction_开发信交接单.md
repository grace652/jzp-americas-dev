# 【买家 240】开发信交接单 — Whitmore Construction

> 采集日期：2026-09-30 ｜ 来源：batch7 名单（whitmoreconstruction.net，TX）｜ 一句话结论：**德州（Dallas / Irving）一家私有的交钥匙公用事业施工承包商，官网明列 Line Services 含 "Comprehensive high voltage substation construction services" 与 transmission / distribution / storm restoration；官网公布角色邮箱 `info@whitmoreconstruction.net`（一手源）= B 档 → 点名转交 President Clarence Thomas。**
> ⚠️ 本表严格区分「已验证」与「未获取」；未找到的信息一律标注，不做推断填充。
> ⚠️ **本单为 B 档**：主送走角色邮箱 `info@whitmoreconstruction.net` + 点名转交；**未取得任何具名直邮**（官网无团队页、无具名邮箱）。

## 闸门（留痕）

- 发信资格：✅ **通过**（B 档角色邮箱 → 点名转交 Clarence Thomas）
- 邮箱档位：**B（角色邮箱 → 点名转交）**
- 排重：与 `clients/`、`交接单/batch1–6`、`发信队列.json`、`发送日志.csv`、`退信黑名单.json`、`永久排除名录.md`、`_dedup_keywords_v2.txt`、成交客户（16 家）逐条比对 → **0 命中** ✅

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示
Whitmore Construction | Clarence Thomas | President（LinkedIn 现任 + CIVCAST 登记联系人）| `info@whitmoreconstruction.net`（**B 档角色邮箱，官网一手源**）| **已验证（官网一手源明文；格式校验通过）** | 未找到（公司/个人页未获取；个人 LinkedIn 命中未直取）| 德州（Dallas / Irving）私有交钥匙公用事业施工承包商；业务含电信（FTTH）+ Line Services（transmission / **high voltage substation construction** / distribution / storm restoration / utility maintenance）；官网自述 "privately owned… established in Dallas, Texas" | 官网 home / about / contact-us / line-services 实抓 + LinkedIn（Clarence Thomas）+ CIVCAST 登记 + DNS(MX/SPF/DMARC) 实测 | ⚠️ **官网联系地址为虚拟信箱 suite（7750 N MacArthur Blvd STE 120-279）**，非实体厂区 → 正文勿暗示实地；**未取得具名直邮**；第三方规模/营收未采信
```

## 二、补充信息（扩展段）

### 标准字段明细
- 国家+城市：**美国 Texas**，Dallas（官网自述成立于 Dallas）；联系地址在 Irving
- 详细地址：**7750 N MacArthur Blvd STE 120-279, Irving, TX 75063**（官网 contact-us 页）——⚠️ **"STE 120-279" 形似虚拟信箱/邮件转寄 suite，非实体厂区**；另有第三方记 Cedar Hill, TX
- 电话：**972-293-4414**（官网）；CIVCAST 登记另记 **214-868-7039**
- LinkedIn：公司页未找到；个人页 `linkedin.com/in/clarence-thomas-1669022b6`（命中未直取）
- 网站：**whitmoreconstruction.net**（**邮箱域 = 官网域 whitmoreconstruction.net**；MX = **Microsoft 365** `whitmoreconstruction-net.mail.protection.outlook.com`；SPF `include:spf.protection.outlook.com -all`；**DMARC `p=reject; sp=reject`**）
- 成立日：🔴 **未获取**（官网仅称 "established in Dallas, Texas"，无年份）→ **正文不提年份**
- 规模：⚠️ 未获取（官网首页有 "Combined Years of Experience / Miles of FTTH Installed / EMR Rating" 数字位，**未取到具体值**）→ **不引用**
- 法人主体：**Whitmore Construction**（CIVCAST 登记为 **Whitmore Construction LLC**，General Contractor）
- 资质：官网自述 "compliant with all state regulations"；EMR 评级位存在（值未取到）

### 联系人（含 still_here 在职核验）
| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| **Clarence Thomas（本次主送对象）** | 公司负责人 | **LinkedIn 现任 "President at Whitmore Construction"**（Location: Irving）+ **CIVCAST 登记联系人 "CLARENCE THOMAS"** | 未获取 | LinkedIn 现任（未取到最近日期）| **中**（LinkedIn + CIVCAST 双源，但均非官网一手源）| `linkedin.com/in/clarence-thomas-1669022b6`（⚠️ 另有同名页 `clarence-ct-thomas-a8298a17`，须按 Irving + Whitmore 锁定）|

> 🔴 **一家只发 1 人**：主送对象 = **Clarence Thomas（President）**——LinkedIn + CIVCAST 双源。
> ⚠️ **同名风险**：LinkedIn 上存在两个 Clarence Thomas 相关页（`-1669022b6` 与 `-ct-thomas-a8298a17`）→ **须按 Irving + Whitmore Construction 锁定**，勿混（勿与最高法院同名人物混淆）。

### 邮箱分档（A/B/C）
- **B 档（角色邮箱，官网一手源）**：✅ **`info@whitmoreconstruction.net`**（官网 contact 页 + 首页页脚明文）
- **A 档（具名）**：❌ **未取得**（官网无团队页/具名邮箱；第三方库未取到可用具名地址）→ **禁推演**
- **主送路径**：**`info@whitmoreconstruction.net`（B 档）**，正文首句**请求转交 President Clarence Thomas**；电话 **972-293-4414** 并行
- ⚠️ **H3/H6 说明**：主送邮箱来自**官网一手源**（满足 H5）；**仅有角色邮箱，升级三步未获具名直邮** → **显式标风险**（§4.4）。
- 🔴 **SMTP 不可用**：`whitmoreconstruction.net` MX = Microsoft 365；本机 25 端口整体不可用 → 未能做 RCPT 复核，**以官网一手源为准**。

### 我为什么找他
- 官网 **Line Services 段逐字写明** "Whitmore Construction provides power line construction and electric utility services… including new construction, repairs, and maintenance for **distribution lines, transmission lines, and power substations**"，且 **Substation 子页称 "Comprehensive high voltage substation construction services"** —— **一家自述做「高压变电站建设」的线路承包商，是配变/主变的直接使用方**。
- 官网 **Storm Restoration** 段称 "**24/7 emergency electric utility repairs and storm response**" —— **应急更换需求（变压器更换高频场景）**。
- 官网自述为 **"turn-key contractor privately owned company, established in Dallas, Texas"** —— **私有、交钥匙 → 决策链较短，非层层转包**。

### 买家类型 / 需求品类
- 买家类型：🔥 **B 电气承包商（电力线路 / 变电站 EPC，私有，交钥匙）**——实测画像 B 型
- 需求品类（带结论态）：
  - `三相液浸电力变 / 主变（UL E541626，72–121 kV、750–110,000 kVA，可直供）` —— 其高压变电站建设主业对口，**首推方向**
  - `三相液浸配电变 / 三相美变（UL E541627，45–5,000 kVA，可直供）` —— 配电场景
  - `单相柱上变（认证在办 E544629，条件切入）` —— 配网场景，**条件切入**
  - `干变（美国不匹配：无 UL）` —— ❌ **不推**，**钩子绝不挂干变**
  - ⚠️ 客户在**美国**：60 Hz；认证须 **UL**

### 电压·频率·认证要求
- 电压：🔴 **未获取**（官网仅称 "high voltage substation"、"transmission lines"，未给 kV）→ **正文不引用电压数字**，首轮问
- 频率：**60 Hz**（美国，产品零改造适配）
- 认证：美国市场须 **UL**；我方持 **UL E541626** 与 **E541627** 正式 CoC —— 可写 `UL listed (E541627 / E541626)`；⛔ **不得写 `CSA Certified` / `SASO` / `SONCAP`**

### 采购信号
- 官网 Line Services 含 **high voltage substation construction + transmission + distribution + utility maintenance** → 变电站/线路设备更换场景
- 官网 **Storm Restoration**（24/7 应急）→ **变压器应急更换需求**
- **RDOF Partner / FTTH 交钥匙** → 有承接公用事业级大项目的能力与合规流程
- 私有交钥匙承包商 → **决策链较短**

### 可利用的钩子（按强度排序）
1. **官网自述 "Comprehensive high voltage substation construction services"**（一手源）—— 最对口的能力角度
2. **24/7 storm restoration / emergency utility repairs** —— 应急更换场景角度
3. **Turn-key + privately owned（Dallas 起家）** —— 决策链短角度
4. **RDOF Partner / FTTH 全国部署** —— 项目承接能力角度

### 开发信建议
- **收件人策略**：**B 档 → 主送 `info@whitmoreconstruction.net`**，正文首句**请求转交 President Clarence Thomas**；电话 **972-293-4414** 并行
- 🔴 **话术红线**：**联系地址为虚拟信箱 suite（非实体厂区）** → **正文勿暗示"到访厂区/实地考察"**；**不引用人数/营收/成立年份**
- **开场角度**：从其 **high voltage substation construction + storm restoration** 切入（写信 agent 决定措辞）
- **发送时段**：TX = **CT（中部时区）**，周二–周四当地上午 ≈ **北京时间 22:00–01:00**（夏令时期间）
- **送达配置**：MX = **Microsoft 365**；SPF `-all`；**DMARC `p=reject; sp=reject`（对方收信严格）**；发信域须 SPF/DKIM/DMARC 齐备
- **附件建议**：不带名录/供货记录；如需仅附 UL 证书号 + 容量区间

### ⚠️ 矛盾点与风险提示
- 🔴 **未取得具名直邮**：官网无团队页/具名邮箱 → **仅角色邮箱，按 §4.4 显式标风险**。
- ⚠️ **联系地址为虚拟信箱 suite**（`STE 120-279`）→ **正文勿暗示实地厂区**；另有第三方记 Cedar Hill, TX，地址口径不完全一致。
- ⚠️ **Clarence Thomas 职务仅第三方来源**（LinkedIn + CIVCAST，均非官网一手源）→ **称 "Clarence" 即可**；⚠️ 与最高法院同名人物**无任何关联**，勿联想。
- ⚠️ **成立年份未获取** → **正文不提年份**。
- ⚠️ **员工数 / 营收 / EMR 值**：未获取（**不可引用具体数字**）。
- ⚠️ **电压未获取** → 正文不引用电压数字。
- ⚠️ **公司 LinkedIn 未找到** → 无法做 LinkedIn 公司页侧核验。
- ⚠️ **DMARC `p=reject`** → 对方邮件系统严格；首封须确保我方 SPF/DKIM 对齐，否则易被拒。

### 信息缺口清单（请勿编造）
- **具名直邮（Clarence Thomas 个人邮箱）**：**未找到**（禁推演）
- Clarence Thomas 的**任职时长 / 最近活跃**：未获取
- **公司成立年份**：未获取（**不得引用**）
- **员工数 / 营收 / EMR 评级值**：未获取（**不可引用具体数字**）
- **电压等级 / 常用变压器容量 / 品牌**：未获取
- **TX TDLR / 州执照号**：未查
- **实体办公地址（vs 虚拟信箱 suite）**：**口径不一致，须核实**

### 一句话画像
德州（Dallas / Irving）一家私有交钥匙公用事业施工承包商（**官网明列 Line Services 含 "Comprehensive high voltage substation construction services" 与 transmission / distribution / storm restoration**）——**官网公布角色邮箱 `info@whitmoreconstruction.net`（一手源）= B 档，点名转交 President Clarence Thomas**；⚠️ 未取得具名直邮，且联系地址为虚拟信箱 suite（非实体厂区）。

### 渠道覆盖清单（L-1、L0–L7）
| 层 | 结果 | 一句话 |
|---|---|---|
| L-1 锁人 | ⚠️ | LinkedIn + CIVCAST 双源锁定 President Clarence Thomas；**均为第三方，非官网一手源** |
| L0 官网 | ✅ | home / about / contact-us / line-services 全抓；**角色邮箱 `info@whitmoreconstruction.net` 明文（B 档一手源）** |
| L1 政府一手 | ⚠️ | CIVCAST 登记（General Contractor 联系人 Clarence Thomas）；**TDLR 执照库未查** |
| L2 命名+DNS | ⚠️ | MX = Microsoft 365；SPF `-all`；**DMARC `p=reject`**；**具名推演未采信**；SMTP 本机不可用 |
| L3 B2B 库 | ⚠️ | aeroleads / contactout 命中，**未取到可用具名地址** |
| L4 社媒协会 | ⚠️ | 个人 LinkedIn 命中未直取；公司页未找到 |
| L5 黄页同址 | ⚠️ | Irving 虚拟信箱 suite；第三方另记 Cedar Hill |
| L6 电话表单 | ✅ | 972-293-4414 + 官网表单（未拨打/未提交）|
| L7 付费 | ❌ | 未启用 |

### 同名排除表
| 同名 | 地点 | 排除理由 |
|---|---|---|
| Whitmore Construction（其他州）| US | 无关联 |
| Whitmore Construction LLC（Cedar Hill, TX）| TX | **疑同一主体**（BuildZoom 记 Cedar Hill）→ 交人工判；投递以官网域 `whitmoreconstruction.net` 为准 |
| **Clarence Thomas**（最高法院大法官）| US | 🔴 **同名人物，无任何关联** → 勿联想 |
| Clarence 'CT' Thomas（LinkedIn `-a8298a17`）| — | **须按 Irving + Whitmore 锁定**，勿混 |
