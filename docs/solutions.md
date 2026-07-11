# コンペ解法

本ページでは、コンペの解法に関する情報を掲載します。

## Kaggle 公式

- Discussion: Kaggle コンペごとに、参加者が投稿した解法が Discussion で閲覧できます。順位表の「Solution」から個別の投稿に遷移できます。
- [YouTube](https://www.youtube.com/kaggle): 定期的に解法動画が公開されています。
- [DOIs for Competition and Project Writeups](https://www.kaggle.com/discussions/product-announcements/705158): 個別の解法（Writeup）に DOI を付与できます。論文などからの引用に利用できます。

## 有志によるコンペ解法一覧サイト

- [Kaggle Solution Search](https://compsearch.dev/)
- [Kaggle Solutions](https://farid.one/kaggle-solutions/)
- [Kaggle Past Solutions](https://ndres.me/kaggle-past-solutions/)

## コンペ参加録

<style>
.filter-container {
  background: #f5f5f5;
  padding: 16px;
  border-radius: 8px;
  margin-bottom: 24px;
}
.filter-row {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  align-items: center;
}
.filter-group {
  display: flex;
  flex-direction: column;
  gap: 4px;
}
.filter-group label {
  font-size: 12px;
  font-weight: bold;
  color: #666;
}
.filter-group select {
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 14px;
  min-width: 150px;
}
.filter-actions {
  display: flex;
  align-items: flex-end;
  gap: 12px;
}
.reset-btn {
  padding: 8px 16px;
  background: #e0e0e0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
}
.reset-btn:hover {
  background: #d0d0d0;
}
.result-count {
  font-size: 14px;
  color: #666;
  margin-left: auto;
}
.competition-entry {
  margin-bottom: 24px;
  padding-bottom: 16px;
  border-bottom: 1px solid #eee;
}
.competition-entry.hidden {
  display: none;
}
.competition-entry h3 {
  margin-bottom: 8px;
}
.badge {
  display: inline-block;
  padding: 2px 8px;
  font-size: 11px;
  border-radius: 12px;
  margin-right: 4px;
  margin-bottom: 8px;
}
.badge-year {
  background: #e3f2fd;
  color: #1565c0;
}
.badge-datatype {
  background: #f3e5f5;
  color: #7b1fa2;
}
.badge-platform {
  background: #e8f5e9;
  color: #2e7d32;
}
@media (max-width: 600px) {
  .filter-row {
    flex-direction: column;
    align-items: stretch;
  }
  .filter-group select {
    width: 100%;
  }
  .result-count {
    margin-left: 0;
    margin-top: 8px;
  }
}
</style>

<div class="filter-container">
  <div class="filter-row">
    <div class="filter-group">
      <label>データ種類</label>
      <select id="filter-datatype">
        <option value="">すべて</option>
        <option value="tabular">Tabular</option>
        <option value="image">Image</option>
        <option value="text">Text/NLP</option>
        <option value="audio">Audio</option>
        <option value="timeseries">Time Series</option>
        <option value="video">Video</option>
        <option value="3d">3D</option>
        <option value="multimodal">Multimodal</option>
        <option value="other">Other</option>
      </select>
    </div>
    <div class="filter-group">
      <label>開催年</label>
      <select id="filter-year">
        <option value="">すべて</option>
        <option value="2026">2026</option>
        <option value="2025">2025</option>
        <option value="2024">2024</option>
        <option value="2023">2023</option>
        <option value="2022">2022</option>
        <option value="2021">2021</option>
        <option value="2020">2020</option>
        <option value="2019">2019以前</option>
      </select>
    </div>
    <div class="filter-group">
      <label>プラットフォーム</label>
      <select id="filter-platform">
        <option value="">すべて</option>
        <option value="kaggle">Kaggle</option>
        <option value="atmacup">atmaCup</option>
        <option value="signate">SIGNATE</option>
        <option value="nishika">Nishika</option>
        <option value="other">その他</option>
      </select>
    </div>
    <div class="filter-actions">
      <button class="reset-btn" onclick="resetFilters()">リセット</button>
      <span class="result-count"><span id="visible-count">0</span> 件表示</span>
    </div>
  </div>
</div>

<div id="competition-list">

<div class="competition-entry" markdown="1" data-year="2026" data-datatype="image" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/physionet-ecg-image-digitization">PhysioNet - Digitization of ECG Images</a></h3>
<span class="badge badge-year">2026</span> <span class="badge badge-datatype">Image</span> <span class="badge badge-platform">Kaggle</span>

- [kaggle PhysioNetコンペ　上位解法まとめ](https://zenn.dev/yume_neko/articles/54304df1bcb17d): 心電図画像から時系列データを抽出するコンペの上位解法まとめ。

</div>

<div class="competition-entry" markdown="1" data-year="2026" data-datatype="image" data-platform="atmacup">
<h3><a href="https://www.guruguru.science/competitions/31">Turing × atmaCup 2nd（atmaCup #23）</a></h3>
<span class="badge badge-year">2026</span> <span class="badge badge-datatype">Image</span> <span class="badge badge-platform">atmaCup</span>

- [Turing x atmaCup #23 2nd Place Solution](https://speakerdeck.com/k951286/atmacup23-2nd-place-dot-pptx): 車載カメラ画像から位置（緯度経度）を推定するコンペの 2 位解法。
- [atmaCup #23でAIコーディングを活用した話](https://speakerdeck.com/ml_bear/atmacup-number-23deaikodeinguwohuo-yong-sitahua): AI コーディングを駆使した 3 位解法。

</div>

<div class="competition-entry" markdown="1" data-year="2025" data-datatype="text" data-platform="atmacup">
<h3><a href="https://www.guruguru.science/competitions/28">#21 atmaCup in collaboration with Elith</a></h3>
<span class="badge badge-year">2025</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">atmaCup</span>

- [LLM Securityコンペ（#21 atmaCup）に参加してみた！](https://qiita.com/Isaka-code/items/fa73084e839ca778de4f): LLM のセキュリティを題材にしたコンペの参加録。

</div>

<div class="competition-entry" markdown="1" data-year="2025" data-datatype="other" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/santa-2025">Santa 2025 - Christmas Tree Packing Challenge</a></h3>
<span class="badge badge-year">2025</span> <span class="badge badge-datatype">Other</span> <span class="badge badge-platform">Kaggle</span>

- [サンタコンペ2025完全攻略 ～お前らの焼きなましは遅すぎる～](https://speakerdeck.com/terryu16/santakonpe2025wan-quan-gong-lue-oqian-ranoshao-kinamasihachi-sugiru): 初期解の構築と巨大近傍焼きなましに焦点を当てた 2 位解法。

</div>

<div class="competition-entry" markdown="1" data-year="2026" data-datatype="3d" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/vesuvius-challenge-surface-detection">Vesuvius Challenge - Surface Detection</a></h3>
<span class="badge badge-year">2026</span> <span class="badge badge-datatype">3D</span> <span class="badge badge-platform">Kaggle</span>

- [Kaggleの火山コンペで12位、金メダルを獲得しました](https://blog.recruit.co.jp/data/articles/kaggle_vesvius/): 3 次元 X 線スキャンからインクを検出し巻物の中身を読み取るコンペの金メダル解法。
- [kaggle Vesuvius Challenge - Surface Detection速報まとめ](https://speakerdeck.com/sugupoko/vesuvius2-combined): 18 位解法と上位解法の解説を含む速報まとめ。

</div>

<div class="competition-entry" markdown="1" data-year="2026" data-datatype="image" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/csiro-biomass">CSIRO - Image2Biomass Prediction</a></h3>
<span class="badge badge-year">2026</span> <span class="badge badge-datatype">Image</span> <span class="badge badge-platform">Kaggle</span>

- [Claude Code / CodexでKaggle金メダルを取った話](https://zenn.dev/chiman/articles/b233cc808d6af3): 生成 AI を用いた開発方法と役割分担を詳述する金メダル解法。
- [草コンペ振り返り](https://speakerdeck.com/chihironakayama/cao-konhezhen-rifan-ri): 牧草画像から飼料の量を予測するコンペの 5 位解法。
- [Kaggle 草コンペ振り返り & 上位解法まとめ | CSIRO - Image2Biomass Prediction](https://zenn.dev/prgckwb/articles/kaggle-csiro-image2biomass)

</div>

<div class="competition-entry" markdown="1" data-year="2026" data-datatype="multimodal" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/med-gemma-impact-challenge">The MedGemma Impact Challenge</a></h3>
<span class="badge badge-year">2026</span> <span class="badge badge-datatype">Multimodal</span> <span class="badge badge-platform">Kaggle</span>

- [Kaggle MedGemma Impact Challenge 全解剖：受賞9件＋落選30件から学ぶ医療AI開発](https://zenn.dev/sugupoko/articles/e93bfcbfa95409): 医療 AI ハッカソンの受賞作 9 件と落選作を横断したまとめ記事。

</div>

<div class="competition-entry" markdown="1" data-year="2026" data-datatype="text" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/deep-past-initiative-machine-translation">Deep Past Challenge - Translate Akkadian to English</a></h3>
<span class="badge badge-year">2026</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">Kaggle</span>

- [Kaggle アッカド語コンペの振り返りと1位解法 + α の紹介](https://zenn.dev/ihiratch/articles/3f8a1d2873ebca): アッシリア楔形文字の機械翻訳コンペの振り返りと 1 位解法の紹介。

</div>

<div class="competition-entry" markdown="1" data-year="2026" data-datatype="image" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/recodai-luc-scientific-image-forgery-detection/">Recod.ai/LUC - Scientific Image Forgery Detection</a></h3>
<span class="badge badge-year">2026</span> <span class="badge badge-datatype">Image</span> <span class="badge badge-platform">Kaggle</span>

- [科学論文の不正画像を検出！Kaggle Recod.ai/LUC メモ[編集中・更新予定]](https://zenn.dev/yuki16/articles/27a60b48fa1e11): 生物医学研究の画像の偽造を検出するコンペの概要と上位解法のまとめ。

</div>

<div class="competition-entry" markdown="1" data-year="2026" data-datatype="text" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/ai-mathematical-olympiad-progress-prize-3">AI Mathematical Olympiad - Progress Prize 3</a></h3>
<span class="badge badge-year">2026</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">Kaggle</span>

- [SOTAのさらに先へ：厳しい推論制約下での高性能モデルのPost-Training](https://speakerdeck.com/analokmaus/sotanosaranixian-he-yan-siitui-lun-zhi-yue-xia-denogao-xing-neng-moderunopost-training): 数式を解く AI を開発するコンペの参加録。推論制約下での post-training を扱う。

</div>

<div class="competition-entry" markdown="1" data-year="2026" data-datatype="3d" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/stanford-rna-3d-folding-2">Stanford RNA 3D Folding Part 2</a></h3>
<span class="badge badge-year">2026</span> <span class="badge badge-datatype">3D</span> <span class="badge badge-platform">Kaggle</span>

- [Stanford RNA 3D Folding Part 2：上位3解法から読み解くRNA立体構造予測の現在地](https://zenn.dev/sasaki_kanji/articles/8daa2cfe3a361e): RNA の 3 次元構造を配列のみから予測するコンペの上位 3 解法まとめ。
- [【Kaggle】Stanford RNA 3D Folding Part 2 上位解法メモ：TBMと次世代AIモデルが拓くRNA立体構造予測](https://zenn.dev/yuki16/articles/36fb38f9b9e244)

</div>

<div class="competition-entry" markdown="1" data-year="2026" data-datatype="audio" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/birdclef-2026">BirdCLEF+ 2026</a></h3>
<span class="badge badge-year">2026</span> <span class="badge badge-datatype">Audio</span> <span class="badge badge-platform">Kaggle</span>

- [【Kaggle】BirdCLEF+ 2026 参加記録(🥈31位)](https://zenn.dev/dalab/articles/7ea7584b75af39): 毎年恒例の鳥の鳴き声認識コンペの銀メダル解法。

</div>

<div class="competition-entry" markdown="1" data-year="2026" data-datatype="text" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/nvidia-nemotron-model-reasoning-challenge">NVIDIA Nemotron Model Reasoning Challenge</a></h3>
<span class="badge badge-year">2026</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">Kaggle</span>

- [Kaggleコンペ紹介：NVIDIA Nemotron Model Reasoning Challenge](https://zenn.dev/mkj/articles/3a4d70ac4e8fb4): LLM「Nemotron-3-Nano-30B」の推論性能改善に取り組むコンペの金メダル解法。
- [振り返り動画（NVIDIA 所属 Kaggle Grandmaster）](https://www.youtube.com/watch?v=hJ_blKSJbU4)

</div>

<div class="competition-entry" markdown="1" data-year="2025" data-datatype="image" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/image-matching-challenge-2025">Image Matching Challenge 2025</a></h3>
<span class="badge badge-year">2025</span> <span class="badge badge-datatype">Image</span> <span class="badge badge-platform">Kaggle</span>

- [Kaggle Image Matching Challenge 2025 紹介](https://www.docswell.com/s/7056084/K7EPVD-2025-07-14-153705)
- [Image Matching Challenge 2025 振り返り会で発表してきた](https://ho.lc/blog/image-matching-challenge-2025): 7 位チームの発表資料つきの振り返り会参加録。
- [Image Matching Challenge 2025 参加記](https://www.ariseanalytics.com/tech-info/20250822)
- [kaggle IMC2025コンペ　上位解法まとめ](https://zenn.dev/yume_neko/articles/bee802ebf8b4d0)
- [20250714_IMC2025振り返り会_Team_Sony_Matching](https://speakerdeck.com/muku_8949/20250714-imc2025zhen-rifan-rihui-team-sony-matching)
- [IMC2025振り返り会　How can we win at IMC2025?](https://speakerdeck.com/yumeneko/imc2025zhen-rifan-rihui-how-can-we-win-at-imc2025)

</div>

<div class="competition-entry" markdown="1" data-year="2025" data-datatype="timeseries" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/ariel-data-challenge-2025">NeurIPS - Ariel Data Challenge 2025</a></h3>
<span class="badge badge-year">2025</span> <span class="badge badge-datatype">Time Series</span> <span class="badge badge-platform">Kaggle</span>

- [NeurIPS - Ariel Data Challenge 2025の振り返り](https://takaito0423.hatenablog.com/entry/2025/09/26/000201)
- [NeurIPS - Ariel Data Challenge 2025の振り返り](https://horikitasaku.github.io/jp/posts/adc2025/): 系外惑星のスペクトル回復コンペの金メダル獲得者による振り返り。

</div>

<div class="competition-entry" markdown="1" data-year="2025" data-datatype="text" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/llms-you-cant-please-them-all/">LLMs - You Can't Please Them All</a></h3>
<span class="badge badge-year">2025</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">Kaggle</span>

- [【振り返りメモ】LLMs - You Can't Please Them All](https://zenn.dev/mytm/articles/d766e49b77a3c4): 3 つの LLM の評価の不一致を最大化するコンペの概要と上位解法の紹介。

</div>

<div class="competition-entry" markdown="1" data-year="2025" data-datatype="text" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/openai-gpt-oss-20b-red-teaming">Red‑Teaming Challenge - OpenAI gpt-oss-20b</a></h3>
<span class="badge badge-year">2025</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">Kaggle</span>

- [【受賞手法解説】OpenAI主催のセキュリティコンペで発見した脆弱性について解説](https://note.com/lively_phlox2856/n/n8dd8a9940b96)

</div>

<div class="competition-entry" markdown="1" data-year="2025" data-datatype="text" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/make-data-count-finding-data-references">Make Data Count - Finding Data References</a></h3>
<span class="badge badge-year">2025</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">Kaggle</span>

- [Kaggleコンペ紹介：Make Data Count - Finding Data References](https://zenn.dev/mkj/articles/0d42ec3db44749)

</div>

<div class="competition-entry" markdown="1" data-year="2025" data-datatype="tabular" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/nfl-big-data-bowl-2026-prediction">NFL Big Data Bowl 2026 - Prediction</a></h3>
<span class="badge badge-year">2025</span> <span class="badge badge-datatype">Tabular</span> <span class="badge badge-platform">Kaggle</span>

- [第5会 関東kaggler会 NFLコンペ 2026 解法紹介](https://speakerdeck.com/ohkawa3/di-5hui-guan-dong-kagglerhui-nflkonpe-2026-jie-fa-shao-jie)
- [NFLコンペ2026 解法](https://speakerdeck.com/lycorptech_jp/20260526b): ボールが空中にある間の選手の動きを予測するコンペの金メダル解法。
- [初めてプロジェクト起因で参加したkaggle - NFL2026 ふりかえり -](https://www.docswell.com/s/DeNA_Tech/5DWYXG-2026-02-25-152109): 5 位解法。生成 AI の活用事例も含む振り返り。
- [NFL Big Data Bowl 2026 - Prediction 上位解法MEMO](https://zenn.dev/ottantachinque/articles/2025-12-05_nfl-big-data-bowl-2026-predition)

</div>

<div class="competition-entry" markdown="1" data-year="2025" data-datatype="text" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/jigsaw-agile-community-rules/">Jigsaw - Agile Community Rules Classification</a></h3>
<span class="badge badge-year">2025</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">Kaggle</span>

- [Jigsaw - Agile Community Rules Classificationのまとめ](https://takaito0423.hatenablog.com/entry/2025/12/29/000232)
- [Kaggle - Jigsawコンペ振り返りメモ](https://zenn.dev/hasibirok0/articles/adb47c6df37ca6)

</div>

<div class="competition-entry" markdown="1" data-year="2025" data-datatype="3d" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/stanford-rna-3d-folding">Stanford RNA 3D Folding</a></h3>
<span class="badge badge-year">2025</span> <span class="badge badge-datatype">3D</span> <span class="badge badge-platform">Kaggle</span>

- [Kaggle - Stanford RNA 3D Folding コンペ 上位解法](https://qiita.com/Isaao/items/8a14b41a42e4b3227e93)

</div>

<div class="competition-entry" markdown="1" data-year="2025" data-datatype="tabular" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/neurips-open-polymer-prediction-2025">NeurIPS - Open Polymer Prediction 2025</a></h3>
<span class="badge badge-year">2025</span> <span class="badge badge-datatype">Tabular</span> <span class="badge badge-platform">Kaggle</span>

- [NeurIPS - Open Polymer Prediction 2025 反省会](https://speakerdeck.com/calpis10000/kaggle-neurips-open-polymer-prediction-2025-konpe-fan-sheng-hui)
- [NeurIPS Polymer 2025 上位解法の追試してみた話](https://zenn.dev/amana/articles/neurips-polymer-2025): 優勝解法の再現をコード付きで試みる記事。

</div>

<div class="competition-entry" markdown="1" data-year="2025" data-datatype="text" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/map-charting-student-math-misunderstandings">MAP - Charting Student Math Misunderstandings</a></h3>
<span class="badge badge-year">2025</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">Kaggle</span>

- [Kaggle コンペ紹介：MAP - Charting Student Math Misunderstandings](https://zenn.dev/mkj/articles/1f374627377474)
- [Kaggle銀メダル獲得に向けた実験管理の工夫](https://aitc.dentsusoken.com/column/how-to-approach-kaggle-competitions/): 銀メダル獲得までの取り組みを時系列で紹介する振り返り。
- [Kaggle MAPコンペのオリジナルデータと合成データの比較](https://qiita.com/Isaka-code/items/acc18a6798b3ffb6bdfb): 7 位解法で用いた合成データ作成の解説記事。

</div>

<div class="competition-entry" markdown="1" data-year="2025" data-datatype="audio" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/birdclef-2025">BirdCLEF+ 2025</a></h3>
<span class="badge badge-year">2025</span> <span class="badge badge-datatype">Audio</span> <span class="badge badge-platform">Kaggle</span>

- [BirdCLEF+2025 Noir 5位解法紹介](https://speakerdeck.com/myso/birdclef-plus-2025-noir-5wei-jie-fa-shao-jie)
- [なぜ俺は銀メダルなのか 25th solutionから⾦メダルへとの差分考える「BirdCLEF2025振り返り」](https://speakerdeck.com/ryushi496/nazean-hayin-medarunanoka-25th-solutionkara-medaruhetonochai-fen-kao-eru-birdclef2025zhen-rifan-ri)

</div>

<div class="competition-entry" markdown="1" data-year="2025" data-datatype="multimodal" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/drawing-with-llms">Drawing with LLMs</a></h3>
<span class="badge badge-year">2025</span> <span class="badge badge-datatype">Multimodal</span> <span class="badge badge-platform">Kaggle</span>

- [Kaggle Drawing with LLMs 振り返り & 上位解法まとめ](https://zenn.dev/prgckwb/articles/kaggle-dwllm)
- [【解法紹介】Drawing with LLMs](https://www.rist.co.jp/kaggleshowcase/202506107947/)

</div>

<div class="competition-entry" markdown="1" data-year="2025" data-datatype="text" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/ai-mathematical-olympiad-progress-prize-2">AI Mathematical Olympiad - Progress Prize 2</a></h3>
<span class="badge badge-year">2025</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">Kaggle</span>

- [Towards a More Efficient Reasoning LLM: AIMO2 Solution](https://speakerdeck.com/analokmaus/towards-a-more-efficient-reasoning-llm-aimo2-solution-summary-and-introduction-to-fast-math-models)
- [教師あり学習と強化学習で作る 最強の数学特化LLM](https://speakerdeck.com/analokmaus/jiao-shi-arixue-xi-toqiang-hua-xue-xi-dezuo-ru-zui-qiang-noshu-xue-te-hua-llm): SFT と強化学習による数学特化 LLM の性能改善を解説する資料。
- [AIMO-2 Winning Solution: Building State-of-the-Art Mathematical Reasoning Models with OpenMathReasoning dataset](https://arxiv.org/abs/2504.16891): 優勝解法をデータセット・学習済みモデルと合わせて公開した論文。

</div>

<div class="competition-entry" markdown="1" data-year="2025" data-datatype="tabular" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/equity-post-HCT-survival-predictions">CIBMTR - Equity in post-HCT Survival Predictions</a></h3>
<span class="badge badge-year">2025</span> <span class="badge badge-datatype">Tabular</span> <span class="badge badge-platform">Kaggle</span>

- [Kaggle CIBMTRコンペ1位解法まとめ〜感想を添えて〜](https://zenn.dev/knkmt/articles/9b081f458444b4)
- [CIBMTR上位解法MEMO](https://zenn.dev/ottantachinque/articles/2025-03-08_cibmtr-top-solution)
- [CIBMTR振り返り＋敗北から学ぶコンペの取り組み方反省](https://speakerdeck.com/takanao/cibmtrzhen-rifan-ri-plus-bai-bei-karaxue-bukonpenoqu-rizu-mifang-fan-sheng)
- [GBDT系モデルで生存予測分析](https://zenn.dev/sqrt4kaido/articles/328f92a6a41dbe)

</div>

<div class="competition-entry" markdown="1" data-year="2025" data-datatype="3d" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/czii-cryo-et-object-identification">CZII - CryoET Object Identification</a></h3>
<span class="badge badge-year">2025</span> <span class="badge badge-datatype">3D</span> <span class="badge badge-platform">Kaggle</span>

- [CZII - CryoET Object Identification 参加振り返り・解法共有](https://speakerdeck.com/tattaka/czii-cryoet-object-identification-can-jia-zhen-rifan-rijie-fa-gong-you)
- [Kaggle CZII コンペ上位解法まとめ](https://zenn.dev/508shuto/articles/d6374f134b282c)
- [CZII コンペ振り返り](https://speakerdeck.com/sugupoko/cziikonpezhen-rifan-ri-guan-xi-kagglerhui-jiao-liu-hui-in-osaka-2025-number-1)

</div>

<div class="competition-entry" markdown="1" data-year="2025" data-datatype="text" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/wsdm-cup-multilingual-chatbot-arena">WSDM Cup - Multilingual Chatbot Arena</a></h3>
<span class="badge badge-year">2025</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">Kaggle</span>

- [Kaggle WSDM Cup 参加記録](https://zenn.dev/dalab/articles/d0e6938bf50db1)

</div>

<div class="competition-entry" markdown="1" data-year="2025" data-datatype="timeseries" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/cmi-detect-behavior-with-sensor-data">CMI - Detect Behavior with Sensor Data</a></h3>
<span class="badge badge-year">2025</span> <span class="badge badge-datatype">Time Series</span> <span class="badge badge-platform">Kaggle</span>

- [2025 CMI - Detect Behavior with Sensor Data 大反省備忘録](https://qiita.com/humanbeans893/items/3b2e5fddffe883646e31)

</div>

<div class="competition-entry" markdown="1" data-year="2025" data-datatype="tabular" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/march-machine-learning-mania-2025">March Machine Learning Mania 2025</a></h3>
<span class="badge badge-year">2025</span> <span class="badge badge-datatype">Tabular</span> <span class="badge badge-platform">Kaggle</span>

- [ド文系だった私が、 KaggleのNCAAコンペでソロ金取れるまで](https://speakerdeck.com/wakamatsu_takumu/dowen-xi-datutasi-ga-kagglenoncaakonpedesorojin-qu-rerumade)

</div>

<div class="competition-entry" markdown="1" data-year="2025" data-datatype="timeseries" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/waveform-inversion">Yale/UNC-CH - Geophysical Waveform Inversion</a></h3>
<span class="badge badge-year">2025</span> <span class="badge badge-datatype">Time Series</span> <span class="badge badge-platform">Kaggle</span>

- [Geophysical Waveform Inversion 上位解法MEMO](https://zenn.dev/ottantachinque/articles/2025-07-03_waveform-inversion-top-solution)

</div>

<div class="competition-entry" markdown="1" data-year="2024" data-datatype="text" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/llm-20-questions">LLM 20 Questions</a></h3>
<span class="badge badge-year">2024</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">Kaggle</span>

- [Kaggle LLM 20 Questionsの解説と上位ソリューションまとめ](https://qiita.com/Isaka-code/items/9b19b588f36c54845aa0)

</div>

<div class="competition-entry" markdown="1" data-year="2024" data-datatype="tabular" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/leap-atmospheric-physics-ai-climsim">LEAP - Atmospheric Physics using AI (ClimSim)</a></h3>
<span class="badge badge-year">2024</span> <span class="badge badge-datatype">Tabular</span> <span class="badge badge-platform">Kaggle</span>

- [Kaggle LEAP Competition Solution解説&振り返り](https://speakerdeck.com/abeja/kaggle-leap-competition-solutionjie-shuo-and-zhen-rifan-ri)

</div>

<div class="competition-entry" markdown="1" data-year="2024" data-datatype="text" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/eedi-mining-misconceptions-in-mathematics">Eedi - Mining Misconceptions in Mathematics</a></h3>
<span class="badge badge-year">2024</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">Kaggle</span>

- [Kaggle Eedi - Mining Misconceptions in Mathematics 振り返り](https://zenn.dev/mkj/articles/a6e26546e31439)
- [Eediコンペ参戦記](https://www.docswell.com/s/kaeru_nantoka/53GLVL-2025-02-13-182323)
- [Kaggle Eedi 参加記録](https://zenn.dev/dalab/articles/e56f7691cc7c8d)
- [Kaggleコンペティション「Eedi – Mining Misconceptions in Mathematics」で得られた学び](https://tech.andpad.co.jp/entry/2025/01/08/100000)
- [【解法紹介】Eedi – Mining Misconceptions in Mathematics](https://www.rist.co.jp/kaggleshowcase/202502047619/)
- [Kaggle Solution Walkthroughs: Eedi - Mining Misconceptions in Mathematics with Team MTH 101](https://youtu.be/xCLMZT4pHQM?si=5OPjfQS9E06b9vvr)

</div>

<div class="competition-entry" markdown="1" data-year="2024" data-datatype="timeseries" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/ariel-data-challenge-2024">NeurIPS - Ariel Data Challenge 2024</a></h3>
<span class="badge badge-year">2024</span> <span class="badge badge-datatype">Time Series</span> <span class="badge badge-platform">Kaggle</span>

- [NeurIPS - Ariel Data Challenge 2024 振り返り](https://www.docswell.com/s/6883279/K1RXRP-2024-11-08-162001)

</div>

<div class="competition-entry" markdown="1" data-year="2024" data-datatype="tabular" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/um-game-playing-strength-of-mcts-variants/">UM - Game-Playing Strength of MCTS Variants</a></h3>
<span class="badge badge-year">2024</span> <span class="badge badge-datatype">Tabular</span> <span class="badge badge-platform">Kaggle</span>

- [UM - Game-Playing Strength of MCTS Variants 11th Place Solution](https://speakerdeck.com/ryushi496/um-game-playing-strength-of-mcts-variants-11th-place-solution)
- [モンテカルロ木探索のパフォーマンスを予測する Kaggleコンペ解説 〜生成AIによる未知のゲーム生成〜](https://speakerdeck.com/rist/solution-um-game-playing-strength-of-mcts-variants): コンペ概要と取り組みの紹介資料。
- [Kaggleコンペ「UM - Game-Playing Strength of MCTS Variants 」3位入賞解法徹底解説](https://qiita.com/DataRobot_PR/items/7e8195d1bcd11394ccaa)
- [kaggle(UM-MCTSコンペ)振り返り(11th Place) &上位解法](https://zenn.dev/ryushi496/articles/ddd480808f6a86)

</div>

<div class="competition-entry" markdown="1" data-year="2024" data-datatype="other" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/lux-ai-season-3">NeurIPS 2024 - Lux AI Season 3</a></h3>
<span class="badge badge-year">2024</span> <span class="badge badge-datatype">Other</span> <span class="badge badge-platform">Kaggle</span>

- [kaggle Lux AI Season 3 強化学習ソリューションまとめ＋振り返り](https://zenn.dev/kurupical/articles/61dbeedf89a29d)

</div>

<div class="competition-entry" markdown="1" data-year="2024" data-datatype="other" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/santa-2024">Santa 2024 - The Perplexity Permutation Puzzle</a></h3>
<span class="badge badge-year">2024</span> <span class="badge badge-datatype">Other</span> <span class="badge badge-platform">Kaggle</span>

- [Santa2024上位解法MEMO](https://zenn.dev/ottantachinque/articles/2025-02-01_santa2024-top-solution)
- [毎年恒例のSanta2024に挑戦｜Kaggleチャレンジ記録](https://tech.aru-zakki.com/kaggle-santa2024/)
- [Santaコンペ + 焼きなまし法入門](https://speakerdeck.com/nocchi1/santakonpe-plus-shao-kinamasifa-ru-men-975c112e-10de-4043-a38f-c40268674899)

</div>

<div class="competition-entry" markdown="1" data-year="2024" data-datatype="image" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/rsna-2024-lumbar-spine-degenerative-classification">RSNA 2024 Lumbar Spine Degenerative Classification</a></h3>
<span class="badge badge-year">2024</span> <span class="badge badge-datatype">Image</span> <span class="badge badge-platform">Kaggle</span>

- [RSNA2024振り返り](https://speakerdeck.com/nanachi/rsna2024zhen-rifan-ri)
- [Kaggleコンペ: RSNA2024 上位解法まとめ](https://zenn.dev/mkj/articles/ba630a8837ee72)

</div>

<div class="competition-entry" markdown="1" data-year="2024" data-datatype="tabular" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/child-mind-institute-problematic-internet-use">Child Mind Institute — Problematic Internet Use</a></h3>
<span class="badge badge-year">2024</span> <span class="badge badge-datatype">Tabular</span> <span class="badge badge-platform">Kaggle</span>

- [【参加録】Child Mind Institute — Problematic Internet Use](https://www.nogawanogawa.com/entry/cmi_2)

</div>

<div class="competition-entry" markdown="1" data-year="2024" data-datatype="audio" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/birdclef-2024">BirdCLEF 2024</a></h3>
<span class="badge badge-year">2024</span> <span class="badge badge-datatype">Audio</span> <span class="badge badge-platform">Kaggle</span>

- [BirdCLEF2024：鳥コンペ振り返り](https://qiita.com/butsuyaki-kmn/items/e945691001c962a8726e)
- [BirdCLEF 2024に挑戦 - Kaggleチャレンジ記録](https://tech.aru-zakki.com/kaggle-birdclef-2024-challenge-report/)

</div>

<div class="competition-entry" markdown="1" data-year="2024" data-datatype="text" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/pii-detection-removal-from-educational-data">The Learning Agency Lab - PII Data Detection</a></h3>
<span class="badge badge-year">2024</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">Kaggle</span>

- [Kaggle PII Data Detection 振り返り](https://zenn.dev/sinchir0/articles/396967387196dc)

</div>

<div class="competition-entry" markdown="1" data-year="2024" data-datatype="text" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/learning-agency-lab-automated-essay-scoring-2">Learning Agency Lab - Automated Essay Scoring 2.0</a></h3>
<span class="badge badge-year">2024</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">Kaggle</span>

- [Kaggle Automated Essay Scoring 2.0 コンペ上位解法まとめ](https://zenn.dev/ml_bear/articles/bd8bf184732de6)

</div>

<div class="competition-entry" markdown="1" data-year="2024" data-datatype="text" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/ai-mathematical-olympiad-prize">AI Mathematical Olympiad - Progress Prize 1</a></h3>
<span class="badge badge-year">2024</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">Kaggle</span>

- [AIMOコンペ 上位解法まとめ](https://zenn.dev/morim34/articles/3a23b8c6a7abbb)

</div>

<div class="competition-entry" markdown="1" data-year="2023" data-datatype="timeseries" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/tlvmc-parkinsons-freezing-gait-prediction">Parkinson's Freezing of Gait Prediction</a></h3>
<span class="badge badge-year">2023</span> <span class="badge badge-datatype">Time Series</span> <span class="badge badge-platform">Kaggle</span>

- [「育児中でも、新しい挑戦はできる」データ分析未経験から、Kaggle金メダルをつかんだ女性の物語](https://findy-code.io/engineer-lab/lycorp_kaggle)

</div>

<div class="competition-entry" markdown="1" data-year="2023" data-datatype="text" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/kaggle-llm-science-exam">LLM Science Exam</a></h3>
<span class="badge badge-year">2023</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">Kaggle</span>

- [【DeNATechCon2024】新卒がソロでatmaCup 優勝&Kaggle 金メダル獲得した時の取り組み](https://www.docswell.com/s/DeNA_Tech/538W4D-2024-02-29-092204)

</div>

<div class="competition-entry" markdown="1" data-year="2023" data-datatype="3d" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/rsna-intracranial-aneurysm-detection">RSNA Intracranial Aneurysm Detection</a></h3>
<span class="badge badge-year">2023</span> <span class="badge badge-datatype">3D</span> <span class="badge badge-platform">Kaggle</span>

- [RSNA Intracranial Aneurysm Detection 反省会](https://speakerdeck.com/k951286/kaggle-rsna-intracranial-aneurysm-detectionkonpe-fan-sheng-hui)

</div>

<div class="competition-entry" markdown="1" data-year="2023" data-datatype="image" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/hubmap-hacking-the-human-vasculature">HuBMAP - Hacking the Human Vasculature</a></h3>
<span class="badge badge-year">2023</span> <span class="badge badge-datatype">Image</span> <span class="badge badge-platform">Kaggle</span>

- [20250515_今更ながら2023年に参加したHuBMAP金ソリューションを綺麗にまとめ](https://speakerdeck.com/sugupoko/20250515-jin-geng-nagara2023nian-nican-jia-sitahubmapjin-soriyusiyonmatome)
- [Kaggle HuBMAP2023 上位解法まとめと復習](https://zenn.dev/syu_tan/articles/fbf0b40aa8c686)

</div>

<div class="competition-entry" markdown="1" data-year="2023" data-datatype="text" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/commonlit-evaluate-student-summaries/">CommonLit - Evaluate Student Summaries</a></h3>
<span class="badge badge-year">2023</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">Kaggle</span>

- [CommonLitコンペで学んだこと](https://speakerdeck.com/nogawanogawa/commonlitkonhetexue-ntakoto)

</div>

<div class="competition-entry" markdown="1" data-year="2023" data-datatype="image" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/benetech-making-graphs-accessible">Benetech - Making Graphs Accessible</a></h3>
<span class="badge badge-year">2023</span> <span class="badge badge-datatype">Image</span> <span class="badge badge-platform">Kaggle</span>

- [Kaggle Benetech コンペ振り返り](https://speakerdeck.com/k951286/kaggle-benetechkonpezhen-rifan-ri)

</div>

<div class="competition-entry" markdown="1" data-year="2023" data-datatype="video" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/nfl-player-contact-detection">1st and Future - Player Contact Detection</a></h3>
<span class="badge badge-year">2023</span> <span class="badge badge-datatype">Video</span> <span class="badge badge-platform">Kaggle</span>

- [NFL 1st and Future - Player Contact Detection 振り返り](https://sqrt4kaido.hatenablog.com/entry/2023/03/17/033111)

</div>

<div class="competition-entry" markdown="1" data-year="2022" data-datatype="other" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/kaggle-days-championship">Kaggle Days Championship 2022</a></h3>
<span class="badge badge-year">2022</span> <span class="badge badge-datatype">Other</span> <span class="badge badge-platform">Kaggle</span>

- [KaggleDays Championship 2022, Barcelona](https://ho.lc/blog/barcerona-kaggledays-2022)
- [Kaggle Days World Championshipで優勝した話](https://tech-blog.abeja.asia/entry/kaggledays-champion-202211)
- [Kaggle Days Championship Final 2022 参加報告](https://speakerdeck.com/dena_tech/kaggledays-championship-final-2022)
- [Kaggle Days Championship @ Barcelona に参加しました](https://en-jp.wantedly.com/companies/wantedly/post_articles/448102)
- [Kaggle Days Championship Final 参加記（majimekunチーム）](https://blog.recruit.co.jp/data/articles/kaggle-days-championship-final-majimekun/)

</div>

<div class="competition-entry" markdown="1" data-year="2022" data-datatype="text" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/nbme-score-clinical-patient-notes">NBME - Score Clinical Patient Notes</a></h3>
<span class="badge badge-year">2022</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">Kaggle</span>

- [NBMEコンペ反省会](https://connpass.com/event/246896/)

</div>

<div class="competition-entry" markdown="1" data-year="2022" data-datatype="text" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/jigsaw-toxic-severity-rating">Jigsaw Rate Severity of Toxic Comments</a></h3>
<span class="badge badge-year">2022</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">Kaggle</span>

- [KAGGLEのJigsawで銀メダルを獲得した解法等](https://www.docswell.com/s/2600123617/58M475-2022-03-07-204955)

</div>

<div class="competition-entry" markdown="1" data-year="2022" data-datatype="timeseries" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/g2net-detecting-continuous-gravitational-waves">G2Net Detecting Continuous Gravitational Waves</a></h3>
<span class="badge badge-year">2022</span> <span class="badge badge-datatype">Time Series</span> <span class="badge badge-platform">Kaggle</span>

- [Learning to detect continuous gravitational waves: an open data-analysis competition](https://arxiv.org/abs/2509.06445)

</div>

<div class="competition-entry" markdown="1" data-year="2022" data-datatype="text" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/us-patent-phrase-to-phrase-matching/">U.S. Patent Phrase to Phrase Matching</a></h3>
<span class="badge badge-year">2022</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">Kaggle</span>

- [Kaggleコンペ初参加でチームに恵まれ金メダル(8位)だった](https://secon.dev/entry/2022/06/21/110000-kaggle-uspppm/)

</div>

<div class="competition-entry" markdown="1" data-year="2022" data-datatype="tabular" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/amex-default-prediction">American Express - Default Prediction</a></h3>
<span class="badge badge-year">2022</span> <span class="badge badge-datatype">Tabular</span> <span class="badge badge-platform">Kaggle</span>

- [Meta Feature とは（Kaggle Amex 振り返り）](https://zenn.dev/chimuichimu/articles/42719df8f7e197)
- [Becoming world's 1st - My first gold medal](https://christofhenkel.github.io/dieters-blog/kaggle/2022/09/07/chapter-2.html)

</div>

<div class="competition-entry" markdown="1" data-year="2022" data-datatype="tabular" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/otto-recommender-system">OTTO – Multi-Objective Recommender System</a></h3>
<span class="badge badge-year">2022</span> <span class="badge badge-datatype">Tabular</span> <span class="badge badge-platform">Kaggle</span>

- [【Kaggle】OTTOコンペ参加記(22th/2587th)🥈](https://zenn.dev/zerebom/articles/91910acb0d9b93)
- [6日目: Ottoコンペの振り返り](https://bilzard.hatenablog.com/entry/2023/02/01/092026)

</div>

<div class="competition-entry" markdown="1" data-year="2022" data-datatype="tabular" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations">H&M Personalized Fashion Recommendations</a></h3>
<span class="badge badge-year">2022</span> <span class="badge badge-datatype">Tabular</span> <span class="badge badge-platform">Kaggle</span>

- [AI/機械学習を実務に活かす：レコメンドコンペティション優勝解法徹底解説（1）](https://www.datarobot.com/jp/blog/thorough-explanation-of-the-winning-solution-of-the-recommendation-competition-1/)

</div>

<div class="competition-entry" markdown="1" data-year="2022" data-datatype="tabular" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/jpx-tokyo-stock-exchange-prediction">JPX Tokyo Stock Exchange Prediction</a></h3>
<span class="badge badge-year">2022</span> <span class="badge badge-datatype">Tabular</span> <span class="badge badge-platform">Kaggle</span>

- [【マケデコ】JPX Kaggleコンペ5位解法共有](https://speakerdeck.com/ghtaro/makedeko-jpx-kagglekonpe5wei-jie-fa-gong-you)

</div>

<div class="competition-entry" markdown="1" data-year="2021" data-datatype="video" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/MABe-mouse-behavior-detection">MABe Challenge - Social Action Recognition in Mice</a></h3>
<span class="badge badge-year">2021</span> <span class="badge badge-datatype">Video</span> <span class="badge badge-platform">Kaggle</span>

- [Kaggleコンペティション「MABe Challenge」振り返り](https://speakerdeck.com/yu4u/kagglekonpeteisiyon-mabe-challenge-social-action-recognition-in-mice-zhen-rifan-ri)
- [MABe Challenge振り返りと Cursorを使った実験の回し方](https://www.docswell.com/s/DeNA_Tech/Z8W439-2026-02-25-154748): 2 位解法。Cursor を使った実験の回し方も紹介。
- [Kaggle MABe Challenge 金メダル獲得までの開発スタイル振り返り](https://go-drive-tech.hatenablog.com/entry/2026/01/28/180859)

</div>

<div class="competition-entry" markdown="1" data-year="2020" data-datatype="text" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/c/jigsaw-multilingual-toxic-comment-classification">Jigsaw Multilingual Toxic Comment Classification</a></h3>
<span class="badge badge-year">2020</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">Kaggle</span>

- [Jigsaw Multilingual Competition 1st Place Solution](https://www.kaggle.com/c/jigsaw-multilingual-toxic-comment-classification/discussion/160862)
- [文章有害性評価コンペティションへの挑戦](https://engineering.linecorp.com/ja/blog/challenge-the-jigsaw-rate-severity-of-toxic-comments/)

</div>

<div class="competition-entry" markdown="1" data-year="2020" data-datatype="text" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/c/tweet-sentiment-extraction">Tweet Sentiment Extraction</a></h3>
<span class="badge badge-year">2020</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">Kaggle</span>

- [kaggle tweet コンペの闇と光 (コンペ概要と上位解法)](https://guchio3.hatenablog.com/entry/2020/06/20/115616)
- [Tweet Sentiment Extraction Top Teams YouTube Discussion](https://youtu.be/gdhqdDwLuU0)
- [Tweet Sentiment Extraction 反省記録](http://mathshingo.chillout.jp/blog24.html)

</div>

<div class="competition-entry" markdown="1" data-year="2020" data-datatype="tabular" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/c/lish-moa">Mechanisms of Action (MoA) Prediction</a></h3>
<span class="badge badge-year">2020</span> <span class="badge badge-datatype">Tabular</span> <span class="badge badge-platform">Kaggle</span>

- [Kaggle「MoA」で4位入賞、Masterの称号を獲得しました](https://techblog.recruit.co.jp/article-236/)

</div>

<div class="competition-entry" markdown="1" data-year="2025" data-datatype="tabular" data-platform="atmacup">
<h3><a href="https://www.guruguru.science/competitions/27">atmaCup #20 in collaboration with Udemy</a></h3>
<span class="badge badge-year">2025</span> <span class="badge badge-datatype">Tabular</span> <span class="badge badge-platform">atmaCup</span>

- [atmaCup#20参加レポート](https://takaito0423.hatenablog.com/entry/2025/09/03/222301)

</div>

<div class="competition-entry" markdown="1" data-year="2025" data-datatype="tabular" data-platform="atmacup">
<h3><a href="https://www.guruguru.science/competitions/30/">#22 CA x atmaCup 3rd :||</a></h3>
<span class="badge badge-year">2025</span> <span class="badge badge-datatype">Tabular</span> <span class="badge badge-platform">atmaCup</span>

- [#22 CA x atmaCup 3rd :|| 1st Place Solution](https://speakerdeck.com/yumizu/number-22-ca-x-atmacup-3rd-1st-place-solution)
- [atmaCup#22 振り返り](https://zenn.dev/dalab/articles/85e77d0ea8ed55)
- [atmaCup22で使用された手法まとめ](https://qiita.com/making111/items/cb20ebffe2238c9a2226)

</div>

<div class="competition-entry" markdown="1" data-year="2024" data-datatype="tabular" data-platform="atmacup">
<h3><a href="https://www.guruguru.science/competitions/26/">#19 atmaCup</a></h3>
<span class="badge badge-year">2024</span> <span class="badge badge-datatype">Tabular</span> <span class="badge badge-platform">atmaCup</span>

- [atmaCup#19 2nd Place Solution](https://speakerdeck.com/chimuichimu/atmacup-number-19-2nd-place-solution)

</div>

<div class="competition-entry" markdown="1" data-year="2024" data-datatype="image" data-platform="atmacup">
<h3><a href="https://www.guruguru.science/competitions/25/">#18 Turing × atmaCup</a></h3>
<span class="badge badge-year">2024</span> <span class="badge badge-datatype">Image</span> <span class="badge badge-platform">atmaCup</span>

- [#18 Turing × atmaCup - 1st Place Solution](https://speakerdeck.com/hakubishin3/turing-x-atmacup-number-18-1st-place-solution)
- [atmaCup #18 参戦記（Public7位→Private17位）](https://zenn.dev/dalab/articles/2148b5616a9304)
- [atmaCup#18を復習する](https://zenn.dev/dalab/articles/ba97d8a17c61a8)

</div>

<div class="competition-entry" markdown="1" data-year="2024" data-datatype="tabular" data-platform="atmacup">
<h3><a href="https://atma.connpass.com/event/301535/">atmaCup #16 in collaboration with RECRUIT</a></h3>
<span class="badge badge-year">2024</span> <span class="badge badge-datatype">Tabular</span> <span class="badge badge-platform">atmaCup</span>

- [atmaCup #16 in collaboration with RECRUIT Winning Solution](https://www.guruguru.science/competitions/22/discussions/815241a7-0a00-4700-a456-5eed40a3ff9b/)

</div>

<div class="competition-entry" markdown="1" data-year="2021" data-datatype="tabular" data-platform="atmacup">
<h3>atmaCup</h3>
<span class="badge badge-year">2021</span> <span class="badge badge-datatype">Tabular</span> <span class="badge badge-platform">atmaCup</span>

- [atmaCup#8振り返り〜個人的なテーブルコンペの取組み方と解法〜](https://speakerdeck.com/tomo20180402/atmacup-number-8zhen-rifan-ri-ge-ren-de-nateburukonpefalsequ-zu-mifang-tojie-fa)
- [atmaCup#10参加レポート](https://takaito0423.hatenablog.com/entry/2021/03/17/213956)

</div>

<div class="competition-entry" markdown="1" data-year="2020" data-datatype="tabular" data-platform="signate">
<h3>SIGNATE</h3>
<span class="badge badge-year">2020</span> <span class="badge badge-datatype">Tabular</span> <span class="badge badge-platform">SIGNATE</span>

- [第1回 国土交通省コンペ優勝！賃料予測コンペ1位解法](https://www.estie.jp/blog/entry/2024/12/24/160000)
- [第４回空戦AIチャレンジ最終一位チームの「最終解法」](https://qiita.com/TaroKawa_Spakona/items/0a2f110216f4d00f295c)
- [SIGNATE Student Cup 2020](https://signate.jp/competitions/281/summary)
- [SIGNATE 鰹節コンペ 2nd Place Solution](https://www.slideshare.net/ren4yu/signate-2nd-place-solution)
- [【２位解法】SIGNATE開催CDLEハッカソン2020予測性能部門 「画像データに基づく気象予測」の振り返り。](https://oregin-ai.hatenablog.com/entry/2020/09/06/175415)

</div>

<div class="competition-entry" markdown="1" data-year="2023" data-datatype="tabular" data-platform="nishika">
<h3>Nishika</h3>
<span class="badge badge-year">2023</span> <span class="badge badge-datatype">Tabular</span> <span class="badge badge-platform">Nishika</span>

- [Nishika音声認識コンペに参加して2位になりました！🎉](https://www.ai-shift.co.jp/techblog/4813)
- [Nishika 財務・非財務情報を活用した株式の価値予測コンペ振り返り](https://note.com/nishika_inc/n/n8678212cb614)
- [AI×商標：イメージサーチコンペティション 2nd place solution](https://speakerdeck.com/anyai/nishika-aixshang-biao-imezisatikonpeteisiyon-2nd-place-solution)
- [Nishika 日本酒銘柄画像検索コンペ 7位解法（備忘録）](https://zenn.dev/ubex/articles/0a49c6e912220f)

</div>

<div class="competition-entry" markdown="1" data-year="2024" data-datatype="other" data-platform="other">
<h3>国際・日本人工知能オリンピック</h3>
<span class="badge badge-year">2024</span> <span class="badge badge-datatype">Other</span> <span class="badge badge-platform">その他</span>

- [IOAI2024 参加記 (onnoboru 視点)](https://onnoboru.hatenablog.com/entry/2024/12/23/000344)
- [IOAI2024 (At-Home Task) 日本代表ソリューション](https://zenn.dev/chizuchizu/articles/b556a5b6ad6019)
- [[JOAI] 第一回日本人工知能オリンピックで金賞を受賞しました！！](https://zenn.dev/kanda9685/articles/a6e9dc0cc89493)
- [【解法解説】日本人工知能オリンピックで金賞（5位）受賞したよ！JOAI2025参加体験記！](https://ray-globallife.com/joai-2025/)

</div>

<div class="competition-entry" markdown="1" data-year="2024" data-datatype="tabular" data-platform="other">
<h3><a href="https://www.recsyschallenge.com/">RecSys Challenge</a></h3>
<span class="badge badge-year">2024</span> <span class="badge badge-datatype">Tabular</span> <span class="badge badge-platform">その他</span>

- [RecSys Challenge 2025 Solution Article](https://blog.recruit.co.jp/data/articles/recsys-challenge-2025/)
- [RecSys Challenge 2025 で優勝しました](https://blog.recruit.co.jp/data/articles/recsys-challenge-2025-appeal/): ユーザの行動履歴から埋め込み表現を獲得するコンペの優勝報告。
- [RecSys Challenge 2024 優勝報告](https://speakerdeck.com/unonao/jsai2025-recsyschallenge2024-you-sheng-bao-gao)
- [「Team Wantedly」 が RecSys Challenge 2020 で３位に入賞しました](https://www.wantedly.com/companies/wantedly/post_articles/249713)
- [RecSys Challenge 2020 備忘録](https://note.com/myaun/n/ndcbd9a4e7150)

</div>

<div class="competition-entry" markdown="1" data-year="2024" data-datatype="text" data-platform="other">
<h3>RAG-1グランプリ</h3>
<span class="badge badge-year">2024</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">その他</span>

- [Raggle第2回コンペ 1位解法 – 製薬企業向けRAGの精度改善](https://qiita.com/keiYM/items/99b5298e9e82d61330cd)
- [RAG-1グランプリ 10位解法と振り返り - 質問と関連文書から Q&A システムを設計する](https://note.com/catshun_/n/n61347ef06b2c)

</div>

<div class="competition-entry" markdown="1" data-year="2024" data-datatype="other" data-platform="other">
<h3><a href="https://solafune.com/">Solafune</a></h3>
<span class="badge badge-year">2024</span> <span class="badge badge-datatype">Other</span> <span class="badge badge-platform">その他</span>

- [シミュレーションコンペで銅メダル2つを獲得してkaggle Expertになった方法](https://zenn.dev/epicai_techblog/articles/a80959e01d62fd)

</div>

<div class="competition-entry" markdown="1" data-year="2024" data-datatype="image" data-platform="other">
<h3>眼科AI学会</h3>
<span class="badge badge-year">2024</span> <span class="badge badge-datatype">Image</span> <span class="badge badge-platform">その他</span>

- [第5回日本眼科AI学会総会_AIコンテスト_３位解法](https://speakerdeck.com/neilsaw/di-5hui-ri-ben-yan-ke-aixue-hui-zong-hui-aikontesuto-3wei-jie-fa)
- [眼科AIコンテスト2024_特別賞_Solution](https://speakerdeck.com/pon0matsu/yan-ke-aikontesuto2024-te-bie-shang-6wei-solution)

</div>

<div class="competition-entry" markdown="1" data-year="2024" data-datatype="image" data-platform="other">
<h3>その他</h3>
<span class="badge badge-year">2024</span> <span class="badge badge-datatype">Image</span> <span class="badge badge-platform">その他</span>

- [SpaceNet 9 Challenge 2nd place solution](https://www.docswell.com/s/motokimura/KN968L-spacenet9-2nd-place-solution)
- [国際学会SIGSPATIALワークショップの位置情報予測コンペHumob2024 ドコモ3位入賞解法＆アメリカ現地参加レポート](https://nttdocomo-developers.jp/entry/2024/12/01/090000_2)
- [「Ego4D Challenge 2023」 の長期動作予測部門で、準優勝](https://connect.panasonic.com/jp-ja/about/who-we-are/research/cvpr2023)
- [KDDCup2025 マルチモーダルRAGコンペにおける入賞チーム解法の紹介](https://nttdocomo-developers.jp/entry/2025/12/17/090000_4)
- [RAG精度向上を目指したCRAGコンペ上位解法の紹介](https://nttdocomo-developers.jp/entry/2025/04/21/090000)
- [Kaggleでソロ金メダル獲得！primeNumber若松さんがデータの力で世界に挑む](https://lounge.primenumber.com/entry/n/n8425a299b9ed)
- [Comp with Agent - AI agent for autonomous competition](https://github.com/jintonic3561/comp_with_agent)

</div>

<div class="competition-entry" markdown="1" data-year="2022" data-datatype="image" data-platform="other">
<h3>全国医療AIコンテスト</h3>
<span class="badge badge-year">2022</span> <span class="badge badge-datatype">Image</span> <span class="badge badge-platform">その他</span>

- [全国医療AIコンテスト 1位解法](https://drive.google.com/file/d/1CLd5R3JOHUPbr50YQCRtTXp4TtRiYSsu/view)
- [全国医療AIコンテスト 2位解法](https://docs.google.com/presentation/d/1XfWN1gZYxe6yBI63X0ZXVWBxTJJYpkf89WKabubwea0/edit)
- [Kaggleから学んだ医療画像データ解析の取り組み方](https://speakerdeck.com/inoichan/di-4hui-quan-guo-yi-liao-aikontesuto-kagglekaraxue-ndayi-liao-hua-xiang-detajie-xi-falsequ-rizu-mifang)

</div>

<div class="competition-entry" markdown="1" data-year="2021" data-datatype="text" data-platform="other">
<h3>AI王 〜クイズAI日本一決定戦〜</h3>
<span class="badge badge-year">2021</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">その他</span>

- [AutoGluon-Tabular を用いたアンサンブルによる日本語質問応答システムの構築](https://speakerdeck.com/upura/aio-solution-by-autogluon-tabular)
- [【AI王 〜クイズAI日本一決定戦〜】ふりかえり](https://www.ai-shift.co.jp/techblog/1781)

</div>

<div class="competition-entry" markdown="1" data-year="2020" data-datatype="other" data-platform="other">
<h3>学会コンペ</h3>
<span class="badge badge-year">2020</span> <span class="badge badge-datatype">Other</span> <span class="badge badge-platform">その他</span>

- [2020年に学会コンペに3つ参加したので感想など](https://myaun.hatenablog.com/entry/2020/12/22/000326)
- [学会コンペで論文執筆の流れを学んだ話](https://upura.hatenablog.com/entry/kaggle-advent-20241217)
- [学会コンペ参加してみた](https://qiita.com/ShunsukeKikuchi/items/8f4a431e0a804b3871fe)
- [眼科AI学会 AIコンペティション 8th solutionと上位解法](https://www.docswell.com/s/yuki-tashiro/K3G7NE-ophthalmology-AI-competition-8th-solution)

</div>

<div class="competition-entry" markdown="1" data-year="2020" data-datatype="tabular" data-platform="other">
<h3>ProbSpace</h3>
<span class="badge badge-year">2020</span> <span class="badge badge-datatype">Tabular</span> <span class="badge badge-platform">その他</span>

- [jupyterノートブックを公開いたします（ Public２位、Private１位）](https://comp.probspace.com/topics/datascience-Post2959de7ddfcc4ee201b7)

</div>

</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const datatypeFilter = document.getElementById('filter-datatype');
  const yearFilter = document.getElementById('filter-year');
  const platformFilter = document.getElementById('filter-platform');
  const visibleCount = document.getElementById('visible-count');
  const entries = document.querySelectorAll('.competition-entry');

  function applyFilters() {
    const datatype = datatypeFilter.value;
    const year = yearFilter.value;
    const platform = platformFilter.value;
    let count = 0;

    entries.forEach(entry => {
      const entryDatatype = entry.dataset.datatype;
      const entryYear = entry.dataset.year;
      const entryPlatform = entry.dataset.platform;

      let show = true;

      if (datatype && entryDatatype !== datatype) {
        show = false;
      }

      if (year) {
        if (year === '2019') {
          if (parseInt(entryYear) > 2019) {
            show = false;
          }
        } else if (entryYear !== year) {
          show = false;
        }
      }

      if (platform && entryPlatform !== platform) {
        show = false;
      }

      if (show) {
        entry.classList.remove('hidden');
        count++;
      } else {
        entry.classList.add('hidden');
      }
    });

    visibleCount.textContent = count;
  }

  window.resetFilters = function() {
    datatypeFilter.value = '';
    yearFilter.value = '';
    platformFilter.value = '';
    applyFilters();
  };

  datatypeFilter.addEventListener('change', applyFilters);
  yearFilter.addEventListener('change', applyFilters);
  platformFilter.addEventListener('change', applyFilters);

  applyFilters();
});
</script>
