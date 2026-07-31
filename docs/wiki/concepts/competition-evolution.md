# コンペ形式・技術動向の変遷

Kaggle のコンペは、表データ・GBDT を中心とした時代から、画像・自然言語処理の深層学習化、コード提出形式の定着を経て、直近では LLM エージェントと対戦型コンペがプラットフォームの中心機能になりつつあります。
本ページは各データ種別・技術動向系のページを横断する時系列の見取り図です（本リンク集は Weekly Kaggle News のアーカイブが始まる 2019 年末以降を主にカバーするため、それ以前の記述は一般的な文脈情報として扱っています）。後半では、この見取り図を Kaggle 公式の Meta Kaggle データセットで裏づける図も掲載しています。

## 押さえどころ

- 表データ・GBDT はコンペの共通言語として今も生き続けている。Titanic の後継として月次開催された Tabular Playground Series がその象徴で、初学者の入口という役割は形を変えて続いている。一方でメダル対象コンペに限ると、表データの構成比は 2015 年の 8 割超から 2020 年代半ばには 1〜2 割へと下がっており、主戦場が月次の Playground 側へ移ったことがうかがえる（下図）
- 2019〜2021 年にかけて、[表データコンペ](./tabular.md)と並走する形で[画像認識コンペ](./image-recognition.md)・[自然言語処理コンペ](./nlp-llm.md)が本格的な柱になった。メダル対象コンペでも同区間は画像が最大種別で、2019 年は 27 件中 14 件と過半を占めた。同時期に「学習済みモデルと推論コードをノートブックとして提出する」[コードコンペティション](./code-competition.md)形式の導入が進み、実行時間制限・オフライン実行という制約が戦い方を変えた
- 「値の予測」ではなく「エージェントを提出して対戦する」Simulation Competitions は、実は 2018〜2021 年の Halite・Connect X・Lux AI・Hungry Geese の頃から存在する古参の形式。実データでもシミュレーション系のコンペは 2020〜2021 年にまとまって現れる。この時期はまだ強化学習中心の一分野という位置づけだった（[エージェント対戦コンペ](./agent-competition.md)）
- 2022〜2023 年は表・画像・NLP のどれが主流とも言えない並走期。[表データコンペ](./tabular.md)では「深層学習 vs 決定木」論争が続く一方、NLP 側では LLM によるデータ生成・水増しが精度向上の主要な手段として台頭し始めた
- 2023〜2025 年で LLM が戦い方そのものに入り込んだ。NLP コンペはエンコーダ型（BERT・DeBERTa 系）からデコーダ型 LLM への移行が明確になり、メダル対象コンペではテキスト（NLP）が 2024 年に単年最大種別（8 件）へ伸びて画像と入れ替わった。同時に AI コーディングエージェントが「惨敗」（2023 年、ChatGPT Code Interpreter）から「上位 30%」（2025 年、Claude Code）へとわずか 2 年で実用性を急速に高めた（[AI エージェント活用](./ai-agent.md)）
- 2025〜2026 年、初期の Simulation Competitions の系譜が新しい意味を持ち始めている。公式ゲームエンジン提供の大型対戦コンペや、Kaggle 自身が運営するモデル評価基盤「Game Arena」の登場により、対戦型コンペは実験的な一形式から、フロンティアモデルを評価する中心的な仕組みへと役割を広げた。データ上もシミュレーションは 2025 年に再登場し、マルチモーダルも 2024〜2025 年に初めて現れるなど、直近の多様化がうかがえる（[性能評価と検証](./evaluation-validation.md)も参照）
- 「その年に何が話題だったか」を振り返るアンケート・年次まとめ記事が 2020 年以降ほぼ毎年蓄積されており、技術動向を定点観測する材料になっている

## データで見る：メダル対象コンペのデータ種別構成（2015〜2026）

押さえどころで述べた変遷を、Kaggle 公式の Meta Kaggle データセットで裏づけます。メダル対象コンペ（`CanQualifyTiers` が真のもの）だけを抜き出し、締切年ごとにデータ種別の構成を集計しました。表データが最大種別だった時代から、画像（2017〜2021 年）・テキスト（2022 年以降）へと主役が移り、直近ではシミュレーション（対戦型）とマルチモーダルが加わる流れが見て取れます。「構成比」と「件数」を切り替えられ、棒にカーソルを合わせると内訳を表示します。データ種別はコンペタグからの推定である点に注意が必要で、より精緻な分類は人手でタグ付けした[コンペ参加録](../../solutions.md)のほうが正確です。なお末尾の 2026 年（`*`）は進行中の暫定値で、集計方法も他の年と異なります（図の下の注記を参照）。

<style>
#ce-fig { border: 1px solid #d0d7de; border-radius: 8px; padding: 16px 18px 18px; margin: 8px 0; }
#ce-fig .ce-toggle { display: inline-flex; background: #f6f8fa; border: 1px solid #d0d7de; border-radius: 8px; padding: 3px; margin-bottom: 12px; }
#ce-fig .ce-toggle button { font: inherit; font-size: 13px; color: #57606a; background: transparent; border: 0; padding: 6px 14px; border-radius: 6px; cursor: pointer; }
#ce-fig .ce-toggle button[aria-pressed="true"] { background: #fff; color: #1f2328; font-weight: 600; box-shadow: 0 1px 2px rgba(0,0,0,.1); }
#ce-legend { display: flex; flex-wrap: wrap; gap: 6px 14px; margin: 2px 0 12px; }
#ce-legend span { display: inline-flex; align-items: center; gap: 6px; font-size: 12px; color: #57606a; }
#ce-legend i { width: 11px; height: 11px; border-radius: 3px; display: inline-block; }
#ce-chart-wrap { overflow-x: auto; }
#ce-chart { display: block; width: 100%; height: auto; }
#ce-chart text { fill: #57606a; }
#ce-chart .ce-axis { stroke: #d0d7de; }
#ce-chart .ce-grid { stroke: #eff2f5; stroke-width: 1; }
#ce-chart rect.ce-seg { stroke: #fff; stroke-width: 2; transition: opacity .12s; }
#ce-chart rect.ce-seg.ce-prov { opacity: .58; }
#ce-chart rect.ce-seg.ce-dim { opacity: .24; }
#ce-chart text.ce-prov-mark { fill: #6e7781; font-style: italic; }
#ce-tip { position: fixed; z-index: 10; max-width: 240px; background: #fff; border: 1px solid #d0d7de; border-radius: 8px; padding: 8px 11px; box-shadow: 0 4px 12px rgba(0,0,0,.14); font-size: 12px; color: #57606a; pointer-events: none; display: none; line-height: 1.6; }
#ce-tip .ce-tt { font-weight: 600; color: #1f2328; }
#ce-tip .ce-tr { display: flex; align-items: center; gap: 6px; margin-top: 2px; }
#ce-tip .ce-tr i { width: 9px; height: 9px; border-radius: 2px; }
#ce-fig details { margin-top: 12px; }
#ce-fig summary { cursor: pointer; color: #57606a; font-size: 13px; }
#ce-fig table { border-collapse: collapse; font-size: 12px; margin-top: 10px; }
#ce-fig th, #ce-fig td { border: 1px solid #d0d7de; padding: 3px 7px; text-align: right; white-space: nowrap; }
#ce-fig th:first-child, #ce-fig td:first-child { text-align: left; }
#ce-fig th { background: #f6f8fa; color: #57606a; }
.ce-note { font-size: 12px; color: #6e7781; margin-top: 12px; }
</style>

<div id="ce-fig" markdown="0">
  <div class="ce-toggle" role="group" aria-label="表示切替">
    <button id="ce-btn-share" type="button" aria-pressed="true">構成比</button>
    <button id="ce-btn-count" type="button" aria-pressed="false">件数</button>
  </div>
  <div id="ce-legend"></div>
  <div id="ce-chart-wrap"></div>
  <details>
    <summary>データを表で見る（件数）</summary>
    <div style="overflow-x:auto"><table id="ce-table"></table></div>
  </details>
  <p class="ce-note">出典: Kaggle 公式 <code>Meta Kaggle</code>（2026-07-31 取得）。メダル対象は <code>CanQualifyTiers = true</code> で定義。年は締切年ベースで、単年の母数は 14〜27 件と小さいため構成比はぶれやすい。<br><b>2015〜2025 年</b>: データ種別はコンペタグ（<code>data type &gt; …</code> 等）からの機械的な集計で、タグの付かないコンペは除外している（タグ付き 245/326 件、カバー率 75%、2025 年は 52%）。<br><b>* 2026 年（暫定・要注意）</b>: 2026-07-31 時点で進行中の年で、コンペタグがまだ整備されていないため、<b>他の年と集計方法が異なり</b>、締切・タイトルから手作業で分類した。メダル対象 24 件のうち分類できた 18 件を集計し、データ種別の枠組みに馴染まない 6 件（数理最適化の Santa、分子構造予測の RNA 3D Folding、抽象推論の ARC-AGI-2／3、内容が判別しづらい NeuroGolf・Kaggriculture）は除外している。とくに ARC・AIMO のような大型の推論・エージェント系コンペは「データ種別」に収まりにくく、この図は 2026 年に進む推論・対戦型へのシフトを過小評価する（賞金規模では推論・エージェント・対戦型が 2026 年メダルコンペの約 8 割を占める）。年後半にコンペが追加され得る点も含め、2026 年は参考値として扱ってほしい。より精緻な分類は人手でタグ付けした<a href="../../solutions.md">コンペ参加録</a>のほうが正確。</p>
</div>
<div id="ce-tip" role="tooltip"></div>

<script>
(function () {
  var YEARS = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026];
  var PROVISIONAL = 2026;
  var MODS = ["tabular", "text", "image", "timeseries", "audio", "video", "multimodal", "simulation"];
  var JA = {
    tabular: "テーブル", text: "テキスト (NLP)", image: "画像", timeseries: "時系列",
    audio: "音声", video: "動画", multimodal: "マルチモーダル", simulation: "シミュレーション"
  };
  var COL = {
    tabular: "#2a78d6", text: "#008300", image: "#e87ba4", timeseries: "#eda100",
    audio: "#1baf7a", video: "#eb6834", multimodal: "#4a3aa7", simulation: "#e34948"
  };
  var BY = {
    tabular: [19, 17, 6, 4, 8, 3, 4, 7, 7, 3, 1, 4],
    text: [1, 1, 4, 1, 3, 4, 3, 7, 2, 8, 4, 4],
    image: [2, 6, 12, 10, 14, 11, 12, 9, 8, 5, 4, 5],
    timeseries: [1, 0, 0, 0, 0, 2, 0, 1, 2, 2, 2, 2],
    audio: [0, 0, 0, 0, 1, 1, 2, 1, 2, 1, 0, 1],
    video: [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    multimodal: [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    simulation: [0, 0, 0, 0, 0, 2, 3, 1, 1, 0, 2, 2]
  };
  var NS = "http://www.w3.org/2000/svg";
  var mode = "share";
  var wrap = document.getElementById("ce-chart-wrap");
  var legend = document.getElementById("ce-legend");
  var tip = document.getElementById("ce-tip");

  function svg(name, attrs) {
    var e = document.createElementNS(NS, name);
    for (var k in attrs) { e.setAttribute(k, attrs[k]); }
    return e;
  }
  function totalAt(i) {
    var s = 0;
    for (var m = 0; m < MODS.length; m++) { s += BY[MODS[m]][i]; }
    return s;
  }

  function render() {
    var W = 760, H = 400, mt = 14, mr = 14, mb = 32, ml = 36;
    var iw = W - ml - mr, ih = H - mt - mb;
    var share = mode === "share";
    var totals = YEARS.map(function (_, i) { return totalAt(i); });
    var maxTot = Math.max.apply(null, totals);
    var nice = share ? 100 : Math.ceil(maxTot / 5) * 5;
    var yOf = function (v) { return mt + ih - (v / nice) * ih; };
    var bw = iw / YEARS.length, bar = Math.min(38, bw * 0.66);
    var step = share ? 20 : (nice <= 15 ? 3 : 5);

    var s = svg("svg", { id: "ce-chart", viewBox: "0 0 " + W + " " + H, preserveAspectRatio: "xMinYMin meet" });

    for (var v = 0; v <= nice; v += step) {
      var y = yOf(v);
      s.appendChild(svg("line", { "class": "ce-grid", x1: ml, x2: W - mr, y1: y, y2: y }));
      var lt = svg("text", { x: ml - 6, y: y + 3, "text-anchor": "end", "font-size": 11 });
      lt.textContent = share ? v + "%" : v;
      s.appendChild(lt);
    }
    s.appendChild(svg("line", { "class": "ce-axis", x1: ml, x2: W - mr, y1: yOf(0), y2: yOf(0) }));

    YEARS.forEach(function (yr, i) {
      var cx = ml + bw * i + bw / 2, x = cx - bar / 2, acc = 0, tot = totals[i];
      MODS.forEach(function (k) {
        var raw = BY[k][i];
        if (raw <= 0) { return; }
        var val = share ? (tot ? raw / tot * 100 : 0) : raw;
        var y0 = yOf(acc), y1 = yOf(acc + val);
        acc += val;
        var r = svg("rect", { "class": (yr === PROVISIONAL ? "ce-seg ce-prov" : "ce-seg"), x: x, y: y1, width: bar, height: Math.max(0, y0 - y1), fill: COL[k] });
        r.setAttribute("data-k", k);
        attachTip(r, yr, k, raw, tot);
        s.appendChild(r);
      });
      var xl = svg("text", { x: cx, y: H - mb + 15, "text-anchor": "middle", "font-size": 10.5 });
      xl.textContent = "'" + String(yr).slice(2) + (yr === PROVISIONAL ? "*" : "");
      if (yr === PROVISIONAL) { xl.setAttribute("class", "ce-prov-mark"); }
      s.appendChild(xl);
      if (!share && tot > 0) {
        var tl = svg("text", { x: cx, y: yOf(tot) - 5, "text-anchor": "middle", "font-size": 10, "font-weight": 600, fill: "#6e7781" });
        tl.textContent = tot;
        s.appendChild(tl);
      }
    });

    wrap.textContent = "";
    wrap.appendChild(s);
    buildLegend();
  }

  function buildLegend() {
    legend.textContent = "";
    MODS.forEach(function (k) {
      var sp = document.createElement("span");
      var i = document.createElement("i");
      i.style.background = COL[k];
      sp.appendChild(i);
      sp.appendChild(document.createTextNode(JA[k]));
      legend.appendChild(sp);
    });
  }

  function segs() { return wrap.querySelectorAll("rect.ce-seg"); }

  function attachTip(r, yr, k, raw, tot) {
    r.addEventListener("mousemove", function (ev) {
      var all = segs();
      for (var j = 0; j < all.length; j++) {
        if (all[j].getAttribute("data-k") === k) { all[j].classList.remove("ce-dim"); }
        else { all[j].classList.add("ce-dim"); }
      }
      var pct = tot ? Math.round(raw / tot * 100) : 0;
      tip.textContent = "";
      var t = document.createElement("div");
      t.className = "ce-tt";
      t.textContent = yr + "年 ・ タグ付き " + tot + " 件";
      tip.appendChild(t);
      var row = document.createElement("div");
      row.className = "ce-tr";
      var ic = document.createElement("i");
      ic.style.background = COL[k];
      row.appendChild(ic);
      row.appendChild(document.createTextNode(JA[k] + ": " + raw + " 件 (" + pct + "%)"));
      tip.appendChild(row);
      tip.style.display = "block";
      var x = ev.clientX + 14;
      if (x + 250 > window.innerWidth) { x = ev.clientX - 250; }
      tip.style.left = Math.max(x, 8) + "px";
      tip.style.top = (ev.clientY + 14) + "px";
    });
    r.addEventListener("mouseleave", function () {
      tip.style.display = "none";
      var all = segs();
      for (var j = 0; j < all.length; j++) { all[j].classList.remove("ce-dim"); }
    });
  }

  function buildTable() {
    var t = document.getElementById("ce-table");
    var head = document.createElement("tr");
    head.appendChild(th("年"));
    MODS.forEach(function (k) { head.appendChild(th(JA[k])); });
    head.appendChild(th("計"));
    t.appendChild(head);
    YEARS.forEach(function (yr, i) {
      var tr = document.createElement("tr");
      tr.appendChild(td(yr, false));
      var tot = 0;
      MODS.forEach(function (k) {
        var v = BY[k][i];
        tot += v;
        tr.appendChild(td(v || "", false));
      });
      tr.appendChild(td(tot, true));
      t.appendChild(tr);
    });
  }
  function th(x) { var e = document.createElement("th"); e.textContent = x; return e; }
  function td(x, bold) {
    var e = document.createElement("td");
    if (bold) { var b = document.createElement("strong"); b.textContent = x; e.appendChild(b); }
    else { e.textContent = x; }
    return e;
  }

  function setMode(x) {
    mode = x;
    document.getElementById("ce-btn-share").setAttribute("aria-pressed", String(x === "share"));
    document.getElementById("ce-btn-count").setAttribute("aria-pressed", String(x === "count"));
    render();
  }
  document.getElementById("ce-btn-share").addEventListener("click", function () { setMode("share"); });
  document.getElementById("ce-btn-count").addEventListener("click", function () { setMode("count"); });

  buildTable();
  render();
})();
</script>

## 資料

### 表データ時代の名残・共通の入口

- [「Tabular Playground Series」の紹介記事](https://towardsdatascience.com/progressively-approaching-kaggle-f58db71a42a9?gi=32e36ede2a44): Titanic に代わる月次開催の練習用コンペを紹介する記事。
- [Tabular Playground Series 2021年4月分開始](https://www.kaggle.com/c/tabular-playground-series-apr-2021/): Titanic データに GAN を用いて生成したデータセットを使用。
- [BigQuery上の機械学習機能「BQML」の検証資料](https://speakerdeck.com/shimacos/bqmlkotohazime): Kaggle「Otto Group Product Classification Challenge」のデータを用いた検証結果。

### 深層学習化とコード提出形式の定着（2019〜2021年）

- [2010年以降のコンピュータビジョン分野の動向まとめ記事](https://gihyo.jp/dev/column/newyear/2021/computer-vision-trends): 深層学習による画像認識コンペの革新から近年の潮流までを解説。
- [「Code Competitions」形式のTipsまとめ記事](https://nonbiri-tereka.hatenablog.com/entry/2020/09/03/091530): 多くのコンペで導入が進む開催形式の攻略 Tips。
- [「Halite」AIコンペからの知見まとめ記事（2018年）](https://www.twosigma.com/insights/article/best-practices-from-building-a-machine-learning-bot-for-halite/): 「強化学習が必ずしも最良ではない」など至言をまとめた記事。
- [Kaggle「Halite by Two Sigma」強化学習体験談](https://threecourse.hatenablog.com/entry/2020/09/17/014155): ルールベースに対する難しさなどの所感を語る記事。

### 年次まとめ・定点観測

- [2020年の面白かったコンペ・論文に関する9人のKagglerアンケート記事](https://sorabatake.jp/18734/): 2020 年を振り返るアンケート結果のまとめ記事。
- [2021年の面白かったコンペと論文を7人のKagglerに調査した記事](https://sorabatake.jp/26199/): 回答者のコメントも併記した調査記事。
- [2022年時点での機械学習コンペの動向をまとめた記事](https://medium.com/machine-learning-insights/winning-approach-ml-competition-2022-b89ec512b1bb): プログラミング言語・上位解法アプローチ・利用ライブラリなどを可視化した記事。
- [Kaggleランカーの5人に聞いた、2023年面白かったコンペ5選と論文5選](https://sorabatake.jp/37130/): Grandmaster・Master 5 人へのアンケートをまとめた記事。
- [直近3年間のKaggle優勝解法を分析した記事](https://www.datarobot.com/jp/blog/is-deep-learning-almighty/): 非構造化データはディープラーニング、テーブルデータは勾配ブースティングという傾向を分析。
- [The State of Machine Learning Competitions 2025 Edition](https://mlcontests.com/state-of-machine-learning-competitions-2025/): 対戦トーナメント形式の導入を含む 2025 年のコンペ動向の年次まとめ。

### LLM・エージェントの主役化（2023〜2025年）

- [データコンペでCode Interpreter片手に戦ってみたけど惨敗でした](https://zenn.dev/karaage0703/articles/1fa0a14d4cdd63): ChatGPT の Code Interpreter でコミュニティコンペに挑んだ 2023 年の初期事例。
- [Claude Code と Kaggle をやったら何も考えずに上位30%になれた話](https://zenn.dev/genda_jp/articles/20250909_kaggle_with_claude_code): エージェントに任せた場合の到達点と限界、MLflow・GitHub を使った協働体制の実験報告。
- [Agent時代のKaggleで、人間は何を見るべきか (関西kaggler会 2026.5.22)](https://speakerdeck.com/chihironakayama/agentshi-dai-nokagglede-ren-jian-hahe-wojian-rubekika-guan-xi-kagglerhui-2026-dot-5-22): エージェントによるコーディングが普及した時代の Kaggle の変化と人間の役割を論じる発表資料。

### 対戦型・評価基盤としての定着（2025〜2026年）

- [The Pokémon Company - PTCG AI Battle Challenge Simulation](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle): ポケモンカードゲームの対戦 AI を競う大型コンペ（Simulation Track）。
- [Kaggle Game Arena evaluates AI models through games](https://blog.google/innovation-and-ai/products/kaggle-game-arena/): モデル同士をゲームで対戦させる評価基盤 Game Arena の公式発表。
- [Game Arena: Poker and Werewolf, and Gemini 3 tops chess](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/kaggle-game-arena-updates/): ポーカー・人狼ベンチマークの追加とチェストーナメント結果の続報。
- [AtCoder World Tour Finals 2025 に OpenAI がスポンサーとして参画](https://prtimes.jp/main/html/rd/p/000000059.000028415.html): 「人間 vs AI」のエキシビションが行われた競技プログラミングイベントの発表。

## 関連概念

- [表データコンペ](./tabular.md) / [画像認識コンペ](./image-recognition.md) / [自然言語処理コンペ](./nlp-llm.md) / [コードコンペティション](./code-competition.md) / [エージェント対戦コンペ](./agent-competition.md) / [AI エージェント活用](./ai-agent.md) / [性能評価と検証](./evaluation-validation.md)
