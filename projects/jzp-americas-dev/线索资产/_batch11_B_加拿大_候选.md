# batch11 · B 类（分销商/贸易商）· 加拿大 · 环节① 找客户候选

> 生成：2026-10-06 ｜ 起始编号 **买家 424**（batch10 止于 423）
> 排重基线：`_dedup_baseline_batch11.txt`（**1445 关键词**）｜ 校验器：`scripts/check_dedup.py --baseline ...`
> 域名验证：`dig @8.8.8.8 MX <域> +short`（本机 TUN fake-ip 已按纪律绕开）
> 逐家**进官网读业务描述原句** + 反身排除（⓪ 层）＋ 排重 ＋ MX。

---

## 〇、结论先说（宁缺毋滥）

**只找到 10 家合格**（目标 20）。**⭐ 高价值档 8 家**。
另有 **2 家「边界候选」**（⓪ 层存疑，需人工定夺），单列于 §三。
**本轮剔除 30+ 家** —— 主因是**来源池见底**：本批最大新来源 Surplus Record 加拿大变压器经销商共 14 家，
**其中 5 家直接命中基线**（A C Nelson / Surplus Electrical Equipment / Boundary Electric〔成交客户〕等），
其余多为制造商或修复翻新商。**SK / MB 依旧颗粒无收**（变压器实体全为制造商：PTI / ETAC / Multicore 等）。
**BC / QC 两省几乎被前批吃光**（Westgrid、Dubo、Distributeck、Besco、CAYER、Renegade、Evolt、FEL、SIB 全部在基线）。

---

## 一、制表符分隔清单（程序解析用）

```
Moncur Electric Supply Ltd.	moncurelectric.com
Electrical Material Company (E.M.C. Ltd.)	electricalmaterials.ca
Parrline Supply	parrline.com
Northern Breaker Group	northernbreakergroup.ca
Carroll Transformer & Switchgear	carrolltransformer.ca
EcoTech NL Inc.	ecotechnl.ca
Powerlogy	powerlogy.ca
O'Neil Electric Supply Ltd.	oneilelectric.com
Argo International Corp	argointl.com
Lakeport Power Ltd.	lakeportpower.com
```

---

## 二、逐家详表

### 1. Moncur Electric Supply Ltd. ｜ 简称 Moncur
| 字段 | 内容 |
|---|---|
| 公司全称 | Moncur Electric Supply Ltd. |
| 国家 / 州省 / 城市 | 加拿大 / ON / Windsor |
| 官网 | moncurelectric.com |
| **业务描述原句** | "As a premier electrical supplier, Moncur Electric Supply prides itself on offering a comprehensive range of high-quality products across various categories to meet all your electrical needs."（https://moncurelectric.com/）／产品页 "We carry: Lighting, distribution, conduit, fittings, cable, data, fuses, enclosures, **transformers**, and more."（https://moncurelectric.com/products-vendors/） |
| 高价值档 | ⭐（transformer） |
| 来源 | 定向检索 `electrical supply Windsor Ontario distributor` |
| MX | ✅ 有（`moncurelectric-com.mail.protection.outlook.com`） |
| 排重 | ✅ 未命中 |
| 排除判定 | 保留（独立电气分销商，含变压器品类） |

### 2. Electrical Material Company (E.M.C. Ltd.) ｜ 简称 E.M.C.
| 字段 | 内容 |
|---|---|
| 公司全称 | Electrical Material Company (E.M.C. Ltd.) |
| 国家 / 州省 / 城市 | 加拿大 / ON / Hamilton |
| 官网 | electricalmaterials.ca |
| **业务描述原句** | "Electrical Material Company (E.M.C. Ltd.) has always been known as a great source for new, used, and surplus electrical materials. We are also a distributor for many new products… As authorized distributors, we provide products from trusted names such as … **Rex transformers, Marcus transformers, Bemag transformers**…"（https://www.electricalmaterials.ca/company/our-suppliers/） |
| 高价值档 | ⭐（transformer） |
| 来源 | 定向检索 `used surplus electrical equipment dealer Hamilton Ontario` |
| MX | ✅ 有（`d408283.a/b.ess.ca.barracudanetworks.com`） |
| 排重 | ✅ 未命中 |
| 排除判定 | 保留（新/旧/积压电气设备经销 + 多家变压器品牌授权分销） |

### 3. Parrline Supply ｜ 简称 Parrline
| 字段 | 内容 |
|---|---|
| 公司全称 | Parrline Supply |
| 国家 / 州省 / 城市 | 加拿大 / ON / Windsor（Essex County） |
| 官网 | parrline.com |
| **业务描述原句** | "Parrline Supply is a proud, family run, third generation independent business in Windsor Essex County. Approaching fifty years in business, Parrline was founded in 1976 by George and Alan Parr which has grown to be a mainstay in the **electrical distribution industry**."（https://www.parrline.com/） |
| 高价值档 | —（官网未出现四关键词） |
| 来源 | 定向检索 `electrical supply Windsor Ontario independent` |
| MX | ✅ 有（`mail.parrline.com`） |
| 排重 | ✅ 未命中 |
| 排除判定 | 保留（独立电气批发商） |

### 4. Northern Breaker Group ｜ 简称 NBG
| 字段 | 内容 |
|---|---|
| 公司全称 | Northern Breaker Group |
| 国家 / 州省 / 城市 | 加拿大 / AB / Calgary（+ Edmonton AB、Surrey BC 共 3 仓） |
| 官网 | northernbreakergroup.ca |
| **业务描述原句** | "Northern Breaker Group has emerged as Western Canada's premier electrical supply network through the strategic alliance of three established regional leaders: Alberta Breaker & Supply Co. Ltd., National Breaker & Supply Ltd., and CPM Electrical Sales."（https://northernbreakergroup.ca/about-us/）／同页 "New, Used & Obsolete Products — We specialize in hard-to-find and obsolete equipment…"；品类页含 **REX 变压器**（https://northernbreakergroup.ca/product-category/transformers/） |
| 高价值档 | ⭐（transformer） |
| 来源 | Surplus Record 电路断路器经销商目录（AB/ON 加拿大经销商）+ 定向检索 |
| MX | ✅ 有（`aspmx.l.google.com`） |
| 排重 | ✅ 未命中 |
| 排除判定 | 保留（西部加拿大电气供应网络，常备变压器） |

### 5. Carroll Transformer & Switchgear ｜ 简称 Carroll
| 字段 | 内容 |
|---|---|
| 公司全称 | Carroll Transformer & Switchgear |
| 国家 / 州省 / 城市 | 加拿大 / ON / Tillsonburg |
| 官网 | carrolltransformer.ca |
| **业务描述原句** | "a 'dedicated' **high voltage substation distribution** company, providing engineered-product solutions for the North American marketplace… We will utilize our network of global supply partners… delivering high quality products…"（https://carrolltransformer.ca/carroll_002.htm） |
| 高价值档 | ⭐（high voltage / substation） |
| 来源 | Surplus Record 变压器经销商目录（ON · Tillsonburg） |
| MX | ✅ 有（`carrolltransformer.ca` 自建） |
| 排重 | ✅ 未命中 |
| 排除判定 | 保留（高压变电站产品**分销**商；官网无 manufacturer / we manufacture / factory 字样） |

### 6. EcoTech NL Inc. ｜ 简称 EcoTech
| 字段 | 内容 |
|---|---|
| 公司全称 | EcoTech NL Inc. |
| 国家 / 州省 / 城市 | 加拿大 / NL / St. John's |
| 官网 | ecotechnl.ca |
| **业务描述原句** | "EcoTech NL Inc. located in St. John's, Newfoundland and Labrador specializes in **new and repurposing of electrical equipment** such as switchgear, motor control centers, panel boards, e-houses, and **transformers**, along with the associated engineering services."（https://www.ecotechnl.ca/） |
| 高价值档 | ⭐（transformer） |
| 来源 | 定向检索 `electrical supply Newfoundland` |
| MX | ✅ 有（`ecotechnl-ca.mail.protection.outlook.com`） |
| 排重 | ✅ 未命中 |
| 排除判定 | ⚠️ **保留但存疑** —— 主营「新设备供应 + 旧设备再制造/翻新」，含变压器；官网未出现 `manufacturer`/`we manufacture`/`our factory`/`in-house remanufacturing`/`coil rewinding` 任一 ⓪ 层触发词。**投递前建议复核是否触碰「翻新再售＝同业」红线。** |

### 7. Powerlogy ｜ 简称 Powerlogy
| 字段 | 内容 |
|---|---|
| 公司全称 | Powerlogy |
| 国家 / 州省 / 城市 | 加拿大 / ON / Mississauga |
| 官网 | powerlogy.ca |
| **业务描述原句** | "At Powerlogy, we pride ourselves on being both an **electrical supply wholesale destination** and a full-service electrical store."（https://powerlogy.ca/）／同页 "Bulk offerings for contractors, including panelboards, switchgear, and automation components"；品类页含 **Transformer**（https://powerlogy.ca/categories/transformer） |
| 高价值档 | ⭐（transformer 品类） |
| 来源 | 定向检索 `electrical wholesaler Mississauga Ontario` |
| MX | ✅ 有（`aspmx.l.google.com`） |
| 排重 | ✅ 未命中 |
| 排除判定 | 保留（本地电气批发/零售分销商，含变压器品类） |

### 8. O'Neil Electric Supply Ltd. ｜ 简称 O'Neil
| 字段 | 内容 |
|---|---|
| 公司全称 | O'Neil Electric Supply Ltd. |
| 国家 / 州省 / 城市 | 加拿大 / ON / Woodbridge（GTA；另 Scarborough、Cambridge） |
| 官网 | oneilelectric.com |
| **业务描述原句** | "O'Neil Electric Supply provides complete lighting, controls, and electrical solutions for projects of every size across Ontario. Our specialists work closely with developers, consultants, and contractors to review specifications, improve designs, **manage procurement**, and ensure timely delivery."（https://www.oneilelectric.com/）／"Proud Canadian Owned, Independent Wholesale Supplier of Premium Electrical Products in Ontario and the GTA for over 50 years." |
| 高价值档 | —（官网未出现四关键词） |
| 来源 | 定向检索 `electrical distributor Ontario independent` |
| MX | ✅ 有（`d235215a/b.ess.barracudanetworks.com`） |
| 排重 | ✅ 未命中 |
| 排除判定 | 保留（安省独立电气批发商） |

### 9. Argo International Corp ｜ 简称 Argo
| 字段 | 内容 |
|---|---|
| 公司全称 | Argo International Corp |
| 国家 / 州省 / 城市 | 加拿大 / ON / Burlington |
| 官网 | argointl.com |
| **业务描述原句** | "Argo International has been in business since 1952… has grown over the years to service a broad range of markets; Steel, Paper, **Utility**, Water/Waste Water, Mining, OEM's, Transit, Oil & Gas, Warehousing and Contractors."（https://www.argointl.com/）／产品页 "**Transformers** — Dry type, Machine Tool, Pad Mount, Oil filled, Auto transformer, and Control transformers"（https://www.argointl.com/transformers） |
| 高价值档 | ⭐（transformer） |
| 来源 | CTI 名录（Control & Distribution Transformers Suppliers, ON）+ 定向检索 |
| MX | ✅ 有（`argointl-com.mail.protection.outlook.com`） |
| 排重 | ✅ 未命中 |
| 排除判定 | 保留（1952 年创立的电气设备分销商，含变压器全品类） |

### 10. Lakeport Power Ltd. ｜ 简称 Lakeport
| 字段 | 内容 |
|---|---|
| 公司全称 | Lakeport Power Ltd. |
| 国家 / 州省 / 城市 | 加拿大 / ON / Colborne（+ BC 仓） |
| 官网 | lakeportpower.com |
| **业务描述原句** | "Lakeport Power Ltd. is an **electrical utility supply distributor**, servicing utilities and their contractors… we supply **brand new transformers from industry-leading manufacturers**, fabricated to your exact specifications. We also maintain a large inventory of new and reconditioned transformers…"（https://www.lakeportpower.com/about-us） |
| 高价值档 | ⭐（transformer / utility） |
| 来源 | Surplus Record 变压器经销商目录（ON · Colborne） |
| MX | ✅ 有（`lakeportpower.com` 自建） |
| 排重 | ✅ 未命中 |
| 排除判定 | ⚠️ **保留但存疑** —— 官网自述为**分销商**（供新变压器、买 surplus 批量再售），主体不是制造商；但同页含 "in-house transformer repair, reconditioning" ⇒ **接近 ⓪ 层「in-house remanufacturing」**（参照已排除的 Miami Transformers）。**建议人工定夺。** |

---

## 三、⚠️ 边界候选（⓪ 层存疑，未计入主名单）

| 公司 | 地区 | 官网 | 存疑原句 | 判定 |
|---|---|---|---|---|
| **Transcanada Transformers & Switchgear Inc.** | ON · Pickering | transcanadatransformers.com | "Our best-in-class products are **engineered** at the forefront of transformer and switchgear design… we offer **custom fabrication**…"（https://transcanadatransformers.com/about/） | 疑似「设计+定制装配」⇒ 可能为制造商，**暂不计入** |
| **3L2R Inc.** | ON · Cambridge | 3l2r.com | "We also **design and manufacture new custom switchboards** 4000A–800A for fast-track projects."（https://www.3l2r.com/） | 自述**制造**开关柜 ⇒ 触 ⓪ 层，**暂不计入** |

---

## 四、本轮剔除记录（查过但排除）

### 4.1 排重命中基线（已触达，直接丢）
| 公司 | 域 | 命中来源 |
|---|---|---|
| Rev-Amp Electrical Equipment | revampelectrical.com | batch7 |
| Distributeck Électrique | distributeck.com | v2 |
| Lenmark Industries | lenmark.com | batch8 |
| Besco | besco.qc.ca | batch7 |
| Lizco Sales & Rentals | lizcosales.com | batch7 |
| Daltco Electric | daltco.com | batch9 |
| Metro Systems | metrosystems.ca | batch9 |
| CT Sales | ctsales.ca | batch9 |
| McLoughlan Supplies | mcloughlansupplies.com | batch6 |
| CAYER Transformateurs | cayertransformateurs.com | batch7 |
| EWEL Electrical Wholesalers Edmonton | ewel.ca | v2 |
| Pro Energy | proenergy.ca | v2 |
| HUDCO | hudco.ca | batch7 |
| Boundary Electric | boundaryelectric.com | **成交客户** |
| Westgrid Power | westgridpower.ca | batch9 |
| Dubo Électrique | dubo.ca | batch8 |
| Province Electric Supply | province-electric.com | batch6 |
| Electrozad | electrozad.com | v2 |
| RS Breakers and Controls | rsbreakers.com | v2 |
| Renegade Electric Supply | renegadeelectricsupply.com | batch7 |
| Prairie Central Line Supply | pclsupply.ca | v2 |
| Evolt Electrical Supply | evolt.ca | batch7 |
| Independent Electric Supply (IES) | iesupply.ca / iesbuy.com | batch9 |
| Beaver Electrical Machinery | beaverelectrical.com | v2 |
| Electrical Wholesalers (Calgary) Ltd. | electricalwholesalers.com | batch8 |
| FEL — Fourniture Électrique Laurentienne | feldistribution.com | batch9 |
| EA Supply | easupply.ca | batch9 |
| Torbram Electric Supply | torbramelectric.com | batch6 |
| First Choice Electrical Supply | fcsupply.ca | batch8 |
| SIB Électrique | sibelectrique.com | batch8 |
| Lord Electrical Industrial Distributors | lordelectrical.com | batch9 |
| Canadian Industrial Electrical Supply | canadianindustrial.net | batch7 |

### 4.2 ⓪ 层反身排除（制造商 / 重绕 / 中国货源 / 连锁）
| 公司 | 地区 | 剔除依据（官网原句） |
|---|---|---|
| **Surplec** | QC · Sherbrooke | "**REMANUFACTURING & REPAIR**… **remanufactured** or new transformers"（https://www.surplec.com/en/）⇒ 触 ⓪ 层「in-house remanufacturing」 |
| **MGB Transformers / MGB Électrique** | QC · Saint-Pie | "**Winding, repair, rewinds** and modifications of power transformers."（mgbelectrique.com）⇒ 绕线重绕 |
| **Electric Power Inc. (EPI)** | ON · Mississauga | "leading **manufacturer** of full line standard and custom-engineered dry-type transformers"；团队含 coil winders ⇒ 制造商 |
| **Commercial Switchgear Limited (CSL)** | ON · Thornhill | "CSA approved **manufacturer**… All equipment is built and tested **in our factory**."（comswgr.com）⇒ 触 ⓪ 层 |
| **CES Transformers** | ON · Markham | "specialize in **manufacturing** all transformer products" ⇒ 制造商 |
| **Trydor Industries / Trydor Manufacturing** | BC · Vancouver | Trydor Manufacturing 归 **Rexel Utility**，自述 "**DESIGN AND MANUFACTURING** FOR THE HIGH VOLTAGE INDUSTRY"（rexelutility.ca）⇒ 制造商 + 连锁 |
| **SGE — Société Générale d'Électrotechnique** | QC | 集团含 **Transmag「MANUFACTURIER DE TRANSFORMATEURS DE PUISSANCE」**（groupeseg.ca）⇒ 集团内含变压器制造商 |
| **Canpower Global Inc.** | ON · Cambridge | "We source exclusively from certified Tier-1 factories worldwide — including **manufacturers in China, Taiwan, Turkey, Brazil, Indonesia**…" ⇒ 触「中国货源→北美」判据（排除规则 §2） |
| **Rockwill Canada** | — | 中国 Rockwill Electric 加拿大分支，主营中国产电力设备（rockwill.ca）⇒ 同源代理 |
| **Entogo** | 加拿大 | 《永久排除名录》§1.1（官网自称 transformer manufacturer） |
| **PTI Transformers / ETAC Service & Supply** | SK / MB | 《永久排除名录》§1.1（变压器制造商） |
| **Purcee Industrial Power** | AB | 《永久排除名录》§五（YAWEI 加拿大独家代理，禁用品牌） |
| **Trinity Power** | — | 《永久排除名录》§五 |
| **CED Ontario** | ON | 美国 CED（Consolidated Electrical Distributors）连锁，"opened its doors in California back in 1957… nearly 800 locations across America" ⇒ 连锁 |
| **McLoughlan Supplies** | NS/NB | 2021 年被 **Guillevin International** 收购（mcloughlansupplies.com）⇒ 连锁 |
| **Duke Electric Ltd** | ON · Hamilton | "…**rewind, rebuild**… your AC and DC motors and brakes…"（dukeelectric.com）⇒ 电机重绕修复厂，变压器仅附带 |
| **Hammond Power Solutions / Rex Power Magnetics / Moloney / Transformateurs Delta** | 多地 | CTI/IQS 名录标注为**变压器制造商** ⇒ 同业 |

### 4.3 类型不符 / 无法核实（纪律①不编造）
| 公司 | 地区 | 剔除依据 |
|---|---|---|
| **Westcana Electric Inc.** | BC | "Over 30 Years Of Reliable electrical **Contracting**" ⇒ 属 A 类承包商，非 B |
| **Collicutt Energy Services** | AB · Red Deer | "engines, generators, and rentals" ⇒ 发动机/发电机厂，非变压器分销 |
| **Landel Controls Ltd** | AB · Calgary | "Industrial Electronics & **Automation** Distributor"（传感器/机器人/运动控制）⇒ 与 MV/HV 变压器无关 |
| **Icon Electrical Ltd** | MB · Winnipeg | 官网自述为电气**承包商**（"industrial and institutional projects"）⇒ A 类 |
| **Brockway Enterprises** | NS | "Electrical **Independent Manufacturers Representative**" ⇒ 厂商代表（不持货、不采购） |
| **Henka Power** | — | 官网无任何实体地址（batch10 亦因此剔除）；"refurbished or new transformers, for sale and for rent"，实体与制造/进口身份均无法核实 ⇒ 丢 |
| **Canada Transformers (canadatransformers.com)** | — | 官网被 Cloudflare 拦截，取不到业务描述原句 ⇒ 未报 |
| **Transformer Source (transformersource.ca)** | — | 官网「Country Blocked」，取不到原句 ⇒ 未报 |
| **Surplus Assets (surplusassets.ca)** | — | 品类含 Transformer，但官网**无实体地址**，无法核实加拿大主体（batch10 同因剔除）⇒ 丢 |
| **Repower Electric Supply (repowerelectricsupply.ca)** | — | 排重干净，但官网无地址、无变压器、仅断路器 ⇒ 证据不足，丢 |
| **Crantex Electric Wholesale Inc.** | BC · Richmond | 仅第三方名录有登记，**找不到官网** ⇒ 无原句可引，未报 |
| **Aztec Electrical Supply** | ON · Concord | 官网 "Under Construction"，无业务描述原句 ⇒ 未报 |
| **Certified Mining and Construction** | SK · Saskatoon | 官网抓取失败，无法读原句 ⇒ 未报 |
| **R. L. Brews Ltd.** | AB · Calgary | 官网 JS 渲染，取不到业务描述原句（batch10 同因）⇒ 未报 |
| **Harris & Roome Supply** | NS/NL | 已并入 **Graybar Canada** ⇒ 连锁 |
| **Ontario Electrical Supply** | ON | 域名 `ontarioelectricalsupply.com` **无 MX 记录** ⇒ 收不了信，丢（排除规则 §6） |
| **Andarr Industries** | AB · Edmonton | `andarr.com` 为待售域名（For Sale），非该公司官网 ⇒ 丢 |

### 4.4 未采用来源说明
- **CTI 名录其余类别**（Electrical Apparatus & Equipment Wholesalers、Substations、Switchgear）：页面经 WebFetch/curl 多次超时或返回空，仅零星取到 Aztec / Argo / Transcanada 等；未能系统性拉全。
- **CanadaBuys 供应商库（换检索词）**：按 "transformer & switchgear" 命中 1 条中标公告，得标方为 **Wesco Distribution Canada**（连锁，已排除），无新独立主体。
- **省级批发商协会**：魁省 `electricite-plus.com` 分销商名录页持续超时，未取得；安省/BC 协会名录多为制造商或连锁。
- **EUDA / EASA / ThomasNet / GlobalSpec / IndustryNet / SupplyForce / AD**：按任务书，已失效，未触碰。

---

## 五、给下游环节的提示

1. 本批 **10 家全部为独立（非连锁）分销商/贸易商**，且均已过 MX。其中 **Argo International（ON·1952 年）** 与 **Northern Breaker Group（西部网络·常备变压器）** 契合度最高，建议优先交接。
2. **2 家 ⚠️ 存疑（EcoTech NL、Lakeport Power）** 与 **2 家边界（Transcanada、3L2R）** 请人工定夺后再决定是否进入挖人环节。
3. **地理分布严重不均**：ON 8 ／ AB 1 ／ NL 1 ／ **BC 0 ／ QC 0 ／ SK 0 ／ MB 0**。BC/QC 候选**几乎全部命中前批基线**（Westgrid、Dubo、Distributeck、Besco、CAYER、Renegade、Evolt、FEL、SIB、Électrimat…），非本批未努力，而是**来源池已被 batch6–10 吃干**。
4. 🔴 **强烈建议**：把本批验证过的「加拿大 B 类已触达」名单（见 §4.1 共 32 家）**补进 `_dedup_baseline`**（多数已在，但 Renegade / Westgrid / SIB / FEL / Evolt 等若未落数据行需补），并**将 Surplec / MGB / EPI / CSL / Trydor 登记进《永久排除名录》** —— 否则 batch12 必重犯。
