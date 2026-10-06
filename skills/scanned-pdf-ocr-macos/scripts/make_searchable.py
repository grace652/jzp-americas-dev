#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把「隐形文字层 PDF」叠加回原扫描件，产出可搜索 PDF，并做三重校验。

用法:
  python make_searchable.py <原扫描件.pdf> <文字层.pdf> <输出.pdf>

前置: 先用 scripts/ocrtext.swift 编译出的 ocrtext 生成文字层 PDF：
  ./ocrtext <原扫描件.pdf> <文字层.pdf> [起页] [止页]

依赖: pikepdf + pypdf（建议放在项目自己的 venv 里）

为什么这么做:
  在 CGContext 里重新渲染页面图像会得到未压缩位图（约 1.9MB/页，300 页就 500MB+）。
  正确做法是只生成体积很小的隐形文字层，再用 pikepdf 叠加回原书，保留原始压缩。
"""
from __future__ import annotations

import hashlib
import os
import sys

try:
    import pikepdf
    from pypdf import PdfReader
except ImportError:
    sys.exit("需要 pikepdf + pypdf: pip install pikepdf pypdf")


def md5_of_first_image(reader: PdfReader, idx: int) -> str | None:
    try:
        keys = list(reader.pages[idx].images.keys())
        if not keys:
            return None
        return hashlib.md5(reader.pages[idx].images[keys[0]].data).hexdigest()
    except Exception:
        return None


def main() -> None:
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    src, layer, out = sys.argv[1], sys.argv[2], sys.argv[3]

    with pikepdf.open(src) as base, pikepdf.open(layer) as lay:
        nb, nl = len(base.pages), len(lay.pages)
        print(f"原扫描件 {nb} 页　文字层 {nl} 页")
        if nb != nl:
            sys.exit(f"页数不一致，中止（原 {nb} / 层 {nl}）")
        for i in range(nb):
            base.pages[i].add_overlay(lay.pages[i])
        base.save(out, compress_streams=True,
                  object_stream_mode=pikepdf.ObjectStreamMode.generate)

    size = os.path.getsize(out) / 1024 / 1024
    print(f"已写出 {out}　{size:.1f}MB")

    a, b = PdfReader(src), PdfReader(out)
    print(f"页数 {len(b.pages)}　加密 {b.is_encrypted}")

    total, rich = 0, 0
    for p in b.pages:
        t = p.extract_text() or ""
        total += len(t)
        if len(t.strip()) > 50:
            rich += 1
    print(f"可提取正文字符 {total}　有实质文字的页数 {rich}/{len(b.pages)}")

    sample = [i for i in range(0, len(b.pages), max(1, len(b.pages) // 5))][:5]
    ok = 0
    for i in sample:
        if md5_of_first_image(a, i) == md5_of_first_image(b, i):
            ok += 1
    print(f"页面图像未被破坏 {ok}/{len(sample)}")

    if ok != len(sample):
        sys.exit("⚠️ 有页面图像被改动，请检查叠加逻辑")
    if total < 1000:
        sys.exit("⚠️ 文字层疑似未生效，请检查 ocrtext 是否正常输出")
    print("✅ 校验通过")


if __name__ == "__main__":
    main()
