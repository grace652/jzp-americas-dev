# Wallpaper sources — link patterns and case studies

## Primary: osxdaily.com

Publishes one article per Apple release with **direct CDN links** to full-size
files. URL pattern:

```
https://cdn.osxdaily.com/wp-content/uploads/<YYYY>/<MM>/<slug>.jpeg
```

Two gotchas:

1. The article body shows **lazy-load placeholder GIFs** (`a3-lazy-load`), not
   the real images. Fetch the page as text/markdown and read the anchor `href`,
   not the `<img src>`.
2. Files are served from a slow CDN. Use resume + retry and background it.

**Limitation:** osxdaily writes launch-day posts and does not always backfill
later beta additions. Do not treat its count as complete.

## Best for a complete set: iclarified.com

Keeps a **single page updated as betas land**, and publishes a consolidated ZIP:

```
https://www.iclarified.com/files/macos/iClarified-<OS>-<Version>-<Name>-Wallpaper.zip
```

This is the fastest route to the whole collection — one download, every variant
including the abstract light/dark and their 4K/5K/HEIC forms.

**Individual image links on the article are hotlink-protected.** Fetching
`https://www.iclarified.com/images/news/<id>/<file>.jpg` directly returns HTTP
404 (a 32 KB error page), even though the same files are inside the ZIP. Take
the ZIP.

## Fallbacks

| site | notes |
|---|---|
| 9to5mac.com | usually links the same source files; good for confirming resolution |
| basicappleguy.com/haberdashery | frequently the **original capturer** of landscape stills pulled from screen savers, and he runs a real super-resolution upscale + sharpen. Also publishes his own iPhone portrait crops. |
| applealmond.com | Chinese-language; often tabulates the full set and hosts keynote-only artwork not shipped as a wallpaper |
| 4kwallpapers.com | desktop resolutions only; the scenic sets have no portrait section |
| wallpaperaccess.com | community reposts, quality varies, verify resolution |

**Search queries that work:** `macOS <ver> <name> wallpaper`,
`download official macOS <ver> <name> wallpaper`, `macOS <name> <ver> 默认壁纸 下载`,
and for completeness `<os> <ver> <codename> wallpaper beta`.

---

## Case study: macOS 27 Golden Gate (released 2026)

Announced at WWDC26, named after the Golden Gate Bridge rather than a park —
the first macOS release not named for a natural landmark. iOS 27, iPadOS 27 and
macOS 27 share variations of the same artwork (curved shapes forming a stylised
"27").

### The complete set — seven items, added across three waves

| # | variant | added | subject | native |
|---|---|---|---|---|
| 1 | Golden Gate (abstract, Light) | beta 1 | abstract curves | 4480×3088 |
| 2 | Golden Gate (abstract, Dark) | beta 1 | abstract curves | 4480×3088 |
| 3 | Golden Gate Sunset | beta 3 | bridge at golden hour from a rocky shoreline | 4096×2160 |
| 4 | Golden Gate Night | beta 3 | aerial, bridge lit, skyline + moon | 4096×2160 |
| 5 | Golden Gate Day | beta 6 | aerial, bright blue sky | 4096×2160 |
| 6 | Golden Gate Evening | beta 6 | dramatic clouds, silhouetted, low over water | 4096×2160 |
| 7 | Golden Gate (WWDC artwork) | keynote | illustrated / comic-style | 5504×3072 |

Items 5 and 6 landed **two months after** every launch-day article, which is why
a set built from June coverage is missing a third of the scenic wallpapers. Item
7 is keynote slide artwork, not a shipped system wallpaper — label it as such.

### Naming collisions — identify by opening the file

| image | BasicAppleGuy | iClarified / OSXDaily |
|---|---|---|
| rocky shoreline, golden hour | "Day" | "Sunset" |
| aerial, lit at night | "Night" | "Night" |

BAG posted his beta-3 pair before Apple's official naming settled. His
`GoldenGate_Day.jpg` is the **sunset** image. Never infer content from a
filename or a blog label.

### Measured anchors

`vedge` (vertical-edge energy), band 0.55, smooth 41, on the 4096×2160 natives:

| image | tower edge peaks | chosen anchor | `redness` result (for contrast) |
|---|---|---|---|
| Day | 2719 / 2877 | `2818:0.42` | 2754 — marginal |
| Evening | 1306 / 1478 | `1392:0.40` | 20 — **sky, wrong** |
| Sunset | 2996 | `2996:0.58` | 20 — **sky, wrong** |
| Night | 1616 / 1843 | `1726:0.40` | 1616 — correct |

`redness` inverts on Sunset and Evening: the golden sky is the most "red" thing
in frame, so it takes rank 1. `vedge` finds the tower on all four.

### Native resolution — and who is upscaling

Third parties routinely upscale Apple's assets and publish the bigger file as if
it were higher quality. Check the native before trusting a pixel count:

| asset | true native | circulating "bigger" version | upscale |
|---|---|---|---|
| Golden Gate abstract (Light/Dark) | **4480×3088** (HEIC, Apple's own) | osxdaily 6016×4147 | 1.343× |
| Golden Gate scenic (Day/Evening/Sunset/Night) | **4096×2160** (4K video frame) | BasicAppleGuy 7396×3900 | 1.806× |

Both pairs were verified to be the *same image* by pixel comparison, not merely
similar dimensions. So osxdaily's 6016×4147 abstracts are BAG upscales too, and
its 7396×3900 landscapes likewise.

Practical consequence: the abstract's real detail is 4480×3088 either way, so a
9:16 crop from the 6016×4147 version (2333×4147 → clean downscale to 2160×3840)
is preferable to cropping the native (1737×3088 → would need 1.24× upscaling).
For the scenic wallpapers the opposite holds — see SKILL.md Step 4b.

### Super-resolution models — measured and rejected

Tested via `opencv-contrib-python` (`cv2.dnn_superres`), all against the same
2160×3840 target. **None beat `LANCZOS + unsharp r1.4 p70`.** Kept here so the
experiment is not repeated:

| model | URL | size |
|---|---|---|
| EDSR_x2 | `https://github.com/Saafke/EDSR_Tensorflow/raw/master/models/EDSR_x2.pb` | 36.7 MB |
| ESPCN_x2 | `https://github.com/fannymonori/TF-ESPCN/raw/master/export/ESPCN_x2.pb` | 84 KB |
| FSRCNN_x3 | `https://github.com/Saafke/FSRCNN_Tensorflow/raw/master/models/FSRCNN_x3.pb` | 39 KB |
| LapSRN_x2 / x4 | `https://github.com/fannymonori/TF-LapSRN/raw/master/export/LapSRN_x2.pb` | 1.3 / 2.6 MB |

Install with `pip install opencv-contrib-python` (~56 MB wheel; measured 1.6 MB/s
from PyPI, ~45 s). Model files came down at ~750 KB/s. Both are far faster than
the wallpaper CDNs — the download cost is not the reason to skip this; the
measured quality result is.

The blocker is structural: **opencv's models only offer ×2/×3/×4.** The needed
factor here is 1.78×, so any model output must be downscaled back, and that
resample throws away the detail the model just added. EDSR_x2 at 2430×4320
scored 1.279 after the downscale — *below* plain LANCZOS at 1.328.

### Verified output geometry

| output | crop rect | result | upscale |
|---|---|---|---|
| 9:16 Day / Evening | (2308 or 906, 0, 1215×2160) | 2160×3840 | 1.78× |
| 19.5:9 Day / Evening | (2401 or 994, 0, 994×2160) | 1320×2868 | 1.33× |
| no-upscale Day / Evening | same as 9:16 | 1215×2160 | none |
| 9:16 Night / Sunset | (2242 or 4124, 0, 2194×3900) | 2160×3840 | from 7396×3900 source |
| 19.5:9 Night / Sunset | (2402 or 4356, 0, 1795×3900) | 1320×2868 | ditto |
| 9:16 abstract | (1841, 0, 2333×4147) | 2160×3840 | 1.25×-ish |
| 9:16 WWDC | (2406, 0, 1728×3072) | 2160×3840 | 1.25× |

Night and Sunset were cropped from **BasicAppleGuy's super-resolution upscale**
(7396×3900) rather than the 4096×2160 native, because his upscale carries ~30%
more acutance than LANCZOS can produce — measured, see SKILL.md Step 4b. Day and
Evening have no such upscale in circulation, so they are LANCZOS + unsharp from
native. **The set is therefore mixed-provenance; say so rather than implying all
seven went through the same pipeline.**

### Download reliability

The osxdaily and basicappleguy CDNs both run slow (100–400 KB/s observed). A
plain foreground `curl` gets SIGKILLed before finishing. Always use resume +
retry and `run_in_background=true`:

```bash
curl -sL -C - --retry 8 --retry-delay 3 --retry-all-errors --max-time 900 \
  -o out.jpg "<url>"
```

The iClarified ZIP (~35 MB) is the exception — it came down in ~34 s.

### Delivered artefact set

```
macos27-golden-gate-wallpapers/
├── 4k-9x16/                    7 files @ 2160×3840
├── iphone-native-19.5x9/       7 files @ 1320×2868
├── native-no-upscale/
│   ├── 9x16/                   2 files @ 1215×2160  (Day, Evening)
│   └── 19.5x9/                 2 files @  994×2160  (Day, Evening)
├── originals-native/           Apple's own assets: 2 abstracts @ 4480×3088,
│                               4 scenic @ 4096×2160
├── originals-upscaled/         third-party upscales @ 6016×4147 / 7396×3900
└── sources/                    basicappleguy / iclarified / wwdc
```

`native-no-upscale/` holds only Day and Evening, and that is correct rather than
incomplete: the abstracts are downscaled from 4480×3088 and Night/Sunset are
downscaled from BasicAppleGuy's 7396×3900, so those five never upscale in the
first place. **Emit both aspect ratios here** — a 9:16 "no-upscale" file is the
wrong shape for a 19.5:9 phone, which would crop it again on device.

### Verification

Every delivered file was checked by opening it and asserting its exact pixel
size (18/18 pass on the macOS 27 set). Both aspect-ratio sets were also viewed as
contact sheets — the 19.5:9 crops are ~20% narrower than the 9:16 ones, so a
composition that works at 9:16 can still clip the subject at 19.5:9. **Check
both; they are not interchangeable.**
