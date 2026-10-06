#!/usr/bin/env python3
"""Render a thumbnail locally from the style DNA - deterministic, no AI involved.

This is the high-fidelity path for CJK headlines. GPT-image class models render
Chinese characters unreliably (missing strokes, Japanese/Traditional variants,
stray Latin letters). Since this family of designs is essentially
"paper texture + typography", the robust split is:

    AI generates the blank background  ->  this script sets the type

Result: 100% correct Simplified Chinese glyphs, exact font, reproducible
chromatic-aberration effect.

Usage:
    python 06_render_cover.py <channel> --text "人生大坑" --top "第 24 集" --out cover.png
    python 06_render_cover.py <channel> --text "内耗" --bg chatgpt-bg.png --out cover.png
    python 06_render_cover.py <channel> --text "希望" --out cover.png --width 1280
"""
from __future__ import annotations

import argparse
import random
import re
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

from _common import read_json, resolve_channel_dir

# Sensible fallbacks if the DNA does not specify a font.
CJK_FONT_STACK = [
    ("/System/Library/Fonts/Supplemental/Songti.ttc", 0, "Songti SC Black"),
    ("/System/Library/Fonts/Supplemental/Songti.ttc", 1, "Songti SC Bold"),
    ("/System/Library/Fonts/Hiragino Sans GB.ttc", 2, "Hiragino Sans GB W6"),
    ("/System/Library/Fonts/STHeiti Medium.ttc", 1, "Heiti SC Medium"),
]
LATIN_FONT_STACK = [
    ("/System/Library/Fonts/Supplemental/PlayfairDisplay-Bold.ttf", 0, "Playfair Display Bold"),
    ("/System/Library/Fonts/Supplemental/Georgia Bold.ttf", 0, "Georgia Bold"),
    ("/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf", 0, "Times New Roman Bold"),
    ("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 0, "Arial Bold"),
]


# --------------------------------------------------------------------------- #
# fonts
# --------------------------------------------------------------------------- #
def pick_font(explicit: str | None, explicit_index: int | None, stack) -> tuple[str, int, str]:
    if explicit:
        p = Path(explicit)
        if not p.exists():
            raise SystemExit(f"error: font file not found: {explicit}")
        return str(p), explicit_index or 0, p.name
    for path, idx, label in stack:
        if Path(path).exists():
            try:
                ImageFont.truetype(path, 40, index=idx)
                return path, idx, label
            except OSError:
                continue
    raise SystemExit("error: no usable font found; pass --font-file explicitly")


def load_font(path: str, index: int, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size, index=index)


def fit_size(path: str, index: int, text: str, target_glyph_h: int) -> int:
    """Binary-search the em size whose rendered glyph height is closest to target."""
    lo, hi = 10, 3000
    best, best_err = lo, None
    while lo <= hi:
        size = (lo + hi) // 2
        bb = load_font(path, index, size).getbbox(text)
        h = max(1, bb[3] - bb[1])
        err = abs(h - target_glyph_h)
        if best_err is None or err < best_err:
            best, best_err = size, err
        if h < target_glyph_h:
            lo = size + 1
        else:
            hi = size - 1
    return best


# --------------------------------------------------------------------------- #
# background
# --------------------------------------------------------------------------- #
def add_signed_noise(img: Image.Image, sigma: float, scale_div: int = 1,
                     gain: float = 1.0) -> Image.Image:
    """Add zero-mean Gaussian noise without shifting the mean brightness.

    ImageChops.add(a, b, offset=-128) yields a + (b - 128), so the noise stays
    centred on the base tone and `sigma * gain` is the resulting stddev.
    """
    w, h = img.size
    sw, sh = max(2, w // scale_div), max(2, h // scale_div)
    n = Image.effect_noise((sw, sh), sigma).convert("L")
    if (sw, sh) != (w, h):
        n = n.resize((w, h), Image.BICUBIC)
    if gain != 1.0:
        n = n.point(lambda v: int(max(0, min(255, 128 + (v - 128) * gain))))
    return ImageChops.add(img, Image.merge("RGB", (n, n, n)), scale=1, offset=-128)


def procedural_paper(width: int, height: int, base_hex: str = "#F3F3F3",
                     seed: int = 7) -> Image.Image:
    """Off-white paper, calibrated to the reference measurements.

    Reference background measures mean 243 with stddev only 3.3-4.2, so this is
    deliberately almost flat: a hint of large-scale unevenness, fine grain, two
    faint fold creases, and a barely-there edge darkening.
    """
    rnd = random.Random(seed)
    rgb = tuple(int(base_hex.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4))
    img = Image.new("RGB", (width, height), rgb)

    # large-scale soft unevenness - kept very low, the reference energy is mostly
    # in fine grain rather than visible blotching
    img = add_signed_noise(img, sigma=11, scale_div=42, gain=0.10)
    # fine grain (~3.3 stddev, pixel level)
    img = add_signed_noise(img, sigma=3.3, scale_div=1, gain=1.0)

    # faint fold creases
    creases = Image.new("L", (width, height), 0)
    cd = ImageDraw.Draw(creases)
    for _ in range(rnd.randint(2, 3)):
        if rnd.random() < 0.55:
            x = rnd.randint(int(width * 0.15), int(width * 0.85))
            cd.line([(x + rnd.randint(-5, 5), 0), (x + rnd.randint(-5, 5), height)],
                    fill=rnd.randint(6, 13), width=1)
        else:
            y = rnd.randint(int(height * 0.15), int(height * 0.85))
            cd.line([(0, y + rnd.randint(-3, 3)), (width, y + rnd.randint(-3, 3))],
                    fill=rnd.randint(5, 11), width=1)
    creases = creases.filter(ImageFilter.GaussianBlur(3.0))
    img = ImageChops.subtract(img, Image.merge("RGB", (creases, creases, creases)), scale=1)

    # barely-there edge darkening
    vign = Image.new("L", (width, height), 0)
    vd = ImageDraw.Draw(vign)
    steps = 60
    for i in range(steps):
        t = i / steps
        inset = int(min(width, height) * 0.45 * (1 - t))
        vd.rectangle([inset, inset, width - inset, height - inset], outline=int(9 * (1 - t)))
    vign = vign.filter(ImageFilter.GaussianBlur(min(width, height) * 0.05))
    img = ImageChops.subtract(img, Image.merge("RGB", (vign, vign, vign)), scale=1)
    return img


def cover_crop(img: Image.Image, width: int, height: int) -> Image.Image:
    img = img.convert("RGB")
    src_ratio = img.width / img.height
    dst_ratio = width / height
    if src_ratio > dst_ratio:
        new_w = int(img.height * dst_ratio)
        left = (img.width - new_w) // 2
        img = img.crop((left, 0, left + new_w, img.height))
    else:
        new_h = int(img.width / dst_ratio)
        top = (img.height - new_h) // 2
        img = img.crop((0, top, img.width, top + new_h))
    return img.resize((width, height), Image.LANCZOS)


# --------------------------------------------------------------------------- #
# type rendering
# --------------------------------------------------------------------------- #
def render_mask(text: str, font: ImageFont.FreeTypeFont, tracking: int = 0) -> Image.Image:
    """White-on-black ink mask, centred, with optional letter tracking."""
    pad = 40
    widths = []
    for ch in text:
        bb = font.getbbox(ch)
        widths.append(bb[2] - bb[0])
    total_w = sum(widths) + tracking * max(0, len(text) - 1)
    asc, desc = font.getmetrics()
    w = max(1, total_w + pad * 2)
    h = max(1, asc + desc + pad * 2)

    mask = Image.new("L", (w, h), 0)
    d = ImageDraw.Draw(mask)
    x = pad
    for ch, cw in zip(text, widths):
        bb = font.getbbox(ch)
        d.text((x - bb[0], pad), ch, font=font, fill=255)
        x += cw + tracking
    return mask


def chromatic_text_layer(mask: Image.Image, offset: int, strength: float = 1.0) -> Image.Image:
    """Build the RGB ink layer with RGB-split fringing.

    Red fringe on the left of each stroke, cyan fringe on the right.
    Derived from:  R = 1 - mask_shifted_right,  G = B = 1 - mask_shifted_left
    """
    w, h = mask.size
    right = Image.new("L", (w, h), 0)
    right.paste(mask, (offset, 0))
    left = Image.new("L", (w, h), 0)
    left.paste(mask, (-offset, 0))

    layer = Image.merge(
        "RGB",
        (ImageChops.invert(right), ImageChops.invert(left), ImageChops.invert(left)),
    )
    if strength < 1.0:
        layer = Image.blend(Image.new("RGB", (w, h), (255, 255, 255)), layer, strength)
    return layer


def draw_tracked(draw: ImageDraw.ImageDraw, centre_x: int, centre_y: int, text: str,
                 font: ImageFont.FreeTypeFont, tracking: int, fill):
    widths = []
    for ch in text:
        bb = font.getbbox(ch)
        widths.append(bb[2] - bb[0])
    total = sum(widths) + tracking * max(0, len(text) - 1)
    x = centre_x - total / 2
    asc, desc = font.getmetrics()
    for ch, cw in zip(text, widths):
        bb = font.getbbox(ch)
        draw.text((x - bb[0], centre_y - (asc + desc) / 2), ch, font=font, fill=fill)
        x += cw + tracking


# Canvas presets. WeChat renders at a multiple of the official 900x383 so the
# type stays crisp after the platform downscales it.
CANVAS_PRESETS = {
    "youtube": {"size": (1920, 1080), "label": "YouTube 16:9"},
    "wechat-headline": {"size": (1880, 800), "label": "微信公众号头图 2.35:1"},
    "wechat-square": {"size": (1080, 1080), "label": "公众号次条 / 朋友圈 1:1"},
    "wechat-headline-exact": {"size": (900, 383), "label": "微信公众号头图 900x383（官方原始尺寸）"},
}


# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #
def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("channel", help="channel dir / slug whose style_dna.json to use")
    ap.add_argument("--text", required=True, help="the main headline (keep it to 2-4 CJK chars)")
    ap.add_argument("--top", default="", help="small label above the headline, e.g. 第 24 集")
    ap.add_argument("--bottom", default="", help="small label below the headline")
    ap.add_argument("--bg", help="background image (e.g. the AI-generated blank paper). "
                                "Omit to generate a procedural paper background.")
    ap.add_argument("--out", required=True, help="output PNG path")
    ap.add_argument("--canvas", default="youtube", choices=sorted(CANVAS_PRESETS),
                    help="canvas preset (default: youtube 16:9)")
    ap.add_argument("--width", type=int, help="output width (overrides --canvas)")
    ap.add_argument("--height", type=int)
    ap.add_argument("--font-file")
    ap.add_argument("--font-index", type=int)
    ap.add_argument("--headline-height-pct", type=float,
                    help="headline glyph height as %% of canvas height (default: from DNA)")
    ap.add_argument("--ca-offset", type=int, help="chromatic aberration offset in px (default: from DNA)")
    ap.add_argument("--ca-strength", type=float, default=1.0, help="0-1, fringing intensity")
    ap.add_argument("--top-y-pct", type=float)
    ap.add_argument("--headline-y-pct", type=float)
    ap.add_argument("--bottom-y-pct", type=float)
    ap.add_argument("--no-chromatic", action="store_true")
    args = ap.parse_args()

    ch_dir = resolve_channel_dir(args.channel)
    dna_file = ch_dir / "style_dna.json"
    dna = read_json(dna_file) if dna_file.exists() else {}
    if not dna:
        print(f"[render] note: {dna_file} not found, using built-in defaults")

    head = dna.get("typography", {}).get("headline", {}) or {}
    sec = dna.get("typography", {}).get("secondary", {}) or {}
    layout = dna.get("layout", {}) or {}
    effects = (dna.get("effects", {}) or {}).get("chromatic_aberration", {}) or {}

    canvas = dna.get("format", {}).get("canvas", "")
    m = re.search(r"(\d{3,4})\s*[x×]\s*(\d{3,4})", str(canvas))
    preset = CANVAS_PRESETS[args.canvas]
    default_w, default_h = preset["size"]
    if not m:
        m = re.match(r"(\d+)x(\d+)", f"{default_w}x{default_h}")
    width = args.width or default_w
    height = args.height or (round(width * default_h / default_w) if args.width else default_h)
    print(f"[render] canvas: {preset['label']}  {width}x{height}")

    # ---- background
    if args.bg:
        bg_path = Path(args.bg)
        if not bg_path.exists():
            raise SystemExit(f"error: background not found: {args.bg}")
        bg = cover_crop(Image.open(bg_path), width, height)
        print(f"[render] background: {args.bg} -> {width}x{height}")
    else:
        bg_hex = str(dna.get("palette", {}).get("background_hex") or "")
        if not re.fullmatch(r"#[0-9A-Fa-f]{6}", bg_hex):
            bg_hex = "#F3F4F4"
        bg = procedural_paper(width, height, bg_hex)
        print(f"[render] background: procedural paper {width}x{height} (base {bg_hex})")

    # ---- headline
    cjk = bool(re.search(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]", args.text))
    font_path, font_index, font_label = pick_font(
        args.font_file or head.get("font_file"), args.font_index if args.font_index is not None else head.get("font_index"),
        CJK_FONT_STACK if cjk else LATIN_FONT_STACK,
    )
    h_pct = args.headline_height_pct or head.get("size_pct_of_canvas_height") or 18.0
    target_h = int(height * float(h_pct) / 100)
    size = fit_size(font_path, font_index, args.text, target_h)
    font = load_font(font_path, font_index, size)
    print(f"[render] font: {font_label}  size={size}px  (target glyph height {target_h}px = {h_pct}% of {height})")

    tracking = int(head.get("tracking_px") or 0)
    mask = render_mask(args.text, font, tracking)

    ca_offset = args.ca_offset if args.ca_offset is not None else int(effects.get("offset_px_at_1920") or round(width * 0.004))
    ca_offset = max(0, int(round(ca_offset * width / 1920)))
    if args.no_chromatic or not effects.get("enabled", True):
        ca_offset = 0

    if ca_offset > 0:
        layer = chromatic_text_layer(mask, ca_offset, args.ca_strength)
        print(f"[render] chromatic aberration: offset={ca_offset}px, strength={args.ca_strength}")
    else:
        layer = Image.merge("RGB", (ImageChops.invert(mask),) * 3)

    # place the headline layer centred on the canvas
    x = (width - mask.width) // 2
    y = int(height * (args.headline_y_pct or layout.get("headline_y_pct") or 41.0) / 100 - mask.height / 2)

    canvas_img = bg.copy()
    region = canvas_img.crop((x, y, x + mask.width, y + mask.height))
    canvas_img.paste(ImageChops.multiply(region, layer), (x, y))

    # ---- small labels
    draw = ImageDraw.Draw(canvas_img)
    fill = head.get("fill_hex") or "#111111"
    if not str(fill).startswith("#"):
        fill = "#111111"
    label_font_path, label_index, _ = pick_font(
        sec.get("font_file") or (font_path if cjk else None),
        sec.get("font_index"),
        CJK_FONT_STACK if cjk else LATIN_FONT_STACK,
    )

    for label, y_pct, key in (
        (args.top, args.top_y_pct or sec.get("top_y_pct") or 20.0, "top"),
        (args.bottom, args.bottom_y_pct or sec.get("bottom_y_pct") or 60.0, "bottom"),
    ):
        if not label:
            continue
        l_pct = (sec.get("size_pct_of_canvas_height") or 4.4)
        l_size = fit_size(label_font_path, label_index, label, int(height * float(l_pct) / 100))
        l_font = load_font(label_font_path, label_index, l_size)
        l_track = int(sec.get("tracking_px") or (2 if cjk else 10))
        draw_tracked(draw, width // 2, int(height * float(y_pct) / 100), label, l_font, l_track, fill)
        print(f"[render] {key} label: {label!r}  size={l_size}px  y={y_pct}%")

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    canvas_img.save(out, "PNG")
    print(f"[render] wrote {out}  ({width}x{height})")


if __name__ == "__main__":
    main()
