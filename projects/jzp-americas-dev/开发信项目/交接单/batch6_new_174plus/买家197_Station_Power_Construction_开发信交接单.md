# 【买家 197】开发信交接单 — Station Power Construction, LLC

> 采集日期：2026-09-29 / 来源：batch6 名单（第 24 行，CSV 州省 **空**、备注「无 MX」）/ 一句话结论：**亚利桑那 Phoenix 的小型家族变电站/线路承包商**；**官网域确实无 MX，但真实邮箱域是 `stationpwr.com`** —— 已 SMTP 实测验证 **owner 级具名邮箱（jbarriger@stationpwr.com）**，A 档可主送。**州省已补全：CSV「—」→ 实测 AZ（Phoenix）**。

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示(如有)
Station Power Construction, LLC | John Barriger | Founder / Senior Operations Director（owner） | jbarriger@stationpwr.com | 已验证（SMTP 250，控制地址 250 + 非 catch-all + 对照组 550） | 未找到公司/个人 LinkedIn 页 | AZ Phoenix，家族企业，变电站安装+架空/地下线路，IBEW 769 工会工，ISNetworld 会员，创始人 John & Dana Barriger | EVITP 名录（邮箱明文）+ 官网 /about + SMTP 实测 + stationpwr.com DNS | 🔴 邮箱域 ≠ 官网域（stationpwr.com）；官网域无 MX，勿发官网域
```

## 二、补充信息（扩展段）

### 标准字段明细
- 国家+城市：美国 Arizona，Phoenix
- 详细地址：**22 N 27th Ave #225, Phoenix, AZ 85027**（EVITP 名录登记）
- 电话：**623-262-7228**（EVITP 名录）
- LinkedIn：**未找到**（公司页与个人页均未命中）
- 网站：stationpowerconstruction.com（**Wix 建站，NS=wixdns.net，A=185.230.63.107，无 MX、无 SPF**）
- **真实邮箱域**：`stationpwr.com`（MX=Outlook/M365，A=74.220.219.183，SPF `include:spf.protection.outlook.com -all`；站点可访问 HTTP 200）
- 成立日：未找到（官网只述「began with underground work…」，无年份）
- 规模：**小型家族企业**（官网原句 "this small family-owned business"；创始人 John & Dana Barriger）
- 营收：未找到
- 资质：**IBEW Local 769** 工会工；学徒由 Southwestern Line Constructors 培训；**ISNetworld® 会员**（安全合规平台）
- 州省修正：**CSV 原值 = 「—」（空）｜ 实测 = AZ（Phoenix）**（依据：官网标题 "…| Phoenix"、/about 明写 "Arizona"、EVITP 地址 Phoenix AZ 85027、电话 623 亚利桑那号段）

### 联系人（含 still_here 在职核验）
| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| John Barriger | **创始人 / 经营负责人（本次主送）** | Founder & Senior Operations Director | 公司自创立至今（>30 年行业经验） | 中：官网首页与 /about 均列其名 + 邮箱 SMTP 250 实测 | 低（owner，与公司存续绑定） | 未找到 |
| Dana Barriger | 共同创始人 | Co-founder（John 之妻） | 自创立至今 | 中：官网 /about 列其名 | 低（owner） | 未找到 |

> 🔴 一家只发 1 人：**主送 John Barriger（Founder / Senior Operations Director）**。

### 邮箱分档（A/B/C）
- **A 档（具名，已验证）**：`jbarriger@stationpwr.com`（John Barriger）
  - 验证矩阵：控制地址 `info@stationpwr.com` = **250**（该域真实地址）｜随机地址 `zzz_nonexistent_probe_9987@stationpwr.com` = **550**（非 catch-all）｜对照组 `john.smith@`/`jane.doe@`/`bob.jones@` = 全 **550**｜候选 `jbarriger@` = **250** ✅
  - 交叉印证：**EVITP 名录（Electric Vehicle Infrastructure Training Program 官方项目登记）**明文给出 `jbarriger@stationpwr.com` ＋ SMTP 实测（一手级来源 + 实测，H5 达标）
  - 附带命中：`dbarriger@stationpwr.com` = **250**（Dana Barriger，备选，不重复发）
- **B 档（角色）**：`info@stationpwr.com`（该域控制地址实测 250，可作兜底）
- 🔴 **H6 声明**：**不适用**（已取得具名决策人邮箱）
- 🔴 **域名陷阱处置**：官网域 `stationpowerconstruction.com` **无 MX ⇒ 必退信**；**务必用 `stationpwr.com` 域**（详见「开发信建议」）。

### 我为什么找他
- 这家公司官网**只给了一个联系表单和电话、且官网域根本不收信**——多数人到此就会放弃；但 **John Barriger 的名字在官网 /about 页被明确写为公司的起点**（"After years of building and maintaining power lines and substations… **John Barriger** identified a rapid need… That discovery led **John and his wife Dana Barriger** to venture out"）——即**他是这家公司的创办人兼实际经营者**。
- 同时 **EVITP 官方项目登记库**给出他的直邮 `jbarriger@stationpwr.com`，且该邮箱**经 SMTP 实测确认真实可达**——一家「官网收不了信」的公司，**唯一可达的决策人邮箱**已被锁定。

### 买家类型 / 需求品类
- 买家类型：🔥 **B 电气承包商（变电站安装 + 架空/地下线路，小微家族企业）**——实测画像 B 型
- 需求品类（带结论态）：
  - `三相美变（UL E541627，45–5,000 kVA，可直供）` —— 变电站安装/扩容主谈
  - `主变 / 变电站变（UL E541626，750–110,000 kVA，可直供）` —— 其 "large substations for utility companies" 业务对口，项目制
  - `单相柱上变（认证在办 E544629，条件切入）` —— 配网线路，非首推
  - ⚠️ 美国客户：**不谈干变**（无 UL 不匹配）

### 电压·频率·认证要求
- 电压：未获取（其业务含 "electrical substations" 与配电线路，典型 AZ 中压，**未证实**）
- 频率：**60 Hz**（美国）
- 认证：我方 UL **E541627 / E541626** 正式 CoC，适配美国

### 采购信号
- 官网业务明写 "**new services of power lines and electrical substations**"、"upgrade and increase the **capacity of substations and lines**" → **变电站扩容 = 变压器需求场景**
- **ISNetworld 会员 + IBEW 769 工会工** → 有正规安全/合规体系，是**可接合格供应商的承包商**（非游击队）
- 客户群含 "public and private utilities, municipalities, and industrial companies in Arizona" → 有公用事业项目流
- 家族企业、决策链短 → 老板直接拍板

### 可利用的钩子（按强度排序）
1. **变电站安装/扩容专精**（官网 "substations" 与 "upgrade capacity of substations"）—— 与美变/主变强相关
2. **创始人亲管项目**（官网 "John Barriger … oversees every project"）—— 一把手可达
3. **IBEW 769 + ISNetworld + 工会工** → 合规体系健全，供货准入路径清晰
4. **Arizona 本地公用事业/市政客户群** → 项目制采购

### 开发信建议
- **收件人策略**：主送 `jbarriger@stationpwr.com`（John Barriger，A 档，可写个性化正文）；`dbarriger@` 与 `info@stationpwr.com` 仅作兜底，**不重复发**
- 🔴 **域名提醒（务必照做）**：**收件地址必须用 `@stationpwr.com`**，**绝不可**写成 `@stationpowerconstruction.com`（该域无 MX，必退信，会伤发件域信誉）
- **开场角度**：从其 **变电站安装/扩容 + 家族企业创始人亲管**切入（写信 agent 决定措辞）
- **发送时段**：亚利桑那 **MST（UTC-7，全年不夏令时）**，周二–周四当地上午 = **北京时间次日 00:00–03:00** 区间（勿按 PDT 折算）
- **送达配置**：MX = **Outlook / Exchange Online（M365）**，SPF `-all` → 发信域须 SPF/DKIM/DMARC 齐备；**M365 对探测 IP 有 Spamhaus 反制，勿对本域做多轮 SMTP 探测**
- **附件建议**：不带名录/供货记录；如需仅附 UL 证书号 + 容量区间

### ⚠️ 矛盾点与风险提示
- 🔴 **官网域 ≠ 邮箱域（本单核心陷阱）**：`stationpowerconstruction.com`（Wix）**无 MX ⇒ 不可收信**；真实邮箱域为 `stationpwr.com`。写信/发送环节**必须用 stationpwr.com**。
- ⚠️ **州省为补全值**：CSV 原为「—」，本单据官网标题 + EVITP 地址判定为 **AZ（Phoenix）**。
- ⚠️ 官网**无公司/个人 LinkedIn 页**、无成立年份 → 规模/历史信息稀薄，画像以官网自述为准。
- ⚠. **公司名易混**：站内 testimonial 提到 "American Line **Builders**, Inc."（ALB，另一家公司）与 "Klondyke, Inc."——**不是本司**，勿混入。
- ⚠️ 地址 22 N 27th Ave **#225** 为带套房号的办公单元 → 可能为小办公室；寄样前建议电话 623-262-7228 确认收货地。

### 信息缺口清单（请勿编造）
- 公司**成立年份**：未找到
- **年营收 / 员工数**：未找到
- **常用变压器容量 / 电压 / 品牌**：未获取
- 公司/个人 **LinkedIn 页**：未找到
- **州注册主体全称 / 注册日**（AZCC 备案）：未查
- John Barriger 的**正式职务全称**（官网记 "Senior Operations Director"，/about 记其为创始人）：以官网两处口径并存为准，**勿写死**
- **官网域与邮箱域不一致的原因**（是否另有一实体的 stationpwr.com）：未证实

### 一句话画像
凤凰城一家官网收不了信的家族变电站承包商——真正的决策人 John Barriger 的邮箱藏在 `stationpwr.com` 域里，**SMTP 实测可达**；创始人亲管项目、IBEW 工会体系，是最典型的「小而有决策权」的 B 型目标。

### 渠道覆盖清单（L-1、L0–L7）
| 层 | 结果 | 一句话 |
|---|---|---|
| L-1 锁人 | ⚠️ | 官网 /about 锁定创始人 John & Dana Barriger；无 LinkedIn |
| L0 官网 | ✅ | 首页 + /about 取业务与创始人；Contact 页为 Wix 表单（JS 渲染，抓不到邮箱） |
| L1 政府一手 | ⚠️ | AZ UTRACS（AZDOT）企业档案页存在但抓取失败；EVITP 为官方项目登记（半一手） |
| L2 命名+DNS | ✅ | 官网域无 MX；实测邮箱域 stationpwr.com 有 MX，SMTP 四步协议验证 jbarriger@ 250 |
| L3 B2B 库 | ❌ | 未找到有效条目（D&B 付费墙） |
| L4 社媒协会 | ⚠️ | 无 LinkedIn；ISNetworld 会员（平台内） |
| L5 黄页同址 | ✅ | EVITP 地址与官网 Phoenix 一致 |
| L6 电话表单 | ✅ | 623-262-7228 + Wix 表单（未拨打/未提交） |
| L7 付费 | ❌ | 未启用 |
