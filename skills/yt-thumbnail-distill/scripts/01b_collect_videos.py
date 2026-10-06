#!/usr/bin/env python3
"""Stage 1 (variant) - collect specific videos by URL instead of a whole channel.

Use this when the user points at a handful of particular videos whose covers
they like, rather than wanting a channel-wide style read.

Writes the same videos.json shape as 01_collect.py, so 02_fetch.py and the rest
of the pipeline work unchanged.

Usage:
    python 01b_collect_videos.py <url> [<url> ...] --name my-style
    python 01b_collect_videos.py --from-file urls.txt --name my-style
"""
from __future__ import annotations

import argparse
import datetime
import re
import subprocess
import sys
from pathlib import Path

from _common import CHANNELS_DIR, die, slugify, write_json

FIELDS = [
    "id",
    "title",
    "view_count",
    "upload_date",
    "duration",
    "channel",
    "uploader",
    "webpage_url",
]


def extract_video_id(url: str) -> str | None:
    """Accept full URLs (with extra query params), youtu.be links, or a bare id."""
    url = url.strip()
    if re.fullmatch(r"[A-Za-z0-9_-]{11}", url):
        return url
    for pattern in (
        r"[?&]v=([A-Za-z0-9_-]{11})",
        r"youtu\.be/([A-Za-z0-9_-]{11})",
        r"/shorts/([A-Za-z0-9_-]{11})",
        r"/embed/([A-Za-z0-9_-]{11})",
    ):
        m = re.search(pattern, url)
        if m:
            return m.group(1)
    return None


def fmt_duration(seconds: int | None) -> str | None:
    if not seconds:
        return None
    h, rem = divmod(int(seconds), 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def probe(url: str) -> tuple[dict | None, str | None]:
    cmd = [
        "yt-dlp", "--no-warnings", "--skip-download", "--no-playlist",
        "--print", "\t".join(f"%({f})s" for f in FIELDS), url,
    ]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    except subprocess.TimeoutExpired:
        return None, "yt-dlp timed out"
    if proc.returncode != 0:
        return None, (proc.stderr.strip().splitlines() or ["yt-dlp failed"])[-1]

    line = (proc.stdout.strip().splitlines() or [""])[0]
    parts = line.split("\t")
    if len(parts) < len(FIELDS):
        return None, f"unexpected yt-dlp output: {line[:120]!r}"

    raw = dict(zip(FIELDS, parts))
    if not raw.get("id") or raw["id"] == "NA":
        return None, "no video id returned"

    views = None
    if raw.get("view_count") and raw["view_count"] != "NA":
        try:
            views = int(raw["view_count"])
        except ValueError:
            views = None

    age_days = None
    upload_date = raw.get("upload_date")
    if upload_date and re.fullmatch(r"\d{8}", upload_date):
        d = datetime.date(int(upload_date[:4]), int(upload_date[4:6]), int(upload_date[6:]))
        age_days = round((datetime.date.today() - d).days, 4)

    duration_s = None
    if raw.get("duration") and raw["duration"] != "NA":
        try:
            duration_s = int(float(raw["duration"]))
        except ValueError:
            duration_s = None

    def human(n: int | None) -> str | None:
        if n is None:
            return None
        if n >= 1_000_000_000:
            return f"{n / 1_000_000_000:.1f}B views"
        if n >= 1_000_000:
            return f"{n / 1_000_000:.0f}M views"
        if n >= 1_000:
            return f"{n / 1_000:.0f}K views"
        return f"{n:,} views"

    return {
        "video_id": raw["id"],
        "title": raw.get("title") or "",
        "views_text": human(views),
        "views": views,
        "age_text": f"{age_days:.0f} days ago" if age_days is not None else None,
        "age_days": age_days,
        "duration_text": fmt_duration(duration_s),
        "duration_seconds": duration_s,
        "url": raw.get("webpage_url") or f"https://www.youtube.com/watch?v={raw['id']}",
        "thumbnail_url": f"https://i.ytimg.com/vi/{raw['id']}/maxresdefault.jpg",
        "channel_name": raw.get("channel") if raw.get("channel") != "NA" else None,
        "uploader": raw.get("uploader") if raw.get("uploader") != "NA" else None,
    }, None


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("urls", nargs="*", help="video URLs or bare video IDs")
    ap.add_argument("--from-file", help="file containing one URL per line")
    ap.add_argument("--name", help="output slug (default: derived from the channel name)")
    args = ap.parse_args()

    urls = list(args.urls)
    if args.from_file:
        urls += [
            ln.strip()
            for ln in Path(args.from_file).read_text(encoding="utf-8").splitlines()
            if ln.strip() and not ln.strip().startswith("#")
        ]
    if not urls:
        die("no URLs given (pass them as arguments or use --from-file)")

    videos, failed, channel_name = [], [], None
    for i, url in enumerate(urls, 1):
        vid = extract_video_id(url)
        target = f"https://www.youtube.com/watch?v={vid}" if vid else url
        print(f"[videos] {i}/{len(urls)} probing {vid or url}")
        rec, err = probe(target)
        if not rec:
            failed.append({"url": url, "error": err})
            print(f"[videos]   FAILED: {err}")
            continue
        channel_name = channel_name or rec.get("channel_name")
        videos.append(rec)
        print(
            f"[videos]   ok  {rec['video_id']}  {rec['views_text'] or 'n/a':>12}  "
            f"{rec['title'][:46]}"
        )

    if not videos:
        die("no videos could be collected")

    slug = args.name or slugify(channel_name or "custom-set")
    out_dir = CHANNELS_DIR / slug
    out_dir.mkdir(parents=True, exist_ok=True)

    write_json(
        out_dir / "videos.json",
        {
            "source_url": "user-specified video list",
            "source_kind": "explicit_videos",
            "channel_name": channel_name or slug,
            "channel_input": args.urls,
            "collected_at": datetime.datetime.now().isoformat(timespec="seconds"),
            "video_count": len(videos),
            "failed": failed,
            "videos": videos,
        },
    )

    registry_path = CHANNELS_DIR / "index.json"
    registry = {}
    if registry_path.exists():
        try:
            import json as _json

            registry = _json.loads(registry_path.read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001
            registry = {}
    registry.setdefault("channels", {})[slug] = {
        "channel_name": channel_name or slug,
        "source_url": "user-specified video list",
        "source_kind": "explicit_videos",
        "dir": str(out_dir),
        "video_count": len(videos),
    }
    write_json(registry_path, registry)

    print()
    print(f"[videos] wrote {out_dir / 'videos.json'}  ({len(videos)} videos)")
    if failed:
        print(f"[videos] WARNING: {len(failed)} failed: {[f['url'] for f in failed]}")
    print(f"[videos] next: 02_fetch.py {slug} --top {len(videos)} --recent {len(videos)}")


if __name__ == "__main__":
    main()
