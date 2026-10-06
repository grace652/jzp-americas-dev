#!/usr/bin/env python3
"""Stage 4/5 - style DNA assembly and the prompt compiler.

Three subcommands:

    template   build style_dna.json, pre-filled with the pixel anchors from
               pixel_stats.json. The agent fills in the qualitative fields.
    guide      render STYLE_GUIDE.md (human-readable) from style_dna.json
    prompts    compile ChatGPT-ready thumbnail prompts for a given video title

The tool NEVER calls an image-generation API. Its entire output is text that
the user pastes into ChatGPT themselves.

Usage:
    python 04_prompt.py template mrbeast
    python 04_prompt.py guide    mrbeast
    python 04_prompt.py prompts  mrbeast --title "..." [--text "DAY 30"] [--variants 3]
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

from _common import PROMPTS_DIR, read_json, resolve_channel_dir, slugify, write_json

# --------------------------------------------------------------------------- #
# shared wording blocks
# --------------------------------------------------------------------------- #
SAFE_BAND = (
    "16:9 widescreen YouTube thumbnail composition "
    "(keep all key elements inside a centred 16:9 safe band)"
)

BASE_CONSTRAINTS = [
    "no watermark",
    "no extra text or captions",
    "no logos or channel branding",
    "no border or frame",
    "no collage panels or split-screen",
    "no duplicated subject",
    "no distorted or melted faces",
    "no visible UI elements or play buttons",
]

DEFAULT_AVOID = [
    "flat vector illustration",
    "minimalist empty space",
    "pastel or desaturated palette",
    "stock-photo blandness",
    "cluttered background with competing detail",
    "small illegible text",
]

CJK_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")

# Added automatically when the on-image text is Chinese.
NO_LATIN_CONSTRAINTS = [
    "no Latin letters, no English words, no roman alphabet characters anywhere in the image",
    "no pinyin, no romanised text",
    "no Japanese kana or Korean hangul",
    "no random or invented glyphs",
]

# Constraints that only make sense when the headline must be Latin.
LATIN_ONLY_AVOID = {"thin elegant serif or script type"}


def is_cjk(text: str | None) -> bool:
    return bool(text and CJK_RE.search(text))


def negative_block(dna: dict, text: str | None = None) -> str:
    avoid = [
        a for a in (dna.get("avoid") or [])
        if a and not (is_cjk(text) and a in LATIN_ONLY_AVOID)
    ]
    extra = NO_LATIN_CONSTRAINTS if is_cjk(text) else []
    return ", ".join(BASE_CONSTRAINTS + avoid + extra)

# Composition hooks used to spread the variants apart while keeping one style.
VARIANT_HOOKS = [
    ("faithful", "follow the channel's dominant layout as closely as possible"),
    ("mirrored", "mirror the dominant layout horizontally"),
    ("centred", "pull the subject to the centre with the text as a top band"),
    ("closeup", "push in to an extreme close-up on the subject's face/expression"),
]


# --------------------------------------------------------------------------- #
# template
# --------------------------------------------------------------------------- #
def build_template(ch_dir: Path) -> dict:
    stats = read_json(ch_dir / "pixel_stats.json")
    manifest = read_json(ch_dir / "refs" / "manifest.json")

    dominant = [
        {
            "hex": c["hex"],
            "role": "unassigned",
            "coverage_pct": c["weighted_coverage_pct"],
            "consistency_pct": c["consistency_pct"],
        }
        for c in stats["consensus_palette"]
    ]
    accents = [
        {
            "hex": c["hex"],
            "role": "accent",
            "coverage_pct": c["weighted_coverage_pct"],
            "consistency_pct": c["consistency_pct"],
        }
        for c in stats["consensus_accent"]
    ]
    agg = stats["aggregate_stats"]

    ages = [p["age_days"] for p in stats["per_image"] if p.get("age_days") is not None]

    return {
        "_instructions": (
            "Fill in every field marked TODO. Pixel-anchored numbers below came from "
            "pixel_stats.json and should not be invented. invariants = features present in "
            ">=60% of the sample; avoid = things this channel never does."
        ),
        "meta": {
            "channel": manifest.get("channel_name"),
            "handle": ch_dir.name,
            "sample_size": stats["sample_size"],
            "date_range": (
                f"last {max(ages):.0f} days" if ages else "unknown"
            ),
            "confidence": "TODO: high | medium | low",
            "confidence_note": "TODO: what limits confidence (small sample, era shift, outliers...)",
        },
        "format": {
            "aspect_ratio": "16:9",
            "canvas": "1280x720 source; deliver 1920x1080",
            "letterbox_cropped": any(
                r.get("letterbox_cropped") for r in manifest.get("references", [])
            ),
            "safe_area_note": (
                "TODO: how close do text/elements run to the edges? "
                f"canvas variants seen: {stats['canvas_variants']}"
            ),
        },
        "palette": {
            "dominant": dominant,
            "accent_small_area": accents,
            "background_hex": (
                "TODO: the colour the background actually reads as "
                f"(highest-coverage candidate: {dominant[0]['hex'] if dominant else 'n/a'})"
            ),
            "background_luminance": agg["border_luma"],
            "palette_archetype": "TODO: e.g. 'saturated warm earth + hard accent' ",
            "grading_note": (
                "TODO (human-facing only - never enters the prompt): describe the grade in words"
            ),
        },
        "contrast": {
            "subject_bg_delta_e": agg["subject_bg_delta_e"],
            "saturation_mean": agg["sat_mean"],
            "pct_pixels_high_sat": agg["pct_pixels_high_sat"],
            "value_mean": agg["val_mean"],
            "global_luma_std": agg["global_luma_std"],
            "colorfulness": agg["colorfulness"],
        },
        "layout": {
            "subject_position": "TODO: e.g. 'left third, eyes on upper-third line'",
            "subject_area_pct": 0,
            "text_zone": "TODO: e.g. 'upper-right, 2 lines, right-aligned'",
            "text_area_pct": 0,
            "split_rule": "TODO: e.g. 'clean vertical split at 45% width'",
            "negative_space_pct": 0,
            "headline_y_pct": 0,
        },
        "effects": {
            "chromatic_aberration": {
                "enabled": False,
                "offset_px_at_1920": 0,
                "note": "TODO: e.g. 'red fringe on the left of strokes, cyan on the right'",
            }
        },
        "subject": {
            "type": "TODO",
            "framing": "TODO",
            "gaze": "TODO",
            "expression": "TODO",
            "emotion_intensity": 0,
            "cutout_style": "TODO: e.g. 'hard-edged photographic cut-out with 4px white rim'",
            "outline": {"color": "TODO", "width_px": 0},
        },
        "typography": {
            "headline": {
                "case": "TODO: UPPERCASE / Title Case / lowercase",
                "max_words": 0,
                "font_class": "TODO: e.g. 'heavy condensed grotesque, slightly italic'",
                "font_class_zh": "TODO: 中文字体描述，用于中文文字指令块，例如「粗宋体（明朝体），横细竖粗，笔画对比强烈」",
                "weight": "TODO",
                "fill_hex": "TODO: the actual text fill colour",
                "stroke": {"color": "TODO", "width_px": 0},
                "shadow": {"type": "TODO", "offset": "TODO"},
                "position": "TODO",
                "lines": 0,
                "size_pct_of_canvas_height": 0,
                "tracking_px": 0,
                "font_file": "TODO: absolute path for the local renderer (06_render_cover.py)",
                "font_index": 0,
            },
            "secondary": {
                "font_file": "TODO",
                "font_index": 0,
                "size_pct_of_canvas_height": 0,
                "tracking_px": 0,
                "top_y_pct": 0,
                "bottom_y_pct": 0,
            },
            "badge": {},
        },
        "lighting": {"key": "TODO", "direction": "TODO", "color_temp": "TODO", "glow": "TODO"},
        "background": {"type": "TODO", "depth_of_field": "TODO", "elements": []},
        "motifs": {"recurring": [], "consistency_pct": 0},
        "grade": {"lut_feel": "TODO", "grain": "TODO", "vignette": "TODO"},
        "signature_move": "TODO: one sentence - the single most recognisable device",
        "invariants": [],
        "avoid": list(DEFAULT_AVOID),
        "prompt_anchor_paragraph": "TODO: reusable style-anchoring paragraph",
        "per_image": [
            {
                "video_id": p["video_id"],
                "title": p["title"],
                "views": p["views"],
                "bucket": p["bucket"],
                "deviation_score": p["deviation_score"],
                "is_outlier": p["video_id"] in stats["outlier_video_ids"],
                "dominant_hex": p["palette"][0]["hex"],
                "accent_hex": p["accent"]["hex"],
                "notes": "TODO: what is distinctive about this one",
            }
            for p in stats["per_image"]
        ],
        "_pixel_evidence": {
            "era_check": stats["era_check"],
            "outlier_video_ids": stats["outlier_video_ids"],
            "quality_tiers_used": stats["quality_tiers_used"],
            "method_notes": stats["method_notes"],
        },
    }


# --------------------------------------------------------------------------- #
# prompt assembly
# --------------------------------------------------------------------------- #
# Matches only a value that is *entirely* a placeholder - so "none" is dropped but
# "none - flat, even, shadowless (printed page)" survives as real content.
_PLACEHOLDER = re.compile(r"^\s*(todo\b.*|n/?a|none|nil|null|-|—|n/a.*)\s*$", re.I)


def val(x) -> str | None:
    """Return a usable string, or None for placeholders / empty / 'none' values.

    Without this, DNA fields that legitimately hold 'n/a' (a typographic poster
    has no subject, no lighting) leak into the prompt as 'n/a, n/a, n/a'.
    """
    if x is None:
        return None
    s = str(x).strip()
    if not s or _PLACEHOLDER.match(s):
        return None
    return s


def join_vals(*items) -> str:
    return ", ".join(v for v in (val(i) for i in items) if v)


def anchor(dna: dict) -> str:
    a = val(dna.get("prompt_anchor_paragraph"))
    if a:
        return a
    sig = val(dna.get("signature_move")) or "clean, high-contrast thumbnail design"
    pal = ", ".join(
        f"{c['hex']} ({c['role']})" for c in dna.get("palette", {}).get("dominant", [])[:4]
    )
    return (
        f"Photorealistic YouTube thumbnail in the house style of this channel. "
        f"Signature device: {sig}. Palette anchored on {pal}. "
        f"Very high contrast, punchy saturation, crisp cut-out subject against a "
        f"readable background."
    )


def typography_line(dna: dict) -> str:
    t = dna.get("typography", {}).get("headline", {})
    stroke = t.get("stroke") or {}
    shadow = t.get("shadow") or {}

    case = val(t.get("case"))
    if case and "for chinese" in case.lower():
        case = None  # a note, not a value

    stroke_txt = None
    if val(stroke.get("color")):
        w = stroke.get("width_px") or 0
        stroke_txt = f"{w}px {stroke['color']} stroke" if w else f"{stroke['color']} stroke"
    shadow_txt = None
    if val(shadow.get("type")):
        shadow_txt = str(shadow["type"])
        if not shadow_txt.lower().endswith("shadow"):
            shadow_txt += " shadow"
        shadow_txt = re.sub(r"\b(\w+)\s+\1\b", r"\1", shadow_txt, flags=re.I)

    lines = val(t.get("lines"))
    size = val(t.get("size_pct_of_canvas_height"))
    try:
        n_lines = int(lines) if lines else 0
    except (TypeError, ValueError):
        n_lines = 0

    out = join_vals(
        t.get("font_class"),
        case,
        f"fill {t['fill_hex']}" if val(t.get("fill_hex")) else None,
        stroke_txt,
        shadow_txt,
        f"positioned {val(t.get('position'))}" if val(t.get("position")) else None,
        f"{n_lines} line{'s' if n_lines != 1 else ''}" if n_lines else None,
        f"about {size}% of canvas height" if size else None,
    )
    return out or "heavy bold uppercase sans-serif, white fill, black stroke"


def layout_line(dna: dict, hook: str) -> str:
    lay = dna.get("layout", {})
    pos = val(lay.get("subject_position"))
    zone = val(lay.get("text_zone"))

    if hook == "mirrored":
        def flip(text: str) -> str:
            out = re.sub(r"\bleft\b", "\x00", text, flags=re.I)
            out = re.sub(r"\bright\b", "left", out, flags=re.I)
            return out.replace("\x00", "right")

        if pos:
            pos = flip(pos)
        if zone:
            zone = flip(zone)
    elif hook == "centred":
        pos, zone = "the centre, filling the middle 60% of the frame", "a band across the top"
    elif hook == "closeup":
        pos, zone = "an extreme close-up filling the left half", "the right half, 2 short lines"

    bits = []
    if pos:
        # a phrase that already reads as a full clause shouldn't get "subject occupies"
        if re.match(r"^(there\s+is|there\s+are|no\b|none\b|the\s+type|everything)", pos, re.I):
            bits.append(pos)
        else:
            bits.append(f"subject occupies {pos}")
    if zone:
        bits.append(f"text occupies {zone}")
    rule = val(lay.get("split_rule"))
    if rule and not re.match(r"^none\b", rule, re.I):
        bits.append(rule)
    return ", ".join(bits) or "centred, generous margins"


def subject_line(dna: dict, subject_override: str | None) -> str | None:
    s = dna.get("subject", {})
    parts = [subject_override] if subject_override else []
    parts += [s.get(k) for k in ("type", "framing", "gaze", "expression", "cutout_style")]
    out = join_vals(*parts)
    return out or None


def palette_line(dna: dict) -> str:
    """Colour anchors for the prompt. Human-facing commentary (palette.grading_note)
    is deliberately excluded - it belongs in the style guide, not the prompt."""
    pal = dna.get("palette", {})
    head = dna.get("typography", {}).get("headline", {})

    bg = val(pal.get("background_hex"))
    if not bg:
        dom = pal.get("dominant") or []
        bg = next(
            (c["hex"] for c in dom if c.get("role") == "background"),
            dom[0]["hex"] if dom else None,
        )

    txt = val(head.get("fill_hex"))
    accents = pal.get("accent_small_area") or []
    acc = accents[0]["hex"] if accents else None
    lut = val(dna.get("grade", {}).get("lut_feel"))

    return join_vals(
        f"background {bg}" if bg else None,
        f"headline {txt}" if txt else None,
        f"accent {acc}" if acc else None,
        lut.split(" - ")[0] if lut else None,
    ) or "high-contrast saturated palette"


def lighting_line(dna: dict) -> str:
    li = dna.get("lighting", {})
    return join_vals(li.get("key"), li.get("direction"), li.get("color_temp"), li.get("glow")) \
        or "hard key light, strong rim separation, warm colour temperature"


def background_line(dna: dict) -> str:
    b = dna.get("background", {})
    bits = join_vals(b.get("type"), b.get("depth_of_field"))
    els = [e for e in (b.get("elements") or []) if val(e)]
    if els:
        bits = (bits + ", " if bits else "") + "background elements: " + ", ".join(els)
    return bits or "environmental background matching the video's subject"


def motif_line(dna: dict) -> str:
    motifs = [m for m in (dna.get("motifs", {}).get("recurring") or []) if val(m)]
    return ", ".join(motifs) if motifs else ""


def cjk_text_directive(text: str, dna: dict, with_text: bool) -> list[str]:
    """Chinese-language text directive for GPT Image.

    Follows the wording pattern that works best for GPT Image text rendering:
    state the copy verbatim (逐字呈现), quote it, then pin down language, font
    temperament, size hierarchy, position and occurrence count, demand
    legibility, and explicitly ban the known failure modes.
    """
    t = dna.get("typography", {}).get("headline", {})
    sec = dna.get("typography", {}).get("secondary", {}) or {}
    n_chars = len(re.findall(CJK_RE, text))
    size = t.get("size_pct_of_canvas_height") or 20
    fill = val(t.get("fill_hex")) or "#111111"

    # Prefer an explicit Chinese description so the directive reads naturally.
    # Never splice an English font_class into a Chinese sentence - a stray "宋体"
    # inside an otherwise English sentence is not enough to qualify.
    font_class = val(t.get("font_class_zh"))
    if not font_class:
        en = val(t.get("font_class")) or ""
        cjk_chars = len(re.findall(CJK_RE, en))
        if en and cjk_chars >= len(en) * 0.5:
            font_class = en
        else:
            font_class = "粗宋体（明朝体），横细竖粗，笔画对比强烈，字形端正有力"

    if not with_text:
        return [
            "画面中不要出现任何文字：不要汉字、不要字母、不要数字、不要符号。",
            "文字区域保持干净空白，便于后期叠加文字。",
        ]

    lines = [
        "必须包含以下文字，逐字呈现：",
        f'  "{text}"',
        "",
        "文字要求：",
        f"  - 语言：简体中文。只使用规范简体汉字，共 {n_chars} 个字。",
        f"  - 字体气质：{font_class}。",
        f"  - 字号：文字高度约占画面高度的 {size}%，是画面中最大的元素。",
        f"  - 颜色：{fill}，纯色填充，不要描边，不要投影。",
        "  - 位置：画面正中央，水平居中。",
        "  - 字距：均匀干净，不要挤压。",
        "  - 文案只出现一次，不要重复，不要多加任何其他文字。",
        "  - 每个字都必须是笔画完整、正确无误的简体汉字：不得缺笔，",
        "    不得写成繁体字、日文汉字或形近字，不得混入英文字母或拼音。",
        "  - 文字必须清晰可读，边缘锐利，不要模糊、不要变形、不要艺术化扭曲。",
    ]
    top = val(sec.get("top_y_pct"))
    if top:
        lines.append(
            f"  - 若需要一行小字标识，放在大字正上方（约画面高度 {top}% 处），"
            "同样必须是简体中文；若无法正确书写，宁可不写这一行。"
        )
    return lines


def assemble(dna: dict, text: str | None, subject: str | None, hook: str,
             with_text: bool = True, text_renderer: str = "gpt",
             safe_band: str | None = None) -> str:
    lines = [(safe_band or SAFE_BAND) + ".", ""]
    lines.append(f"Style: {anchor(dna)}")
    lines.append(f"Scene: {background_line(dna)}")
    subj = subject_line(dna, subject)
    if subj:
        lines.append(f"Subject: {subj}")
    lit = lighting_line(dna)
    if lit:
        lines.append(f"Lighting: {lit}")
    lines.append(f"Colour: {palette_line(dna)}")
    lines.append(f"Layout: {layout_line(dna, hook)}")
    if motif_line(dna):
        lines.append(f"Recurring motifs: {motif_line(dna)}")

    lines.append("")
    if is_cjk(text):
        # The Chinese directive block, written in Chinese: this is the part that
        # decides whether the glyphs come out right.
        lines += cjk_text_directive(text or "", dna, with_text)
    elif with_text and text:
        lines.append(f'Text: render exactly "{text}" - {typography_line(dna)}.')
        lines.append(f'The only text in the image is "{text}".')
    else:
        lines.append(
            "Text: NO text of any kind - no letters, no Chinese characters, no numbers. "
            "Leave the designated text area clean and uncluttered so text can be added later."
        )

    lines.append("")
    lines.append(f"Constraints: {negative_block(dna, text)}.")
    if is_cjk(text):
        lines.append(
            "补充禁止项：不要随机文字，不要无意义占位文字，不要乱码字符，"
            "不要水印，不要 logo，不要额外文字，不要重复文案。"
        )
    return "\n".join(lines)


def suggest_text(title: str) -> str:
    """A starting suggestion only - the user should override it."""
    # Chinese titles: strip the episode prefix and keep the first short phrase.
    if is_cjk(title):
        stripped = re.sub(r"^\s*(EP|Ep|ep)\s*\.?\s*\d+\s*[.、:：]?\s*", "", title).strip()
        stripped = re.sub(r"[「」『』《》〈〉【】（）()\[\]\"'“”‘’]", "", stripped)
        head = re.split(r"[，,。.？！?!；;：:、\s]+", stripped)[0]
        return head[:4] if head else stripped[:4]

    money = re.search(r"\$\s?([\d,.]+)\s*([KMB]?)", title, re.I)
    if money:
        return f"${money.group(1)}{(money.group(2) or '').upper()}".upper()
    days = re.search(r"(\d+)\s*(?:days?|hours?|minutes?|years?)", title, re.I)
    if days:
        unit = re.search(r"days?|hours?|minutes?|years?", title, re.I).group(0).upper()
        return f"{unit.rstrip('S')} {days.group(1)}"
    words = [w for w in re.findall(r"[A-Za-z0-9$%#]+", title) if len(w) > 2][:3]
    return " ".join(words).upper() if words else "WATCH THIS"


def build_prompts(dna: dict, title: str, text: str, subject: str | None,
                  variants: int, renderer_cmd: str | None = None,
                  text_renderer: str = "gpt", canvas: str = "youtube") -> str:
    hooks = [VARIANT_HOOKS[i % len(VARIANT_HOOKS)] for i in range(variants)]
    suggested = suggest_text(title)
    cjk = is_cjk(text)
    preset = CANVAS_PRESETS.get(canvas) or CANVAS_PRESETS["youtube"]
    safe_band = preset["safe_band"]

    usage = [
        "1. **优先用 Mode B**：在 ChatGPT 里**同时上传 1–2 张该频道的真实封面**，再粘贴 Mode B 的 prompt。",
        "   纯文字描述只能做到「同类风格」，做不到「同一频道」——上传参考图是保真度最高的路径。",
        f"2. 目标画布：**{preset['label']}**。{preset['note']}",
    ]
    if cjk:
        usage += [
            "3. **中文文字由 GPT 直接生成。** 文字指令块用中文写，并按「逐字呈现」的写法组织：",
            "   给出原文 → 锁定语言/字体/字号/位置/出现次数 → 要求笔画完整 → 明确禁止随机文字。",
            "4. **出图后必须逐字核对**（见下方「验收清单」）。汉字常见错误：缺笔、写成繁体或日文汉字、",
            "   形近字替换、多出无意义文字。**只要有错就直接用修复 prompt 重试**，不要将就。",
            "5. 若同一个字连续 3 次都写错，再考虑把字数减到 2 个字，或改用本地叠字兜底。",
            "6. 每轮迭代都**重复完整的文字指令块**，并说明「只改 X，其余保持不变」，否则风格会漂移。",
        ]
    else:
        usage += [
            "3. **画面文字是最容易出错的一环**。若拼写错误，用文末的「修复 prompt」重试。",
            "4. 每轮迭代都**重复完整的 Text 段落**，并说明「只改 X，其余保持不变」，否则风格会漂移。",
        ]

    md = [
        f"# 封面 Prompt 包 — {dna.get('meta', {}).get('channel') or dna.get('meta', {}).get('handle')}",
        "",
        f"- **视频标题**：{title}",
        f"- **画面文字**：`{text}`" + (" （自动建议，建议你手动改写）" if text == suggested else ""),
        f"- **文字语言**：{'简体中文（已强制：画面内不得出现任何英文/Latin 字母）' if cjk else '拉丁字母'}",
        f"- **文字生成方式**：{'GPT 直接生成' if cjk else 'GPT 直接生成'}",
        f"- **风格签名手法**：{dna.get('signature_move', '')}",
        f"- **样本量**：{dna.get('meta', {}).get('sample_size')}　"
        f"**置信度**：{dna.get('meta', {}).get('confidence')}",
        "",
        "---",
        "",
        "## 使用说明（先读这一段）",
        "",
        *usage,
        "",
        "---",
        "",
        "## Mode B — 带参考图（推荐）",
        "",
        "**做法**：在 ChatGPT 上传 1–2 张该频道的真实封面 → 粘贴以下 prompt。",
        "",
    ]

    for i, (hook_name, hook_desc) in enumerate(hooks, 1):
        body = assemble(dna, text, subject, hook_name, with_text=True,
                        text_renderer=text_renderer, safe_band=safe_band)
        md += [
            f"### B{i}. 变体 {i} — {hook_desc}",
            "",
            "```text",
            "Image 1 is a STYLE REFERENCE only. Do not copy its subject, its people, "
            "or its text. Create a completely new YouTube thumbnail that looks like it "
            "came from the same channel and the same designer.",
            "",
            body,
            "```",
            "",
        ]

    md += [
        "---",
        "",
        "## Mode A — 纯文本（无参考图）",
        "",
    ]
    for i, (hook_name, hook_desc) in enumerate(hooks, 1):
        body = assemble(dna, text, subject, hook_name, with_text=True,
                        text_renderer=text_renderer, safe_band=safe_band)
        md += [
            f"### A{i}. 变体 {i} — {hook_desc}",
            "",
            "```text",
            body,
            "```",
            "",
        ]

    md += [
        "---",
        "",
        "## 兜底 — 无字底图 prompt",
        "",
        "若 ChatGPT 反复写错画面文字，用它生成干净底图，再按下面的规格自己压字。",
        "",
        "```text",
        assemble(dna, None, subject, "faithful", with_text=False, safe_band=safe_band),
        "```",
        "",
        "### 文字叠加规格",
        "",
        f"| 项 | 值 |",
        f"|---|---|",
        f"| 文字内容 | `{text}` |",
        f"| 语言 | {'简体中文（不得出现英文）' if cjk else '拉丁字母'} |",
        f"| 字体 | {dna.get('typography', {}).get('headline', {}).get('font_class', '—')} |",
        f"| 大小写 | {dna.get('typography', {}).get('headline', {}).get('case', '—')} |",
        f"| 填充色 | {dna.get('typography', {}).get('headline', {}).get('fill_hex', '—')} |",
        f"| 描边 | {(dna.get('typography', {}).get('headline', {}).get('stroke') or {}).get('color', '—')} "
        f"{(dna.get('typography', {}).get('headline', {}).get('stroke') or {}).get('width_px', '')}px |",
        f"| 位置 | {dna.get('typography', {}).get('headline', {}).get('position', '—')} |",
        f"| 占画布高度 | {dna.get('typography', {}).get('headline', {}).get('size_pct_of_canvas_height', '—')}% |",
        f"| 背景色参考 | {palette_line(dna)} |",
    ]
    if cjk:
        md += [
            "",
            "**中文可用字体（本机已安装，任选）**",
            "",
            "| 字体 | 文件 | 风格 |",
            "|---|---|---|",
            "| Songti SC Black | `/System/Library/Fonts/Supplemental/Songti.ttc` (index 0) | 宋体粗黑，与参考封面最接近 |",
            "| Songti SC Bold | 同上 (index 1) | 略轻 |",
            "| Hiragino Sans GB W6 | `/System/Library/Fonts/Hiragino Sans GB.ttc` (index 2) | 黑体，无衬线 |",
            "| Heiti SC Medium | `/System/Library/Fonts/STHeiti Medium.ttc` (index 1) | 黑体 |",
            "",
            "> ⚠️ 用 `Songti TC` / `Heiti TC` 会输出**繁体字形**，务必选带 `SC` 的那个 index。",
        ]
    md += [
        "",
        f"推荐工具：Keynote / Canva / Photoshop" + ("，或直接用本项目的本地渲染器（见下）" if cjk else "") + "。"
        + ("宋体类字体在 Keynote 里叫「宋体-简 粗体」。" if cjk else "描边用「外侧描边」而非投影。"),
        "",
    ]
    if cjk:
        md += [
            "---",
            "",
            "## 验收清单（出图后逐条核对，中文必查）",
            "",
            f"对照你要的文字：**{text}**（{len(re.findall(CJK_RE, text))} 个字）",
            "",
            "| # | 检查项 | 不合格的处理 |",
            "|---|---|---|",
            "| 1 | **字数对不对**——有没有多字、少字、重复 | 用修复 prompt 重试 |",
            "| 2 | **每个字是否笔画完整**——有没有缺笔、糊成一团 | 重试 |",
            "| 3 | **有没有写成繁体字或日文汉字** | 重试（这是最常见的错） |",
            "| 4 | **有没有形近字替换**（如「未/末」「己/已」「戌/戍」） | 重试 |",
            "| 5 | **画面里有没有多出别的文字**——英文、拼音、乱码、水印 | 重试 |",
            "| 6 | 字体是不是宋体（不是黑体/圆体/手写体） | 用修复 prompt 指定字体 |",
            "| 7 | 位置是不是居中、字号是不是最大元素 | 用修复 prompt 指定位置 |",
            "| 8 | 背景是不是空白纸（没有多出人物、道具、装饰） | 重试 |",
            "",
            "**「修复 prompt」的正确用法**：一次只改一个问题，其余全部列入 preserve 清单。",
            "同时改两处会让模型把两处都改坏。",
            "",
            "---",
            "",
            "## 备选路线：本地精确叠字",
            "",
            "如果同一个字连续 3 次都写错，或者你要的字超过 4 个，再走这条路：",
            "**让 AI 只出无字背景，文字用本地渲染器叠上去**——字形 100% 正确、可复现。",
            "",
            "```bash",
            "# 1. 用上面的「无字底图 prompt」在 ChatGPT 生成背景，存成 bg.png",
            "# 2. 本地叠字（自动应用字体/位置/色差规格）",
            (renderer_cmd or
             "$PY <skill>/scripts/06_render_cover.py <channel> --bg bg.png "
             f'--text "{text}" --top "<顶部小字>" --out cover.png'),
            "```",
            "",
        ]
    md += [
        "---",
        "",
        "## 修复 prompt（出图跑偏时用）",
        "",
        "先说明**只改什么**，再列出**必须保持不变**的清单。",
        "",
        "```text",
        "Keep this image exactly as it is. Change ONLY the following:",
        "  - <在这里写你要改的那一处，例如：the headline text is misspelled>",
        "",
        "Preserve everything else unchanged:",
        f"  - the composition and layout ({layout_line(dna, 'faithful')})",
        f"  - the lighting ({lighting_line(dna)})",
        f"  - the colour grade ({palette_line(dna)})",
        f"  - the subject's pose, framing and expression",
        f"  - the overall level of contrast and saturation",
        "",
    ]
    if cjk:
        md += [
            f'The only text in the image must be exactly the Simplified Chinese text "{text}" '
            "- every character correctly formed, in Simplified form, nothing else added.",
            "Do not render any English words or Latin letters.",
        ]
    else:
        md += [
            f'The only text in the image must be exactly "{text}" - spelled correctly, '
            "nothing else added.",
        ]
    md += [
        "```",
        "",
        "---",
        "",
        "## 硬约束汇总（每个 prompt 都已内联）",
        "",
        "**必须出现（invariants）**",
        "",
    ]
    for inv in dna.get("invariants") or ["（尚未填写）"]:
        md.append(f"- {inv}")
    md += ["", "**必须避免（avoid）**", ""]
    for av in (dna.get("avoid") or []) + BASE_CONSTRAINTS + (NO_LATIN_CONSTRAINTS if cjk else []):
        md.append(f"- {av}")
    md += [
        "",
        "> 提示：不要用 Stable Diffusion 语法（`(word:1.5)`、tag 堆、`8K masterpiece`），",
        "> 这些对 GPT-image 类模型无效甚至有害。用自然语言句子描述。",
        "",
    ]
    return "\n".join(md)


# --------------------------------------------------------------------------- #
# guide
# --------------------------------------------------------------------------- #
def build_guide(dna: dict) -> str:
    m, f, p = dna.get("meta", {}), dna.get("format", {}), dna.get("palette", {})
    md = [
        f"# 风格指南 — {m.get('channel') or m.get('handle')}",
        "",
        f"- 样本：{m.get('sample_size')} 张（{m.get('date_range')}）",
        f"- 置信度：**{m.get('confidence')}** — {m.get('confidence_note', '')}",
        f"- 画布：{f.get('canvas')}　宽高比：{f.get('aspect_ratio')}",
        "",
        "## 一句话签名手法",
        "",
        f"> {dna.get('signature_move', '')}",
        "",
        "## 风格锚定段落（可复用）",
        "",
        "```text",
        anchor(dna),
        "```",
        "",
        "## 调色板（像素实测）",
        "",
        "| 色值 | 角色 | 加权占比 | 出现在 |",
        "|---|---|---|---|",
    ]
    for c in p.get("dominant", []):
        md.append(
            f"| `{c['hex']}` | {c.get('role', '—')} | {c.get('coverage_pct', '—')}% | "
            f"{c.get('consistency_pct', '—')}% 的样本 |"
        )
    md += ["", "**强调色（小面积高饱和）**", ""]
    for c in p.get("accent_small_area", []):
        md.append(f"- `{c['hex']}` — 占比 {c.get('coverage_pct', '—')}%")
    md += [
        "",
        f"调色板原型：{p.get('palette_archetype', '—')}",
        f"调色说明：{p.get('grading_note', '—')}",
        "",
        "## 实测对比度与饱和度",
        "",
        "| 指标 | 值 | 含义 |",
        "|---|---|---|",
        f"| 主体/背景 ΔE | {dna.get('contrast', {}).get('subject_bg_delta_e')} | 越大主体越跳脱 |",
        f"| 平均饱和度 | {dna.get('contrast', {}).get('saturation_mean')} | 0–1 |",
        f"| 高饱和像素占比 | {dna.get('contrast', {}).get('pct_pixels_high_sat')}% | 色彩浓度 |",
        f"| 亮度标准差 | {dna.get('contrast', {}).get('global_luma_std')} | 全局对比度 |",
        f"| 色彩丰富度 | {dna.get('contrast', {}).get('colorfulness')} | Hasler–Süsstrunk 指标 |",
        "",
        "## 版面",
        "",
        f"- 主体位置：{dna.get('layout', {}).get('subject_position')}",
        f"- 文字区：{dna.get('layout', {}).get('text_zone')}",
        f"- 分割规则：{dna.get('layout', {}).get('split_rule')}",
        f"- 留白比例：{dna.get('layout', {}).get('negative_space_pct')}%",
        "",
        "## 主体处理",
        "",
        f"- 类型：{dna.get('subject', {}).get('type')}",
        f"- 取景：{dna.get('subject', {}).get('framing')}",
        f"- 视线：{dna.get('subject', {}).get('gaze')}",
        f"- 表情：{dna.get('subject', {}).get('expression')}（强度 {dna.get('subject', {}).get('emotion_intensity')}/5）",
        f"- 抠像：{dna.get('subject', {}).get('cutout_style')}",
        "",
        "## 文字排版",
        "",
        f"- 字体：{dna.get('typography', {}).get('headline', {}).get('font_class')}",
        f"- 大小写：{dna.get('typography', {}).get('headline', {}).get('case')}",
        f"- 填充：{dna.get('typography', {}).get('headline', {}).get('fill_hex')}",
        f"- 描边：{(dna.get('typography', {}).get('headline', {}).get('stroke') or {}).get('color')} "
        f"{(dna.get('typography', {}).get('headline', {}).get('stroke') or {}).get('width_px')}px",
        f"- 位置：{dna.get('typography', {}).get('headline', {}).get('position')}",
        f"- 行数：{dna.get('typography', {}).get('headline', {}).get('lines')}",
        f"- 占画布高度：{dna.get('typography', {}).get('headline', {}).get('size_pct_of_canvas_height')}%",
        "",
        "## 光线与影调",
        "",
        f"- 主光：{dna.get('lighting', {}).get('key')}",
        f"- 方向：{dna.get('lighting', {}).get('direction')}",
        f"- 色温：{dna.get('lighting', {}).get('color_temp')}",
        f"- 调色：{dna.get('grade', {}).get('lut_feel')}",
        "",
        "## 背景",
        "",
        f"- 类型：{dna.get('background', {}).get('type')}",
        f"- 景深：{dna.get('background', {}).get('depth_of_field')}",
        f"- 元素：{', '.join(dna.get('background', {}).get('elements') or []) or '—'}",
        "",
        "## 反复出现的母题",
        "",
    ]
    for mo in dna.get("motifs", {}).get("recurring") or ["—"]:
        md.append(f"- {mo}")
    md += ["", "## 必须出现 / 必须避免", "", "**必须出现（≥60% 样本）**", ""]
    for inv in dna.get("invariants") or ["—"]:
        md.append(f"- {inv}")
    md += ["", "**必须避免**", ""]
    for av in dna.get("avoid") or ["—"]:
        md.append(f"- {av}")
    md += ["", "## 逐图记录", "", "| # | 视频 | 播放量 | 主色 | 偏离度 | 备注 |", "|---|---|---|---|---|---|"]
    for i, pimg in enumerate(dna.get("per_image", [])):
        flag = " ⚠️异常" if pimg.get("is_outlier") else ""
        md.append(
            f"| {i} | {pimg.get('title', '')[:40]} | {pimg.get('views') or '—'} | "
            f"`{pimg.get('dominant_hex')}` | {pimg.get('deviation_score')}{flag} | "
            f"{(pimg.get('notes') or '')[:60]} |"
        )
    md += ["", "---", "", "## 像素证据（原始测量）", ""]
    ev = dna.get("_pixel_evidence", {})
    era = ev.get("era_check", {})
    if era.get("compared"):
        md += [
            f"- 时代检测：前段平均饱和度 {era['older_half_mean_sat']} → 后段 {era['newer_half_mean_sat']}"
            f"（位移 {era['sat_shift']}）",
            f"- 是否检出风格迁移：**{era['style_shift_detected']}**",
        ]
    md.append(f"- 被标记为异常的样本：{ev.get('outlier_video_ids')}")
    md.append(f"- 缩略图质量档位：{ev.get('quality_tiers_used')}")
    md += ["", "方法说明：", ""]
    for note in ev.get("method_notes", []):
        md.append(f"- {note}")
    md += [
        "",
        "> 注意：像素统计给的是**精确锚点**，不是风格本身。",
        "> 真正的风格判断来自对参考图的视觉解读（Stage 3）。",
        "",
    ]
    return "\n".join(md)


# --------------------------------------------------------------------------- #
# canvas presets
# --------------------------------------------------------------------------- #
CANVAS_PRESETS = {
    "youtube": {
        "label": "YouTube 16:9",
        "ratio": 16 / 9,
        "safe_band": (
            "16:9 widescreen composition "
            "(keep all key elements inside a centred 16:9 safe band)"
        ),
        "note": "ChatGPT 出图 1536x1024（3:2），裁切成 16:9。",
    },
    "wechat-headline": {
        "label": "微信公众号头图 2.35:1",
        "ratio": 900 / 383,
        "safe_band": (
            "2.35:1 ultra-wide banner composition, 900x383 "
            "(keep ALL text and key elements inside the centre of the frame, "
            "clear of the bottom-left and bottom-right corners)"
        ),
        "note": (
            "公众号头图 2.35:1（900×383）。信息流里**左下角和右下角会被标题文字盖住**，"
            "所以文字一律放中间偏上，不要贴底。"
        ),
    },
    "wechat-square": {
        "label": "公众号次条 / 朋友圈 1:1",
        "ratio": 1.0,
        "safe_band": (
            "1:1 square composition (keep all key elements inside a centred square safe band)"
        ),
        "note": "次条缩略图只有 200×200，**字要大、元素要少、对比要强**，别堆细节。",
    },
}


def safe_band_for(canvas: str) -> str:
    preset = CANVAS_PRESETS.get(canvas) or CANVAS_PRESETS["youtube"]
    return preset["safe_band"]


# --------------------------------------------------------------------------- #
# cli
# --------------------------------------------------------------------------- #
def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_t = sub.add_parser("template", help="build style_dna.json skeleton with pixel anchors")
    p_t.add_argument("channel")
    p_t.add_argument("--force", action="store_true", help="overwrite an existing style_dna.json")

    p_g = sub.add_parser("guide", help="render STYLE_GUIDE.md from style_dna.json")
    p_g.add_argument("channel")

    p_p = sub.add_parser("prompts", help="compile ChatGPT-ready prompts")
    p_p.add_argument("channel")
    p_p.add_argument("--title", required=True, help="the new video's title")
    p_p.add_argument("--text", help="exact on-image text (default: auto suggestion)")
    p_p.add_argument("--subject", help="describe the subject you want")
    p_p.add_argument("--variants", type=int, default=3)
    p_p.add_argument(
        "--canvas", default="youtube", choices=sorted(CANVAS_PRESETS),
        help="target canvas preset (default: youtube 16:9)",
    )
    p_p.add_argument(
        "--text-renderer", default="gpt", choices=["gpt", "local"],
        help="gpt = let the model render the text (default); local = plan for 06_render_cover.py",
    )

    args = ap.parse_args()
    ch_dir = resolve_channel_dir(args.channel)

    if args.cmd == "template":
        out = ch_dir / "style_dna.json"
        if out.exists() and not args.force:
            raise SystemExit(f"error: {out} already exists (use --force to overwrite)")
        write_json(out, build_template(ch_dir))
        print(f"[dna] wrote {out}")
        print("[dna] next: fill in every field marked TODO, then run `guide` and `prompts`")
        return

    dna_file = ch_dir / "style_dna.json"
    if not dna_file.exists():
        raise SystemExit(f"error: {dna_file} not found - run `04_prompt.py template {args.channel}` first")
    dna = read_json(dna_file)

    if args.cmd == "guide":
        out = ch_dir / "STYLE_GUIDE.md"
        out.write_text(build_guide(dna), encoding="utf-8")
        print(f"[guide] wrote {out}")
        return

    text = args.text or suggest_text(args.title)
    skill_scripts = Path(__file__).resolve().parent
    renderer = (
        f'PY=/Users/eric/.workbuddy-ai/binaries/python/envs/default/bin/python\n'
        f'$PY "{skill_scripts / "06_render_cover.py"}" {ch_dir.name} --bg bg.png '
        f'--text "{text}" --top "<顶部小字>" --out cover.png'
    )
    md = build_prompts(dna, args.title, text, args.subject, args.variants, renderer,
                       text_renderer=args.text_renderer, canvas=args.canvas)
    PROMPTS_DIR.mkdir(parents=True, exist_ok=True)
    out = PROMPTS_DIR / f"{ch_dir.name}_{slugify(args.title)}.md"
    out.write_text(md, encoding="utf-8")
    print(f"[prompts] wrote {out}")
    print(f"[prompts] on-image text used: {text!r}")
    print(f"[prompts] variants: {args.variants} x (Mode A + Mode B), plus textless fallback and repair prompt")


if __name__ == "__main__":
    main()
