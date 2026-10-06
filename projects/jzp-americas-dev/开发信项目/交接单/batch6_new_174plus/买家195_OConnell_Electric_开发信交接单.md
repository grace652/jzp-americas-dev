# 【买家 195】开发信交接单 — O'Connell Electric Company

> 采集日期：2026-09-29 / 来源：batch6 名单（第 22 行，CSV 州省 NY，核实无误）/ 一句话结论：**纽约上州的大型电气承包商（全国 Top50、1911 年创立、约 800 人）**，官网 Executive/Leadership 页公开完整团队，已锁到 **Manager, Procurement（Alex Miller）**；但邮箱域为 **catch-all**，具名邮箱无法验证 → **B 档（角色邮箱/电话点名转交）**。

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示(如有)
O'Connell Electric Company | Alex Miller | Manager, Procurement（采购经理，最对口） | 未找到具名直邮（域为 catch-all）；B 档：OCEHR@oconnellelectric.com / 电话 (585) 924-2176 点名转交 | 未找到（A 档）；B 档角色邮箱为官网明文 | linkedin.com/company/o'connell-electric-inc.（公司页）；个人页未确认（同名者多） | NY Victor，1911 创立，全国 Top50 电气承包商，约 800 人 / 营收约 $509M，施工+Utility（输配/变电站）+EPC+VDC | 官网 /company/ 团队页 + /careers/ + /contact/ + 新闻页 + DNS | 邮箱域 catch-all，禁止推演具名地址（H2/H6）；Proofpoint 网关
```

## 二、补充信息（扩展段）

### 标准字段明细
- 国家+城市：美国 New York，Victor（上州，罗切斯特都会区）
- 详细地址：830 Phillips Road, Victor, NY 14564（总部）；另 Schenectady 2360 Maxon Road Ext（518-346-0077）、Rochester、Buffalo（716-675-9010）
- 电话：总部 (585) 924-2176；Toll Free 1-800-343-2176
- LinkedIn：公司页 linkedin.com/company/o'connell-electric-inc.；**个人页未确认**（检索出现同名者属他司，见风险）
- 网站：oconnellelectric.com（MX=Proofpoint；A 记录 141.193.213.10/11；NS=AWS）
- 成立日：**1911**
- 规模：约 **800 人**（Kona Equity 估）；LeadIQ 记 201–500 人区间 → 取「数百人级」
- 营收：约 **$509.2M**（Kona Equity 估，2024-12）
- NAICS：**238210 Electrical Contractors and Other Wiring Installation Contractors**（incfact）
- 定位：官网自述「one of the largest electrical contractors in the nation」「one of the nation's top 50 largest electrical contractors」

### 联系人（含 still_here 在职核验）
| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| Alex Miller | **采购（最对口，本次主送）** | Manager, Procurement, O'Connell Electric | 未获取 | 中：官网 /company/ 团队页 2026-09-22 仍列其名（第一方） | 中（无个人页直证，仅公司页在列） | 未找到（检索命中的 Alex Miller@Procurement 属 Schuler-Haas，**非本司**，勿混） |
| Chris Thomas | 估价（Utility 线） | Chief Estimator, Utility Services | 未获取 | 中：官网团队页在列 | 中 | 未找到 |
| Matt McDonald | 估价（Construction 线） | Chief Estimator, Construction | 未获取 | 中：官网团队页在列 | 中 | 未找到 |
| Michael Parkes, PE | 最高层（备选，不作首收件） | Chief Executive Officer | 未获取（2026-07 仍以 CEO 身份出席 ELECTRI） | 高：2026-07/2025-12 新闻点名 CEO | 低 | 公司新闻页署名 |

> 🔴 一家只发 1 人：**主送 Alex Miller（Manager, Procurement）**——采购岗优先于 CEO。
> 备选（同一公司不重复发）：Chris Thomas（Utility 估价）/ Matt McDonald（Construction 估价）。

### 邮箱分档（A/B/C）
- **A 档（具名）**：**未找到** —— 官网 Contact 页只有表单与电话，无具名邮箱
- **B 档（角色，官网明文，first-party）**：`OCEHR@oconnellelectric.com`（Careers 页「合理便利申请」联系邮箱）—— 属 HR 职能，**用于销售点名转交不理想**，仅作兜底
- **主推路径（B 档）**：**电话 (585) 924-2176 / 官网 Contact 表单** → 点名转交 **Alex Miller, Manager, Procurement**
- 🔴 **H6 声明**：**仅取得角色邮箱（且为 HR 职能），未取得决策人直邮** —— 已跑「升级三步」：
  1. 挖职能邮箱：官网仅见 `OCEHR@`（HR），**未见** `Purchasing@`/`Supplier@`/`Estimating@` 类
  2. 从真实回信反推命名规则：无回信样本
  3. 免费试推演：**域为 catch-all，推演地址无法验证 → 依 §六 严格禁止使用非第一方来源地址，停止推演**
  → 结论：**本单只能走 B 档（电话/表单点名转交）**，已如实标注为风险。

> 🔴 **catch-all 判定证据**：控制地址 `info@oconnellelectric.com` = 250（但 catch-all 下无区分力）｜随机地址 `zzz_nonexistent_probe_9987@oconnellelectric.com` = **250** ⇒ **该域 catch-all，SMTP 探测永久无效**。`{first}.{last}@oconnellelectric.com` 的格式仅来自 ContactOut/RocketReach/Seamless 等 **B2B 库**（互证不算印证，H5），**且 catch-all 下无法证伪** ⇒ **不得作主送**。

### 我为什么找他
- 该公司官网 **Executive Team + Senior Leadership + Corporate Leadership 三张名单全公开**，而 Alex Miller 是**整份名单里唯一以「Procurement」为职能的人**——对一家「施工 + Utility（输配/变电站）+ EPC」的承包商而言，这正是**变压器这类设备采购的天然对接岗**，优先级高于 CEO。
- 公司业务含 **substation construction、transmission & distribution、EPC**（官网 Utility 与 EPC 服务页原句），即**变压器的直接使用/成套采购场景**，而非纯民用安装。

### 买家类型 / 需求品类
- 买家类型：🔥🔥 **B 电气承包商（大型，含 Utility 输配/变电站 + EPC）**——实测画像 B 型主力
- 需求品类（带结论态）：
  - `三相美变（UL E541627，45–5,000 kVA，可直供）` —— Utility 配电/变电站场景主谈
  - `主变 / 变电站变（UL E541626，750–110,000 kVA，可直供）` —— 其 substation construction / EPC 业务对口，项目制
  - `单相柱上变（认证在办 E544629，条件切入）` —— 配网线路，非首推
  - ⚠️ 美国客户：**不谈干变**（无 UL 不匹配）

### 电压·频率·认证要求
- 电压：未获取（其业务含 transmission & distribution + substation，典型中压 13.8/34.5/69 kV，**未证实**）
- 频率：**60 Hz**（美国）
- 认证：我方 UL **E541627 / E541626** 正式 CoC，适配美国

### 采购信号
- 官网公开 **Manager, Procurement** 岗位 → 有**常设采购职能**（非老板一人兼）
- 服务含 **EPC（Engineer, Procure, Construct）** → 明确含**采购环节**，是设备采购的天然入口
- 规模大（约 800 人 / 全国 Top50）+ 跨 Northeast/Mid-Atlantic/Mid-West/Southern → **项目制、批量采购潜力**
- 参与 **NECA / IBEW** 体系、获 NY State Empire Award（2026-05）→ 体系内正规承包商

### 可利用的钩子（按强度排序）
1. **EPC 服务线**（官网明列 "Engineer, Procure, Construct"）→ 采购是其业务的一环
2. **Utility 输配 + substation construction** 专线 → 主变/美变强相关
3. **1911 年创立、百年承包商**（官网 "over a century"）→ 稳健传承角度
4. **2026 年新闻密集**（ELECTRI 电网现代化圆桌、NY Empire Award、TEGG 奖）→ 时效性开场素材
5. 全国 Top50 / 约 800 人 → 规模背书

### 开发信建议
- **收件人策略**：**不要**盲发 `{first}.{last}@` 具名地址（catch-all，无法验证，触 H2/H6）；走 **B 档**——官网 Contact 表单或电话 (585) 924-2176，**点名转交 Alex Miller, Manager, Procurement**；正文首句明确请求转交
- **开场角度**：从其 **EPC / Utility 变电站**业务线与「常设采购职能」切入（写信 agent 决定措辞）
- **发送时段**：纽约 **ET**，周二–周四当地上午 = **北京时间 21:00–24:00**（夏令时期间）；美东夏令时 3–11 月
- **送达配置**：MX = **Proofpoint（pphosted）**；SPF 含 `_spf.salesforce.com`、`~all`；发信域须 SPF/DKIM/DMARC 齐备；**Proofpoint 可能对未授权来源不透露目录，勿反复探测**
- **附件建议**：不带名录/供货记录；如需仅附 UL 证书号 + 容量区间

### ⚠️ 矛盾点与风险提示
- 🔴 **邮箱域 catch-all**：`oconnellelectric.com` 对任意地址返回 250 ⇒ 具名邮箱**不可验证**；任何 `{first}.{last}@` 均为**未证实的推演**，**严禁作主送**（H2/H6）。
- 🔴 **同名陷阱**：检索「Alex Miller + Procurement」命中的是 **Schuler-Haas Electric Corp**（另一家 Rochester 承包商）的 Alex Miller，**与本司不是同一人**；本司 Alex Miller 的在职依据**仅官网 /company/ 团队页**（2026-09-22 在列）。→ 打电话时须口头确认「Manager, Procurement」这一岗。
- ⚠️ 规模口径不一：Kona Equity 约 800 人 / $509M vs LeadIQ 201–500 人 → 取「数百人级」，勿引用精确数字。
- ⚠️ 官网 Contact 页**无邮箱**，只有表单 + 电话 → 第一触达手段为电话/表单。
- ⚠️ 无个人 LinkedIn 直链 → 离职风险评为「中」，非「低」。

### 信息缺口清单（请勿编造）
- Alex Miller 的**具名邮箱**：未找到（域 catch-all，无法验证）
- Alex Miller 的**个人 LinkedIn 直链 / 任职时长**：未获取
- 公司**常用变压器容量 / 电压 / 品牌**：未获取
- 是否有 **`Purchasing@` / `Supplier@`** 等职能邮箱：未找到
- 公司**统一信用代码 / 注册主体全称**（NYSE 无关，NY 州注册）：未查
- **采购决策归属**（Alex Miller 是否单独拍板 vs 需上级）：未明

### 一句话画像
纽约上州百年、约 800 人的全国 Top50 电气承包商，EPC 与变电站专线俱全、且官网公开设「采购经理」岗——**对口度极高，但邮箱域 catch-all 挡住了具名直邮**，只能电话/表单点名转交 Alex Miller。

### 渠道覆盖清单（L-1、L0–L7）
| 层 | 结果 | 一句话 |
|---|---|---|
| L-1 锁人 | ✅ | 官网 Executive/Senior/Corporate 三张名单全取，锁定 Procurement 岗 Alex Miller |
| L0 官网 | ✅ | /company/ 团队页 + /contact/ + /careers/ 全取；Contact 页无邮箱 |
| L1 政府一手 | ⚠️ | 未查 NY 州注册；新闻页含官方颁奖（NY Empire Award）佐证 |
| L2 命名+DNS | ⚠️ | MX=Proofpoint；域 catch-all → 探测无效，禁止推演 |
| L3 B2B 库 | ⚠️ | ContactOut/RocketReach/Seamless 均给 {first}.{last} 格式（互证不算，H5） |
| L4 社媒协会 | ✅ | 公司 LinkedIn 页 + NECA/IBEW 体系提及 |
| L5 黄页同址 | ⚠️ | 多分支地址一致（Victor/Schenectady/Rochester/Buffalo） |
| L6 电话表单 | ✅ | 电话 (585) 924-2176 + 官网表单（未拨打/未提交） |
| L7 付费 | ❌ | 未启用 |
