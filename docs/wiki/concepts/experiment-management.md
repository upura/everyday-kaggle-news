# 実験管理

コンペの成績は「単位時間あたりの質の高い試行回数」に大きく依存します。
実験の記録、再現性、チーム内での重複防止を仕組み化するのが実験管理です。

## 押さえどころ

- チーム戦では GitHub Issue で実験や知見を管理し、実験の重複を防いで試行回数を最大化する体制が有効（[分析コンペをチームで戦うための技術](https://www.takapy.work/entry/2020/12/22/225715)）
- リポジトリのテンプレート化（Docker、uv、モノレポ構成など）で、コンペごとの環境構築コストを下げてコードを再利用する
- MLflow などの実験管理ツールは、AI エージェントとの協働でも再現性の基盤になる（[AI エージェント活用](./ai-agent.md)）
- 書籍では「[目指せメダリスト！Kaggle実験管理術](https://www.shoeisha.co.jp/book/detail/9784798187457)」がこの話題を専門に扱う（[書籍一覧](../../books.md)）

## 資料

### 考え方・体制

- [分析コンペをチームで戦うための技術](https://www.takapy.work/entry/2020/12/22/225715): 5 人チームでの Issue ベースの実験管理・情報連携の実践記録。
- [実験管理 - 結局、重要なのは何なの？-](https://speakerdeck.com/chumajin/shi-yan-guan-li-jie-ju-zhong-yao-nanohahe-nano): 実験管理で本当に重要な点を問い直す登壇資料。
- [機械学習プロジェクトにおける実験管理](https://www.docswell.com/s/2625216247/ZQXY9J-2026-02-02-185832): 再現性を担保するための考え方を紹介する講演資料。
- [Kaggle銀メダル獲得に向けた実験管理の工夫](https://aitc.dentsusoken.com/column/how-to-approach-kaggle-competitions/): NLP コンペでの銀メダル獲得を支えた実験管理の実践記録。
- [Kaggle Competitions Expertが振り返る、データ分析コンペ初心者が入賞するために必要なこと](https://codezine.jp/article/detail/21110)
- [Kaggle GMに学ぶ実験管理 ~2025 spring~](https://hakuhodo-technologies.connpass.com/event/343750/)
- [【書籍メモ】『先輩データサイエンティストからの指南書 -実務で生き抜くためのエンジニアリングスキル』（技術評論社）](https://upura.hatenablog.com/entry/2025/08/19/181856): コード品質管理・データ確認・実験管理を扱う書籍の書評。
- [資源として見る実験プログラム](https://speakerdeck.com/hpprc/zi-yuan-tositejian-rushi-yan-puroguramu): 実験プログラムの管理・実装の指針と技法を紹介する発表資料。
- [Kaggleで考えるMLシステムの設計とアーキテクチャ](https://qiita.com/ieiringoo/items/dec48924e1b82e62752a): コンペを題材に機械学習システムの要件とアーキテクチャを考察する記事。
- [学習が何で律速してるか、把握してますか？](https://aru47.hatenablog.com/entry/2022/12/07/170944): 学習速度低下の要因をデータ読み込み・前処理の観点で整理する記事。
- [機械学習の実験管理ツール比較記事](https://qiita.com/fam_taro/items/401ba82e710dca2781eb): TensorBoard・MLflow・Neptune.ai・Weights & Biases・Comet を比較する記事。
- [Kaggle用独自ライブラリの構成・思想に関する記事](https://teadev.netlify.app/posts/2021-10-20/): 「Google Brain - Ventilator Pressure Prediction」17 位のコード公開も予定した記事。
- [ViEW2021チュートリアル「最新研究の始め方」発表資料](https://www.slideshare.net/cvpaperchallenge/tips-ver2-250474910): 3 社 12 研究室による約 300 ページの研究効率化ノウハウ集。
- [深層学習の実験試行回数を増やすTips資料](https://speakerdeck.com/butsugiri/increasing-number-of-attempts-ver-2021): ファイル分割・コード管理・便利ツールをまとめた資料。
- [Optuna・MLflow・Hydraを組み合わせた実験管理方法の発表資料](https://speakerdeck.com/supikiti/hydra-mlflow-optunafalsezu-mihe-wasedeshou-qing-nishi-meruhaipaparametaguan-li-210b3f53-5c57-4468-b7c8-07ba5f1f05a4): 「Optuna Meetup #1」での発表資料。
- [「1実験1スクリプト」を勧める発表動画](https://www.youtube.com/watch?v=Gmm96T1lpSg&feature=youtu.be): コンペのためのコード管理方針を扱う発表。同勉強会の他 2 件の動画も公開。
- [Pythonのlinter統合ツール「pysen」の紹介記事（Preferred Networks）](https://tech.preferred.jp/ja/blog/pysen-is-the-new-sempai/): flake8・isort・mypy・black を統合管理できるツールの紹介。
- [pysen OSS公開（Preferred Networks）](https://github.com/pfnet/pysen): 3 位入賞コンペでも使われた実績を持つ linter 統合ライブラリの公開。
- [国内10研究室による研究効率化Tipsまとめ資料（200ページ超）](https://www.slideshare.net/cvpaperchallenge/cvpaperchallenge-tips-241914101): 実験管理・便利ツール・他者とのやり取りなど Kaggle 観点でも参考になる資料。
- [実験管理ツール「Weights and Biases」が4500万ドルの資金調達](https://wandb.ai/wandb/news/reports/Weights-and-Biases-raises-45m-to-build-better-tools-for-ML-practitioners--Vmlldzo0NDExMTE): 実験管理の必要性と今後の展開に言及した発表。
- [Hydra・MLflow・Optunaを組み合わせた実験管理術の紹介記事](https://supikiti22.medium.com/hydra-mlflow-optuna%E3%81%AE%E7%B5%84%E3%81%BF%E5%90%88%E3%82%8F%E3%81%9B%E3%81%A7%E6%89%8B%E8%BB%BD%E3%81%AB%E5%A7%8B%E3%82%81%E3%82%8B%E3%83%8F%E3%82%A4%E3%83%91%E3%83%BC%E3%83%91%E3%83%A9%E3%83%A1%E3%83%BC%E3%82%BF%E7%AE%A1%E7%90%86-6b8e6d41b3da): 各ツールの利点や使い方をまとめた記事。
- [Kaggle GrandmasterのtakuokoさんによるpipelineとKaggle過去解法活用の発表](https://the-ai.jp/): コンペに向けた開発環境などを紹介する発表。
- [Kaggle「Tweet Sentiment Extraction」2位チームによる実験管理術の記事](https://recruit.gmo.jp/engineer/jisedai/blog/kaggleops-mlflow/): Google Colaboratory と Kaggle Notebook を駆使した検証結果管理方法の紹介。
- [Kaggle「Otto Group Product Classification Challenge」の実験環境共有記事](https://qiita.com/chizuchizu/items/8261bb831b2eebf1a6af): 「Kaggle Advent Calendar 2020」で多数投稿された実験環境記事の一つ。
- [PyTorchと実験管理ライブラリMLflowの連携記事](https://medium.com/pytorch/mlflow-and-pytorch-where-cutting-edge-ai-meets-mlops-1985cf8aa789): PyTorch Lightning のログ機能強化を紹介。
- [数カ月にわたるKaggleコンペを戦うためのメモ術記事](https://zenn.dev/fkubota/articles/3d8afb0e919b555ef068): 小規模データでコードを検証する実験のコツも紹介。
- [機械学習実験管理ツール「Guild AI」の紹介記事](https://kuromt.hatenablog.com/entry/2020/09/11/230142): コード追加なしで簡単に試せる点が特徴。
- [設定ファイル管理ツール「Hydra」v1.0.0リリース](https://hydra.cc/blog/2020/09/03/Hydra_1.0/): サンプルコードと共に主要な追加機能を解説する公式ブログ記事。
- [実験管理ツール「Comet.ml」の紹介記事](https://www.nogawanogawa.com/entry/comet_ml): Weights & Biases・Neptune.ai と並ぶ実験管理ツールの紹介。
- [機械学習実験管理ツールの紹介・比較記事](http://nonbiri-tereka.hatenablog.com/entry/2020/02/17/090613): Excel・mlflow・Weights and Biases などを複数観点で比較。

### ツール・テンプレート

- [kaggle_pipeline](https://github.com/phalanx-hk/kaggle_template): GPU インスタンス前提の Kaggle パイプラインテンプレート。モノレポ構成で Docker・uv・mise を組み込み、コンペ間のコード再利用を促す。
- [Introducing Trackio: A Lightweight Experiment Tracking Library from Hugging Face](https://huggingface.co/blog/trackio): Hugging Face 製の軽量な実験管理ライブラリの紹介。
- [【関西Kaggler会 2025#1】DatabricksからKaggler向けにMLflowのセッションを実施させて頂きました](https://qiita.com/naoyabe/items/2c19c77cc862cd4cbb00): MLflow を用いた実験管理方法の紹介記事。
- [Google ColabでLightGBM+MLFlow使ってみた](https://qiita.com/tetsuro731/items/671c81669955d98bb6ff): Colab 上で LightGBM と MLflow を組み合わせる方法の紹介。
- [実験を高速化する機械学習パイプライン開発の挑戦](https://tech-blog.abeja.asia/entry/ml-pipeline-development-202307): 加工・学習・推論を一連のワークフローで実行するツール開発の記事。
- [MLコンペ実験テンプレートを作ろう!](https://speakerdeck.com/unonao/mlkonpeshi-yan-tenpuretowozuo-rou): Kaggle Grandmaster によるコンペ向け実験テンプレートの紹介資料。

### コード品質・高速化

- [Pythonでコードに意図を込める方法](https://qiita.com/suikabar/items/29cdc4a2bf1214f0966c)
- [読みやすいPythonコードの書き方 (Ruff・命名規則・型ヒント)](https://www.docswell.com/s/2625216247/52Q6J9-2025-11-11-194450): コーディング規約・型ヒント・整形ツールを扱う講義資料。
- [[関西Kaggler会2025#2LT] 初学者+MLエンジニア対象！ モダンなPythonの書き方](https://speakerdeck.com/koheiiwamasa/guan-xi-kagglerhui-2025-number-2lt-chu-xue-zhe-plus-mlenziniadui-xiang-modannapythonnoshu-kifang): uv・ruff・mypy などを使う可読性向上 Tips の発表資料。
- [テスト駆動Kaggle](https://speakerdeck.com/isax1015/tesutoqu-dong-kaggle): テストコードを書きながらコンペに取り組む考え方と実装例の発表資料。
- [AIエンジニアリング入門：Pythonによる開発の基礎（uv, Ruff, dataclass, Pyright, Git hooks）](https://zenn.dev/dalab/articles/61f06f6b516f4e): 機械学習開発でのバージョン管理・コード品質管理の基礎をまとめた記事。
- [Kaggleに役立つ高速化・並列化テクニック](https://speakerdeck.com/yuyamaguchi/kaggleniyi-li-tugao-su-hua-bing-lie-hua-tekunituku): アルゴリズム・実行速度・並列化の観点で試行回数を上げる技法の発表資料。
- [オブジェクト指向に学ぶデータサイエンスのコーディング術](https://zenn.dev/zenkigen_tech/articles/f15988969d9c3f): 前処理をクラスに整理して可読性・再利用性を高める考え方の紹介。
- [2024年のPythonプログラミング](https://tech.uzabase.com/entry/2024/02/02/120601): 利用頻度の高い Python の新機能・ライブラリ・ツールのまとめ。
- [reduce_mem_usageの高速化](https://tellmoogle.hatenablog.com/entry/2020/12/22/faster_reduce_mem_usage)
- [爆速Python](https://www.shoeisha.co.jp/book/detail/9784798183732): 組み込み機能から GPU 利用まで、Python の処理速度に焦点を当てた書籍。

## 関連概念

- [コードコンペティション](./code-competition.md) / [AI エージェント活用](./ai-agent.md)
