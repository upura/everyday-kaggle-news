# Everyday Kaggle News

データサイエンスコンペティション「[Kaggle](https://www.kaggle.com/)」に関する非公式リンク集です。
有志による記事やサービスなども対象に、用途や話題別にまとめています。

本サイトの特徴は、LLM Wiki として運用している点です。
[u++](https://www.kaggle.com/sishihara) が選定する毎週金曜日配信のニューズレター「[Weekly Kaggle News](https://weeklykagglenews.substack.com/)」の紹介リンクをもとに、LLM が話題ごとの知見の統合と相互リンクを維持し、最新情報の反映前には Pull Request のレビューを通じて確認しています。

競技プログラミングサイト「[AtCoder](https://atcoder.jp/)」における「[AtCoder Clans](https://kato-hiro.github.io/AtCoderClans/)」のような立ち位置を意識しています。
なお既存の類似サイトとして、日本人 Kaggler コミュニティ「kaggler-ja」による「[Kaggler Ja Wiki](https://kaggler-ja.wiki/)」があります。

## 最近の更新

直近の更新の抜粋です（全履歴は[操作ログ](./docs/wiki/log.md)）。

- 2026-07-16: [入門者・初学者向けガイド](./docs/quickstart.md)に「話題別の学び方ガイド」を新設。9つのデータ種別・コンペ形式ごとに対応する概念ページと最初に読む資料への導線を追加
- 2026-07-14: 新規概念ページ「[コンペ形式・技術動向の変遷](./docs/wiki/concepts/competition-evolution.md)」を「技術動向」に追加。表データ中心の時代から対戦型エージェントコンペまでを横断整理
- 2026-07-14: 全号バックフィル完了を受け、全19本の概念ページの「押さえどころ」を資料全体に照らして推敲（GPU 高速化・Optimizer 系譜など、複数ソースを横断した気づきを補強）
- 2026-07-14: 目次を再構成。技術動向系の2ページ（[画像認識・視覚モデルの技術動向](./docs/wiki/concepts/image-recognition-trends.md)・[LLM・自然言語処理の技術動向](./docs/wiki/concepts/nlp-llm-trends.md)）を新見出し「技術動向」へ移動し、「コンペの開催」見出しは廃止して[コンペ開催](./docs/wiki/concepts/competition-hosting.md)を「情報収集・コミュニティ」へ統合
- 2026-07-14: [画像認識コンペ](./docs/wiki/concepts/image-recognition.md)・[自然言語処理コンペ](./docs/wiki/concepts/nlp-llm.md)を実践・定跡と技術動向に分割し、上記 2 ページを新設
- 2026-07-14: Markdown テーブルとして誤レンダリングされていたリンク 4 件（パイプ文字未エスケープ）を修正

## 目次

話題ごとに、Wiki ページ（概説・押さえどころ・資料一覧）と一覧ページを案内します。
リンクの横断検索は「[検索](./docs/search.md)」、ページ間のつながりの可視化は「[概念マップ](./docs/concept-map.md)」から。

### 学び方

- [入門者・初学者向けガイド](./docs/quickstart.md): Kaggle の概要と始め方、まず読む・見る定番資料
- [心構え](./docs/wiki/concepts/mindset.md): コンペとの向き合い方・学び方・実務との関係
- [書籍](./docs/books.md): Kaggle 関連書籍の一覧
- [称号振り返り・インタビュー](./docs/milestones.md): 称号到達の振り返り記事とインタビュー

### 情報収集・コミュニティ

- [最新情報の確認](./docs/recent.md): 公式・有志による情報源
- [コンペプラットフォーム](./docs/platform.md): Kaggle 以外のコンペプラットフォーム・学会併設コンペとコンペの選び方
- [イベント](./docs/events.md): 勉強会・ミートアップなどの記録
- [サービス・ツール](./docs/service.md): 非公式のサービス・ツール
- [コンペ開催](./docs/wiki/concepts/competition-hosting.md): コンペを開く側の知見・開催報告

### データ種別・タスク

- [コンペ解法](./docs/solutions.md): コンペ別の解法・参加録（年・データ種別・プラットフォームで絞り込み可）
- [表データコンペ](./docs/wiki/concepts/tabular.md): GBDT・特徴量エンジニアリング・Polars・表向け NN
- [画像認識コンペ](./docs/wiki/concepts/image-recognition.md): バックボーン選択・公開モデルの活用と高速化
- [自然言語処理コンペ](./docs/wiki/concepts/nlp-llm.md): BERT 系の定跡と LLM 活用・推論高速化
- [時系列予測コンペ](./docs/wiki/concepts/time-series.md): 時間分割バリデーション・損失設計・時系列基盤モデル
- [音声コンペ](./docs/wiki/concepts/audio.md): メルスペクトログラム化と画像モデル適用・異常音検知
- [グラフ](./docs/wiki/concepts/graph.md): グラフ構造データの学習
- [推薦](./docs/wiki/concepts/recommendation.md): 推薦アルゴリズムの基礎と 2 段構成の解法
- [数理最適化コンペ](./docs/wiki/concepts/optimization.md): Santa 系コンペ・AtCoder との親和性
- [エージェント対戦コンペ](./docs/wiki/concepts/agent-competition.md): エージェント提出・対戦形式のコンペと Game Arena などの評価基盤

### 技術動向

- [画像認識・視覚モデルの技術動向](./docs/wiki/concepts/image-recognition-trends.md): Vision Transformer・CLIP・自己教師あり学習と国際会議サーベイ
- [LLM・自然言語処理の技術動向](./docs/wiki/concepts/nlp-llm-trends.md): モデル公開・日本語リソース・ライブラリ・研究サーベイ
- [コンペ形式・技術動向の変遷](./docs/wiki/concepts/competition-evolution.md): 表データ中心の時代から対戦型エージェントコンペまでの変遷を横断整理

### 進め方・環境

- [PyTorch](./docs/wiki/concepts/pytorch.md): 深層学習実装の基礎と高速化
- [コードコンペティション](./docs/wiki/concepts/code-competition.md): 提出形式の制約と作業フロー・提出自動化
- [実験管理](./docs/wiki/concepts/experiment-management.md): 試行回数の最大化・再現性・チーム体制
- [環境構築](./docs/wiki/concepts/environment.md): ローカル・クラウドの計算環境
- [性能評価と検証](./docs/wiki/concepts/evaluation-validation.md): リーク防止・バリデーション設計・データセット品質
- [AI エージェント活用](./docs/wiki/concepts/ai-agent.md): LLM エージェントによるコンペ作業の自動化と限界

## 更新フロー

本リポジトリは LLM Wiki として運用しており、規約は [CLAUDE.md](./CLAUDE.md) に定義しています。

- 週次: Weekly Kaggle News の配信後、GitHub Actions（[weekly-ingest](./.github/workflows/weekly-ingest.yml)）が最新号を取り込み、Pull Request を作成します。号に含まれる URL が展開され、重複を除いて各話題ページ・一覧ページに追加されます。編集者がレビューしてマージすると GitHub Pages に反映されます。Claude Code で `/ingest <URL>` を手動実行することもできます
- 月次: `/lint` でリンク切れ・重複・形式の検査を実行します

## 貢献

Issue や Pull Request を歓迎しています。詳しくは [CONTRIBUTING.md](https://github.com/upura/everyday-kaggle-news/blob/main/CONTRIBUTING.md) をご覧ください。
