# 【买家 3】开发信交接单 — ISCOCA Ltd. (Iscoca Electrical Services Limited)【2026-09-21 全量重查覆盖版】

> 采集日期：2026-09-21（全量重查，覆盖 2026-09-15 旧版）
> 重查原因：用户指定"很符合定位"，要求推倒重来、结果覆盖旧文件
> ⚠️ 本表严格区分「已验证」与「未获取」，未找到的信息一律标注，不做推断填充

---

## 0. 用户提供信息核验（本次新增）

| 用户提供的 | 核实结果 |
|---|---|
| 公司名 Iscoca Electrical Services Limited | ✅ 正确（官网页脚全称 `Iscoca Electrical Services Limited`，LinkedIn `ISCOCA Limited`，名录 `Iscoca Ltd.`，三名同一主体） |
| 地址 5004 Timberlea Blvd #14, Mississauga, ON L4W 2S6 | ✅ 正确（官网 Contact 页原文字 `5004 Timberlea Blvd #14 Mississauga, ON L4W 2S6 Canada`，与用户写法一字不差） |
| 官网 iscoca.ca / 电话 905-238-8700 | ✅ 全部正确（官网全站页眉/页脚统一为该电话，且为 24/7 应急线） |

---

## 标准字段

**公司全称**
ISCOCA Ltd.（商业用名 Iscoca Electrical Services Limited / ISCOCA Limited，三名同一主体，已交叉印证）

**国家 + 城市**
加拿大（Canada）+ 安大略省密西沙加市（Mississauga, Ontario）
办公地址：5004 Timberlea Blvd, Unit/Suite 14, Mississauga, ON（官网 Contact 页邮编 **L4W 2S6**；LinkedIn / YellowPages / ZoomInfo 登记邮编 **L4W 5C5**，见矛盾点章节，属同一地址不同写法）
服务范围：GTA（大多伦多地区）及安大略省全省；Procore 登记服务区另含 Markham / Toronto / Whitby / Ontario（单一来源，未经第二方印证）

**联系人 / 职位**

| 姓名 | 职位 | 来源与印证数 |
|---|---|---|
| **Selva Sathasevam** | President, Director of Technical Services（联合创始人，技术负责人） | 官网 About 页 + LinkedIn 个人页 + RocketReach，三源印证 ✅ |
| **Susan Selva** | Director of Operations（联合创始人，运营负责人） | 官网 About 页，单一来源 ⚠️（LinkedIn 上同名"MRT(T)/PMP"系多伦多医疗行业人士，**非本人**，已排除） |
| Keenan Pillai | Project Manager | 官网 About 页 + SignalHire，双源 ✅ |
| Nishadh Jasrotia | Materials and Operations Support Specialist（材料与运营支持，最接近采购职能） | 官网 About 页，单一来源 ⚠️ |
| Siva Sivanesan | Lead Project Control Specialist | 官网 About 页，单一来源 ⚠️ |
| Vikram Rai | Operations Coordinator | 官网 About 页 + ZoomInfo，双源 ✅ |
| Chrysanthus Perera | Field Service Technician | LinkedIn 公司页员工列表 + ZoomInfo + RocketReach，三源 ✅（本次新增） |
| Lisa Song | Operational Specialist | ZoomInfo 单一来源 ⚠️（本次新增，未经官网印证，不写入正文推荐收件人） |
| Jean Cote / Erin Troupe / Shivam Patel | 员工（职位未获取） | LinkedIn 公司页员工列表，单一来源 ⚠️ |
| Abdelkader Dib / Dhaval Badva / Mais Al-Doury | EIT现场工程师 / 电气技术员 / 实习生 | SignalHire / ZoomInfo，单一来源 ⚠️ |

- ⚠️ **独立采购职位：未获取**（官网领导团队无专职采购岗，Nishadh Jasrotia 的材料岗为最相关职能）
- 🆕 Selva 履历（RocketReach，单一来源）：Siemens 现场服务技术员 2001–2005 → Eaton Lead Field Service Engineer 2005–2011 → Iscoca 高级现场技术员 2011–2012 → 现场服务主管 2012–2024 → 技术服务总监 2024–今。西门子+Eaton 出身是强技术背书。

**邮箱**

| 邮箱 | 状态 | 来源 |
|---|---|---|
| `iscoca@iscoca.ca` | ✅ 已确认（主送首选） | Facebook 公司页简介 + YellowPages 描述 + Cylex 名录，三源一致 |
| `info@iscoca.ca` | ✅ 已确认（抄送） | **本次实测**：`Invoke-WebRequest` 抓首页 HTML 源码含该地址；旧版称"官网 HTML 出现"本次复现确认 |

- 关键人个人邮箱：**未获取** — 无任何已验证的个人邮箱（RocketReach 显示 Selva 有 1 个 `@iscoca.ca` 邮箱但掩码未公开全文，不可采用）
- 邮箱命名规则（两方口径，**互相矛盾，均未经投递验证**）：
  - Prospeo（本次重查）：`{firstname}.{lastname}` 75% + `{firstname}` 25%（如 selva.sathasevam@ / selva@）
  - ContactOut（旧版）：`{first_initial}{last}` 75%（如 ssathasevam@）
  - ⚠️ 两方规则冲突，且本次 Prospeo 口径与旧版 ContactOut 口径不一致，**任何推演地址均不可作主送，需先验证**
- ✅ **DNS 已验证（本次复测）**：MX `iscoca-ca.mail.protection.outlook.com`，SPF `v=spf1 include:spf.protection.outlook.com -all`，另有 `v=verifydomain MS=9773452` → 托管于 **Microsoft 365**，域名邮箱真实可收，无自建网关特征

**LinkedIn / 网站**
- 官网：https://iscoca.ca/（首页 / about-us / services / rental / projects / contact 全页本次重抓正常，无改版）
  - 设备租售：https://iscoca.ca/rental.html（本次确认为 `.html` 后缀版与无后缀版并存，内容一致）
  - 联系：https://iscoca.ca/contact.html（含询价表单，无明文邮箱）
- 公司 LinkedIn：https://www.linkedin.com/company/iscoca（本次重查显示 **53 followers**，旧版 56，量级一致；公司规模 11–50；可查看 14 名员工）
- 个人 LinkedIn：Selva Sathasevam https://ca.linkedin.com/in/selva-sathasevam-ba51aa66（Founder of Iscoca Power Systems；RocketReach 印证西门子/Eaton履历）
- Facebook：https://facebook.com/industrialelectricaliscoca（**202 followers**，简介含 `iscoca@iscoca.ca` + 双电话 + 地址）
- Instagram / Twitter / YouTube：**未找到**

**买家类型**
终端承包商（Terminal Contractor）— 工业/商业中高压电力工程服务商
- 双重身份：**既是服务承包商，也是设备租售商**（Equipment Rental & Sales 独立页）
- ESA 持牌电气承包商 + **ACP**（Authorized Contractor Program），**ECRA/ESA 牌照号 7007530**（官网全站页眉页脚统一标注）
- Procore 登记身份：Engineer + General Contractor，专长 Electrical / 高低压配电 / 发电（单一来源，佐证承包商属性）

**需求品类（区分"租"与"买"）**

官网 Equipment 页原文复核（本次逐字重抓，与旧版一致，无变更）：

**🔄 出租类（Rental，按项目周期）**
- **变压器**：油浸式与干式变压器 + **变压器油**
- **开关柜**：临时/应急租赁开关柜
- **临时电源与电缆**：临时交直流电源 + 高压电缆，现场敷设运行
- **电力监测仪**

**🛒 买断类（Purchase，可直接销售）**
- 编织连接线、负荷断路肘型接头、终端套件
- **高低压断路器**
- 母线（多种规格）
- **VFD 与软启动器**（服务页另有 Drive Support：多品牌 VFD 调试/故障诊断）
- 熔断器

**其他服务场景物资**：应急抢修（变压器/断路器/开关柜/配电盘/电缆/绝缘子套管维修更换）、发电机安装与临时部署、电缆与接地材料（35m 裸铜 4/0 接地线、接地端子连接器见 Niagara 项目）、600V 以上预防性维护、Doble/Hipot 测试、油分析与换油、红外扫描、电能质量分析（谐波/骤降/暂态）。

**触达来源**
1. 官网全站重抓（首页/about/services/rental/projects/contact + HTML 源码邮箱挖掘）
2. LinkedIn 公司页 + 个人页搜索摘要
3. Facebook 公司页简介
4. YellowPages 本地黄页（地址反查）
5. Procore 工程网络（本次新增：认领企业、规模、合同、活跃项目）
6. Indeed 雇主评价（本次新增：在营证据）
7. Prospeo / ZoomInfo / RocketReach / SignalHire / Tracxn（B2B 交叉，单源均标注）
8. NAPC / Oilmonster 行业名录
9. DNS 查询（MX / SPF，PowerShell 实测）

**我为什么找他（具体观察，1-2 句）**
这是一家 ESA 持牌（7007530）+ ACP 授权的中高压电力服务商，官网专设 Equipment Rental & Sales 页**公开列出可买断清单**（高低压断路器、母线、肘型接头、终端套件、VFD、熔断器），并自述"与安大略及全球供应商网络合作、按客户规格快速交付"；其变压器业务贯穿租售装修测全链条（出租油/干变、安装 2500/3125kVA 与 13.8kV–600V 变压器、27.6kV 变压器年维），与我方配电变压器主力产品直接对口，且 24/7 应急属性决定其对现货交期极度敏感。

**电压 / 频率 / 认证要求**
- **电压等级：已获取**：定位 "medium to high voltage"；预防性维护门槛 **600V 及以上**；项目实证 27.6kV、13.8kV–600V、2500/3125kVA；预防页 NETA 标准
- **频率：未获取**（公开渠道未提及；加拿大 60Hz 属行业常识，不得当该公司披露信息引用）
- **认证要求：部分获取**：公司自身 ESA 持牌 + ACP（7007530）✅；测试遵循 NETA ✅；**对其供应商产品的具体认证清单：未获取**

**采购信号（按强度排序）**
1. ✅ 官网公开"可买断"产品清单（最直接采购证据）
2. ✅ 自述全球供应商网络 + "access and deliver equipment quickly and to specifications"
3. ✅ 24/7 应急 + GTA 1 小时响应 + 设备 24/7 可用 = 现货交期敏感
4. ✅ 优质客户名单（约克大学/York、Bay-Adelaide Centre、Atlantic Packaging、Litens、Hatch、CBRE、Sunnybrook、多伦多大学、Sofina、Maple Lodge、New Forest，共 9+6 家）= 持续项目物资需求
5. 🆕 Procore：在营实证 — 2024-11 入驻，平均合同 <$10 万，累计 2 个项目、平均规模 $479 万，**当前 1 个活跃项目**（采购窗口信号）
6. 🆕 Indeed 2026-04 仍有新员工评价 = 在营
7. 海关提单：**未发现记录**（公开搜索无；承包商无规律进口，符合类型预期，不要硬拗）
8. 公开招标/中标、招聘采购岗、扩产公告：**未获取**

---

## 【补充信息】

### 1. 公司规模（多方对比）

| 来源 | 员工数 | 营收 | 备注 |
|---|---|---|---|
| LinkedIn 公司页 | 11–50（可查看 14 名员工） | — | 本次重查 |
| Tracxn | **16 人**（Official） | — | 最精确数字 |
| ContactOut（旧） | 15 人 | 估算 660 万美元 | 算法估算 |
| Prospeo | 11–20 | 估算 145 万美元 | 算法估算 |
| Procore | 10–50 | 平均合同 <$10 万 | 工程侧口径 |
| ZoomInfo | 11–50 | <$500 万 | 区间口径 |

**判断**：约 **15 人上下小型专业承包商**；营收均为算法估算（145 万 vs 660 万），**不可引用**。NAICS 口径冲突：ZoomInfo 23,238（建筑）vs Prospeo 3332（机械制造），均系 B2B 推断，未验证。

### 2. 客户与项目实证（官网 Projects 页，本次重抓 6 个全量）

| 客户 | 项目内容 |
|---|---|
| York University | 3 台 2MW 发电机 + 2500/3125kVA 变压器 + 13.8kV–600V 变压器 |
| Atlantic Packaging Whitby | 27.6kV 变压器年维 + 红外扫描 |
| Bay-Adelaide Centre | 年维 + 红外扫描 |
| Pelham | 4 台 1.4MW 发电机 |
| Niagara-on-the-Lake | 3 台 XQ2000 租赁机组 + 35m 裸铜 4/0 接地线 + 接地端子连接器 |
| Maple Lodge Farms | 变电站维护 |
| 首页客户墙 | Litens、Hatch、CBRE、Sunnybrook、多大、Atlantic、Sofina、Maple Lodge、New Forest |

### 3. 可利用的钩子（落点收在我方真有产品上）

① **可买断清单直切（最强）**：断路器/母线/肘型接头/终端套件/VFD/熔断器中我方能供哪几类就报哪几类。
② **变压器主钩子（最对口）**：对方变压器租售装修测全链条 + 变压器油；我方油浸配电变压器、干式变压器即主力，可谈"新变替换租赁老变、事故备用现货"。
③ **24/7 现货交期**：GTA 1 小时响应承诺 → 主打常备库存、紧急调配、多伦多周边交付时效。
④ **NETA + 600V 门槛**：报产品测试报告、出厂试验标准，用技术语言。
⑤ **Siemens/Eaton 出身创始人**：Selva 技术出身，对参数与工艺敏感，用工程师口吻而非营销话术。
⑥ ** grounding/电缆耗材**：Niagara 项目裸铜接地线、端子连接器是持续耗材，可搭单。

### 4. 开发信建议

- **主送 `iscoca@iscoca.ca`，抄送 `info@iscoca.ca`**（双已确认地址；推演个人邮箱一律备选且须先验证）
- 电话：**905-238-8700（24/7 总机，第一备用触达）**；647-501-4568 为旧应急号（FB+YP 仍载，官网已统一为 905 号，以官网为准）；416-450-8276（Procore 单一来源，未经印证，慎用，先核实）
- 官网询价表单 + LinkedIn Selva 私信为补充渠道
- 开场按优先级：①引用 Equipment 可买断清单 ②变压器+变压器油现货 ③24/7 紧急调配 ④NETA/测试报告 ⑤提及约克大学/Bay-Adelaide 案例表功课
- 时区：Mississauga 为加东 ET，夏令时与北京差 12h，建议北京时间 21:00–23:00 发送；对方 24/7 运营但商务邮件仍走工作时段
- 篇幅短、技术口吻；不要用"大集团"话术（对方 ~15 人）；**不要断言成立年份**（1983 单一来源 vs 35+ 年经验口径冲突，见下）

### 5. ⚠️ 矛盾点与风险提示

| # | 冲突 | 判定 |
|---|---|---|
| 1 | 邮编 L4W 2S6（官网）vs L4W 5C5（LinkedIn/YP/ZoomInfo） | 同一楼宇不同写法，**以官网 L4W 2S6 为准**寄样；下单前电话确认单元号 |
| 2 | 应急号 647-501-4568（FB+YP）vs 官网统一 905-238-8700 | 以新官网为准；旧号可能是转接/历史号，电话跟进时可顺带核实 |
| 3 | 邮箱格式 Prospeo（名.姓75%）vs ContactOut（首字母+姓75%） | 均未验证，**不可盲发个人邮箱** |
| 4 | 成立年份 Oilmonster"Since 1983/Est.1983" vs 官网"35+年经验"（2026-35=1991） | 1983 为单一来源，官网"35年"指团队经验非注册年限；**开发信不写成立年份** |
| 5 | 营收 145万 vs 660万；NAICS 23,238 vs 3332；员工 15 vs 16 | 均为 B2B 算法估算，**不引用** |
| 6 | Procore 电话 416-450-8276 全网仅此一处 | 单一来源，**发信前电话核实** |
| 7 | Susan Selva：LinkedIn 同名医疗人士 | 已排除非本人；运营总监无公开个人档案 |

### 6. 是否还在经营判定（7 判据）

官网 ©2026 + 全站可访问 ✅ / Procore 1 个活跃项目 ✅ / Indeed 2026-04 新评价 ✅ / YP 2026 版权页活跃 ✅ / 电话 MX/DNS 存活 ✅ / Tracxn 16 人在册 ✅ → **明确在营**，可投入。Indeed 负面评价（排班混乱、管理评价 1 星×3）属内部管理问题，**仅内部参考，绝不写入开发信**。

### 7. 信息缺口清单（请勿编造）

关键人个人邮箱 / 直拨电话 / 独立采购负责人 / 频率要求 / 产品认证清单 / 联邦注册号（查无，疑省注册）/ 具体采购量 / 现有供应商名单 / 公开招标 / 海关提单 / 采购岗招聘 — 以上**经多渠道核查确认无公开信息**。

### 8. 一句话画像

> 密西沙加约 15 人 ESA 持牌（7007530）+ ACP 中高压电力承包商，做 600V 以上设备 24/7 应急抢修、预防性维护（NETA）、工程研究与测试，服务约克大学、Bay-Adelaide 等；官网 Equipment 页公开可买断器材清单并出租变压器/开关柜，自述有全球供应商网络——是与我方配电变压器高度对口、且对现货交期极度敏感的明确采购方。

---

## 附：Waterfall L0–L7 覆盖表（本次重查实测）

| 层级 | 内容 | 结果 |
|---|---|---|
| L0 官网全量 | 首页/about/services/rental/projects/contact 全抓 + HTML 源码正则 | ✅ 首页源码含 `info@iscoca.ca`；contact 页仅表单无明文邮箱；页脚执照/电话/地址齐全 |
| L1 政府一手 | 安大略注册库 / ESA 执照库 / 联邦库 | ⚠️ 执照号 7007530 仅官网自述，ESA 公开查询需交互会话未独立验证；联邦库查无（疑省注册） |
| L2 命名+DNS | MX/SPF/域名验证 | ✅ M365 托管、可收发；无网关；推演规则冲突不可用 |
| L3 B2B 交叉 | Prospeo/ZoomInfo/RocketReach/SignalHire/Tracxn | ✅ 规模/人名交叉，邮箱规则冲突已记录；B2B 人名凡官网无印证者判待核 |
| L4 社媒协会 | LinkedIn/FB/Indeed/Procore | ✅ 公司+创始人+8 名员工+在营证据；Susan 同名已排重 |
| L5 本地黄页同址 | YP/Yelp/Mapquest/NAPC | ✅ YP 5星1评+双电话+24h营业；同址无多 LLC 集群 |
| L6 电话表单兜底 | 总机+表单 | ✅ 905-238-8700 多源；官网表单可用；点名转交话术已备 |
| L7 付费 API | Hunter/Snov/Apollo | ❌ 未启用（无 API，标注） |

## 附：渠道覆盖清单

官网 ✅ / HTML 源码 ✅ / LinkedIn ✅ / Facebook ✅ / Indeed ✅ / Procore ✅ / YellowPages ✅ / NAPC ✅ / Oilmonster ✅ / Prospeo ✅ / ZoomInfo ✅ / RocketReach ✅ / SignalHire ✅ / Tracxn ✅ / DNS ✅ / 安省注册库 ⚠️（需会话）/ ESA 执照库 ⚠️（官网自述为准）/ 海关 ❌（无记录）/ Instagram-Twitter-YouTube ❌（未找到）

---

*交接信息来源截止：2026-09-21*
*本次覆盖重写新增：用户供信息核验表、Procore 在营与合同情报、Selva 西门子/Eaton 履历、LinkedIn 14 员工新名单 4 人、Oilmonster 1983 单源年份、Indeed 在营证据、416 新电话单源警告、info@ 首页源码实测复现、L0–L7 与渠道覆盖表、在营 7 判据结论*
