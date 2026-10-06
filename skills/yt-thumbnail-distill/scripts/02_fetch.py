#!/usr/bin/env python3
"""Stage 2a - select the reference sample and download the thumbnails.

Sampling rule (see plan): 10 top-by-views (proven) + 6 most recent (current
style), deduplicated. Downloads maxresdefault.jpg with a quality fallback
chain and strips any letterbox bars.

Usage:
    python 02_fetch.py <channel-dir-or-slug> [--top 10] [--recent 6]
"""
from __future__ import annotations

import argparse
import urllib.error
from pathlib import Path

from PIL import Image, ImageStat

from _common import http_get, read_json, resolve_channel_dir, write_json

# ordered best -> worst; maxresdefault 404s when the uploader never provided one
QUALITY_CHAIN = ["maxresdefault", "sddefault", "hqdefault", "mqdefault"]

MIN_ACCEPTABLE_WIDTH = 480  # below this the "maxres" is really an upscaled stub


def select_sample(videos: list[dict], top_n: int, recent_n: int) -> tuple[list[dict], list[str]]:
    """Return (selected, notes). Videos without view counts are still eligible
    for the recent bucket."""
    with_views = [v for v in videos if v.get("views") is not None]
    top = sorted(with_views, key=lambda v: v["views"], reverse=True)[:top_n]

    dated = [v for v in videos if v.get("age_days") is not None]
    recent = sorted(dated, key=lambda v: v["age_days"])[:recent_n]

    selected, seen, notes = [], set(), []
    for bucket, items in (("top_views", top), ("recent", recent)):
        for v in items:
            if v["video_id"] in seen:
                continue
            seen.add(v["video_id"])
            selected.append({**v, "bucket": bucket})

    if len(top) < top_n:
        notes.append(f"only {len(top)} videos had a view count (wanted {top_n})")
    if len(recent) < recent_n:
        notes.append(f"only {len(recent)} videos had an upload age (wanted {recent_n})")
    return selected, notes


def strip_letterbox(img: Image.Image, dark_threshold: int = 22, max_frac: float = 0.14):
    """Detect and crop uniform near-black bars top/bottom. Returns (img, meta)."""
    w, h = img.size
    gray = img.convert("L")
    max_bar = int(h * max_frac)

    def bar_from(edge: str) -> int:
        size = 0
        for i in range(max_bar):
            y = i if edge == "top" else h - 1 - i
            row = gray.crop((0, y, w, y + 1))
            st = ImageStat.Stat(row)
            if st.mean[0] <= dark_threshold and st.stddev[0] <= 6:
                size = i + 1
            else:
                break
        return size

    top_bar, bottom_bar = bar_from("top"), bar_from("bottom")
    if top_bar or bottom_bar:
        img = img.crop((0, top_bar, w, h - bottom_bar))
        return img, {"letterbox_cropped": True, "top_px": top_bar, "bottom_px": bottom_bar}
    return img, {"letterbox_cropped": False, "top_px": 0, "bottom_px": 0}


def download_thumbnail(video_id: str, dest_dir: Path) -> dict:
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / f"{video_id}.jpg"

    last_err = None
    for quality in QUALITY_CHAIN:
        url = f"https://i.ytimg.com/vi/{video_id}/{quality}.jpg"
        try:
            raw = http_get(url, timeout=30)
        except urllib.error.HTTPError as exc:
            last_err = f"{quality}: HTTP {exc.code}"
            continue
        except Exception as exc:  # noqa: BLE001 - network noise, try next tier
            last_err = f"{quality}: {exc}"
            continue

        dest.write_bytes(raw)
        try:
            with Image.open(dest) as im:
                im.load()
                width, height = im.size
                img = im.convert("RGB")
        except Exception as exc:  # noqa: BLE001
            last_err = f"{quality}: unreadable image ({exc})"
            continue

        if quality == "maxresdefault" and width < MIN_ACCEPTABLE_WIDTH:
            last_err = f"{quality}: stub image {width}x{height}"
            continue

        img, box_meta = strip_letterbox(img)
        if box_meta["letterbox_cropped"]:
            img.save(dest, "JPEG", quality=95)

        return {
            "ok": True,
            "path": str(dest),
            "quality_used": quality,
            "width": img.size[0],
            "height": img.size[1],
            "aspect_ratio": round(img.size[0] / img.size[1], 4),
            "bytes": dest.stat().st_size,
            **box_meta,
        }

    return {"ok": False, "path": None, "quality_used": None, "error": last_err}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("channel", help="channel dir name, slug, or path")
    ap.add_argument("--top", type=int, default=10, help="how many top-by-views (default 10)")
    ap.add_argument("--recent", type=int, default=6, help="how many most recent (default 6)")
    args = ap.parse_args()

    ch_dir = resolve_channel_dir(args.channel)
    videos_file = ch_dir / "videos.json"
    if not videos_file.exists():
        raise SystemExit(f"error: {videos_file} not found - run 01_collect.py first")

    payload = read_json(videos_file)
    selected, notes = select_sample(payload["videos"], args.top, args.recent)
    print(f"[fetch] selected {len(selected)} references from {payload['video_count']} videos")
    for n in notes:
        print(f"[fetch] note: {n}")

    refs_dir = ch_dir / "refs"
    results, failed = [], []
    for i, v in enumerate(selected, 1):
        r = download_thumbnail(v["video_id"], refs_dir)
        rec = {**v, **r}
        results.append(rec)
        if r["ok"]:
            print(
                f"[fetch] {i:>2}/{len(selected)}  {r['quality_used']:<14} "
                f"{r['width']}x{r['height']}  {v['title'][:44]}"
            )
        else:
            failed.append(v["video_id"])
            print(f"[fetch] {i:>2}/{len(selected)}  FAILED  {v['title'][:44]}  ({r['error']})")

    write_json(
        ch_dir / "refs" / "manifest.json",
        {
            "channel_name": payload.get("channel_name"),
            "sample_size": len(results),
            "ok_count": len([r for r in results if r["ok"]]),
            "failed": failed,
            "notes": notes,
            "references": results,
        },
    )
    print(f"[fetch] wrote {ch_dir / 'refs' / 'manifest.json'}")
    if failed:
        print(f"[fetch] WARNING: {len(failed)} downloads failed: {failed}")


if __name__ == "__main__":
    main()
