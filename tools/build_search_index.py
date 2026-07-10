#!/usr/bin/env python3
"""docs/ 配下の全 Markdown からリンク索引 docs/search.json を生成する。

GitHub Pages のビルドワークフローが Jekyll ビルド前に実行する。
各エントリ: t=リンクタイトル, u=URL, a=注釈, p=掲載ページ(docs/ からの相対 HTML パス), pt=ページ名, s=セクション名
"""
import json
import os
import re

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
DOCS = os.path.join(ROOT, "docs")

LINK_RE = re.compile(r"^\s*-\s+\[([^\]]+)\]\((https?://[^)\s]+)\)(?::\s*(.+))?")
TABLE_LINK_RE = re.compile(r"^\|\s*\[([^\]]+)\]\((https?://[^)\s]+)\)")
HEADING_RE = re.compile(r"^(#{1,3})\s+(.+)")
H3_HTML_RE = re.compile(r'<h3><a href="[^"]*">([^<]+)</a></h3>')

entries = []
for dirpath, _, files in sorted(os.walk(DOCS)):
    for fname in sorted(files):
        if not fname.endswith(".md"):
            continue
        path = os.path.join(dirpath, fname)
        rel_md = os.path.relpath(path, DOCS)
        rel_html = rel_md[:-3] + ".html"
        page_title = ""
        section = ""
        for line in open(path, encoding="utf-8"):
            m = HEADING_RE.match(line)
            if m:
                if not page_title:
                    page_title = m.group(2).strip()
                else:
                    section = m.group(2).strip()
                continue
            m = H3_HTML_RE.search(line)
            if m:
                section = m.group(1).strip()
                continue
            m = LINK_RE.match(line) or TABLE_LINK_RE.match(line)
            if m:
                groups = m.groups()
                entries.append({
                    "t": groups[0].strip(),
                    "u": groups[1],
                    "a": (groups[2].strip() if len(groups) > 2 and groups[2] else ""),
                    "p": rel_html,
                    "pt": page_title,
                    "s": section,
                })

out = os.path.join(DOCS, "search.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(entries, f, ensure_ascii=False, separators=(",", ":"))
print(f"search.json: {len(entries)} entries")
