#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
project1 · 开工前置检查

职责：在项目1 开始任何推导工作之前，验证数据源是否可用、是否为最新、结构是否变化。
      任何一项不通过 → 明确报错，不进入推导流程。

依据：00_data_source_setup.md §六（读取方式）、§八（数据失效判定）

用法：
    python 00_readiness_check.py
    python 00_readiness_check.py --max-age-days 3     # 默认 3 天
    python 00_readiness_check.py --json               # 机器可读输出

退出码：
    0 = 全部通过（可能有 ⚠️ 警告）
    1 = 有 ⛔ 阻断项，禁止继续
"""

import argparse
import datetime as dt
import json
import os
import re
import sys

# ─────────────────────────────────────────────────────────────
# 数据源 A 契约（🔴 改动必须同步 00_data_source_setup.md）
# ─────────────────────────────────────────────────────────────

XLSX_PATH = (
    r"C:\Users\win\WorkBuddy AI\项目：开发信2026-09-15-14-09-34\开发信跟进表.xlsx"
)
SHEET_NAME = "开发信跟进表"
HEADER_ROW = 4  # 🔴 表头在第 4 行，不是第 1 行
DATA_START_ROW = 5
EXPECTED_COLUMNS = [
    "#",
    "发送日期",
    "公司名称",
    "国家/地区",
    "联系人",
    "职位",
    "买家类型",
    "需求产品",
    "触达来源",
    "骨架",
    "建议发送时间(北京)",
    "邮箱",
    "状态",
    "跟进次数",
    "下次跟进日",
    "最后联系日",
    "备注 / 下一步",
]
# 公司名列（0-based index）
COL_COMPANY = 2
COL_REGION = 3
COL_EMAIL = 11
COL_STATUS = 12

KNOWN_STATUSES = [
    "待发送", "已发送", "已送达", "已回复", "已报价", "已寄样",
    "谈判中", "已成交", "无回应", "已退订（对方拒联）", "已放弃",
]
# 带前缀/后缀修饰的变体（如「已发送（用户 2026-09-17 发出）」「个人处理」），
# 只要以已知状态开头即视为同族，否则报未知。
STATUS_PREFIX_OK = ["个人处理", "已发送", "已退订", "已放弃"]

# 数据源 B 契约
SKILL_DIR = os.path.expanduser(r"~\.workbuddy-ai\skills\jzp-company-knowledge")
SKILL_REQUIRED_FILES = [
    "SKILL.md",
    os.path.join("references", "09-customer-profile.md"),
    os.path.join("references", "02-products.md"),
    os.path.join("references", "01-company.md"),
]

# 排重：公司名标准化时剥离的后缀
CORP_SUFFIXES = [
    "incorporated", "corporation", "company", "limited", "corp",
    "inc", "llc", "ltd", "llp", "plc", "co",
]


# ─────────────────────────────────────────────────────────────
# 工具
# ─────────────────────────────────────────────────────────────

class Report:
    def __init__(self):
        self.items = []

    def ok(self, msg):
        self.items.append(("OK", msg))

    def warn(self, msg):
        self.items.append(("WARN", msg))

    def fail(self, msg):
        self.items.append(("FAIL", msg))

    @property
    def blocked(self):
        return any(lv == "FAIL" for lv, _ in self.items)

    @property
    def has_warn(self):
        return any(lv == "WARN" for lv, _ in self.items)

    def render(self):
        icon = {"OK": "[OK]  ", "WARN": "[WARN]", "FAIL": "[STOP]"}
        lines = ["数据源健康检查", "-" * 52]
        for lv, msg in self.items:
            lines.append("%s %s" % (icon[lv], msg))
        lines.append("-" * 52)
        return "\n".join(lines)


def normalize_company(name):
    """
    公司名标准化 —— 与 00 文件 §5.3 主键规则一致。

    🔴 关键点：必须把连续单字母缩写折叠（b g -> bg），否则
       「B.G. High Voltage Systems Ltd.」与「BG High Voltage Systems」不会被判为同一家。
       这是 2026-09-23 自检发现的真实 bug，勿回退。
    """
    if not name:
        return ""
    s = str(name).lower()
    s = re.sub(r"（[^）]*）|\([^)]*\)", " ", s)   # 去括号注释
    s = re.sub(r"[.,\-_/&']", " ", s)             # 去标点
    s = re.sub(r"\s+", " ", s).strip()

    toks = [t for t in s.split() if t not in CORP_SUFFIXES]

    # 折叠连续单字母（缩写）：['b','g','high',...] -> ['bg','high',...]
    folded, run = [], []
    for t in toks:
        if len(t) == 1 and t.isalpha():
            run.append(t)
        else:
            if run:
                folded.append("".join(run))
                run = []
            folded.append(t)
    if run:
        folded.append("".join(run))

    return " ".join(folded).strip()


def extract_domains(email_field):
    """从邮箱字段抽域名（辅助键）。"""
    if not email_field or not isinstance(email_field, str):
        return set()
    return {d.lower() for d in
            re.findall(r"[A-Za-z0-9._%+-]+@([A-Za-z0-9.-]+\.[A-Za-z]{2,})", email_field)}


# ─────────────────────────────────────────────────────────────
# 排重匹配器（供推导时复用）
# ─────────────────────────────────────────────────────────────

def match_against_master(candidate_name, master_norm):
    """
    三层匹配，返回 (level, matched_key)。

    level:
      "EXACT"   —— 标准化后完全相等 → 🔴 直接剔除
      "PARTIAL" —— 一方是另一方的词序列子串（如 "bg high voltage" ⊂ "bg high voltage systems"）
                   → ⚠️ 高度疑似同一家，需人工确认
      None      —— 未命中

    🔴 背景（2026-09-23 小规模测试实测）：纯相等比对会漏掉"检索时只拿到部分公司名"的情况。
       例：跟进表登记 "B.G. High Voltage Systems Ltd."，但检索时可能只看到 "BG High Voltage"，
       标准化后为全名的子串，相等比对判否 → 排重失效。故必须有 PARTIAL 层。
    """
    c = normalize_company(candidate_name)
    if not c:
        return None, None

    if c in master_norm:
        return "EXACT", c

    c_tokens = c.split()
    for m in master_norm:
        m_tokens = m.split()
        if not m_tokens or not c_tokens:
            continue
        # 词序列子串判定
        if _is_subseq(c_tokens, m_tokens) or _is_subseq(m_tokens, c_tokens):
            return "PARTIAL", m
    return None, None


def _is_subseq(short, long):
    """short 是否为 long 的连续词子串。"""
    n, k = len(short), len(long)
    if n > k:
        return False
    for i in range(k - n + 1):
        if long[i:i + n] == short:
            return True
    return False


# ─────────────────────────────────────────────────────────────
# 检查项
# ─────────────────────────────────────────────────────────────

def check_source_a(report, max_age_days):
    """数据源 A：跟进表。返回 (rows, meta) 或 (None, None)。"""
    meta = {}

    if not os.path.exists(XLSX_PATH):
        report.fail("跟进表不存在：%s" % XLSX_PATH)
        report.fail("→ 请确认路径未变更；若已迁移，更新 00 文件 §2.1 与本脚本 XLSX_PATH")
        return None, None
    report.ok("跟进表路径存在")

    mtime = dt.datetime.fromtimestamp(os.path.getmtime(XLSX_PATH))
    age_days = (dt.datetime.now() - mtime).total_seconds() / 86400.0
    meta["mtime"] = mtime.strftime("%Y-%m-%d %H:%M")
    meta["age_days"] = round(age_days, 2)

    if age_days > max_age_days:
        report.warn(
            "数据可能已过期：最后修改 %s（%.1f 天前，阈值 %d 天）"
            % (mtime.strftime("%Y-%m-%d %H:%M"), age_days, max_age_days)
        )
        report.warn("→ 请向用户确认是否为最新版本，不要悄悄用旧数据继续跑")
    else:
        report.ok("最后修改：%s（%.1f 天前）" % (mtime.strftime("%Y-%m-%d %H:%M"), age_days))

    try:
        import openpyxl
    except ImportError:
        report.fail("缺少 openpyxl，无法读取 Excel。请先安装：pip install openpyxl")
        return None, None

    try:
        wb = openpyxl.load_workbook(XLSX_PATH, data_only=True)
    except Exception as e:
        report.fail("Excel 打开失败：%s" % e)
        return None, None

    if SHEET_NAME not in wb.sheetnames:
        report.fail("Sheet 未找到：期望「%s」，实际 %s" % (SHEET_NAME, wb.sheetnames))
        return None, None
    if len(wb.sheetnames) != 1:
        report.warn("Sheet 数量变化：期望 1 个，实际 %s 个 %s" % (len(wb.sheetnames), wb.sheetnames))
    else:
        report.ok("Sheet 名称与数量一致：" + SHEET_NAME)

    ws = wb[SHEET_NAME]

    header_row = [c.value for c in ws[HEADER_ROW]]
    header_row = [(str(v).strip() if v is not None else "") for v in header_row]
    while header_row and header_row[-1] == "":
        header_row.pop()

    missing = [c for c in EXPECTED_COLUMNS if c not in header_row]
    if missing:
        report.fail("列名缺失/变更：%s" % missing)
        report.fail("→ 表头行（第 %d 行）实际为：%s" % (HEADER_ROW, header_row))
        report.fail("→ 如用户确认改版，先更新 00 文件 §2.3 再改本脚本")
        return None, None
    if header_row != EXPECTED_COLUMNS:
        report.warn("列顺序与预期不同（列名齐全，但顺序变了）：%s" % header_row)
    else:
        report.ok("列名完整性：%d/%d 通过，顺序一致" % (len(EXPECTED_COLUMNS), len(EXPECTED_COLUMNS)))

    rows = [r for r in ws.iter_rows(min_row=DATA_START_ROW, values_only=True)
            if r[COL_COMPANY]]
    meta["row_count"] = len(rows)
    if not rows:
        report.fail("数据行数为 0 —— 表可能为空或结构已变")
        return None, None
    report.ok("数据行数：%d" % len(rows))

    # 状态枚举
    statuses = {}
    for r in rows:
        s = (str(r[COL_STATUS]).strip() if r[COL_STATUS] else "(空)")
        statuses[s] = statuses.get(s, 0) + 1

    def _known(s):
        if s in KNOWN_STATUSES or s == "(空)":
            return True
        return any(s.startswith(p) for p in STATUS_PREFIX_OK)

    unknown = [s for s in statuses if not _known(s)]
    meta["statuses"] = statuses
    if unknown:
        report.warn("出现未知状态值：%s" % unknown)
        report.warn("→ 可能是用户新增状态；需人工确认是否排除（默认建议排除）")
    else:
        variants = [s for s in statuses if s not in KNOWN_STATUSES]
        report.ok("状态枚举：%d 类，全部可识别%s"
                  % (len(statuses),
                     "（其中 %d 个为带修饰的变体）" % len(variants) if variants else ""))

    # 数据质量
    no_email = sum(1 for r in rows if not r[COL_EMAIL])
    if no_email:
        report.warn("有 %d 行无邮箱字段（不影响排重主键，但影响辅助键匹配）" % no_email)

    dup_names = {}
    for r in rows:
        n = normalize_company(r[COL_COMPANY])
        dup_names.setdefault(n, []).append(str(r[COL_COMPANY]))
    dups = {k: v for k, v in dup_names.items() if len(v) > 1}
    if dups:
        report.warn("跟进表内部存在 %d 组同名（已按地区二次区分，仅供参考）：%s"
                    % (len(dups), list(dups.values())[:3]))
    else:
        report.ok("跟进表内部无同名冲突")

    return rows, meta


def check_source_b(report):
    """数据源 B：公司知识库技能。"""
    if not os.path.isdir(SKILL_DIR):
        report.fail("技能目录不存在：%s" % SKILL_DIR)
        report.fail("→ 产品信息是本项目的必需输入，缺失则无法判定目标客户")
        return None
    report.ok("技能目录存在：jzp-company-knowledge")

    missing = [f for f in SKILL_REQUIRED_FILES
               if not os.path.exists(os.path.join(SKILL_DIR, f))]
    if missing:
        report.fail("技能必需文件缺失：%s" % missing)
        return None
    report.ok("技能必需文件：%d/%d 就位" % (len(SKILL_REQUIRED_FILES), len(SKILL_REQUIRED_FILES)))

    # 技能最后刷新时间（从 SKILL.md 末尾提取）
    meta = {}
    try:
        with open(os.path.join(SKILL_DIR, "SKILL.md"), encoding="utf-8") as f:
            txt = f.read()
        m = re.search(r"最后刷新[：:]\s*(\d{4}-\d{2}-\d{2})", txt)
        if m:
            refresh = dt.date.fromisoformat(m.group(1))
            days = (dt.date.today() - refresh).days
            meta["refresh"] = m.group(1)
            meta["refresh_age_days"] = days
            if days > 30:
                report.warn("技能最后刷新 %s（%d 天前）—— 产品/客户画像可能已变，建议请用户刷新"
                            % (m.group(1), days))
            else:
                report.ok("技能最后刷新：%s（%d 天前）" % (m.group(1), days))
    except Exception as e:
        report.warn("无法解析技能刷新时间：%s" % e)

    return meta


def self_test(report, rows):
    """排重机制自检：用跟进表自身的公司名跑一遍标准化+匹配，验证链路有效。"""
    master = {normalize_company(r[COL_COMPANY]): str(r[COL_COMPANY]) for r in rows}
    probe = [str(r[COL_COMPANY]) for r in rows[:3]]

    hits = 0
    for p in probe:
        if normalize_company(p) in master:
            hits += 1
    if hits == len(probe):
        report.ok("排重链路自检：%d/%d 命中（标准化与匹配正常）" % (hits, len(probe)))
    else:
        report.fail("排重链路自检失败：仅 %d/%d 命中 —— 标准化函数有问题" % (hits, len(probe)))

    # 排重边界样本（改后缀/大小写/加点/缩写折叠/部分名，仍应命中）
    tricky = [
        ("B.G. High Voltage Systems Ltd.", True),
        ("bg high voltage systems", True),
        ("ISCOCA Ltd. (Iscoca Electrical Services Ltd.)", True),
        ("Some Brand New Company That Does Not Exist LLC", False),
    ]
    ok_count = 0
    for name, should_hit in tricky:
        got = normalize_company(name) in master
        if got == should_hit:
            ok_count += 1
        else:
            report.warn("排重边界样本异常：「%s」期望命中=%s 实际=%s"
                        % (name, should_hit, got))
    if ok_count == len(tricky):
        report.ok("排重边界样本：%d/%d 符合预期（含改名/去后缀/干扰项）" % (ok_count, len(tricky)))

    # 三层匹配器自检（EXACT / PARTIAL / None）
    match_probe = [
        ("B.G. High Voltage Systems Limited", "EXACT"),
        ("BG High Voltage", "PARTIAL"),
        ("Brownstone Electric Supply LLC", None),
    ]
    m_ok = 0
    for name, expect in match_probe:
        lvl, _ = match_against_master(name, set(master.keys()))
        if lvl == expect:
            m_ok += 1
        else:
            report.warn("三层匹配器异常：「%s」期望=%s 实际=%s" % (name, expect, lvl))
    if m_ok == len(match_probe):
        report.ok("三层匹配器（EXACT/PARTIAL/None）：%d/%d 符合预期" % (m_ok, len(match_probe)))

    return master


# ─────────────────────────────────────────────────────────────
# 主流程
# ─────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser(description="project1 开工前置检查")
    ap.add_argument("--max-age-days", type=float, default=3.0,
                    help="数据源最大允许陈旧天数（默认 3）")
    ap.add_argument("--json", action="store_true", help="输出 JSON")
    ap.add_argument("--write-master", metavar="PATH",
                    help="把排重主表（73 家标准化公司名）导出为 JSON，供推导时加载")
    args = ap.parse_args()

    report = Report()
    rows, meta_a = check_source_a(report, args.max_age_days)
    meta_b = check_source_b(report)

    master = None
    if rows:
        master = self_test(report, rows)

    if args.json:
        print(json.dumps({
            "blocked": report.blocked,
            "items": report.items,
            "source_a": meta_a,
            "source_b": meta_b,
        }, ensure_ascii=False, indent=2))
    else:
        print(report.render())
        if report.blocked:
            print("\n>>> 存在阻断项：禁止进入推导流程。请先解决上述 [STOP] 项。")
        elif report.has_warn:
            print("\n>>> 检查通过，但有警告项。请把警告显著告知用户后再继续。")
        else:
            print("\n>>> 全部通过，可以开始推导。")

    if args.write_master and master:
        payload = {
            "generated_at": dt.datetime.now().isoformat(timespec="seconds"),
            "source": XLSX_PATH,
            "count": len(master),
            "normalized": sorted(master.keys()),
            "raw": sorted(master.values()),
        }
        os.makedirs(os.path.dirname(os.path.abspath(args.write_master)), exist_ok=True)
        with open(args.write_master, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)
        print("\n排重主表已导出：%s（%d 家）" % (args.write_master, len(master)))

    return 1 if report.blocked else 0


if __name__ == "__main__":
    sys.exit(main())
