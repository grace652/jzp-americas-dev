#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""9/30 跟进信 · 跟进表更新（.xlsx 主文件）

与 `apply_followup_0930.py`（.md）**逐字段一致**。

依据 `开发信项目/01_skill_email_writing.md` §十一：
  · 🔴 **绝不读写 `freeze_panes`**（getter 返回 "C60"，写回会把冻结行变 1–59）
  · 只改**已有单元格的值**（不新增行 → 不触发「追加行丢格式」陷阱）
  · 状态必须与 M 列下拉**逐字一致**，否则不变色

状态口径：`已退信（暂缓至 …）` **不是下拉合法值**，故用 `已放弃`
（与 KVA Electric / Pritchard 的既有先例一致），退信类别 + 冷却日 + 换发法要求写进「备注 / 下一步」。
"""

import shutil
import sys
import zipfile
from pathlib import Path

import openpyxl

ROOT = Path(Path(__file__).resolve().parents[1])
XLSX = ROOT / "开发信项目/工作区/开发信跟进表.xlsx"
BAK = ROOT / ".workbuddy-ai/开发信跟进表.bak-20261001-跟进0930前.xlsx"

C_STATUS, C_CNT, C_NEXT, C_LAST, C_NOTE = 13, 14, 15, 16, 17

FU = {  # # → (跟进次数, 下次跟进日, 备注追加)
    17:  (2, "2026-10-09", "✅ 9/30 跟进信已发 2026-10-01（clients/开发信-跟进-Scientechnic.md）"),
    18:  (2, "2026-10-09", "✅ 9/30 跟进信已发 2026-10-01（clients/开发信-跟进-Bossie-Electric.md）"),
    19:  (2, "2026-10-09", "✅ 9/30 跟进信已发 2026-10-01（clients/开发信-跟进-Premier-Electric.md）"),
    20:  (2, "2026-10-09", "✅ 9/30 跟进信已发 2026-10-01（clients/开发信-跟进-Oregon-Electric-Service.md）"),
    128: (1, "2026-10-07", "✅ 9/30 跟进信已发 2026-10-01（clients/开发信-跟进-Gescan-Sonepar.md）"),
    134: (1, "2026-10-07", "✅ 9/30 跟进信已发 2026-10-01（clients/开发信-跟进-Mott-Electric.md）"),
    137: (1, "2026-10-07", "✅ 9/30 跟进信已发 2026-10-01（clients/开发信-跟进-Canem.md）"),
    140: (1, "2026-10-07", "✅ 9/30 跟进信已发 2026-10-01（clients/开发信-跟进-AES-Electric.md）"),
    143: (1, "2026-10-07", "✅ 9/30 跟进信已发 2026-10-01（clients/开发信-跟进-EC-Electric.md）"),
    144: (1, "2026-10-07", "✅ 9/30 跟进信已发 2026-10-01（clients/开发信-跟进-Houle-Electric.md）"),
    146: (1, "2026-10-07", "✅ 9/30 跟进信已发 2026-10-01（clients/开发信-跟进-North-Coast.md）"),
}
BOUNCED = {  # # → (下次跟进日, 最后联系日, 备注)
    126: ("2026-10-09", "2026-09-25",
          "⛔ 2026-09-25 首封退信（软退信-服务商拒收，550 5.4.1 Access denied / EXO）。"
          "冷却至 2026-10-09；重试须换发法（改主题+重写正文+去链接+纯文本+间隔≥2周）。⛔ 本批 9/30 跟进信未发。"),
    135: ("2026-10-14", "2026-09-30",
          "⛔ 2026-09-30 23:40 北京补发（batch4 缺口补发）后约 2 分钟被 Mimecast 拒（5.4.1 Access denied）。"
          "冷却至 2026-10-14；重试须换发法。⚠️ 原登记「待发送」有误 —— 实际已发且已退信。"),
    213: ("2026-10-30", "2026-09-29",
          "⛔ 2026-09-30 00:10 北京投递后被 Barracuda 拒（550 permanent failure … :blocked），"
          "归类软退信-暂时停用。冷却至 2026-10-30；重试须换发法。⚠️ 原登记「待发送」有误 —— 实际已发且已退信。"),
}


def find_row(ws, num):
    hits = [r for r in range(5, ws.max_row + 1) if ws.cell(r, 1).value == num]
    if len(hits) != 1:
        raise SystemExit(f"⛔ 表 `{ws.title}` 中 #{num} 命中 {len(hits)} 行")
    return hits[0]


def main():
    if not BAK.exists():
        shutil.copy2(XLSX, BAK)
        print(f"已备份 → {BAK.name}")

    wb = openpyxl.load_workbook(XLSX)
    ws_old = wb["开发信跟进表"]
    ws_new = wb["开发信跟进表-batch5+6"]

    def sheet_for(num):
        for ws in (ws_old, ws_new):
            if any(ws.cell(r, 1).value == num for r in range(5, ws.max_row + 1)):
                return ws
        raise SystemExit(f"⛔ 两个 sheet 都找不到 #{num}")

    log = []
    for num, (cnt, nxt, note) in FU.items():
        ws = sheet_for(num)
        r = find_row(ws, num)
        assert ws.cell(r, C_STATUS).value == "已发送", f"#{num} 状态异常：{ws.cell(r,C_STATUS).value!r}"
        ws.cell(r, C_CNT).value = cnt
        ws.cell(r, C_NEXT).value = nxt
        ws.cell(r, C_LAST).value = "2026-10-01"
        old = ws.cell(r, C_NOTE).value or ""
        ws.cell(r, C_NOTE).value = (old + "｜" if old and old != "—" else "") + note
        log.append(f"  #{num} [{ws.title}] r{r} 跟进次数={cnt} 下次={nxt} 最后=2026-10-01")

    for num, (nxt, last, note) in BOUNCED.items():
        ws = sheet_for(num)
        r = find_row(ws, num)
        ws.cell(r, C_STATUS).value = "已放弃"
        ws.cell(r, C_NEXT).value = nxt
        ws.cell(r, C_LAST).value = last
        old = ws.cell(r, C_NOTE).value or ""
        ws.cell(r, C_NOTE).value = (old + "｜" if old and old != "—" else "") + note
        log.append(f"  #{num} [{ws.title}] r{r} 状态=已放弃 下次={nxt}")

    wb.save(XLSX)

    # 完整性校验
    with zipfile.ZipFile(XLSX) as z:
        bad = z.testzip()
    if bad:
        raise SystemExit(f"⛔ xlsx 损坏：{bad}")

    wb2 = openpyxl.load_workbook(XLSX)
    print(f"✅ 已更新 {XLSX.name}（{len(log)} 处）｜ freeze: "
          f"{wb2['开发信跟进表'].freeze_panes} / {wb2['开发信跟进表-batch5+6'].freeze_panes}")
    for l in log:
        print(l)
    return 0


if __name__ == "__main__":
    sys.exit(main())
