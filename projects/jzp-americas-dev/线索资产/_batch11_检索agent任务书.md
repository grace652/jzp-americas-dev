# batch11 检索 agent 任务书（自包含，读完即可开工）

> 生成：2026-10-06 ｜ 环节①找客户 ｜ 起始编号 **买家 424**（batch10 止于 423）

---

## 〇、你只做一件事

**找公司级线索。** 产出「公司全称 / 官网 / 业务描述原句 / 国别州省 / 来源」五要素。
**不挖人、不挖邮箱、不写正文、不碰话术。** 那是后面环节的活。

---

## 一、两个目标类型（只找这两类）

### 类型 A：电气承包商 / 工程公司
做电气施工安装的承包商，或做电气工程设计的工程公司。
- 采购动机：**承接项目 → 按图纸采购变压器安装到客户现场**
- 典型容量：配电级 15–3000 kVA
- 识别关键词：`electrical contractor`、`electrical contracting`、`design-build`、`EPC`、`electrical engineering`、`utility contractor`、`powerline construction`、`substation construction`

### 类型 B：分销商 / 贸易商
电气产品分销商、批发商，或做电气设备贸易的公司。
- 采购动机：**备库存 / 转售 → 批量采购**，看价格与供货稳定性
- 典型容量：配电级至变电站级 15 kVA – 5 MVA
- 识别关键词：`distributor`、`wholesale`、`electrical supply`、`power equipment supplier`、`transformer sales`、`apparatus sales`

### ⭐ 高价值档（尽量多抓）
官网业务描述**原句**出现以下任一词：`substation` / `high voltage` / `transformer` / `transmission`。

---

## 二、地理边界

**只找加拿大 + 美国。不做南美。**
- 加拿大优先省：ON / BC / AB / QC / NS / MB / SK / NL
- 美国优先州：**用 batch10 没重点用过的州**（batch10 集中 TX / AZ / NY / FL / MI / LA / SD / IA / NJ / MA / MO / CO / IL / WI / MN）

---

## 三、🔴 排除规则（命中即丢，不要报上来）

| # | 排除项 | 判据 |
|---|---|---|
| **1** | **变压器同业 / 竞品制造商** | 官网出现 `manufacturer` / `we manufacture` / `our factory` / `in-house remanufacturing` / `coil rewinding` ⇒ **一票否决** |
| **2** | **「中国货源 → 北美」代理 / 贴牌商** | 主营为中国厂商北美代理 |
| **3** | **我方关联实体** | 地址 **`1243 N Roseburg Ct, Visalia, CA 93291`**（我方美国据点，POWER ELECTRONICS 同址）⇒ 一律排除 |
| **4** | **已触达的公司** | 跑 `scripts/check_dedup.py` 对照 `_dedup_baseline_batch11.txt`（**1445 词**）|
| **5** | **退信域名** | 见 `_bounce_domains.txt`（13 个）|
| **6** | **域名无 MX** | 收不了信，直接丢 |
| **7** | **民用电工 / 纯安防 / 纯弱电** | 业务与 MV/HV 变压器无关 |
| **8** | **工程咨询（规格制定方，非采购方）** | 只出图纸不采购 ⇒ 低优先级，标出来但不计入主名单 |

---

## 四、🔴 必须做的验证（每家都要）

1. **进官网读「业务描述原句」** —— 这是唯一可靠的类型判定依据，**不许靠公司名猜**
2. **查 MX 记录** —— 用 `dig @8.8.8.8 MX <domain>`（**不要用本机默认 DNS**：本机有 TUN + fake-ip 劫持，任何查询都返回 `198.18.0.x`）
3. **跑排重** —— `python3 scripts/check_dedup.py <候选文件>` 或手工对照基线
4. **读官网 About / Services / Capabilities 页**确认是采购方还是制造商

> ⚠️ **遇 Cloudflare / CAPTCHA 停下换路径，不硬闯。**

---

## 五、🔴 batch11 指定搜索来源（**与 batch5–10 全部不同**）

| 路 | 优先来源 |
|---|---|
| **A 加拿大** | ① **NECA 其余分会**（100+ 分会，batch10 只用了 South Texas 一个）② **省级电气承包商协会**（非 CECA/ECAS）③ **CCIB / CAMSC 原住民企业名录**（batch10 验证有效）④ 省 SoS 按 NAICS 238210 ⑤ **IEEE PES T&D / RE+ / PowerGen 参展商名录** |
| **A 美国** | ① **NECA 其余分会**（逐个翻）② **州级电气承包商协会**（各州独立协会，非 NECA）③ 州 SoS 按 NAICS 238210 / 237130 ④ **PowerGen / DistribuTECH 参展商名录**⑤ **AGC / ABC 分会**（batch9 用过全国，分会未用） |
| **B 加拿大** | ① **Surplus Record 经销商目录**（二手/租赁垂直平台）② **CTI 名录其余类别**③ 省级批发商协会 ④ **CanadaBuys 供应商库**（batch9 用过，换检索词）⑤ 工业供应垂直站 |
| **B 美国** | ① **Surplus Record 经销商目录** ② **NEMRA 其余分区**（batch9 用过全国）③ 州级电力供应协会 ④ **PEARL 其余会员** ⑤ 二手电力设备垂直平台（如 Transformer 交易站） |

> ⚠️ **已知失效来源，不要再碰**：EUDA（全量 9 家已全命中基线）、EASA（明示禁止营销用途）、
> ThomasNet / GlobalSpec / IndustryNet（全站 JS 门控）、SupplyForce / AD / Network Distribution（需登录）。

---

## 六、产出格式（严格照此，便于程序解析）

每条一行，**制表符分隔**：

```
公司全称<TAB>官网域名
```

另附一份 markdown 详表，每家含：

| 字段 | 说明 |
|---|---|
| 公司全称 | 与工商登记一致 |
| 简称 | 便于文件命名 |
| 国家 / 州省 / 城市 | 必填 |
| 官网 | 域名 |
| **业务描述原句** | 🔴 **官网原文，用引号，可指认 URL** |
| 高价值档 | ⭐ 若含 substation/high voltage/transformer/transmission |
| 来源 | 具体到「哪个名录/哪个页面」|
| MX | `✅ 有（网关名）` / `❌ 无` |
| 排重 | `✅ 未命中` / `🔴 命中基线（词）` |
| 排除判定 | 若被排除，写明依据 |

---

## 七、交付

写到 `~/jzp-americas-git/projects/jzp-americas-dev/线索资产/` 下：
- `_batch11_A_加拿大_候选.md`（20 家）
- `_batch11_A_美国_候选.md`（20 家）
- `_batch11_B_加拿大_候选.md`（20 家）
- `_batch11_B_美国_候选.md`（20 家）

**目标 20 家/路，宁缺毋滥** —— 凑不够就如实说「只找到 N 家」，**不要用不合格的充数**。
