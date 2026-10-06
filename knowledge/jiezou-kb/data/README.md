# data/ —— 海关线索流水线的工作数据层

这个目录存放线索挖掘流水线用到的数据。**只有人工维护的配置进版本库，抓取/导出数据一律忽略。**

## 进版本库（人工维护）

| 文件 | 作用 |
|---|---|
| `watchlist_suppliers.csv` | 供应商名单：`supplier_key,label,role,source`，role ∈ `self` / `competitor` / `partner` / `other`。**这是「竞对买家」信号可配置而非写死的关键**——往这里加一行，打分逻辑立刻把该供应商的买家当作高价值线索。 |
| `company_aliases.csv` | 公司名别名表：`alias_key,canonical_key,note,source,updated`。跨来源同一家公司的不同拼写在这里归一。键值都写**归一化后**的形式（大写、去标点、去法律后缀）。 |
| `fixtures/` | 离线自测用的固定样本与期望结果，保证不联网也能验证打分逻辑。 |

## 被忽略（不进版本库）

| 路径 | 内容 |
|---|---|
| `cache/` | 下载的原始文件（如加拿大 CID 的 XLSX）及其 `.meta.json` |
| `raw/` | 每次运行的原始记录 JSONL |
| `normalized/` | 归一化后的 CSV 及运行元数据 |
| `import_state.json` | 导入器的可选加速缓存 |

**为什么忽略**：抓取下来的数据可能受来源方授权条款限制（Trademo / ImportGenius / Volza 等付费平台的导出文件尤其如此），而且体积大。放进 git 既不合规也不合适。

## 相关命令

```bash
# 查看可用适配器
python3 scripts/customs_data_fetch.py --list-adapters

# 只打印可点的查询链接，不抓取任何东西（零风险）
python3 scripts/customs_data_fetch.py --print-urls --hs 8504.21,8504.22,8504.33

# 离线解析本地 CSV（广交会名录 / 平台导出文件）
python3 scripts/customs_data_fetch.py --adapter local_csv --file <路径> --profile <预设>

# 打分并生成线索
python3 scripts/lead_scoring.py --latest --dry-run
```
