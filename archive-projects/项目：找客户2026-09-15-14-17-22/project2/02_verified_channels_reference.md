# 02 · 已验证渠道清单

> **本文件职责**：存放**已验证比较可靠的信息渠道清单**（领英 / 行业黄页 / 展会名录等）。
> ✅ **本文件属参考资料：可以较自由地增删。由用户补充实际清单。**
> 步骤顺序见 `01_execution_steps.md`；全量渠道细节在技能库 `references/02-sources.md`。

---

## 一、渠道清单（待用户补充为主）

> 下面先给出**本项目已实测可用**的渠道作为起点，**请用户按实际使用情况增删**。
> 状态列：`✅已验证` / `🟡待验证` / `❌不可用`。

### 1.1 领英（LinkedIn）—— 🔴 双岗使用（2026-09-23 更新）

> **LinkedIn 在本项目有两个岗位**：**L-1 找人**（最优先）+ **L4 核验**。

| 渠道 | 岗位 | 状态 | 备注 |
|---|---|---|---|
| 公司页 JSON-LD 结构化数据 | L-1 + L4 | ✅已验证 | 拿精确员工数、地址、业务描述（个人页常 999/451） |
| 公司页 **Employees 名单**（员工姓名+头衔） | **L-1** | ✅已验证 | **锁具名决策人的主要入口** |
| 公司页 People 区（按职能/层级筛） | **L-1** | 🟡待验证 | 有则用；`/people/` 子路径常跳登录墙 |
| 个人页（公司页 dork / 头衔核验） | L-1 + L4 | ✅已验证 | 只读公开页与搜索摘要 |
| 个人页 **Contact info / About 区取邮箱** | L-1 后 | 🟡待验证 | Contact info 约 30% 命中；About 区 Ctrl+F 搜 `at`/`dot` |
| **still_here 在职核验**（current 公司 / 任职时长 / 最近活跃） | **L4** | ✅已验证 | 🔴 任何邮箱进主送前必做（见 `01-methods.md` §2.6） |
| 组织图反推（谁 tag 谁 / endorsement / People also viewed） | **L-1** | ✅已验证 | 小微买家兜底 |
| Google X-Ray（`site:linkedin.com/in/ "人名" "@域名"`） | L-1 后 | ✅已验证 | 免费取信一步 |
| 领英公司页 slug 直访 | — | 🟡待验证 | 部分需登录 |
| **Sales Navigator 过滤器**（Seniority/Function 等） | — | ❌**未启用** | 本环境无订阅，**不要写进操作步骤** |
| LinkedIn Boolean（自建 query） | L-1 | ✅已验证 | 运算符须大写、只用直引号、免费版 OR ≤3–4 个 |

### 1.2 行业黄页 / 商业名录
| 渠道 | 状态 | 备注 |
|---|---|---|
| opengovus.com（SAM.gov 镜像） | ✅已验证 | 拿 CAGE 码、PSC 采购品类 |
| opengovwa.com（WA 州） | ✅已验证 | 未被 Cloudflare 封 |
| opengovca.com（加拿大注册库） | ✅已验证 | 董事、注册日、状态 |
| Yahoo Local / Yelp / BBB / Manta | 🟡待验证 | 反查本地信息用 |
| AllBiz / CompanyListing（加拿大） | 🟡待验证 | 联系人+邮箱，注意单一来源 |
| Bizapedia / opencorporates | ❌不可用 | 403 / 验证码 |

### 1.3 展会名录 / 名片
| 渠道 | 状态 | 备注 |
|---|---|---|
| 公司提供的展会名片 | ✅已验证 | 见 `buyers/_series/迪拜展会名片跟进表.md` |
| 展会官方参展商名录 | 🟡待验证 | 待用户补充实际网址 |

### 1.4 政府 / 官方一手源
| 渠道 | 状态 | 备注 |
|---|---|---|
| FMCSA 联邦运输档案 | ✅已验证 | 挖真实邮箱的金矿 |
| SAM.gov / USAspending API | ✅已验证 | 采购品类与合同明细 |
| 州承包商执照库（agentlookups / ccblookup 等） | ✅已验证 | 执照状态、qualifier 姓名 |
| ImportYeti（美国海关） | ✅已验证 | 免费免登录，供应商名单 + HS 码 |
| 州务卿（apps.sos.wv.gov 等） | ✅已验证 | 公司档案 |

---

## 二、❌ 本环境「不可用」清单（实测，避免重复踩坑）

| 站点 / 服务 | 症状 | 替代 |
|---|---|---|
| `facebook.com` / `mbasic` / `instagram.com` | HTTP 000（直连被墙） | WebSearch 索引；抓官网页脚扫社媒链接 |
| `linkedin.com` 个人页 | 999 / 451 | WebSearch 取摘要 |
| `dns.google` / `cloudflare-dns.com`（DoH） | 空响应 | `nslookup <域名> 8.8.8.8` |
| `web.archive.org`（curl CDX API） | 超时 | 改用 WebFetch |
| `r.jina.ai` | HTTP 000 | 不可用 |
| `bizapedia.com` | 403 / 付费墙 | Google 摘要 |
| `opencorporates.com` | 验证码 | 州务卿镜像站 |
| `washingtoncompany.net` / `alaskacompanydir.com` / `kycompanydir.com` | Cloudflare ASN 封禁 | opengovwa / opengovus |
| `data.wa.gov` / `data.colorado.gov` Socrata API | HTTP 000 | opengovwa / OpenGovCO |
| `safer.fmcsa.dot.gov` 姓名检索 | 403 | 按 DOT 号查快照 |
| 加勒比媒体/政府站（`bahamas.gov.bs`） | 403 / 国家限制 | 同区域其他媒体站；WebSearch |
| 斯里兰卡 ROC（`eroc.drc.gov.lk`） | HTTP 000 | 官网 + RDAP |
| Alabama SOS | SSL 握手失败 | Google 摘要 |
| WA L&I 官方 API / WV 承包商执照库 | 需会话或令牌 | 无法绕过 |

**✅ 已验证可用的通用通道**：WebFetch、Googlebot UA、`nslookup ... 8.8.8.8`、Verisign RDAP、ImportYeti、opengovus / opengovwa、USAspending API、`apps.sos.wv.gov`。

---

## 三、渠道使用顺序（对应 waterfall **L-1、L0–L7**）

| 层 | 渠道 | 说明 |
|---|---|---|
| **L-1** | 🔥 **锁具名决策人** | 岗位映射表 → 公司页 Employees → 4 组 query → 组织图反推；**通关：≥1 份「姓名+职能+在职证据+个人页 URL」** |
| L0 | 官网全量 | 角色邮箱 + 页脚 + PDF + `og:description` + Cloudflare `data-cfemail` |
| L1 | 政府一手源 | FMCSA / SAM / 州执照库 / 投标文件（**政府邮箱 > 官网通用**） |
| L2 | 命名规则 + DNS | MX/TXT；有两库一致 + 真样本才可推演；**免费第一跳≈1/3 命中** |
| L3 | B2B 库交叉 | ContactOut / Seamless.AI / LeadIQ / Prospeo / Apollo / Hunter |
| L4 | 社媒与协会 | Facebook / **LinkedIn 第二岗（still_here 核验）** / ABC·NECA·IBEW / 商会 |
| L5 | 本地黄页与同址 | Yahoo Local / Yelp / BBB / Manta / 公用事业合格承包商 PDF |
| L6 | 电话 / 表单兜底 | 表单首触 + 点名转交 |
| L7 | 付费 API 预留 | Hunter / Snov / Apollo（未启用时标注）；**Sales Navigator 同属此位** |

> 🔴 **角色邮箱升级三步**（唯一收获是 `info@` 时强制跑）：挖职能邮箱 → 反推命名规则 → 免费推演。见 `01_execution_steps.md` 步骤 2.4 与 `00_core_rules.md` H6。

---

## 四、DNS / RDAP 命令速查

```bash
curl -sL "https://rdap.verisign.com/com/v1/domain/<域名>"   # 注册日/到期日/NS
curl -sL "https://rdap.org/domain/<域名>"                    # 其他 TLD
nslookup -type=MX <域名> 8.8.8.8                             # 邮件服务器
nslookup -type=TXT <域名> 8.8.8.8                            # SPF
nslookup -type=NS <域名> 8.8.8.8                             # 域名服务器
curl -sIL -o /dev/null -w "%{url_effective}" "http://<域名>" # HTTP 跳转
```

**网关识别**：`*.ess.barracudanetworks.com`=Barracuda、`*.ppe-hosted.com`=Proofpoint、`*.mimecast.com`=Mimecast。

---

*请用户在下方或本节中持续补充实际验证过的渠道。*
