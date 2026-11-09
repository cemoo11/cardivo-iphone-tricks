#!/usr/bin/env python3
"""Generate the day's TikTok carousel posts for every English Buffer account.

Usage: python generate.py [--date YYYY-MM-DD] [--force] [--account main|ny]
Accounts (see ACCOUNTS):
  main -> posts/<date>/post-<n>/     (cardivo.ai), history in state/history.json
  ny   -> posts/<date>/ny-post-<n>/  (cemalsatis, New York audience, longer carousels),
          history in state/history_ny.json
Dates are US Eastern dates; posts are timed for peak New York / US TikTok hours.
"""
import argparse
import json
import random
import shutil
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

from cardivo_posts import render
from cardivo_posts.captions import build_caption
from cardivo_posts.tips import THEMES, TIPS, TIP_BY_ID

ROOT = Path(__file__).resolve().parent
ET = ZoneInfo("America/New_York")
REPO = "cemoo11/cardivo-iphone-tricks"
RAW_BASE = f"https://raw.githubusercontent.com/{REPO}/main"

# Peak US TikTok hours (Eastern), Mon=0. Based on Buffer's 2026 analysis of 7M posts,
# spread out so posts are at least 2 hours apart.
SLOTS = {
    0: ["08:00", "13:00", "20:00"],
    1: ["07:00", "13:00", "22:00"],
    2: ["06:00", "13:00", "21:00"],
    3: ["06:00", "13:00", "22:00"],
    4: ["13:00", "18:00", "22:00"],
    5: ["11:00", "15:00", "17:00"],
    6: ["09:00", "13:00", "19:00"],
}

MAX_USES = 3          # a tip can appear in at most 3 posts...
WINDOW_DAYS = 14      # ...within any 14-day window
TIP_COUNT_WEIGHTS = {1: 1, 2: 2, 3: 4, 4: 5, 5: 4, 6: 2}  # slides = tips + cover + Cardivo (3-8)

COVER_MANY = [
    ("hidden iPhone {label}features you're not using", "Swipe →  and save it for later"),
    ("iPhone {label}tricks you need to know", "Swipe →  you'll use these daily"),
    ("iPhone {label}hacks nobody told you about", "Save this before you forget"),
    ("{label}settings to change on your iPhone right now", "Swipe →  takes 2 minutes"),
    ("underrated iPhone {label}features", "Swipe →  and try them today"),
]
COVER_ONE = [
    ("iPhone {label}trick you need to know", "Swipe →  and try it now"),
    ("hidden iPhone {label}feature nobody uses", "Swipe →  to see it"),
]
CARDIVO_SLIDES = [
    ("BONUS", "Check your heart rate with just your camera",
     "Place your fingertip on the back camera and Cardivo reads your pulse in seconds. No watch needed."),
    ("ONE MORE", "Your iPhone camera can read your pulse",
     "Cardivo turns your camera into a heart rate monitor. Just cover the lens with your fingertip."),
    ("PRO TIP", "Measure your heart rate without a smartwatch",
     "Open Cardivo, place a finger on the camera and get your BPM in about 30 seconds."),
    ("BONUS", "Turn your iPhone into a heart rate monitor",
     "Cardivo uses your camera and flash to measure your heart rate and track it over time."),
]


# Second English account: New York audience. Commute / lunch / evening scroll times (ET),
# deliberately offset from the main account's slots.
NY_SLOTS = {
    0: ["07:30", "12:30", "19:30"],
    1: ["08:30", "12:30", "20:30"],
    2: ["07:30", "17:30", "21:30"],
    3: ["08:30", "12:30", "20:30"],
    4: ["07:30", "12:30", "19:30"],
    5: ["10:30", "14:30", "20:30"],
    6: ["10:30", "16:30", "20:30"],
}
NY_TIP_COUNT_WEIGHTS = {5: 3, 6: 4, 7: 3, 8: 1}  # longer carousels: 7-10 slides

NY_COVER_MANY = [
    ("iPhone {label}tricks every New Yorker should know", "Swipe →  perfect for your commute"),
    ("iPhone {label}hacks for your NYC subway ride", "Swipe →  try them before your stop"),
    ("hidden iPhone {label}features NYC needs to know", "Save this for your next train ride"),
    ("iPhone {label}tricks I learned living in New York", "Swipe →  you'll use these daily"),
    ("{label}settings every New Yorker should change today", "Swipe →  takes 2 minutes"),
    ("iPhone {label}hacks for busy New Yorkers", "Swipe →  and save it for later"),
    ("iPhone {label}features your NYC friends don't know", "Send this to your roommate"),
]
NY_CARDIVO_SLIDES = [
    ("BONUS", "Check your heart rate with just your camera",
     "Waiting for the train? Place your fingertip on the back camera and Cardivo reads your pulse in seconds."),
    ("ONE MORE", "Your iPhone camera can read your pulse",
     "Cardivo turns your camera into a heart rate monitor. Cover the lens with a fingertip and you're done."),
    ("PRO TIP", "No smartwatch? No problem",
     "Open Cardivo, place a finger on the camera and get your BPM in about 30 seconds, anywhere in the city."),
]

ACCOUNTS = {
    "main": {
        "history": ROOT / "state" / "history.json",
        "prefix": "post-",
        "slots": SLOTS,
        "weights": TIP_COUNT_WEIGHTS,
        "cover_many": COVER_MANY,
        "cardivo": CARDIVO_SLIDES,
        "caption_style": "us",
        "seed": 7919,
    },
    "ny": {
        "history": ROOT / "state" / "history_ny.json",
        "prefix": "ny-post-",
        "slots": NY_SLOTS,
        "weights": NY_TIP_COUNT_WEIGHTS,
        "cover_many": NY_COVER_MANY,
        "cardivo": NY_CARDIVO_SLIDES,
        "caption_style": "ny",
        "seed": 104729,
    },
}


def load_history(acc):
    h = acc["history"]
    return json.loads(h.read_text()) if h.exists() else {"posts": []}


def recent_uses(history, day: date):
    start = day - timedelta(days=WINDOW_DAYS - 1)
    counts = {}
    for p in history["posts"]:
        d = date.fromisoformat(p["date"])
        if start <= d <= day:
            for t in p["tips"]:
                counts[t] = counts.get(t, 0) + 1
    return counts


def pick_tips(rng, history, day, used_today, used_themes, weights, avoid=()):
    counts = recent_uses(history, day)
    for t in used_today:
        counts[t] = counts.get(t, 0) + 1
    available = [t for t in TIPS if counts.get(t[0], 0) < MAX_USES and t[0] not in used_today]
    fresh = [t for t in available if t[0] not in avoid]  # prefer tips the other account isn't posting today
    k = rng.choices(list(weights), weights=list(weights.values()))[0]
    if len(fresh) >= k:
        available = fresh

    themes = [th for th in THEMES if th not in used_themes]
    rng.shuffle(themes)
    for th in themes + ["mixed"]:
        pool = available if th == "mixed" else [t for t in available if t[1] == th]
        if len(pool) >= k:
            return th, rng.sample(pool, k)
    # bank exhausted for this window: fall back to least-used tips
    pool = sorted(TIPS, key=lambda t: counts.get(t[0], 0))[: max(k, 1)]
    return "mixed", pool


def build_post(rng, acc, day, n, slot, theme, tips, part_no, out_dir: Path):
    label = "" if theme == "mixed" else THEMES[theme] + " "
    k = len(tips)
    options = acc["cover_many"] if k > 1 else COVER_ONE
    if theme == "settings":  # avoid "settings settings"
        options = [o for o in options if "{label}settings" not in o[0]]
    headline, sub = rng.choice(options)
    if theme == "settings" and "features" in headline:  # avoid "settings features"
        label = ""
    headline = headline.format(label=label)
    total = k + 2
    seed0 = int(day.strftime("%Y%m%d")) * 10 + n * 100 + rng.randint(0, 99)

    out_dir.mkdir(parents=True, exist_ok=True)
    slides = [render.cover(seed0, str(k), headline, sub, 1, total)]
    for i, (_, _, title, body, path) in enumerate(tips, start=1):
        slides.append(render.tip(seed0 + i, i, title, body, path, i + 1, total))
    lab, h, b = rng.choice(acc["cardivo"])
    slides.append(render.cardivo(seed0 + 50, lab, h, b, total, total))

    names = []
    for i, im in enumerate(slides, start=1):
        name = f"{i:02d}.jpg"
        im.save(out_dir / name, quality=88)
        names.append(name)

    caption = build_caption(rng, part_no, acc["caption_style"])
    title = f"{k} {headline}"[:90]
    local = datetime.combine(day, datetime.strptime(slot, "%H:%M").time(), ET)
    rel = out_dir.relative_to(ROOT).as_posix()
    meta = {
        "date": day.isoformat(),
        "account": acc["name"],
        "post": n,
        "theme": theme,
        "tips": [t[0] for t in tips],
        "slides": len(names),
        "title": title,
        "caption": caption,
        "slot_et": local.isoformat(),
        "due_at_utc": local.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z"),
        "images": [f"{RAW_BASE}/{rel}/{x}" for x in names],
        "buffer_post_id": None,
    }
    (out_dir / "caption.txt").write_text(caption + "\n")
    (out_dir / "meta.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n")
    return meta


def generate_day(name: str, day: date, force: bool, avoid=()):
    """Generate one account's posts for a day. Returns the tip ids used that day."""
    acc = dict(ACCOUNTS[name], name=name)
    history = load_history(acc)
    day_dir = ROOT / "posts" / day.isoformat()
    existing = [p for p in history["posts"] if p["date"] == day.isoformat()]
    if existing:
        if not force:
            print(f"{name} {day} already generated; skipping")
            return [t for p in existing for t in p["tips"]]
        history["posts"] = [p for p in history["posts"] if p["date"] != day.isoformat()]
        for d in day_dir.glob(acc["prefix"] + "*"):
            shutil.rmtree(d, ignore_errors=True)

    rng = random.Random(day.toordinal() * acc["seed"])
    used_today, used_themes = [], []
    part_no = len(history["posts"])
    for n, slot in enumerate(acc["slots"][day.weekday()], start=1):
        theme, tips = pick_tips(rng, history, day, used_today, used_themes, acc["weights"], avoid)
        used_today += [t[0] for t in tips]
        used_themes.append(theme)
        part_no += 1
        meta = build_post(rng, acc, day, n, slot, theme, tips, part_no, day_dir / f"{acc['prefix']}{n}")
        history["posts"].append({"date": meta["date"], "post": n, "theme": theme, "tips": meta["tips"]})
        print(f"{name} {day} post {n}: {theme}, {meta['slides']} slides, {slot} ET")

    acc["history"].write_text(json.dumps(history, indent=2) + "\n")
    return used_today


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", help="US Eastern date (default: today and tomorrow in ET)")
    ap.add_argument("--force", action="store_true", help="regenerate even if the day exists")
    ap.add_argument("--account", choices=list(ACCOUNTS), help="only this account (default: all)")
    args = ap.parse_args()
    if args.date:
        days = [date.fromisoformat(args.date)]
    else:
        # GitHub cron often starts hours late, so always prepare tomorrow too:
        # tomorrow's early-morning slots get scheduled well in advance.
        today = datetime.now(ET).date()
        days = [today, today + timedelta(days=1)]
    names = [args.account] if args.account else list(ACCOUNTS)
    for d in days:
        used = []
        for name in names:
            used += generate_day(name, d, args.force, avoid=set(used))


if __name__ == "__main__":
    main()
