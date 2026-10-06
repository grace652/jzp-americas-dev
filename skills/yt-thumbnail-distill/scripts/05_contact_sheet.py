#!/usr/bin/env python3
"""Stage 3 prep - build a 4x4 contact sheet of the reference thumbnails.

The agent reads this single image first to get a global feel for the channel's
style, then opens 4-6 individual originals for detail. Reading one grid beats
reading sixteen full-size images.

Usage:
    python 05_contact_sheet.py <channel-dir-or-slug> [--cols 4]
"""
from __future__ import annotations

import argparse
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from _common import read_json, resolve_channel_dir

CELL_W = 480
LABEL_H = 34
PAD = 10
HEADER_H = 64

FONT_CANDIDATES = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
    "/System/Library/Fonts/Supplemental/Verdana.ttf",
]


def load_font(size: int):
    for path in FONT_CANDIDATES:
        if Path(path).exists():
            try:
                return ImageFont.truetype(path, size)
            except OSError:
                continue
    return ImageFont.load_default()


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("channel")
    ap.add_argument("--cols", type=int, default=4)
    args = ap.parse_args()

    ch_dir = resolve_channel_dir(args.channel)
    manifest = read_json(ch_dir / "refs" / "manifest.json")
    refs = [r for r in manifest["references"] if r.get("ok")]
    if not refs:
        raise SystemExit("error: no references available")

    stats_file = ch_dir / "pixel_stats.json"
    stats = read_json(stats_file) if stats_file.exists() else {}
    dev = {p["video_id"]: p.get("deviation_score") for p in stats.get("per_image", [])}

    cols = max(1, min(args.cols, len(refs)))
    rows = math.ceil(len(refs) / cols)
    cell_h = round(CELL_W * 9 / 16)
    sheet_w = PAD + cols * (CELL_W + PAD)
    sheet_h = HEADER_H + PAD + rows * (cell_h + LABEL_H + PAD)

    sheet = Image.new("RGB", (sheet_w, sheet_h), (18, 18, 20))
    draw = ImageDraw.Draw(sheet)
    f_title = load_font(24)
    f_label = load_font(15)

    channel = manifest.get("channel_name") or ch_dir.name
    draw.text(
        (PAD + 4, 16),
        f"{channel}  -  {len(refs)} reference thumbnails"
        f"   (sample: {manifest.get('ok_count')}/{manifest.get('sample_size')})",
        font=f_title,
        fill=(240, 240, 240),
    )

    for i, ref in enumerate(refs):
        col, row = i % cols, i // cols
        x = PAD + col * (CELL_W + PAD)
        y = HEADER_H + PAD + row * (cell_h + LABEL_H + PAD)

        with Image.open(ref["path"]) as im:
            thumb = im.convert("RGB").resize((CELL_W, cell_h), Image.LANCZOS)
        sheet.paste(thumb, (x, y))
        draw.rectangle([x, y, x + CELL_W - 1, y + cell_h - 1], outline=(70, 70, 76))

        views = ref.get("views_text") or "n/a"
        age = ref.get("age_text") or "n/a"
        d = dev.get(ref["video_id"])
        extra = f"  dev={d}" if d is not None else ""
        draw.text(
            (x + 2, y + cell_h + 4),
            f"#{i:>2} {ref['video_id']}  {views}  {age}  [{ref.get('bucket')}]{extra}",
            font=f_label,
            fill=(200, 200, 205),
        )
        draw.text(
            (x + 2, y + cell_h + 19),
            ref["title"][:64],
            font=f_label,
            fill=(150, 150, 158),
        )

    out = ch_dir / "contact_sheet.jpg"
    sheet.save(out, "JPEG", quality=90)
    print(f"[sheet] wrote {out}  ({sheet_w}x{sheet_h}, {len(refs)} cells)")
    print("[sheet] order:")
    for i, ref in enumerate(refs):
        print(
            f"        #{i:>2} {ref['video_id']}  {(ref.get('views_text') or 'n/a'):>10}  "
            f"[{ref.get('bucket'):<9}]  {ref['title'][:50]}"
        )


if __name__ == "__main__":
    main()
