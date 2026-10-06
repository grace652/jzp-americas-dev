# 【买家 176】开发信交接单 — Tidal Electrical Inc.

> 采集日期：2026-09-29 / 来源：batch6 名单（目标客户清单-batch6.csv 序 3）/ 一句话结论：BC Langley 商业电气承包商，专精**低压/中压配电系统改造**与租户改造（ECABC 会员）；Director Drew Linfoot 具名邮箱 `drew@tidalelectrical.ca` 经 SMTP 实测命中（250），A 档可直接主送。

## 一、核心字段

```
公司名 | 联系人姓名 | 职位 | 邮箱 | 邮箱验证状态 | 社媒链接 | 背调摘要 | 信息来源 | 合规风险提示(如有)
Tidal Electrical Inc. | Drew Linfoot | Director | drew@tidalelectrical.ca | 已验证（SMTP 250 命中 + LinkedIn 职务） | linkedin.com/in/drew-linfoot-950419211 | Langley BC 商业电气承包商，专精低压/中压配电系统改造与租户改造，作业于在用/占用场所，ECABC 会员 | 官网 + LinkedIn + ECABC 名录 + BBB + BuildZoom + SMTP 探测 + DNS | 邮箱域=官网域；MX=M365(Exchange Online)，DBEB 拒绝未授权来源（5.4.1），仅真实地址返 250
```

## 二、补充信息（扩展段）

### 标准字段明细
- 国家+城市：加拿大 British Columbia — Langley（大温菲沙河谷）
- 详细地址：70 – 8508 204 St, Langley, BC（BuildZoom）；另见 8929 202 St, Langley（MapQuest）——**两址并存，需电话确认**
- 电话：(778) 246-4393（BBB + ECABC 名录一致）
- LinkedIn：个人 `ca.linkedin.com/in/drew-linfoot-950419211`（"Director at Tidal Electrical Inc."）
- 网站：tidalelectrical.ca
- 成立日：未获取
- 规模：未获取（BuildZoom 称 "ranks in the top 32% of licensed contractors"）
- 营收：未获取
- NAICS：未获取
- 行业名录：**ECABC（Electrical Contractors Association of BC）会员**，名录条目 value/15756
- BBB：未认证（Not BBB Accredited）
- 官网平台：Wix 建站（contact 页为 `/contact` 不存在，首页含 "Contact Us" 区块）

### 联系人（含 still_here 在职核验）

| 姓名 | 职能 | 在职称谓 | 任职时长 | 最近活跃 | 离职风险 | 个人页 |
|---|---|---|---|---|---|---|
| **Drew Linfoot**（主送） | 公司最高决策 | Director | 未获取 | LinkedIn 个人页现职 "Director at Tidal Electrical Inc."（"With a strong background in the electrical…"） | 低 | ca.linkedin.com/in/drew-linfoot-950419211 |

> 说明：官网无 Team/Leadership 页。经 LinkedIn 检索锁定 **Director Drew Linfoot**；域内 SMTP 实测 `drew@` 为真实邮箱，与人名一致，互为佐证。按优先级落到 **老板/Owner** 层。

### 邮箱分档（A/B/C）
- **A 档（具名，主送）**：`drew@tidalelectrical.ca` — Drew Linfoot（Director）
  - **SMTP 实测**（MX = `tidalelectrical-ca.mail.protection.outlook.com`，Microsoft 365）：
    ```
    550  info@tidalelectrical.ca              ← 5.4.1 Access denied
    550  zzz_nonexistent_probe_9987@...       ← 5.4.1 ⇒ 非 catch-all ✅
    550  zzz_random_ab12@tidalelectrical.ca   ← 5.4.1（第二轮复测一致）
    550  drew.linfoot@tidalelectrical.ca      ← 5.4.1
    550  dlinfoot@tidalelectrical.ca          ← 5.4.1
    550  linfoot@tidalelectrical.ca           ← 5.4.1
    250  drew@tidalelectrical.ca              ← ⭐ 候选命中（两轮一致）
    ```
    该 M365 租户启用了目录型拒绝（DBEB）：不存在的收件人返 `550 5.4.1 Access denied`，**真实收件人返 250**。随机地址与三种具名格式全 550，**只有 `drew@` 返 250** ⇒ 网关**具备区分力**，`drew@` 为真实邮箱。
  - 交叉印证：LinkedIn 现职 Director + 域内唯一 "drew"（Drew Linfoot）→ 人名/职务一致。
  - 验证状态：**已验证**。
- **B 档（角色邮箱）**：`info@tidalelectrical.ca` **未通过**（SMTP 550）→ 该域无 `info@`；官网亦未公开邮箱。如需兜底走电话 (778) 246-4393。
- **C 档**：无。
- **H6 声明**：不适用（已取得具名决策人邮箱）。

### 我为什么找他
- ECABC 会员名录里 Tidal 的自我描述**高度具体且与我们的品类直接对撞**：*"a commercial electrical contractor specializing in **intricate retrofit projects on low and medium voltage power distribution systems**, and tenant improvements across commercial and institutional facilities. Our strength lies in **navigating occupied, fully operational settings**"* —— 低压/中压配电系统改造正是变压器替换/增容的典型场景。
- 官网 + LinkedIn 一致指向 **Director Drew Linfoot**，且域内 SMTP 实测 `drew@` 为唯一命中的具名邮箱 —— 说明他是实际收信决策人，不是搜出来的稻草人。

### 买家类型 / 需求品类
- 买家类型：🔥 **B 型 —— 电气承包商**（商业/机构，专精改造），非制造商、非分销商
- 需求品类（带结论态）：
  - `三相美变（UL E541627，可直供）` —— 低压/中压配电系统改造、配电室替换的主谈品类
  - `单相柱上变（认证在办，条件切入）` —— 若涉户外/柱上场景，仅条件性提及
  - `主变（产能可覆盖，UL 区间外，需人工确认）` —— 若其"中压"项目涉及较大容量，需人工确认后推进
- ⛔ 不推：干变对美客户不谈（本案为加拿大客户，如被问可谈 built-to-CSA，但非首选）

### 电压·频率·认证要求
- 电压：**明确涉及低压与中压配电系统**（ECABC 名录原文 "low and medium voltage power distribution systems"）；具体电压等级未获取
- 频率：60 Hz（加拿大）
- 认证：项目执行 CSA/加拿大电气规范（公司未自述产品认证）

### 采购信号
- **改造类项目为主**（retrofit / tenant improvements）→ 旧设备替换 = 变压器更换需求频发
- 专精 **在用/占用场所作业**（occupied, fully operational settings）→ 对交期与可靠性敏感，倾向稳定供应商
- ECABC 会员 → 行业内规范运营、有协会背书
- 官网自述 "We work as true partners with owners, consultants, and general contractors" → 与总包/业主协作型，采购决策链相对清晰

### 可利用的钩子（按强度排序）
1. **ECABC 名录原文的"低压/中压配电系统改造"** —— 与变压器替换场景零距离对撞（最强，可指名）
2. **"在用/占用场所作业"的专精** —— 可谈替换型供货的可靠性/交期适配（注意：首封不报交期数字）
3. **租户改造（tenant improvements）+ 商业/机构设施** —— 常态配电设备消耗
4. **"true partners with owners/consultants/GCs"** —— 关系导向型买家，适合长线

### 开发信建议
- **收件人策略**：主送 `drew@tidalelectrical.ca`（Drew Linfoot，Director，A 档）。**一家只发 1 人**。
- **送达配置**：MX = Microsoft 365（Exchange Online），租户启用目录型拒绝（DBEB，未授权来源返 5.4.1）→ **必须走正规 ESP/合规发件域**，SPF/DKIM/DMARC 三件套齐（该域 SPF = `include:spf.protection.outlook.com -all`，硬策略）；纯文本优先。首封后关注是否因 DBEB 被拒（若退信，改走电话）。
- **发送时段**：温哥华（PT，UTC-8/-7）周二–周四 上午 09:00–11:00 ≈ 北京时间 次日 01:00–03:00（夏令时）。
- **附件建议**：首封不带供货名录/PDF；可提及 UL 证书号与容量区间。
- **备注**：邮箱域 = 官网域（tidalelectrical.ca），无需换域。

### ⚠️ 矛盾点与风险提示
- ⚠️ **两个地址并存**（70-8508 204 St vs 8929 202 St, Langley）→ 寄样/上门前须电话确认实际经营地。
- ⚠️ **官网无 Team 页、无邮箱、Contact 页缺失**（`/contact` 404）→ 人名与邮箱均依赖 LinkedIn + SMTP；任职信息以 LinkedIn 现职为准。
- ⚠️ 公司规模/成立年份未获取，勿在信中引用。
- ⚠️ 同名主体：美国有 **Tidal Electric**（tidalelectric.com，Connecticut）—— **非本案主体**；本案为 **BC Langley 的 Tidal Electrical Inc.**（tidalelectrical.ca）。
- ⚠️ 首封红线：不写交期数字、不写价格词、不提 CSA Certified / SASO / SONCAP / YAWEI。

### 信息缺口清单（请勿编造）
- Drew Linfoot 的**任职起止精确日期**：未获取
- 公司**成立年份 / 规模 / 年营收 / NAICS**：未获取
- **常用变压器容量、电压等级、品牌**：未获取（ECABC 名录仅写"低压/中压"，未给具体等级）
- **采购/估料对接人**：未找到（官网无人名，LinkedIn 仅见 Director）
- **实际经营地址**（两址并存）：需电话确认
- **邮箱可投递性之外的第二方印证**：仅 LinkedIn 职务 + SMTP，**无官网明文**（H3 已满足 SMTP 实测 + 人名一致，但注明无官网明文）

### 一句话画像
Langley 的一家专啃"在用场所低压/中压配电改造"的商业承包商——改造即换变，Director Drew Linfoot 的 `drew@` 直邮实测可达。

### 渠道覆盖清单（L-1、L0–L7）
| 层 | 结果 | 一句话 |
|---|---|---|
| L-1 锁人 | ✅ | LinkedIn 锁定 Director Drew Linfoot |
| L0 官网 | ⚠️ | 官网取到业务/服务；**无 Team 页、无邮箱、/contact 404** |
| L1 政府一手 | ⚠️ | 未查 BC 注册库；BBB/BuildZoom 给出地址电话 |
| L2 命名+DNS | ✅ | MX=M365(DBEB)；**随机 550 + 三种具名格式 550 + drew@ 250（两轮一致）⇒ 实测命中** |
| L3 B2B 库 | ⚠️ | seamless.ai 有档案（未取具名邮箱） |
| L4 社媒协会 | ✅ | LinkedIn 个人页 + **ECABC 会员名录（含业务描述原文）** |
| L5 黄页同址 | ⚠️ | BuildZoom / MapQuest 两址不一致，待确认 |
| L6 电话表单 | ✅ | (778) 246-4393 + 官网 Contact Us 区块（未拨打） |
| L7 付费 | ❌ | 未启用 |

---

- 发信资格：✅ 通过（核心字段齐、still_here 四栏齐、有「我为什么找他」与缺口清单）
- 邮箱档位：**A（具名，SMTP 实测命中）**
- ⓪ 层反身排除：**PASS** —— 官网自述 *"Tidal Electrical Inc is a trusted **commercial electrical contractor**"*、*"We specialize in mechanical upgrades, tenant improvements, and **low-voltage distribution**"*；服务为安装/改造类 ⇒ **承包商客户，非竞品**。
