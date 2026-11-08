#!/usr/bin/env python3
"""Metricool'a henüz planlanmamış Türkçe postları listeler ya da planlananları işaretler.

python metricool_pending.py              -> planlanacak her post için JSON satırı: {meta, date, info}
python metricool_pending.py --mark META_PATH POST_ID   -> meta.json'a metricool_post_id yazar
"""
import json, sys
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent
TZ = ZoneInfo("Europe/Istanbul")

if len(sys.argv) == 4 and sys.argv[1] == "--mark":
    p = Path(sys.argv[2]); m = json.loads(p.read_text()); m["metricool_post_id"] = sys.argv[3]
    p.write_text(json.dumps(m, indent=2, ensure_ascii=False) + "\n"); sys.exit(0)

now = datetime.now(TZ)
for p in sorted(ROOT.glob("posts-tr/*/post-*/meta.json")):
    m = json.loads(p.read_text())
    if m.get("metricool_post_id"):
        continue
    when = datetime.fromisoformat(m["publish_local"]).replace(tzinfo=TZ)
    if when < now + timedelta(minutes=15):
        continue
    info = {
        "autoPublish": True, "draft": False, "descendants": [], "firstCommentText": "",
        "hasNotReadNotes": False, "media": m["images"], "mediaAltText": [],
        "providers": [{"network": "tiktok"}],
        "publicationDate": {"dateTime": m["publish_local"], "timezone": "Europe/Istanbul"},
        "shortener": False, "smartLinkData": {"ids": []}, "text": m["caption"],
        "tiktokData": {"disableComment": False, "disableDuet": False, "disableStitch": False,
                        "privacyOption": "PUBLIC_TO_EVERYONE", "commercialContentThirdParty": False,
                        "commercialContentOwnBrand": False, "title": m["title"],
                        "autoAddMusic": True, "photoCoverIndex": 0},
    }
    print(json.dumps({"meta": str(p.relative_to(ROOT)), "date": when.isoformat(), "info": json.dumps(info, ensure_ascii=False)}, ensure_ascii=False))
