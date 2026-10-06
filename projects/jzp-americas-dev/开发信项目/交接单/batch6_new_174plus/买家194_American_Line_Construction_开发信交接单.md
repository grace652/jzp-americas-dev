# 【买家 194】开发信交接单 — American Line Construction LLC

> 采集日期：2026-09-29 / 来源：batch6 名单（第 21 行，原 CSV 州省 CA）/ 一句话结论：**亚利桑那 Gilbert 的小型变电站/线路承包商**，已锁到 owner 级具名邮箱（SMTP 实测 250），A 档可主送；但 ROC 执照分类与营销口径存在矛盾，需人工留意。

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示(如有)
American Line Construction LLC | Edmond Istanbouly | Member（owner，与 Christine Ashkar 并列） | eistanbouly@americanlineconstruction.com | 已验证（SMTP 250，控制地址 250 + 非 catch-all + 对照组 550） | linkedin.com/in/edmond-istanbouly-59612274（个人页，未见公司名，仅旁证） | AZ Gilbert，LLC 2022-08-25 成立，变电站建设+架空/地下线路，自称持 AZ/CA/UT/NV 执照 | 官网首页（info@ 明文）+ AZ Corporation Commission 实体 23415243 + AZ ROC #362430 + SMTP 实测 | 域名 M365 域，勿多轮探测；ROC 分类与营销口径不一致（见风险段）
```

## 二、补充信息（扩展段）

### 标准字段明细
- 国家+城市：美国 Arizona，Gilbert（大凤凰城都会区）
- 详细地址：1214 W Seascape Ct, Gilbert, AZ 85233（注册主址）；法定送达代理地址 1010 E Jefferson St, Phoenix, AZ 85034
- 电话：+1 480-620-8847（官网首页，480 = 亚利桑那凤凰城号段）
- LinkedIn：个人页 linkedin.com/in/edmond-istanbouly-59612274（Edmond，Chandler AZ）；**未找到公司 LinkedIn 页**
- 网站：americanlineconstruction.com（GoDaddy 建站 / WordPress，页面含模板占位文案，站点较新）
- 成立日：**2022-08-25**（AZ LLC 成立，Document No. 23415243）—— 与官网自称「50 Solid Years」**口径矛盾**（见风险段）
- 规模：小微（成员仅 2 人：Christine Ashkar、Edmond Istanbouly；BuildZoom 记 Employees: Christine Ashkar and Edmond…）
- 营收：未找到
- NAICS：未找到（未在 supplychain.wemakeithere.org 命中制造业代码；官网为服务描述，非制造）
- 执照：AZ ROC **#362430**，分类 **CR-67 Low Voltage Communication Systems**，状态 Active，签发 2025-11-20，到期 2027-11-30
- 州省修正：**CSV 原值 = CA ｜ 实测 = AZ（Gilbert）**（依据：官网首页电话 480 号段 + AZCC 注册主址 + AZ ROC 执照，三处一致）

### 联系人（含 still_here 在职核验）
| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| Edmond Istanbouly | owner / 决策人（本次主送） | Member, American Line Construction LLC（AZCC 备案） | 2022-08 至今（约 4 年，公司成立即任） | 中：AZCC 备案 Active（2026-09-02 抓取）+ 邮箱 SMTP 250 实测 | 低（owner，与公司存续绑定） | linkedin.com/in/edmond-istanbouly-59612274 |
| Christine Ashkar | 共同 owner（并列 Member） | Member, American Line Construction LLC（AZCC 备案） | 2022-08 至今 | 中：AZCC 备案 Active | 低（owner） | 未找到个人页；`cashkar@` SMTP 550（非此格式） |

> 🔴 一家只发 1 人：**主送 Edmond Istanbouly**（唯一有已验证具名邮箱的 owner）。

### 邮箱分档（A/B/C）
- **A 档（具名，已验证）**：`eistanbouly@americanlineconstruction.com` —— Edmond Istanbouly
  - 验证矩阵：控制地址 `info@americanlineconstruction.com` = **250**（官网首页明文，真实）｜随机地址 `zzz_nonexistent_probe_9987@` = **550**（非 catch-all）｜对照组 `john.smith@`/`jane.doe@`/`bob.jones@` = 全 **550**｜候选 `eistanbouly@` = **250** ✅
  - 命名规则佐证：`{first-initial}{last}@`（e+istanbouly）；同域 `edmond@` = 550（排除纯名格式）
  - 交叉印证：AZCC 备案 Member 姓名「Edmond Istanbouly」（一手源，H5 达标）＋ SMTP 实测
- **B 档（角色）**：`info@americanlineconstruction.com`（官网首页明文，first-party）—— 备选/兜底
- H6 声明：**不适用**（已取得具名决策人邮箱，非仅角色邮箱）

### 我为什么找他
- 他不是从名单里随手挑的「联系人」：**AZ Corporation Commission 实体 23415243 的备案文件里，Edmond Istanbouly 与 Christine Ashkar 并列为仅有的两名 Member**——即这家公司的两个实际 owner；而公司官网首页自述「specialized & focused in **substation and powerline construction**」，正是我方能供美变/主变的采购场景。
- 旁证：他名下另有关联物业投资（elementix 显示其控制多个实体），说明是本地的实际出资人而非挂名员工。

### 买家类型 / 需求品类
- 买家类型：🔥 **B 电气承包商（变电站 + 架空/地下线路施工，小微）**——实测画像里的 B 型
- 需求品类（带结论态）：
  - `三相美变（UL E541627，45–5,000 kVA，可直供）` —— 变电站新建/扩容主谈
  - `主变 / 变电站变（UL E541626，750–110,000 kVA，可直供）` —— 项目制，按标段容量确认
  - `单相柱上变（认证在办 E544629，条件切入）` —— 架空/配电线路场景，非首推
  - ⚠️ 美国客户：**不谈干变**（无 UL 不匹配）

### 电压·频率·认证要求
- 电压：未获取（需电话确认其常用一次/二次电压段，典型 AZ 配网 12.47/25 kV，未证实）
- 频率：**60 Hz**（美国）
- 认证：我方持 UL **E541627 / E541626** 正式 CoC，适配美国市场

### 采购信号
- 官网明写「**send us a scope and let us show you how we do business**」→ 典型的**按标段询价**模式，愿意接新供应商报价
- 业务聚焦变电站建设 → 变压器是核心采购品类（非边缘）
- 小微、自有团队（installers/linemen），无中间分销层 → 决策链短

### 可利用的钩子（按强度排序）
1. **变电站建设专精**（官网原句 "specialized & focused in substation and powerline construction"）—— 与主变/美变品类强相关
2. **持 AZ/CA/UT/NV 四州执照 + 「all across the southwest」**—— 跨州项目供货想象空间
3. **「50 Solid Years」团队经验叙事**（可作切入点，但需避开与 LLC 2022 成立的矛盾，别点破）
4. 「send us a scope」的开放询价姿态 → 低门槛切入

### 开发信建议
- **收件人策略**：主送 `eistanbouly@americanlineconstruction.com`（Edmond Istanbouly，A 档，可写个性化正文）；`info@` 仅作兜底，不重复发
- **开场角度**：从其「变电站专精 + 西南四州」定位切入（写信 agent 决定最终措辞）
- **发送时段**：亚利桑那 **MST（UTC-7，全年不夏令时）**，周二–周四当地上午 = **北京时间次日 00:00–03:00** 区间（美西无夏令时，勿按 PDT 折算）
- **送达配置**：MX = **Outlook / Exchange Online（M365）**，SPF `include:secureserver.net -all` → 发信域须有合规 SPF/DKIM/DMARC；**M365 对探测 IP 有 Spamhaus 反制，勿对本域做多轮 SMTP 探测**
- **附件建议**：不带名录/供货记录；如需，仅附 UL 证书号与容量区间（由写信环节决定）

### ⚠️ 矛盾点与风险提示
- 🔴 **执照分类矛盾**：AZ ROC #362430 分类为 **CR-67 Low Voltage Communication Systems**（低电压通信），与官网自称「substation construction」**不完全吻合**；plumbintel 关联的 2 张许可均为小额工程（如 "Adding SES/switch gear to suite"）。→ 该公司可能是**以低压通信执照承接、实际做小规模电力安装**的小微；其变电站能力需电话确认。
- 🔴 **成立年份矛盾**：官网称「50 Solid Years Of Building Substations」，但 AZ LLC 2022-08-25 才成立。→ 应为**创始人团队经验**，非公司历史；写信时勿引用「50 年公司史」。
- ⚠️ 官网含模板占位文案（"This can be a short description about a project…"）→ 站点较新/未完工，佐证其为新公司。
- ⚠️ 地址校验：主址 1214 W Seascape Ct 为**住宅区门牌样式**（Gilbert 住宅街），另 1010 E Jefferson St 为法定送达代理（National Contractor Services Corp）地址 → 寄样前须电话确认实际经营/收货地。
- ⚠️ `cashkar@`（Christine）SMTP 550 → Christine 的邮箱非该格式或不存在，**不要给 Christine 发**。

### 信息缺口清单（请勿编造）
- 常用变压器**容量区间 / 一次二次电压 / 品牌偏好**：未获取（需电话）
- 公司**年营收 / 员工数**：未找到
- **NAICS 代码**：未找到
- 公司 **LinkedIn 页**：未找到
- Edmond 的**具体职务头衔**（President/Manager？备案仅记 Member）：未找到
- 是否**实际经营地**在 Gilbert（vs 仅为注册地址）：未证实
- ROC 是否另有**高压/电力类执照**（plumbintel 仅显示 CR-67 一条）：未证实

### 一句话画像
凤凰城都会区一家 2022 年新设、仅两名 owner 的变电站/线路小微承包商——营销喊「50 年」，执照却是低压通信类；owner Edmond 的邮箱实测可达，可作为**低门槛试单对象**。

### 渠道覆盖清单（L-1、L0–L7）
| 层 | 结果 | 一句话 |
|---|---|---|
| L-1 锁人 | ✅ | AZCC 备案锁定 2 名 Member（owner）；LinkedIn 个人页旁证 |
| L0 官网 | ✅ | 首页取 info@ + 电话 + 业务描述；Team 页无（站点较新） |
| L1 政府一手 | ✅ | AZCC 实体 23415243 + AZ ROC #362430（均为一手源） |
| L2 命名+DNS | ✅ | MX=Outlook；SMTP 四步协议验证 eistanbouly@ 250 |
| L3 B2B 库 | ⚠️ | BuildZoom 记 Employees: Christine Ashkar / Edmond…（旁证） |
| L4 社媒协会 | ⚠️ | 仅个人 LinkedIn 页；无公司页、无协会名录命中 |
| L5 黄页同址 | ✅ | bizprofile / bizapedia / BuildZoom 同址交叉一致 |
| L6 电话表单 | ✅ | 480-620-8847（未拨打）；官网无表单 |
| L7 付费 | ❌ | 未启用 |
