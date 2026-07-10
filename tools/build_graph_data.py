#!/usr/bin/env python3
"""概念マップ用のグラフデータ docs/graph.json を生成する。

ノード = README の目次に載る全ページ(概念ページ+一覧ページ)、
エッジ = ページ本文間の相対リンク。GitHub Pages のビルドワークフローが
Jekyll ビルド前に実行する。
"""
import json
import os
import re

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))

readme = open(os.path.join(ROOT, "README.md"), encoding="utf-8").read()
nodes = {}
group = None
for line in readme.splitlines():
    h = re.match(r"^### (.+)", line)
    if h:
        group = h.group(1).strip()
        continue
    m = re.match(r"- \[([^\]]+)\]\(\./(docs/[\w/-]+\.md)\)", line)
    if m and group:
        label, relpath = m.group(1), m.group(2)
        nodes[relpath] = {"id": relpath, "label": label, "group": group}

ext_re = re.compile(r"\]\(https?://")
int_re = re.compile(r"\]\((\.{1,2}/[^)#\s]+\.md)\)")
edges = {}
for relpath, node in nodes.items():
    text = open(os.path.join(ROOT, relpath), encoding="utf-8").read()
    node["links"] = len(ext_re.findall(text))
    # docs/ からの相対 HTML パス(concept-map.html から辿るリンク先)
    node["p"] = relpath[len("docs/"):-3] + ".html"
    for m in int_re.finditer(text):
        target = os.path.normpath(os.path.join(os.path.dirname(relpath), m.group(1)))
        if target in nodes and target != relpath:
            key = tuple(sorted([relpath, target]))
            edges[key] = edges.get(key, 0) + 1

data = {
    "nodes": sorted(nodes.values(), key=lambda n: n["group"]),
    "edges": [{"a": a, "b": b, "w": w} for (a, b), w in sorted(edges.items())],
}
out = os.path.join(ROOT, "docs", "graph.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, separators=(",", ":"))
print(f"graph.json: nodes={len(nodes)} edges={len(edges)}")
