# batch6 合并投递排程表（首封 23 + 跟进 21 = 44 封）

> 队列：`发信队列.json` ｜ 生成：`定时发送.py --build --batch6-all`
> 目标：客户**当地工作日 09:00–10:00** 送达 ｜ **跨时区同刻已去重**（无两封同分钟）
> 定时任务：`batch6 定时投递（首封23 + 跟进21 = 44 封）`（每小时唤醒 + 小时内循环）

## 按时区汇总

| 时区 | 封数 | 北京窗口 | 当地送达 |
|---|---|---|---|
| AT 大西洋 | 2 | 09-29 20:15 – 20:45 | 09:15 – 09:45 |
| ET 美东 | 13 | 09-29 21:00 – 21:56 | 09:00 – 09:56 |
| CT 美中 | 12 | 09-29 22:00 – 22:55 | 09:00 – 09:55 |
| MT 美山 | 6 | 09-29 23:05 – 23:55 | 09:05 – 09:55 |
| PT 美西 | 7 | 09-30 00:00 – 00:55 | 09:00 – 09:55 |
| AZ 亚利桑那 | 2 | 09-30 00:15 – 00:45 | 09:15 – 09:45 |
| AK 阿拉斯加 | 2 | 09-30 01:15 – 01:45 | 09:15 – 09:45 |

**合计 44 封**，跨度 **北京 09-29 20:15 → 09-30 01:45**。

---

## 全量明细

| # | 北京 | 当地 | 时区 | 类型 | 收件人 | 信件 |
|---|---|---|---|---|---|---|
| 1 | 09-29 20:15 | 09:15 | AT | 首封 | `gwoodman@mcloughlans.ca` | McLoughlan-Supplies |
| 2 | 09-29 20:45 | 09:45 | AT | 首封 | `barattod@sourceatlantic.ca` | Source-Atlantic |
| 3 | 09-29 21:00 | 09:00 | ET | 首封 | `louis.vining@colonialelectricsupply.com` | Colonial-Electric |
| 4 | 09-29 21:04 | 09:04 | ET | 首封 | `gwillis@etcinc.net` | Every-Thing-Construction |
| 5 | 09-29 21:08 | 09:08 | ET | 首封 | `planthier@groupedeschenes.com` | Groupe-Deschenes |
| 6 | 09-29 21:16 | 09:16 | ET | 首封 | `austin.sparks@loebelectric.com` | Loeb-Electric |
| 7 | 09-29 21:20 | 09:20 | ET | 首封 | `jmole@province-electric.com` | Province-Electric |
| 8 | 09-29 21:24 | 09:24 | ET | 首封 | `Frank.Johnson@ISGInc.com` | RE-Warner-Associates |
| 9 | 09-29 21:28 | 09:28 | ET | 跟进 | `owners@aequitaspower.com` | 跟进-Aequitas-Power |
| 10 | 09-29 21:32 | 09:32 | ET | 跟进 | `cara.backman@franklinempire.com` | 跟进-Franklin-Empire |
| 11 | 09-29 21:36 | 09:36 | ET | 跟进 | `andre.odeh@guillevin.com` | 跟进-Guillevin |
| 12 | 09-29 21:40 | 09:40 | ET | 跟进 | `estimating@kraun.ca` | 跟进-Kraun-Electric |
| 13 | 09-29 21:48 | 09:48 | ET | 跟进 | `aaron.dlugos@monvalleyintegration.com` | 跟进-MVI-Mon-Valley |
| 14 | 09-29 21:52 | 09:52 | ET | 跟进 | `tbrady@wewireu.com` | 跟进-Progressive-Electric |
| 15 | 09-29 21:56 | 09:56 | ET | 跟进 | `act@stateelectric.com` | 跟进-State-Electric-Supply |
| 16 | 09-29 22:00 | 09:00 | CT | 首封 | `rkunkel@butlersupply.com` | Butler-Supply |
| 17 | 09-29 22:05 | 09:05 | CT | 首封 | `ecavazos@cavaelectric.com` | Cava-Electric |
| 18 | 09-29 22:10 | 09:10 | CT | 首封 | `charlie.ferrara@dynagrid.com` | DynaGrid |
| 19 | 09-29 22:15 | 09:15 | CT | 首封 | `john.sutton@expanseelectrical.com` | Expanse-Electrical |
| 20 | 09-29 22:20 | 09:20 | CT | 首封 | `lvillarreal@primepower.services` | Prime-Power-Services |
| 21 | 09-29 22:25 | 09:25 | CT | 首封 | `david.dowd@netwes.com` | Wholesale-Electric-Supply |
| 22 | 09-29 22:30 | 09:30 | CT | 跟进 | `info@echoelectric.com` | 跟进-Echo-Electric |
| 23 | 09-29 22:35 | 09:35 | CT | 跟进 | `info@eganco.com` | 跟进-Egan-Company |
| 24 | 09-29 22:40 | 09:40 | CT | 跟进 | `paul.guerryelectric@gmail.com` | 跟进-Guerry-Electric |
| 25 | 09-29 22:45 | 09:45 | CT | 跟进 | `Dave@technicalpowerservices.com` | 跟进-Technical-Power-Services |
| 26 | 09-29 22:50 | 09:50 | CT | 跟进 | `CedarRapids@vanmeterinc.com` | 跟进-Van-Meter |
| 27 | 09-29 22:55 | 09:55 | CT | 跟进 | `tpotts@wtei.us` | 跟进-Wolfe-and-Travis-Electric |
| 28 | 09-29 23:05 | 09:05 | MT | 首封 | `don@albertabreaker.net` | Alberta-Breaker |
| 29 | 09-29 23:15 | 09:15 | MT | 首封 | `dowens@incomelectric.com` | InCom-Electric |
| 30 | 09-29 23:25 | 09:25 | MT | 跟进 | `businessdevelopment@cve.com` | 跟进-Cache-Valley-Electric |
| 31 | 09-29 23:35 | 09:35 | MT | 跟进 | `wmyers@iconicpowersystems.com` | 跟进-Iconic-Power |
| 32 | 09-29 23:45 | 09:45 | MT | 跟进 | `help@summit.com` | 跟进-Summit-Electric |
| 33 | 09-29 23:55 | 09:55 | MT | 跟进 | `ksones@valard.com` | 跟进-Valard-Construction |
| 34 | 09-30 00:00 | 09:00 | PT | 首封 | `brian@compasselectric.net` | Compass-Electric |
| 35 | 09-30 00:10 | 09:10 | PT | 首封 | `tmyers@hotlineconstructioninc.com` | Hot-Line-Construction |
| 36 | 09-30 00:15 | 09:15 | AZ | 首封 | `eistanbouly@americanlineconstruction.com` | American-Line-Construction |
| 37 | 09-30 00:20 | 09:20 | PT | 首封 | `kmalouf@mainelectricsupply.com` | Main-Electric-Supply |
| 38 | 09-30 00:30 | 09:30 | PT | 首封 | `cpaquin@sascocontractors.com` | Sasco-Contractors |
| 39 | 09-30 00:35 | 09:35 | PT | 首封 | `drew@tidalelectrical.ca` | Tidal-Electrical |
| 40 | 09-30 00:45 | 09:45 | AZ | 首封 | `jbarriger@stationpwr.com` | Station-Power-Construction |
| 41 | 09-30 00:50 | 09:50 | PT | 跟进 | `utilitydivision@walterswholesale.com` | 跟进-Walters-Wholesale |
| 42 | 09-30 00:55 | 09:55 | PT | 跟进 | `zac.kady@zeuselectric.ca` | 跟进-Zeus-Electric |
| 43 | 09-30 01:15 | 09:15 | AK | 跟进 | `jamesz@northernpowerline.com` | 跟进-Chatham-Electric |
| 44 | 09-30 01:45 | 09:45 | AK | 跟进 | `info@megawattelectric.com` | 跟进-Megawatt-Electric |

## 发送前闸门（均已通过）

| 闸门 | 结果 |
|---|---|
| 红线自检 | ✅ 44/44 通过 |
| 退信闸门 | ✅ 0 命中（含 2 个整域封锁）|
| 窗口合规 | ✅ 44 封当地送达**全部落在 09:00–10:00** |
| 同刻去重 | ✅ **0 处同分钟冲突** |
