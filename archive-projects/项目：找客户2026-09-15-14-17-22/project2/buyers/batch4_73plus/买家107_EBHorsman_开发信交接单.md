# 【买家 107】开发信交接单 — E.B. Horsman & Son

> 采集日期：2026-09-23 / 来源：项目1候选输入（公司名+Surrey地址+125年/22网点/22000SKU线索+官网/BBB）/ 已验证与未获取声明见各字段
> 一句话结论：西加最大独立家族+员工持股分销（125年，400+人，22网点三省，DC 10.3万平方英尺22000SKU），35年采购VP+11年买手双锁定但直邮无一手印证，主送走总机点名。

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示(如有)
E.B. Horsman & Son | Todd Taverner（主）/ Loreena Horrobin（执行） | VP Purchasing & Inventory / Purchaser | 无直邮（B档：总机778-545-9916+888-467-7626点名转交；ar@备选；推演禁主送） | 未找到(A档) | 公司 linkedin.com/company/ebhorsman；个人仅第三方快照+TheOrg（直链见缺口） | 加拿大BC Surrey，1900年，五代家族+员工持股，400+人，22网点BC/AB/SK，DC 22,000 SKU 99.95%拣准，600+供应商 | 官网全站(history/blogs/分支PDF)+LinkedIn公司页+DNS+格式库三源 | 员工400vs350两口径；推演三库一致仍禁主送；M365+DMARC quarantine
```

## 二、补充信息（扩展段）

### 标准字段明细
- 国家+城市：加拿大 BC Surrey（总部+DC）；Port Kells第二总部（Langley）；网点BC/AB/SK三省22–23个
- 详细地址：19295 25th Ave, Surrey, BC V3Z 3X1（官网+分支PDF+用户一致；2011年迁入，DC 103,000平方英尺；54总部+25 DC人员）
- 电话：778-545-9916（总部）；免费888-467-7626；传真778-545-3099；Surrey门店604-596-7111；Port Kells 778-705-0015
- LinkedIn：公司 linkedin.com/company/ebhorsman（150–200档，1900；2025-02招Purchaser帖在职实证）
- 网站：ebhorsman.com（Magento电商+在线报价；品类含Transformers/Control Transformers/Current Transformers/MV fuses/Generator Panels/Panels）
- 成立：1900 Moosomin五金 → 1907 Vancouver → 1925电气批发 → 2025年125周年（官网编年史）
- 员工：400+（2025官博）/ 350+（Albrite页）→ 用400+注年份；营收聚合$10–20M（过低，废弃不用）
- 身份：家族+员工持股独立（80年代衰退唯一存活家族分销）；Albrite Lighting/Intec/MCL旗下；EFC语境（Tim Horsman董事见Wesco案EFC名单）
- DC：22,000 SKU常备，99.953%拣准，WMS，每日发全BC分支

### 联系人（含 still_here 在职核验）
| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| Todd Taverner | VP Purchasing & Inventory，采购总决策（主送点名） | VP | 1991-07至今（~35年） | 中：快照+TheOrg现任 | 低 | exa.ai/library/person/t4f83m33dlq + theorg.com/org-chart/todd-taverner |
| Loreena Horrobin | Purchaser，采购执行 | Purchaser | 2015-05至今（~11年） | 中：快照Current | 低 | exa.ai/library/person/sq8z3lkckvz |
| Luke Hoa | Purchasing Assistant HQ，采购助理 | Assistant | 2023-02至今 | 中：快照Current | 低 | exa快照 |
| Tim Horsman | President & CEO五代（Surrey店起步） | CEO | 2011至今 | 高：125周年各帖 | 低，不作首收件 | 官网 |
| Sumeet Sodhi / Shane Smith | Regional VP / Surrey Dist Mgr，分支口 | RVP/DM | 现任 | 中：分支PDF 2026-09 | 低，不作首收件 | 分支PDF |
| Kyle Irving | Distribution Manager DC（10年内部晋升+P.LOG在考） | DC Mgr | 10年+ | 中：官博2025-05 | 低，不作首收件 | 官博 |

### 邮箱分档（A/B/C）
- **A档（具名）**：无。格式三库92–99%一致（LeadIQ 95 / RocketReach 92.3 / AeroLeads 99.41 FLast）但**纯B2B互证=H5作废** → `ttaverner@`/`lhorrobin@`仅2分备选，**禁主送**。
- **B档（电话+角色）**：总机778-545-9916 + 免费888-467-7626点名Todd/Loreena；`ar@ebhorsman.com`（官网结账问题联系，AR部门，B档备选转交）。
- H6声明：仅电话/角色入口；升级三步：①职能邮箱即ar（非采购，备选）；②无回信样本；③三库一致仍停手（买家10事故：75%都会翻车，何况无样本）。

### 我为什么找他
- 用户给的4项（125年独立/员工持股/22网点/DC 22000SKU）全部命中且超配：2025年125周年三帖+“largest independent employee & family-owned Western Canada”原话；22网点三省+Port Kells第二总部；DC 22,000 SKU+99.953%+WMS官博数据——是西加独立分销最大公开入口（Sonepar系Gescan之外最优独立标的，BC承包商VIE/K2/Mott/BV的共同上游）。

### 买家类型 / 需求品类
- 买家类型：🔥🔥 **分销商（西加独立龙头，电商+技术专家+Major Projects三通道）**
- 需求品类（带结论态）：
  - `三相美变（UL E541627，可直供）` — 22网点备货+vendor-managed主谈
  - `干变（加拿大可谈，built to CSA标准）` — 商业工业备选
  - `主变/变电站变（产能可覆盖，UL区间外，需人工确认）` — Major Projects口（Port Kells）项目制
  - 注意：600+供应商墙厚 → 谈**缺口规格+DC直发+分支补货**，附125年家族共鸣

### 电压·频率·认证要求
- 电压：未定位具体kV（Control/CT/MV fuse/generator panels品类齐；首轮问Todd常用变压器段）
- 频率：60Hz（加拿大）
- 认证：`built to CSA/IEEE标准`；美变亮E541627

### 采购信号
- 125周年+Grande Prairie新店COMING SOON → 扩张备货
- 2025-02招Purchaser（South Surrey）→ 采购团队扩编，进货增量
- Port Kells第二总部2023（Lighting/Albrite/Datacom/PAC/Major Projects/eCommerce）→ 项目型采购集中化
- 技术专家（报价/选型/审计/培训/盘柜改装）→ 吃submittals那套

### 开发信建议
- 收件人：电话先行（总机点名Todd，Loreena备选），拿到直邮再发；ar@抄送无效不单独发
- 开场：125年+五代家族+80年代唯一存活+DC 99.95%（做过功课感），点名Transformers品类页
- 附件：不带名录；UL号+容量区间
- 发送时段：温哥华（PT）周二–周四上午 = 北京时间24–26点
- 送达：M365专线+HubSpot源+SPF `-all`硬+DMARC **quarantine** → 三件套须齐；首封纯文本

### ⚠️ 矛盾点与风险提示
- 员工：400+（2025）vs 350+（Albrite页）→ 用400+注年份
- 网点：22 vs 23+ → 用22（三省PDF口径）注+Port Kells
- 推演三库一致≠可主送（H5+H2，买家10事故）
- 个人页直链未取（仅快照+TheOrg）
- DMARC quarantine → 发件域自查先行

### 信息缺口清单（请勿编造）
- 具名直邮：未找到
- 个人LinkedIn直链：未取
- 年营收：未获取（聚合值废弃）
- 常用变压器容量/品牌：未获取

### 一句话画像
西加125年的家族分销常青树——80年代同行死光就剩它，DC十万尺两万料，找干了35年的Todd电话开门。

### 渠道覆盖清单（L-1、L0–L7）
| 层 | 结果 | 一句话 |
|---|---|---|
| L-1 锁人 | ✅ | 采购VP35年+买手11年+助理全锁 |
| L0 官网 | ✅ | 总机+分支PDF+125年史+品类页全取 |
| L1 政府一手 | ⚠️ | 市执照语境无；官网125年史作准 |
| L2 命名+DNS | ✅ | M365+SPF硬+DMARC quarantine；三库一致仍停手 |
| L3 B2B库 | ⚠️ | 三库+TheOrg仅参考 |
| L4 社媒协会 | ✅ | LinkedIn公司页+招聘帖+EFC语境 |
| L5 黄页同址 | ✅ | 分支PDF 22网点交叉 |
| L6 电话表单 | ✅ | 总机+免费+分机（未拨打） |
| L7 付费 | ❌ | 未启用 |
