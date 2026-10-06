---
name: yt-thumbnail-distill
description: Distil the visual style of a YouTube channel's thumbnails into a reusable "style DNA", then compile ChatGPT-ready image-generation prompts that reproduce that style for a new video. Use when the user wants to analyse, replicate, clone, or "distil" a channel's thumbnail/cover style, or asks for a thumbnail prompt based on a reference channel. The pipeline measures real pixel statistics AND performs a visual read of the reference thumbnails.
description_zh: "蒸馏 YouTube 频道封面风格，产出可直接粘贴进 ChatGPT 的封面出图 prompt"
description_en: "Distil a YouTube channel's thumbnail style into reusable image prompts"
agent_created: true
---

# YouTube Thumbnail Style Distillation

Turn "I like this channel's thumbnails" into a reusable style spec plus
copy-paste prompts the user can take to ChatGPT.

## Hard constraints (do not violate)

1. **NEVER call an image-generation API or tool.** The entire deliverable is
   *text*. The user generates images themselves in ChatGPT. No exceptions —
   this is the whole point of the skill.
2. **Never invent pixel measurements.** Every hex code, coverage percentage and
   contrast number must come from `pixel_stats.json`.
3. **Stage 3 is your job, not a script's.** You are multimodal: you must
   actually look at the contact sheet and the individual thumbnails. The
   numeric stats are anchors, not the style itself.

## Scripts

All scripts live in `$SKILL_DIR/scripts/`. Run them from the directory where
you want `channels/` and `out/` to be created (or set
`THUMBNAIL_DISTILLER_HOME`).

```bash
PY=python3
SKILL_DIR=~/.workbuddy-ai/skills/yt-thumbnail-distill
```

Dependency: **Pillow** (images) plus **jieba** and **opencc-python-reimplemented**
(Chinese word segmentation and Traditional→Simplified conversion, both pure
Python). All three are already installed in the venv above. If the venv is missing:

```bash
python3 \
  -m venv /Users/eric/.workbuddy-ai/binaries/python/envs/default
/Users/eric/.workbuddy-ai/binaries/python/envs/default/bin/pip install Pillow jieba opencc-python-reimplemented
```

> If `pip install` fails with `EEXIST: file already exists, mkdir .../pip-install-*`,
> the sandbox is blocking pip's build temp dir. Both packages are pure Python —
> download the sdist from `https://pypi.org/pypi/<name>/json` with curl, extract
> it, and copy the package directory (`jieba/`, `opencc/`) straight into
> `.../envs/default/lib/python3.13/site-packages/`.

## Workflow

### Step 0 — Design the on-cover text FIRST (if there is an article)

A title is a sentence; a cover headline is a concept. Do not put the title on
the cover. Derive the text:

```bash
$PY "$SKILL_DIR/scripts/07_design_text.py" --title "<文章标题>" --body article.md
$PY "$SKILL_DIR/scripts/07_design_text.py" --url "https://mp.weixin.qq.com/s/xxxx"
```

It segments with jieba, converts Traditional→Simplified, and returns ranked
2–4 character candidates plus subtitle options. **Read the full method in
`$SKILL_DIR/references/text_design.md`** — the checklist there matters more than
the ranking. The script is a candidate generator, not an oracle: on the reference
channel it hits 3 of 4 real headlines within its top 4, and the miss was a
metaphor ("人生大坑") that no mechanical extractor can reach. Expect to invent
the final word yourself sometimes.

### Step 1 — Collect the channel
```bash
$PY "$SKILL_DIR/scripts/01_collect.py" "<channel URL or @handle>"
```
One request to the channel's `/videos` page yields ~30 videos with view counts.
Do **not** use `yt-dlp --flat-playlist` for view counts (returns `NA`) and do
**not** rely on `?sort=p` (yt-dlp ignores it).

### Step 1b — …or collect specific videos instead
When the user points at a handful of particular videos rather than wanting a
channel-wide read:
```bash
$PY "$SKILL_DIR/scripts/01b_collect_videos.py" "<url1>" "<url2>" --name my-style
```
Accepts full URLs (extra query params are fine), `youtu.be` links, Shorts links
or bare IDs. Writes the same `videos.json` shape, so the rest of the pipeline is
unchanged. Note: fewer than 8 references means lower confidence — say so.

### Step 2 — Download references
```bash
$PY "$SKILL_DIR/scripts/02_fetch.py" <slug> --top 10 --recent 6
```
Downloads `maxresdefault.jpg` with a quality fallback chain, strips letterbox
bars, and records the real pixel size. **Check the output**: if any image came
from `hqdefault` or smaller, say so — it means no true max-res thumbnail exists.

### Step 3 — Measure pixels
```bash
$PY "$SKILL_DIR/scripts/03_analyze.py" <slug>
```
Reads `pixel_stats.json`. Note the consensus palette, the hue-bucketed accent
colours, the aggregate contrast, the era check and the flagged outliers.

### Step 4 — Build the contact sheet
```bash
$PY "$SKILL_DIR/scripts/05_contact_sheet.py" <slug>
```

### Step 5 — VISUAL READ (the part only you can do)

**Read `channels/<slug>/contact_sheet.jpg` first** to get the overall feel, then
read **4–6 individual originals** from `channels/<slug>/refs/` for detail. Then:

1. Write `channels/<slug>/per_image_notes.md` — a short structured note per
   thumbnail: composition, subject treatment, expression, background, text
   typography (font weight / case / fill / stroke / placement), colour accents,
   and anything that deviates.
2. Synthesise the **cross-image consensus**. A feature belongs in `invariants`
   only if it appears in **>= 60%** of the sample. Things the channel never does
   go in `avoid`.

Consult `$SKILL_DIR/references/stage3_checklist.md` for the per-field prompts.

**Critical judgement:** the measured dominant palette is often *not* the
signature colour. Skin tones, soil and wood dominate by area while the actual
brand colour (bright yellow type, red props) is small-area and only shows up in
the accent buckets. Reconcile the two — do not blindly copy the top dominant.

### Step 6 — Assemble the style DNA
```bash
$PY "$SKILL_DIR/scripts/04_prompt.py" template <slug>
```
This writes `style_dna.json` pre-filled with the pixel anchors. Fill in **every
field marked `TODO`** using your Stage 5 read. Do not invent numbers.

Schema: `$SKILL_DIR/references/style_dna.schema.json`

### Step 7 — Render the guide
```bash
$PY "$SKILL_DIR/scripts/04_prompt.py" guide <slug>
```
Writes `channels/<slug>/STYLE_GUIDE.md`.

### Step 8 — Compile the prompts
```bash
$PY "$SKILL_DIR/scripts/04_prompt.py" prompts <slug> \
    --title "<the new video's title>" \
    --text "<exact on-image text>" \
    --canvas wechat-headline \
    --variants 3
```

`--canvas` picks the target and its safe band:

| value | target | ratio |
|---|---|---|
| `youtube` (default) | YouTube thumbnail | 16:9 |
| `wechat-headline` | 微信公众号头图 | 2.35:1 (900×383) |
| `wechat-square` | 公众号次条 / 朋友圈 | 1:1 |

**WeChat specifics worth knowing:** the headline cover is 2.35:1 and, in the
feed, **the bottom-left and bottom-right corners get covered by the overlaid
title**. Keep all text in the centre and upper half. The secondary-article cover
renders at only 200×200 — big type, few elements, high contrast, no detail.

Writes `out/prompts/<slug>_<title>.md` containing:

- **Mode B — with reference image** (recommended): user uploads 1–2 real
  thumbnails to ChatGPT alongside the prompt. Highest fidelity.
- **Mode A — text only**: no reference image.
- **Textless background prompt** for the local-render route.
- **Repair prompt** for when the output drifts.

For CJK text the compiler emits a **Chinese-language directive block** built
around the wording that works best for GPT Image:

```
必须包含以下文字，逐字呈现：
  "内耗"
文字要求：
  - 语言：简体中文。只使用规范简体汉字，共 2 个字。
  - 字体气质：粗宋体（明朝体）…
  - 字号：文字高度约占画面高度的 20.6%…
  - 文案只出现一次，不要重复…
  - 每个字都必须是笔画完整、正确无误的简体汉字…
补充禁止项：不要随机文字，不要无意义占位文字，不要乱码字符，不要水印…
```

It also appends a **验收清单** (per-character verification checklist) — always
tell the user to check the output glyph by glyph before accepting it.

**Always show the compiled Mode B prompt in your reply**, not just the file
path — the user's next action is to paste it into ChatGPT.

### Step 9 — Local rendering (only when the model keeps failing)

Let GPT render the text first. Use the local renderer as a fallback: when the
same character comes out wrong three times running, when the headline exceeds
4 characters, or when the user explicitly wants pixel-exact type.

1. Ask ChatGPT for the **blank background only** (the textless prompt the
   compiler already emits) and save it as `bg.png`.
2. Set the type locally — exact glyphs, exact font, reproducible effect:

```bash
$PY "$SKILL_DIR/scripts/06_render_cover.py" <slug> \
    --text "人生大坑" --top "第 24 集" --bottom "一句话说明" \
    --bg bg.png --out cover.png --canvas wechat-headline
```

Omit `--bg` to use the built-in procedural paper background (calibrated against
the reference measurements). The renderer reads `style_dna.json` for font file,
size, position, and the chromatic-aberration offset.

**Font choice matters for Simplified vs Traditional.** In `Songti.ttc` and
`STHeiti*.ttc` the index selects the script: pick the `SC` index (Songti index
0/1/3/6, Heiti index 1). Using a `TC` index silently outputs Traditional glyphs,
which is a common and hard-to-spot failure.

Verify the render afterwards by measuring it with the same method used on the
references (row-band ink thresholding) and compare the headline's y-centre,
glyph height and width. If they differ by more than ~1 percentage point, adjust
`size_pct_of_canvas_height` / `headline_y_pct` in the DNA.

## Definition of done

- [ ] `channels/<slug>/pixel_stats.json` exists and covers >= 8 references
      (fewer is allowed for an explicit video list — but flag the lower confidence)
- [ ] `channels/<slug>/contact_sheet.jpg` was actually viewed by you
- [ ] `channels/<slug>/per_image_notes.md` written
- [ ] `style_dna.json` has **no remaining `TODO`** fields
- [ ] `STYLE_GUIDE.md` rendered
- [ ] `out/prompts/*.md` rendered, with Mode A, Mode B, textless background prompt and repair prompt
- [ ] For CJK text: the Chinese directive block is present and the 验收清单 is in the file
- [ ] The Mode B prompt is quoted in your reply to the user
- [ ] If an article was supplied: `07_design_text.py` was run and the candidate
      list was actually read (not blindly taking rank 1)
- [ ] You stated the limitations (see below) rather than overselling fidelity

## Prompt-craft rules (baked into the compiler, respect them when editing)

- Order: **scene → subject → details → constraints**.
- Keep all key elements inside a **centred 16:9 safe band** — ChatGPT outputs
  3:2 (1536×1024), so the user must crop to 16:9.
- On-image text: quote the string, prefer **UPPERCASE and <= 4-5 short words**,
  give fill hex + stroke + position + size as a percentage of canvas height.
  Always add `The only text in the image is "<TEXT>".` — a positive statement is
  required; negatives alone do not work.
- Spell tricky strings letter by letter (`H-O-W`) if the model keeps failing.
- State both the positive and the negative for text: `no watermark, no extra
  text, no logos...`.
- **Chinese on-image text**: the compiler auto-detects CJK in `--text` and then
  (a) switches the Text block to a Chinese-specific form, (b) adds "no Latin
  letters / no English words / no pinyin / no kana" to the constraints, and
  (c) drops Latin-only advice such as "avoid script type". Keep headlines to
  **2-4 characters** — success rate falls off sharply beyond that.
- **Never** use Stable Diffusion syntax (`(word:1.5)`, tag soup, `8K
  masterpiece`) — ineffective to harmful on GPT-image models.
- Describe position and size in **canvas proportions**, not vague words.
- For iteration, repeat the full Text block and say "change only X, keep
  everything else the same".
- Use `a fictional person` for any human subject — real names/faces trip
  moderation.

## Honest limitations (tell the user these)

- Style DNA describes a **distribution**, not the distribution itself. A
  text-only prompt gets you "same genre", not "same channel". **Mode B with a
  real reference image is the only high-fidelity path.**
- **Chinese glyph rendering is the weak point of every image model.** The
  compiler mitigates it (verbatim quoting, short strings, explicit language and
  legibility demands, banned failure modes) but cannot eliminate it. Always hand
  the user the 验收清单 and tell them to check character by character. Keep
  headlines to **2–4 characters** — the error rate climbs fast beyond that.
- **`07_design_text.py` cannot invent a metaphor.** Back-tested against the
  reference channel it lands 3 of 4 real headlines within its top 4, but the
  miss was the one where the author coined an image ("人生大坑") that appears
  nowhere in the title. Treat its output as a strong starting set, not an answer.
- With fewer than 8 references the style read is indicative, not solid. Do not
  claim high confidence from 4 samples — say "medium" and explain why.
- Cannot capture: real identities/faces, specific IP, comedic subtext, brand assets.
- The pixel stats are precise but **weakly causal** — they are anchors and
  cross-checks, not the style judgement.
- Top-by-views skews toward older hits and away from the current style; view
  counts drift over time.
- Faithfully cloning another channel's style sits in a **copyright / likeness
  grey zone** — recommend personal-reference use only.
