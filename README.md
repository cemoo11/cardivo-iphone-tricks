# Cardivo — daily iPhone tricks for TikTok

Every day a GitHub Action generates **3 TikTok photo carousels** (3–8 slides each) about iPhone features, commits them to [`posts/`](posts/) and schedules them on Buffer at peak US TikTok hours (US Eastern).

- Slides: 1080×1920, grainy gradient backgrounds, cover + tips + a Cardivo slide.
- A single tip is used in at most **3 posts within any 14-day window**.
- Captions are freshly combined every post (US search-friendly hooks, extra iPhone tricks, how to download Cardivo, hashtags) and never mention health topics.
- Posting times (ET): Mon 8/13/20 · Tue 7/13/22 · Wed 6/13/21 · Thu 6/13/22 · Fri 13/18/22 · Sat 11/15/17 · Sun 9/13/19.

## Get Cardivo

Open the App Store on your iPhone, search **"Cardivo"** and tap **Get** — or go to <https://apps.apple.com/app/id6793211638>.

## Run locally

```bash
pip install -r requirements.txt
python generate.py --date 2026-11-05          # writes posts/2026-11-05/post-{1,2,3}
python schedule_buffer.py --date 2026-11-05 --dry-run
```

## Setup (one time)

- Repo secret `BUFFER_API_KEY` — from publish.buffer.com/settings/api
- Repo variable `BUFFER_CHANNEL_ID` — the Buffer TikTok channel id

Fonts: Inter (SIL Open Font License) is downloaded during the workflow.
