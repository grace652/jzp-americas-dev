# Stage 3 checklist — the visual read

Fill these in by **looking at the images**, then reconcile against
`pixel_stats.json`. The stats give you anchors; this gives you the style.

Read `contact_sheet.jpg` first for the overall feel, then 4–6 individual
originals from `refs/` for detail.

---

## 1. First impression (write one sentence before analysing)

What does a viewer register in the first half-second? If you cannot say it in
one sentence, keep looking.

## 2. The signature move

The single most recognisable device. One sentence. This becomes
`signature_move` and it is the highest-leverage field in the whole DNA.

Ask: if I removed this one thing, would the thumbnail still look like this
channel?

## 3. Per-image notes (`per_image_notes.md`)

For each reference, note:

| Dimension | What to record |
|---|---|
| Composition | Where is the subject? Where is the text? What is the split? |
| Subject | Who/what, framing (close-up / chest-up / wide), gaze direction |
| Expression | The actual emotion and its intensity (1–5) |
| Background | Environment, depth of field, is it defocused? |
| Text | Exact string, font class, case, fill colour, stroke, shadow, position, line count |
| Colour accents | Which saturated colours appear and where |
| Lighting | Key direction, rim separation, colour temperature |
| Deviation | What makes this one different from the others? |

## 4. Cross-image consensus

For each feature, count how many of the sample share it.

- **>= 60%** → belongs in `invariants` (goes into every prompt as a hard requirement)
- **Never appears** → belongs in `avoid` (becomes a negative constraint)
- **20–60%** → a variant, not an invariant. Do not put it in `invariants`.

## 5. Reconcile with the pixel stats

Answer these explicitly:

1. Is the top dominant colour actually the **brand** colour, or just the
   largest photographic area (skin, soil, sky)?
2. Which colours appear in the **accent buckets** (`accents[]`)? Those are the
   small-area high-saturation colours — usually the real brand palette.
3. What is `typography.headline.fill_hex`? This is the text colour and it is
   often **not** in the dominant palette at all.
4. Does `era_check.style_shift_detected` flag a style change? If yes, say so and
   base the DNA on the **recent** half.
5. Which videos are flagged as outliers? Exclude them from the consensus read
   but keep their notes.

## 6. Palette roles

Assign a role to each dominant colour: `background` / `subject` / `skin` /
`text` / `accent` / `unassigned`.

Then set `palette.background_hex`. It may be a hex code **or a short phrase**
when the channel varies its backgrounds per video — e.g.
`"a saturated environment keyed to the video premise (common dark base #322C25)"`.

## 7. Common traps

- **Dominant ≠ signature.** Skin and soil win on area. The brand colour is small.
- **Don't trust a single image.** One striking thumbnail is not a style.
- **Outliers look like the style but aren't.** Check `deviation_score`.
- **Numbers in the headline are a motif, not decoration** — if every sample has
  one, it belongs in `invariants`.
- **A textless variant is not a different style.** If some samples lack a
  headline, note it, but the headline rule usually still holds for the majority.
- **Don't invent precision.** If you can't tell whether the stroke is 6px or
  8px, say "thick" and let the round number stand.
