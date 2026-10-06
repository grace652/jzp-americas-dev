# clients/ · 客户信件索引

> ⚠️ **本文件是派生文件，不要在这里手改客户行。**
> 数据来自 `开发信跟进表.md`（客户/买家类型/骨架/国家/状态）+ 各封信的批注（钩子/切片/开场）。
> 改完源数据后重跑生成脚本即可刷新（脚本见文末 §五）。

## 一、用途（写新信前先查这里）

写一封新开发信时，**先在本表里找 1–2 家同类客户**，看当时用的是哪种钩子、
切的是哪片段、开场引的是什么证据 —— 避免同一买家里用重复措辞，
也避免重新发明已经验证过的角度。

| 要查什么 | 看哪一列 |
|---|---|
| 这家是什么买家 | 买家类型 |
| 同类买家上次用什么钩子 | 钩子 |
| 落点收在哪段产品 | 产品切片 |
| 开场引的是什么证据 | 开场角度 |
| 信文件 | 文件 |

> 🔴 **铁律提醒（`01` §三）**：钩子落点只落在**自己真有的产品**上。
> 本表「产品切片」列记录的就是实际落点，可作同类的参考基线。

## 二、速查统计

**买家类型分布**（共 116 家）

| 买家类型 | 家数 | 默认钩子（`01` §三）|
|---|---|---|
| 承包商 | 57 | 工厂测试数据 / 规格书（按电压切片） |
| 分销商 | 47 | 价格阶梯 + MOQ + 交期 |
| EPC | 7 | 报审 submittals |
| 服务商 | 3 | 工厂测试数据 |
| 渠道 | 1 | 价格阶梯 + MOQ + 交期 |
| 咨询 | 1 | （试探函） |

**钩子实际使用分布**

| 钩子 | 家数 | 备注 |
|---|---|---|
| 价格阶梯+MOQ+交期 | 48 | 分销商/合作社/渠道默认 |
| 工厂测试数据+规格书 | 46 | 承包商默认（多数信未显式标注，按买家类型归类） |
| 报审 submittals | 9 | design-build 有选型权的客户 |
| 测试报告样本 | 5 | 信件中显式记载 |
| 文档备档 for bids | 4 | 投标驱动总包（Williams） |
| 规格书（分电压） | 2 | 早期信件显式记载（BG / Ontario） |
| PSC 品类直引 | 1 | 联邦承包商（ALB，最锋利钩子） |
| 工厂测试数据 | 1 | 调试/测试专家（TPS） |

> 其中 **15 家**信件批注里有显式钩子记载，其余按买家类型归入默认钩子类。

## 三、索引表（116 家）

按买家类型分组，同组内按跟进表序号排列。

### 承包商（57 家）

| # | 客户 | 国家/州 | 骨架 | 钩子 | 产品切片 | 开场角度 | 文件 |
|---|---|---|---|---|---|---|---|
| 2 | Ontario High Voltage Services Ltd. | 安大略省奥兰治维尔 | A | 规格书（分电压） | 变电站变+液浸 | 直接点电压等级 + 超量库存 | 开发信-Ontario-High-Voltage.md |
| 3 | ISCOCA Ltd. (Iscoca Electrical Services Limited) | 安大略省密西沙加 | A | 工厂测试数据+规格书 | 干变+液浸 | 直接引用对方 Equipment 页的"可买断清单" | 开发信-ISCOCA.md |
| 4 | Williams Electric & Line Construction Inc. | 阿拉巴马州 Tuscumbia | A | 文档备档 for bids | 变电站变+柱上变 | 引用对方业务范围本身 | 开发信-Williams-Electric.md |
| 5 | ALCO Electric, LLC | 华盛顿州 Vancouver | A | 报审 submittals | 柱上变+液浸 | 用对方官网 Projects 页的 15 个实名项目 | 开发信-ALCO-Electric.md |
| 6 | Alaska Line Builders, LLC | 阿拉斯加州 Houston · Big Lake | A | PSC 品类直引 | 变电站变+液浸 | Your SAM.gov registration lists PSC 6120 — Tra… | 开发信-Alaska-Line-Builders.md |
| 7 | PowerTec Electric LLC | 阿拉斯加 Anchorage + 华盛顿州 Redm | A | 测试报告样本 | 变电站变+液浸 | 先点他的专业领域，再点具体项目 | 开发信-PowerTec-Electric.md |
| 8 | Technical Power Services, Ltd. Co. | 德克萨斯州 Ennis | A | 工厂测试数据 | 变电站变+液浸 | 用官网原文的电压范围 + 两项服务 | 开发信-Technical-Power-Services.md |
| 9 | KVA Electric, Inc. | 华盛顿州 Arlington | A | 测试报告样本 | 变电站变+液浸 | 用最硬的公开证据 —— Oahe 大坝 GSU 变压器套管检修 | 开发信-KVA-Electric.md |
| 10 | Chatham Electric, Inc. | 阿拉斯加州 | A | 测试报告样本 | 变电站变+液浸 | 两个实名项目 + 一句判断 | 开发信-Chatham-Electric.md |
| 11 | Pritchard Electric Company, Inc. | 西弗吉尼亚州 Huntington | A | 测试报告样本 | 柱上变+液浸 | 两句话完成"研究证明 + 落点" | 开发信-Pritchard-Electric.md |
| 12 | Aequitas Power Company, LLC | 肯塔基州 Shelbyville | A | 测试报告样本 | 美变/箱变+柱上变 | 不带"浏览动作"地引用他的业务 | 开发信-Aequitas-Power.md |
| 13 | Pitts Electric Co., Inc. | 佐治亚州 Macon | A | 工厂测试数据+规格书 | 柱上变+配电变 | 抓住库存清单里的那个 "some" | 开发信-Pitts-Electric.md |
| 14 | Wolfe & Travis Electric Company, Inc. | 田纳西州 Nashville | A | 报审 submittals | 美变/箱变+液浸 | 具名项目 + 电压等级（两句话完成"研究证明"） | 开发信-Wolfe-Travis-Electric.md |
| 15 | Guerry Electric, LLC | 密西西比州 Columbus | A | 工厂测试数据+规格书 | 美变/箱变+柱上变 | 两个官网原文事实 + 一句过渡 | 开发信-Guerry-Electrical.md |
| 18 | Bossie Electric (BOSSIE, INC.) | 西弗吉尼亚州 Charleston | A | 工厂测试数据+规格书 | 变压器整机(通用) | 用他最强的差异化（塔站 30 年）做证据，落点只收变压器 | 开发信-Bossie-Electric.md |
| 19 | Premier Electric, LLC | 阿拉斯加州 Palmer | A | 工厂测试数据+规格书 | 柱上变+配电变 | 最硬的那条证据：他们在 SAM.gov 自己申报了采购品类 | 开发信-Premier-Electric.md |
| 20 | Oregon Electric Service, L.L.C. | 俄勒冈州 Eugene | A | 工厂测试数据+规格书 | 柱上变 | 用他自己的服务条目 + 三个实名项目 | 开发信-Oregon-Electric-Service.md |
| 21 | C.W. Galle Contracting, Inc. | 密西西比州 Ocean Springs | A | 工厂测试数据+规格书 | 小变压器(≤500kVA) | 只引官网原话，不加县名、不加高压词 | 开发信-CW-Galle.md |
| 23 | Romar Electrical Services Inc. | 安省 Hamilton | A | 工厂测试数据+规格书 | 变电站变+美变/箱变 | 硬电压证据 + 变压器维修原话 | 开发信-Romar-Electrical.md |
| 28 | Vancouver Industrial Electric Ltd. | BC 省 Langley | A | 工厂测试数据+规格书 | 变电站变+美变/箱变 | 测试分部原话 + 服务区 | 开发信-Vancouver-Industrial-Electric.md |
| 29 | Amped Electric LLC | 西弗吉尼亚州 Parkersburg | A | 工厂测试数据+规格书 | 美变/箱变+柱上变 | You do 200A panel upgrades and standby generat… | 开发信-Amped-Electric.md |
| 34 | Transformer Engineering Services | 安省 Stouffville | — | 工厂测试数据+规格书 | — | — | （电话店，无信文件） |
| 36 | Reeve Electric Company, Inc. | 阿拉巴马州 Birmingham | A | 工厂测试数据+规格书 | 配电变+变电站变 | Your data center page lists medium and high vo… | 开发信-Reeve-Electric.md |
| 37 | DECH High Voltage Inc. | 安省 Greater Sudbury | A | 工厂测试数据+规格书 | 整机+逐台测试报告 | You work on electrical systems rated 480V and … | 开发信-DECH-High-Voltage.md |
| 38 | Rogers Electrical Contracting Company, Inc. | 西弗吉尼亚州 Fairmont | A | 工厂测试数据+规格书 | 变电站变+美变/箱变 | Could you please forward this to Ian Frailey i… | 开发信-Rogers-Electrical.md |
| 39 | South Charleston Electric Company, Inc. | 西弗吉尼亚州 South Charleston | A | 工厂测试数据+规格书 | 美变/箱变+柱上变 | Could you please forward this to Eric Moore? S… | 开发信-South-Charleston-Electric.md |
| 40 | Washington State Power, LLC | 华盛顿州 Olympia | A | 工厂测试数据+规格书 | 箱变+柱上变 | Your high voltage page lists transformer servi… | 开发信-Washington-State-Power.md |
| 42 | VoltCore Electrical LLC | 德州 Austin | A | 工厂测试数据+规格书 | 整机+逐台测试报告 | Your substation page lists distribution and tr… | 开发信-VoltCore-Electrical.md |
| 43 | GLS Electric, Inc. | 俄亥俄州 South Point | A | 工厂测试数据+规格书 | 工业配电变 | Your power distribution page promises "Power D… | 开发信-GLS-Electric.md |
| 47 | GEC, Inc. | 西弗吉尼亚州 Bruceton Mills | A | 工厂测试数据+规格书 | 变电站+箱变+小控制变 | 138kV 原话 + 自产控制变六档 + 接地保护/模块化中心，均为官网原文。 | 开发信-GEC.md |
| 50 | K2 Electric Ltd. | BC 省 Prince George | A | 工厂测试数据+规格书 | 整机+逐台测试报告 | 1999 + 100+ BC Hydro + Barlow 互联 + 变压器集成 + 盘厂，… | 开发信-K2-Electric.md |
| 53 | Sunbelt Solomon | 德州 Temple | A | 工厂测试数据+规格书 | 新机整机 | 全生命周期 + 42 地 + 新箱变/站用线，均为官网原文。落点新变压器整机。 | 开发信-Sunbelt-Solomon.md |
| 55 | Westmoreland Electric Services, LLC | 宾州 Tarrs | A | 工厂测试数据+规格书 | 工业配电变 | MV 升级（Clarion 点名）+ 4000A/500kW + 6 污水厂（Unionto… | 开发信-Westmoreland.md |
| 56 | Dana Power and Poles, LLC | 纽约州 Port Jervis | A | 工厂测试数据+规格书 | 中压配电变 | MV 全阶段 + URD/HI POT/电杆，均为官网原文。落点中压配电变。 | 开发信-Dana-Power.md |
| 58 | GRIDLINK (Thunder Bay) | 安省 Thunder Bay | A | 工厂测试数据+规格书 | 整机+逐台测试报告 | 变电站新建重建 + 4–25kV + 230kV 清洗 + Hydro One/Siemen… | 开发信-GRIDLINK.md |
| 59 | Kirby Electric, Inc. | 宾州 Warrendale | A | 工厂测试数据+规格书 | 工业配电变 | blanket order + Conemaugh（13.8kV 开关柜点名）+ Wheel… | 开发信-Kirby-Electric.md |
| 60 | BV Electric Ltd. | BC 省 Telkwa | A | 工厂测试数据+规格书 | 整机+逐台测试报告 | 四水电 + Forrest Kerr 195MW + 变电站/MCC-PDC/开关场 + 北… | 开发信-BV-Electric.md |
| 61 | Stewart Electric Company, Inc. | 阿拉巴马州 Huntsville | A | 工厂测试数据+规格书 | 配电变+变电站变 | 高压变电站/杆线/工业配电 + 1976 + 估算师逐单报价，均为官网原文。 | 开发信-Stewart-Electric.md |
| 63 | Birmingham Electrical Contractors, Inc. | 阿拉巴马州 Bessemer | A | 工厂测试数据+规格书 | 配电变 | MV 测试更换 + 新旧电缆/终端 + 开关柜/发电机/政府，均为官网原文。 | 开发信-Birmingham-Electric.md |
| 64 | Everlast Electric | 新斯科舍省 Halifax | A | 工厂测试数据+规格书 | 小变压器(≤500kVA) | 600V 三相 + 变压器安装 + 商厨 + NS Power 断表换盘，均为官网原文。 | 开发信-Everlast-Electric.md |
| 68 | Amps Powerline Inc. | 曼省 Winnipeg | A | 工厂测试数据+规格书 | 整机+逐台测试报告 | 变电站端到端 + 6–14 小时 + 矿业公用事业，均为官网原文。 | 开发信-Amps-Powerline.md |
| 69 | Fullford Electric Inc. | 阿拉斯加州 Fairbanks | A | 工厂测试数据+规格书 | 变电站变+液浸 | LRDR 室外变电站 + Eielson（杆塔/应急变压器）+ 极寒偏远，均为公开原文。 | 开发信-Fullford-Electric.md |
| 76 | GNS Technologies LLC | 内华达州 Las Vegas | A | 文档备档 for bids | 美变/箱变+液浸 | Came across GNS Technologies in Las Vegas — NV… | 开发信-GNS-Technologies.md |
| 78 | TM3 Inc. | ON Cambridge | A | 文档备档 for bids | 整机+逐台测试报告 | Came across TM3 in Cambridge — substations, sw… | 开发信-TM3.md |
| 82 | HEI Utility Contractors | 印第安纳州 Griffith | A | 文档备档 for bids | 液浸 | Came across HEI Utility Contractors in Griffit… | 开发信-HEI-Utility-Contractors.md |
| 87 | Kraun Electric Inc. | ON St. Catharines | A | 工厂测试数据+规格书 | 配电变 | Could you please forward this to Brandon Bouch… | 开发信-Kraun-Electric.md |
| 89 | Continental Power Services (1987) Ltd. | BC Burnaby | — | 工厂测试数据+规格书 | — | — | （电话店，无信文件） |
| 90 | Intel Electric LLC | AK Anchorage | A | 工厂测试数据+规格书 | 美变/箱变+液浸 | Could you please forward this to Matt Tennant?… | 开发信-Intel-Electric.md |
| 94 | Leading Edge Electric LLC | 阿拉斯加 Wasilla | — | 工厂测试数据+规格书 | — | — | （电话店，无信文件） |
| 95 | Megawatt Electric, LLC | AK Anchorage | A | 工厂测试数据+规格书 | 美变/箱变+液浸 | Could you please forward this to Tony Gongliew… | 开发信-Megawatt-Electric.md |
| 97 | Zeus Electric & Controls Inc. | BC Burnaby | A | 工厂测试数据+规格书 | 整机+逐台测试报告 | Came across Zeus Electric in Burnaby — high-vo… | 开发信-Zeus-Electric.md |
| 100 | Progressive Electric, Inc. | WV Charleston | A | 工厂测试数据+规格书 | 整机+逐台测试报告 | Came across Progressive Electric in Charleston… | 开发信-Progressive-Electric.md |
| 101 | Alcan Electrical & Engineering, Inc. | 阿拉斯加 Anchorage | — | 工厂测试数据+规格书 | — | — | （电话店，无信文件） |
| 105 | Cache Valley Electric Co. | UT Logan | A | 工厂测试数据+规格书 | 整机+逐台测试报告 | Could you please forward this to Scott Gustafs… | 开发信-Cache-Valley-Electric.md |
| 109 | Lemberg Electric Company, Inc. | 威斯康星 Brookfield | — | 工厂测试数据+规格书 | — | — | （电话店，无信文件） |
| 110 | Egan Company | MN Champlin | A | 工厂测试数据+规格书 | 整机+逐台测试报告 | Could you please forward this to Jamie Allen i… | 开发信-Egan-Company.md |
| 111 | Big State Electric, Ltd. | 德州 San Antonio | — | 工厂测试数据+规格书 | — | — | （电话店，无信文件） |

### 分销商（47 家）

| # | 客户 | 国家/州 | 骨架 | 钩子 | 产品切片 | 开场角度 | 文件 |
|---|---|---|---|---|---|---|---|
| 17 | Scientechnic LLC | 阿联酋 · 迪拜 | A | 价格阶梯+MOQ+交期 | 液浸 | 最暖的触达状态）。 | 开发信-Scientechnic.md |
| 24 | Hillfort, LLC | TN Memphis | A | 价格阶梯+MOQ+交期 | 美变/箱变 | OEM 模式 + 交期承诺倒逼供应链 | 开发信-Hillfort.md |
| 25 | MVA Power Inc. | 魁北克 Montreal + L'Assomptio | A | 价格阶梯+MOQ+交期 | 美变/箱变 | turnkey 缺口 + 现货口径 | 开发信-MVA-Power.md |
| 26 | Purcee Industrial Power | 阿省 Foothills | A | 价格阶梯+MOQ+交期 | 美变/箱变+柱上变 | 不写 "your site"，用直陈句 | 开发信-Purcee-Industrial-Power.md |
| 27 | Tri-State Utility Products, Inc. | 佐治亚州 Marietta | A | 价格阶梯+MOQ+交期 | 变压器整机(通用) | 独家代表制 + 四 IOU + Howard 原话 | 开发信-Tri-State-Utility.md |
| 30 | Brownstown Electric Supply Co., Inc. | 印第安纳州 Brownstown | A | 价格阶梯+MOQ+交期 | 配电变整机 | utility-only + 四州 + Howard + 风暴备库 | 开发信-Brownstown-Electric.md |
| 31 | Power Line Supply Company | 密歇根州 Reed City | A | 价格阶梯+MOQ+交期 | 配电变整机 | 最大独立分销 + 六州 + NAIL | 开发信-Power-Line-Supply.md |
| 32 | Irby Utilities (Stuart C. Irby Co.) | 密西西比州 Jackson | A | 价格阶梯+MOQ+交期 | 配电变整机 | 49 州 + 输变电打包 + 高压测试维修 + 风暴应急，均为官网原文。 | 开发信-Irby-Utilities.md |
| 33 | OneSource Distributors, LLC | 加州 Oceanside | A | 价格阶梯+MOQ+交期 | 配电变整机 | 三中心 + Miramar + Rockwell 授权，均为官网原文。落点只收配电变整机。 | 开发信-OneSource-Distributors.md |
| 35 | Techline, Inc. | 德州 Austin | — | 价格阶梯+MOQ+交期 | — | — | （电话店，无信文件） |
| 44 | Rexel Utility | 安省 Mississauga | A | 价格阶梯+MOQ+交期 | 配电变整机 | premier distributor + 三仓 + Trydor + NAIL，均为官网原… | 开发信-Rexel-Utility.md |
| 48 | Fletcher-Reinhardt Company | 密苏里州 Bridgeton | A | 价格阶梯+MOQ+交期 | 整机+维修替换单元 | 1962 + 三仓 + 维修站（重合闸/调压器）+ WBE，均为官网原文。 | 开发信-Fletcher-Reinhardt.md |
| 49 | KBS Electrical Distributors Inc. | 德州 Bryan | A | 价格阶梯+MOQ+交期 | 配电变整机 | 1982 + 10 分仓 + NAAUD + Transformers 在售 + Austi… | 开发信-KBS-Electrical.md |
| 51 | Valley Electrical Suppliers, Inc. | 加州 Visalia | A | 价格阶梯+MOQ+交期 | 配电变整机 | 1977 + 三代 + 5万 SKU/98.6% + 20–30 年复购，均为官网/BBB … | 开发信-Valley-Electrical.md |
| 52 | Border States Electric | 北达科他州 Fargo | A | 价格阶梯+MOQ+交期 | 变电站变+美变/箱变 | 退 AD 事件驱动（本批独有） | 开发信-Border-States.md |
| 62 | Texas Electric Cooperatives, Inc. | 德州 Georgetown | A | 价格阶梯+MOQ+交期 | 整机+套管/油/备件 | 75 社 300万户 + 电杆厂 + EPA 维修 + 钢构，均为官网原文。 | 开发信-TEC.md |
| 65 | Priester-Mell & Nicholson Inc. | 德州 Austin | A | 价格阶梯+MOQ+交期 | 配电变 | Austin Energy + 杆变/死前端开关柜/计量 + 在线商城，均为公开原文。 | 开发信-Priester.md |
| 70 | AECI / Arkansas Electric Cooperatives | 阿肯色州 Little Rock | A | 价格阶梯+MOQ+交期 | 变电站变整机 | 17 成员/120万户 + 发输电 + Jobs Act 2025，均为公开原文。 | 开发信-AECI.md |
| 71 | United Utility Supply Cooperative | 肯塔基州 Louisville | A | 价格阶梯+MOQ+交期 | 变电站/特殊规格 | 全线库存 + 六仓二十州 + custom services + storm invento… | 开发信-UUS.md |
| 72 | RESCO / Rural Electric Supply Cooperative | 威斯康星州 Middleton | — | 价格阶梯+MOQ+交期 | — | — | （电话店，无信文件） |
| 73 | Western United Electric Supply Corp. | 科罗拉多州 Brighton | A | 价格阶梯+MOQ+交期 | 变电站/特殊规格 | 89 社 + 五仓 + W.E.S.T. 打包 + EUDA 池，均为官网原文。 | 开发信-WUE.md |
| 74 | CEEUS, Inc. | 南卡 West Columbia | A | 价格阶梯+MOQ+交期 | 美变齐口+柱上变 | 多品牌并列 + 测试实验室 + 新总部，均为官网原文。 | 开发信-CEEUS.md |
| 75 | General Pacific, Inc. (GenPac) | 俄勒冈州 Fairview | A | 价格阶梯+MOQ+交期 | 现品牌外配电变 | 西北合作社 + Howard/ERMCO 双品牌 + 变压器组 + Fairview/Anc… | 开发信-GenPac.md |
| 77 | RESA Power Components Group | TN Lebanon + CA San Jose | A | 价格阶梯+MOQ+交期 | 美变/箱变+液浸 | Could you please forward this to Dan Arnold in… | 开发信-RESA-Power-Components.md |
| 79 | Electrozad Supply | ON London | A | 价格阶梯+MOQ+交期 | 美变/箱变+液浸 | Could you please forward this to Dave Kruk in … | 开发信-Electrozad-Supply.md |
| 80 | Schaedler Yesco Distribution | PA Mechanicsburg | — | 价格阶梯+MOQ+交期 | — | — | （电话店，无信文件） |
| 81 | Franklin Empire Inc. | QC St-Laurent | A | 价格阶梯+MOQ+交期 | 美变/箱变+液浸 | Could you please forward this to Lucia Nardo o… | 开发信-Franklin-Empire.md |
| 83 | Van Meter Inc. | IA Cedar Rapids | A | 价格阶梯+MOQ+交期 | 美变/箱变+液浸 | Could you please forward this to Lura McBride … | 开发信-Van-Meter.md |
| 85 | Kendall Electric | MI Portage | A | 价格阶梯+MOQ+交期 | 美变/箱变+液浸 | Could you please forward this to Mike Beisel o… | 开发信-Kendall-Electric.md |
| 86 | McNaughton-McKay Electric Co. | MI Madison Heights | — | 价格阶梯+MOQ+交期 | — | — | （电话店，无信文件） |
| 88 | Turtle & Hughes, Inc. | 新泽西州 Clark | — | 价格阶梯+MOQ+交期 | — | — | （电话店，无信文件） |
| 91 | State Electric Supply Co. | WV Huntington | A | 价格阶梯+MOQ+交期 | 美变/箱变+液浸 | Could you please forward this to Brent Mackie … | 开发信-State-Electric.md |
| 92 | Guillevin International Co. | QC St-Leonard | A | 价格阶梯+MOQ+交期 | 美变/箱变+液浸 | Could you please forward this to Rob Appleton,… | 开发信-Guillevin.md |
| 93 | City Electric Supply Company (CES) | 德州 Dallas | — | 价格阶梯+MOQ+交期 | — | — | （电话店，无信文件） |
| 96 | E.B. Horsman & Son | BC Surrey | — | 价格阶梯+MOQ+交期 | — | — | （电话店，无信文件） |
| 98 | Cooper Electric Supply Co. | 新泽西州 Cranbury | — | 价格阶梯+MOQ+交期 | — | — | （电话店，无信文件） |
| 99 | Walters Wholesale Electric Co. | CA Fontana | A | 价格阶梯+MOQ+交期 | 美变/箱变+液浸 | Could you please forward this to Michael Therr… | 开发信-Walters-Wholesale.md |
| 103 | Standard Electric Supply Co. | WI Milwaukee | — | 价格阶梯+MOQ+交期 | — | — | （电话店，无信文件） |
| 104 | Advance Electrical & Industrial Supply | GA Norcross | A | 价格阶梯+MOQ+交期 | 美变/箱变+液浸 | Could you please forward this to Jim Paolucci?… | 开发信-Advance-Electrical.md |
| 106 | Bartle & Gibson Co. Ltd. | AB Edmonton | A | 价格阶梯+MOQ+交期 | 美变/箱变+液浸 | Could you please forward this to Dustin Heske … | 开发信-Bartle-Gibson.md |
| 107 | World Electric Supply, Inc. | 佛州 Jacksonville | A | 价格阶梯+MOQ+交期 | 美变/箱变+液浸 | Could you please forward this to Ben Austin or… | 开发信-World-Electric.md |
| 108 | Echo Electric | IL Springfield | A | 价格阶梯+MOQ+交期 | 整机+逐台测试报告 | Could you please forward this to Rick Larson o… | 开发信-Echo-Electric.md |
| 112 | J.H. Larson Company | 明尼苏达 Plymouth | — | 价格阶梯+MOQ+交期 | — | — | （电话店，无信文件） |
| 113 | Summit Electric Supply | NM Albuquerque | A | 价格阶梯+MOQ+交期 | 美变/箱变+液浸 | Could you please forward this to Bill Seward o… | 开发信-Summit-Electric.md |
| 114 | Dixon Electric | 安省 Burlington | — | 价格阶梯+MOQ+交期 | — | — | （电话店，无信文件） |
| 115 | SESCO / Electrozad | 安省 Toronto | — | 价格阶梯+MOQ+交期 | — | — | （电话店，无信文件） |
| 116 | Robertson Electric Wholesale | ON Vaughan | — | 价格阶梯+MOQ+交期 | — | — | （电话店，无信文件） |

### 渠道（1 家）

| # | 客户 | 国家/州 | 骨架 | 钩子 | 产品切片 | 开场角度 | 文件 |
|---|---|---|---|---|---|---|---|
| 16 | High to Low Voltage, LLC | 科罗拉多州 Commerce City | A | 价格阶梯+MOQ+交期 | 美变/箱变+柱上变 | 用具体规格证明"我懂你的产品结构"（最锋利的一击） | 开发信-High-To-Low-Voltage.md |

### EPC（7 家）

| # | 客户 | 国家/州 | 骨架 | 钩子 | 产品切片 | 开场角度 | 文件 |
|---|---|---|---|---|---|---|---|
| 22 | T&N Electrical Contracting Ltd. | BC 省 Vancouver | A | 报审 submittals | 变压器整机(通用) | 业务线原话 + 当前项目窗口 | 开发信-TN-Electrical.md |
| 45 | R.A. Electrical High Voltage Ltd. | 安省 Cookstown | A | 报审 submittals | 变电站变+美变/箱变 | The Terminator 原话 + 5–230kV + 变压器业务线 + 3700MW，… | 开发信-RA-Electrical.md |
| 46 | Ross Morrison Electrical Ltd. | BC 省 Burnaby | A | 报审 submittals | 整机+逐台测试报告 | 69kV 原话 + BC Hydro/FortisBC + Parkland + 变压器油分… | 开发信-Ross-Morrison.md |
| 57 | Iconic Power Systems Inc. | 阿省 Calgary | A | 报审 submittals | 整机+逐台测试报告 | 500kV AIS/GIS + 端到端 + Chestermere 项目 + 可再生/BES… | 开发信-Iconic-Power.md |
| 66 | Rising Edge Group | 阿省 Calgary | A | 报审 submittals | 整机+逐台测试报告 | 735kV 端到端 + 风光储并网 + Lower Churchill/Suncor，均为官… | 开发信-Rising-Edge.md |
| 84 | MVI LLC | WV Morgantown | A | 报审 submittals | 整机+逐台测试报告 | Noticed MVI designs and builds substations in-… | 开发信-Mon-Valley-Integration.md |
| 102 | Valard Construction | AB Edmonton | A | 报审 submittals | 整机+逐台测试报告 | Came across Valard in Edmonton — hundreds of s… | 开发信-Valard-Construction.md |

### 服务商（3 家）

| # | 客户 | 国家/州 | 骨架 | 钩子 | 产品切片 | 开场角度 | 文件 |
|---|---|---|---|---|---|---|---|
| 1 | B.G. High Voltage Systems Ltd. | 安大略省士嘉堡 | A | 规格书（分电压） | 干变+液浸 | 用了对方官网真实的业务分层（干式 46kV 以下室内 / 液体 46kV 以上户外） | 开发信-BG-High-Voltage.md |
| 54 | Power Substation Services LLC | 西弗吉尼亚州 Wheeling | A | 工厂测试数据+规格书 | 整机+套管/油/备件 | 装配注油调试 + OEM 外包 + 带电再生 + 油实验室，均为官网原文。 | 开发信-PSS.md |
| 67 | Tryggr Technical Services Inc. | 阿省 Edmonton | A | 工厂测试数据+规格书 | 变电站变+液浸 | 30 年 + 69–500kV + 变电站/调试/油务/SF6 + 三省，均为官网原文。 | 开发信-Tryggr.md |

### 咨询（1 家）

| # | 客户 | 国家/州 | 骨架 | 钩子 | 产品切片 | 开场角度 | 文件 |
|---|---|---|---|---|---|---|---|
| 41 | WinAsia Power Corporation Limited | 斯里兰卡 | 试探函 | 工厂测试数据+规格书 | 液浸 | I came across the WinAsia Group's renewable en… | 开发信-WinAsia-Power.md |

## 四、使用规程

### 写新信前（3 步）

1. **定买家类型** → 在本表 §二 找到该类默认钩子。
2. **查同组已有信** → 看「钩子」「开场角度」两列，**不要重复用同一措辞**。
   同类文档钩子要换行话：`for your bids`（投标）/ `for your submittals`（报审）/
   `test report samples`（联邦项目文件）。
3. **定产品切片** → 参考同组「产品切片」列，再按对方电压等级收窄
   （15kV 配电级客户**刻意不提 500kV**；输电/变电站级才谈高压电力变）。

### 写完后（2 项同步）

- 把新客户追加到 `开发信跟进表.md`（**主数据在这里**）。
- 在本表 §三 对应分组里能看到新行 → 重跑生成脚本即可，**不要手改**。

### ⛔ 不要做的事

- ❌ 直接在 INDEX 里手改/新增客户行（会被下次重跑覆盖）。
- ❌ 把「产品切片」当成对某客户的产品范围承诺（它只记录**首封实际落点**）。

## 五、生成脚本

脚本在 `project3/scripts/`（两条命令，按顺序跑）：

```
python project3/scripts/gen_clients_index.py     # 解析源 → recs.json
python project3/scripts/render_clients_index.py  # 渲染 → 本文件
```

脚本逻辑：客户名/买家类型/骨架/国家 ← 跟进表；
钩子（显式批注优先，否则按买家类型兜底）/ 产品切片（「落点」记载优先，
否则从正文产品词反推）/ 开场角度 ← 各封信。

**何时重跑**：

- 新增客户信件后（跟进表追加 + `clients/` 放信）
- 改了某封信的「钩子」或「落点」批注后
- 改了 `01` §三 钩子表里买家类型与钩子的对应关系后
