---
name: apple-wallpaper-portrait
description: Turn Apple's landscape stock wallpapers (macOS / iOS / iPadOS) into phone-ready portrait wallpapers at 4K and native iPhone resolutions. Use when the user asks for a 竖版 / vertical / portrait / phone wallpaper of a macOS or iOS stock wallpaper, or wants a stock wallpaper downloaded and fitted to a phone. Covers sourcing the official artwork, locating the photographic subject, and anchored (non-centred) cropping.
description_zh: "把 Apple 官方横版壁纸裁成手机竖版 4K，含主体锚点定位"
description_en: "Crop Apple stock wallpapers into phone-ready portrait 4K"
agent_created: true
---

# Apple Stock Wallpaper → Phone Portrait

Turn "I want the macOS/iOS stock wallpaper in portrait for my phone" into a
delivered set of correctly composed portrait images.

## Hard constraints (do not violate)

1. **Apple never ships portrait stock wallpapers.** Every stock wallpaper is
   landscape. A portrait version is always a *crop*, never an official asset.
   **Tell the user this explicitly** — do not let them believe they are getting
   an official portrait file.
2. **Never centre-crop a scenery wallpaper.** On the macOS 27 Golden Gate
   *sunset* wallpaper the bridge tower sits at x = 0.730 of the width; a centre
   crop deletes the Golden Gate Bridge from a Golden Gate wallpaper. Locate the
   subject first (Step 2), then crop around it (Step 3).
3. **Never upscale.** If the crop is larger than the source region, the output
   is fake detail. The script flags this — if it flags, say so.
4. **Always look at the result.** Generate a contact sheet and read it. Numeric
   crop coordinates are not evidence that the composition works.
5. **Never claim the dynamic/aerial wallpapers.** macOS ships animated
   wallpapers and drone-footage screen savers; those cannot be captured as a
   still. Any "dynamic version" circulating online is a screen recording.

## Environment

```bash
PY=python3
SKILL_DIR=~/.workbuddy-ai/skills/apple-wallpaper-portrait
```

Dependencies: **Pillow** + **numpy**. Both already installed in the venv above.
If the venv is missing:

```bash
python3 \
  -m venv /Users/eric/.workbuddy-ai/binaries/python/envs/default
/Users/eric/.workbuddy-ai/binaries/python/envs/default/bin/pip install Pillow numpy
```

## Workflow

### Step 1 — Source the originals

See `references/sources.md` for the known direct-link patterns and a per-release
case study. Summary of what works:

- **osxdaily.com** publishes direct CDN links per release — fastest path, and
  the URLs are stable. Look for the `cdn.osxdaily.com/wp-content/uploads/...`
  link on the article page (the on-page thumbnails are lazy-load placeholders,
  so fetch the page and read the *anchor href*, not the `<img src>`).
- **9to5mac.com / iclarified.com / basicappleguy.com** are fallbacks.
- Expect roughly: abstract wallpapers ~6016×4147, photographic wallpapers
  ~7396×3900.

**Downloads from these CDNs are slow** (100–400 KB/s observed). A plain
foreground `curl` gets SIGKILLed before finishing. Always:

```bash
curl -sL -C - --retry 8 --retry-delay 3 --retry-all-errors --max-time 900 \
  -o out.jpeg "<url>"
```

…run with `run_in_background=true`. Verify afterwards with `PIL.Image.open()`
— check both that it parses and that the pixel dimensions match the published
resolution. A resumed download can silently end short.

### Step 2 — Locate the subject before cropping

```bash
$PY "$SKILL_DIR/scripts/crop_portrait.py" detect <image.jpeg>
```

Default metric is `vedge` — **vertical-edge energy** — measured over the top 55%
of the frame and smoothed with a 41 px moving average.

**Why `vedge` and not `redness`.** The obvious instinct is to find the red
Golden Gate towers by colour. It works on some frames and fails badly on others.
Measured on the four macOS 27 scenic wallpapers (4096×2160 native):

| image | `redness` top hit | correct? | `vedge` top hit | correct? |
|---|---|---|---|---|
| Golden Gate Night | x=1616 (0.395) | yes | x=1085 (0.265) | no |
| Golden Gate Sunset | x=20 (0.005) | **no — sky** | x=2996 (0.731) | yes |
| Golden Gate Day | x=2754 (0.672) | marginal | x=2719 (0.664) | yes |
| Golden Gate Evening | x=20 (0.005) | **no — sky** | x=1478 (0.361) | yes |

`redness` averages over the whole column, so a large smooth sky dilutes — and on
Sunset and Evening it inverts, putting the brightest sky at rank 1. `vedge`
looks for *vertical structure*, which is what a bridge tower is, and it does not
care about illumination: it works on the silhouetted Evening frame where colour
carries no signal at all. Use `redness` only when the subject is genuinely the
only warm thing in frame and the sky is dark.

**Peaks come in pairs.** A tower produces two edge-peaks — one per side. The
midpoint is the anchor you want. Night's pair is x=1616/1843 → tower centre
≈1730; Evening's is x=1306/1478 → ≈1392. `--merge-gap` can average a pair for
you, but it is **off by default on purpose**: on the Day wallpaper the bridge
deck adds a peak at x=2637, only 82 px from the tower edge at 2719, so a merge
wide enough to catch the pair also swallows the deck and drags the centre
off-frame. Read the raw peaks and take the midpoint yourself.

**The top hit is never automatically the subject.** Cross-check by cropping the
candidate and looking at it. Ask: *is this a compact vertical structure, or a
wide soft gradient?* A narrow spike is an object; a broad plateau is sky.

Metric cheat sheet:

| metric | finds | use for |
|---|---|---|
| `vedge` (default) | vertical structure | bridge towers, masts, buildings, aerial scenery |
| `local_contrast` | busiest detail columns | texture, crowds, foliage |
| `p95_redness` | small warm subjects | a red object under a large sky |
| `redness` | dominant warm region | sunsets where the subject *is* the sky |
| `warmth` | broad warm regions | sand, desert, golden-hour fields |
| `variance` | busiest columns | generic "where's the detail" probe |

For pure abstract artwork there is no subject — **centre-crop is correct there.**
Use `vedge` only to sanity-check that the crop is not landing on a featureless band.

### Step 3 — Crop with an anchor

```bash
$PY "$SKILL_DIR/scripts/crop_portrait.py" crop <image> \
    --out 4k/name.jpg --size 2160x3840 --anchor 5397:0.58
```

`--anchor X:FRAC` = "put the subject pixel at X at FRAC of the crop width".
Rules of thumb:

- Photographic scenery: `FRAC` 0.35–0.40 puts the subject left-of-centre with
  the scene opening to the right; 0.55–0.60 puts it right-of-centre. Both beat
  0.50 because the phone's clock and dock occupy the vertical centre band.
- Omit `--anchor` for abstract artwork.

Crop geometry (also in `compute_crop()`): take the full source height and
derive the crop width from the target aspect; if that overflows the source
width, fit the width instead and centre vertically. Then
`x0 = round(anchor_x − FRAC × crop_w)`, clamped to the image.

### Step 4 — Emit every target size in one pass

Prefer `batch` over repeated `crop` calls — one manifest, all sizes:

```json
{
  "targets": [
    {"name": "4k-9x16",              "w": 2160, "h": 3840},
    {"name": "iphone-native-19.5x9", "w": 1320, "h": 2868}
  ],
  "images": [
    {"src": "desktop-originals/01-dark-abstract.jpeg", "slug": "…-dark-abstract"},
    {"src": "desktop-originals/02-bridge-night.jpeg",  "slug": "…-bridge-night",  "anchor": [3120, 0.40]},
    {"src": "desktop-originals/04-bridge-sunset.jpeg", "slug": "…-bridge-sunset", "anchor": [5397, 0.58]}
  ]
}
```

```bash
$PY "$SKILL_DIR/scripts/crop_portrait.py" batch manifest.json
```

**Ship two aspect ratios by default.** "4K portrait" means 2160×3840 (9:16),
but modern iPhones are 19.5:9 (1320×2868). On a 19.5:9 device a 9:16 image is
width-filled and then cropped top and bottom, losing ~18% of the frame. The
native-size set avoids any device-side rescaling. Output is JPEG q95,
`subsampling=0` (4:4:4), sRGB ICC embedded.

### Step 4b — Know the resolution ceiling before you promise 4K

**Apple's aerial/photographic stock wallpapers are 4K video frames: the native
still is 4096×2160.** A 9:16 portrait crop of that is only **1215×2160**, so
every "4K portrait" version is an upscale — 1.78×. There is no larger official
asset; the 5K/6K files floating around are third-party upscales.

So before delivering, establish what real detail you actually have:

| source | native still | 9:16 crop | upscale to 2160×3840 |
|---|---|---|---|
| macOS 27 scenic (Day/Evening/Sunset/Night) | 4096×2160 | 1215×2160 | 1.78× |
| macOS 27 abstract | 4480×3088 | 1737×3088 | 1.25× |

`crop_portrait.py` refuses to upscale unless you pass `--allow-upscale`, and
always reports `real_detail` and `upscale_factor`. Surface both numbers to the
user. Also offer a **no-upscale** variant at the true native crop size
(e.g. `--size 1215x2160` with no `--allow-upscale`) so the user can choose
interpolation-free pixels over nominal resolution.

**If a high-quality upscale of the source already exists, use it instead of
upscaling yourself.** This is not a stylistic preference, it is measurable.
Calibrating on the macOS 27 night wallpaper, at an identical 2160×3840 output:

| pipeline | gradX (acutance) | vs reference | time / frame |
|---|---|---|---|
| LANCZOS only | 0.866 | −37% | <1 s |
| iterative back-projection (IBP, 8–15 iters) | 0.812 | −41% | ~20 s |
| LANCZOS + unsharp r1.4 p70 (this script's default) | 0.985 | −28% | <1 s |
| two-pass ×1.33 with sharpening between | 1.014 | −26% | ~1 s |
| ESPCN_x2 + unsharp (ML) | 0.988 | −28% | ~1 s |
| FSRCNN_x3 + unsharp (ML) | 1.010 | −26% | ~1 s |
| LapSRN_x2 + unsharp (ML) | 0.912 | −33% | ~6 s |
| EDSR_x2 + unsharp (ML) | 1.334* | −34% | ~6 min |
| third-party super-resolution upscale (BasicAppleGuy) | 1.370 | reference | — |

**Do not reach for a local super-resolution model.** Every one was measured and
none beats `LANCZOS + unsharp r1.4 p70` at the 2160×3840 target:

- The light models (ESPCN, FSRCNN) land within 2% of LANCZOS + unsharp — no
  benefit for the added dependency.
- **LapSRN is worse** and **EDSR is worse still** (1.279 raw on a sub-region,
  below plain LANCZOS). The reason is structural: EDSR only ships ×2/×3/×4, so
  its 2430×4320 output must then be downscaled to 2160×3840, and that resample
  discards exactly the high-frequency detail the model added.
- EDSR also costs ~6 minutes per frame on CPU.
- *On a sub-region, EDSR+USM scored 1.334 against a reference of 2.010 — the
  full-frame figure is the one to compare against the table above.

So: **prefer an existing good upscale; otherwise use LANCZOS + `r1.4 p70` and
say which path each file took.** Do not silently mix the two and present the set
as uniform. Model URLs are in `references/sources.md` if you ever want to
re-verify this.

**Acutance is not the same as real detail.** Chasing the reference's number by
sharpening harder does not recover information — it adds halos and ringing. The
gap above is a genuine information gap, not a tuning failure, and the honest
move is to disclose it rather than mask it.

### Step 5 — Verify by looking

Build a contact sheet of all outputs at ~520 px tall, in one row, and **read
it**. Check specifically: is the subject present, is it cut by an edge, does
the composition survive being covered by a clock at the top and a dock at the
bottom.

## Reproducibility note

Re-running `batch` on the same inputs reproduces the same crop rectangles and
**pixel-identical** output. The only byte-level difference is 3 bytes inside
the embedded ICC profile (its creation timestamp). `numpy` comparison of the
decoded arrays returns max diff = 0. So: safe to regenerate; do not `cmp`
the files and conclude something changed.

## Enumerate the complete set first

**Apple adds stock wallpapers across the beta cycle, not all at once.** Trusting
a single article gives you an incomplete set. The macOS 27 case is the warning:
the launch coverage listed four wallpapers, but two more (Golden Gate Day and
Golden Gate Evening) arrived in beta 6 two months later, and one more existed
only as WWDC keynote artwork.

Before cropping anything, establish the full list:

1. Find the **latest** article for the release, not the launch-day one. Search
   `<os> <version> <codename> wallpaper beta` and check the date.
2. Prefer a source that **consolidates the collection** — iClarified keeps one
   page updated as betas land, which is why its ZIP contained all four scenic
   wallpapers while the launch-day posts had two.
3. Cross-check the count against a second-language source; Chinese-language
   coverage often tabulates the set (the macOS 27 tally of seven came from one).
4. Ask explicitly: *is there a variant for a different time of day, light/dark,
   or a keynote-only artwork?* Those are the ones that go missing.

## Definition of done

- [ ] The complete wallpaper list was established from the **latest** source,
      not a launch-day article, and the count was cross-checked
- [ ] Originals downloaded and their real pixel dimensions verified by opening
      them, not by trusting the article text
- [ ] `detect` run on every photographic image, and the chosen anchor
      cross-checked against a visual read (false peaks ruled out)
- [ ] Both a 9:16 4K set and a native-iPhone-aspect set emitted
- [ ] A no-upscale set emitted for any image whose source cannot fill 4K, **in
      both aspect ratios** — a 9:16 no-upscale file is the wrong shape for a
      19.5:9 phone and will be cropped again on device
- [ ] Contact sheets built for **both** aspect ratios and actually viewed — the
      19.5:9 crop is ~20% narrower than the 9:16 one, so a composition that
      works at 9:16 can still clip the subject at 19.5:9
- [ ] Every delivered file opened and its exact pixel size asserted
- [ ] Every upscaled output disclosed with its `upscale_factor` and real detail
- [ ] Each file's provenance known — existing high-quality upscale vs own
      LANCZOS — and the set not presented as uniform if it is mixed
- [ ] The user was told portrait versions are crops, not official assets

## Honest limitations (tell the user these)

- **Portrait stock wallpapers do not exist.** Every portrait version is a crop,
  so it shows less of the artwork than the landscape original.
- **The native ceiling is a 4K video frame.** Photographic/aerial stock
  wallpapers are 4096×2160 stills; a 9:16 crop leaves 1215×2160 of real detail.
  Any 2160×3840 file is a 1.78× upscale, and no amount of local sharpening
  matches a true super-resolution pass (~30% acutance shortfall, measured).
- **Animated wallpapers cannot be captured.** macOS's dynamic wallpapers and
  aerial screen savers are motion; a still is a still.
- **Cropping a landscape to 19.5:9 discards a lot.** On a 4096×2160 source the
  19.5:9 crop keeps 994 of 4096 columns — 24% of the width. If the subject is
  not compact, the result may feel over-zoomed; say so rather than shipping it.
- **Third-party redistribution.** The convenient direct links are community
  mirrors, not Apple's own download page. Content matches, but for public or
  commercial use the licensing should be checked independently. Personal use is
  the normal case.
- **Naming is inconsistent across sites.** BasicAppleGuy's "Golden Gate Day" is
  the image iClarified and OSXDaily call "Sunset". Identify images by opening
  them, never by filename or by a blog's label.
- There is **no universal subject detector** here. `vedge` is a good default for
  vertical structure but the script's top hit can still be a false positive —
  the visual check is not optional.
