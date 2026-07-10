# 実験管理

コンペの成績は「単位時間あたりの質の高い試行回数」に大きく依存します。
実験の記録、再現性、チーム内での重複防止を仕組み化するのが実験管理です。

## 押さえどころ

- チーム戦では GitHub Issue で実験や知見を管理し、実験の重複を防いで試行回数を最大化する体制が有効([分析コンペをチームで戦うための技術](https://www.takapy.work/entry/2020/12/22/225715))
- リポジトリのテンプレート化(Docker、uv、モノレポ構成など)で、コンペごとの環境構築コストを下げてコードを再利用する
- MLflow などの実験管理ツールは、AI エージェントとの協働でも再現性の基盤になる([AI エージェント活用](./ai-agent.md))
- 書籍では「[目指せメダリスト！Kaggle実験管理術](https://www.shoeisha.co.jp/book/detail/9784798187457)」がこの話題を専門に扱う([書籍一覧](../../books.md))

## 資料

- [kaggle_pipeline](https://github.com/phalanx-hk/kaggle_template): GPU インスタンス前提の Kaggle パイプラインテンプレート。モノレポ構成で Docker・uv・mise を組み込み、コンペ間のコード再利用を促す。
- [分析コンペをチームで戦うための技術](https://www.takapy.work/entry/2020/12/22/225715): 5 人チームでの Issue ベースの実験管理・情報連携の実践記録。
- [Kaggle Competitions Expertが振り返る、データ分析コンペ初心者が入賞するために必要なこと](https://codezine.jp/article/detail/21110)
- [Kaggle GMに学ぶ実験管理 ~2025 spring~](https://hakuhodo-technologies.connpass.com/event/343750/)
- [機械学習プロジェクトにおける実験管理](https://www.docswell.com/s/2625216247/ZQXY9J-2026-02-02-185832): 再現性を担保するための考え方を紹介する講演資料。
- [Kaggle銀メダル獲得に向けた実験管理の工夫](https://aitc.dentsusoken.com/column/how-to-approach-kaggle-competitions/): NLP コンペでの銀メダル獲得を支えた実験管理の実践記録。
- [reduce_mem_usageの高速化](https://tellmoogle.hatenablog.com/entry/2020/12/22/faster_reduce_mem_usage)
- [Pythonでコードに意図を込める方法](https://qiita.com/suikabar/items/29cdc4a2bf1214f0966c)

## 関連概念

- [コードコンペティション](./code-competition.md) / [AI エージェント活用](./ai-agent.md)
