import re, os
from collections import Counter

LINK = re.compile(r'\[([^\]]+)\]\((https?://[^)]+)\)')
ENTRY = re.compile(r'^\s*-\s+\[([^\]]+)\]\((https?://[^)]+)\)')


def norm(u):
    return u.rstrip('/')


files = []
for d, _, fs in os.walk("docs"):
    for f in fs:
        if f.endswith(".md"):
            files.append(os.path.join(d, f))
files.append("README.md")
texts = {p: open(p, encoding="utf-8").read() for p in files}
sol = texts["docs/solutions.md"]
sol_urls = set(norm(m.group(2)) for m in LINK.finditer(sol))
prob = []
for p, t in texts.items():
    if p == "docs/solutions.md":
        continue
    for line in t.splitlines():
        m = ENTRY.match(line)
        if m and norm(m.group(2)) in sol_urls:
            prob.append("[solutions重複] %s: %s" % (p, norm(m.group(2))))

h3 = re.findall(r'<h3><a href="[^"]*">(.*?)</a></h3>', sol)
for k, c in Counter(h3).items():
    if c > 1:
        prob.append("[h3重複] %s x%d" % (k, c))

DT = set("tabular text image audio timeseries video 3d multimodal other".split())
for div in re.findall(r'<div class="competition-entry"[^>]*>', sol):
    for a in ("markdown=", "data-year", "data-datatype", "data-platform"):
        if a not in div:
            prob.append("[div属性欠落] %s: %s" % (a, div))
    dt = re.search(r'data-datatype="([^"]+)"', div)
    if dt and dt.group(1) not in DT:
        prob.append("[不正datatype] %s" % dt.group(1))

for p, t in texts.items():
    for i, line in enumerate(t.splitlines(), 1):
        if ENTRY.match(line) and "|" in line and "\\|" not in line:
            prob.append("[未エスケープパイプ] %s:%d" % (p, i))

print("\n".join(prob) if prob else "OK: no problems")
print("div open:", sol.count('<div class="competition-entry"'), "close:", sol.count("</div>"))
