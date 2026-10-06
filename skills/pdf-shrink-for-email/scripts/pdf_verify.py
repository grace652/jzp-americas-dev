#!/usr/bin/env python3
"""
验证压缩后 PDF：结构一致性 + 逐页渲染画质指标 + 可选目检对比图。

用法:
  python pdf_verify.py <original.pdf> <compressed.pdf> [more.pdf ...]
  python pdf_verify.py --visual <original.pdf> <compressed.pdf> [--outdir DIR]

判定门槛（经验值）:
  PSNR >= 42 dB 且 SSIM >= 0.999   → 视觉无损
  SSIM >= 0.995                    → 屏幕观看无差别
  SSIM <  0.995                    → 属于「有损轻量版」，必须向用户明说
"""
import os, sys
import numpy as np
import pymupdf


def psnr(a, b):
    a = a.astype(np.float64); b = b.astype(np.float64)
    mse = np.mean((a - b) ** 2)
    return 999.0 if mse == 0 else 10 * np.log10(255.0 ** 2 / mse)


def ssim_global(a, b):
    """全局 SSIM（灰度近似）。整页级别的保真度判据，够用且快。"""
    a = a.astype(np.float64).mean(axis=2)
    b = b.astype(np.float64).mean(axis=2)
    mu1, mu2 = a.mean(), b.mean()
    v1, v2 = a.var(), b.var()
    cov = ((a - mu1) * (b - mu2)).mean()
    C1, C2 = (0.01 * 255) ** 2, (0.03 * 255) ** 2
    return ((2 * mu1 * mu2 + C1) * (2 * cov + C2)) / \
           ((mu1 ** 2 + mu2 ** 2 + C1) * (v1 + v2 + C2))


def edge_density_ranking(doc):
    """按边缘密度排序页面 —— 密度越高越考验压缩（规格表、技术图纸）。"""
    out = []
    for pno in range(doc.page_count):
        pix = doc[pno].get_pixmap(dpi=40)
        a = np.frombuffer(pix.samples, dtype=np.uint8) \
             .reshape(pix.height, pix.width, pix.n)[:, :, :3].astype(np.float32)
        g = a.mean(axis=2)
        out.append((np.abs(np.diff(g, axis=1)).mean() +
                    np.abs(np.diff(g, axis=0)).mean(), pno))
    out.sort(reverse=True)
    return out


def compare(src_path, targets, visual=False, outdir=None):
    src = pymupdf.open(src_path)
    print(f"基准: {os.path.basename(src_path)}  "
          f"{os.path.getsize(src_path) / 1048576:.2f} MB  {src.page_count} 页")
    print()
    print(f"{'文件':<42} {'MB':>7} {'页':>4} {'尺寸一致':>8} "
          f"{'PSNR均':>8} {'PSNRmin':>8} {'SSIM均':>8}  判定")
    verdicts = {}
    for t in targets:
        d = pymupdf.open(t)
        size_ok = (d.page_count == src.page_count) and all(
            abs(d[i].rect.width - src[i].rect.width) < 0.5 and
            abs(d[i].rect.height - src[i].rect.height) < 0.5
            for i in range(min(d.page_count, src.page_count)))
        ps, ss = [], []
        for i in range(src.page_count):
            A = src[i].get_pixmap(dpi=200)
            B = d[i].get_pixmap(dpi=200)
            if (A.width, A.height, A.n) != (B.width, B.height, B.n):
                ps.append(0.0); ss.append(0.0); continue
            X = np.frombuffer(A.samples, dtype=np.uint8).reshape(A.height, A.width, A.n)
            Y = np.frombuffer(B.samples, dtype=np.uint8).reshape(B.height, B.width, B.n)
            ps.append(psnr(X[:, :, :3], Y[:, :, :3]))
            ss.append(ssim_global(X[:, :, :3], Y[:, :, :3]))
        pm, sm = float(np.mean(ps)), float(np.mean(ss))
        if sm >= 0.999 and pm >= 42:
            v = "视觉无损"
        elif sm >= 0.995:
            v = "屏幕无差别"
        else:
            v = "有损轻量版"
        verdicts[t] = v
        print(f"{os.path.basename(t):<42} {os.path.getsize(t) / 1048576:>7.2f} "
              f"{d.page_count:>4} {str(size_ok):>8} {pm:>8.2f} {min(ps):>8.2f} "
              f"{sm:>8.4f}  {v}")
        d.close()
    print()

    if visual:
        from PIL import Image, ImageDraw
        outdir = outdir or "/tmp/pdf_verify_visual"
        os.makedirs(outdir, exist_ok=True)
        rank = edge_density_ranking(src)
        picks = [rank[0][1]]                       # 最密的页
        picks += [i for i in (0, src.page_count // 2, src.page_count - 1)
                  if i not in picks][:2]
        for t in targets:
            d = pymupdf.open(t)
            tag = os.path.splitext(os.path.basename(t))[0].replace(" ", "_")[:30]
            for pno in picks:
                A = src[pno].get_pixmap(dpi=250)
                B = d[pno].get_pixmap(dpi=250)
                IA = Image.frombytes("RGB", (A.width, A.height), A.samples)
                IB = Image.frombytes("RGB", (B.width, B.height), B.samples)
                W, H = IA.size
                box = (int(W * 0.05), int(H * 0.25), int(W * 0.65), int(H * 0.60))
                ca, cb = IA.crop(box), IB.crop(box)
                canvas = Image.new("RGB", (ca.width, ca.height * 2 + 34), (245, 245, 245))
                canvas.paste(ca, (0, 0)); canvas.paste(cb, (0, ca.height + 34))
                ImageDraw.Draw(canvas).text(
                    (6, ca.height + 10),
                    f"P{pno + 1} 250DPI  TOP=ORIGINAL  BOTTOM={tag}", fill=(180, 0, 0))
                fn = f"{outdir}/{tag}_p{pno + 1}.png"
                canvas.save(fn)
                print("目检图:", fn)
            d.close()
        print("\n注意: 目检图必须用 Read 工具真正看一眼，不能只看指标。")
    src.close()


def main():
    args = sys.argv[1:]
    visual = False
    outdir = None
    if "--visual" in args:
        visual = True
        args.remove("--visual")
    if "--outdir" in args:
        i = args.index("--outdir")
        outdir = args[i + 1]
        del args[i:i + 2]
    if len(args) < 2:
        print(__doc__)
        sys.exit(1)
    compare(args[0], args[1:], visual=visual, outdir=outdir)


if __name__ == "__main__":
    main()
