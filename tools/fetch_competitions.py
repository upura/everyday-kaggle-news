#!/usr/bin/env python3
"""開催中の Kaggle コンペのうちメダル対象のものを docs/competitions.json に書き出す。

Kaggle API (https://www.kaggle.com/api/v1/competitions/list) を標準ライブラリのみで叩き、
awardsPoints(メダル・ポイント付与のランク対象コンペ)が偽のものは除外する。
認証情報は次の順で読む(KGAT_ で始まる新形式トークンは Bearer、従来の username/key は Basic):
KAGGLE_API_TOKEN → KAGGLE_USERNAME / KAGGLE_KEY → ~/.kaggle/kaggle.json
docs/calendar.md がこの JSON を読み込んでタイムライン表示する。

Usage: python3 tools/fetch_competitions.py [output.json]
"""

import base64
import json
import os
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

API_BASE = "https://www.kaggle.com/api/v1/competitions/list"
# タイムラインに載せる締切の上限(これより先はロングラン・常設扱い)
LONG_RUNNING_DAYS = 400


def auth_header():
    token = os.environ.get("KAGGLE_API_TOKEN")
    if token:
        return f"Bearer {token}"
    username = os.environ.get("KAGGLE_USERNAME")
    key = os.environ.get("KAGGLE_KEY")
    if not (username and key):
        cred_path = Path.home() / ".kaggle" / "kaggle.json"
        if cred_path.exists():
            with open(cred_path) as f:
                cred = json.load(f)
            username, key = cred.get("username"), cred.get("key")
    if key and key.startswith("KGAT_"):
        return f"Bearer {key}"
    if username and key:
        basic = base64.b64encode(f"{username}:{key}".encode()).decode()
        return f"Basic {basic}"
    raise SystemExit(
        "Kaggle API credentials not found: set KAGGLE_API_TOKEN, "
        "KAGGLE_USERNAME / KAGGLE_KEY, or place ~/.kaggle/kaggle.json"
    )


def fetch_page(auth_header, page):
    params = urllib.parse.urlencode({"sortBy": "latestDeadline", "page": page})
    req = urllib.request.Request(
        f"{API_BASE}?{params}",
        headers={"Authorization": auth_header, "User-Agent": "everyday-kaggle-news"},
    )
    with urllib.request.urlopen(req, timeout=30) as res:
        return json.load(res)


def parse_date(value):
    if not value:
        return None
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def main():
    out_path = Path(sys.argv[1] if len(sys.argv) > 1 else "docs/competitions.json")
    header = auth_header()

    now = datetime.now(timezone.utc)
    competitions = []
    seen = set()
    for page in range(1, 21):
        items = fetch_page(header, page)
        if not items:
            break
        for item in items:
            ref = item.get("ref") or ""
            slug = ref.rstrip("/").rsplit("/", 1)[-1]
            if not slug or slug in seen:
                continue
            seen.add(slug)
            deadline = parse_date(item.get("deadline"))
            if deadline is None or deadline < now:
                continue
            # メダル対象のみ掲載(フィールドが無い場合は除外しない)
            if item.get("awardsPoints") is False:
                continue
            start = parse_date(item.get("enabledDate"))
            competitions.append(
                {
                    "slug": slug,
                    "title": item.get("title") or slug,
                    "url": item.get("url") or f"https://www.kaggle.com/competitions/{slug}",
                    "category": item.get("category") or "Other",
                    "reward": (item.get("reward") or "").replace(" Usd", " USD"),
                    "organization": item.get("organizationName") or "",
                    "start": start.strftime("%Y-%m-%d") if start else None,
                    "deadline": deadline.strftime("%Y-%m-%dT%H:%M:%SZ"),
                    "teamCount": item.get("teamCount") or 0,
                    "longRunning": deadline > now + timedelta(days=LONG_RUNNING_DAYS),
                }
            )

    competitions.sort(key=lambda c: c["deadline"])
    payload = {
        "updatedAt": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "competitions": competitions,
    }
    out_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
    )
    print(f"wrote {len(competitions)} competitions -> {out_path}")


if __name__ == "__main__":
    main()
