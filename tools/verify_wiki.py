#!/usr/bin/env python3
"""LLM Wiki の整合性チェック(lint の内部検査項目)。

検査: 相対リンク切れ / 孤立概念ページ / README.md 目次と実ファイルの同期 /
目次ラベルと H1 の一致 / solutions.md の div・datatype 形式 / 同一セクション内の URL 重複
参考情報として注釈カバレッジも表示する。問題があれば終了コード 1。
"""
import os
import re
import sys
from collections import Counter

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
DATATYPES = {"tabular", "text", "image", "audio", "timeseries",
             "video", "3d", "multimodal", "other"}
LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")
ENTRY_RE = re.compile(r"^\s*-\s+\[([^\]]+)\]\((https?://[^)\s]+)\)(?::\s*(.+))?")

problems = []

md_files = [os.path.join(ROOT, "README.md"), os.path.join(ROOT, "CONTRIBUTING.md")]
for dirpath, _, files in os.walk(os.path.join(ROOT, "docs")):
    md_files += [os.path.join(dirpath, f) for f in files if f.endswith(".md")]
all_text = {p: open(p, encoding="utf-8").read() for p in md_files}

# 1. 相対リンク切れ
for path, text in all_text.items():
    for m in LINK_RE.finditer(text):
        target = m.group(2)
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        target_path = target.split("#")[0]
        if not target_path:
            continue
        resolved = os.path.normpath(os.path.join(os.path.dirname(path), target_path))
        if not os.path.exists(resolved):
            problems.append(f"[相対リンク切れ] {os.path.relpath(path, ROOT)}: {target}")

# 2. 孤立概念ページ
concepts_dir = os.path.join(ROOT, "docs/wiki/concepts")
concept_files = sorted(f for f in os.listdir(concepts_dir) if f.endswith(".md"))
for cf in concept_files:
    own = os.path.normpath(os.path.join(concepts_dir, cf))
    if not any(cf in t for p, t in all_text.items() if os.path.normpath(p) != own):
        problems.append(f"[孤立ページ] docs/wiki/concepts/{cf} はどこからもリンクされていない")

# 3. README.md の目次と実ファイルの同期・ラベル一致
readme = all_text[os.path.join(ROOT, "README.md")]
toc = dict(re.findall(r"- \[([^\]]+)\]\(\./docs/wiki/concepts/([\w-]+\.md)\)", readme))
toc_targets = set(toc.values())
for missing in sorted(set(concept_files) - toc_targets):
    problems.append(f"[目次未掲載] concepts/{missing} が README.md の目次にない")
for stale in sorted(toc_targets - set(concept_files)):
    problems.append(f"[目次リンク切れ] README.md が存在しない concepts/{stale} を参照")
for label, fname in toc.items():
    fpath = os.path.join(concepts_dir, fname)
    if os.path.exists(fpath):
        h1 = open(fpath, encoding="utf-8").readline().strip().lstrip("# ")
        if label != h1:
            problems.append(f"[目次ラベル不一致] README.md「{label}」 vs {fname} H1「{h1}」")

# 4. solutions.md の div / datatype 形式
sol = all_text[os.path.join(ROOT, "docs/solutions.md")]
for div in re.findall(r'<div class="competition-entry"[^>]*>', sol):
    for attr in ("data-year", "data-datatype", "data-platform", 'markdown="1"'):
        if attr not in div:
            problems.append(f"[solutions形式] 属性 {attr} 欠落: {div[:80]}")
    dt = re.search(r'data-datatype="([^"]*)"', div)
    if dt and dt.group(1) not in DATATYPES:
        problems.append(f"[solutions形式] 不正な data-datatype: {dt.group(1)}")

# 5. 同一セクション内の URL 重複
def norm(u):
    return u.rstrip("/").replace("http://", "https://")

for path, text in all_text.items():
    for section in re.split(r"^#{1,3} ", text, flags=re.M):
        urls = [norm(m.group(2)) for m in LINK_RE.finditer(section)
                if m.group(2).startswith("http")]
        for url, c in Counter(urls).items():
            if c > 1:
                problems.append(
                    f"[同一セクション内重複] {os.path.relpath(path, ROOT)}: {url} ×{c}")

# 参考: 注釈カバレッジ(検査ではなく情報表示)
total = annotated = 0
coverage = []
for path, text in sorted(all_text.items()):
    n = a = 0
    for line in text.splitlines():
        m = ENTRY_RE.match(line)
        if m:
            n += 1
            if m.group(3):
                a += 1
    if n:
        coverage.append((os.path.relpath(path, ROOT), a, n))
        total += n
        annotated += a
print(f"注釈カバレッジ: {annotated}/{total} ({100 * annotated // max(total, 1)}%)")
for rel, a, n in sorted(coverage, key=lambda x: x[1] / x[2])[:5]:
    print(f"  低: {rel} {a}/{n}")

print(f"\n検査対象: {len(md_files)} ファイル / 概念ページ {len(concept_files)} 本")
if problems:
    print(f"検出 {len(problems)} 件:")
    for p in problems:
        print(" -", p)
    sys.exit(1)
print("問題なし")
