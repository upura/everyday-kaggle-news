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

<div class="competition-entry" markdown="1" data-year="2022" data-datatype="image" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/mayo-clinic-strip-ai">Mayo Clinic - STRIP AI</a></h3>
<span class="badge badge-year">2022</span> <span class="badge badge-datatype">Image</span> <span class="badge badge-platform">Kaggle</span>

- [MATLABとPythonの違いとは: PythonでKaggleに参加し、3位に入賞したMathWorks社員が感じたこと](https://blogs.mathworks.com/japan-community/2022/12/08/mayo-clinic-3rd-kaggle/): 脳卒中の血栓画像分類コンペの 3 位解法。

</div>

<div class="competition-entry" markdown="1" data-year="2022" data-datatype="text" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/feedback-prize-effectiveness">Feedback Prize - Predicting Effective Arguments</a></h3>
<span class="badge badge-year">2022</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">Kaggle</span>

- [Kaggle「Feedback Prize - Predicting Effective Arguments」上位解法まとめ](https://zenn.dev/yume_neko/articles/6e8f78a12a1d2a): 生徒の論証を分類するコンペの上位解法まとめ。

</div>

<div class="competition-entry" markdown="1" data-year="2022" data-datatype="text" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/feedback-prize-2021">Feedback Prize - Evaluating Student Writing</a></h3>
<span class="badge badge-year">2022</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">Kaggle</span>

- [Kaggle「Feedback Prize - Evaluating Student Writing」振り返り資料](https://speakerdeck.com/shimacos/kaggle-feedback-prizekonpe-fan-sheng-hui): 学生が書いた議論用文章を解析するコンペの概要と上位解法のまとめ。

</div>

<div class="competition-entry" markdown="1" data-year="2021" data-datatype="image" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/c/tensorflow-great-barrier-reef">Tensorflow - Help Protect the Great Barrier Reef</a></h3>
<span class="badge badge-year">2021</span> <span class="badge badge-datatype">Image</span> <span class="badge badge-platform">Kaggle</span>

- [Great Barrier Reef 参加録](https://kdl-di.hatenablog.com/entry/2022/09/30/090000): オニヒトデ検出コンペの進め方と参加意義を綴る参加録。

</div>

<div class="competition-entry" markdown="1" data-year="2022" data-datatype="tabular" data-platform="nishika">
<h3><a href="https://competition.nishika.com/">Nishika 生鮮野菜の価格予測</a></h3>
<span class="badge badge-year">2022</span> <span class="badge badge-datatype">Tabular</span> <span class="badge badge-platform">Nishika</span>

- [生鮮野菜の価格予測 優勝解法](https://qiita.com/aji-pandas/items/4cb941a7ea9020a501de)

</div>

<div class="competition-entry" markdown="1" data-year="2022" data-datatype="tabular" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/tabular-playground-series-may-2022">Tabular Playground Series - May 2022</a></h3>
<span class="badge badge-year">2022</span> <span class="badge badge-datatype">Tabular</span> <span class="badge badge-platform">Kaggle</span>

- [【Kaggle】 Tabular Playground Series - May 2022コンペ参加記(9th/1151)](https://zenn.dev/bizyu/articles/5e7dae75dcbc06)

</div>

<div class="competition-entry" markdown="1" data-year="2022" data-datatype="text" data-platform="nishika">
<h3><a href="https://competition.nishika.com/">Nishika ボケ判定AIを作ろう！</a></h3>
<span class="badge badge-year">2022</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">Nishika</span>

- [「笑い」を理解するAIを作ってみました　～ボケ判定AIを作ろう！ (ボケてコンペ ＃1) 1st place solution ～](https://qiita.com/z-lai/items/2d51ce123d77ad7100e8)

</div>

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
- [Geminiを使ったらKaggle初挑戦、参加期間10日間でも5位入賞できたので手法をすべて書く](https://qiita.com/yukky_memo/items/6e1c7fa08b9b91278886): 生成 AI を活用して初参加 10 日間で 5 位入賞した振り返り。
- [KaggleのLLM 20 Questionsで金メダルを獲得しました](https://blog.recruit.co.jp/data/articles/kaggle-llm-20-questions-majimekun/): 対戦形式コンペの金メダル解法。

</div>

<div class="competition-entry" markdown="1" data-year="2024" data-datatype="tabular" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/leap-atmospheric-physics-ai-climsim">LEAP - Atmospheric Physics using AI (ClimSim)</a></h3>
<span class="badge badge-year">2024</span> <span class="badge badge-datatype">Tabular</span> <span class="badge badge-platform">Kaggle</span>

- [Kaggle LEAP Competition Solution解説&振り返り](https://speakerdeck.com/abeja/kaggle-leap-competition-solutionjie-shuo-and-zhen-rifan-ri)
- [Kaggle LEAP コンペ 上位解法まとめ](https://zenn.dev/dena/articles/b4c3a5a04b7644): 4 位チーム参加者による上位解法のまとめ記事。

</div>

<div class="competition-entry" markdown="1" data-year="2024" data-datatype="text" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/eedi-mining-misconceptions-in-mathematics">Eedi - Mining Misconceptions in Mathematics</a></h3>
<span class="badge badge-year">2024</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">Kaggle</span>

- [Kaggle Eedi - Mining Misconceptions in Mathematics 振り返り](https://zenn.dev/mkj/articles/a6e26546e31439)
- [Kaggle Eediコンペ振り返り](https://speakerdeck.com/kuto5046/kaggle-eedikonpezhen-rifan-ri): 上位解法をまとめた発表資料。
- [Eediコンペ上位解法まとめ](https://zenn.dev/kuto5046/articles/8e612b473c4d75)
- [RTX3090x1でKaggle LLMコンペは戦えるのか？](https://zenn.dev/yume_neko/articles/5cd27dac3d8311): 計算資源の制限下で金メダル圏スコアの再現を目指す検証記事。
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
- [Kaggle NeurIPS - Ariel Data Challenge 2024の2位ベイズ解法の解説](https://qiita.com/m5t0/items/21fa66c5ffb473e23b29): 系外惑星の信号抽出コンペの 2 位ベイズ解法の解説。
- [Arielコンペ負け犬の遠吠え](https://medium.com/@junkoda/ariel%E3%82%B3%E3%83%B3%E3%83%9A%E8%B2%A0%E3%81%91%E7%8A%AC%E3%81%AE%E9%81%A0%E5%90%A0%E3%81%88-c60b6bf512bd): コンペの要点と難しさを解説する参加録。

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
- [kaggle RSNA2024コンペ　上位解法まとめ](https://zenn.dev/yume_neko/articles/7c3f2744f07b9f)

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
- [kaggle LLM コンペ 上位解法を自分なりにまとめてみた話](https://note.com/japan_d2/n/na873dd82de6a)
- [Kaggleコンペ（LLM Science Exam）の振り返りと上位解法まとめ](https://zenn.dev/nishimoto/articles/aff1fba9c75c34)

</div>

<div class="competition-entry" markdown="1" data-year="2023" data-datatype="3d" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/rsna-intracranial-aneurysm-detection">RSNA Intracranial Aneurysm Detection</a></h3>
<span class="badge badge-year">2023</span> <span class="badge badge-datatype">3D</span> <span class="badge badge-platform">Kaggle</span>

- [RSNA Intracranial Aneurysm Detection 反省会](https://speakerdeck.com/k951286/kaggle-rsna-intracranial-aneurysm-detectionkonpe-fan-sheng-hui)

</div>

<div class="competition-entry" markdown="1" data-year="2023" data-datatype="video" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/asl-signs">Google - Isolated Sign Language Recognition</a></h3>
<span class="badge badge-year">2023</span> <span class="badge badge-datatype">Video</span> <span class="badge badge-platform">Kaggle</span>

- [1st place code with reproducibility](https://www.kaggle.com/competitions/asl-signs/discussion/406978): 手話認識コンペの再現実装つき優勝解法。

</div>

<div class="competition-entry" markdown="1" data-year="2023" data-datatype="text" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/learning-equality-curriculum-recommendations">Learning Equality - Curriculum Recommendations</a></h3>
<span class="badge badge-year">2023</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">Kaggle</span>

- [Kaggleの『Learning Equality - Curriculum Recommendations』コンペティションで金メダル(6位/1057チーム)を獲得しました！](https://www.mcdigital.jp/blog/kaggle-lecr-2023/): GM 昇格を決めた 6 位金メダル解法。

</div>

<div class="competition-entry" markdown="1" data-year="2023" data-datatype="image" data-platform="solafune">
<h3><a href="https://solafune.com/ja/competitions/7a1fc5e3-49bd-4ec1-8378-974951398c98">衛星画像の5倍超解像度化 (for OSS)</a></h3>
<span class="badge badge-year">2023</span> <span class="badge badge-datatype">Image</span> <span class="badge badge-platform">Solafune</span>

- [Solafune の衛星画像の超解像コンペで 1 位を獲得しました](https://hack.nikkei.com/blog/solafune202304/): 衛星画像超解像コンペの 1 位解法。
- [【solafune:5x Super-resolution of Satellite Images】private 2nd](https://qiita.com/roadto93ds/items/6b4c97bd082bf3fe8bbe)

</div>

<div class="competition-entry" markdown="1" data-year="2023" data-datatype="multimodal" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/stable-diffusion-image-to-prompts">Stable Diffusion - Image to Prompts</a></h3>
<span class="badge badge-year">2023</span> <span class="badge badge-datatype">Multimodal</span> <span class="badge badge-platform">Kaggle</span>

- [Stable Diffusion - Image to Prompts](https://speakerdeck.com/kfujikawa/stable-diffusion-image-to-prompts): 生成プロンプトを推定するコンペの概要と上位解法の解説資料。
- [1st Place Solution | Stable Diffusion - Image to Prompts](https://www.kaggle.com/competitions/stable-diffusion-image-to-prompts/discussion/411237): 当時ランキング 1 位 bestfitting さんの優勝解法。

</div>

<div class="competition-entry" markdown="1" data-year="2023" data-datatype="image" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/vesuvius-challenge-ink-detection/">Vesuvius Challenge - Ink Detection</a></h3>
<span class="badge badge-year">2023</span> <span class="badge badge-datatype">Image</span> <span class="badge badge-platform">Kaggle</span>

- [$12,000 Ink Detection Followup (August 28th)](https://scrollprize.org/ink_detection_followup): 主催者による上位解法の紹介ページ。解説動画とコードへのリンクつき。

</div>

<div class="competition-entry" markdown="1" data-year="2023" data-datatype="image" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/hubmap-hacking-the-human-vasculature">HuBMAP - Hacking the Human Vasculature</a></h3>
<span class="badge badge-year">2023</span> <span class="badge badge-datatype">Image</span> <span class="badge badge-platform">Kaggle</span>

- [20250515_今更ながら2023年に参加したHuBMAP金ソリューションを綺麗にまとめ](https://speakerdeck.com/sugupoko/20250515-jin-geng-nagara2023nian-nican-jia-sitahubmapjin-soriyusiyonmatome)
- [Kaggle HuBMAP2023 上位解法まとめと復習](https://zenn.dev/syu_tan/articles/fbf0b40aa8c686)
- [Kaggle振り返り🥈：HuBMAP - Hacking the Human Vasculature](https://moritake04.hatenablog.com/entry/2023/08/06/202956)

</div>

<div class="competition-entry" markdown="1" data-year="2023" data-datatype="text" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/commonlit-evaluate-student-summaries/">CommonLit - Evaluate Student Summaries</a></h3>
<span class="badge badge-year">2023</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">Kaggle</span>

- [CommonLitコンペで学んだこと](https://speakerdeck.com/nogawanogawa/commonlitkonhetexue-ntakoto)
- [ARISE Kaggle部活動記 #5](https://www.ariseanalytics.com/activities/report/20231117/): 個人参加 12 位の金メダル解法の紹介。
- [【参加録】CommonLit - Evaluate Student Summaries](https://www.nogawanogawa.com/entry/commonlit_evaluate_student_summaries)
- [kaggle Commonlit2　上位解法まとめ](https://zenn.dev/chiman/articles/246b309925e65d)

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
- [NFLのPlayer Contact Detectionで金メダル獲得＆コンペ振り返り](https://acro-engineer.hatenablog.com/entry/2023/03/29/100000)

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
- [Kaggle「NBME - Score Clinical Patient Notes」の4位解法](https://blog.recruit.co.jp/data/articles/kaggle-nbme-score-clinical-patient-notes/): 取り組みの概要や上位解法の考察をまとめた記事。
- [NBME - Score Clinical Patient Notes 1位解法](https://www.docswell.com/s/currypurin/Z8L7L5-2022-05-23-081854): 有志による「NBMEコンペ反省会」での発表資料。
- [NBME - Score Clinical Patient Notes 参加録](https://www.ai-shift.co.jp/techblog/2583): コンペ概要や解法をまとめた参加記録。

</div>

<div class="competition-entry" markdown="1" data-year="2022" data-datatype="text" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/jigsaw-toxic-severity-rating">Jigsaw Rate Severity of Toxic Comments</a></h3>
<span class="badge badge-year">2022</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">Kaggle</span>

- [KAGGLEのJigsawで銀メダルを獲得した解法等](https://www.docswell.com/s/2600123617/58M475-2022-03-07-204955)
- [Jigsaw Rate Severity of Toxic Comments 銀メダル解法](https://qiita.com/Toshihikoko/items/cde3480eab7e02a9d7f2): 取り組んだ内容やコード・発表資料をまとめた記事。

</div>

<div class="competition-entry" markdown="1" data-year="2022" data-datatype="timeseries" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/g2net-detecting-continuous-gravitational-waves">G2Net Detecting Continuous Gravitational Waves</a></h3>
<span class="badge badge-year">2022</span> <span class="badge badge-datatype">Time Series</span> <span class="badge badge-platform">Kaggle</span>

- [Learning to detect continuous gravitational waves: an open data-analysis competition](https://arxiv.org/abs/2509.06445)
- [G2Netコンペ2023 振り返り](https://sqrt4kaido.hatenablog.com/entry/2023/01/07/020404): CNN を用いた 17 位解法の振り返り記事。

</div>

<div class="competition-entry" markdown="1" data-year="2022" data-datatype="text" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/us-patent-phrase-to-phrase-matching/">U.S. Patent Phrase to Phrase Matching</a></h3>
<span class="badge badge-year">2022</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">Kaggle</span>

- [Kaggleコンペ初参加でチームに恵まれ金メダル(8位)だった](https://secon.dev/entry/2022/06/21/110000-kaggle-uspppm/)
- [Kaggle PPPMコンペ反省会](https://speakerdeck.com/k951286/kaggle-pppmkonpefan-sheng-hui): 銀メダル解法。上位への鍵となった手法を紹介。
- [Kaggle「U.S. Patent Phrase to Phrase Matching」8位解法](https://hack.nikkei.com/blog/kaggle202207/): 複数の対象を同時に扱う方法や敵対的学習手法を紹介。

</div>

<div class="competition-entry" markdown="1" data-year="2022" data-datatype="image" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/rsna-2022-cervical-spine-fracture-detection">RSNA 2022 Cervical Spine Fracture Detection</a></h3>
<span class="badge badge-year">2022</span> <span class="badge badge-datatype">Image</span> <span class="badge badge-platform">Kaggle</span>

- [Kaggle RSNA 2022 10位 解法の紹介　～頸椎のCT画像から骨折の有無を予測する～](https://datascience.nri.com/entry/2022/12/09/163110): CT 画像から頸椎骨折を予測するコンペの金メダル解法。

</div>

<div class="competition-entry" markdown="1" data-year="2022" data-datatype="text" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/AI4Code">Google AI4Code – Understand Code in Python Notebooks</a></h3>
<span class="badge badge-year">2022</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">Kaggle</span>

- [Kaggleコンペ「AI4Code」振り返り](https://qiita.com/yufuin/items/1bc0bb391ad65d8595d7): 公開 Notebook のコードとコメントの関係性を分析するコンペの 3 位解法。

</div>

<div class="competition-entry" markdown="1" data-year="2022" data-datatype="tabular" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/amex-default-prediction">American Express - Default Prediction</a></h3>
<span class="badge badge-year">2022</span> <span class="badge badge-datatype">Tabular</span> <span class="badge badge-platform">Kaggle</span>

- [Meta Feature とは（Kaggle Amex 振り返り）](https://zenn.dev/chimuichimu/articles/42719df8f7e197)
- [Becoming world's 1st - My first gold medal](https://christofhenkel.github.io/dieters-blog/kaggle/2022/09/07/chapter-2.html)
- [【Kaggle】American Express - Default Predictionコンペで金メダルを獲得しました](https://blog.brainpad.co.jp/entry/2022/12/22/154432)

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
- [DeNA共同執筆発表資料「H&Mコンペの振り返り」](https://speakerdeck.com/kuto5046/denamot-aiji-shu-gong-you-hui-fa-biao-zi-liao-h-and-mkonpefalsezhen-rifan-ri): 46 位の参加者を含む振り返り資料。
- [Kaggle「H&M Personalized Fashion Recommendations」の金メダル解法](https://blog.recruit.co.jp/data/articles/kaggle-h-and-m/): コンペから得た着想で CVR を 20〜30% 向上させた業務活用も報告。
- [Kaggle「H&M Personalized Fashion Recommendations」個人参加25位の参加録](https://yng87.github.io/blog/2022/05/kaggle_hm/): 81 位・133 位のチームの取り組みも合わせて紹介。

</div>

<div class="competition-entry" markdown="1" data-year="2022" data-datatype="tabular" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/jpx-tokyo-stock-exchange-prediction">JPX Tokyo Stock Exchange Prediction</a></h3>
<span class="badge badge-year">2022</span> <span class="badge badge-datatype">Tabular</span> <span class="badge badge-platform">Kaggle</span>

- [【マケデコ】JPX Kaggleコンペ5位解法共有](https://speakerdeck.com/ghtaro/makedeko-jpx-kagglekonpe5wei-jie-fa-gong-you)
- [JPX Tokyo Stock Exchange Prediction Award Ceremony 解法総評](https://speakerdeck.com/gamella/jpx-tokyo-stock-exchange-prediction-award-ceremony-jie-fa-zong-ping): 主催者による表彰式での上位解法総評。
- [システムトレーダー視点での「JPX Tokyo Stock Exchange Prediction」参加感想](https://qiita.com/blog_UKI/items/efba4ac7b1543a9bef85): 記事を受けて主催者が問題設計の流れを解説する記事も公開された。
- [システムトレーダーによる「JPX: Tokyo Stock Exchange Prediction」考察記事](https://note.com/uki_profit/n/nd32b67489e23): 同コンペが個人投資家に与える影響について説明する記事。

</div>

<div class="competition-entry" markdown="1" data-year="2022" data-datatype="tabular" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/foursquare-location-matching">Foursquare - Location Matching</a></h3>
<span class="badge badge-year">2022</span> <span class="badge badge-datatype">Tabular</span> <span class="badge badge-platform">Kaggle</span>

- [Foursquare - Location Matching の7位解法](https://future-architect.github.io/articles/20220720a/): コンペ概要や具体的な取り組みを詳細に解説。
- [Kaggle「Foursquare - Location Matching」の銀メダル解法](https://www.t88.work/entry/2022/07/10/210909): コンペ概要や解法、Kaggle 環境での推論時の工夫を紹介。

</div>

<div class="competition-entry" markdown="1" data-year="2022" data-datatype="image" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/image-matching-challenge-2022">Image Matching Challenge 2022</a></h3>
<span class="badge badge-year">2022</span> <span class="badge badge-datatype">Image</span> <span class="badge badge-platform">Kaggle</span>

- [Kaggle「Image Matching Challenge 2022」の優勝解法](https://zenn.dev/yume_neko/articles/1912be56cd77d9): 参加から優勝に至るまでの取り組みを時系列で紹介。
- [Kaggle「Image Matching Challenge 2022」の10位解法](https://forxai.konicaminolta.com/blog/017): コンペ概要や特徴、チームとしての取り組みをまとめた記事。

</div>

<div class="competition-entry" markdown="1" data-year="2022" data-datatype="audio" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/birdclef-2022">BirdCLEF 2022</a></h3>
<span class="badge badge-year">2022</span> <span class="badge badge-datatype">Audio</span> <span class="badge badge-platform">Kaggle</span>

- [BirdCLEF 2022 6位解法](https://docs.google.com/presentation/d/1K-uFxM7edPpWamEQCF5qzyYylGj0JcRvZQScDHwesi8/edit): 肝となった「ハンドラベリング」を中心に解説。

</div>

<div class="competition-entry" markdown="1" data-year="2022" data-datatype="image" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/happy-whale-and-dolphin">Happywhale - Whale and Dolphin Identification</a></h3>
<span class="badge badge-year">2022</span> <span class="badge badge-datatype">Image</span> <span class="badge badge-platform">Kaggle</span>

- [Happywhale - Whale and Dolphin Identification 上位解法まとめ](https://zenn.dev/yume_neko/articles/f0177aadbb4eb5): クジラとイルカの個体識別コンペの上位解法まとめ。
- [Happywhale 優勝・10位解法解説](https://tech.preferred.jp/ja/blog/kaggle-happywhale-1st-10th-solution/): Preferred Networks 社員による優勝・10 位解法の解説。2 位の Rist、6 位のアイリスからもそれぞれプレスリリースが公開された。

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
- [atmaCup #16: 1st place solution + 取り組み方振り返り](https://speakerdeck.com/unonao/atmacup-number-16-1st-place-solution-plus-qu-rizu-mifang-zhen-rifan-ri)
- [atmaCup #16 2nd Place Solution](https://speakerdeck.com/senkin13/atmacup-number-16-in-collaboration-with-recruit-2nd-place-solution)
- [atmaCup #16 3rd Place Solution](https://speakerdeck.com/chimuichimu/atmacup-number-16-3rd-place-solution)
- [推薦データ分析コンペに参加して得た知見](https://speakerdeck.com/yudai00/tui-jian-detafen-xi-konpenican-jia-sitede-tazhi-jian)

</div>

<div class="competition-entry" markdown="1" data-year="2021" data-datatype="tabular" data-platform="atmacup">
<h3>atmaCup</h3>
<span class="badge badge-year">2021</span> <span class="badge badge-datatype">Tabular</span> <span class="badge badge-platform">atmaCup</span>

- [atmaCup#8振り返り〜個人的なテーブルコンペの取組み方と解法〜](https://speakerdeck.com/tomo20180402/atmacup-number-8zhen-rifan-ri-ge-ren-de-nateburukonpefalsequ-zu-mifang-tojie-fa)
- [atmaCup#10参加レポート](https://takaito0423.hatenablog.com/entry/2021/03/17/213956)
- [「Sansan × atmaCup #12」開催報告](https://buildersbox.corp-sansan.com/entry/2021/12/18/110000): コンペの概要や上位解法を紹介する主催者記事。
- [「#12 Sansan × atmaCup」9位参加録](https://caddi.tech/archives/2866): 特徴量生成や後処理に利用したライブラリを紹介。

</div>

<div class="competition-entry" markdown="1" data-year="2022" data-datatype="tabular" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/g-research-crypto-forecasting">G-Research Crypto Forecasting</a></h3>
<span class="badge badge-year">2022</span> <span class="badge badge-datatype">Tabular</span> <span class="badge badge-platform">Kaggle</span>

- [システムトレーダー視点での「G-Research Crypto Forecasting」参加感想](https://qiita.com/blog_UKI/private/fbad4b19e734084e73bf): コンペの仕様に関する考察などを紹介する記事。

</div>

<div class="competition-entry" markdown="1" data-year="2022" data-datatype="image" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/sartorius-cell-instance-segmentation">Sartorius - Cell Instance Segmentation</a></h3>
<span class="badge badge-year">2022</span> <span class="badge badge-datatype">Image</span> <span class="badge badge-platform">Kaggle</span>

- [Sartorius - Cell Instance Segmentation の4位解法](https://acro-engineer.hatenablog.com/entry/2022/02/02/120000): 顕微鏡画像からニューロン細胞を検出するコンペの概要や取り組みを紹介。

</div>

<div class="competition-entry" markdown="1" data-year="2022" data-datatype="image" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/petfinder-pawpularity-score">PetFinder.my - Pawpularity Contest</a></h3>
<span class="badge badge-year">2022</span> <span class="badge badge-datatype">Image</span> <span class="badge badge-platform">Kaggle</span>

- [PetFinder.my - Pawpularity Contest の銀メダル解法](https://qiita.com/tt20210824/items/6cef4a715cfefa50e8a7): 解法の詳細や得られた知見をまとめた記事。
- [PetFinder.my - Pawpularity Contest 2位入賞者の振り返り](https://teyoblog.hatenablog.com/entry/2022/01/23/211430): 取組内容や考察を綴った振り返り記事。

</div>

<div class="competition-entry" markdown="1" data-year="2022" data-datatype="tabular" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/nfl-health-and-safety-helmet-assignment">NFL Health &amp; Safety - Helmet Assignment</a></h3>
<span class="badge badge-year">2022</span> <span class="badge badge-datatype">Tabular</span> <span class="badge badge-platform">Kaggle</span>

- [NFL Health &amp; Safety - Helmet Assignment 優勝者によるコンペ紹介](https://qiita.com/Kmat67916008/items/8ccf0171219036621540): コンペ特有の難しさや取り組み方を綴った記事。
- [NFL Health &amp; Safety - Helmet Assignment 概要資料（16位解法・上位3チーム解法紹介）](https://speakerdeck.com/takarasawa_/kaggle-nfl2): 資料作成者による 16 位解法と上位 3 チームの解法を紹介。
- [NFL Health &amp; Safety - Helmet Assignment 振り返り会の回顧録](https://fam-taro.hatenablog.com/entry/2021/11/08/230247): コンペ上位 3 人や運営に携わった Kaggle Grandmaster も参加した振り返り会の回顧録。

</div>

<div class="competition-entry" markdown="1" data-year="2022" data-datatype="tabular" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/ventilator-pressure-prediction">Google Brain - Ventilator Pressure Prediction</a></h3>
<span class="badge badge-year">2022</span> <span class="badge badge-datatype">Tabular</span> <span class="badge badge-platform">Kaggle</span>

- [Google Brain - Ventilator Pressure Prediction 上位解法まとめ](https://teyoblog.hatenablog.com/entry/2021/12/05/000000): 公開情報を参考に金メダル相当のスコアを再現した記事。
- [Google Brain - Ventilator Pressure Prediction 17位解法](https://sqrt4kaido.hatenablog.com/entry/2021/11/07/152227): コンペ概要や具体的な取り組みをまとめた記事。

</div>

<div class="competition-entry" markdown="1" data-year="2022" data-datatype="text" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/chaii-hindi-and-tamil-question-answering">chaii - Hindi and Tamil Question Answering</a></h3>
<span class="badge badge-year">2022</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">Kaggle</span>

- [chaii - Hindi and Tamil Question Answering の12位解法](https://blog.recruit.co.jp/data/articles/kaggle-chaii/): コンペの概要と解法をまとめた記事。
- [chaii - Hindi and Tamil Question Answering の2位解法](https://techblog.exawizards.com/entry/2021/12/14/170743): 外部データ・アンサンブル・言語特有の後処理などを紹介。

</div>

<div class="competition-entry" markdown="1" data-year="2022" data-datatype="text" data-platform="nishika">
<h3><a href="https://competition.nishika.com/">Nishika 小説家になろう ブクマ数予測</a></h3>
<span class="badge badge-year">2022</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">Nishika</span>

- [「小説家になろう ブクマ数予測 ~"伸びる"タイトルとは？~」3位解法](https://qiita.com/z-lai/items/4b563c4c78bf25427120): 公式振り返り会の録画も公開されている。

</div>

<div class="competition-entry" markdown="1" data-year="2020" data-datatype="tabular" data-platform="other">
<h3>エンジニアの年収予測</h3>
<span class="badge badge-year">2020</span> <span class="badge badge-datatype">Tabular</span> <span class="badge badge-platform">その他</span>

- [「エンジニアの年収予測」1位解法](https://github.com/go5paopao/quevico-salary-prediction-1st-place-solution): Stack Overflow のアンケートから回答者の給料を予測するコンペの解法。

</div>

<div class="competition-entry" markdown="1" data-year="2021" data-datatype="image" data-platform="other">
<h3>Facebook AI Image Similarity Challenge</h3>
<span class="badge badge-year">2021</span> <span class="badge badge-datatype">Image</span> <span class="badge badge-platform">その他</span>

- [Facebook AI Image Similarity Challenge 上位解法まとめ](https://www.drivendata.co/blog/image-similarity-winners/): Kaggle Grandmaster の lyakaap さんが Descriptor Track で優勝。
- [Facebook AI Image Similarity Challenge: Matching Track 2位解法](https://arxiv.org/abs/2111.09113): 同時開催の Descriptor Track では lyakaap さんが優勝。
- [Facebook AI Image Similarity Challenge 入賞解法](https://engineering.dena.com/blog/2021/12/fb-isc-1st/): 課題設定や取り組みを丁寧に解説する記事。

</div>

<div class="competition-entry" markdown="1" data-year="2021" data-datatype="image" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/c/landmark-retrieval-2021">Google Landmark Retrieval 2021</a></h3>
<span class="badge badge-year">2021</span> <span class="badge badge-datatype">Image</span> <span class="badge badge-platform">Kaggle</span>

- [Google Landmark Retrieval 2021 の5位解法](https://acro-engineer.hatenablog.com/entry/2021/10/22/172917): ICCV 2021 の傾向にも言及し、画像処理での Transformer の台頭について紹介。

</div>

<div class="competition-entry" markdown="1" data-year="2021" data-datatype="image" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/c/landmark-recognition-2021">Google Landmark Recognition 2021</a></h3>
<span class="badge badge-year">2021</span> <span class="badge badge-datatype">Image</span> <span class="badge badge-platform">Kaggle</span>

- [Google Landmark Recognition 2021 2位解法論文（bestfitting）](https://arxiv.org/abs/2110.02638): Transformer を用いた画像認識モデルを駆使した解法をまとめた論文。

</div>

<div class="competition-entry" markdown="1" data-year="2021" data-datatype="tabular" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/c/g2net-gravitational-wave-detection">G2Net Gravitational Wave Detection</a></h3>
<span class="badge badge-year">2021</span> <span class="badge badge-datatype">Tabular</span> <span class="badge badge-platform">Kaggle</span>

- [G2Net Gravitational Wave Detection の19位解法](https://qiita.com/anonamename/items/5b7fa5d9d5d7f9970e06): コンペ概要や性能改善で重要だった点を紹介。
- [G2Net Gravitational Wave Detection 銀メダル解法](https://medium.com/@junkoda/kaggle-%E9%87%8D%E5%8A%9B%E6%B3%A2%E3%81%A7%E9%8A%80%E3%83%A1%E3%83%80%E3%83%AB-1c7135e69817): 試行錯誤の過程も含めてまとめた記事。

</div>

<div class="competition-entry" markdown="1" data-year="2021" data-datatype="image" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/c/seti-breakthrough-listen">SETI Breakthrough Listen - E.T. Signal Search</a></h3>
<span class="badge badge-year">2021</span> <span class="badge badge-datatype">Image</span> <span class="badge badge-platform">Kaggle</span>

- [SETI Breakthrough Listen - E.T. Signal Search 金メダル解法](https://oumpy.github.io/blog/2021/08/seti.html): 勉強会での発表も予定された金メダル解法の解説。

</div>

<div class="competition-entry" markdown="1" data-year="2021" data-datatype="tabular" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/c/google-smartphone-decimeter-challenge">Google Smartphone Decimeter Challenge</a></h3>
<span class="badge badge-year">2021</span> <span class="badge badge-datatype">Tabular</span> <span class="badge badge-platform">Kaggle</span>

- [Google Smartphone Decimeter Challenge 金メダル解法（1）](https://lab.mo-t.com/blog/kaggle-gnss): コンペの特徴や上位チームの取り組みをまとめた記事。
- [Google Smartphone Decimeter Challenge 金メダル解法（2）](https://www.t88.work/entry/2021/08/10/005037): 車両に設置した Android スマートフォンのデータから位置を推定する課題の解法。18 位・34 位の銀メダル解法記事も公開。
- [Google Smartphone Decimeter Challenge メダル獲得者によるKaggle取り組み方記事](https://qiita.com/shu421/items/ed255c1ad846c92ba448): Titanic 後の軌跡や所感を綴る記事。

</div>

<div class="competition-entry" markdown="1" data-year="2021" data-datatype="text" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/c/commonlitreadabilityprize">CommonLit Readability Prize</a></h3>
<span class="badge badge-year">2021</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">Kaggle</span>

- [CommonLit Readability Prize 25位の参加録](https://note.com/shigeru_0414/n/n0b0cb0da0c84): コンペ概要・解法・反省点をまとめた参加録。

</div>

<div class="competition-entry" markdown="1" data-year="2021" data-datatype="image" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/c/siim-covid19-detection">SIIM-FISABIO-RSNA COVID-19 Detection</a></h3>
<span class="badge badge-year">2021</span> <span class="badge badge-datatype">Image</span> <span class="badge badge-platform">Kaggle</span>

- [SIIM-FISABIO-RSNA COVID-19 Detection 銅メダルの取り組み](https://qiita.com/RedBull_132/items/97a1fefc8d00d6d4d520): 試行錯誤の過程や反省点を綴った記事。CommonLit Readability Prize の銅メダル解法も合わせて公開。

</div>

<div class="competition-entry" markdown="1" data-year="2021" data-datatype="tabular" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/c/mlb-player-digital-engagement-forecasting">MLB Player Digital Engagement Forecasting</a></h3>
<span class="badge badge-year">2021</span> <span class="badge badge-datatype">Tabular</span> <span class="badge badge-platform">Kaggle</span>

- [MLB Player Digital Engagement Forecasting 参加録](https://sqrt4kaido.hatenablog.com/entry/2021/08/06/022645): 将来のデータを予測するコンペ特有の難しさを端的にまとめた記事。
- [MLB Player Digital Engagement Forecasting コンペ紹介記事（Kaggle公式）](https://cloud.google.com/blog/products/ai-machine-learning/using-machine-learning-to-deconstruct-baseball-fandom): Kaggle の Julia Elliott さんによる紹介記事。大谷翔平選手にも言及。

</div>

<div class="competition-entry" markdown="1" data-year="2021" data-datatype="text" data-platform="other">
<h3>#SwipeToSuccess（Yenta）</h3>
<span class="badge badge-year">2021</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">その他</span>

- [ビジネス版マッチングアプリ「Yenta」のデータを用いた「#SwipeToSuccess」コンペ振り返り](https://note.com/datagateway/n/n19d015dd7483): Kaggle Grandmaster の Senkin さんのコメントも掲載する振り返り記事。

</div>

<div class="competition-entry" markdown="1" data-year="2021" data-datatype="audio" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/c/birdclef-2021">BirdCLEF 2021 - Birdcall Identification</a></h3>
<span class="badge badge-year">2021</span> <span class="badge badge-datatype">Audio</span> <span class="badge badge-platform">Kaggle</span>

- [BirdCLEF 2021 優勝解法まとめ](https://speakerdeck.com/startjapan/birdclef2021matome): 優勝解法に絞って解説した記事も別途公開。
- [BirdCLEF 2021 2位解法](https://arxiv.org/abs/2107.07728): ソースコードも公開された 2 位解法。
- [BirdCLEF 2021 10位解法](https://arxiv.org/abs/2107.04878): 弱ラベルを用いた教師あり学習の枠組みを提案する解法。
- [BirdCLEF 2021 銅メダル解法](https://teyoblog.hatenablog.com/entry/2021/06/05/154849): データの準備から後処理までを具体的に紹介する記事。

</div>

<div class="competition-entry" markdown="1" data-year="2021" data-datatype="multimodal" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/c/shopee-product-matching">Shopee - Price Match Guarantee</a></h3>
<span class="badge badge-year">2021</span> <span class="badge badge-datatype">Multimodal</span> <span class="badge badge-platform">Kaggle</span>

- [Shopee - Price Match Guarantee 2位解法](https://speakerdeck.com/lyakaap/shopee-2nd-place-solutiontoshang-wei-jie-fa-matome): スコアと合わせた解説、コード提出形式コンペでの Tips も掲載。
- [Shopee - Price Match Guarantee 銀メダル解法](https://techblog.exawizards.com/entry/2021/06/07/141648): 画像・テキスト情報を用いて商品をまとめ上げる手法の解説。
- [Shopee - Price Match Guarantee 5位解法](https://acro-engineer.hatenablog.com/entry/2021/05/31/120000): 候補群の生成や凝縮型クラスタリングなどを詳細に紹介。
- [Shopee - Price Match Guarantee 10位解法](https://lab.mo-t.com/blog/kaggle-shopee): 手法を選んだ背景と上位解法もあわせて詳細にまとめた記事。
- [Shopee - Price Match Guarantee 銅メダル解法](https://masatakashiwagi.github.io/portfolio/post/kaggle-shopee-solution/): 記事後半で上位解法もまとめて紹介。

</div>

<div class="competition-entry" markdown="1" data-year="2021" data-datatype="text" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/c/bms-molecular-translation">Bristol-Myers Squibb – Molecular Translation</a></h3>
<span class="badge badge-year">2021</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">Kaggle</span>

- [Bristol-Myers Squibb – Molecular Translation 3位解法](https://dena.ai/news/202106-kaggle-bms/): 同コンペで Grandmaster に昇格した KF さんによる 3 位チーム解法。

</div>

<div class="competition-entry" markdown="1" data-year="2021" data-datatype="text" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/c/coleridgeinitiative-show-us-the-data">Coleridge Initiative - Show US the Data</a></h3>
<span class="badge badge-year">2021</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">Kaggle</span>

- [Coleridge Initiative - Show US the Data 銀メダル解法](https://tmyoda.hatenablog.com/entry/20210628/1624883322): 別の参加者による参加録も合わせて公開。

</div>

<div class="competition-entry" markdown="1" data-year="2021" data-datatype="tabular" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/c/indoor-location-navigation">Indoor Location & Navigation</a></h3>
<span class="badge badge-year">2021</span> <span class="badge badge-datatype">Tabular</span> <span class="badge badge-platform">Kaggle</span>

- [Indoor Location & Navigation 15位解法](https://cocoinit23.com/kaggle-indoor-location-navigation-15th-place-solution/): モデル作成・後処理などを丁寧に説明する解法解説。
- [Indoor Location & Navigation 銅メダル獲得者の取り組み](https://cpptake.com/archives/791): 限られた参加期間でスコアを上げた方法をまとめた記事。Shopee - Price Match Guarantee 終盤参戦での銀メダル獲得記事も合わせて公開。

</div>

<div class="competition-entry" markdown="1" data-year="2021" data-datatype="tabular" data-platform="other">
<h3>ProbSpace「論文の被引用数予測」</h3>
<span class="badge badge-year">2021</span> <span class="badge badge-datatype">Tabular</span> <span class="badge badge-platform">その他</span>

- [ProbSpace「論文の被引用数予測」4位解法](https://pop-ketle.hatenablog.com/entry/2021/04/12/203016): 作成した特徴量などコンペ中の取り組みを具体的に紹介。

</div>

<div class="competition-entry" markdown="1" data-year="2020" data-datatype="tabular" data-platform="signate">
<h3>SIGNATE</h3>
<span class="badge badge-year">2020</span> <span class="badge badge-datatype">Tabular</span> <span class="badge badge-platform">SIGNATE</span>

- [第1回 国土交通省コンペ優勝！賃料予測コンペ1位解法](https://www.estie.jp/blog/entry/2024/12/24/160000)
- [【PCDUA】第1回 国土交通省 地理空間情報データチャレンジの戦い方を考える](https://takaito0423.hatenablog.com/entry/2024/10/23/221608): 地理空間情報コンペの取り組み方の紹介記事。
- [第４回空戦AIチャレンジ最終一位チームの「最終解法」](https://qiita.com/TaroKawa_Spakona/items/0a2f110216f4d00f295c)
- [SIGNATE Cup 2024 夏 旅行パッケージ成約率予測 Bronze Solution](https://resweater.hatenablog.com/entry/2024/09/03/202547): 旅行パッケージの成約率予測コンペの銅メダル解法。
- [ARISE Kaggle部活動記 #6](https://www.ariseanalytics.com/activities/report/20240206/): 第 1 回金融データ活用チャレンジの 4 位解法。
- [SIGNATE 金融データ活用チャレンジ ～解法編～](https://www.nri-digital.jp/tech/20230530-13833/): 第 1 回金融データ活用チャレンジの 21 位解法。
- [【FDUA】第一回 金融データ活用チャレンジの戦い方を考える](https://takaito0423.hatenablog.com/entry/2023/02/03/212539): 提出までのソースコードと改善点を紹介するチュートリアル記事。
- [SIGANTE「ブルーカーボン・ダイナミクスを可視化せよ！」最終評価 14 位の取り組みとコード](https://github.com/upura/signate-jsai2023-bluecarbon)
- [Signate 第2回 金融データ活用チャレンジ ベースラインサマリー](https://zenn.dev/nishimoto/articles/1587fe7a29f145): 企業向けローンの返済可否予測コンペのベースライン記事。
- [SIGNATE Student Cup 2023 の感想](https://qiita.com/haru1385/items/d947a1ba45720e357b1f): 前処理・特徴量・モデルを紹介する 25 位解法。
- [SIGNATE Student Cup 2020](https://signate.jp/competitions/281/summary)
- [SIGNATE 鰹節コンペ 2nd Place Solution](https://www.slideshare.net/ren4yu/signate-2nd-place-solution)
- [【２位解法】SIGNATE開催CDLEハッカソン2020予測性能部門 「画像データに基づく気象予測」の振り返り。](https://oregin-ai.hatenablog.com/entry/2020/09/06/175415)
- [SIGNATE「医学論文の自動仕分けチャレンジ」参加録](https://zenn.dev/kuboko/articles/signate-srwspsg-pytorch): BERT を用いた取り組みを紹介する参加録。
- [SIGNATE「ファンダメンタルズ分析チャレンジ」「ニュース分析チャレンジ」上位チームのコード公開](https://www.jpx.co.jp/corporate/news/news-releases/0010/20210813-01.html): 表彰式での発表資料も掲載。
- [SIGNATE「J-Quants データ分析コンペティション」表彰式 質問への追加回答](https://qiita.com/blog_UKI/items/1e329bd684f06db50ca7): 両部門で 2 位になった参加者による、ソースコード・資料付きの回答記事。
- [SIGNATE「ファンダメンタルズ分析チャレンジ」「ニュース分析チャレンジ」上位解法まとめ（表彰式発表資料）](https://speakerdeck.com/gamella/j-quantsbiao-zhang-hui-zi-liao-shang-wei-ru-shang-zhe-jie-fa-zong-ping-number-jquants): 両部門で 2 位になった参加者のソースコード・資料も掲載。
- [SIGNATE「日本取引所グループ ファンダメンタルズ分析チャレンジ」優勝解法](https://dena.ai/news/202106-fundamentals-analysis-challenge/): 財務諸表から株価の将来の動きを予測するコンペの優勝解法。

</div>

<div class="competition-entry" markdown="1" data-year="2023" data-datatype="tabular" data-platform="nishika">
<h3>Nishika</h3>
<span class="badge badge-year">2023</span> <span class="badge badge-datatype">Tabular</span> <span class="badge badge-platform">Nishika</span>

- [Nishika音声認識コンペに参加して2位になりました！🎉](https://www.ai-shift.co.jp/techblog/4813)
- [Nishika 財務・非財務情報を活用した株式の価値予測コンペ振り返り](https://note.com/nishika_inc/n/n8678212cb614)
- [AI×商標：イメージサーチコンペティション 2nd place solution](https://speakerdeck.com/anyai/nishika-aixshang-biao-imezisatikonpeteisiyon-2nd-place-solution)
- [Nishika「AI×商標：イメージサーチコンペティション（類似商標画像の検出）」優勝解法](https://techblog.yahoo.co.jp/entry/2022061330306280/): 参加から優勝に至るまでの取り組みを時系列で紹介。
- [Nishika 日本酒銘柄画像検索コンペ 7位解法（備忘録）](https://zenn.dev/ubex/articles/0a49c6e912220f)
- [Nishika 中古マンション価格予測コンペ 2023夏の部 3位解法](https://qiita.com/9en310/items/1ef8c957fd43b850162b)
- [材料コンペ（Nishika）の2位解法](https://qiita.com/mi-212/items/694124649d2848a6b559)

</div>

<div class="competition-entry" markdown="1" data-year="2024" data-datatype="3d" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/blood-vessel-segmentation">SenNet + HOA - Hacking the Human Vasculature in 3D</a></h3>
<span class="badge badge-year">2024</span> <span class="badge badge-datatype">3D</span> <span class="badge badge-platform">Kaggle</span>

- [SenNet + HOA 上位解法と復習まとめ](https://zenn.dev/syu_tan/articles/859a3fc56c714b): 腎臓血管のセグメンテーションコンペの上位解法まとめ。

</div>

<div class="competition-entry" markdown="1" data-year="2024" data-datatype="text" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/llm-detect-ai-generated-text">LLM - Detect AI Generated Text</a></h3>
<span class="badge badge-year">2024</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">Kaggle</span>

- [LLM - Detect AI Generated Textの振り返り](https://takaito0423.hatenablog.com/entry/2024/02/06/213041): LLM 生成テキストの判定コンペの 14 位金メダル解法。

</div>

<div class="competition-entry" markdown="1" data-year="2024" data-datatype="tabular" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/home-credit-credit-risk-model-stability">Home Credit - Credit Risk Model Stability</a></h3>
<span class="badge badge-year">2024</span> <span class="badge badge-datatype">Tabular</span> <span class="badge badge-platform">Kaggle</span>

- [Kaggle Home Credit - Credit Risk Model Stability 金メダル(13位)解法](https://qiita.com/Kento_Okumura/items/26004d5c5e129870a6ae): 債務不履行の可能性を評価するコンペの 13 位解法。

</div>

<div class="competition-entry" markdown="1" data-year="2024" data-datatype="image" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/image-matching-challenge-2024">Image Matching Challenge 2024 - Hexathlon</a></h3>
<span class="badge badge-year">2024</span> <span class="badge badge-datatype">Image</span> <span class="badge badge-platform">Kaggle</span>

- [kaggle IMC2024コンペ　上位解法まとめ](https://zenn.dev/yume_neko/articles/050c204c3afd20): 画像から空間表現を生成するコンペの上位解法まとめ。
- [kaggle IMC2024 振り返り（雑）](https://zenn.dev/sugupoko/articles/a656446c336dfd)

</div>

<div class="competition-entry" markdown="1" data-year="2024" data-datatype="text" data-platform="other">
<h3>DS Dojo #1（松尾研究所）</h3>
<span class="badge badge-year">2024</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">その他</span>

- [松尾研究所主催分析コンペ [DS Dojo #1] 回答したLLMの分類 - 1st Solution -](https://zenn.dev/mkj/articles/fe662c205e4158): テキストの出力元 LLM を特定するコンペの優勝解法。

</div>

<div class="competition-entry" markdown="1" data-year="2024" data-datatype="text" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/llm-prompt-recovery">LLM Prompt Recovery</a></h3>
<span class="badge badge-year">2024</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">Kaggle</span>

- [LLM Prompt Recoveryコンペの振り返り](https://speakerdeck.com/ktm/llm-prompt-recoverykonpenozhen-rifan-ri): LLM の出力からプロンプトの再現を試みるコンペの 12 位解法。
- [Kaggle LLM Prompt Recoveryコンペまとめ](https://zenn.dev/s_shohey/articles/be7260809e7a75)

</div>

<div class="competition-entry" markdown="1" data-year="2024" data-datatype="text" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/lmsys-chatbot-arena">LMSYS - Chatbot Arena Human Preference Predictions</a></h3>
<span class="badge badge-year">2024</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">Kaggle</span>

- [Kaggle 「LMSYS - Chatbot Arena Human Preference Predictions」 まとめ](https://zenn.dev/sinchir0/articles/1cb47925a225cb): コンペ概要・データ漏洩の経緯・上位解法の総括記事。

</div>

<div class="competition-entry" markdown="1" data-year="2024" data-datatype="timeseries" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification">HMS - Harmful Brain Activity Classification</a></h3>
<span class="badge badge-year">2024</span> <span class="badge badge-datatype">Time Series</span> <span class="badge badge-platform">Kaggle</span>

- [20240803_関東kaggler会_HMS振り返り&チームで取り組むkaggle](https://speakerdeck.com/sugupoko/20240803-guan-dong-kagglerhui-hmszhen-rifan-ri-and-timudequ-rizu-mukaggle): 脳波分類コンペの 1 位解法と社内チームでの取り組みの発表資料。
- [HMSコンペ 11th Solution (team : kansai-kaggler)](https://speakerdeck.com/t88/hmskonpe-11th-solution-team-kansai-kaggler)
- [2024/04 Kaggle HMS 全体的な解法のまとめ](https://zenn.dev/ycarbon/articles/35f8f6db98b6b2)

</div>

<div class="competition-entry" markdown="1" data-year="2024" data-datatype="text" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/uspto-explainable-ai/">USPTO - Explainable AI for Patent Professionals</a></h3>
<span class="badge badge-year">2024</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">Kaggle</span>

- [Kaggle の『USPTO - Explainable AI for Patent Professionals』コンペティションで金メダル(5位/572チーム)の解法解説](https://www.mcdigital.jp/blog/kaggle-uspto-2024/): 特許検索の説明可能性を扱うコンペの 5 位解法。

</div>

<div class="competition-entry" markdown="1" data-year="2024" data-datatype="image" data-platform="solafune">
<h3><a href="https://solafune.com/ja/competitions/5dfc315c-1b24-4573-804f-7de8d707cd90?menu=about&tab=overview">Sentinel-2 を活用した太陽光パネル検出</a></h3>
<span class="badge badge-year">2024</span> <span class="badge badge-datatype">Image</span> <span class="badge badge-platform">Solafune</span>

- [[solafune] Sentinel-2 を活用した太陽光パネル検出 - 2nd Solution -](https://zenn.dev/mkj/articles/75e9dfac5d309a): 衛星画像から太陽光パネルを検出するコンペの 2 位解法と上位解法の紹介。

</div>

<div class="competition-entry" markdown="1" data-year="2023" data-datatype="tabular" data-platform="atmacup">
<h3><a href="https://www.guruguru.science/competitions/21">#15 atmaCup</a></h3>
<span class="badge badge-year">2023</span> <span class="badge badge-datatype">Tabular</span> <span class="badge badge-platform">atmaCup</span>

- [#15 atmaCup 振り返り& 1st place solution](https://speakerdeck.com/unonao/number-15-atmacup-zhen-rifan-ri-and-1st-place-solution): 振り返り会で発表された優勝解法。

</div>

<div class="competition-entry" markdown="1" data-year="2023" data-datatype="tabular" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/predict-student-performance-from-game-play">Predict Student Performance from Game Play</a></h3>
<span class="badge badge-year">2023</span> <span class="badge badge-datatype">Tabular</span> <span class="badge badge-platform">Kaggle</span>

- [Kaggle : PSPコンペ復習](https://qiita.com/Ak_ki/items/38b85992547454005533): 特徴量選択の考え方に焦点を当てた上位解法の紹介。

</div>

<div class="competition-entry" markdown="1" data-year="2023" data-datatype="image" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/image-matching-challenge-2023">Image Matching Challenge 2023</a></h3>
<span class="badge badge-year">2023</span> <span class="badge badge-datatype">Image</span> <span class="badge badge-platform">Kaggle</span>

- [Kaggle Image Matching Challenge 2023を振り返る](https://qiita.com/roniheka/items/ad4717afff1891c0eea3): 個人参加 3 位の振り返り記事。

</div>

<div class="competition-entry" markdown="1" data-year="2023" data-datatype="tabular" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/icr-identify-age-related-conditions">ICR - Identifying Age-Related Conditions</a></h3>
<span class="badge badge-year">2023</span> <span class="badge badge-datatype">Tabular</span> <span class="badge badge-platform">Kaggle</span>

- [ICRの上位解法を眺めた](https://teyoblog.hatenablog.com/entry/2023/08/15/165058): 匿名特徴量から症状を予測するコンペの上位解法まとめ。

</div>

<div class="competition-entry" markdown="1" data-year="2023" data-datatype="image" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/google-research-identify-contrails-reduce-global-warming">Google Research - Identify Contrails to Reduce Global Warming</a></h3>
<span class="badge badge-year">2023</span> <span class="badge badge-datatype">Image</span> <span class="badge badge-platform">Kaggle</span>

- [Kaggle飛行機雲コンペで3位を獲得しました](https://tech.preferred.jp/ja/blog/kaggle-contrails-3rd-place/): 衛星画像から飛行機雲をセグメンテーションするコンペの 3 位解法。
- [kaggle飛行機雲コンペ　上位解法まとめ](https://zenn.dev/yume_neko/articles/464e6ade7bd736)

</div>

<div class="competition-entry" markdown="1" data-year="2023" data-datatype="image" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/rsna-2023-abdominal-trauma-detection">RSNA 2023 Abdominal Trauma Detection</a></h3>
<span class="badge badge-year">2023</span> <span class="badge badge-datatype">Image</span> <span class="badge badge-platform">Kaggle</span>

- [RSNA 2023 Abdominal Trauma Detection 反省会](https://speakerdeck.com/yu4u/rsna-2023-abdominal-trauma-detection-fan-sheng-hui): 腹部 CT から臓器損傷を判定するコンペの振り返り資料。

</div>

<div class="competition-entry" markdown="1" data-year="2023" data-datatype="audio" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/bengaliai-speech">Bengali.AI Speech Recognition</a></h3>
<span class="badge badge-year">2023</span> <span class="badge badge-datatype">Audio</span> <span class="badge badge-platform">Kaggle</span>

- [【kaggle】 ベンガル語音声認識コンペの振り返り](https://zenn.dev/ktrw/articles/d156db0d3fda8e): ベンガル語音声認識コンペの概要と上位解法のまとめ。
- [kaggle Bengaliコンペ 上位解法まとめ](https://zenn.dev/esprit/articles/89d83756e9f43b)

</div>

<div class="competition-entry" markdown="1" data-year="2023" data-datatype="other" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/stanford-ribonanza-rna-folding">Stanford Ribonanza RNA Folding</a></h3>
<span class="badge badge-year">2023</span> <span class="badge badge-datatype">Other</span> <span class="badge badge-platform">Kaggle</span>

- [Stanford Ribonanza RNA Foldingコンペ 上位解法まとめ](https://zenn.dev/nishimoto/articles/14da0f491c7632): RNA 分子の構造推定コンペの上位解法まとめ。

</div>

<div class="competition-entry" markdown="1" data-year="2023" data-datatype="audio" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/birdclef-2023">BirdCLEF 2023</a></h3>
<span class="badge badge-year">2023</span> <span class="badge badge-datatype">Audio</span> <span class="badge badge-platform">Kaggle</span>

- [Kaggle過去コンペ解説　BirdCLEF 2023](https://zenn.dev/yuto_mo/articles/4e428c3effffcc): 東アフリカの鳥の鳴き声分類コンペの優勝解法の解説。
- [Kaggle振り返り🥈：BirdCLEF 2023](https://moritake04.hatenablog.com/entry/2023/05/29/213619)

</div>

<div class="competition-entry" markdown="1" data-year="2023" data-datatype="timeseries" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/optiver-trading-at-the-close">Optiver - Trading At The Close</a></h3>
<span class="badge badge-year">2023</span> <span class="badge badge-datatype">Time Series</span> <span class="badge badge-platform">Kaggle</span>

- [Optiver 2023 勉強会（データの基礎的な解析＋1st Solution）](https://www.docswell.com/s/8980249862/K6YQ3E-2024-05-23-200638): 終値予測コンペの基礎解析と 1 位解法の勉強会資料。録画も公開。

</div>

<div class="competition-entry" markdown="1" data-year="2023" data-datatype="timeseries" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/child-mind-institute-detect-sleep-states">Child Mind Institute - Detect Sleep States</a></h3>
<span class="badge badge-year">2023</span> <span class="badge badge-datatype">Time Series</span> <span class="badge badge-platform">Kaggle</span>

- [睡眠コンペ 1st place solution](https://speakerdeck.com/unonao/shui-mian-konpe-1st-place-solution): 評価指標に対する後処理の工夫を含む 1 位解法。

</div>

<div class="competition-entry" markdown="1" data-year="2023" data-datatype="other" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/neurips-2023-machine-unlearning">NeurIPS 2023 - Machine Unlearning</a></h3>
<span class="badge badge-year">2023</span> <span class="badge badge-datatype">Other</span> <span class="badge badge-platform">Kaggle</span>

- [Kaggleで賞金200万円ゲットした話 〜 Machine Unlearning と Google AI Assistants 〜](https://speakerdeck.com/toshi_k_datasci/kaggledeshang-jin-200mo-yuan-getutositahua-machine-unlearning-to-google-ai-assistants): 2 つのコンペで賞金を獲得した体験談。

</div>

<div class="competition-entry" markdown="1" data-year="2024" data-datatype="image" data-platform="kaggle">
<h3><a href="https://www.kaggle.com/competitions/isic-2024-challenge">ISIC 2024 - Skin Cancer Detection with 3D-TBP</a></h3>
<span class="badge badge-year">2024</span> <span class="badge badge-datatype">Image</span> <span class="badge badge-platform">Kaggle</span>

- [kaggleのISIC 2024で5位、金メダルと賞金1万ドルを獲得しました](https://blog.recruit.co.jp/data/articles/kaggle_isic2024/): 3 次元全身写真から皮膚がんを特定するコンペの 5 位解法。
- [timmのModelEmaについて（ISIC2024コンペ振り返り①）](https://zenn.dev/morim34/articles/bfa2465defee06): 上位解法の特徴的な取り組みを紹介する振り返り記事。
- [【Kaggle】ISIC2024 240位🥉 振り返り](https://zenn.dev/yuto_mo/articles/9366013cba8d11)

</div>

<div class="competition-entry" markdown="1" data-year="2024" data-datatype="text" data-platform="atmacup">
<h3><a href="https://www.guruguru.science/competitions/24/">#17 [初心者歓迎] atmaCup</a></h3>
<span class="badge badge-year">2024</span> <span class="badge badge-datatype">Text/NLP</span> <span class="badge badge-platform">atmaCup</span>

- [atma cup #17 振り返り会](https://speakerdeck.com/ktrw1011/atma-cup-number-17-zhen-rifan-rihui): 過去コンペの振り返りが効いた優勝解法の発表資料。
- [atmaCup#17-3rd Place Solution-](https://speakerdeck.com/syurenuko/atmacup-number-17-3rd-place-solution): NLP コンペの初手で LLM を活用した 3 位解法。
- [atmaCup #17 参加記録](https://zenn.dev/dalab/articles/e3343558ab97b7): レビューから商品推薦の有無を判定するコンペの 11 位解法。

</div>

<div class="competition-entry" markdown="1" data-year="2024" data-datatype="other" data-platform="other">
<h3>Data Science Osaka Autumn 2024</h3>
<span class="badge badge-year">2024</span> <span class="badge badge-datatype">Other</span> <span class="badge badge-platform">その他</span>

- [Data Science Osaka Autumn 2024 -16th Place solution-](https://speakerdeck.com/ryushi496/data-science-osaka-autumn-2024-16th-place-solution): 人狼の特定と勝利陣営の予測を競うコミュニティコンペの参加記録。

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
- [RecSys Challege 3 位入賞 & 現地参加報告](https://voice.pkshatech.com/n/nd1d935935a90): RecSys Challenge 2024 の 3 位解法と現地参加の報告。
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
- [Solafune「市街地画像の超解像化」11位解法](https://yuta0306.github.io/mscup-feedback): コンペ概要や具体的な取り組みをまとめた記事。
- [Solafune「市街地画像の超解像化」5位解法](https://jp.morgenrot.cloud/blog/super-resolution-of-city-images/): 画像コンペで利用が増えている Swin Transformer を用いた超解像モデルを採用。
- [Solafune「市街地画像の超解像化」参加録](https://sorabatake.jp/25220/): コンペの概要や取り組み、難しかった点を紹介。
- [Solafune「市街地画像の超解像化」ベースライン（ESPCN）](https://zenn.dev/ren_uechi/articles/ab9eea97ec42e5): 日本マイクロソフトとの共同開催コンペのベースライン手法とコードを公開。

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
- [データ分析コンペKDDCUP 2024 OAG-AQA 6位入賞解法の紹介](https://nttdocomo-developers.jp/entry/2024/10/17/090000): 学術質問応答を題材にした KDD Cup 2024 の 6 位解法。
- [データ分析コンペKDDCUP2023にてドコモの2チームが入賞した解法の紹介](https://nttdocomo-developers.jp/entry/2023099840900): 多言語推薦を題材にした KDD Cup 2023 の入賞解法。
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
- [「AI王 〜クイズAI日本一決定戦〜」優勝解法](https://qiita.com/z-lai/items/e547cd2a88a9b7f8e0b6): 言語処理学会第 27 回年次大会のワークショップとして開催されたコンペの優勝解法。

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
- [ProbSpace「Kiva／クラウドファンディングの資金調達額予測」の12位解法](https://yshr10ic.com/2022/02/27/probspace-kiva/): 融資マッチング支援機関「Kiva」の融資額を予測するコンペの解法。

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
