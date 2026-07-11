# 実験管理

コンペの成績は「単位時間あたりの質の高い試行回数」に大きく依存します。
実験の記録、再現性、チーム内での重複防止を仕組み化するのが実験管理です。

## 押さえどころ

- チーム戦では GitHub Issue で実験や知見を管理し、実験の重複を防いで試行回数を最大化する体制が有効（[分析コンペをチームで戦うための技術](https://www.takapy.work/entry/2020/12/22/225715)）
- リポジトリのテンプレート化（Docker、uv、モノレポ構成など）で、コンペごとの環境構築コストを下げてコードを再利用する
- MLflow などの実験管理ツールは、AI エージェントとの協働でも再現性の基盤になる（[AI エージェント活用](./ai-agent.md)）
- 書籍では「[目指せメダリスト！Kaggle実験管理術](https://www.shoeisha.co.jp/book/detail/9784798187457)」がこの話題を専門に扱う（[書籍一覧](../../books.md)）

## 資料

- [kaggle_pipeline](https://github.com/phalanx-hk/kaggle_template): GPU インスタンス前提の Kaggle パイプラインテンプレート。モノレポ構成で Docker・uv・mise を組み込み、コンペ間のコード再利用を促す。
- [分析コンペをチームで戦うための技術](https://www.takapy.work/entry/2020/12/22/225715): 5 人チームでの Issue ベースの実験管理・情報連携の実践記録。
- [Kaggle Competitions Expertが振り返る、データ分析コンペ初心者が入賞するために必要なこと](https://codezine.jp/article/detail/21110)
- [Kaggle GMに学ぶ実験管理 ~2025 spring~](https://hakuhodo-technologies.connpass.com/event/343750/)
- [機械学習プロジェクトにおける実験管理](https://www.docswell.com/s/2625216247/ZQXY9J-2026-02-02-185832): 再現性を担保するための考え方を紹介する講演資料。
- [Kaggle銀メダル獲得に向けた実験管理の工夫](https://aitc.dentsusoken.com/column/how-to-approach-kaggle-competitions/): NLP コンペでの銀メダル獲得を支えた実験管理の実践記録。
- [reduce_mem_usageの高速化](https://tellmoogle.hatenablog.com/entry/2020/12/22/faster_reduce_mem_usage)
- [Pythonでコードに意図を込める方法](https://qiita.com/suikabar/items/29cdc4a2bf1214f0966c)
- [読みやすいPythonコードの書き方 (Ruff・命名規則・型ヒント)](https://www.docswell.com/s/2625216247/52Q6J9-2025-11-11-194450): コーディング規約・型ヒント・整形ツールを扱う講義資料。
- [AIエンジニアリング入門：Pythonによる開発の基礎（uv, Ruff, dataclass, Pyright, Git hooks）](https://zenn.dev/dalab/articles/61f06f6b516f4e): 機械学習開発でのバージョン管理・コード品質管理の基礎をまとめた記事。
- [Kaggleに役立つ高速化・並列化テクニック](https://speakerdeck.com/yuyamaguchi/kaggleniyi-li-tugao-su-hua-bing-lie-hua-tekunituku): アルゴリズム・実行速度・並列化の観点で試行回数を上げる技法の発表資料。
- [【書籍メモ】『先輩データサイエンティストからの指南書 -実務で生き抜くためのエンジニアリングスキル』（技術評論社）](https://upura.hatenablog.com/entry/2025/08/19/181856): コード品質管理・データ確認・実験管理を扱う書籍の書評。

## 関連概念

- [コードコンペティション](./code-competition.md) / [AI エージェント活用](./ai-agent.md)
