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
import urllib.error
import urllib.request

BASE = "https://weeklykagglenews.substack.com"
JINA_PREFIX = "https://r.jina.ai/"
RSS2JSON_URL = (
    "https://api.rss2json.com/v1/api.json?rss_url=https://weeklykagglenews.substack.com/feed"
)
ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
LOG = os.path.join(ROOT, "docs", "wiki", "log.md")

# 取りこぼしが積もっていても 1 回の実行で PR を作りすぎないための上限
MAX_ISSUES = 5
# アーカイブの何号分を取りこぼし検査の対象にするか
ARCHIVE_LIMIT = 10

# log.md の号ごとの記録行。行頭に固定した形式だけを取り込み済みとみなす
# (本文中で別の号に言及している場合を誤検出しないため)
LOGGED_RE = re.compile(r"^- \d{4}-\d{2}-\d{2} ingest: WKN #(\d+)", re.M)
POST_URL_RE = re.compile(
    r"https://weeklykagglenews\.substack\.com/p/(weekly-kaggle-(?:news|issue)-(?:issue-)?(\d+)[a-z0-9-]*)"
)
RSS_ITEM_RE = re.compile(r"<item>(.*?)</item>", re.S)
RSS_TITLE_RE = re.compile(r"<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>", re.S)
RSS_LINK_RE = re.compile(r"<link>\s*(https://[^\s<]+)\s*</link>")
RSS_CONTENT_RE = re.compile(
    r"<content:encoded>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</content:encoded>", re.S
)

USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
)

try:
    from curl_cffi import requests as _cffi_requests
except ImportError:
    _cffi_requests = None


def _http_get_text(url, accept="text/html,application/xhtml+xml,application/xml;q=0.9,text/plain;q=0.8,*/*;q=0.7"):
    """URL からテキストを取得する。curl_cffi が利用可能なら Chrome TLS フィンガープリントを優先する。"""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": accept,
        "Accept-Language": "ja,en-US;q=0.9,en;q=0.8",
    }
    if _cffi_requests is not None:
        try:
            res = _cffi_requests.get(url, headers=headers, impersonate="chrome", timeout=30)
            if res.status_code == 200 and res.text:
                return res.text
        except Exception:
            pass

    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as res:
        return res.read().decode("utf-8", errors="replace")


def fetch_json(url):
    """JSON API からオブジェクトを取得する。"""
    text = _http_get_text(url, accept="application/json, text/plain, */*")
    return json.loads(text)


def fetch_rss2json():
    """rss2json API 経由で Substack RSS フィードから号一覧を取得する。"""
    data = fetch_json(RSS2JSON_URL)
    if not isinstance(data, dict) or data.get("status") != "ok":
        raise ValueError("rss2json status is not ok: {!r}".format(data.get("status") if isinstance(data, dict) else data))
    items = data.get("items") or []
    posts = []
    for item in items:
        title = (item.get("title") or "").strip()
        link = (item.get("link") or item.get("guid") or "").strip()
        if title and link:
            posts.append({"title": title, "canonical_url": link})
    if not posts:
        raise ValueError("rss2json returned no items")
    return posts


def extract_posts_from_text(text):
    """HTML / XML / Markdown / 部分 JSON テキストから号一覧を抽出する。"""
    found = {}
    # RSS フィードの <item> 要素がある場合は title と link の組を優先抽出する
    # (スラッグに号番号が含まれない #346 等も正確に拾える)
    for item_xml in RSS_ITEM_RE.findall(text):
        t_m = RSS_TITLE_RE.search(item_xml)
        l_m = RSS_LINK_RE.search(item_xml)
        if t_m and l_m:
            title = t_m.group(1).strip()
            link = l_m.group(1).strip()
            num_m = re.search(r"#(\d+)", title)
            if num_m:
                num = int(num_m.group(1))
                found[num] = {
                    "title": title,
                    "slug": link.rstrip("/").rsplit("/", 1)[-1],
                    "canonical_url": link,
                }

    for slug, num_str in POST_URL_RE.findall(text):
        num = int(num_str)
        if num not in found:
            found[num] = {
                "title": "Weekly Kaggle News #{}".format(num),
                "slug": slug,
                "canonical_url": "{}/p/{}".format(BASE, slug),
            }
    return found


def fetch_posts_with_fallback(limit, logged):
    """Substack API を試し、Cloudflare 403 等で失敗した場合は rss2json / RSS / sitemap / r.jina.ai 経由で号一覧を取得する。"""
    api_url = "{}/api/v1/archive?sort=new&limit={}&offset=0".format(BASE, limit)
    try:
        posts = fetch_json(api_url)
        if isinstance(posts, list) and posts:
            return posts
    except Exception as e:
        print("警告: {} の直接取得に失敗 ({})。フォールバックを試行します".format(api_url, e), file=sys.stderr)

    try:
        posts = fetch_rss2json()
        if posts:
            return posts[:limit]
    except Exception as e:
        print("警告: rss2json の取得に失敗 ({})".format(e), file=sys.stderr)

    found = {}
    fallback_urls = [
        "{}/feed".format(BASE),
        "{}/sitemap.xml".format(BASE),
        "{}{}/feed".format(JINA_PREFIX, BASE),
        "{}{}/sitemap.xml".format(JINA_PREFIX, BASE),
        "{}{}/archive".format(JINA_PREFIX, BASE),
        "{}{}".format(JINA_PREFIX, api_url),
    ]
    for candidate in fallback_urls:
        try:
            text = _http_get_text(candidate)
            found.update(extract_posts_from_text(text))
            if len(found) >= limit:
                break
        except Exception as e:
            print("警告: {} の取得に失敗 ({})".format(candidate, e), file=sys.stderr)

    if not found:
        raise RuntimeError("すべての経路で Weekly Kaggle News の号一覧取得に失敗しました")

    # プロキシ応答が途中で切れて最新号付近しか抽出できなかった場合でも、
    # log.md の最新記録号から最新号までの連番(160 号以降は weekly-kaggle-news-<N> で固定)を補完する
    max_found = max(found)
    min_num = max(max(logged) + 1 if logged else 160, max_found - limit + 1, 160)
    for num in range(min_num, max_found + 1):
        if num not in found:
            slug = "weekly-kaggle-news-{}".format(num)
            found[num] = {
                "title": "Weekly Kaggle News #{}".format(num),
                "slug": slug,
                "canonical_url": "{}/p/{}".format(BASE, slug),
            }

    top_nums = sorted(found, reverse=True)[:limit]
    return [found[n] for n in top_nums]


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


def fetch_issue_content(issue_url):
    """指定号の本文 (HTML または Markdown) を取得して返す。"""
    target = issue_url.rstrip("/")
    slug = target.rsplit("/", 1)[-1]

    # 1. Substack Posts API
    try:
        post = fetch_json("{}/api/v1/posts/{}".format(BASE, slug))
        if isinstance(post, dict) and post.get("body_html"):
            return "<h1>{}</h1>\n<p>URL: {}</p>\n{}".format(
                post.get("title", ""), target, post["body_html"]
            )
    except Exception as e:
        print("警告: Posts API からの本文取得に失敗 ({})".format(e), file=sys.stderr)

    # 2. rss2json API (直近 10 号の完全な content HTML を含む)
    try:
        data = fetch_json(RSS2JSON_URL)
        for item in (data.get("items") or []) if isinstance(data, dict) else []:
            link = (item.get("link") or item.get("guid") or "").strip().rstrip("/")
            content = item.get("content") or item.get("description") or ""
            if link == target and content:
                return "<h1>{}</h1>\n<p>URL: {}</p>\n{}".format(
                    item.get("title", ""), target, content
                )
    except Exception as e:
        print("警告: rss2json からの本文取得に失敗 ({})".format(e), file=sys.stderr)

    # 3. Substack RSS フィード (<content:encoded>)
    for feed_url in ("{}/feed".format(BASE), "{}{}/feed".format(JINA_PREFIX, BASE)):
        try:
            xml_text = _http_get_text(feed_url)
            for item_xml in RSS_ITEM_RE.findall(xml_text):
                l_m = RSS_LINK_RE.search(item_xml)
                c_m = RSS_CONTENT_RE.search(item_xml)
                if l_m and c_m and l_m.group(1).strip().rstrip("/") == target:
                    t_m = RSS_TITLE_RE.search(item_xml)
                    title = t_m.group(1).strip() if t_m else ""
                    return "<h1>{}</h1>\n<p>URL: {}</p>\n{}".format(
                        title, target, c_m.group(1)
                    )
        except Exception as e:
            print("警告: {} からの本文取得に失敗 ({})".format(feed_url, e), file=sys.stderr)

    # 4. ページ直接取得 / r.jina.ai リーダー経由
    for page_url in (target, "{}{}".format(JINA_PREFIX, target)):
        try:
            text = _http_get_text(page_url)
            if text and len(text.strip()) > 200:
                return text
        except Exception as e:
            print("警告: {} の本文取得に失敗 ({})".format(page_url, e), file=sys.stderr)

    raise RuntimeError("すべての経路で号本文の取得に失敗しました: {}".format(issue_url))


def main():
    if len(sys.argv) >= 3 and sys.argv[1] == "--fetch-issue":
        content = fetch_issue_content(sys.argv[2])
        sys.stdout.write(content)
        if not content.endswith("\n"):
            sys.stdout.write("\n")
        return 0

    issue_url = os.environ.get("ISSUE_URL", "").strip()
    force = os.environ.get("FORCE", "").strip().lower() == "true"

    with open(LOG, encoding="utf-8") as f:
        logged = {int(n) for n in LOGGED_RE.findall(f.read())}

    if issue_url:
        slug = issue_url.rstrip("/").rsplit("/", 1)[-1]
        try:
            posts = [fetch_json("{}/api/v1/posts/{}".format(BASE, slug))]
        except Exception:
            m = re.search(r"weekly-kaggle-(?:news|issue)-(?:issue-)?(\d+)", slug)
            if not m:
                posts = [
                    p
                    for p in fetch_posts_with_fallback(ARCHIVE_LIMIT, logged)
                    if post_url(p) and post_url(p).rstrip("/") == issue_url.rstrip("/")
                ]
                if not posts:
                    raise
            else:
                num = int(m.group(1))
                posts = [
                    {
                        "title": "Weekly Kaggle News #{}".format(num),
                        "slug": slug,
                        "canonical_url": "{}/p/{}".format(BASE, slug),
                    }
                ]
    else:
        posts = fetch_posts_with_fallback(ARCHIVE_LIMIT, logged)

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
