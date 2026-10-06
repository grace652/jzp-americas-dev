"""Shared helpers for the YouTube thumbnail style distillation pipeline.

Only the Python standard library is used here; Pillow is used in 03/05.
"""
from __future__ import annotations

import json
import os
import re
import sys
import unicodedata
import urllib.error
import urllib.request
from pathlib import Path

# The scripts are portable (they ship inside the skill). Outputs land wherever
# you run them from, unless THUMBNAIL_DISTILLER_HOME overrides it.
ROOT = Path(os.environ.get("THUMBNAIL_DISTILLER_HOME") or Path.cwd()).resolve()
CHANNELS_DIR = ROOT / "channels"
OUT_DIR = ROOT / "out"
PROMPTS_DIR = OUT_DIR / "prompts"

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)

VIEW_UNITS = {"": 1, "K": 1_000, "M": 1_000_000, "B": 1_000_000_000}
AGE_UNITS_DAYS = {
    "second": 1 / 86400,
    "minute": 1 / 1440,
    "hour": 1 / 24,
    "day": 1,
    "week": 7,
    "month": 30.44,
    "year": 365.25,
}


# --------------------------------------------------------------------------- #
# small utilities
# --------------------------------------------------------------------------- #
def die(msg: str, code: int = 1):
    print(f"error: {msg}", file=sys.stderr)
    raise SystemExit(code)


def slugify(text: str) -> str:
    """Filesystem-safe slug that keeps CJK characters readable."""
    text = unicodedata.normalize("NFKC", text or "").strip()
    text = re.sub(r"^https?://", "", text)
    text = re.sub(r"[^\w\u4e00-\u9fff\-]+", "-", text, flags=re.UNICODE)
    text = re.sub(r"-{2,}", "-", text).strip("-")
    return text.lower()[:60] or "channel"


def write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def read_json(path: Path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def http_get(url: str, timeout: int = 30) -> bytes:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept-Language": "en-US,en;q=0.9",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def parse_views(text: str | None) -> int | None:
    """'94M views' -> 94000000, '1,234 views' -> 1234, 'No views' -> 0."""
    if not text:
        return None
    if re.search(r"\bno views\b", text, re.I):
        return 0
    m = re.search(r"([\d][\d.,]*)\s*([KMB]?)\s*view", text, re.I)
    if not m:
        return None
    num = m.group(1).replace(",", "")
    unit = (m.group(2) or "").upper()
    try:
        value = float(num)
    except ValueError:
        return None
    return int(value * VIEW_UNITS.get(unit, 1))


def parse_age_days(text: str | None) -> float | None:
    """'9 days ago' -> 9.0, '2 weeks ago' -> 14.0, 'Premiered 5 hours ago' -> 0.208."""
    if not text:
        return None
    m = re.search(r"(\d+)\s*(second|minute|hour|day|week|month|year)s?\s*ago", text, re.I)
    if not m:
        return None
    return round(int(m.group(1)) * AGE_UNITS_DAYS[m.group(2).lower()], 4)


def parse_duration(text: str | None) -> int | None:
    """'23:28' -> 1408 seconds. Returns None when not a plain duration badge."""
    if not text or not re.fullmatch(r"\d{1,2}:\d{2}(:\d{2})?", text.strip()):
        return None
    parts = [int(p) for p in text.strip().split(":")]
    seconds = 0
    for p in parts:
        seconds = seconds * 60 + p
    return seconds


def resolve_channel_dir(channel: str) -> Path:
    """Accept a slug, a handle, or a URL and return the matching channel dir."""
    candidate = CHANNELS_DIR / channel
    if candidate.is_dir():
        return candidate
    slug = slugify(channel)
    candidate = CHANNELS_DIR / slug
    if candidate.is_dir():
        return candidate
    # fall back to substring match against channel dirs
    for d in sorted(CHANNELS_DIR.iterdir()) if CHANNELS_DIR.exists() else []:
        if d.is_dir() and slug and (slug in d.name or d.name in slug):
            return d
    die(f"no channel directory matches {channel!r} under {CHANNELS_DIR}")


def walk(obj, key: str):
    """Yield every value stored under `key` anywhere in a nested dict/list."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == key:
                yield v
            yield from walk(v, key)
    elif isinstance(obj, list):
        for item in obj:
            yield from walk(item, key)


def collect_strings(obj, out: list[str]):
    """Collect every {'content': <str>} value, in document order."""
    if isinstance(obj, dict):
        c = obj.get("content")
        if isinstance(c, str):
            out.append(c)
        for v in obj.values():
            collect_strings(v, out)
    elif isinstance(obj, list):
        for item in obj:
            collect_strings(item, out)
    return out
