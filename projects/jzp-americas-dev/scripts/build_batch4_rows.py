#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""阶段 1：构建 batch4 历史缺口 31 家的数据行（编号 117–147）

🔴 关键约束：
  · batch4 存在**编号复用**（买家 111 有两家）→ 一律按**文件名白名单**取用，禁止按编号
  · 必须排除**假匹配**：Robert's Electrical(92) ≠ Robertson(#116)；
    Gresco(109) ≠ RESCO(#72)；EC Electric(119) ≠ PowerTec(#7)
  · 发送日期从**已发送邮箱**逐封取证（26 家已发 9/23–9/25，5 家未发）

输出：/tmp/batch4_rows.json
"""
import json, re, sys, glob, os
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from build_followup_rows import (clean, sec, rows_of, parse_core, pick_type, pick_products,
                                 norm_country, norm_src, workday_add, NEXT_AFTER,
                                 NOT_FOUND, NO_LETTER, CLIENTS)

ROOT = Path("/Users/eric/WorkBuddy AI/2026-09-27-00-43-30/jzp-americas-dev")
HANDOFF = ROOT / "开发信项目/交接单/batch4_73plus"
START_N = 117          # 老 sheet 到 #116，本次接 117

# 🔴 文件名白名单（31 家，逐字精确；禁止按编号 glob）
WHITELIST = [
    "买家75_HS_Energy_System_开发信交接单.md",
    "买家76_Universal_Electric_Services_开发信交接单.md",
    "买家78_Graybar_Canada_Oshawa_开发信交接单.md",
    "买家79_Wesco_Distribution_Canada_开发信交接单.md",
    "买家80_Killmer_Electric_开发信交接单.md",
    "买家82_Northern_High_Voltage_开发信交接单.md",
    "买家83_Moody_Electric_开发信交接单.md",
    "买家88_Rhododendron_Electric_开发信交接单.md",
    "买家90_AW_High_Voltage_开发信交接单.md",
    "买家91_PTS_Power_Transformer_Services_开发信交接单.md",
    "买家92_Roberts_Electrical_开发信交接单.md",
    "买家95_Gescan_Sonepar_开发信交接单.md",
    "买家97_Aurum_Electric_开发信交接单.md",
    "买家99_Amtek_开发信交接单.md",
    "买家100_Elliott_Electric_开发信交接单.md",
    "买家102_Yale_Electric_开发信交接单.md",
    "买家103_Solectric_开发信交接单.md",
    "买家105_Mott_Electric_开发信交接单.md",
    "买家107_Codale_开发信交接单.md",
    "买家109_Gresco_开发信交接单.md",
    "买家111_Canem_开发信交接单.md",
    "买家111_J_Ranck_开发信交接单.md",
    "买家114_Agilix_开发信交接单.md",
    "买家115_AES_Electric_开发信交接单.md",
    "买家117_Lumen_开发信交接单.md",
    "买家118_Sargent_Electric_开发信交接单.md",
    "买家119_EC_Electric_开发信交接单.md",
    "买家120_Houle_Electric_开发信交接单.md",
    "买家121_Lapp_Electric_开发信交接单.md",
    "买家123_North_Coast_开发信交接单.md",
    "买家125_Van_Ert_开发信交接单.md",
]


def load_sent_from_mailbox():
    """从已发送邮箱取「邮箱 → 发送日期」。失败则返回空 dict（调用方需降级处理）。"""
    try:
        import imaplib, email
        cfg = json.loads((Path.home() / ".config/jiezou-mail/config.json").read_text(encoding="utf-8"))
        M = imaplib.IMAP4_SSL(cfg["imap_host"], int(cfg["imap_port"]))
        M.login(cfg["email"], cfg["password"])
        M.select('"Sent Messages"', readonly=True)
        typ, d = M.uid("search", None, "ALL")
        sent = {}
        for u in d[0].split():
            typ, dd = M.uid("fetch", u, "(BODY.PEEK[HEADER.FIELDS (TO DATE)])")
            if not dd or not dd[0]:
                continue
            raw = dd[0][1].decode("utf-8", "replace")
            msg = email.message_from_string(raw)
            dt = str(msg.get("Date") or "")
            m = re.search(r"(\d{1,2} \w{3} \d{4})", dt)
            iso = ""
            if m:
                for fmt in ("%d %b %Y",):
                    try:
                        from datetime import datetime
                        iso = datetime.strptime(m.group(1), fmt).strftime("%Y-%m-%d")
                        break
                    except Exception:
                        pass
            for a in re.findall(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}", raw):
                if iso:
                    sent.setdefault(a.lower(), iso)
        M.logout()
        return sent
    except Exception as e:
        print(f"⚠️ 邮箱取证失败（{e}），将退回空表")
        return {}


def main():
    sent_map = load_sent_from_mailbox()
    print(f"已发送邮箱取证：{len(sent_map)} 个地址")
    rows = []
    n = START_N - 1
    for fn in WHITELIST:
        f = HANDOFF / fn
        if not f.exists():
            print(f"❌ 白名单文件不存在：{fn}")
            continue
        m = re.match(r"买家(\d+)_", fn)
        buyer = int(m.group(1))
        text = f.read_text(encoding="utf-8")
        core = parse_core(text)
        std = dict(rows_of(sec(text, "标准字段明细")))
        tm = re.search(r"^#\s*【买家\s*\d+】开发信交接单\s*—\s*(.+)$", text, re.M)
        company = clean(core.get("公司名") or (tm.group(1) if tm else fn))
        email = clean(core.get("邮箱", ""))
        dz = re.search(r"邮箱档位[：:]\s*\**([ABC][+−\-]?)", text)
        tier = dz.group(1) if dz else ""
        btype, _ = pick_type(text, core)
        prod = pick_products(text)
        country = norm_country(core.get("国家 + 城市") or core.get("国家+城市") or
                               next((v for k, v in std.items() if "国家" in k), ""), text, core)
        source = norm_src(core.get("信息来源", ""))

        # 找信件：**优先从交接单文件名推导**（最可靠）
        #   买家95_Gescan_Sonepar_开发信交接单.md → 开发信-Gescan-Sonepar.md
        #   ⚠️ 不能用「公司名字符串」匹配 —— 公司名常带括号后缀（如
        #   「Gescan, Division of Sonepar Canada」），会把 11 家误判为「未写信」（实测）
        letter, skel, window = None, NO_LETTER, ""
        fkey = re.sub(r"_开发信交接单\.md$", "", re.sub(r"^买家\d+_", "", fn))
        fkeyn = re.sub(r"[^a-z0-9]", "", fkey.lower())
        all_letters = [c for c in CLIENTS.glob("开发信-*.md") if "跟进" not in c.name]
        if fkeyn:
            for cand in all_letters:
                if fkeyn in re.sub(r"[^a-z0-9]", "", cand.name.lower()):
                    letter = cand
                    break
        if letter is None:      # 退化：按买家号 / 公司名
            for cand in all_letters:
                ct = cand.read_text(encoding="utf-8", errors="replace")
                if f"买家 {buyer}" in ct or f"买家{buyer}" in ct:
                    letter = cand
                    break
        if letter is None:
            key = re.sub(r"[^a-z0-9]", "", company.lower())[:10]
            for cand in all_letters:
                if key and key in re.sub(r"[^a-z0-9]", "", cand.name.lower()):
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
        status = "已发送" if send_date else "待发送"
        next_date = workday_add(date.fromisoformat(send_date), 3).isoformat() if send_date else ""

        notes = [f"买家{buyer}", "batch4 历史补登记"]
        if tier:
            notes.append(f"{tier}档")
        if not send_date:
            notes.append("未发（待补发）")
        if send_date:
            notes.append(f"首封{send_date}")

        n += 1
        rows.append({"#": n, "发送日期": send_date, "公司名称": company, "国家/地区": country,
                     "联系人": clean(core.get("联系人姓名", "")) or NOT_FOUND,
                     "职位": clean(core.get("职位", "")) or NOT_FOUND,
                     "买家类型": btype, "需求产品": prod, "触达来源": source, "骨架": skel,
                     "建议发送时间(北京)": window or NOT_FOUND, "邮箱": email or NOT_FOUND,
                     "状态": status, "跟进次数": 0, "下次跟进日": next_date,
                     "最后联系日": send_date, "备注 / 下一步": "｜".join(notes),
                     "_buyer": buyer, "_file": fn, "_letter": letter.name if letter else ""})

    print(f"构建完成：{len(rows)} 行（编号 {rows[0]['#']}–{rows[-1]['#']}）")
    Path("/tmp/batch4_rows.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    from collections import Counter
    print("状态：", dict(Counter(r["状态"] for r in rows)))
    print("类型：", dict(Counter(r["买家类型"] for r in rows)))
    print("有信件：", sum(1 for r in rows if r["_letter"]), "｜有发送日期：", sum(1 for r in rows if r["发送日期"]))
    print("\n未发的 5 家：")
    for r in rows:
        if not r["发送日期"]:
            print(f"  买家{r['_buyer']} {r['公司名称'][:34]:<36}{r['邮箱'][:36]}")


if __name__ == "__main__":
    main()
