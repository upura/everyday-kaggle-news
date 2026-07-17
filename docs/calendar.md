# コンペ開催カレンダー

開催中の Kaggle コンペのうち、メダル獲得の対象となるコンペの開催期間をタイムラインで表示します。
バーにカーソルを合わせると詳細を表示し、クリックするとコンペページへ移動します。
データは GitHub Actions が Kaggle API から毎日取得しています。X の bot など他の情報源は[最新情報の確認](./recent.md)を参照してください。

<style>
#cal-updated { font-size: 12px; color: #6e7781; margin: 12px 0 4px; }
#cal-msg { border: 1px solid #d0d7de; border-radius: 8px; padding: 12px 16px; color: #57606a; font-size: 14px; display: none; }
#cal-legend { display: flex; flex-wrap: wrap; gap: 8px; margin: 12px 0; }
#cal-legend button {
  font: inherit; font-size: 13px; color: #57606a; background: #fff;
  border: 1px solid #d0d7de; border-radius: 999px; padding: 4px 12px 4px 8px;
  cursor: pointer; display: flex; align-items: center; gap: 7px;
}
#cal-legend button .dot { width: 10px; height: 10px; border-radius: 50%; }
#cal-legend button[aria-pressed="true"] { border-color: #57606a; color: #1f2328; }
.cal-wrap { display: none; border: 1px solid #d0d7de; border-radius: 8px; overflow: hidden; }
.cal-wrap.show { display: flex; }
#cal-names { flex: 0 0 200px; min-width: 0; overflow: hidden; border-right: 1px solid #d0d7de; background: #fff; z-index: 2; }
#cal-names .cal-axis-spacer { height: 44px; border-bottom: 1px solid #d0d7de; }
.cal-name { height: 32px; display: flex; align-items: center; padding: 0 10px; font-size: 13px; }
.cal-name a { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; text-decoration: none; color: #1f2328; }
.cal-name a:hover { color: #0969da; text-decoration: underline; }
#cal-scroll { overflow-x: auto; flex: 1; }
#cal-canvas { position: relative; }
#cal-axis { height: 44px; border-bottom: 1px solid #d0d7de; position: relative; font-size: 11px; color: #6e7781; }
#cal-axis .month { position: absolute; top: 5px; font-size: 12px; color: #57606a; font-weight: 600; white-space: nowrap; }
#cal-axis .tick { position: absolute; top: 25px; white-space: nowrap; }
#cal-body { position: relative; }
.cal-grid { position: absolute; top: 0; bottom: 0; width: 1px; background: #eff2f5; }
.cal-grid.month { background: #d8dee4; }
#cal-today { position: absolute; top: 0; bottom: 0; width: 1px; background: #57606a; z-index: 1; }
#cal-today-label {
  position: absolute; top: 3px; transform: translateX(-50%); z-index: 1;
  background: #57606a; color: #fff; font-size: 10px; border-radius: 999px; padding: 1px 7px;
}
.cal-track { height: 32px; position: relative; }
.cal-bar { position: absolute; top: 9px; height: 14px; border-radius: 4px; display: block; }
.cal-bar::before { content: ""; position: absolute; top: -9px; bottom: -9px; left: 0; right: 0; }
.cal-bar:hover, .cal-bar:focus-visible { filter: brightness(0.85); }
.cal-bar:focus-visible { outline: 2px solid #0969da; outline-offset: 2px; }
.cal-bar.clip-l { border-top-left-radius: 0; border-bottom-left-radius: 0; }
.cal-bar.clip-r { border-top-right-radius: 0; border-bottom-right-radius: 0; }
.cal-note { font-size: 12px; color: #6e7781; margin-top: 8px; }
#cal-tip {
  position: fixed; z-index: 10; max-width: 320px; background: #fff;
  border: 1px solid #d0d7de; border-radius: 8px; padding: 10px 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12); font-size: 12px; color: #57606a;
  pointer-events: none; display: none; line-height: 1.7;
}
#cal-tip .tip-title { font-size: 13px; font-weight: 600; color: #1f2328; margin-bottom: 2px; }
#cal-tip .key { display: inline-block; width: 12px; height: 3px; border-radius: 2px; vertical-align: middle; margin-right: 5px; }
#cal-tip strong { color: #1f2328; }
#cal-long-section, #cal-table-section { display: none; }
#cal-table td, #cal-table th { white-space: nowrap; }
#cal-table td:first-child, #cal-table th:first-child { white-space: normal; }
@media (max-width: 640px) { #cal-names { flex-basis: 130px; } }
</style>

<div id="cal-updated"></div>
<div id="cal-msg"></div>
<div id="cal-legend" role="group" aria-label="カテゴリの絞り込み"></div>

<div class="cal-wrap">
  <div id="cal-names"><div class="cal-axis-spacer"></div></div>
  <div id="cal-scroll">
    <div id="cal-canvas">
      <div id="cal-axis"></div>
      <div id="cal-body"></div>
    </div>
  </div>
</div>

<p class="cal-note" id="cal-wrap-note" style="display:none">縦の濃い線は今日の位置です。左右に切れているバーは表示範囲の外まで続きます。締切が 400 日以上先のコンペは下の「常設・長期開催」に分けて表示します。</p>

<div id="cal-long-section" markdown="0">
  <h2>常設・長期開催</h2>
  <ul id="cal-long"></ul>
</div>

<div id="cal-table-section" markdown="0">
  <h2>一覧（表形式）</h2>
  <div style="overflow-x:auto">
    <table id="cal-table">
      <thead><tr><th>コンペ</th><th>カテゴリ</th><th>開始</th><th>締切（JST）</th><th>残り</th><th>賞金</th><th>チーム数</th></tr></thead>
      <tbody></tbody>
    </table>
  </div>
</div>

<div id="cal-tip" role="tooltip"></div>

<script>
(function () {
  var CAT_ORDER = ["Featured", "Research", "Community", "Playground", "Getting Started", "Analytics", "Simulations"];
  var CAT_COLORS = {
    "Featured": "#2a78d6", "Research": "#008300", "Community": "#e87ba4",
    "Playground": "#eda100", "Getting Started": "#1baf7a", "Analytics": "#eb6834",
    "Simulations": "#4a3aa7"
  };
  var OTHER = "その他", OTHER_COLOR = "#898781";
  var DAY = 86400e3, JST = 9 * 3600e3, PX = 9;

  var names = document.getElementById("cal-names");
  var axis = document.getElementById("cal-axis");
  var body = document.getElementById("cal-body");
  var canvas = document.getElementById("cal-canvas");
  var legend = document.getElementById("cal-legend");
  var tip = document.getElementById("cal-tip");
  var rows = [], active = {};

  fetch("competitions.json")
    .then(function (r) { if (!r.ok) { throw new Error(r.status); } return r.json(); })
    .then(init)
    .catch(function () { message("コンペ情報の読み込みに失敗しました。時間をおいて再読み込みしてください。"); });

  function message(text) {
    var el = document.getElementById("cal-msg");
    el.textContent = text;
    el.style.display = "block";
  }

  function jstDay(t) { return Math.floor((t + JST) / DAY); }
  function dayDate(d) { return new Date(d * DAY); }
  function pad(n) { return (n < 10 ? "0" : "") + n; }
  function ymd(d) {
    var t = dayDate(d);
    return t.getUTCFullYear() + "-" + pad(t.getUTCMonth() + 1) + "-" + pad(t.getUTCDate());
  }
  function jstDateTime(t) {
    return t.toLocaleString("ja-JP", {
      timeZone: "Asia/Tokyo", year: "numeric", month: "2-digit", day: "2-digit",
      hour: "2-digit", minute: "2-digit"
    });
  }
  function catOf(c) { return CAT_COLORS[c.category] ? c.category : OTHER; }
  function colorOf(cat) { return CAT_COLORS[cat] || OTHER_COLOR; }

  function init(data) {
    if (data.updatedAt) {
      document.getElementById("cal-updated").textContent =
        "最終更新: " + jstDateTime(new Date(data.updatedAt)) + " JST（毎日自動更新）";
    }
    var comps = (data.competitions || []).map(function (c) {
      return Object.assign({}, c, {
        end: Date.parse(c.deadline),
        startT: c.start ? Date.parse(c.start) : null,
        cat: catOf(c)
      });
    }).filter(function (c) { return isFinite(c.end) && c.end > Date.now(); });
    if (!comps.length) {
      message("コンペ情報がまだ生成されていません。次回のサイトビルド後に表示されます。");
      return;
    }
    comps.sort(function (a, b) { return a.end - b.end; });
    var timeline = comps.filter(function (c) { return !c.longRunning; });
    var longs = comps.filter(function (c) { return c.longRunning; });

    var cats = CAT_ORDER.concat([OTHER]).filter(function (cat) {
      return comps.some(function (c) { return c.cat === cat; });
    });
    cats.forEach(function (cat) { active[cat] = true; });
    buildLegend(cats, comps);
    if (timeline.length) { buildTimeline(timeline); }
    buildLongs(longs);
    buildTable(comps);
    applyFilter();
  }

  function buildLegend(cats, comps) {
    cats.forEach(function (cat) {
      var n = comps.filter(function (c) { return c.cat === cat; }).length;
      var b = document.createElement("button");
      b.type = "button";
      b.setAttribute("aria-pressed", "true");
      var dot = document.createElement("span");
      dot.className = "dot";
      dot.style.background = colorOf(cat);
      b.appendChild(dot);
      b.appendChild(document.createTextNode(cat + " (" + n + ")"));
      b.addEventListener("click", function () {
        active[cat] = !active[cat];
        b.setAttribute("aria-pressed", String(active[cat]));
        applyFilter();
      });
      legend.appendChild(b);
    });
  }

  function buildTimeline(timeline) {
    var today = jstDay(Date.now());
    var w0 = today - 14;
    var maxEnd = jstDay(timeline[timeline.length - 1].end);
    var w1 = Math.min(Math.max(maxEnd + 5, today + 42), today + 150);
    canvas.style.width = ((w1 - w0) * PX) + "px";
    var x = function (d) { return (d - w0) * PX; };

    for (var d = w0; d <= w1; d++) {
      var t = dayDate(d);
      if (t.getUTCDate() === 1 || d === w0) {
        var m = document.createElement("div");
        m.className = "month";
        m.style.left = (x(d) + 4) + "px";
        m.textContent = t.getUTCFullYear() + "年" + (t.getUTCMonth() + 1) + "月";
        axis.appendChild(m);
      }
      if (t.getUTCDay() === 1 || t.getUTCDate() === 1) {
        var g = document.createElement("div");
        g.className = "cal-grid" + (t.getUTCDate() === 1 ? " month" : "");
        g.style.left = x(d) + "px";
        body.appendChild(g);
        if (t.getUTCDay() === 1) {
          var tick = document.createElement("div");
          tick.className = "tick";
          tick.style.left = (x(d) + 3) + "px";
          tick.textContent = (t.getUTCMonth() + 1) + "/" + t.getUTCDate();
          axis.appendChild(tick);
        }
      }
    }

    var line = document.createElement("div");
    line.id = "cal-today";
    line.style.left = x(today) + "px";
    body.appendChild(line);
    var lbl = document.createElement("div");
    lbl.id = "cal-today-label";
    lbl.style.left = x(today) + "px";
    lbl.textContent = "今日";
    axis.appendChild(lbl);

    timeline.forEach(function (c) {
      var name = document.createElement("div");
      name.className = "cal-name";
      var a = document.createElement("a");
      a.href = c.url;
      a.textContent = c.title;
      a.title = c.title;
      name.appendChild(a);
      names.appendChild(name);

      var track = document.createElement("div");
      track.className = "cal-track";
      var s = c.startT ? jstDay(c.startT) : w0;
      var e = jstDay(c.end) + 1;
      var bar = document.createElement("a");
      bar.className = "cal-bar";
      bar.href = c.url;
      if (s < w0) { s = w0; bar.classList.add("clip-l"); }
      if (e > w1) { e = w1; bar.classList.add("clip-r"); }
      bar.style.left = x(s) + "px";
      bar.style.width = Math.max((e - s) * PX - 2, 8) + "px";
      bar.style.background = colorOf(c.cat);
      bar.setAttribute("aria-label", barLabel(c));
      attachTip(bar, c);
      track.appendChild(bar);
      body.appendChild(track);
      rows.push({ comp: c, els: [name, track] });
    });
    document.querySelector(".cal-wrap").classList.add("show");
    document.getElementById("cal-wrap-note").style.display = "block";
  }

  function daysLeft(c) { return Math.ceil((c.end - Date.now()) / DAY); }
  function period(c) {
    return (c.startT ? ymd(jstDay(c.startT)) + " " : "") + "〜 " + ymd(jstDay(c.end));
  }
  function barLabel(c) {
    return c.title + "（" + c.cat + "、" + period(c) + "、残り " + daysLeft(c) + " 日）";
  }

  function attachTip(el, c) {
    var show = function (ev) {
      tip.textContent = "";
      var title = document.createElement("div");
      title.className = "tip-title";
      title.textContent = c.title;
      tip.appendChild(title);
      var cat = document.createElement("div");
      var key = document.createElement("span");
      key.className = "key";
      key.style.background = colorOf(c.cat);
      cat.appendChild(key);
      cat.appendChild(document.createTextNode(c.cat + (c.organization ? "・" + c.organization : "")));
      tip.appendChild(cat);
      addRow("期間", period(c));
      addRow("締切", jstDateTime(new Date(c.end)) + " JST（残り " + daysLeft(c) + " 日）");
      if (c.reward) { addRow("賞金", c.reward); }
      if (c.teamCount) { addRow("チーム数", String(c.teamCount)); }
      tip.style.display = "block";
      move(ev);
    };
    var addRow = function (label, value) {
      var row = document.createElement("div");
      var strong = document.createElement("strong");
      strong.textContent = value;
      row.appendChild(strong);
      row.appendChild(document.createTextNode("｜" + label));
      tip.appendChild(row);
    };
    var move = function (ev) {
      var px = ev && ev.clientX != null ? ev.clientX : el.getBoundingClientRect().left;
      var py = ev && ev.clientY != null ? ev.clientY : el.getBoundingClientRect().top;
      var w = tip.offsetWidth, h = tip.offsetHeight;
      var left = Math.min(px + 14, window.innerWidth - w - 8);
      var top = py + 16 + h > window.innerHeight ? py - h - 12 : py + 16;
      tip.style.left = Math.max(left, 8) + "px";
      tip.style.top = Math.max(top, 8) + "px";
    };
    var hide = function () { tip.style.display = "none"; };
    el.addEventListener("pointerenter", show);
    el.addEventListener("pointermove", move);
    el.addEventListener("pointerleave", hide);
    el.addEventListener("focus", show);
    el.addEventListener("blur", hide);
  }

  function buildLongs(longs) {
    if (!longs.length) { return; }
    var ul = document.getElementById("cal-long");
    longs.forEach(function (c) {
      var li = document.createElement("li");
      var a = document.createElement("a");
      a.href = c.url;
      a.textContent = c.title;
      li.appendChild(a);
      var far = c.end - Date.now() > 3 * 365 * DAY;
      li.appendChild(document.createTextNode(
        "（" + c.cat + (far ? "、常設" : "、締切 " + ymd(jstDay(c.end))) + "）"));
      ul.appendChild(li);
      rows.push({ comp: c, els: [li] });
    });
    document.getElementById("cal-long-section").style.display = "block";
  }

  function buildTable(comps) {
    var tbody = document.querySelector("#cal-table tbody");
    comps.forEach(function (c) {
      var tr = document.createElement("tr");
      var cells = [
        null, c.cat, c.startT ? ymd(jstDay(c.startT)) : "-",
        jstDateTime(new Date(c.end)), daysLeft(c) + " 日",
        c.reward || "-", c.teamCount ? String(c.teamCount) : "-"
      ];
      cells.forEach(function (v, i) {
        var td = document.createElement("td");
        if (i === 0) {
          var a = document.createElement("a");
          a.href = c.url;
          a.textContent = c.title;
          td.appendChild(a);
        } else {
          td.textContent = v;
        }
        tr.appendChild(td);
      });
      tbody.appendChild(tr);
      rows.push({ comp: c, els: [tr] });
    });
    document.getElementById("cal-table-section").style.display = "block";
  }

  function applyFilter() {
    rows.forEach(function (row) {
      var on = active[row.comp.cat];
      row.els.forEach(function (el) { el.style.display = on ? "" : "none"; });
    });
  }
})();
</script>
