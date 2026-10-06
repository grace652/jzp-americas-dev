# 【买家 112】开发信交接单 — Alcan Electrical & Engineering, Inc.

> 采集日期：2026-09-23 / 来源：项目1候选输入（公司名+Anchorage地址+1971/200人/NECA-IBEW线索+官网电话）/ 已验证与未获取声明见各字段
> 一句话结论：阿拉斯加本土最大电气承包商之一（1971年，200+人，NECA/IBEW 1547，四城+北坡，Providence $50M/F-35实证），三位共主+估算师实名但直邮缺失，主送dispatch转交；偏大备选同意。

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示(如有)
Alcan Electrical & Engineering, Inc. | Chrys Fleming（主）/ Jesse Hale（备选）/ Scott Shafer（估算口） | President/Owner / VP/Owner / Estimator | 无直邮（B档：dispatch 907-563-3787+四城电话点名转交） | 未找到(A档) | 公司 linkedin.com/company/alcan-electrical-&-engineering-inc.；个人仅第三方快照（直链见缺口） | 美国AK Anchorage，1971年，200+人56白领$3730万，高压输电到弱电全包，Providence 15年$50M/F-35/北坡BP，NECA/IBEW 1547 | 官网全站(JSON-LD schema)+team页+AGC会员+LinkedIn公司页+DNS | 个人直邮缺失；规模三口径；DMARC quarantine；备选定级
```

## 二、补充信息（扩展段）

### 标准字段明细
- 国家+城市：美国 Alaska Anchorage（总部）+ Fairbanks + Juneau + Wasilla；北坡/阿留申全州
- 详细地址：6670 Arctic Spur Rd, Anchorage, AK 99518（JSON-LD+AGC+MapQuest+用户一致）；PO Box 91499 99509
- 电话：Anchorage dispatch 907-563-3787；Fairbanks 907-452-1771；Juneau 907-780-4404；Wasilla 907-357-6088（schema四城）；工时M–F 7:30–16:30
- LinkedIn：公司 linkedin.com/company/alcan-electrical-&-engineering-inc.（389粉，56人+9.8%，$3730万，1971/1972两口径）
- 网站：alcanelectric.com（2023–2026持续更新；Commercial Electrical high-voltage/design & engineering明文；System Integration/Milestone视频/Corning布线）
- 成立：1971（官网+schema+MapQuest；LinkedIn 1972单源，注差）
- 员工：200+（官网；56 LinkedIn白领；聚合20–30旧口径废弃）；2008营收$5050万（vLex存档）
- 身份：NECA + IBEW Local 1547；AGC Alaska会员（Chrys/Jesse/Mary/Naomi四联系人）；AlcanTel电信（90年代初）；Procore 2023入驻（101–500档）

### 联系人（含 still_here 在职核验）
| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| Chrys Fleming | President/Owner，终身Alcan（主送点名） | President | 2020至今President（终身在职，IBEW→估算→收购） | 高：team页+AGC Primary+快照Current | 低 | exa.ai/library/person/p968lwwd05x（快照；直链见缺口） |
| Jesse Hale | VP/Owner（备选） | VP | 2020至今（IBEW→$15M项目） | 高：team页+AGC+快照 | 低 | exa.ai/library/person/z6b1k7f04yb |
| Sage Bringmann | CAO/Owner（家族传承） | CAO | 收购三人组 | 中：team页+AGC Naomi Sage | 低，不作首收件 | team页 |
| Scott Shafer | Estimator，估算口 | Estimator | 现任 | 中：team页 | 低 | team页 |
| Scott Bringmann | Director（上一代家族） | Director | 老 | 中：LinkedIn高管 | 低，不作首收件 | LinkedIn |
| Mary Hansen | AGC联系人（行政口） | — | 现任 | 中 | 低，不作首收件 | AGC |

### 邮箱分档（A/B/C）
- **A档（具名）**：无（Chrys/Jesse/Scott直邮零公开；team页无邮箱）
- **B档（电话点名转交）**：dispatch 907-563-3787 + 四城分机（官网schema一手）→ 点名Chrys Fleming / Scott Shafer；AGC Send Email表单备选
- H6声明：仅电话入口；升级三步：①职能邮箱无；②无回信样本；③无样本停推演。如实记录。

### 我为什么找他
- 用户给的5项（1971/200+/NECA-IBEW/地址电话/偏大备选）全部命中：1971三源+200+官网原话+NECA/IBEW 1547原话+地址电话schema逐字一致；高压backbone明文（Commercial Electrical high-voltage）+MapQuest“low-voltage to high-voltage transmission”——是AK州配电+弱电基本盘（Providence 82,000尺Tower M/F-35 16机库/北坡BP控制），同意备选（Megawatt/Fullford/Intel/Leading Edge之后第五家AK）。

### 买家类型 / 需求品类
- 买家类型：**商工集成大承包商（强电+弱电+安防一站式，医疗/航空/军工/北坡）**
- 需求品类（带结论态）：
  - `干变（美国项目按业主规范，条件谈）` — 医院/机库/学校配电备选
  - `三相美变（UL E541627，仅条件提）` — 偏远站点顺带，物流贵
  - `开关柜（按项目，switchgear图实证）` — 配电房问法
  - 总判：备选，首封问其高低压常用容量（transmission线只见一句话，首轮核实）

### 电压·频率·认证要求
- 电压：未定位现役kV（transmission一句话+switchgear图；F-35机库480V级推测不写入信；首轮问）
- 频率：60Hz（美国）
- 认证：NECA/IBEW施工侧；BICSI/Corning弱电；产品侧亮UL号

### 采购信号
- $24M单项目能力（Chrys）+ $15M（Jesse）→ 大单备货
- Providence 15年$50M复购 → 医疗基本盘稳
- 北坡BP/Schlumberger油服 → 工业配套
- 2023 Procore入驻 → 项目管理数字化（submittals好讲）

### 开发信建议
- 收件人：dispatch电话点名Chrys（终身Alcan家族共鸣）+ Scott（估算）；Jesse备选
- 开场：1971本土+Providence $50M+F-35+北坡，点名IBEW 1547/NECA
- 附件：不带名录；submittals目录
- 发送时段：Anchorage（AKT）周二–周四上午 = 北京时间次日0–2点
- 送达：M365专线+SPF `-all`硬+DMARC **quarantine** → 三件套须齐；纯文本+电话跟进

### ⚠️ 矛盾点与风险提示
- 规模：200+ vs 56 vs 20–30 → 200+全口径+56白领双注，旧口径废弃
- 成立：1971 vs 1972 → 用1971（三源）
- 高压能力：仅MapQuest一句话+commercial页high-voltage词 → 首封必核实（勿预设kV）
- 个人页直链×3未取（仅快照）；直邮零
- DMARC quarantine → 发件域自查

### 信息缺口清单（请勿编造）
- 个人直邮×4：未找到
- 个人LinkedIn直链：未取
- 现役高压kV/变压器容量：未获取（首轮问）

### 一句话画像
阿拉斯加本土电气一哥——54年三代人，医院机库北坡全接，200多号，找终身Alcan的Chrys谈配电。

### 渠道覆盖清单（L-1、L0–L7）
| 层 | 结果 | 一句话 |
|---|---|---|
| L-1 锁人 | ✅ | 总裁+副总+CAO+估算师全锁（team+AGC在职） |
| L0 官网 | ✅ | 四城电话+高低压业务+项目墙全取 |
| L1 政府一手 | ⚠️ | AGC会员四联系人；注册未查 |
| L2 命名+DNS | ✅ | M365+SPF硬+DMARC quarantine；无样本停推演 |
| L3 B2B库 | ⚠️ | 快照旁证 |
| L4 社媒协会 | ✅ | LinkedIn公司页+NECA/IBEW/Procore |
| L5 黄页同址 | ✅ | AGC/MapQuest/Procore交叉 |
| L6 电话表单 | ✅ | 四城电话（未拨打） |
| L7 付费 | ❌ | 未启用 |
