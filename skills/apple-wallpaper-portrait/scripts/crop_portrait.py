#!/usr/bin/env python3
"""
Portrait crop tool for landscape stock wallpapers.

Apple ships every stock wallpaper in landscape. Turning one into a phone
wallpaper is NOT a resize — it is a *cropped recomposition*, and a naive
centre crop destroys scenery shots (on the macOS 27 Golden Gate sunset
wallpaper the bridge tower sits at x = 0.730, so a centre crop removes the
bridge entirely).

This script provides the two halves of the fix:
  detect  - locate the subject column(s) by colour/edge projection
  crop    - crop to a target aspect ratio, anchoring the subject at a
            chosen relative position inside the frame

Run `--help` on any subcommand.  See ../SKILL.md for the full workflow.

Examples
--------
  PY=/Users/eric/.workbuddy-ai/binaries/python/envs/default/bin/python
  $PY crop_portrait.py detect originals/04-bridge-sunset.jpeg
  $PY crop_portrait.py crop originals/04-bridge-sunset.jpeg \
        --out 4k/bridge-sunset.jpg --size 2160x3840 --anchor 2996:0.58
  $PY crop_portrait.py batch manifest.json
"""

import argparse
import json
import os
import sys

import numpy as np
from PIL import Image, ImageCms, ImageFilter

# ---------------------------------------------------------------- ICC profile


def srgb_icc_bytes():
    """Return sRGB ICC profile bytes so colours survive the round-trip."""
    prof = ImageCms.createProfile("sRGB")
    return ImageCms.ImageCmsProfile(prof).tobytes()


# ------------------------------------------------------------------- detect


def _column_score(arr, metric):
    """Return a length-W array scoring how 'interesting' each column is."""
    if metric == "vedge":
        # Vertical-edge energy.  The best general metric for wide aerial
        # scenery: bridge towers and cables are vertical structure against a
        # smooth sky, and unlike colour this works on silhouettes too.
        g = arr.mean(axis=2)
        dx = np.abs(np.diff(g, axis=1))
        return np.concatenate([dx[:, :1], dx], axis=1).mean(axis=0)
    if metric == "local_contrast":
        g = arr.mean(axis=2)
        blur = np.asarray(
            Image.fromarray(g.astype(np.uint8)).filter(ImageFilter.GaussianBlur(6))
        ).astype(np.float32)
        return np.abs(g - blur).mean(axis=0)
    if metric == "redness":
        # Warm landmarks.  R - (G+B)/2.  Dilutes badly when a large smooth
        # sky shares the column — see SKILL.md.
        s = arr[:, :, 0] - (arr[:, :, 1] + arr[:, :, 2]) / 2.0
        return s.mean(axis=0)
    if metric == "p95_redness":
        # Percentile instead of mean, so a small bright subject is not
        # averaged away by the sky above it.
        s = arr[:, :, 0] - (arr[:, :, 1] + arr[:, :, 2]) / 2.0
        return np.percentile(s, 95, axis=0)
    if metric == "warmth":
        return (arr[:, :, 0] - arr[:, :, 2]).mean(axis=0)
    if metric == "variance":
        return arr.mean(axis=2).std(axis=0)
    raise SystemExit(f"unknown metric: {metric}")


def _merge_peaks(col, W, top, merge_gap):
    """Non-maximum suppression, then merge peaks closer than `merge_gap`.

    A bridge tower produces a *pair* of peaks (its two edges).  Averaging the
    pair weighted by score recovers the tower centre, which is what you
    actually want to anchor on.  With merge_gap=0 the raw peaks are returned.
    """
    order = np.argsort(col)[::-1]
    picked = []
    min_sep = max(1, int(round(W * merge_gap))) if merge_gap > 0 else 1
    # Collect a generous pool first, then merge.
    pool = []
    sep = max(1, int(round(W * 0.02)))
    for x in order:
        x = int(x)
        if all(abs(x - p) >= sep for p in pool):
            pool.append(x)
        if len(pool) >= max(top * 4, 12):
            break

    if merge_gap <= 0:
        picked = pool[:top]
    else:
        used = [False] * len(pool)
        for i in range(len(pool)):
            if used[i]:
                continue
            group = [pool[i]]
            used[i] = True
            for j in range(i + 1, len(pool)):
                if not used[j] and abs(pool[j] - pool[i]) < min_sep:
                    group.append(pool[j])
                    used[j] = True
            w = np.array([max(float(col[p]), 0.0) + 1e-6 for p in group])
            centre = int(round(float(np.average(group, weights=w))))
            picked.append(centre)
        picked.sort(key=lambda p: -float(col[p]))
        picked = picked[:top]

    return picked, pool


def detect_anchors(path, band=0.55, smooth=41, top=3, metric="vedge",
                   merge_gap=0.0):
    """Locate candidate subject columns.

    `band` restricts the analysis to the top N fraction of the image — the
    subject is normally above the horizon, and the water below only adds noise.
    """
    im = Image.open(path).convert("RGB")
    arr = np.asarray(im).astype(np.float32)
    H, W = arr.shape[:2]

    rows = max(1, int(round(H * band)))
    col = _column_score(arr[:rows], metric)

    k = int(smooth)
    if k > 1:
        if k % 2 == 0:
            k += 1
        col = np.convolve(col, np.ones(k) / k, mode="same")

    picked, pool = _merge_peaks(col, W, top, merge_gap)

    return {
        "path": path,
        "width": W,
        "height": H,
        "metric": metric,
        "band": band,
        "smooth": k,
        "merge_gap": merge_gap,
        "anchors": [
            {"x": p, "frac": round(p / W, 4), "score": round(float(col[p]), 2)}
            for p in picked
        ],
        "raw_peaks": [
            {"x": p, "frac": round(p / W, 4), "score": round(float(col[p]), 2)}
            for p in pool[:8]
        ],
    }


# --------------------------------------------------------------------- crop


def compute_crop(W, H, tw, th, anchor=None):
    """Return (x0, y0, cw, ch) for a tw:th crop of a WxH image.

    `anchor` is (x_pixel_of_subject, desired_relative_position_in_crop),
    e.g. (2996, 0.58) puts the subject at 58% of the crop width.
    """
    aspect = tw / th
    cw = int(round(H * aspect))
    if cw <= W:
        ch, y0 = H, 0
    else:                                  # source too narrow -> fit width
        cw = W
        ch = int(round(W / aspect))
        y0 = (H - ch) // 2
    if anchor is not None:
        ax, frac = anchor
        x0 = int(round(ax - frac * cw))
    else:
        x0 = (W - cw) // 2
    x0 = max(0, min(x0, W - cw))
    y0 = max(0, min(y0, H - ch))
    return x0, y0, cw, ch


def parse_anchor(text):
    if text is None:
        return None
    try:
        x, frac = text.split(":")
        return (float(x), float(frac))
    except ValueError:
        raise SystemExit(
            f"--anchor must be X:FRAC (e.g. 2996:0.58), got {text!r}"
        )


def parse_size(text):
    try:
        w, h = text.lower().split("x")
        return int(w), int(h)
    except ValueError:
        raise SystemExit(f"--size must be WxH (e.g. 2160x3840), got {text!r}")


def do_crop(src, out, size, anchor=None, quality=95, allow_upscale=True,
            sharpen=True, verbose=True):
    """Crop, then optionally upscale.

    Returns a dict including `real_detail`: the pixel size actually captured
    from the source.  If that is smaller than the output size, the file is an
    upscale and `upscale_factor` > 1 — report it, do not hide it.
    """
    tw, th = size
    im = Image.open(src).convert("RGB")
    W, H = im.size
    x0, y0, cw, ch = compute_crop(W, H, tw, th, anchor)
    crop = im.crop((x0, y0, x0 + cw, y0 + ch))

    real_detail = [cw, ch]
    factor = max(tw / cw, th / ch)

    if factor > 1.0001 and not allow_upscale:
        raise SystemExit(
            f"refusing to upscale: crop is {cw}x{ch} but target is {tw}x{th} "
            f"({factor:.2f}x). Pass --allow-upscale to override, or pick a "
            f"smaller target."
        )

    result = crop.resize((tw, th), Image.LANCZOS)
    if factor > 1.0001 and sharpen:
        # Light unsharp mask to offset interpolation softening.  Calibrated
        # against a known-good super-resolution upscale of the same source:
        # see the acutance measurements in SKILL.md.  Even at maximum useful
        # strength this only closes part of the gap — LANCZOS+USM tops out
        # around gradX 1.06 where a real SR upscale reaches 1.37.
        result = result.filter(
            ImageFilter.UnsharpMask(radius=1.4, percent=70, threshold=3)
        )

    os.makedirs(os.path.dirname(os.path.abspath(out)) or ".", exist_ok=True)
    result.save(out, "JPEG", quality=quality, subsampling=0,
                optimize=True, icc_profile=srgb_icc_bytes(), dpi=(72, 72))

    info = {
        "out": out,
        "src": src,
        "src_size": [W, H],
        "crop": [x0, y0, cw, ch],
        "size": [tw, th],
        "real_detail": real_detail,
        "upscale_factor": round(factor, 3),
        "upscaled": factor > 1.0001,
        "kb": round(os.path.getsize(out) / 1024),
    }
    if verbose:
        if info["upscaled"]:
            flag = (f"  UPSCALED {factor:.2f}x "
                    f"(real detail {cw}x{ch})")
        else:
            flag = ""
        print(f"{out}  crop=({x0},{y0},{cw}x{ch}) -> {tw}x{th}  "
              f"{info['kb']} KB{flag}")
    return info


# -------------------------------------------------------------------- batch


def run_batch(manifest_path):
    """Manifest shape:

    {
      "targets": [{"name": "4k-9x16", "w": 2160, "h": 3840}, ...],
      "images":  [{"src": "...", "slug": "...", "anchor": [2996, 0.58]}, ...]
    }

    `anchor` may be omitted (centre crop) or null.  One pass emits every
    image at every target size, so adding a second phone aspect ratio later
    costs one line.
    """
    with open(manifest_path) as fh:
        m = json.load(fh)
    base = os.path.dirname(os.path.abspath(manifest_path))
    targets = m["targets"]
    allow_up = m.get("allow_upscale", True)
    report = []
    for img in m["images"]:
        src = img["src"]
        if not os.path.isabs(src):
            src = os.path.join(base, src)
        anchor = img.get("anchor")
        if anchor is not None:
            anchor = (float(anchor[0]), float(anchor[1]))
        for t in targets:
            out = os.path.join(base, t["name"], f"{img['slug']}.jpg")
            report.append(do_crop(src, out, (t["w"], t["h"]), anchor,
                                  allow_upscale=allow_up))
    up = [r for r in report if r["upscaled"]]
    print(f"\n{len(report)} file(s) written, {len(up)} upscaled")
    if up:
        print("NOTE: these carry less real detail than their pixel size:")
        for r in up:
            print(f"   {r['out']}  {r['upscale_factor']}x  "
                  f"real {r['real_detail'][0]}x{r['real_detail'][1]}")
    return report


# ---------------------------------------------------------------------- CLI


def main(argv=None):
    ap = argparse.ArgumentParser(
        prog="crop_portrait.py",
        description="Portrait-crop landscape stock wallpapers.",
    )
    sub = ap.add_subparsers(dest="cmd", required=True)

    d = sub.add_parser("detect", help="locate subject columns")
    d.add_argument("image")
    d.add_argument("--band", type=float, default=0.55,
                   help="analyse only the top N fraction (default 0.55)")
    d.add_argument("--smooth", type=int, default=41,
                   help="moving-average window in px (default 41)")
    d.add_argument("--top", type=int, default=3)
    d.add_argument("--metric", default="vedge",
                   choices=["vedge", "local_contrast", "redness",
                            "p95_redness", "warmth", "variance"])
    d.add_argument("--merge-gap", type=float, default=0.0,
                   help="merge peaks closer than this fraction of width into "
                        "one centroid (0 = off, the default). Peak PAIRS are "
                        "usually a tower's two edges — take their midpoint "
                        "yourself. Naive merging is unreliable: on the macOS 27 "
                        "Day wallpaper the bridge deck adds a peak 0.02 from "
                        "the tower edge, which drags the centroid off-centre.")
    d.add_argument("--json", action="store_true", help="raw JSON output")

    c = sub.add_parser("crop", help="crop a single image")
    c.add_argument("image")
    c.add_argument("--out", required=True)
    c.add_argument("--size", required=True, help="WxH, e.g. 2160x3840")
    c.add_argument("--anchor", default=None, help="X:FRAC, e.g. 2996:0.58")
    c.add_argument("--quality", type=int, default=95)
    c.add_argument("--allow-upscale", action="store_true",
                   help="permit upscaling beyond the source's real detail")
    c.add_argument("--no-sharpen", action="store_true",
                   help="skip the unsharp mask applied after upscaling")

    b = sub.add_parser("batch", help="crop a whole manifest")
    b.add_argument("manifest")

    args = ap.parse_args(argv)

    if args.cmd == "detect":
        info = detect_anchors(args.image, args.band, args.smooth,
                              args.top, args.metric, args.merge_gap)
        if args.json:
            print(json.dumps(info, indent=2))
        else:
            print(f"{args.image}  {info['width']}x{info['height']}  "
                  f"metric={info['metric']}  merge_gap={info['merge_gap']}")
            print("  anchors (use these):")
            for a in info["anchors"]:
                print(f"    x={a['x']:<6} frac={a['frac']:<8} score={a['score']}")
            print("  raw peaks (pre-merge):")
            for a in info["raw_peaks"]:
                print(f"    x={a['x']:<6} frac={a['frac']:<8} score={a['score']}")
        return 0

    if args.cmd == "crop":
        do_crop(args.image, args.out, parse_size(args.size),
                parse_anchor(args.anchor), args.quality,
                allow_upscale=args.allow_upscale,
                sharpen=not args.no_sharpen)
        return 0

    if args.cmd == "batch":
        run_batch(args.manifest)
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
