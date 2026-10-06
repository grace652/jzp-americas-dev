#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
阶段 1a（v2）：构建跟进表新 sheet 的 92 行数据（batch5 + batch6）

v2 修正（v1 实测发现的问题）：
  1. 买家类型正则漏了 `**` —— `- **买家类型**：` 匹配不到
  2. 169–173 用**第三种格式**（表格制，无核心字段代码块）→ 加专门分支
  3. `非分销商` 这类否定词会误命中 → 先剔除否定短语再匹配
  4. 需求产品要只取反引号里的品类名，不要带描述
  5. 国家/地区要归一为 `加拿大 · BC（Castlegar）` 风格

输出：/tmp/new_rows.json + /tmp/new_rows.tsv
铁律：提不到的写「（未获取）」，绝不编造。
"""
import json, re, glob, os
from datetime import date, timedelta
from pathlib import Path
from collections import Counter

ROOT = Path("/Users/eric/WorkBuddy AI/2026-09-27-00-43-30/jzp-americas-dev")
HANDOFF_DIRS = [ROOT / "开发信项目/交接单/batch5_new_129plus",
                ROOT / "开发信项目/交接单/batch6_new_174plus"]
CLIENTS = ROOT / "开发信项目/clients"
QUEUE_FILES = [ROOT / "发信队列.json",
               ROOT / "发信队列.json.bak-batch5已发38封",
               ROOT / "发信队列-batch5备份.json",
               ROOT / "发信队列-batch5剩余.json"]
NOT_FOUND = "（未获取）"
NO_LETTER = "—（未写信）"


def clean(s):
    s = str(s or "")
    s = re.sub(r"\*\*|`|~~", "", s).replace("&nbsp;", " ")
    return re.sub(r"\s+", " ", s).strip()


def sec(text, title, lvl=r"#{2,4}"):
    m = re.search(rf"^{lvl}\s*{re.escape(title)}[^\n]*\n(.*?)(?=\n#{{2,4}}\s|\Z)", text, re.S | re.M)
    return m.group(1).strip() if m else ""


def rows_of(body):
    """把「标准字段明细」解析成 [(k, v), ...]。

    🔴 必须同时支持两种形态：
       · batch5 及更早 = markdown 表格 `| **国家 + 城市** | … |`
       · batch6        = **项目符号列表** `- 国家+城市：…`（实测踩过：只认表格会整段漏掉）
    """
    out = []
    for m in re.finditer(r"^\|\s*(.+?)\s*\|\s*(.+?)\s*\|", body, re.M):
        k, v = clean(m.group(1)), clean(m.group(2))
        if k and k not in ("项", "字段", "层级", "---") and not set(k) <= set("-: "):
            out.append((k, v))
    for m in re.finditer(r"^\s*[-*]\s*\**([^：:*]+?)\**\s*[：:]\s*(.+)$", body, re.M):
        k, v = clean(m.group(1)), clean(m.group(2))
        if k:
            out.append((k, v))
    return out


# ------------------------------------------------------------ 核心字段（三种格式）
def parse_core(text):
    body = sec(text, "一、核心字段")
    out = {}
    if body:
        cb = re.search(r"```[^\n]*\n(.*?)```", body, re.S)
        if cb:
            lines = [l for l in cb.group(1).split("\n") if l.strip()]
            if len(lines) >= 2:
                names = [clean(x) for x in lines[0].split("|")]
                vals = [clean(x) for x in lines[1].split("|")]
                out = dict(zip(names, vals + [""] * (len(names) - len(vals))))
        if not out:
            for k, v in rows_of(body):
                out.setdefault(k, v)
    # 第三种格式（169–173）：无「一、核心字段」，改用「二、公司基本档案」+「一、身份与定性」
    if not out.get("公司名"):
        b2 = sec(text, "二、公司基本档案")
        for k, v in rows_of(b2):
            if "公司全称" in k:
                out["公司名"] = v
            elif "总部地址" in k or "注册地址" in k:
                out.setdefault("详细地址", v)
    # 第三种格式补人：`## 四、决策人清单` 取首个具名 + `## 五、邮箱验证` 取首个邮箱
    if not out.get("联系人姓名"):
        b4 = sec(text, "四、决策人清单（★ 核心产出）") or sec(text, "四、决策人清单")
        m = re.search(r"\*\*([A-Z][A-Za-z.\-']+(?:\s+[A-Z][A-Za-z.\-']+){0,3})\*\*", b4)
        if not m:
            m = re.search(r"\|\s*\**([A-Z][A-Za-z.\-']+(?:\s+[A-Z][A-Za-z.\-']+){0,3})\**\s*\|", b4)
        if m:
            out["联系人姓名"] = clean(m.group(1))
    # 第三种格式补人（变体）：`## 二、公司基本档案` 里「职位 | 姓名」型表格
    #   ⚠️ rows_of 已剥掉 `**`，所以这里**不能**要求加粗（实测踩过）
    if not out.get("联系人姓名"):
        b2 = sec(text, "二、公司基本档案")
        NAME_RE = re.compile(r"^([A-Z][A-Za-z.\-']+(?:\s+[A-Z][A-Za-z.\-']+){0,3})")
        for k, v in rows_of(b2):
            if re.search(r"(President|CEO|Owner|Founder|决策人|联系人|Manager|Director)", k, re.I):
                m = NAME_RE.match(v.strip())
                if m and len(m.group(1)) > 4:
                    out["联系人姓名"] = clean(m.group(1))
                    out.setdefault("职位", k)
                    break
    if not out.get("邮箱"):
        b5 = sec(text, "五、邮箱验证（SMTP 三点式探测）") or sec(text, "五、邮箱验证")
        m = re.search(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}", b5 or text)
        if m:
            out["邮箱"] = m.group(0)
    return out


def pick_type(text, core):
    """买家类型（多级 fallback）。返回 (归一值, 原始值)"""
    # A) 「### 买家类型 / 需求品类」段
    b = sec(text, "买家类型 / 需求品类")
    m = re.search(r"买家类型\**\s*[：:]\s*(.+)", b) if b else None
    if m:
        return norm_buyer(clean(m.group(1))), clean(m.group(1))
    # B) 第三种格式：`| ① 类型匹配 | ✅ **B 类 分销商/贸易商** |`
    m = re.search(r"类型匹配[^\n]*?\|\s*(.+)", text)
    if m:
        v = clean(m.group(1))
        return norm_buyer(v), v
    # C) 名单来源行：「A 类 · 电气承包商/工程公司」或「A 类（电气承包商）」
    hdr = text.split("\n---")[0]
    m = re.search(r"[AB]\s*类\s*(?:[·・]\s*([^；;，,）)\n]+)|[（(]\s*([^）)\n]+))", hdr)
    if m:
        v = clean(m.group(1) or m.group(2))
        return norm_buyer(v), v
    return "其他", ""


def pick_products(text):
    """需求产品：多级 fallback。只取品类名，不带描述。"""
    b = sec(text, "买家类型 / 需求品类")
    if b:
        items = [clean(x) for x in re.findall(r"`([^`]{4,60})`", b)
                 if "UL" in x or "变" in x or "kVA" in x or "MVA" in x]
        if not items:
            items = [clean(x) for x in re.findall(r"`([^`]{4,60})`", b)][:2]
        if items:
            return "；".join(items[:2])
    # 🔴 fallback：旧格式没有该段，但 `### 🔴 第一发现：…` 标题里常带品类
    m = re.search(r"^#{3,4}\s*(?:🔴|⚠️|🔥)?\s*第一(?:发现|判断)[：:]\s*(.+)$", text, re.M)
    if m:
        v = clean(m.group(1))
        # 过滤「信号弱」「未获取」这类警告语，它们不是品类
        if any(k in v for k in ("变压器", "变电站", "变")) and not re.search(r"(信号弱|未获取|未找到|存疑)", v):
            return v[:60]
    # 🔴 末级 fallback：核心字段「背调摘要」里找含品类的短句
    body = sec(text, "一、核心字段")
    cb = re.search(r"```[^\n]*\n(.*?)```", body, re.S) if body else None
    if cb:
        lines = [l for l in cb.group(1).split("\n") if l.strip()]
        if len(lines) >= 2:
            vals = [clean(x) for x in lines[1].split("|")]
            for v in vals:
                for seg in re.split(r"[；;。]", v):
                    if any(k in seg for k in ("变压器", "变电站", "美变", "柱上变")) and len(seg) < 80:
                        return seg.strip()[:60]
    return NOT_FOUND


# ------------------------------------------------------------ 类型/来源归一
PROV = [("British Columbia", "BC"), ("Alberta", "AB"), ("Saskatchewan", "SK"),
        ("Manitoba", "MB"), ("Ontario", "ON"), ("Quebec", "QC"), ("Québec", "QC"),
        ("Nova Scotia", "NS"), ("New Brunswick", "NB"), ("Newfoundland", "NL"),
        ("Prince Edward Island", "PE"), ("不列颠哥伦比亚", "BC"), ("安大略", "ON"),
        ("魁北克", "QC"), ("阿省", "AB"), ("亚伯达", "AB"), ("曼省", "MB"),
        ("萨省", "SK"), ("新斯科舍", "NS"), ("新不伦瑞克", "NB"), ("纽芬兰", "NL")]


CITY_STOP = {"总部", "分公司", "总部语境", "办公", "仓库", "等", "同上"}


US_STATES = {
    "Alabama": "AL", "Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR", "California": "CA",
    "Colorado": "CO", "Connecticut": "CT", "Delaware": "DE", "Florida": "FL", "Georgia": "GA",
    "Hawaii": "HI", "Idaho": "ID", "Illinois": "IL", "Indiana": "IN", "Iowa": "IA",
    "Kansas": "KS", "Kentucky": "KY", "Louisiana": "LA", "Maine": "ME", "Maryland": "MD",
    "Massachusetts": "MA", "Michigan": "MI", "Minnesota": "MN", "Mississippi": "MS",
    "Missouri": "MO", "Montana": "MT", "Nebraska": "NE", "Nevada": "NV",
    "New Hampshire": "NH", "New Jersey": "NJ", "New Mexico": "NM", "New York": "NY",
    "North Carolina": "NC", "North Dakota": "ND", "Ohio": "OH", "Oklahoma": "OK",
    "Oregon": "OR", "Pennsylvania": "PA", "Rhode Island": "RI", "South Carolina": "SC",
    "South Dakota": "SD", "Tennessee": "TN", "Texas": "TX", "Utah": "UT", "Vermont": "VT",
    "Virginia": "VA", "Washington": "WA", "West Virginia": "WV", "Wisconsin": "WI",
    "Wyoming": "WY",
}
STATE_CODES = "BC AB SK MB ON QC NS NB NL PE AL AK AZ AR CA CO CT DE FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN MS MO MT NE NV NH NJ NM NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA WA WV WI WY".split()


def find_prov(scope):
    """在给定文本里找州省（全称优先，再 2 字母码）。"""
    for name, ab in list(PROV) + list(US_STATES.items()):
        if name in scope:
            return ab
    m = re.search(r"\b(" + "|".join(STATE_CODES) + r")\b", scope)
    return m.group(1) if m else ""


def norm_country(raw, text, core=None):
    """归一为 `加拿大 · BC`（国家 · 州省两段，与老 sheet D 列同风格）。

    🔴 v2：batch6 交接单没有「标准字段明细」的国家字段，州省只在**背调摘要**里。
    🔴 v3：省/市必须走**严格白名单**（实测踩过「加拿大 · 150+ 年，342 人」）。
    🔴 v4：**不再拼城市** —— 括号内容常是「A 类 · ⭐ 高价值档」这类垃圾。
    🔴 v5：`标准字段明细` 在 batch6 是**项目符号列表**而非表格 → rows_of 已双格式支持。
    """
    raw = clean(raw)
    corpus = " ".join([raw, clean((core or {}).get("背调摘要", "")), text[:4000]])

    def _ctry(scope):
        if "加拿大" in scope or "Canada" in scope:
            return "加拿大"
        if "美国" in scope or re.search(r"\b(US|USA|United States)\b", scope):
            return "美国"
        if "墨西哥" in scope:
            return "墨西哥"
        return ""

    # 🔴 国家判定优先级：① 「国家+城市」字段 ② **头部批次行**（batch5 旧格式常写
    #    「第六批 · 美国 B 类」）③ 全文语料。
    #    实测：直接扫全文会把美国客户误判成加拿大（正文常写「美加双证 / US and Canada」）。
    ctry = _ctry(raw)
    if not ctry:
        ctry = _ctry(text[:400])
    if not ctry:
        ctry = _ctry(corpus)
    # 州省：① 先查「国家+城市」字段本身 ② 再查国家名后 80 字窗口 ③ 最后全语料
    prov = find_prov(raw)
    if not prov and ctry:
        m = re.search(rf"{ctry}[^\n|]{{0,80}}", corpus)
        if m:
            prov = find_prov(clean(m.group(0)))
    if not prov:
        prov = find_prov(corpus)
    parts = [p for p in (ctry, prov) if p]
    return " · ".join(parts) if parts else NOT_FOUND


BUYER_MAP = [("分销", "分销商"), ("批发", "批发商"), ("EPC", "EPC工程商"),
             ("盘厂", "盘厂"), ("开关柜", "盘厂"), ("电力公司", "电力公司"),
             ("公用事业", "电力公司"), ("合作社", "电力公司"), ("工厂", "工厂自用"),
             ("制造", "工厂自用"), ("贸易", "贸易商"), ("代理", "贸易商"),
             ("承包商", "终端承包商"), ("承包", "终端承包商"), ("施工", "终端承包商")]
SRC_MAP = [("官网", "官网"), ("名录", "名录"), ("协会", "名录"), ("LinkedIn", "LinkedIn"),
           ("linkedin", "LinkedIn"), ("展会", "展会"), ("询盘", "询盘"),
           ("搜索", "搜索引擎"), ("推荐", "推荐")]


def norm_buyer(raw):
    r = clean(raw)
    # 🔴 剔除否定短语（「非分销商」「非制造商」会误命中）
    r = re.sub(r"非[^，,。；;、）)]{1,6}", "", r)
    for kw, val in BUYER_MAP:
        if kw in r:
            return val
    return "其他"


def norm_src(raw):
    r = clean(raw)
    hits = []
    for kw, val in SRC_MAP:
        if kw in r and val not in hits:
            hits.append(val)
    return "+".join(hits[:2]) if hits else NOT_FOUND


# ------------------------------------------------------------ 发送记录
def load_sent():
    sent, allsent = {}, []
    for f in QUEUE_FILES:
        if not f.exists():
            continue
        try:
            items = json.loads(f.read_text(encoding="utf-8"))
        except Exception:
            continue
        for it in items:
            if it.get("status") != "sent" or not it.get("sent_at"):
                continue
            d = str(it["sent_at"])[:10]
            for a in it.get("to", []):
                a = a.strip().lower()
                if a:
                    allsent.append((a, it.get("letter", ""), d))
                    if a not in sent or d < sent[a]:
                        sent[a] = d
    return sent, allsent


def workday_add(d0, n):
    d, k = d0, 0
    while k < n:
        d += timedelta(days=1)
        if d.weekday() < 5:
            k += 1
    return d


NEXT_AFTER = {0: 3, 1: 8, 2: 15, 3: 25}


def main():
    sent_map, allsent = load_sent()
    print(f"发送记录：{len(sent_map)} 地址 / {len(allsent)} 条")
    rows, n = [], 116
    for hd in HANDOFF_DIRS:
        for f in sorted(hd.glob("买家*.md")):
            m = re.match(r"买家(\d+)_(.+?)_开发信交接单\.md$", f.name)
            if not m:
                continue
            buyer = int(m.group(1))
            text = f.read_text(encoding="utf-8")
            core = parse_core(text)
            std = dict(rows_of(sec(text, "标准字段明细")))

            tm = re.search(r"^#\s*(?:【买家\s*\d+】开发信交接单\s*—|买家\s*\d+\s*—)\s*(.+)$", text, re.M)
            company = clean(core.get("公司名") or (tm.group(1) if tm else f.stem))
            email = clean(core.get("邮箱", ""))
            dz = re.search(r"邮箱档位[：:]\s*\**([ABC][+−\-]?)", text)
            tier = dz.group(1) if dz else ""

            btype, braw = pick_type(text, core)
            prod = pick_products(text)
            country = norm_country(core.get("国家 + 城市") or core.get("国家+城市") or
                                   next((v for k, v in std.items() if "国家" in k), ""), text, core)
            source = norm_src(core.get("信息来源", ""))

            # 找信件
            letter, skel, window = None, NO_LETTER, ""
            for cand in CLIENTS.glob("开发信-*.md"):
                if "跟进" in cand.name:
                    continue
                if f"买家 {buyer}" in cand.read_text(encoding="utf-8", errors="replace") or \
                   f"买家{buyer}" in cand.read_text(encoding="utf-8", errors="replace"):
                    letter = cand
                    break
            if letter is None:
                key = re.sub(r"[^a-z0-9]", "", company.lower())[:14]
                for cand in CLIENTS.glob("开发信-*.md"):
                    if "跟进" not in cand.name and key and key in re.sub(r"[^a-z0-9]", "", cand.name.lower()):
                        letter = cand
                        break
            if letter:
                lt = letter.read_text(encoding="utf-8")
                sm = re.search(r">\s*骨架[：:]\s*(.+)", lt)
                skel = clean(sm.group(1))[:40] if sm else NO_LETTER
                wm = re.search(r">\s*拟发送时段[：:]\s*(.+)", lt)
                if wm:
                    bj = re.search(r"北京\s*([\d:：–\-—~～\s]+?)(?:）|｜|\||$)", wm.group(1))
                    window = clean(bj.group(1)) if bj else clean(wm.group(1))[:36]

            em = [x.lower() for x in re.findall(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}", email)]
            send_date = next((sent_map[a] for a in em if a in sent_map), "")
            fcount = sum(1 for a, ln, d in allsent if "跟进" in ln and a in em)
            # 🔴 停业 / 破产 / 已排除 → 已放弃（不写「待发送」，避免误发）
            dead = bool(re.search(r"(已停业|停业|破产|清盘|接管|receivership|已排除|⛔\s*排除)", text[:2500]))
            if dead:
                status = "已放弃"
            elif send_date:
                status = "已发送"
            else:
                status = "待发送"
            next_date = ""
            if send_date and not dead:
                k = NEXT_AFTER.get(fcount)
                if k:
                    next_date = workday_add(date.fromisoformat(send_date), k).isoformat()

            notes = [f"买家{buyer}"]
            if tier:
                notes.append(f"{tier}档")
            if dead:
                notes.append("⛔ 停业/排除")
            if not letter:
                notes.append("未写信")
            if not send_date and not dead:
                notes.append("待发/排队中")
            if fcount:
                notes.append(f"已跟进{fcount}次")

            n += 1
            rows.append({"#": n, "发送日期": send_date, "公司名称": company, "国家/地区": country,
                         "联系人": clean(core.get("联系人姓名", "")) or NOT_FOUND,
                         "职位": clean(core.get("职位", "")) or NOT_FOUND,
                         "买家类型": btype, "需求产品": prod, "触达来源": source,
                         "骨架": skel, "建议发送时间(北京)": window or NOT_FOUND,
                         "邮箱": email or NOT_FOUND, "状态": status, "跟进次数": fcount,
                         "下次跟进日": next_date, "最后联系日": send_date,
                         "备注 / 下一步": "｜".join(notes),
                         "_buyer": buyer, "_file": f.name, "_letter": letter.name if letter else "",
                         "_braw": braw})

    print(f"构建完成：{len(rows)} 行")
    Path("/tmp/new_rows.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    cols = ["#", "发送日期", "公司名称", "国家/地区", "联系人", "职位", "买家类型", "需求产品",
            "触达来源", "骨架", "建议发送时间(北京)", "邮箱", "状态", "跟进次数", "下次跟进日",
            "最后联系日", "备注 / 下一步"]
    with open("/tmp/new_rows.tsv", "w", encoding="utf-8") as fh:
        fh.write("\t".join(cols) + "\n")
        for r in rows:
            fh.write("\t".join(str(r.get(c, "")).replace("\t", " ") for c in cols) + "\n")

    print(f"公司名为空：{sum(1 for r in rows if not r['公司名称'])}")
    print("状态：", dict(Counter(r["状态"] for r in rows)))
    print("买家类型：", dict(Counter(r["买家类型"] for r in rows)))
    print("有信件：", sum(1 for r in rows if r["_letter"]), "｜有发送日期：", sum(1 for r in rows if r["发送日期"]))
    print("国家未获取：", sum(1 for r in rows if r["国家/地区"] == NOT_FOUND))
    print("产品未获取：", sum(1 for r in rows if r["需求产品"] == NOT_FOUND))


if __name__ == "__main__":
    main()
