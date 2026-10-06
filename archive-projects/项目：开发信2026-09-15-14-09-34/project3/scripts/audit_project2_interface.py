#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
项目2 接口对齐审计脚本
=======================

用途：把「找客户」(项目2) 的交接单输出，与本项目(项目3)的写作依赖逐字段对表，
      统计每个字段的实际到位率，找出「饿着的字段」。

何时跑：
  - 项目2 改了交接单模板或字段名之后
  - 项目2 出了新批次（batch4+）之后
  - 项目3 新增了写作依赖字段之后

用法：
  python scripts/audit_project2_interface.py
  python scripts/audit_project2_interface.py --project2 "D:/别的路径/project2/buyers"

输出：控制台报告 + 可选 --json 落盘
"""

import argparse
import glob
import json
import os
import re
import sys

DEFAULT_PROJECT2 = (
    r"C:\Users\win\WorkBuddy AI\项目：找客户2026-09-15-14-17-22\project2\buyers"
)

# ---------------------------------------------------------------- 依赖定义
# 每个字段： (显示名, 判定方式, 说明)
#   判定方式 'section' = 找段落标题关键词
#   判定方式 'regex'   = 找正则
#   判定方式 'all'     = 必须全部关键词命中

REQUIRED = [
    ("公司名",            "section", ["公司全称", "公司名"]),
    ("联系人姓名",        "section", ["联系人"]),
    ("职位",              "section", ["职位"]),
    ("邮箱",              "section", ["邮箱"]),
    ("邮箱验证状态",      "all",     ["已验证"]),
    ("社媒链接",          "regex",   r"linkedin|LinkedIn|领英"),
    ("背调摘要",          "regex",   r"背调|画像|摘要"),
    ("信息来源",          "section", ["触达来源", "信息来源"]),
    ("合规风险提示",      "section", ["风险提示", "合规"]),
    ("国家+城市",         "regex",   r"(美国|加拿大|USA|Canada)"),
    ("我为什么找他",      "section", ["我为什么找他"]),
    ("买家类型",          "section", ["买家类型"]),
    ("需求品类",          "section", ["需求品类"]),
    ("电压/频率/认证",    "section", ["电压"]),
    ("采购信号",          "section", ["采购信号"]),
    ("可利用的钩子",      "section", ["钩子"]),
    ("开发信建议",        "section", ["开发信建议"]),
    ("矛盾点与风险",      "section", ["矛盾点"]),
    ("信息缺口清单",      "section", ["信息缺口"]),
    ("一句话画像",        "section", ["一句话画像"]),
    ("渠道覆盖清单",      "section", ["渠道覆盖"]),
]

# 重点关注项（本审计的核心标的）
CRITICAL = {
    "邮箱档位ABC":  r"[ABC]\s*档|具名决策人|角色邮箱",
    "still_here四栏": r"在职称谓",
    "still_here结论行": r"离职风险",
    "采购信号三态": r"采购信号.*(确认为空|未获取)",
    "可引用性标记": r"(可直接引用|需降级|存疑勿用)",
}


def load_docs(root):
    pat = os.path.join(root, "**", "买家*开发信交接单*.md")
    return sorted(glob.glob(pat, recursive=True))


def hit(text, kind, spec):
    if kind == "section":
        return any(k in text for k in spec)
    if kind == "regex":
        return bool(re.search(spec, text))
    if kind == "all":
        return all(k in text for k in spec)
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--project2", default=DEFAULT_PROJECT2,
                    help="项目2 buyers 目录")
    ap.add_argument("--json", default=None, help="把结果落盘为 JSON")
    args = ap.parse_args()

    files = load_docs(args.project2)
    if not files:
        print("❌ 没找到交接单，检查路径：%s" % args.project2)
        return 1

    n = len(files)
    print("=" * 68)
    print("项目2 → 项目3 接口对齐审计")
    print("交接单目录：%s" % args.project2)
    print("交接单数量：%d" % n)
    print("=" * 68)
    print()

    # ---- 主干字段到位率
    print("【主干字段到位率】")
    result = {}
    gaps = []
    for name, kind, spec in REQUIRED:
        got = sum(1 for f in files
                  if hit(open(f, encoding="utf-8").read(), kind, spec))
        rate = got * 100.0 / n
        flag = "✅" if rate >= 95 else ("🟡" if rate >= 60 else "🔴")
        print("  %s %-18s %3d/%d  (%.0f%%)" % (flag, name, got, n, rate))
        result[name] = {"got": got, "total": n, "rate": round(rate, 1)}
        if rate < 95:
            gaps.append((name, got, n, rate))
    print()

    # ---- 重点标的（本审计的核心）
    print("【重点标的 · 决定信件质量上限】")
    crit = {}
    for name, rx in CRITICAL.items():
        got = sum(1 for f in files
                  if re.search(rx, open(f, encoding="utf-8").read()))
        rate = got * 100.0 / n
        flag = "✅" if rate >= 95 else ("🟡" if rate >= 60 else "🔴")
        print("  %s %-22s %3d/%d  (%.0f%%)" % (flag, name, got, n, rate))
        crit[name] = {"got": got, "total": n, "rate": round(rate, 1)}
    print()

    # ---- 单份缺失明细（只报红项，避免刷屏）
    print("【缺段明细（仅列不到位者）】")
    lonely = {}
    for name, kind, spec in REQUIRED:
        bad = [os.path.basename(f) for f in files
               if not hit(open(f, encoding="utf-8").read(), kind, spec)]
        if bad and len(bad) <= 8:
            print("  %s 缺 %d 份：%s" % (name, len(bad), ", ".join(bad)))
            lonely[name] = bad
        elif bad:
            print("  %s 缺 %d 份（过多，略）" % (name, len(bad)))
            lonely[name] = {"count": len(bad)}
    print()

    # ---- 结论
    print("=" * 68)
    print("【结论】")
    if gaps:
        print("  🟡/🔴 未满 95%% 的主干字段：")
        for name, got, tot, rate in gaps:
            print("     - %-18s %.0f%%" % (name, rate))
    else:
        print("  ✅ 主干字段全部 >= 95%")
    red = [k for k, v in crit.items() if v["rate"] < 60]
    if red:
        print("  🔴 需要项目2 补的重点标的：")
        for k in red:
            print("     - %-22s %.0f%%" % (k, crit[k]["rate"]))
    print("=" * 68)
    print()
    print("> 完整分析与改动建议见 project3/06_项目2接口对齐审计-20260923.md")

    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump({"total": n, "main": result,
                       "critical": crit, "missing": lonely},
                      fh, ensure_ascii=False, indent=2)
        print("JSON 已落盘：%s" % args.json)

    return 0


if __name__ == "__main__":
    sys.exit(main())
