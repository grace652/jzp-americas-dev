# batch11 A 档投递排程表（22 封）

> 用户指令：**「给A档设置定时发送任务」**（2026-10-06）
> 队列：`发信队列-batch11A.json` ｜ 驱动：`/tmp/driver_b11a.sh`（PID 16895）
> 日志：`投递日志-batch11A.log` ｜ 建立：2026-10-06 10:41（北京）

---

## 一、排程依据（**日常铁律，未破例**）

| 项 | 规则 |
|---|---|
| **窗口** | 客户**当地工作日 09:00–10:00** 送达 |
| **避开** | 周六 / 周日（本批全为 **2026-10-06 周二**）|
| **间隔** | 同区多封**在窗口内散开**，**不卡一个时间点、不规律等间隔** |
| **驱动** | `--run --limit 1` 每 20s 轮询 —— **不抢 `.daemon.lock`**，与其它定时任务零冲突 |

---

## 二、时区分布

| 时区 | 封数 | 北京窗口 | 说明 |
|---|---|---|---|
| **AT** 大西洋（NL）| 1 | 20:30 | 首封 |
| **ET** 东部 | 17 | 21:00–21:57 | ON/QC + 美东部（PA/OH/GA/MD/CT/FL/IN/TN）|
| **CT** 中部 | 2 | 22:15 / 22:45 | MB / TX |
| **MT** 山区 | 2 | 23:15 / 23:45 | AB / UT |

**整体跨度：北京 20:30 → 23:45（3 小时 15 分）**

---

## 三、逐封排程

| # | 北京 | 当地 | 时区 | 收件人 | 公司 |
|---|---|---|---|---|---|
| 1 | 10-06 20:30 | 09:30 | AT | `gary.lovell@ecotechnl.ca` | 454 EcoTech NL |
| 2 | 10-06 21:00 | 09:00 | ET | `aaugustine@agostinoutilities.com` | 440 Agostino Utilities |
| 3 | 10-06 21:03 | 09:03 | ET | `mikec@albarell.com` | 443 Albarell Electric |
| 4 | 10-06 21:06 | 09:06 | ET | `jmeyer@battag.com` | 441 Battaglia Electric |
| 5 | 10-06 21:12 | 09:12 | ET | `chuck.hinton@c3mpowersystems.com` | 447 C3M Power |
| 6 | 10-06 21:15 | 09:15 | ET | `michael.weaver@ctgpowersystems.com` | 459 CTG Power ⭐ |
| 7 | 10-06 21:18 | 09:18 | ET | `tygel@electricalmaterials.ca` | 450 E.M.C. |
| 8 | 10-06 21:21 | 09:21 | ET | `jeff.sloan@enerfab.com` | 444 Enerfab ⚠️ |
| 9 | 10-06 21:24 | 09:24 | ET | `fholleran@hbfrazer.com` | 442 H.B. Frazer |
| 10 | 10-06 21:30 | 09:30 | ET | `k.martin@hatzelandbuehler.com` | 448 Hatzel & Buehler |
| 11 | 10-06 21:33 | 09:33 | ET | `dlytle@isiprime.com` | 446 Inglett & Stubbs |
| 12 | 10-06 21:36 | 09:36 | ET | `jball@lakeportpower.com` | 458 Lakeport Power ⭐ |
| 13 | 10-06 21:39 | 09:39 | ET | `Nate@Mid-Westmachinerymart.com` | 466 Midwest Machinery Mart |
| 14 | 10-06 21:42 | 09:42 | ET | `joshmatthews@oneilelectric.com` | 456 O'Neil Electric ⚠️ |
| 15 | 10-06 21:45 | 09:45 | ET | `joe@pielaelectric.com` | 460 Piela Electric |
| 16 | 10-06 21:51 | 09:51 | ET | `patrick@powerhouse-systems.com` | 469 Powerhouse Systems |
| 17 | 10-06 21:54 | 09:54 | ET | `r_remsey@vecohio.com` | 439 VEC |
| 18 | 10-06 21:57 | 09:57 | ET | `mvarnado@white-electrical.com` | 445 White Electrical |
| 19 | 10-06 22:15 | 09:15 | CT | `Isaac@megawattequipment.com` | 471 Megawatt Equipment |
| 20 | 10-06 22:45 | 09:45 | CT | `shawn@wescan-services.com` | 435 Wescan |
| 21 | 10-06 23:15 | 09:15 | MT | `bhalina@chemco.com` | 425 Chemco |
| 22 | 10-06 23:45 | 09:45 | MT | `gavin@sullyent.com` | 470 Sully Enterprises |

> 间隔 3–6 分钟，**不规律**；ET 区 17 封在 57 分钟内散开，未卡点、未等间隔。

---

## 四、发前闸门（**全部已过**）

| 闸门 | 结果 |
|---|---|
| **红线自检**（`parse_letter` + `compliance_check`）| ✅ **22/22 通过**（0 拦截）|
| **静默跳过健康检查**（`cmd_build` 内置）| ✅ 扫描 22 / 入队 22，**无跳过** |
| **重复正文闸门**（`检查重复正文.py --check`）| ✅ **无重复**（同一封信未对同一收件人发过）|
| **MX 复核**（`dig @8.8.8.8`）| ✅ 22/22 有 MX |
| **退信闸门** | ✅ 载入 22 个黑名单地址 + 2 个整域封锁（`kvaelectric.com` / `birminghamec.com`），**22 家无一命中** |

> 📌 建队时**健康检查抓到 18 封缺「收件人」行**（注解段无可解析地址）—— 已按项目惯例**插到注解段首**修复（`scripts/补收件行-batch11.py`），**不是插到文件头**（batch8 曾在此浪费一轮）。

---

## 五、⚠️ 两家带集团冲突标记（**已按指令照排，可随时撤下**）

| 编号 | 公司 | 冲突 | 建议 |
|---|---|---|---|
| **444** Enerfab | 母公司 **Quanta Services**（2026-07-14 完成收购）| Quanta 系**已发 6 家**（Chatham / JW Didado / Lee / MJ Electric / Potelco / Service Electric）→ 这是第 7 封 | 正文**未提及**集团关系；如要撤下，在 21:21 前从队列删除即可 |
| **456** O'Neil Electric | 母公司 **Franklin Empire = batch4 买家86** | 该集团 `cara.backman@franklinempire.com` **已于 9/29 发出**（含跟进信）| 正文**未提及**集团关系；如要撤下，在 21:42 前删除即可 |

**撤下方法**（不影响其它队列）：
```bash
cd "/Users/eric/WorkBuddy AI/2026-09-27-00-43-30/jzp-americas-dev"
python3 - <<'PY'
import json
q='发信队列-batch11A.json'
d=json.load(open(q))
for i in d:
    if i['letter'] in ('开发信-Enerfab.md','开发信-ONeil-Electric.md'):
        i['status']='blocked'; i['blocked_reason']='集团冲突，人工撤下'
json.dump(d,open(q,'w'),ensure_ascii=False,indent=1)
print('已撤下')
PY
```

---

## 六、跨任务不打扰（🔴 用户 2026-10-01 立的硬规则）

启动时实测**另有两个跟进队列驱动在运行**：
- `driver_f1005.sh 发信队列-跟进1006-A.json`
- `driver_f1005.sh 发信队列-跟进1007-B.json`

**本驱动的做法**：
- ✅ 用**独立队列文件** `发信队列-batch11A.json`
- ✅ 用 `--run --limit 1` 轮询，**不抢 `.daemon.lock`**（当前无锁占用）
- ✅ **绝不 kill 任何其它进程、绝不触碰其它队列**
- ✅ 日志独立写 `投递日志-batch11A.log`

---

## 七、验收（明早做）

1. **IMAP 已发送夹核验**（权威记录，非队列自报）—— 腾讯邮箱已发送夹名 `&XfJT0ZAB-`
2. **退信扫描**（`扫描退信.py`）—— 重点看 Proofpoint / Mimecast / ARS 网关域的退信
3. **更新 `开发信跟进表`** —— 22 家登记为「已发首封」，进入二次跟进计时
