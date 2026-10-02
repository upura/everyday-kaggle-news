# Everyday Kaggle News

データサイエンスコンペティション「[Kaggle](https://www.kaggle.com/)」に関する非公式リンク集です。
有志による記事やサービスなども対象に、用途や話題別にまとめています。

本サイトの特徴は、LLM Wiki として運用している点です。
[u++](https://www.kaggle.com/sishihara) が毎週金曜日に配信するニュースレター「[Weekly Kaggle News](https://weeklykagglenews.substack.com/)」の掲載リンクをもとに、LLM が話題ごとの知見の統合と相互リンクを更新し、編集者が Pull Request のレビューを経て反映しています。

競技プログラミングサイト「[AtCoder](https://atcoder.jp/)」向けの情報集約サイト「[AtCoder Clans](https://kato-hiro.github.io/AtCoderClans/)」のような立ち位置を目指しています。
なお既存の類似サイトとして、日本人 Kaggler コミュニティ「kaggler-ja」による「[Kaggler Ja Wiki](https://kaggler-ja.wiki/)」があります。

## 最近の更新

直近の更新の抜粋です（全履歴は[操作ログ](./docs/wiki/log.md)）。

- 2026-10-02: Weekly Kaggle News #352〜#355 を取り込み。AI Agent Security コンペの金メダル解法 2 件、ポケカコンペの銀メダルと銅メダルの参加録 2 件、Gemma 4 Developer Agent コンペ、表データ基盤モデル（TabFM、TabFM-Auto、NVIDIA Kumo Tabular）、文書抽出ベンチマーク ExtractBench、YANS2026 ハッカソン設計記事などを追加
- 2026-09-11: Weekly Kaggle News #344〜#346 を取り込み（取りこぼし分の遡及）。最小のニューラルネットを競う NeuroGolf と農業対戦コンペ Kaggriculture、コンペ開催にかかる費用の記事、コーディングエージェント時代の人間の役割、検索モデルの評価ベンチマークなどを追加
- 2026-09-11: Weekly Kaggle News #350 を取り込み（取りこぼし分の遡及）。学生向けの AIYSS Kaggle League、Kaggle Notebook の P100 提供終了、KDD Cup 2026 のデータ分析エージェントコンペ、Kaggle の型をプロダクト開発に転用する記事を追加
- 2026-09-05: Weekly Kaggle News #351 を取り込み。AI Agent Security コンペの銅メダル解法 2 件と解法共有会、ポケカコンペの参加録、ROGII コンペで生成 AI に実装を委ねた金メダル解法、第 18 回最先端 NLP 勉強会、書籍『イラストで学ぶ 自然言語処理』を追加
- 2026-08-22: Weekly Kaggle News #349 を取り込み。Kaggle のメダルの情報価値を分析した論文、金融予測コンペ 15 年分の設計史、CZII コンペの開催報告論文、人工知能学会の開催支援制度の募集要領と採択コンペ主催者インタビューを追加

## 目次

話題ごとに、Wiki ページ（概説、押さえどころ、資料一覧）と一覧ページを案内します。
リンクの横断検索は「[検索](./docs/search.md)」、ページ間のつながりの可視化は「[概念マップ](./docs/concept-map.md)」から利用できます。

### 学び方

- [入門者・初学者向けガイド](./docs/quickstart.md): Kaggle の概要と始め方、まず読むべき定番資料
- [心構え](./docs/wiki/concepts/mindset.md): コンペとの向き合い方、学び方、実務との関係
- [書籍](./docs/books.md): Kaggle 関連書籍の一覧
- [称号振り返り・インタビュー](./docs/milestones.md): 称号到達時の振り返り記事と上位者インタビュー

### 情報収集・コミュニティ

- [最新情報の確認](./docs/recent.md): 公式発表やコミュニティによる最新情報源
- [コンペ開催カレンダー](./docs/calendar.md): 開催中のメダル対象コンペの期間をタイムライン表示（Kaggle API から毎日自動更新）
- [コンペプラットフォーム](./docs/platform.md): Kaggle 以外のプラットフォームや学会併設コンペ、コンペの選び方
- [イベント](./docs/events.md): 勉強会やミートアップなどの開催記録
- [サービス・ツール](./docs/service.md): 有志が開発した周辺サービスや支援ツール
- [コンペ開催](./docs/wiki/concepts/competition-hosting.md): コンペを主催・設計する側の知見と開催報告

### データ種別・タスク

- [コンペ解法](./docs/solutions.md): コンペ別の解法や参加録（年、データ種別、プラットフォームで絞り込み可能）
- [表データコンペ](./docs/wiki/concepts/tabular.md): GBDT、特徴量エンジニアリング、Polars、表向け NN
- [画像認識コンペ](./docs/wiki/concepts/image-recognition.md): バックボーン選定、公開モデルの活用、推論高速化
- [自然言語処理コンペ](./docs/wiki/concepts/nlp-llm.md): BERT 系の定跡、LLM 活用、推論高速化
- [時系列予測コンペ](./docs/wiki/concepts/time-series.md): 時間分割バリデーション、損失関数設計、時系列基盤モデル
- [音声コンペ](./docs/wiki/concepts/audio.md): メルスペクトログラム化、画像モデルの適用、異常音検知
- [グラフ](./docs/wiki/concepts/graph.md): グラフ構造データの学習手法
- [推薦](./docs/wiki/concepts/recommendation.md): 推薦アルゴリズムの基礎と 2 段階構成の解法
- [数理最適化コンペ](./docs/wiki/concepts/optimization.md): Santa 系コンペや AtCoder（特に AHC）との共通点
- [エージェント対戦コンペ](./docs/wiki/concepts/agent-competition.md): プログラム提出による対戦形式コンペと Game Arena などの評価基盤

### 技術動向

- [画像認識・視覚モデルの技術動向](./docs/wiki/concepts/image-recognition-trends.md): Vision Transformer、CLIP、自己教師あり学習、国際会議サーベイ
- [LLM・自然言語処理の技術動向](./docs/wiki/concepts/nlp-llm-trends.md): モデル公開動向、日本語リソース、ライブラリ、研究サーベイ
- [コンペ形式・技術動向の変遷](./docs/wiki/concepts/competition-evolution.md): 表データ中心の時代から対戦型エージェントコンペまでの変遷の整理

### 進め方・環境

- [PyTorch](./docs/wiki/concepts/pytorch.md): 深層学習モデルの実装基礎と高速化
- [コードコンペティション](./docs/wiki/concepts/code-competition.md): 提出形式の制約、作業フロー、提出自動化
- [実験管理](./docs/wiki/concepts/experiment-management.md): 試行回数の最大化、再現性の確保、チーム開発体制
- [環境構築](./docs/wiki/concepts/environment.md): ローカル環境やクラウド環境の整備
- [性能評価と検証](./docs/wiki/concepts/evaluation-validation.md): リーク防止、バリデーション設計、データセット品質
- [AI エージェント活用](./docs/wiki/concepts/ai-agent.md): LLM エージェントによるコンペ作業の支援と限界

## 更新フロー

本リポジトリは LLM Wiki として運用しており、規約は [GEMINI.md](./GEMINI.md) に定義しています。

- 週次: Weekly Kaggle News の配信後、GitHub Actions（[weekly-ingest](./.github/workflows/weekly-ingest.yml)）が最新号を取り込み、Pull Request を作成します。号に含まれる URL が展開され、重複を除いて各話題ページ・一覧ページに追加されます。編集者がレビューしてマージすると GitHub Pages に反映されます。Gemini CLI で `/ingest <URL>` を手動実行することもできます
- 月次: `/lint` でリンク切れ・重複・形式の検査を実行します

## 貢献

Issue や Pull Request を歓迎しています。詳しくは [CONTRIBUTING.md](https://github.com/upura/everyday-kaggle-news/blob/main/CONTRIBUTING.md) をご覧ください。
