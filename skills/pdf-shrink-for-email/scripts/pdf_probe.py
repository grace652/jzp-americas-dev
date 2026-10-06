#!/usr/bin/env python3
"""
诊断 PDF 体积构成，判断是否适合「逐页 JPEG 重编码」压缩。

用法:  python pdf_probe.py <input.pdf>

判据速览:
  字体数=0 且 文本字符=0 且 每页恰好 1 张铺满整页的图  → 纯图片型，走 pdf_shrink.py
  否则  → 有文字/矢量，不要用本 skill 的重编码路线
"""
import os, sys
from collections import defaultdict

import pymupdf


def human(n):
    return f"{n / 1048576:.2f} MB"


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    path = sys.argv[1]
    doc = pymupdf.open(path)
    size = os.path.getsize(path)

    print(f"文件      : {path}")
    print(f"大小      : {human(size)}")
    print(f"页数      : {doc.page_count}")
    print(f"加密      : {doc.is_encrypted}")
    print(f"快速Web   : {doc.is_fast_webaccess}")
    md = doc.metadata or {}
    print(f"生成程序  : {md.get('producer')!r} / 创建 {md.get('creator')!r}")
    print()

    # ---- 逐页构成 ----
    print(f"{'页':>4} {'文本字':>6} {'矢量':>5} {'链接':>5} {'批注':>5} {'图':>3}  页面(pt)")
    n_img_pages = 0
    for pno in range(doc.page_count):
        p = doc[pno]
        txt = p.get_text().strip()
        dr = p.get_drawings()
        imgs = p.get_images(full=True)
        if len(imgs) == 1:
            n_img_pages += 1
        print(f"{pno + 1:>4} {len(txt):>6} {len(dr):>5} {len(p.get_links()):>5} "
              f"{len(list(p.annots() or [])):>5} {len(imgs):>3}  "
              f"{p.rect.width:.0f}x{p.rect.height:.0f}")
    print()

    # ---- 图片统计 ----
    seen = {}
    for pno in range(doc.page_count):
        for im in doc[pno].get_images(full=True):
            xref = im[0]
            if xref in seen:
                continue
            try:
                info = doc.extract_image(xref)
            except Exception:
                continue
            seen[xref] = {
                "page": pno + 1, "xref": xref, "ext": info["ext"],
                "w": info["width"], "h": info["height"],
                "bytes": len(info["image"]), "bpc": info.get("bpc"),
            }
    uniq = list(seen.values())
    img_bytes = sum(r["bytes"] for r in uniq)

    by_ext = defaultdict(lambda: [0, 0])
    for r in uniq:
        by_ext[r["ext"]][0] += 1
        by_ext[r["ext"]][1] += r["bytes"]

    print(f"图片对象(去重): {len(uniq)} 张，合计 {human(img_bytes)}"
          f"（占文件 {img_bytes / size * 100:.1f}%）")
    for ext, (n, b) in sorted(by_ext.items(), key=lambda x: -x[1][1]):
        print(f"  {ext:<6} {n:>4} 张  {human(b)}")

    # 尺寸分布
    sizes = defaultdict(int)
    for r in uniq:
        sizes[(r["w"], r["h"])] += 1
    print("尺寸分布:")
    for (w, h), n in sorted(sizes.items(), key=lambda x: -x[1])[:10]:
        print(f"  {w}x{h}  ×{n}")

    # 有效 DPI（按首页估算）
    if uniq:
        p0 = doc[0].rect
        r0 = max(uniq, key=lambda x: x["bytes"])
        dpi_x = r0["w"] / (p0.width / 72.0) if p0.width else 0
        dpi_y = r0["h"] / (p0.height / 72.0) if p0.height else 0
        print(f"最大图有效分辨率 ≈ {dpi_x:.0f} x {dpi_y:.0f} DPI")
    print()

    # ---- 最大图 ----
    print("最大的 10 张图:")
    for r in sorted(uniq, key=lambda x: -x["bytes"])[:10]:
        print(f"  p{r['page']:<4} xref={r['xref']:<6} {r['ext']:<5} "
              f"{r['w']}x{r['h']}  {human(r['bytes'])}  bpc={r['bpc']}")
    print()

    # ---- 字体 ----
    fonts = set()
    for pno in range(doc.page_count):
        for f in doc[pno].get_fonts(full=True):
            fonts.add(f[3])
    print(f"字体数: {len(fonts)}")
    for name in sorted(fonts)[:20]:
        print(f"  {name}")
    print()

    # ---- 重复图 ----
    import hashlib
    hashes = defaultdict(list)
    for r in uniq:
        raw = doc.extract_image(r["xref"])["image"]
        hashes[hashlib.md5(raw).hexdigest()].append(r["page"])
    dups = {k: v for k, v in hashes.items() if len(v) > 1}
    print(f"完全重复的图片组: {len(dups)}")
    for v in list(dups.values())[:10]:
        print(f"  页 {sorted(v)}")
    print()

    # ---- 结论 ----
    has_text = any(doc[p].get_text().strip() for p in range(doc.page_count))
    pure_image = (not has_text) and len(fonts) == 0 and n_img_pages == doc.page_count
    print("=" * 56)
    if pure_image:
        print("判定: 纯图片型 PDF（每页 = 1 张全幅图，无文字/矢量）")
        print("结论: 体积几乎全部来自图像 → 可安全走 pdf_shrink.py 重编码路线")
        print(f"      图像占文件 {img_bytes / size * 100:.1f}%，即全部体积都在可压缩范围内")
    elif img_bytes / size > 0.6:
        print(f"判定: 图像占文件 {img_bytes / size * 100:.0f}%，但含文字/矢量")
        print("结论: 重编码图片可行，但会同时重编码页面。建议先备份，并优先考虑")
        print("      回源文件重导出（矢量文字更清晰、体积更小）")
    else:
        print(f"判定: 图像仅占 {img_bytes / size * 100:.0f}%，体积主要来自文字/矢量/结构")
        print("结论: 本 skill 不适用。请回源文件重导出，或用 Ghostscript 通用压缩")

    doc.close()


if __name__ == "__main__":
    main()
