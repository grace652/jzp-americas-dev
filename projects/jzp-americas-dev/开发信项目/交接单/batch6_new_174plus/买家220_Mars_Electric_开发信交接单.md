# 【买家 220】开发信交接单 — Mars Electric Co.（Mayfield Village, OH）

> 采集日期：2026-09-29 / 来源：batch6 名单（目标客户清单-batch6.csv 序 47，OH 分销商）/ 一句话结论：东北俄亥俄独立电气+HVAC 分销商（1952 创立，12 分支，家族 Doris 持有），⓪层 PASS（批发分销，非制造商）；采购一把手 Neil Patel（Sr. Director, Purchasing）在职已核，**但邮箱域 `mars-electric.com` 为 catch-all ⇒ 具名直邮无法验证**，主送降级为 B 档角色邮箱 + 点名转交。

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示(如有)
Mars Electric Co. | Neil Patel | Sr. Director, Purchasing（采购高级总监） | 无具名直邮（B 档：info@mars-electric.com 点名转交 Neil Patel） | 未找到（具名）；B 档角色邮箱域为 catch-all，SMTP 不可验证 | linkedin.com/in/neil-patel-70449029（个人页）｜linkedin.com/company/mars-electric-co | 1952 年创立，总部 6655 Beta Dr, Mayfield Village OH 44143；东北俄亥俄 12 家分支，约 190–200 人；电气 + HVAC 双线批发分销；家族持有（CEO Fran Doris，President Michael/Mark Doris）；12 万平方英尺中央仓（2017 启用） | 官网(marselectric.com)+PR.com 新闻稿+ContactOut/Prospeo/RocketReach 旁证+LinkedIn 个人页+SMTP 探测 | ⚠️ 邮箱域 mars-electric.com 为 catch-all → 所有地址一律 250，**禁止据 SMTP 判存在**；无第一方明文邮箱 |
```

## 二、补充信息（扩展段）

### 标准字段明细
- 国家+城市：美国 Ohio — Mayfield Village（总部，Cleveland 都会区）+ 东北俄亥俄 12 家分支
- 详细地址：6655 Beta Drive, Mayfield Village, OH 44143（官网自述总部；Google/PR 稿另见 777 Village Trail 仓库址）
- 电话：(440) 946-2250（官网/名录一致）；800-288-6277（futern 旁证）
- LinkedIn：个人 `linkedin.com/in/neil-patel-70449029`；公司页 `linkedin.com/company/mars-electric-co`
- 网站：**marselectric.com**（官网）；**mars-electric.com**（邮件域，跳转同一站）
- 成立日：**1952**（ContactOut / futern / Glassdoor 三源一致）
- 规模：约 190–200 人（ContactOut 192 / RocketReach 177 / futern 51–200）；12 家分支
- 营收：未获取（ContactOut / Prospeo 估约 $10M，**为第三方估算，勿引用**）
- NAICS：**423610 / 42（批发）** —— ContactOut 归 "Wholesale"，Prospeo 标 NAICS 42，naicslist 标 "Electrical Apparatus & Equipment, Wiring Supplies" ⇒ **分销，非制造**
- 身份：官网自述 *"leading independent, wholesale distributor of lighting, gear, and electrical supplies"* + *"independent electrical and HVAC distributor"*（双线：电气 + HVAC）
- 家族/股权：家族持有（Glassdoor "CEO: Fran Doris"；futern 列 Michael Doris / Mark Doris 为 President）

### 联系人（含 still_here 在职核验）
| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| **Neil Patel**（主送点名对象） | 采购一把手 | Sr. Director, Purchasing | ContactOut 标 "1 year"（≈2025 起任现职） | LinkedIn 现职 "Sr. Director, Purchasing at Mars Electric Co."（Cleveland）；RocketReach / ContactOut / Prospeo 三库现职一致 | 低 | linkedin.com/in/neil-patel-70449029 |
| Fran Doris | 公司最高决策（备选，不发） | CEO | 多年（家族） | Glassdoor 员工评价页现职 "CEO: Fran Doris"；2017 PR 稿以 CEO 身份发言 | 低 | 未取 |
| Michael Doris | 总裁（备选，不发） | President | 未获取 | RocketReach / futern 现职 | 低 | 未取 |
| Michael Mammone | 销售一把手（备选，不发） | Vice President of Sales | 8 年（ContactOut） | 2017 PR 稿 + RocketReach 现职 | 低 | 未取 |

> 选人说明：**Neil Patel 是唯一命中的「采购岗」**（Sr. Director, Purchasing），按优先级（采购岗 > 国际销售 > 品类经理 > 老板/Owner）**优于 CEO/President**，故定为主送点名对象。其余为备选，**不并发发送**。
> ⚠️ **同名区分**：`Neil Patel` 是极常见姓名 —— 本单指 **Cleveland 的 Neil Patel，linkedin.com/in/neil-patel-70449029，现职 Mars Electric Co.**，勿与 LinkedIn 上其他同名 Neil Patel（如 Greater Cleveland 的另一 Neil Patel linkedin.com/in/neil-patel-43a2a8）混淆。

### 邮箱分档（A/B/C）
- **A 档（具名）**：**无** —— 具名邮箱无法验证（域为 catch-all）。
- **B 档（角色邮箱，主送，仅点名转交）**：`info@mars-electric.com`（或 `info@marselectric.com`，同租户）
  - ⚠️ **该域为 catch-all**（SMTP 实测：控制 `info@mars-electric.com` = 250，**随机地址 `zzz_nonexistent_probe_9987@` 亦 = 250**）⇒ **任何地址都返回 250，SMTP 探测对本域完全无效**。
  - ⇒ **无法确认 info@ 本身是否存在**；按规则 catch-all 域**严格禁止使用非第一方来源地址**（H2）。本单未取得任何第一方明文邮箱。
- **推演地址（🔴 不可作主送，仅备选）**：`npatel@mars-electric.com`
  - 依据：ContactOut/Prospeo/futern 三库一致给出本域规则 `{first_initial}{last}@mars-electric.com`（采用率 80% / 61.6% / 96.9%）。
  - 🔴 但域为 catch-all，**推演地址永远返回 250，不会被证伪** → 属「推演不可主送」（H4 待验证）。
- **H6 声明**：⚠️ **适用** —— 升级三步：① 职能邮箱（`purchasing@mars-electric.com` 等）在 catch-all 域同样恒 250，**无区分力、不可采信**；② 无该域真实回信样本；③ 推演被 catch-all 规则禁止作主送。⇒ **仅取得角色邮箱入口，未取得决策人直邮，列为本条风险**。

### 我为什么找他
- Mars 是**双线分销商**（电气 + HVAC），且官网明确经营 **Specialty Wire & Cable / Power Distribution Equipment / Electrical Gear** 等品类（官网 categories 与 info 子域落地页），并自建 12 万平方英尺中央仓（2017 启用）—— **是备货型分销商，配电类设备是其常态品类**。
- **Neil Patel 的头衔是 Sr. Director, Purchasing**（采购一把手，ContactOut 标 2025 年起任）——在 190 人规模的分销商里，这是能拍板新增一条变压器供应线的岗位；且其 LinkedIn 自述 "A Supply Chain Professional with background in Operational Excellence"，是**专业采购背景**，能听懂供应商能力边界。

### 买家类型 / 需求品类
- 买家类型：🔥🔥 **A 型 —— 电气 + HVAC 分销商**（独立批发，12 分支，NAICS 423610）
- 需求品类（带结论态）：
  - `三相美变（UL E541627，可直供）` —— 工业/商业配电与 gear 品类主谈
  - `单相柱上变（认证在办，条件切入）` —— 仅户外/临时供电场景条件性提及
  - ⛔ 不推：**干变（美国不匹配：无 UL）** —— 对美国客户一律不谈干变

### 电压·频率·认证要求
- 电压：未获取（官网未公开常做电压等级，**需电话确认**）
- 频率：**60 Hz**（美国）
- 认证：美国市场需 **UL**；我方三相液浸配电变持 UL **E541627**

### 采购信号
- 12 家分支 + 12 万平方英尺中央仓 → 备货型分销商，SKU 与品类扩张是常态
- 在招岗位含 **Pricing Manager**（futern 抓取的招聘列表）→ 采购/定价职能活跃，正在强化
- 家族持有 + 1952 至今 → 长线关系导向
- 品类含 Power Distribution Equipment / Electrical Gear → 配电变压器在其品类版图内

### 可利用的钩子（按强度排序）
1. **采购一把手 Neil Patel + 其自述 Supply Chain 专业背景**（最强）→ 可对「供应能力/交期可靠性/认证」专业语言开场
2. **12 分支 + 12 万平方英尺中央仓** → 备货型分销商，稳定供货是其核心诉求
3. **电气 + HVAC 双线 + gear 品类** → 配电变压器可切入 gear/配电品类
4. **家族 1952 老店** → 长线培育

### 开发信建议
- **收件人策略**：⚠️ **无 A 档具名邮箱**。**首选路径：电话 (440) 946-2250 点名 Neil Patel（Sr. Director, Purchasing）索取直邮**；若走邮件，只能发 **B 档 `info@mars-electric.com` 并首句请求转交 Neil Patel**。**一家只发 1 人**。
- **送达配置**：邮箱域 = **mars-electric.com**（非官网域 marselectric.com，注意别写错域）；MX = Microsoft 365。catch-all 域**无法预验证**，只能靠**退信（bounce）**判断可达性。
- **发送时段**：克利夫兰（ET，UTC-5/-4）周二–周四 上午 09:00–11:00 ≈ 北京时间 21:00–23:00。
- **附件建议**：首封不带供货名录/PDF；可提及 UL 证书号与容量区间。
- ⛔ 首封红线：不写交期数字、不写价格词、不提 CSA Certified / SASO / SONCAP / YAWEI、不谈干变。

### ⚠️ 矛盾点与风险提示
- 🔴 **邮箱域为 catch-all** —— 具名地址（含 `npatel@`）无法验证，**禁止主送推演地址**（H2）；角色邮箱 info@ 亦无法确认存在。这是本单最大短板。
- ⚠️ **同名主体陷阱（3 个）**：
  1. **Mars Electric（PA）** —— `marselectricpa.com`，宾州**住宅电气承包**，与本案无关；
  2. **Suzhou Mars Electric Appliance Co., Ltd.（中国苏州）** —— 家用电器，与本案无关；
  3. **Mars, Inc.（糖果/宠物食品巨头）** —— 官网 `mars.com`、招聘域 `careers.mars.com`，**LinkedIn/搜索极易误命中**（其 "Sr. Director, Purchasing at Mars" 类结果不是本案）。
  ⇒ 本案主体唯一指向 **OH Mayfield Village 的 Mars Electric Co.（marselectric.com / mars-electric.com）**。
- ⚠️ Neil Patel 为**高频同名**，务必按个人页 ID（neil-patel-70449029）核对。
- ⚠️ 招聘列表里出现 `Pricing Manager` 岗位 —— 未获取是否已招到、是否影响采购分工，**需电话确认**。

### 信息缺口清单（请勿编造）
- **具名邮箱**：未找到（catch-all 域 + 无第一方明文）
- Neil Patel 的**任职起止精确日期**：未获取（ContactOut 标 "1 year" 为估算）
- 公司**常用变压器容量 / 电压等级 / 现有品牌**：未获取（需电话确认）
- **年营收 / 精确员工数**：未获取（第三方估算勿引用）
- **采购团队其他成员 / 供应商准入对接人**：未获取
- **邮箱可投递性**：未实测（catch-all 无法预验证）

### 一句话画像
东北俄亥俄 1952 年创立的家族电气+HVAC 分销商（12 分支、12 万尺中央仓），采购一把手 Neil Patel 在职确凿、但邮箱域是 catch-all 拿不到可验证直邮 —— 先电话点名，再走 info@ 转交。

### 渠道覆盖清单（L-1、L0–L7）
| 层 | 结果 | 一句话 |
|---|---|---|
| L-1 锁人 | ✅ | 锁到采购一把手 Neil Patel（LinkedIn 现职）+ CEO/President/VP Sales 全列 |
| L0 官网 | ⚠️ | About/Categories/Locations 全取；Contact 仅表单，**无任何明文邮箱** |
| L1 政府一手 | ⚠️ | NAICS 423610/42 经第三方库核（非州务卿原件）；OH SOS 未查 |
| L2 命名+DNS | ⚠️ | MX=M365；**catch-all → SMTP 无效**；命名规则 `{first_initial}{last}` 仅三库推断 |
| L3 B2B 库 | ⚠️ | ContactOut / Prospeo / RocketReach / futern / LeadIQ 旁证（**不作印证主力**） |
| L4 社媒协会 | ✅ | LinkedIn 个人页现职 + 公司页；无 NAED/NECA 具名邮箱产出 |
| L5 黄页同址 | ⚠️ | Glassdoor / findglocal / originalyellow 同址旁证 |
| L6 电话表单 | ✅ | 总机 (440) 946-2250 + 表单（**未拨打，本单主要依赖此路径**） |
| L7 付费 | ❌ | 未启用 |

---

- 发信资格：⚠️ **条件通过 / 实质拦截**（第 1 条：**具名邮箱未验证**）—— 无 A 档直邮，仅 B 档角色邮箱且域为 catch-all ⇒ **建议先电话确认，再决定是否发 info@**
- 邮箱档位：**B（角色邮箱，仅点名转交）；A 档无**
- ⓪ 层反身排除：**PASS** —— 官网/PR 稿自述 *"leading independent, wholesale distributor of lighting, gear, and electrical supplies"*、*"independent electrical and HVAC distributor"*，ContactOut 归 "Wholesale"、NAICS 42/423610 ⇒ **分销商**；无 `we manufacture` / `our factory` / `OEM` 表述，**无代理 YAWEI 等禁用品牌** ⇒ 分销商客户，非竞品。
