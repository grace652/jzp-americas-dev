# 项目长期备忘 — 海外买家背景调查项目

> 🚀 **项目状态：✅ 已正式启用（2026-09-23，用户确认）** —— 分层结构 + waterfall 升级（L-1 先锁人 + LinkedIn 双岗）全部就绪，新买家按升级后 SOP 执行。

## 项目性质

为高压电气设备出口业务做海外（美国、加拿大为主）B2B 买家背景调查，输出可直接交给「写开发信 agent」的标准字段交接单。

> 🔴 **主攻市场 = 美国 + 加拿大（2026-09-23 用户明确：「我主要开发美国和加拿大这两地区的客户」）。**
> 「L-1 岗位映射表」按北美设计，**不扩其他地区**。历史上有零星中东/俄罗斯/斯里兰卡买家，但非主攻方向。

- 🔴 **产出目录已改为 `project2/buyers/`（2026-09-23 分层改造后）** —— 交接单按批次存 `batch1_early_1-19/`、`batch2_mid_22-58/`、`batch3_late_59-72/`；专项进 `_series/`（含迪拜名片 + **`_waterfall升级调研_20260923.md`**），旧档进 `_archive/`。索引在 `project2/00_买家调查进度总索引.md`。**旧 `outputs/` 仅留指针 README，勿再往里写**。改造前全量备份在 `outputs_backup_20260923/`。
- **项目分层结构（6 个核心文件）**：`project2/README.md`（总纲/边界）、`00_core_rules.md`（合规边界+硬规则 **H1–H7**）、`01_execution_steps.md`（输入字段/5步执行/输出字段/交付归档）、`02_verified_channels_reference.md`（渠道+封锁清单）、`03_input_contract_from_project1.md`（输入契约）、`04_lessons_learned.md`（踩坑追加）。**开工先读 README + 03 + 00**。
- 🔴 **跨项目字段契约（2026-09-23 与项目3 合并对齐，方案C）**：
  - **输入**（=项目1 输出）：`公司名 | 国家/地区 | 行业 | 公司规模 | 产品线 | 来源链接 | 推导理由`
  - **输出**（=项目3 输入）：核心 9 字段 `公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示(如有)` + **扩展段「补充信息」**（标准字段明细/**联系人含 still_here 四栏**/**邮箱 A/B/C 分档**/买家类型/需求品类/电压认证/采购信号/钩子/开发信建议/矛盾点/缺口清单/一句话画像/**渠道覆盖 L-1、L0–L7**）
  - 🔴 **9 字段名与顺序锁定不动**（2026-09-23 waterfall 升级时**未改字段名**，只改「填写要求」文字与扩展段，故不构成破坏性契约变更）
  - 🔴 **变更前必须在项目3 同步**（项目3 契约文件：`项目：开发信.../project3/05_input_contract_from_project2.md`）
- **文件分层纪律**：00/01 改动前须列改动点等用户确认；02 自由增删；03 随项目1 同步；04 持续追加
- 已完成买家：1–72（27 Galle、28 Romar、29 Hillfort、30 MVA、31 T&N、32 Rexel、33 Tri-State、34 VIE、35 Amped、36 PLS、37 Irby、38 Brownstown、39 OneSource、40 KBS、41 TES、42 R.A. Electrical、43 Ross Morrison、44 K2 Electric、45 GEC、46 Fletcher、47 Techline、48 Sunbelt、49 Valley、50 Border、51 PSS、52 Westmoreland、53 Iconic、54 Dana、55 GRIDLINK、56 Kirby、57 BV Electric、58 Birmingham、62 Everlast、67 AECI、68 UUS、70 WUES、71 CEEUS；59 Texas/60 Stewart/61 Priester/63 Rising/64 Tryggr/65 Amps/66 Fullford/69 RESCO为另一对话；买家1已重跑增补）
- 🔴 **L-1/still_here/A-B-C 只对新买家生效**（2026-09-23 用户拍板）—— 旧买家 1–72 **不回填** L-1 覆盖情况；索引头部已加说明
- 方法论已沉淀为 skill：`~/.workbuddy-ai/skills/b2b-buyer-research/SKILL.md`（**每次新对话开工前必读 SKILL.md + `references/01-methods.md` §2、§5.9 + `references/03-traps.md` #96–#103**）
- 公司产品知识库：`~/.workbuddy-ai/skills/jzp-company-knowledge/SKILL.md`（JZP 节奏变压器：**配电是主力，小变压器也做，主变也做**；本对话不写开发信，只做背调，钩子落点必须在真有产品上）

## 🔴 用户硬性要求（必须遵守）

1. **绝不编造** —— 没找到的信息一律写"未获取"，并在"信息缺口清单"中列明。
2. 🔴 **产出必须落盘成 `.md` 文件（2026-09-23 新增，硬规则 H7）** —— 每个买家一份独立文件，归档 `project2/buyers/batchN_*/`；**对话里只给简短摘要 + 文件路径**并把文件呈现给用户，**不刷全文**。用户原话：「我需要项目的输出结果直接给一个 md 文件的报告，就和之前一样」。
3. **不是仅仅浏览官网** —— 必须覆盖官网、商业名录、公司注册库、社媒、DNS、联邦采购数据等多渠道。
4. **交付格式固定** —— 按用户给定的标准字段输出（公司全称/国家城市/联系人职位/邮箱/LinkedIn 网站/买家类型/需求品类/触达来源/为什么找他/电压频率认证/采购信号），并额外附「补充信息」章节提升开发信转化率。
5. **区分「已验证」与「未获取」** —— 每个关键信息标注来源；单一来源必须显式标注"未经第二方印证"。
6. **用户提供的既有信息也可能有错** —— 必须独立核实并**主动指出冲突**（已多次发生：买家 5 的 ZoomInfo 人名污染、买家 8 的 steve@ 邮箱无来源、买家 9 的 Chris Dodd 头衔错误、买家 10 的 Kenneth Walters 不在官网、买家 11 的 jmoore@/emoore@ 来源不实）。
7. 🔴 **开工前必须先查重（2026-09-17 新增）** —— 用户原话：「之后我给你发的有做过的就直接告诉我，我有时候不记得搞错了。」
   - **每次收到新买家，第一步先 `ls buyers/` 各批次查重**
   - 若已做过 → **立即直接告知用户**，给出已完成文件路径与关键结论摘要，**不要重复劳动**
   - 若文件已存在但结论有误 → **先 Read 全文，做增量更新，绝不覆盖重写**，并在文末加「📌 补充更新」章节标注新增/更正
8. 🔴 **必须用公司地址反查本地名录/黄页（2026-09-18 新增）** —— 用户原话：「通过公司的地址去找当地企业名录和黄页等等信息，尽量去收本地的信息。」
   - **标准动作**：拿到公司地址后，用 `"完整地址" + 黄页/名录关键词` 反查本地信息
   - **必查项**：Yahoo Local / Yelp / AllPages / Superpages / Manta / BBB / 本地商会 / 本地公用事业承包商名单 / 州级特种库（如 Oregon BCD）/ 同址注册集群（opencorpdata 同址检索）
   - **价值**：① 一线技师姓名与口碑（开发信素材）② 黄页类目（佐证业务属性）③ 本地公用事业入围（背书）④ 同址多 LLC（发现业务拆分/整合信号）⑤ GPS 与邮编补全
   - **纪律**：聚合类名录（如 whereorg）与官方源冲突时**以官方源为准**，聚合数据标存疑
9. 🔴 **找联系人/邮箱必须走 Waterfall L-1 → L0–L7，禁止只抓官网（2026-09-21 新增，2026-09-23 升级）** —— 用户原话：之前的 skill 让 agent 特别懒惰，只在官网上爬邮箱。
   - 🔴🔴 **核心顺序：先锁「人」，再找「邮箱」**（2026-09-23 最大改动）—— 链条 = `域名 → 公司 → 正确的人 → 已验证邮箱`，**只拿到 `info@` 不算完成**。用户原话：「有时候整个项目只给我官网的 info@ 类邮箱，这种邮箱价值很低」。
   - **强制顺序**：
     - 🔥 **【新增】L-1 先锁具名决策人**（岗位映射表：买家类型 × 公司规模 → 角色词；**适用地区限美加**；公司页 Employees 名单；4 组 query；组织图反推。通关 = ≥1 份「姓名+职能+在职证据+个人页 URL」）
     - **L0** 官网全量（角色邮箱/页脚/PDF/`og:description`/Cloudflare `data-cfemail` 解码）
     - **L1** 政府一手（FMCSA/SAM/州执照qualifier/投标文件/BC Bid，政府邮箱 > 官网通用）
     - **L2** 命名规则+DNS（MX/TXT，有样本才可推演；**免费第一跳≈1/3 命中**）
     - **L3** B2B库交叉（两库互证不算印证，无一手源的人名判幻觉）
     - **L4** 社媒协会（FB/**LinkedIn 第二岗：still_here 核验**/ABC·NECA·IBEW名录）
     - **L5** 本地黄页同址（见第7条）→ **L6** 电话表单兜底（点名转交）→ **L7** 付费API预留（无API时标注未启用）
   - 🔴 **【强制】still_here 在职核验**（任何邮箱进主送前必做）—— B2B 联系人**每年 18–20% 换工作**；衰减 2.1%/月；37.3% 邮箱 12 个月内失效。核验四栏：`在职称谓 / 任职时长 / 最近活跃 / 离职风险`；**任职 <30 天 = 新入职**（改走「恭喜」角度，邮箱格式可能不同）；current 公司 ≠ 目标公司 → **离职风险 🔴，地址作废**。
   - 🔴 **【硬规则 H6】角色邮箱升级三步** —— 唯一收获是 `info@`/`sales@` 时不得直接交付：① 挖职能邮箱（`Supplier@`/`Owners@`/`Estimating@`/`Purchasing@`）② 从该域名真实回信反推命名规则 ③ 免费先试推演；**三步全失败必须显式写「仅取得角色邮箱，未取得决策人直邮」并列为本条风险**。
   - **邮箱 A/B/C 三档**：A 具名决策人（✅主送）/ B 角色邮箱（⚠️**仅点名转交**）/ C 免费邮箱或 catch-all（🔴需电话确认）。**字段名与顺序不变**（不破坏项目3 契约）。
   - **推演可执行阶梯**：`{first}@ → {first}.{last}@ → {last}@ → {fi}{last}@ → {fi}{li}@`，逐个实测、不批量盲发。
   - **置信度**：政府/官网明文+2，第二独立源+2，样本印证+1，B2B单源+1，纯推演0，catch-all −2；**≥4分才可主送，≤2分备选+电话验证**
   - **停止规则**：① 拿到具名决策人直邮（≥4分）可停 L3–L5（L1 已查）；② 仅有角色邮箱时 **L-1 至 L6 全走完 + 必跑升级三步**
   - **交付**：交接单邮箱章节必须附 **覆盖表（L-1、L0–L7 每行 ✅/⚠️/❌ + 一句话）**，缺一行即自检不通过
   - **LinkedIn 双岗（2026-09-23 升级）** —— ① **L-1 第一岗（找人，主引擎）**：公司页 JSON-LD + Employees 名单 + 4 组 query + 组织图反推 ② **L4 第二岗（核验）**：头衔核验 + still_here + 协会交叉。**Boolean 纪律**：运算符须大写、**只能用直引号**（弯引号**静默失败**）、免费版 **OR ≤3–4 个**、只有 3 字段吃 Boolean、**语法错不报错会静默改写搜索**。Sales Navigator 过滤器**本环境未订阅，不要写进步骤**。
   - **从个人页取信免费四步**：Contact info 标签（≈30%）→ About 区 Ctrl+F 搜 `at`/`dot` → **Google X-Ray**（`site:linkedin.com/in/ "人名" "@域名"`）→ 推演+验证。
   - 详见 skill：`references/01-methods.md` §2（含 §2.5–§2.9）、§5.9 + `references/03-traps.md` #96–#103

## 🔴 交付纪律（2026-09-17 新增，因实际事故确立）

**推演出来的邮箱永远不能作为「首选主送」。**

- **事故背景**：买家 10 中，我用「三库一致 + 一个真实样本印证」推演出 `ifrailey@r-ecci.com`，用户实测**不存在**。
- **规则**：
  1. **主送方案必须用已确认可用的地址**（官网 / Facebook / 官方文件上真实出现的邮箱，如 `info@`）。
  2. **推演地址只能列为备选**，并显著标注"未验证"。
  3. **验证"不存在"前先排除工具假阴性** —— 用同一工具测一个已知真实的地址（如 `info@`）；若 `info@` 也报不存在，说明工具对该域名不可用。
  4. **B2B 库的百分比不是保证**（"75% 采用率"意味着 25% 的人不符合）；**新入职员工尤其可能使用不同格式**。

## 常用渠道速查

| 用途 | 渠道 |
|---|---|
| 官网抓取 | `curl -sL -A "<浏览器UA>"`（WebFetch 被拒时） |
| WordPress 全站清单 | `/<domain>/wp-json/wp/v2/pages?per_page=100&_fields=id,slug,title,date,modified` |
| LinkedIn 公司页 JSON-LD | 拿**精确员工数**、地址、描述（个人页常 HTTP 999）—— **L-1 找人的主入口** |
| LinkedIn 个人页取信（免费四步） | ① Contact info 标签（≈30%）② About 区 Ctrl+F 搜 `at`/`dot` ③ **Google X-Ray**：`site:linkedin.com/in/ "人名" "@域名"` ④ 推演+验证 |
| LinkedIn 在职核验 | 看个人页 current 公司 + 任职时长 + 最近活跃（🔴 主送前必做） |
| 加拿大注册库 | `opengovca.com/corporation/<ID>`、`/director/<name>` |
| 美国 SAM.gov | `opengovus.com/sam-entity/<UEI>`（拿 **CAGE 码、PSC 采购品类代码**） |
| 美国联邦合同 | `POST api.usaspending.gov/api/v2/search/spending_by_award/`（拿**项目级明细含描述**） |
| 美国业主名单 | SBA `search.certifications.sba.gov/profile/<UEI>/<CAGE>`（CloudFront 封锁，**用 Google 摘要取 "Current Principals"**） |
| WV 州务卿（可直接 curl） | `apps.sos.wv.gov/business/corporations/organization.aspx?org=<ID>`（**org ID 用 Google 搜出来**） |
| 州承包商执照 | `contractors.agentlookups.ai`（Plumbline）、`opengovwa.com`、`ccblookup.com`（Oregon） |
| 公用事业合格承包商名单 | 搜 `<电力公司名> "Qualified Contractors" filetype:pdf`（**含手机直拨号 + 同业竞品**） |
| 邮箱格式规则 | ContactOut / Seamless.AI / LeadIQ / Prospeo 的 "Email Format" 板块 |
| 邮件网关识别 | 查 MX：`*.ess.barracudanetworks.com`=Barracuda、`*.ppe-hosted.com`=Proofpoint、`*.mimecast.com`=Mimecast |

## 环境限制（已知）

- **SMTP 实时验证不可行**（25 端口连接后 banner 为空；Microsoft 365 / Google Workspace 不响应 RCPT TO）
- **Alabama SOS SSL 握手失败**；Alaska 官方库连接被拦；Bizapedia / ltddir / alaskacompanydir 等 Cloudflare 封禁 → **改用 Google 搜索摘要取关键句**
- **WA L&I 官方 API 需会话/API key**；WV 承包商执照库需 NetScaler 令牌
- **Facebook 内容需登录**（含 mbasic）→ 只能确认页面存在
- **LinkedIn 个人页常 HTTP 999/451** → 公司页可抓
- **PDF 提取**需先装 pypdf（环境无 pdftotext）；**Read 工具无法读 PDF**，且需 Windows 路径
- **data.wa.gov Socrata API 连接被拦**
