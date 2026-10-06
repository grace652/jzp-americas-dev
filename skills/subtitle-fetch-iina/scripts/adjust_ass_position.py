#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
调整双语 ASS 字幕的垂直位置与字号，不触碰时间轴与文字内容。

用法：
    python adjust_ass_position.py in.ass out.ass --cn-mv 62 --en-mv 10

    --cn-mv   中文(Default)样式底边距屏幕底部的像素数。越大越靠上。
    --en-mv   英文(eng)样式底边距屏幕底部的像素数。应 < --cn-mv，否则重叠。
    --cn-fs   中文字号（可选，默认不改）
    --en-fs   英文字号（可选，默认不改）

原理：ASS 里每个 Style 的 MarginV 是该样式【文字块底边】到屏幕底边的距离，
      中文与英文各自独立摆放。因此要让中英都更贴底，两个值都要减小，
      且必须保持 中文MarginV >= 英文MarginV + 英文字高，否则两行会重叠。
      英文字高 ≈ 字号 × 1.2。
"""
import re
import argparse


def patch_style(line, name, mv=None, fs=None):
    """改写 Style 行：style 名匹配则替换 Fontsize / MarginV。"""
    p = line.split(',')
    # Style: Name,Fontname,Fontsize,...,MarginL,MarginR,MarginV,Encoding
    if len(p) < 23:
        return line, False
    if p[0].split(':', 1)[1].strip() != name:
        return line, False
    if fs is not None:
        p[2] = str(int(fs))
    if mv is not None:
        if name == 'Default':
            p[21] = str(int(mv))          # MarginV 在倒数第 2 个字段
        else:
            p[21] = str(int(mv))
    return ','.join(p), True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('src')
    ap.add_argument('dst')
    ap.add_argument('--cn-mv', type=int, default=None)
    ap.add_argument('--en-mv', type=int, default=None)
    ap.add_argument('--cn-fs', type=int, default=None)
    ap.add_argument('--en-fs', type=int, default=None)
    ap.add_argument('--note-mv', type=int, default=None)
    a = ap.parse_args()

    lines = open(a.src, encoding='utf-8-sig').read().splitlines()
    out, hit = [], {'Default': False, 'eng': False, 'note': False}
    for ln in lines:
        if ln.startswith('Style:'):
            ln2, ok = patch_style(ln, 'Default', a.cn_mv, a.cn_fs)
            if ok:
                hit['Default'] = True
                out.append(ln2)
                continue
            ln2, ok = patch_style(ln, 'eng', a.en_mv, a.en_fs)
            if ok:
                hit['eng'] = True
                out.append(ln2)
                continue
            ln2, ok = patch_style(ln, 'note', a.note_mv, None)
            if ok:
                hit['note'] = True
                out.append(ln2)
                continue
        out.append(ln)

    open(a.dst, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    for ln in out:
        if ln.startswith('Style:') and ',MarginL' not in ln:
            pass
    print(f"{a.src} -> {a.dst}")
    print(f"  命中样式: {hit}")
    for ln in out:
        if ln.startswith('Style:'):
            print("  " + ln)


if __name__ == '__main__':
    main()
