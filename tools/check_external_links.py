#!/usr/bin/env python3
"""外部リンク切れ検査。docs/ 配下の全外部 URL を確認し、Markdown レポートを書き出す。

使い方: python3 tools/check_external_links.py <report.md> [--limit N]
リンク切れ(404/410)が 1 件以上あれば終了コード 1。
ボット対策で誤判定しやすいドメインは「要手動確認」として分けて報告する。
"""
import os
import re
import sys
import time
import urllib.error
import urllib.request

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
LINK_RE = re.compile(r"\]\((https?://(?:[^()\s]|\([^()\s]*\))+)\)")
MANUAL_DOMAINS = ("x.com", "twitter.com", "linkedin.com",
                  "amazon.co.jp", "amazon.com", "amzn.asia", "amzn.to",
                  "kaggle.com", "medium.com")
UA = "Mozilla/5.0 (compatible; everyday-kaggle-news-linkcheck)"

report_path = sys.argv[1] if len(sys.argv) > 1 else "linkcheck-report.md"
limit = None
if "--limit" in sys.argv:
    limit = int(sys.argv[sys.argv.index("--limit") + 1])

urls = {}
for dirpath, _, files in os.walk(os.path.join(ROOT, "docs")):
    for f in files:
        if not f.endswith(".md"):
            continue
        path = os.path.join(dirpath, f)
        rel = os.path.relpath(path, ROOT)
        for m in LINK_RE.finditer(open(path, encoding="utf-8").read()):
            urls.setdefault(m.group(1), rel)

items = sorted(urls.items())
if limit:
    items = items[:limit]


def status(url):
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, method=method, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=15) as r:
                return r.status
        except urllib.error.HTTPError as e:
            if method == "HEAD" and e.code in (403, 405, 501):
                continue
            return e.code
        except Exception:
            if method == "HEAD":
                continue
            return None
    return None


broken, suspect = [], []
for i, (url, page) in enumerate(items):
    code = status(url)
    if code in (404, 410):
        (suspect if url.startswith(tuple(f"https://{d}" for d in MANUAL_DOMAINS))
         or any(d in url for d in MANUAL_DOMAINS) else broken).append((url, page, code))
    elif code is None or code >= 400:
        suspect.append((url, page, code))
    if (i + 1) % 50 == 0:
        print(f"{i + 1}/{len(items)} checked", flush=True)
    time.sleep(0.5)

with open(report_path, "w", encoding="utf-8") as f:
    f.write(f"外部リンク検査: {len(items)} 件中、リンク切れ {len(broken)} 件、要手動確認 {len(suspect)} 件\n\n")
    if broken:
        f.write("## リンク切れ(404/410)\n\n")
        for url, page, code in broken:
            f.write(f"- [{code}] {url} (掲載: {page})\n")
        f.write("\n")
    if suspect:
        f.write("## 要手動確認(403/タイムアウト/ボット対策ドメインなど)\n\n")
        for url, page, code in suspect:
            f.write(f"- [{code}] {url} (掲載: {page})\n")

print(open(report_path, encoding="utf-8").read())
sys.exit(1 if broken else 0)
