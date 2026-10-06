---
name: canada-b2b-prospecting
description: Canadian B2B prospecting and background check. Use when user asks 背调, 找客户, 查公司, 联系方式, 邮箱电话, Canada Yellow Pages, Chamber, Association lookup.
---

# Canada B2B Prospecting

帮用户背调加拿大企业/人物，核心目标：找到**所在公司 + 公开商务联系方式**。

只输出公开商务信息，不做个人隐私人肉（不查家庭住址、个人手机、社保等）。

## Workflow - 5步法（按顺序执行）

### Step 1. 确认主体 Company + Person
- 输入可能只有截图/名字/LinkedIn头衔，如 `President/CEO @ Grid Link | Thunder Bay`
- websearch: `"[Name] [Company] Thunder Bay"` + `"[Company] Thunder Bay Ontario company"`
- 确认：官网域名（如 gridlink.ca）、LinkedIn公司页、地址是否一致
- 记录官网 `/contact` 页的总机、info邮箱、地址

### Step 2. 政府注册验真
- Corporations Canada: `ised-isde.canada.ca/cc/lgcy/fdrlCrprSrch.html` — 查联邦公司名、董事
- Ontario Business Registry: `ontario.ca/page/ontario-business-registry` — 查安省公司注册号、officer、办公地址
- 不一致要明确标注

### Step 3. 商会 Chamber 查负责人直连
优先级最高，商会名录是企业自己为接单提交的：
- Thunder Bay Chamber: `business.tbchamber.ca/list/member/...` — 关键词搜公司名，拿 Rep/Contact Info（President + Phone + 地址）
- Ontario Chamber OCC `occ.ca`, Canadian Chamber `chamber.ca`
- Toronto Region Board of Trade `bot.com`（大多地区公司用）
- websearch模板: `"[Company]" site:tbchamber.ca`, `"[Company]" chamber phone`

### Step 4. 行业协会 Association 查直邮
垂直行业协会自带资质审核，比通用黄页准：
- 建筑/电力：CATB `catb.on.ca/members/...` — 拿 Email / Phone / Fax / Services / Division
  - 例：GRID LINK CORP. 页登记 `jbernst@gridlink.ca / 807-683-0350 / 1499 Rosslyn Road`
- 矿业供应链：MineConnect `mineconnect.com/corporate-members/...`
- 电力：ECAO, Ontario Electrical League
- 建筑总会：CCA `cca-acc.com`
- websearch模板: `"[Company]" site:catb.on.ca`, `"[Name]" email contact`, `"[Name]" j***@gridlink.ca`

### Step 5. 通用黄页补全 + 交叉验证
- YellowPages.ca / Canada411.ca / 411.ca — 补电话地址营业时间
- BBB `bbb.org/ca` — 看投诉+靠谱度
- Google Maps / Yelp.ca — 核对电话地址是否与官网一致
- ZoomInfo / LinkedIn — 只做辅助验证，不直接采用掩码邮箱（如 `j***@gridlink.ca`, `be***@g***.ca`），必须与 Step 3/4 的明文邮箱交叉
- 官网 webfetch: `https://[domain]/contact` 拿 `info@`, 总机，Emergency电话

## Output Template（中文回复）

```markdown
### 1. 人物
[Name] - [Title] @ [Company]，地点，背景一句话

### 2. 所在公司
[Company全称] / 官网 / LinkedIn公司页 / 成立年份 / 规模 / 主业 / 总部地址

### 3. 联系方式（公开商务）
- 直邮: xxx@yyy.ca（来源：CATB/商会）
- 总机/名片电话: (xxx) xxx-xxxx（来源：商会/官网）
- 传真: ...
- 公共邮箱: info@...
- Contact页: URL
触达建议一句话
```

每个联系方式后必须注明来源（官网/CATB/商会/ZoomInfo推测）。

## Example - Jody Bernst / Grid Link
- 人物：Jody Bernst, President/CEO/Owner @ Grid Link, Thunder Bay, 前Thunder Bay Hydro lineman
- 公司：GRIDLINK / Grid Link Corp., gridlink.ca, Founded 2000, 51-200人, Utility Contractor, 1499 Rosslyn Road Thunder Bay ON P7E 6W1
- 联系：jbernst@gridlink.ca（CATB）, (807) 683-0350（商会登记为本人+官网总机）, info@gridlink.ca, fax (807) 345-3693

## Rules
1. 先官网，再商会协会，最后黄页聚合站
2. 掩码邮箱必须交叉验证，不单独作为结论
3. 加拿大区号注意：807=安省西北，416/647=多伦多，604=BC
4. 输出简短客观，带 `文件:行号` 式来源时用 URL 即可
5. 不确定就写“未找到公开信息”，不要编邮箱电话
