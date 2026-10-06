#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
把「中英双轨、但切分粒度不同」的 ASS 字幕，合并到统一时间窗上，
使每一对中英文同时出现、同时消失。

原理：
  1. 收集中文轨(Default)与英文轨(eng)的全部起止时间，取并集作为边界 grid
  2. 相邻边界切成窗口，每个窗口取「覆盖该窗口」的当前中文行/英文行
  3. 合并「文字内容完全相同且类型相同」的相邻窗口（消除边界碎片）
  4. 吸收过短的碎片窗口（<ABSORB）到相邻窗口
  5. 输出：每个窗口写一条 Default + 一条 eng，时间戳完全一致

用法：python merge_bilingual_ass.py <in.ass> <out.ass>
"""
import re, sys

ABSORB = 0.60          # 短于该值的窗口视为碎片，并入邻窗
MIN_DUR = 0.20         # 最终窗口最小时长
GAP_BRIDGE = 0.24      # 两窗之间间隔小于此值则视为连续，可合并同文本

# 中英之间允许的「同时出现」判定容差
OVERLAP_EPS = 0.02


def t2s(x):
    h, m, s = x.split(':')
    return int(h) * 3600 + int(m) * 60 + float(s)


def s2t(v):
    v = max(0.0, v)
    h = int(v // 3600)
    m = int((v % 3600) // 60)
    s = v % 60
    return f"{h}:{m:02d}:{s:05.2f}"


def parse(path):
    raw = open(path, encoding='utf-8-sig').read()
    head, dialogues = [], []
    for line in raw.splitlines():
        if line.startswith('Dialogue:'):
            dialogues.append(line)
        elif line.startswith('Comment:'):
            dialogues.append(line)
        else:
            head.append(line)
    tracks = {'Default': [], 'eng': [], 'note': []}
    for line in dialogues:
        p = line.split(',', 9)
        if len(p) < 10:
            continue
        style = p[3]
        if style in tracks:
            tracks[style].append(
                (t2s(p[1]), t2s(p[2]), p[9])
            )
    return head, tracks


def build_windows(cn, en):
    bounds = sorted(set(
        [x[0] for x in cn] + [x[1] for x in cn] +
        [x[0] for x in en] + [x[1] for x in en]
    ))
    wins = []
    for i in range(len(bounds) - 1):
        a, b = bounds[i], bounds[i + 1]
        if b - a < 0.01:
            continue
        c = next((x[2] for x in cn if x[0] < b - OVERLAP_EPS and x[1] > a + OVERLAP_EPS), None)
        e = next((x[2] for x in en if x[0] < b - OVERLAP_EPS and x[1] > a + OVERLAP_EPS), None)
        if c is None and e is None:
            continue
        wins.append([a, b, c, e])

    # 合并相邻同内容窗口（中英都相同）
    merged = []
    for w in wins:
        if merged:
            p = merged[-1]
            if (p[2], p[3]) == (w[2], w[3]) and w[0] - p[1] <= GAP_BRIDGE:
                p[1] = w[1]
                continue
        merged.append(w)

    # 吸收碎片：把过短窗口并进邻窗（中英任一方与邻窗相同即并入）
    changed = True
    while changed and len(merged) > 1:
        changed = False
        for i, w in enumerate(merged):
            if w[1] - w[0] >= ABSORB:
                continue
            if i > 0:
                prev = merged[i - 1]
                if (prev[2] == w[2] or prev[3] == w[3] or
                        prev[2] is None or w[2] is None or
                        prev[3] is None or w[3] is None):
                    prev[1] = w[1]
                    if prev[2] is None:
                        prev[2] = w[2]
                    if prev[3] is None:
                        prev[3] = w[3]
                    del merged[i]
                    changed = True
                    break
            if i + 1 < len(merged):
                nxt = merged[i + 1]
                nxt[0] = w[0]
                if nxt[2] is None:
                    nxt[2] = w[2]
                if nxt[3] is None:
                    nxt[3] = w[3]
                del merged[i]
                changed = True
                break
    return merged


def render(head, tracks, windows):
    out = []
    for line in head:
        out.append(line)
    # note 轨（字幕组署名等）原样保留
    for st, et, txt in tracks['note']:
        out.append(f"Dialogue: 0,{s2t(st)},{s2t(et)},note,,0,0,0,,{txt}")
    for st, et, txt in tracks['note']:
        pass
    # 先中文后英文：ASS 同层样式下，中文 MarginV 大 → 显示在上
    for a, b, c, e in windows:
        if b - a < MIN_DUR:
            b = a + MIN_DUR
        if c:
            out.append(f"Dialogue: 0,{s2t(a)},{s2t(b)},Default,,0,0,0,,{c}")
        if e:
            out.append(f"Dialogue: 0,{s2t(a)},{s2t(b)},eng,,0,0,0,,{e}")
    return '\n'.join(out) + '\n'


def main(src, dst):
    head, tracks = parse(src)
    windows = build_windows(tracks['Default'], tracks['eng'])
    open(dst, 'w', encoding='utf-8').write(render(head, tracks, windows))
    paired = sum(1 for w in windows if w[2] and w[3])
    print(f"{src} -> {dst}")
    print(f"  窗口 {len(windows)}  中英配对 {paired}  "
          f"仅中文 {sum(1 for w in windows if w[2] and not w[3])}  "
          f"仅英文 {sum(1 for w in windows if w[3] and not w[2])}")


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
