#!/usr/bin/env python3
"""Türkçe günlük 3 TikTok carousel'i üretir (3-7 slayt, büyük sayılar, sonda Cardivo indirme sayfası).

Kullanım: python generate_tr.py [--date YYYY-MM-DD] [--days N] [--force]
Çıktı: posts-tr/<tarih>/post-<n>/ (slaytlar, caption.txt, meta.json); geçmiş: state/history_tr.json
Saatler Türkiye saatiyle (Europe/Istanbul).
"""
import argparse
import json
import random
import shutil
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

from cardivo_posts import render
from cardivo_posts.captions_tr import build_caption_tr
from cardivo_posts.tips_tr import THEMES_TR, TIPS_TR

ROOT = Path(__file__).resolve().parent
HISTORY = ROOT / "state" / "history_tr.json"
TZ = ZoneInfo("Europe/Istanbul")
RAW_BASE = "https://raw.githubusercontent.com/cemoo11/cardivo-iphone-tricks/main"

# Türkiye'de TikTok'un en yoğun saatleri: öğle arası, iş çıkışı, akşam prime time.
SLOTS = {
    0: ["12:30", "18:30", "21:30"],
    1: ["12:30", "18:30", "21:30"],
    2: ["12:30", "18:30", "21:30"],
    3: ["12:30", "18:30", "21:30"],
    4: ["12:30", "19:00", "22:00"],
    5: ["11:00", "16:00", "21:30"],
    6: ["11:00", "16:00", "21:00"],
}

MAX_USES, WINDOW_DAYS = 3, 14
TIP_COUNT_WEIGHTS = {1: 1, 2: 3, 3: 5, 4: 4, 5: 3}  # slayt = kapak + ipuçları + Cardivo => 3-7

COVERS = [
    ("gizli iPhone {label}özelliği", "Kaydır → ve kaydet"),
    ("iPhone'da kimsenin bilmediği {label}özellik", "Kaydır → sonuncusu çok iyi"),
    ("Apple'ın söylemediği iPhone {label}taktiği", "Kaydır → hemen dene"),
    ("iPhone'unda hemen açman gereken {label}özellik", "Kaydır → 2 dakikanı alır"),
    ("iPhone {label}hilesi: herkes bilmeli", "Kaydır → ve arkadaşına gönder"),
]
CTA_SLIDES = [
    ("SON TAKTİK", "Nabzını sadece kamerayla ölç", "Parmağını arka kameraya koy, Cardivo nabzını saniyeler içinde ölçsün. Saat gerekmez."),
    ("BONUS", "iPhone'un bir nabız ölçere dönüşüyor", "Cardivo kamera ve flaşla kalp atışını ölçer, sonuçlarını kaydeder."),
    ("HEMEN İNDİR", "Akıllı saatsiz nabız ölçümü", "Cardivo ile 30 saniyede nabzını ölç, gelişimini grafiklerle takip et."),
]


def load_history():
    return json.loads(HISTORY.read_text()) if HISTORY.exists() else {"posts": []}


def pick(rng, history, day, used_today, used_themes):
    start = day - timedelta(days=WINDOW_DAYS - 1)
    counts = {}
    for p in history["posts"]:
        if start <= date.fromisoformat(p["date"]) <= day:
            for t in p["tips"]:
                counts[t] = counts.get(t, 0) + 1
    avail = [t for t in TIPS_TR if counts.get(t[0], 0) < MAX_USES and t[0] not in used_today]
    k = rng.choices(list(TIP_COUNT_WEIGHTS), weights=list(TIP_COUNT_WEIGHTS.values()))[0]
    themes = [th for th in THEMES_TR if th not in used_themes]
    rng.shuffle(themes)
    for th in themes + ["mixed"]:
        pool = avail if th == "mixed" else [t for t in avail if t[1] == th]
        if len(pool) >= k:
            return th, rng.sample(pool, k)
    return "mixed", sorted(TIPS_TR, key=lambda t: counts.get(t[0], 0))[:k]


def make_post(rng, day, n, slot, theme, tips, part_no, out: Path):
    label = "" if theme == "mixed" else THEMES_TR[theme]
    k = len(tips)
    headline, sub = rng.choice(COVERS)
    headline = headline.format(label=label)
    total = k + 2
    seed0 = int(day.strftime("%Y%m%d")) * 10 + n * 1000 + rng.randint(0, 999)
    out.mkdir(parents=True, exist_ok=True)
    slides = [render.cover_big(seed0, str(k), headline, sub, 1, total)]
    for i, (_, _, title, body, path) in enumerate(tips, 1):
        slides.append(render.tip_big(seed0 + i, i, title, body, path, i + 1, total))
    slides.append(render.cardivo_cta_tr(seed0 + 77, *rng.choice(CTA_SLIDES), total, total))
    names = []
    for i, im in enumerate(slides, 1):
        names.append(f"{i:02d}.jpg")
        im.save(out / names[-1], quality=88)
    caption = build_caption_tr(rng, part_no)
    local = datetime.combine(day, datetime.strptime(slot, "%H:%M").time())
    rel = out.relative_to(ROOT).as_posix()
    meta = {
        "date": day.isoformat(), "post": n, "theme": theme, "tips": [t[0] for t in tips],
        "slides": len(names), "title": f"{k} {headline}"[:90], "caption": caption,
        "publish_local": local.strftime("%Y-%m-%dT%H:%M:%S"), "timezone": "Europe/Istanbul",
        "images": [f"{RAW_BASE}/{rel}/{x}" for x in names], "metricool_post_id": None,
    }
    (out / "caption.txt").write_text(caption + "\n")
    (out / "meta.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n")
    return meta


def generate_day(day: date, force: bool):
    history = load_history()
    day_dir = ROOT / "posts-tr" / day.isoformat()
    if any(p["date"] == day.isoformat() for p in history["posts"]):
        if not force:
            print(f"{day} zaten üretilmiş; atlanıyor")
            return
        history["posts"] = [p for p in history["posts"] if p["date"] != day.isoformat()]
        shutil.rmtree(day_dir, ignore_errors=True)
    rng = random.Random(day.toordinal() * 104729)
    used_today, used_themes = [], []
    part_no = len(history["posts"])
    for n, slot in enumerate(SLOTS[day.weekday()], 1):
        theme, tips = pick(rng, history, day, used_today, used_themes)
        used_today += [t[0] for t in tips]
        used_themes.append(theme)
        part_no += 1
        m = make_post(rng, day, n, slot, theme, tips, part_no, day_dir / f"post-{n}")
        history["posts"].append({"date": m["date"], "post": n, "theme": theme, "tips": m["tips"]})
        print(f"{day} post {n}: {theme}, {m['slides']} slayt, {slot}")
    HISTORY.write_text(json.dumps(history, indent=2) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date")
    ap.add_argument("--days", type=int, default=1, help="kaç gün üretilecek (bugünden itibaren)")
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()
    start = date.fromisoformat(a.date) if a.date else datetime.now(TZ).date()
    for i in range(a.days):
        generate_day(start + timedelta(days=i), a.force)


if __name__ == "__main__":
    main()
