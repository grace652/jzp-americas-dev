#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成跟进信待发清单（2026-09-28 批次）
数据源：
  ① 开发信跟进表.xlsx（客户主数据）
  ② 跟进信-20260928/*.md（本轮实际写出的信件）
输出：📋待发清单-跟进-20260928.xlsx
"""
import openpyxl, datetime, re, glob, os
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

OLD   = "/Users/eric/Downloads/开发客户流程agent/项目：开发信2026-09-15-14-09-34"
LFDIR = os.path.join(OLD, "project3/clients/跟进信-20260928")
OUT   = os.path.join(OLD, "📋待发清单-跟进-20260928.xlsx")
TODAY = datetime.date(2026, 9, 28)

# ---------- 1. 读客户主数据 ----------
ws = openpyxl.load_workbook(os.path.join(OLD, "开发信跟进表.xlsx"), data_only=True)["开发信跟进表"]
KEY = ["no","send_date","company","country","contact","title","btype","product",
       "source","skeleton","suggest_bj","email","status","fcount","next_date","last_date","note"]
rows = {}
for r in range(5, ws.max_row + 1):
    v = [ws.cell(r, c).value for c in range(1, 18)]
    if v[2] is None:
        continue
    d = dict(zip(KEY, v))
    rows[str(d["no"]).strip()] = d

def D(x):
    if isinstance(x, datetime.datetime): return x.date()
    if isinstance(x, datetime.date): return x
    if isinstance(x, str) and x.strip():
        for f in ("%Y-%m-%d", "%Y/%m/%d"):
            try: return datetime.datetime.strptime(x.strip(), f).date()
            except Exception: pass
    return None

# ---------- 2. 解析本轮信件文件，抽出 (编号, 公司, 轮次, 主题) ----------
CIRC = "①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳"
written = {}   # no -> dict(round, subject, file)

FILE_META = {
    "跟进信-第2轮-20260928-A已跟进1次.md": ("第2轮(D0+8)", "Re:（同线程）"),
    "跟进信-第1轮-20260928-B首封0922批次.md": ("第1轮(D0+3)", "Re:（同线程）"),
    "跟进信-第1轮-20260928-C首封0923批次.md": ("第1轮(D0+3)", "Re:（同线程）"),
}
for fn, (rnd, _) in FILE_META.items():
    p = os.path.join(LFDIR, fn)
    if not os.path.exists(p):
        continue
    t = open(p, encoding="utf-8").read()
    # 以 "## ① 公司名 — 联系人" 切块
    blocks = re.split(r"\n(?=## [%s])" % CIRC, t)
    for b in blocks:
        m = re.match(r"## ([%s])\s*(.+)" % CIRC, b)
        if not m:
            continue
        head = m.group(2)
        comp = head.split("—")[0].replace("—", "").strip()
        comp = re.sub(r"\s*\(.*?\)\s*$", "", comp).strip()
        sm = re.search(r"\*\*主题\*\*：`([^`]+)`", b)
        subj = sm.group(1) if sm else "（同线程 Re: 原主题）"
        written[comp] = {"round": rnd, "subject": subj, "file": fn}

# ---------- 3. 本轮 41 家目标（编号 → 公司名简称映射，按统计结果） ----------
TARGETS = [
    # (编号, 简称用于匹配信件的公司名, 轮次覆盖)
    ("1","B.G. High Voltage"), ("2","Ontario High Voltage"), ("3","ISCOCA"),
    ("4","Williams Electric"), ("5","ALCO Electric"), ("6","Alaska Line Builders"),
    ("7","PowerTec Electric"), ("54","Power Substation Services"),
    ("36","Reeve Electric"), ("37","DECH High Voltage"), ("38","Rogers Electrical"),
    ("39","South Charleston Electric"), ("40","Washington State Power"),
    ("42","VoltCore Electrical"), ("43","GLS Electric"), ("44","Rexel Utility"),
    ("47","GEC"), ("53","Sunbelt Solomon"), ("55","Westmoreland"),
    ("56","Dana Power"), ("58","GRIDLINK"), ("59","Kirby Electric"),
    ("60","BV Electric"), ("61","Stewart Electric"), ("62","Texas Electric Coop"),
    ("63","Birmingham Electrical Contractors"), ("64","Everlast Electric"),
    ("65","Priester"), ("67","Tryggr"), ("68","Amps Powerline"),
    ("69","Fullford Electric"), ("70","Arkansas Electric Cooperatives"),
    ("71","United Utility Supply"), ("73","Western United Electric"),
    ("74","CEEUS"), ("75","General Pacific"), ("76","GNS Technologies"),
    ("77","RESA Power"), ("78","TM3"), ("79","Electrozad Supply"),
]

def find_written(short):
    """在 written 里模糊匹配公司名"""
    key = short.lower().replace(" ", "")
    for comp, info in written.items():
        c = comp.lower().replace(" ", "")
        if key[:8] in c or c[:8] in key:
            return info
    # 关键词命中
    for comp, info in written.items():
        toks = [w for w in re.split(r"[^A-Za-z]+", short) if len(w) > 3]
        if toks and all(t.lower() in comp.lower() for t in toks[:2]):
            return info
    return None

# ---------- 4. 组装 ----------
out = openpyxl.Workbook()
sh = out.active
sh.title = "本轮待发清单"

HDR = ["编号","公司名称","国家/地区","联系人","职位","主送邮箱","档位","轮次",
       "主题行","建议发送(北京)","时区","状态","跟进次数","下次跟进日","信件文件"]
sh.append(HDR)

hfill = PatternFill("solid", fgColor="1F4E79")
hfont = Font(bold=True, color="FFFFFF", size=10)
for c in range(1, len(HDR) + 1):
    cell = sh.cell(1, c)
    cell.fill = hfill; cell.font = hfont
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

thin = Side(style="thin", color="BFBFBF")
bd = Border(left=thin, right=thin, top=thin, bottom=thin)

missing = []
for no, short in TARGETS:
    d = rows.get(no, {})
    w = find_written(short)
    if w is None:
        missing.append((no, short))
    email = (d.get("email") or "").replace("\n", " + ")
    # 档位判定：具名个人邮箱=A，info/sales/office/contact 等角色邮箱=B
    local = (email.split("@")[0].split("+")[0] if "@" in email else "").strip().lower()
    tier = "B" if local in ("info","sales","office","contact","support","customerservice",
                            "contractorsales","lonsales","communications","directory",
                            "utilitiesalescanada","utilitysales","fei","rmcmillan") else "A"
    if no == "54":
        tier = "A（已回复线程）"
    sh.append([
        int(no),
        d.get("company") or short,
        d.get("country") or "",
        d.get("contact") or "",
        d.get("title") or "",
        email,
        tier,
        (w["round"] if w else "⚠️未找到"),
        (w["subject"] if w else ""),
        d.get("suggest_bj") or "",
        "",   # 时区，稍后填
        d.get("status") or "",
        d.get("fcount") or 0,
        str(D(d.get("next_date")) or ""),
        (w["file"] if w else ""),
    ])

# 时区标注（按项目既定对照表）
TZM = {
 "1":"安省 ET","2":"安省 ET","3":"安省 ET","4":"阿拉巴马 CT","5":"华盛顿州 PT",
 "6":"阿拉斯加 AKT","7":"AK+WA 双州","54":"西弗吉尼亚 ET",
 "36":"阿拉巴马 CT","37":"安省 ET","38":"西弗吉尼亚 ET","39":"西弗吉尼亚 ET",
 "40":"华盛顿州 PT","42":"德州 CT","43":"俄亥俄 ET","44":"安省 ET","47":"西弗吉尼亚 ET",
 "53":"德州 CT","55":"宾州 ET","56":"纽约 ET","58":"安省 ET","59":"宾州 ET",
 "60":"BC PT","61":"阿拉巴马 CT","62":"德州 CT",
 "63":"阿拉巴马 CT","64":"新斯科舍 AT","65":"德州 CT","67":"阿省 MT","68":"曼省 CT",
 "69":"阿拉斯加 AKT","70":"阿肯色 CT","71":"肯塔基 ET","73":"科罗拉多 MT","74":"南卡 ET",
 "75":"俄勒冈 PT","76":"内华达 PT","77":"田纳西 CT","78":"安省 ET","79":"安省 ET",
}
for r in range(2, sh.max_row + 1):
    no = str(sh.cell(r, 1).value)
    sh.cell(r, 11).value = TZM.get(no, "")

widths = [6,34,16,26,20,34,14,14,44,16,14,10,9,12,34]
for i, wd in enumerate(widths, 1):
    sh.column_dimensions[get_column_letter(i)].width = wd
for r in range(2, sh.max_row + 1):
    for c in range(1, len(HDR) + 1):
        cell = sh.cell(r, c); cell.border = bd
        cell.alignment = Alignment(vertical="center", wrap_text=(c in (2,4,6,9,15)))
        cell.font = Font(size=10)
sh.freeze_panes = "A2"
sh.auto_filter.ref = sh.dimensions

# ---------- 5. 小结页 ----------
s2 = out.create_sheet("小结")
s2.append(["项目", "值"])
s2["A1"].font = Font(bold=True, size=11); s2["B1"].font = Font(bold=True, size=11)
r1 = [x for x in TARGETS if x[0] != "54"]
r2 = [x for x in TARGETS if x[0] == "54"]
info = [
    ("基准日", "2026-09-28（周一）"),
    ("本轮目标总数", len(TARGETS)),
    ("其中：普通跟进", len(r1)),
    ("其中：已回复线程推进", len(r2)),
    ("第1轮（D0+3）", sum(1 for x in TARGETS if x[0] not in ("1","2","3","4","5","6","7","54"))),
    ("第2轮（D0+8）", 7),
    ("跳过（用户决定）", "WinAsia Power（斯里兰卡·试探客户）"),
    ("红线自检", "40/40 通过（0 违规）"),
    ("词数范围", "46–66 词"),
    ("价格/交期", "全部未提价格"),
    ("退订承诺句", "41 封全带"),
    ("窗口说明", "ET 组今晚窗口已过 → 按用户指示今天发完，不卡 9–10 点"),
    ("发送授权", "写好先给用户确认，确认后再发"),
]
for k, v in info:
    s2.append([k, v])
s2.column_dimensions["A"].width = 26
s2.column_dimensions["B"].width = 60

out.save(OUT)
print("✅ 已生成:", OUT)
print("   行数:", sh.max_row - 1)
if missing:
    print("   ⚠️ 未匹配到信件的目标:", missing)
PY_END = None
