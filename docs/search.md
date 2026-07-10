# 検索

掲載している全リンク（タイトル・注釈）を横断検索できます。

<style>
#search-box {
  width: 100%;
  padding: 12px 16px;
  font-size: 16px;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-sizing: border-box;
  margin-bottom: 8px;
}
#search-count { color: #666; font-size: 13px; margin-bottom: 16px; }
.search-hit { padding: 10px 0; border-bottom: 1px solid #eee; }
.search-hit .hit-title { font-weight: bold; }
.search-hit .hit-note { font-size: 14px; margin: 4px 0 0; }
.search-hit .hit-meta { font-size: 12px; color: #666; margin-top: 4px; }
</style>

<input type="search" id="search-box" placeholder="キーワードを入力(例: Polars、リーク、焼きなまし)" autofocus>
<div id="search-count"></div>
<div id="search-results"></div>

<script>
(function () {
  var box = document.getElementById('search-box');
  var count = document.getElementById('search-count');
  var results = document.getElementById('search-results');
  var index = null;

  function load() {
    if (index) return Promise.resolve(index);
    return fetch('search.json').then(function (r) { return r.json(); })
      .then(function (data) { index = data; return index; });
  }

  function esc(s) {
    return s.replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  function render(hits, total) {
    count.textContent = total === null ? '' : total + ' 件ヒット' + (total > 100 ? '(先頭 100 件を表示)' : '');
    results.innerHTML = hits.map(function (e) {
      var meta = esc(e.pt) + (e.s ? ' › ' + esc(e.s) : '');
      return '<div class="search-hit">' +
        '<div class="hit-title"><a href="' + esc(e.u) + '">' + esc(e.t) + '</a></div>' +
        (e.a ? '<div class="hit-note">' + esc(e.a) + '</div>' : '') +
        '<div class="hit-meta">掲載: <a href="' + esc(e.p) + '">' + meta + '</a></div>' +
        '</div>';
    }).join('');
  }

  var timer = null;
  box.addEventListener('input', function () {
    clearTimeout(timer);
    timer = setTimeout(function () {
      var q = box.value.trim().toLowerCase();
      if (!q) { render([], null); return; }
      load().then(function (idx) {
        var terms = q.split(/\s+/);
        var hits = idx.filter(function (e) {
          var hay = (e.t + ' ' + e.a + ' ' + e.pt + ' ' + e.s).toLowerCase();
          return terms.every(function (t) { return hay.indexOf(t) !== -1; });
        });
        render(hits.slice(0, 100), hits.length);
      });
    }, 150);
  });
})();
</script>
