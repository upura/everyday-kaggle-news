#!/usr/bin/env python3
"""docs/wiki/log.md に記録が無い Weekly Kaggle News の号を洗い出す。

weekly-ingest ワークフローの detect ジョブから呼ばれ、号ごとに
`{"number": <号番号>, "url": <号 URL>}` を並べた JSON を GITHUB_OUTPUT の
`issues` に出力する。号番号の小さい順で、1 回の実行で扱う数は MAX_ISSUES 件まで。

環境変数:
  ISSUE_URL  指定するとその号だけを対象にする(workflow_dispatch の入力)
  FORCE      "true" なら log.md に記録済みの号も対象に含める
"""
import json
import os
import re
import sys
import urllib.request

BASE = "https://weeklykagglenews.substack.com"
ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
LOG = os.path.join(ROOT, "docs", "wiki", "log.md")

# 取りこぼしが積もっていても 1 回の実行で PR を作りすぎないための上限
MAX_ISSUES = 5
# アーカイブの何号分を取りこぼし検査の対象にするか
ARCHIVE_LIMIT = 10

# log.md の号ごとの記録行。行頭に固定した形式だけを取り込み済みとみなす
# (本文中で別の号に言及している場合を誤検出しないため)
LOGGED_RE = re.compile(r"^- \d{4}-\d{2}-\d{2} ingest: WKN #(\d+)", re.M)


def fetch_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as res:
        return json.load(res)


def issue_number(post):
    """号の表題から号番号を取り出す(例: "Weekly Kaggle News #351" → 351)。"""
    m = re.search(r"#(\d+)", post.get("title", ""))
    return int(m.group(1)) if m else None


def post_url(post):
    url = post.get("canonical_url")
    if url:
        return url
    slug = post.get("slug")
    return "{}/p/{}".format(BASE, slug) if slug else None


def main():
    issue_url = os.environ.get("ISSUE_URL", "").strip()
    force = os.environ.get("FORCE", "").strip().lower() == "true"

    if issue_url:
        slug = issue_url.rstrip("/").rsplit("/", 1)[-1]
        posts = [fetch_json("{}/api/v1/posts/{}".format(BASE, slug))]
    else:
        posts = fetch_json(
            "{}/api/v1/archive?sort=new&limit={}&offset=0".format(BASE, ARCHIVE_LIMIT)
        )

    with open(LOG, encoding="utf-8") as f:
        logged = {int(n) for n in LOGGED_RE.findall(f.read())}

    targets = {}
    skipped = []
    for post in posts:
        number = issue_number(post)
        url = post_url(post)
        if number is None or url is None:
            print("号番号または URL を特定できないため除外: {!r}".format(post.get("title")))
            continue
        if number in logged and not force:
            skipped.append(number)
            continue
        # 同じ号が重複して返ってきても 1 件にまとめる
        targets[number] = {"number": number, "url": url}

    issues = [targets[n] for n in sorted(targets)][:MAX_ISSUES]

    if skipped:
        print("取り込み済みのためスキップ: {}".format(", ".join("#%d" % n for n in sorted(skipped))))
    if issues:
        print("取り込み対象: {}".format(", ".join("#%d" % i["number"] for i in issues)))
    else:
        print("取り込む号はありません")

    out = os.environ.get("GITHUB_OUTPUT")
    if out:
        with open(out, "a", encoding="utf-8") as f:
            f.write("issues={}\n".format(json.dumps(issues, ensure_ascii=False)))

    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as f:
            if issues:
                f.write("取り込み対象:\n\n")
                for i in issues:
                    f.write("- [WKN #{}]({})\n".format(i["number"], i["url"]))
            else:
                f.write("取り込む号はありません（最新号まで記録済み）。\n")


if __name__ == "__main__":
    sys.exit(main())
