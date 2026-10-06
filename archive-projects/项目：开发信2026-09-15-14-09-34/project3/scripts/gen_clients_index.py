# -*- coding: utf-8 -*-
"""生成 project3/clients/INDEX.md"""
import re, glob, os, json
from collections import Counter, OrderedDict, defaultdict

ROOT = r"C:\Users\win\WorkBuddy AI\项目：开发信2026-09-15-14-09-34"
CLI = os.path.join(ROOT, "project3", "clients")
td = open(os.path.join(ROOT, "开发信跟进表.md"), encoding="utf-8").read()

blocks = re.split(r"\n### ", td)
rows = []
for b in blocks[1:]:
    lines = b.split("\n")
    m = re.match(r"(\d+)\.\s*(.+)", lines[0].strip())
    if not m: continue
    num, name = int(m.group(1)), m.group(2).strip()
    d = {}
    for ln in lines:
        mm = re.match(r"\|\s*([^|]+?)\s*\|\s*(.*?)\s*\|$", ln)
        if mm and mm.group(1) != "字段": d[mm.group(1)] = mm.group(2)
    fm = re.search(r"\*\*信文件\*\*：`([^`]+)`", b)
    d["_file"] = fm.group(1).split("（")[0].strip() if fm else ""
    rows.append((num, name, d))


def clean(s):
    s = re.sub(r"\*\*|\*|`|★|☆|🔥|⚠️|✅|🔴|⚫|→|~~", "", s or "")
    return re.sub(r"\s+", " ", s).strip()


def trunc(s, n):
    s = clean(s)
    return s[:n] + ("…" if len(s) > n else "")


def buyer_tag(bt):
    b = clean(re.sub(r"（[^）]*）|\([^)]*\)", "", bt))
    if "分销" in b and ("转售" in b or "租赁" in b): return "渠道"
    if "分销" in b or "批发" in b: return "分销商"
    if "合作社" in b: return "合作社"
    if "OEM" in b: return "OEM"
    if "EPC" in b: return "EPC"
    if "咨询" in b: return "咨询"
    if "服务" in b: return "服务商"
    return "承包商"


EXPLICIT_HOOK_RULES = [
    ("PSC 品类直引", ["PSC 6120", "PSC 品类", "PSC 代码"]),
    ("文档备档 for bids", ["文档备档", "for your bids"]),
    ("报审 submittals", ["submittal"]),
    ("工厂测试数据", ["工厂测试数据"]),
    ("测试报告样本", ["测试报告样本", "工厂测试报告", "测试报告"]),
    ("北极交期", ["北极交期", "北极"]),
    ("价格阶梯+MOQ", ["价格阶梯", "MOQ", "批量阶梯", "channel pricing"]),
    ("规格书（分电压）", ["规格书"]),
]
DEFAULT_HOOK = [
    (lambda b, n: "调试" in b or "测试" in b, "工厂测试数据"),
    (lambda b, n: "服务" in b, "工厂测试数据+规格书"),
    (lambda b, n: "分销" in b or "渠道" in b or "批发" in b or "合作社" in b, "价格阶梯+MOQ+交期"),
    (lambda b, n: "EPC" in b, "报审 submittals"),
    (lambda b, n: True, "工厂测试数据+规格书"),
]


def find_explicit_hook(text):
    for p in [r"钩子\s*[=＝]\s*\*\*(.+?)\*\*", r"钩子\s*[：:]\s*\*\*(.+?)\*\*",
              r"\*\*钩子\*\*[：:]?\s*(.+)", r"钩子\s*[：:]\s*(.+)"]:
        m = re.search(p, text)
        if m: return clean(m.group(1))
    return ""


def explicit_class(raw):
    for label, keys in EXPLICIT_HOOK_RULES:
        if raw and any(k in raw for k in keys): return label
    return ""


SLICE_RULES = [
    ("配电变整机", ["配电变整机", "只收配电变"]),
    ("配电变+变电站变", ["配电变 + 变电站变", "变电站变 + 配电变"]),
    ("变电站变整机", ["变电站变整机", "电力/变电站变"]),
    ("变电站+箱变+小控制变", ["变电站变 + 箱变"]),
    ("变电站/特殊规格", ["变电站/特殊规格"]),
    ("工业配电变", ["工业配电变"]),
    ("中压配电变", ["中压配电变"]),
    ("美变齐口+柱上变", ["美变齐口"]),
    ("箱变+柱上变", ["箱变 + 柱上变"]),
    ("整机+逐台测试报告", ["逐台测试报告"]),
    ("整机+维修替换单元", ["维修替换"]),
    ("整机+套管/油/备件", ["套管/油", "耗材复购"]),
    ("新机整机", ["新机整机", "新变压器整机"]),
    ("小变压器(≤500kVA)", ["Small transformers", "小变压器"]),
    ("现品牌外配电变", ["现品牌外"]),
    ("变压器整机(通用)", ["只收变压器", "落点整机", "变压器整机"]),
    ("配电变", ["配电变"]),
]
BODY_MAP = [
    ("substation transformer", "变电站变"), ("substation units", "变电站变"),
    ("padmount", "美变/箱变"), ("pole-mount", "柱上变"), ("pole mount", "柱上变"),
    ("polemount", "柱上变"), ("dry-type", "干变"),
    ("liquid-filled", "液浸"), ("oil-immersed", "液浸"),
    ("distribution transformer", "配电变"),
]


def find_slice(fulltext):
    m = re.search(r"落点[^\n]{0,110}", fulltext)
    if m:
        seg = clean(re.sub(r"^落点句?[：:]?\s*", "", clean(m.group(0))))
        for label, keys in SLICE_RULES:
            if any(k in seg for k in keys): return label
    body = fulltext
    mm = re.search(r"【正文】(.*?)(?:【中文批注】|$)", fulltext, re.S)
    if mm: body = mm.group(1)
    body = body.lower()
    hits = []
    for term, label in BODY_MAP:
        if term in body and label not in hits: hits.append(label)
    return "+".join(hits[:2]) if hits else ""


def find_opening(text):
    m = re.search(r"★{0,3}\s*\*{0,2}开场(?:\s*的设计|设计)?\*{0,2}\s*[：:]\s*(.+)", text)
    if m: return trunc(m.group(1), 46)
    m = re.search(r"开场[^\n]{0,6}(?:用|是|取)(?:了)?\s*(.{4,90})", text)
    if m: return trunc(m.group(1), 46)
    return ""


# 开场兜底：从正文第一句提炼
def opening_fallback(letter, num):
    m = re.search(r"【正文】\s*\n+(.{0,200})", letter, re.S)
    if not m: return "—"
    para = re.sub(r"\s+", " ", m.group(1)).strip()
    # 取第一个正文段落（跳过问候语）
    para = re.sub(r"^(Hi|Hello|Dear)[^,]*,?\s*", "", para)
    return trunc(para, 46) or "—"


recs = []
for num, name, d in rows:
    fn = os.path.basename(d["_file"]) if d["_file"] else ""
    p = os.path.join(CLI, fn)
    letter = open(p, encoding="utf-8").read() if fn and os.path.exists(p) else ""
    src = letter + "\n" + d.get("备注", "")
    nm = clean(re.sub(r"（[^）]*）", "", name)).strip()
    bt = buyer_tag(d.get("买家类型", ""))

    eh = find_explicit_hook(src)
    ec = explicit_class(eh)
    is_explicit = bool(ec)
    if not ec:
        for cond, hook in DEFAULT_HOOK:
            if cond(bt, nm):
                ec = hook; break

    op = find_opening(letter)
    if not op and letter:
        op = opening_fallback(letter, num)

    # 国家/州：取「州 + 城市」前两段，去掉括号补注与长解释
    ctry = clean(d.get("国家/地区", "")).replace("美国 · ", "").replace("加拿大 · ", "")
    ctry = re.sub(r"（[^）]*）|\([^)]*\)", "", ctry)
    parts = [p.strip() for p in re.split(r"[／/、，,]", ctry) if p.strip()]
    ctry = " · ".join(parts[:2])[:26]

    recs.append(OrderedDict(
        num=num, name=nm, buyer=bt,
        skel=(clean(d.get("骨架", "-")).split("（")[0].split("(")[0].strip() or "-")[:3],
        country=ctry,
        hook=ec or "—", explicit=is_explicit,
        slice=find_slice(letter) or "—",
        opening=op or "—",
        status=clean(d.get("状态", "")), nxt=clean(d.get("下次跟进日", "")),
        file=fn,
    ))

print("TOTAL", len(recs))
print("切片—:", [(r["num"], r["name"][:12]) for r in recs if r["slice"] == "—"])
print("开场—:", [r["num"] for r in recs if r["opening"] == "—"])
json.dump(recs, open(os.path.join(ROOT, ".workbuddy-ai", "tmp", "recs.json"), "w",
          encoding="utf-8"), ensure_ascii=False, indent=1)
print("saved", len(recs))
