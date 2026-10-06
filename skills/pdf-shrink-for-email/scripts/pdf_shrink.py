#!/usr/bin/env python3
"""
压缩「纯图片型 PDF」：逐页 JPEG 重编码后原位替换，保持页面尺寸/页数/顺序不变。

用法:
  python pdf_shrink.py <input.pdf> <output.pdf> --quality 92 [--dpi 206]
"""
import argparse, io, os, sys, time
import pymupdf
from PIL import Image

def human(n):
    return f"{n/1048576:.2f} MB"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("dst")
    ap.add_argument("--quality", type=int, default=92)
    ap.add_argument("--dpi", type=float, default=None,
                    help="目标 DPI；不填则保持原始像素尺寸")
    ap.add_argument("--subsampling", type=int, default=2,
                    help="0=4:4:4, 1=4:2:2, 2=4:2:0")
    ap.add_argument("--title", default=None)
    args = ap.parse_args()

    t0 = time.time()
    doc = pymupdf.open(args.src)
    orig_size = os.path.getsize(args.src)
    print(f"源文件: {args.src}  {human(orig_size)}  页数 {doc.page_count}")

    total_before = 0
    total_after = 0
    replaced = 0
    failed = []

    for pno in range(doc.page_count):
        page = doc[pno]
        imgs = page.get_images(full=True)
        if not imgs:
            continue
        for im in imgs:
            xref = im[0]
            info = doc.extract_image(xref)
            raw = info["image"]
            total_before += len(raw)
            try:
                pil = Image.open(io.BytesIO(raw))
                mode = pil.mode
                if mode not in ("RGB", "L"):
                    pil = pil.convert("RGB")
                w, h = pil.size
                if args.dpi:
                    rect = page.rect
                    # 原始 DPI：像素 / 英寸
                    src_dpi = w / (rect.width / 72.0)
                    scale = args.dpi / src_dpi
                    if scale < 0.999:
                        nw, nh = max(1, round(w * scale)), max(1, round(h * scale))
                        pil = pil.resize((nw, nh), Image.LANCZOS)
                buf = io.BytesIO()
                pil.save(buf, "JPEG", quality=args.quality, optimize=True,
                         progressive=True, subsampling=args.subsampling)
                new = buf.getvalue()
                # 只有确实变小才替换
                if len(new) < len(raw):
                    page.replace_image(xref, stream=new)
                    total_after += len(new)
                    replaced += 1
                else:
                    total_after += len(raw)
            except Exception as e:
                failed.append((pno + 1, xref, repr(e)))
                total_after += len(raw)

    if args.title:
        md = doc.metadata or {}
        md["title"] = args.title
        doc.set_metadata(md)

    doc.save(args.dst, garbage=4, clean=1, deflate=True, deflate_images=True,
             use_objstms=1, no_new_id=0)
    doc.close()

    new_size = os.path.getsize(args.dst)
    print(f"图片流: {human(total_before)} -> {human(total_after)}  "
          f"({total_after/total_before*100:.1f}%)  替换 {replaced} 张")
    print(f"输出文件: {args.dst}  {human(new_size)}  "
          f"({new_size/orig_size*100:.1f}% of original, 省 {(1-new_size/orig_size)*100:.1f}%)")
    print(f"耗时 {time.time()-t0:.1f}s")
    if failed:
        print("失败:", failed)

if __name__ == "__main__":
    main()
