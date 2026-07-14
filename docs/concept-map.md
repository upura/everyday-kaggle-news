# 概念マップ

本サイトの全ページ（概念ページ+一覧ページ）と、ページ間の相互リンクを可視化したマップです。
ノードの大きさは資料数、線の太さは相互リンクの本数を表します。ドラッグで移動、クリックで詳細を表示します。

<style>
#cmap-legend { display: flex; flex-wrap: wrap; gap: 8px; margin: 12px 0; }
#cmap-legend button {
  font: inherit; font-size: 13px; color: #57606a; background: #fff;
  border: 1px solid #d0d7de; border-radius: 999px; padding: 4px 12px 4px 8px;
  cursor: pointer; display: flex; align-items: center; gap: 7px;
}
#cmap-legend button .dot { width: 10px; height: 10px; border-radius: 50%; }
#cmap-legend button[aria-pressed="true"] { border-color: #57606a; color: #1f2328; }
#cmap-stage { position: relative; border: 1px solid #d0d7de; border-radius: 8px; }
#cmap-cv { width: 100%; height: 70vh; min-height: 420px; display: block; cursor: grab; }
#cmap-card {
  position: absolute; top: 12px; right: 12px; width: 250px; background: #fff;
  border: 1px solid #d0d7de; border-radius: 8px; padding: 12px 14px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08); font-size: 13px; display: none;
}
#cmap-card.show { display: block; }
#cmap-card .group { font-size: 11px; color: #57606a; display: flex; align-items: center; gap: 6px; }
#cmap-card .group .dot { width: 9px; height: 9px; border-radius: 50%; }
#cmap-card h3 { font-size: 15px; margin: 6px 0 8px; }
#cmap-card .meta { color: #57606a; margin-bottom: 8px; }
#cmap-card .nbrs { color: #57606a; line-height: 1.7; }
#cmap-note { font-size: 12px; color: #6e7781; margin-top: 8px; }
</style>

<div id="cmap-legend" role="group" aria-label="話題グループの絞り込み"></div>
<div id="cmap-stage">
  <canvas id="cmap-cv"></canvas>
  <div id="cmap-card"></div>
</div>
<p id="cmap-note">グループをクリックすると絞り込めます。ページの一覧は<a href="../README.md">目次</a>、リンク単位の検索は<a href="./search.md">検索</a>へ。</p>

<script>
(function () {
  var GROUPS = ["学び方", "情報収集・コミュニティ", "データ種別・タスク", "技術動向", "進め方・環境"];
  var COLORS = ["#2a78d6", "#1baf7a", "#eda100", "#4a3aa7", "#008300"];
  var INK = "#1f2328", INK2 = "#57606a", INK3 = "#8c959f", EDGE = "rgba(87,96,106,0.32)";

  var cv = document.getElementById("cmap-cv");
  var ctx = cv.getContext("2d");
  var card = document.getElementById("cmap-card");
  var legend = document.getElementById("cmap-legend");
  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var groupColor = function (g) { return COLORS[GROUPS.indexOf(g)] || INK2; };

  fetch("graph.json").then(function (r) { return r.json(); }).then(init);

  function init(DATA) {
    var nodes = DATA.nodes.map(function (n, i) {
      var angle = (i / DATA.nodes.length) * Math.PI * 2;
      return Object.assign({}, n, {
        x: Math.cos(angle) * 200, y: Math.sin(angle) * 150,
        vx: 0, vy: 0, deg: 0,
        r: Math.min(26, 6 + Math.sqrt(n.links) * 1.5)
      });
    });
    var byId = {};
    nodes.forEach(function (n) { byId[n.id] = n; });
    var edges = DATA.edges.map(function (e) {
      byId[e.a].deg++; byId[e.b].deg++;
      return { a: byId[e.a], b: byId[e.b], w: e.w };
    });
    var nbrs = {};
    nodes.forEach(function (n) { nbrs[n.id] = []; });
    edges.forEach(function (e) { nbrs[e.a.id].push(e.b); nbrs[e.b.id].push(e.a); });

    var focusGroup = null, hovered = null, selected = null, dragging = null;
    GROUPS.forEach(function (g) {
      var b = document.createElement("button");
      b.setAttribute("aria-pressed", "false");
      var d = document.createElement("span");
      d.className = "dot";
      d.style.background = groupColor(g);
      b.appendChild(d);
      b.appendChild(document.createTextNode(g));
      b.addEventListener("click", function () {
        focusGroup = focusGroup === g ? null : g;
        legend.querySelectorAll("button").forEach(function (x) {
          x.setAttribute("aria-pressed", String(x.textContent === (focusGroup || "")));
        });
        draw();
      });
      legend.appendChild(b);
    });

    var W = 0, H = 0;
    function resize() {
      var rect = cv.getBoundingClientRect();
      W = rect.width; H = rect.height;
      var dpr = window.devicePixelRatio || 1;
      cv.width = W * dpr; cv.height = H * dpr;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      draw();
    }

    function step() {
      for (var i = 0; i < nodes.length; i++) {
        for (var j = i + 1; j < nodes.length; j++) {
          var a = nodes[i], b = nodes[j];
          var dx = b.x - a.x, dy = b.y - a.y;
          var d2 = dx * dx + dy * dy + 0.01;
          var f = 2600 / d2;
          var d = Math.sqrt(d2);
          dx /= d; dy /= d;
          a.vx -= dx * f; a.vy -= dy * f;
          b.vx += dx * f; b.vy += dy * f;
        }
      }
      edges.forEach(function (e) {
        var dx = e.b.x - e.a.x, dy = e.b.y - e.a.y;
        var d = Math.sqrt(dx * dx + dy * dy) + 0.01;
        var f = (d - (90 + e.a.r + e.b.r)) * 0.012 * Math.min(e.w, 3);
        dx /= d; dy /= d;
        e.a.vx += dx * f; e.a.vy += dy * f;
        e.b.vx -= dx * f; e.b.vy -= dy * f;
      });
      nodes.forEach(function (n) {
        n.vx -= n.x * 0.004; n.vy -= n.y * 0.004;
        if (n !== dragging) {
          n.x += (n.vx *= 0.82);
          n.y += (n.vy *= 0.82);
        } else { n.vx = 0; n.vy = 0; }
      });
    }

    function dimmed(n) {
      var active = selected || hovered;
      if (active) return n !== active && nbrs[active.id].indexOf(n) === -1;
      return focusGroup ? n.group !== focusGroup : false;
    }

    function draw() {
      ctx.clearRect(0, 0, W, H);
      ctx.save();
      ctx.translate(W / 2, H / 2);
      var active = selected || hovered;
      edges.forEach(function (e) {
        var on = active ? (e.a === active || e.b === active)
          : (!focusGroup || (e.a.group === focusGroup && e.b.group === focusGroup));
        ctx.strokeStyle = EDGE;
        ctx.globalAlpha = on ? 1 : 0.12;
        ctx.lineWidth = 1 + e.w * 0.6;
        ctx.beginPath();
        ctx.moveTo(e.a.x, e.a.y);
        ctx.lineTo(e.b.x, e.b.y);
        ctx.stroke();
      });
      nodes.forEach(function (n) {
        var off = dimmed(n);
        ctx.globalAlpha = off ? 0.18 : 1;
        ctx.fillStyle = groupColor(n.group);
        ctx.beginPath();
        ctx.arc(n.x, n.y, n.r, 0, Math.PI * 2);
        ctx.fill();
        if (n === selected || n === hovered) {
          ctx.strokeStyle = INK;
          ctx.lineWidth = 2;
          ctx.stroke();
        }
        ctx.fillStyle = off ? INK3 : INK;
        ctx.font = "11px 'Hiragino Kaku Gothic ProN','Noto Sans JP',sans-serif";
        ctx.textAlign = "center";
        ctx.fillText(n.label, n.x, n.y + n.r + 13);
      });
      ctx.restore();
      ctx.globalAlpha = 1;
    }

    function esc(s) {
      return s.replace(/[&<>"]/g, function (c) {
        return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
      });
    }
    function showCard(n) {
      if (!n) { card.className = ""; return; }
      var ns = nbrs[n.id].slice().sort(function (a, b) { return b.deg - a.deg; })
        .map(function (m) { return esc(m.label); }).join("、") || "なし(目次からのみ到達)";
      card.innerHTML =
        '<div class="group"><span class="dot" style="background:' + groupColor(n.group) +
        '"></span>' + esc(n.group) + "</div><h3>" + esc(n.label) + "</h3>" +
        '<div class="meta">資料 ' + n.links + " 件 / 接続 " + n.deg + "</div>" +
        '<div class="nbrs"><b>つながり:</b> ' + ns + "</div>" +
        '<div style="margin-top:10px"><a href="' + esc(n.p) + '">ページを開く →</a></div>';
      card.className = "show";
    }

    function pick(mx, my) {
      var x = mx - W / 2, y = my - H / 2;
      for (var i = nodes.length - 1; i >= 0; i--) {
        var n = nodes[i];
        var dx = x - n.x, dy = y - n.y;
        if (dx * dx + dy * dy <= (n.r + 6) * (n.r + 6)) return n;
      }
      return null;
    }
    function pos(ev) {
      var r = cv.getBoundingClientRect();
      var p = ev.touches ? ev.touches[0] : ev;
      return { x: p.clientX - r.left, y: p.clientY - r.top };
    }

    cv.addEventListener("mousemove", function (ev) {
      var p = pos(ev);
      if (dragging) {
        dragging.x = p.x - W / 2;
        dragging.y = p.y - H / 2;
        if (reduced) draw();
        return;
      }
      var n = pick(p.x, p.y);
      if (n !== hovered) {
        hovered = n;
        cv.style.cursor = n ? "pointer" : "grab";
        if (!selected) showCard(n);
        draw();
      }
    });
    cv.addEventListener("mousedown", function (ev) {
      var p = pos(ev);
      dragging = pick(p.x, p.y);
    });
    window.addEventListener("mouseup", function (ev) {
      if (dragging) {
        var p = pos(ev);
        var n = pick(p.x, p.y);
        if (n === dragging) {
          selected = selected === n ? null : n;
          showCard(selected || hovered);
        }
        dragging = null;
        draw();
      }
    });
    window.addEventListener("resize", resize);

    resize();
    if (reduced) {
      for (var k = 0; k < 600; k++) step();
      draw();
    } else {
      var frames = 0;
      (function loop() {
        step();
        draw();
        if (++frames < 900 || dragging) requestAnimationFrame(loop);
        else {
          cv.addEventListener("mousedown", function () {
            frames = 600;
            requestAnimationFrame(loop);
          }, { once: true });
        }
      })();
    }
  }
})();
</script>
