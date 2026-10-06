# 【买家 75】开发信交接单 — HS Energy System LLC

> 采集日期：2026-09-23 / 来源：项目1候选输入（公司名+MD地址+hsenergyusa.com/terms,/about）/ 已验证与未获取声明见各字段
> 一句话结论：ETS迪拜集团2026年2月新设的美国分销前台（UPS地址、无具名美国负责人、仅角色邮箱），同行制造关联强，建议降优先级、只谈缺口/OEM。

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示(如有)
HS Energy System LLC | 未找到（L-1未锁定具名决策人；仅ETS迪拜侧Raniya Fenniri，非决策人） | 未找到 | info@hsenergyusa.com（B档角色，仅点名转交，不可主送） | 已验证(B档) | 公司LinkedIn未找到；ETS关联人linkedin.com/in/raniya-fenniri-9620641b8（迪拜） | 美国MD Gaithersburg，2026年新设，ETS(UAE)/Patel Trading/IEO荷兰背书，自称ETS独家美国伙伴，EHV 132-400kV到UL padmount全产品线+US stock | 官网terms/about/products/locations（搜索索引）+ RDAP + DNS + ETS/Patel官网 + LinkedIn个人页 | 地址为UPS Store邮箱租赁点；域名仅7个月；电话919(NC)与MD地址异地；同行制造关联（ETS自有8工厂）
```

## 二、补充信息（扩展段）

### 标准字段明细
- 国家+城市：美国 Maryland Gaithersburg
- 详细地址：325 Ellington Blvd, Suite #658, Gaithersburg, MD 20878-4591（官网terms原话；用户给的325 Ellington Blvd Suite 658一致）
- 电话：+1 (919) 757-4420（官网全站一致；919为北卡Raleigh区号，与MD地址异地，未经第二源印证）
- LinkedIn：hsenergyusa公司页**未找到**（4组query：linkedin站内dork仅命中波兰/英国/德国同名+休斯顿石油HS Energy，无hsenergyusa slug）
- 网站：hsenergyusa.com（React SPA，Cloudflare NS louis/sarah；直抓仅返回标题，正文靠搜索索引提取）
- 成立：域名RDAP注册 **2026-02-21**（Network Solutions，过期2031-02-21）；公司自称 backed by ETS等，无独立成立年份 → 按2026年新设前台判定
- 员工：未找到（无LinkedIn公司页；无招聘信息）
- 年营收：未找到
- NAICS/PSC/州注册号：未找到（MD SDAT未直取，登录/JS墙，标注缺口）

### 联系人（含 still_here 在职核验）
| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| Raniya Fenniri | ETS迪拜 CRM & Marketing Executive（**非HS美国决策人**，仅网站author/页脚署名） | CRM & Marketing Executive @ Emirates Transformer and Switchgear LTD | ~10个月 | 高：2026-08-25 Middle East Energy 2026转帖；2026-05 IEEE PES T&D 2026 Chicago Booth 470帖 | 不适用（不在目标公司） | linkedin.com/in/raniya-fenniri-9620641b8 |
| 美国具名决策人 | 未找到 | — | — | — | — | — |
| Saurabh Patel / Dax Patel | Patel/Techno集团家族成员（**关联方，非HS任职证据**） | — | — | — | 不作收件人 | technoelectromech.com/about-us/saurabh-patel；about.me/dax |

- L-1结论：**未锁定具名决策人**（官网无Team页、contact仅表单+info/电话、无LinkedIn公司页员工名单、政府一手无业主信息）→ 自动触发H6升级三步（见邮箱分档）。

### 邮箱分档（A/B/C）
- **A档（具名）**：无。🔴 **「仅取得角色邮箱 `info@hsenergyusa.com`，未取得决策人直邮」**
- **B档（角色，已验证）**：`info@hsenergyusa.com` — 官网terms/contact/faq/products全站一致明示；DMARC rua同为该址 → 已验证B档，仅点名转交
- **C档**：无
- H6升级三步（已跑完，均失败，如实记录）：
  1. 职能邮箱挖掘（Supplier/Estimating/Purchasing）：官网contact/products/advantages均只列info+电话+表单 → 未找到
  2. 真实回信反推命名规则：无任何具名样本 → 无法反推
  3. 免费推演：无具名决策人姓名 → 无法推演（不造名推演，防买家10事故）
- 转交策略：首封发info并点名 "Attn: Purchasing / ETS US team – RFQ via Gaithersburg team"，48–72h无回再拨919电话点名要采购负责人姓名。

### 我为什么找他
- 用户给的“ETS独家美国伙伴+EHV到UL padmount+US stock+对标宽产品线”回源全部命中（terms+products各页）；EHV 132–400kV/500MVA、padmount 25–2500kVA UL1561、cast resin 100kVA–25MVA UL1562、package变300kVA–5MVA 72kV、inverter/solar/BESS、MV cable、switchgear——是变压器整机+配套的全口径分销入口；但其自有工厂背景决定只能谈缺口。

### 买家类型 / 需求品类
- 买家类型：🔥🔥 **分销商（ETS独家美国前台）+ 同行制造关联**（ETS集团8工厂，1987年起自产液浸配电变；IEO荷兰1984年被Patel家族收购）
- 需求品类（带结论态）：
  - `三相美变（UL E541627，可直供）` — 仅当其UL padmount无现货/交期缺口时切入，需首轮问stock清单
  - `主变/变电站变（产能可覆盖，UL区间外，需人工确认）` — EHV 220–400kV 100–300MVA远超UL HV区间，只能谈能力+个案
  - `干变（美国可谈条件：对方自称UL1562，但我方对美无UL，主动不提干变）` — 首封不挂干变钩子
  - 总判：对方全产品线自称UL齐全（1561/1562/IEEE C57/DOE 2016），**与我方整机直供正面撞车概率高** → 降优先级，或转OEM/交期补位话术

### 电压·频率·认证要求
- 电压（官网搜索索引原话）：EHV 132/220/400kV（100–300MVA，最大500MVA）；padmount 25–2500kVA / 75kVA–10MVA 4.16–34.5kV；package 300kVA–5MVA up to 72kV（美15/27/35kV classes）；cast resin 100kVA–25MVA 6.6–36kV；medium power 3.15–40MVA；solar 1–100MVA 36kV；BESS 1–300MVA 132kV
- 频率：60Hz（美国）
- 认证：自称 UL 1561 / UL 1562 / IEEE C57.12系 / C57.159 / IEC 60076-11/62271/61439 / DOE 2016 / F1/C2 / K13–K20 / IP54-65（均为官网自称，无第三方证书号印证，首轮要求其提供UL file number后再对等亮我方E541626/E541627）

### 采购信号
- 工厂直销+US stock+48–72h RFQ承诺（contact页meta）— 有真实接单动作
- IEEE PES T&D 2026 Chicago Booth 470参展（Raniya 2026-05帖）— 北美铺渠道进行时
- 背靠ETS/Patel/IEO三国集团（emiratestransformer.com + pateltrading.com双官网互认集团名单，含HS Energy/HS Switchgear）— 身份背书为真
- 反信号：域名7个月、无LinkedIn、无美国具名人、无stock地址 → 前台真实履约能力待验证

### 可利用的钩子（按强度排序，落点只在可直供/条件切入，不挂干变）
1. UL padmount现货缺口/交期补位（E541627区间内规格）— 首轮先要其US stock清单
2. EHV大容量交期分担（只谈产能+IEEE试验依据，不暗示UL覆盖）
3. Data center/BESS inverter-duty K13–K20谐波场景 — 问其常用容量段
4. IEEE T&D 2026 Booth 470跟进 — 以“会后补资料”名义破冰

### 开发信建议
- 收件人：info点名转交（Attn Purchasing）；主题带 "UL padmount stock gap / EHV lead-time support – JZPE (UL E541627/E541626)"
- 正文：先问stock+交期，不报价格交期；附件不带名录PDF； alternates只给UL号
- 发送时段：美东周二–周四上午 = 北京时间21–23点
- 送达：M365 Outlook专线（mx hsenergyusa-com.mail.protection.outlook.com），SPF `include:spf.protection.outlook.com ~all`，DMARC p=none rua=info@ → 可投递，首封纯文本+单链接；48h无回用919电话跟进并索取采购人姓名（补L-1）

### ⚠️ 矛盾点与风险提示
- 🔴 **地址陷阱**：325 Ellington Blvd有The UPS Store门店（locations.theupsstore.com同址），Suite #658系信箱号；同楼另有BullFrog AI Unit 317等多租户 → **不可寄样**，大件必电话确认真实仓
- 🔴 **同行分销**：ETS自产+8工厂，直推整机=给竞争对手供货 → 必须走缺口/OEM/交期话术，忌首封亮底价
- 电话异地：919(NC) vs MD地址 → 转交时核实接听地
- 新域名新站：2026-02-21注册，无历史沉淀；“leading/#1 vendor”系自称，无第三方背书
- Raniya归属：网站author署名≠美国员工，其LinkedIn current=ETS迪拜 → 不作收件人，不作在职核验对象
- “独家美国伙伴”仅官网自称，ETS官网未逐字印证exclusive → 写“自称独家”，项目3勿作背书引用

### 信息缺口清单（请勿编造）
- 美国具名决策人姓名/职位/直邮：未找到（无公司LinkedIn、无Team页、无州注册业主）
- MD州注册号/董事/代理人：未找到（SDAT未直取）
- 年营收/员工数：未找到
- US stock地址/清单：未获取（官网只写availability，无仓址）
- UL file number（对方1561/1562）：未获取
- 职能邮箱（purchasing/estimating）：未找到

### 一句话画像
ETS迪拜集团刚搭的美国卖货前台——货全（EHV到padmount）但根基浅（UPS地址+7个月域名+无人出镜），当同行分销对待，先问库存缺口再决定给不给价。

### 渠道覆盖清单（L-1、L0–L7）
| 层 | 结果 | 一句话 |
|---|---|---|
| L-1 锁人 | ❌ | 美国具名人未锁定；Raniya系迪拜ETS市场非决策人，已排除 |
| L0 官网 | ✅ | info+919电话+MD地址+全产品线（搜索索引提取，SPA直抓空） |
| L1 政府一手 | ⚠️ | RDAP域名2026-02注册；MD SDAT/州注册未直取 |
| L2 命名+DNS | ✅ | M365 Outlook；SPF软配；DMARC p=none；无样本不推演 |
| L3 B2B库 | ❌ | 无覆盖（新设，无档案） |
| L4 社媒协会 | ⚠️ | 无公司LinkedIn；ETS/Patel集团官网背书+IEEE展帖 |
| L5 黄页同址 | ✅ | UPS Store同址反查命中 → 地址陷阱实锤 |
| L6 电话表单 | ✅ | 电话+RFQ表单齐（未拨打，留给项目3跟进索人名） |
| L7 付费 | ❌ | 未启用 |
