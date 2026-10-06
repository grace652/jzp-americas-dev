#!/usr/bin/env python3
"""Stage 1 - collect a channel's video list (id / title / views / age / duration).

Reads the channel's /videos page and parses the embedded `ytInitialData`.
This yields ~30 videos with view counts in ONE request, which is far faster
than asking yt-dlp for per-video metadata (yt-dlp's --flat-playlist returns
view_count as NA, and the channel "Popular" tab sort parameter is ignored).

Usage:
    python 01_collect.py "https://www.youtube.com/@SomeChannel/videos"
    python 01_collect.py @SomeChannel --out-dir channels/mychannel
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from _common import (
    CHANNELS_DIR,
    collect_strings,
    die,
    http_get,
    parse_age_days,
    parse_duration,
    parse_views,
    slugify,
    walk,
    write_json,
)


def normalize_channel_url(target: str) -> str:
    t = target.strip().strip('"').strip("'")
    if t.startswith("http://") or t.startswith("https://"):
        t = re.sub(r"^http://", "https://", t)
        t = re.sub(r"/+$", "", t)
        if not re.search(r"/(videos|shorts|streams|playlists)$", t):
            t = f"{t}/videos"
        return t
    handle = t if t.startswith("@") else f"@{t}"
    return f"https://www.youtube.com/{handle}/videos"


def channel_slug_from_url(url: str) -> str:
    """'https://www.youtube.com/@MrBeast/videos' -> 'mrbeast'."""
    m = re.search(r"youtube\.com/(@[^/]+|channel/[^/]+|c/[^/]+|user/[^/]+)", url)
    if not m:
        return slugify(url)
    raw = m.group(1)
    if raw.startswith("@"):
        return slugify(raw[1:])
    if raw.startswith("channel/"):
        # channel IDs are opaque; a short stable prefix keeps dirs readable
        return slugify(f"uc-{raw.split('/', 1)[1][:12]}")
    return slugify(raw.split("/", 1)[1])


def extract_yt_initial_data(html: str) -> dict:
    m = re.search(r"var ytInitialData\s*=\s*(\{.*?\});\s*</script>", html, re.S)
    if not m:
        m = re.search(r'window\["ytInitialData"\]\s*=\s*(\{.*?\});\s*</script>', html, re.S)
    if not m:
        die(
            "could not find ytInitialData in the channel page. "
            "The page may be a consent/blocked page, or YouTube changed its markup."
        )
    try:
        return json.loads(m.group(1))
    except json.JSONDecodeError as exc:
        die(f"ytInitialData was found but is not valid JSON: {exc}")


def extract_channel_name(html: str) -> str | None:
    m = re.search(r'<meta\s+property="og:title"\s+content="([^"]*)"', html)
    if m:
        return m.group(1).strip()
    m = re.search(r"<title>([^<]*)</title>", html)
    return m.group(1).replace(" - YouTube", "").strip() if m else None


def parse_lockup(lockup: dict) -> dict | None:
    video_id = lockup.get("contentId")
    if not video_id:
        return None

    meta = lockup.get("metadata", {}).get("lockupMetadataViewModel", {})
    title = (meta.get("title") or {}).get("content") or ""

    # metadata rows -> ["94M views", "9 days ago"]
    texts: list[str] = []
    rows = (
        meta.get("metadata", {})
        .get("contentMetadataViewModel", {})
        .get("metadataRows", [])
    )
    for row in rows:
        for part in row.get("metadataParts", []):
            t = (part.get("text") or {}).get("content")
            if isinstance(t, str):
                texts.append(t)

    views_text = next((t for t in texts if re.search(r"view", t, re.I)), None)
    age_text = next((t for t in texts if re.search(r"ago$", t, re.I)), None)

    # duration badge, e.g. "23:28"
    badge_texts: list[str] = []
    overlays = (
        lockup.get("contentImage", {})
        .get("thumbnailViewModel", {})
        .get("overlays", [])
    )
    for ov in overlays:
        collect_strings(ov.get("thumbnailBottomOverlayViewModel", {}), badge_texts)
    duration_text = next((t for t in badge_texts if parse_duration(t) is not None), None)

    return {
        "video_id": video_id,
        "title": title,
        "views_text": views_text,
        "views": parse_views(views_text),
        "age_text": age_text,
        "age_days": parse_age_days(age_text),
        "duration_text": duration_text,
        "duration_seconds": parse_duration(duration_text),
        "url": f"https://www.youtube.com/watch?v={video_id}",
        "thumbnail_url": f"https://i.ytimg.com/vi/{video_id}/maxresdefault.jpg",
    }


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("channel", help="channel URL, /channel/UC..., or @handle")
    ap.add_argument(
        "--out-dir",
        help="explicit output directory (default: channels/<slug>)",
    )
    args = ap.parse_args()

    url = normalize_channel_url(args.channel)
    print(f"[collect] fetching {url}")
    html = http_get(url).decode("utf-8", errors="ignore")
    print(f"[collect] got {len(html):,} bytes")

    data = extract_yt_initial_data(html)
    channel_name = extract_channel_name(html)

    videos, seen = [], set()
    for lockup in walk(data, "lockupViewModel"):
        rec = parse_lockup(lockup)
        if rec and rec["video_id"] not in seen:
            seen.add(rec["video_id"])
            videos.append(rec)

    if not videos:
        die("found ytInitialData but extracted 0 videos; markup may have changed")

    with_views = [v for v in videos if v["views"] is not None]
    print(f"[collect] extracted {len(videos)} videos ({len(with_views)} with view counts)")
    print(f"[collect] channel name: {channel_name!r}")

    out_dir = (
        Path(args.out_dir) if args.out_dir else CHANNELS_DIR / channel_slug_from_url(url)
    )
    out_dir.mkdir(parents=True, exist_ok=True)

    write_json(
        out_dir / "videos.json",
        {
            "source_url": url,
            "channel_name": channel_name,
            "channel_input": args.channel,
            "collected_at": __import__("datetime").datetime.now().isoformat(timespec="seconds"),
            "video_count": len(videos),
            "videos": videos,
        },
    )

    # maintain the multi-channel registry (planned extension point)
    registry_path = CHANNELS_DIR / "index.json"
    registry = {}
    if registry_path.exists():
        try:
            registry = json.loads(registry_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            registry = {}
    registry.setdefault("channels", {})[out_dir.name] = {
        "channel_name": channel_name,
        "source_url": url,
        "dir": str(out_dir),
        "video_count": len(videos),
    }
    write_json(registry_path, registry)

    print(f"[collect] wrote {out_dir / 'videos.json'}")
    print(f"[collect] channel dir -> {out_dir}")
    top = sorted(with_views, key=lambda v: v["views"], reverse=True)[:3]
    for v in top:
        print(f"           top: {v['views']:>12,}  {v['title'][:52]}")


if __name__ == "__main__":
    main()
