#!/usr/bin/env python3
"""Stage 2b - deterministic pixel measurement of the reference thumbnails.

Deliberately uses only Pillow (no numpy / sklearn / cv2). Palette extraction
uses Pillow's built-in MEDIANCUT quantiser rather than k-means: k-means
averages photographic colour into mud, which is exactly the wrong answer for
"what are the signature colours of this channel".

Outputs pixel_stats.json containing per-image measurements plus a
view-weighted aggregate. The numbers here are precise anchors (exact hex,
coverage %) - the qualitative style read happens in Stage 3.

Usage:
    python 03_analyze.py <channel-dir-or-slug>
"""
from __future__ import annotations

import argparse
import math
from pathlib import Path

from PIL import Image, ImageStat

from _common import read_json, resolve_channel_dir, write_json

ANALYSIS_WIDTH = 512
PALETTE_COLORS = 12
GRID = 4
ACCENT_SAT_FLOOR = 191  # 0.75 * 255


# --------------------------------------------------------------------------- #
# colour helpers
# --------------------------------------------------------------------------- #
def to_hex(rgb) -> str:
    r, g, b = (max(0, min(255, int(round(c)))) for c in rgb[:3])
    return f"#{r:02X}{g:02X}{b:02X}"


def hex_to_rgb(value: str) -> tuple[int, int, int]:
    v = value.lstrip("#")
    return tuple(int(v[i : i + 2], 16) for i in (0, 2, 4))  # type: ignore[return-value]


def rgb_distance(a, b) -> float:
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a[:3], b[:3])))


def delta_e76(lab_a, lab_b) -> float:
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(lab_a[:3], lab_b[:3])))


def describe_colour(rgb) -> str:
    """Human-meaningful label for a colour, saturation- and lightness-aware.

    Low-saturation colours get a lightness label instead of a misleading hue
    name (a muted brown should not be called "red").
    """
    r, g, b = (max(0, min(255, int(round(c)))) for c in rgb[:3])
    h, s, v = Image.new("RGB", (1, 1), (r, g, b)).convert("HSV").getpixel((0, 0))
    sat, val = s / 255, v / 255

    if sat < 0.15:
        for limit, name in (
            (0.18, "near-black"), (0.40, "dark-neutral"), (0.70, "mid-neutral"),
            (0.90, "light-neutral"), (1.01, "near-white"),
        ):
            if val < limit:
                return name
        return "near-white"

    base = hue_name(h, s)
    if sat < 0.35:
        return f"muted-{base}"
    if val < 0.35:
        return f"deep-{base}"
    if val > 0.88 and sat < 0.6:
        return f"pale-{base}"
    return base


def hue_name(h: int, sat: int = 255) -> str:
    """Pillow HSV hue is 0-255; map to a coarse bucket name."""
    deg = h * 360 / 256
    for limit, name in (
        (15, "red"), (45, "orange"), (70, "yellow"), (105, "yellow-green"),
        (150, "green"), (180, "cyan"), (210, "azure"), (260, "blue"),
        (290, "violet"), (330, "magenta"), (360, "red"),
    ):
        if deg < limit:
            return name
    return "red"


def pixels(img: Image.Image) -> list:
    """Pillow >= 12 deprecates getdata(); support both spellings."""
    fn = getattr(img, "get_flattened_data", None)
    return list(fn() if fn else img.getdata())


# --------------------------------------------------------------------------- #
# per-image analysis
# --------------------------------------------------------------------------- #
def extract_palette(img: Image.Image) -> list[dict]:
    q = img.quantize(colors=PALETTE_COLORS, method=Image.Quantize.MEDIANCUT)
    palette = q.getpalette() or []
    counts = q.getcolors() or []
    total = sum(c for c, _ in counts) or 1

    out = []
    for count, idx in sorted(counts, reverse=True):
        rgb = tuple(palette[idx * 3 : idx * 3 + 3])
        if len(rgb) < 3:
            continue
        hsv = Image.new("RGB", (1, 1), rgb).convert("HSV").getpixel((0, 0))
        out.append(
            {
                "hex": to_hex(rgb),
                "rgb": list(rgb),
                "coverage_pct": round(100 * count / total, 2),
                "hue": describe_colour(rgb),
                "sat": round(hsv[1] / 255, 3),
                "val": round(hsv[2] / 255, 3),
            }
        )
    return out


def analyze_image(path: Path) -> dict:
    with Image.open(path) as im:
        im.load()
        orig_w, orig_h = im.size
        img = im.convert("RGB")

    small = img.resize(
        (ANALYSIS_WIDTH, max(1, round(ANALYSIS_WIDTH * orig_h / orig_w))),
        Image.LANCZOS,
    )
    rgb_data = pixels(small)
    hsv_data = pixels(small.convert("HSV"))
    n = len(rgb_data)

    # ---- saturation / value statistics -----------------------------------
    sat_mean = sum(s for _, s, _ in hsv_data) / n
    val_mean = sum(v for _, _, v in hsv_data) / n
    pct_high_sat = 100 * sum(1 for _, s, _ in hsv_data if s > 178) / n

    # ---- accent colours: small-area high saturation -----------------------
    # Taking the mean of ALL high-saturation pixels blends red props + blue sky +
    # yellow type into mud. Bucket them by hue instead and report each cluster.
    hue_buckets: dict[int, list] = {}
    for rgb, (h, s, _) in zip(rgb_data, hsv_data):
        if s >= ACCENT_SAT_FLOOR:
            hue_buckets.setdefault(h * 12 // 256, []).append(rgb)

    if not hue_buckets:  # very flat image - fall back to the most saturated 1%
        ranked = sorted(range(n), key=lambda i: hsv_data[i][1], reverse=True)
        hue_buckets = {0: [rgb_data[i] for i in ranked[: max(1, n // 100)]]}

    accents = []
    for _, px in sorted(hue_buckets.items(), key=lambda kv: len(kv[1]), reverse=True)[:3]:
        mean_rgb = tuple(sum(c[i] for c in px) / len(px) for i in range(3))
        hsv = (
            Image.new("RGB", (1, 1), tuple(int(round(c)) for c in mean_rgb))
            .convert("HSV")
            .getpixel((0, 0))
        )
        accents.append(
            {
                "hex": to_hex(mean_rgb),
                "coverage_pct": round(100 * len(px) / n, 2),
                "hue": describe_colour(mean_rgb),
                "sat": round(hsv[1] / 255, 3),
                "val": round(hsv[2] / 255, 3),
            }
        )
    accent = accents[0]

    # ---- colorfulness (Hasler & Suesstrunk 2003) -------------------------
    sum_rg = sum_yb = sum_rg2 = sum_yb2 = 0.0
    for r, g, b in rgb_data:
        rg = r - g
        yb = 0.5 * (r + g) - b
        sum_rg += rg
        sum_yb += yb
        sum_rg2 += rg * rg
        sum_yb2 += yb * yb
    mean_rg, mean_yb = sum_rg / n, sum_yb / n
    var_rg = max(0.0, sum_rg2 / n - mean_rg**2)
    var_yb = max(0.0, sum_yb2 / n - mean_yb**2)
    colorfulness = round(
        math.sqrt(var_rg + var_yb) + 0.3 * math.sqrt(mean_rg**2 + mean_yb**2), 2
    )

    # ---- luminance contrast: centre vs border ----------------------------
    luma = small.convert("L")
    w, h = small.size
    bw, bh = max(1, int(w * 0.08)), max(1, int(h * 0.08))
    border_boxes = [
        (0, 0, w, bh),
        (0, h - bh, w, h),
        (0, bh, bw, h - bh),
        (w - bw, bh, w, h - bh),
    ]
    border_luma = sum(
        ImageStat.Stat(luma.crop(b)).mean[0] for b in border_boxes
    ) / len(border_boxes)
    cx0, cy0 = int(w * 0.25), int(h * 0.25)
    centre_box = (cx0, cy0, w - cx0, h - cy0)
    centre_luma = ImageStat.Stat(luma.crop(centre_box)).mean[0]
    global_luma_std = ImageStat.Stat(luma).stddev[0]

    # ---- LAB delta-E between centre and border ---------------------------
    lab = small.convert("LAB")
    lab_b = [ImageStat.Stat(lab.crop(b)).mean for b in border_boxes]
    lab_b_mean = [sum(p[i] for p in lab_b) / len(lab_b) for i in range(3)]
    subject_bg_delta_e = round(
        delta_e76(ImageStat.Stat(lab.crop(centre_box)).mean, lab_b_mean), 1
    )

    # ---- 4x4 grid: where is the visual mass? -----------------------------
    cells = []
    cw, chh = w // GRID, h // GRID
    for gy in range(GRID):
        row = []
        for gx in range(GRID):
            box = (gx * cw, gy * chh, (gx + 1) * cw, (gy + 1) * chh)
            cell_luma = luma.crop(box)
            cell_rgb = small.crop(box)
            st_l = ImageStat.Stat(cell_luma)
            st_h = ImageStat.Stat(cell_rgb.convert("HSV"))
            row.append(
                {
                    "luma_mean": round(st_l.mean[0], 1),
                    "luma_std": round(st_l.stddev[0], 1),
                    "sat_mean": round(st_h.mean[1], 1),
                    "val_mean": round(st_h.mean[2], 1),
                    "rgb_mean": [round(v) for v in ImageStat.Stat(cell_rgb).mean],
                }
            )
        cells.append(row)

    flat_cells = [
        (gx, gy)
        for gy in range(GRID)
        for gx in range(GRID)
        if cells[gy][gx]["luma_std"] < 22 and cells[gy][gx]["sat_mean"] < 70
    ]

    def centroid(score_fn) -> dict:
        scores = [
            (gx, gy, score_fn(cells[gy][gx]))
            for gy in range(GRID)
            for gx in range(GRID)
        ]
        total = sum(s for _, _, s in scores) or 1
        return {
            "x_pct": round(100 * sum(gx * s for gx, _, s in scores) / total / (GRID - 1), 1),
            "y_pct": round(100 * sum(gy * s for _, gy, s in scores) / total / (GRID - 1), 1),
        }

    return {
        "path": str(path),
        "original_size": [orig_w, orig_h],
        "aspect_ratio": round(orig_w / orig_h, 4),
        "palette": extract_palette(img),
        "accent": accent,
        "accents": accents,
        "stats": {
            "sat_mean": round(sat_mean / 255, 3),
            "val_mean": round(val_mean / 255, 3),
            "pct_pixels_high_sat": round(pct_high_sat, 2),
            "colorfulness": colorfulness,
            "border_luma": round(border_luma, 1),
            "centre_luma": round(centre_luma, 1),
            "global_luma_std": round(global_luma_std, 1),
            "subject_bg_delta_e": subject_bg_delta_e,
            "contrast_ratio": round(
                (max(centre_luma, border_luma) + 5) / (min(centre_luma, border_luma) + 5), 2
            ),
        },
        "grid": cells,
        "grid_summary": {
            "flat_cell_ratio": round(len(flat_cells) / (GRID * GRID), 3),
            "flat_cells": [{"col": c, "row": r} for c, r in flat_cells],
            "bright_mass_centroid": centroid(lambda c: c["luma_mean"]),
            "saturated_mass_centroid": centroid(lambda c: c["sat_mean"]),
            "negative_space_pct": round(
                100
                * sum(
                    1
                    for gy in range(GRID)
                    for gx in range(GRID)
                    if cells[gy][gx]["luma_std"] < 20 and cells[gy][gx]["sat_mean"] < 60
                )
                / (GRID * GRID),
                1,
            ),
        },
    }


# --------------------------------------------------------------------------- #
# aggregation
# --------------------------------------------------------------------------- #
def merge_palettes(entries: list[tuple[float, list[dict]]], threshold: float = 60.0):
    """Merge per-image palettes into a view-weighted consensus palette.

    Colours within `threshold` RGB distance are treated as the same colour.
    `appears_in_images` counts distinct source images, so a single image that
    contributes two nearby entries to the same bucket still counts once.
    """
    buckets: list[dict] = []
    for image_idx, (weight, palette) in enumerate(entries):
        for colour in palette:
            rgb = hex_to_rgb(colour["hex"])
            contribution = weight * colour["coverage_pct"]
            for b in buckets:
                if rgb_distance(rgb, b["_rgb"]) < threshold:
                    b["weight"] += contribution
                    b["_images"].add(image_idx)
                    b["_rgb"] = [
                        (b["_rgb"][i] * (len(b["_images"]) - 1) + rgb[i])
                        / len(b["_images"])
                        for i in range(3)
                    ]
                    break
            else:
                buckets.append(
                    {
                        "_rgb": list(rgb),
                        "hex": colour["hex"],
                        "weight": contribution,
                        "_images": {image_idx},
                        "hue": colour["hue"],
                    }
                )

    total = sum(b["weight"] for b in buckets) or 1
    n_images = max(1, len(entries))
    merged = []
    for b in sorted(buckets, key=lambda b: b["weight"], reverse=True):
        rgb = [max(0, min(255, int(round(c)))) for c in b["_rgb"]]
        merged.append(
            {
                "hex": to_hex(rgb),
                "hue": describe_colour(rgb),
                "weighted_coverage_pct": round(100 * b["weight"] / total, 2),
                "appears_in_images": len(b["_images"]),
                "consistency_pct": round(100 * len(b["_images"]) / n_images, 1),
            }
        )
    return merged[:10]


def weighted_mean(pairs: list[tuple[float, float]]) -> float:
    total = sum(w for w, _ in pairs) or 1
    return round(sum(w * v for w, v in pairs) / total, 3)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("channel")
    args = ap.parse_args()

    ch_dir = resolve_channel_dir(args.channel)
    manifest = read_json(ch_dir / "refs" / "manifest.json")
    refs = [r for r in manifest["references"] if r.get("ok")]
    if not refs:
        raise SystemExit("error: no successfully downloaded references in manifest.json")

    print(f"[analyze] measuring {len(refs)} thumbnails")

    per_image = []
    for i, ref in enumerate(refs, 1):
        stats = analyze_image(Path(ref["path"]))
        views = ref.get("views") or 0
        weight = math.log10(views + 10)
        rec = {
            "video_id": ref["video_id"],
            "title": ref["title"],
            "views": ref.get("views"),
            "views_text": ref.get("views_text"),
            "age_days": ref.get("age_days"),
            "bucket": ref.get("bucket"),
            "quality_used": ref.get("quality_used"),
            "view_weight": round(weight, 4),
            **stats,
        }
        per_image.append(rec)
        top = stats["palette"][0]
        print(
            f"[analyze] {i:>2}/{len(refs)}  dom={top['hex']} ({top['coverage_pct']:>5.1f}%)  "
            f"accent={stats['accent']['hex']}  colour={stats['stats']['colorfulness']:>6.1f}  "
            f"dE={stats['stats']['subject_bg_delta_e']:>5.1f}  {ref['title'][:34]}"
        )

    weights = [img["view_weight"] for img in per_image]
    pal_entries = list(zip(weights, [img["palette"] for img in per_image]))
    consensus_palette = merge_palettes(pal_entries)

    accent_entries = []
    for w, img in zip(weights, per_image):
        items = img.get("accents", [img["accent"]])
        share = w / max(1, len(items))  # keep each image's total weight constant
        accent_entries.append(
            (
                share,
                [
                    {"hex": a["hex"], "coverage_pct": a["coverage_pct"], "hue": a["hue"]}
                    for a in items
                ],
            )
        )
    consensus_accent = merge_palettes(accent_entries, threshold=70.0)

    agg_stats = {
        key: weighted_mean([(w, img["stats"][key]) for w, img in zip(weights, per_image)])
        for key in per_image[0]["stats"]
    }

    # deviation from the consensus: how much does each image stand out?
    consensus_rgb = [hex_to_rgb(c["hex"]) for c in consensus_palette[:5]]
    palette_dist = [
        min(rgb_distance(hex_to_rgb(img["palette"][0]["hex"]), c) for c in consensus_rgb)
        for img in per_image
    ]
    sat_dev = [abs(img["stats"]["sat_mean"] - agg_stats["sat_mean"]) for img in per_image]
    col_dev = [
        abs(img["stats"]["colorfulness"] - agg_stats["colorfulness"]) for img in per_image
    ]
    max_pd = max(palette_dist) or 1
    max_sd = max(sat_dev) or 1
    max_cd = max(col_dev) or 1
    for img, pd, sd, cd in zip(per_image, palette_dist, sat_dev, col_dev):
        img["deviation_score"] = round(
            100 * (0.5 * pd / max_pd + 0.3 * sd / max_sd + 0.2 * cd / max_cd), 1
        )

    ranked = sorted(per_image, key=lambda i: i["deviation_score"], reverse=True)
    outliers = [i["video_id"] for i in ranked[:2]]

    # era check: does the older half look different from the newer half?
    dated = sorted([i for i in per_image if i["age_days"] is not None],
                   key=lambda i: i["age_days"])
    era = {"compared": False}
    if len(dated) >= 6:
        mid = len(dated) // 2
        older, newer = dated[:mid], dated[mid:]
        old_sat = sum(i["stats"]["sat_mean"] for i in older) / len(older)
        new_sat = sum(i["stats"]["sat_mean"] for i in newer) / len(newer)
        old_luma = sum(i["stats"]["border_luma"] for i in older) / len(older)
        new_luma = sum(i["stats"]["border_luma"] for i in newer) / len(newer)
        era = {
            "compared": True,
            "older_half_mean_sat": round(old_sat, 3),
            "newer_half_mean_sat": round(new_sat, 3),
            "older_half_border_luma": round(old_luma, 1),
            "newer_half_border_luma": round(new_luma, 1),
            "sat_shift": round(new_sat - old_sat, 3),
            "luma_shift": round(new_luma - old_luma, 1),
            "style_shift_detected": abs(new_sat - old_sat) > 0.12
            or abs(new_luma - old_luma) > 35,
        }

    sizes = {f"{i['original_size'][0]}x{i['original_size'][1]}" for i in per_image}
    qualities = sorted({i["quality_used"] for i in per_image})

    write_json(
        ch_dir / "pixel_stats.json",
        {
            "channel_name": manifest.get("channel_name"),
            "sample_size": len(per_image),
            "canvas_variants": sorted(sizes),
            "quality_tiers_used": qualities,
            "all_maxres": qualities == ["maxresdefault"],
            "consensus_palette": consensus_palette,
            "consensus_accent": consensus_accent[:4],
            "aggregate_stats": agg_stats,
            "era_check": era,
            "outlier_video_ids": outliers,
            "per_image": per_image,
            "method_notes": [
                "Palette via Pillow MEDIANCUT quantisation (k-means intentionally avoided).",
                "Aggregate palette weighted by log10(views+10).",
                "accent = mean colour of pixels with S >= 0.75 (small-area high-saturation colour).",
                "grid = 4x4 cells; flat cells (low luma stddev + low saturation) suggest text bands "
                "or empty background. Interpretation is Stage 3's job, not this script's.",
                "subject_bg_delta_e = CIE76 delta-E between centre region and border frame in LAB.",
            ],
        },
    )

    print()
    print(f"[analyze] consensus palette ({len(consensus_palette)} colours):")
    for c in consensus_palette[:6]:
        print(
            f"           {c['hex']}  {c['weighted_coverage_pct']:>5.1f}%  "
            f"{c['hue']:<12} in {c['appears_in_images']}/{len(per_image)} images"
        )
    print(f"[analyze] consensus accent: {[c['hex'] for c in consensus_accent[:3]]}")
    print(f"[analyze] aggregate: {agg_stats}")
    print(f"[analyze] era shift detected: {era.get('style_shift_detected')}")
    print(f"[analyze] outliers: {outliers}")
    print(f"[analyze] wrote {ch_dir / 'pixel_stats.json'}")


if __name__ == "__main__":
    main()
