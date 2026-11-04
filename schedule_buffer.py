#!/usr/bin/env python3
"""Schedule a day's generated posts on Buffer (TikTok) via the Buffer GraphQL API.

Env: BUFFER_API_KEY (required), BUFFER_CHANNEL_ID (TikTok channel id).
Usage: python schedule_buffer.py [--date YYYY-MM-DD] [--dry-run]
Images must already be pushed to the public repo (raw.githubusercontent.com URLs).
"""
import argparse
import json
import os
import sys
import time
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent
API = "https://api.buffer.com"
ET = ZoneInfo("America/New_York")


def gql(query: str, key: str):
    req = urllib.request.Request(
        API,
        data=json.dumps({"query": query}).encode(),
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json",
                 "User-Agent": "cardivo-iphone-tricks/1.0"},
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        body = json.loads(r.read())
    if body.get("errors"):
        raise RuntimeError(json.dumps(body["errors"]))
    return body["data"]


def wait_public(url: str, tries: int = 20):
    for _ in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, method="HEAD"), timeout=20) as r:
                if r.status == 200:
                    return
        except Exception:
            pass
        time.sleep(6)
    raise RuntimeError(f"image not reachable: {url}")


def s(v: str) -> str:
    return json.dumps(v, ensure_ascii=False)  # JSON string literal == valid GraphQL string


def create_post(meta: dict, channel: str, key: str) -> str:
    assets = " ".join("{ image: { url: %s } }" % s(u) for u in meta["images"])
    q = f"""
    mutation {{
      createPost(input: {{
        text: {s(meta["caption"])}
        channelId: {s(channel)}
        schedulingType: automatic
        mode: customScheduled
        dueAt: {s(meta["due_at_utc"])}
        assets: [{assets}]
        metadata: {{ tiktok: {{ title: {s(meta["title"])} }} }}
      }}) {{
        ... on PostActionSuccess {{ post {{ id dueAt }} }}
        ... on MutationError {{ message }}
      }}
    }}"""
    res = gql(q, key)["createPost"]
    if "post" not in res:
        raise RuntimeError(res.get("message", str(res)))
    return res["post"]["id"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    day = args.date or datetime.now(ET).date().isoformat()
    key = os.environ.get("BUFFER_API_KEY", "")
    channel = os.environ.get("BUFFER_CHANNEL_ID", "")
    if not args.dry_run and not (key and channel):
        sys.exit("BUFFER_API_KEY and BUFFER_CHANNEL_ID must be set")

    failed = False
    for meta_path in sorted((ROOT / "posts" / day).glob("post-*/meta.json")):
        meta = json.loads(meta_path.read_text())
        if meta.get("buffer_post_id"):
            print(f"{meta_path.parent.name}: already scheduled ({meta['buffer_post_id']})")
            continue
        due = datetime.strptime(meta["due_at_utc"], "%Y-%m-%dT%H:%M:%S.000Z").replace(tzinfo=timezone.utc)
        if due < datetime.now(timezone.utc) + timedelta(minutes=10):
            print(f"{meta_path.parent.name}: slot {meta['slot_et']} already passed; skipping")
            continue
        if args.dry_run:
            print(f"{meta_path.parent.name}: would schedule {len(meta['images'])} slides at {meta['slot_et']}")
            continue
        try:
            for u in meta["images"]:
                wait_public(u)
            meta["buffer_post_id"] = create_post(meta, channel, key)
            meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n")
            print(f"{meta_path.parent.name}: scheduled for {meta['slot_et']} ({meta['buffer_post_id']})")
        except Exception as e:  # keep going with the other posts
            failed = True
            print(f"{meta_path.parent.name}: FAILED: {e}", file=sys.stderr)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
