# 表データコンペ

表（テーブル）データのコンペは、GBDT を軸に特徴量エンジニアリングとバリデーション設計で競う、Kaggle で最も歴史のある形式です。
近年はニューラルネットワーク（TabM など）の併用や、Polars による高速なデータ処理も定着しつつあります。

## 押さえどころ

- 定跡は、分布シフトを意識した EDA、多様なベースラインの迅速な構築、大量の特徴量生成、ヒルクライミングによるアンサンブルとスタッキング、疑似ラベルとシード平均、という流れで進む。「高速な実験」と「慎重な検証」の両輪が原則（[The Kaggle Grandmasters Playbook](https://developer.nvidia.com/blog/the-kaggle-grandmasters-playbook-7-battle-tested-modeling-techniques-for-tabular-data/)）
- データ処理は pandas から Polars への移行が進んでいる。特徴量の変換処理を `pl.Expr` で宣言的に定義し、計算と切り離してマスター管理する手法も提案されている
- NN 系は GBDT と誤りの傾向が異なり、アンサンブルの多様性源になる。TabM は「GBDT 的なアンサンブルを NN で実現する」アプローチ
- 表データにも基盤モデルの波が来ている。TabFM のようなゼロショット予測モデルは、特徴量設計もチューニングもしないベースラインという新しい選択肢
- バリデーション設計とリーク防止は[性能評価と検証](./evaluation-validation.md)を参照

## 資料

- [The Kaggle Grandmasters Playbook: 7 Battle-Tested Modeling Techniques for Tabular Data](https://developer.nvidia.com/blog/the-kaggle-grandmasters-playbook-7-battle-tested-modeling-techniques-for-tabular-data/): NVIDIA の Grandmaster 陣による表データコンペの定跡 7 選。EDA からアンサンブル・疑似ラベルまでの流れを GPU 高速化前提でまとめている。
- [Grandmaster Pro Tip: Winning First Place in a Kaggle Competition with Stacking Using cuML](https://developer.nvidia.com/blog/grandmaster-pro-tip-winning-first-place-in-a-kaggle-competition-with-stacking-using-cuml/): GPU（cuML）を使ったスタッキングで優勝した手法の解説。
- [実践Data Scienceシリーズ Pythonではじめる データ分析のための前処理入門](https://www.amazon.co.jp/dp/4065395860): 前処理からモデリングまでを体系的に解説する書籍。
- [polars.Exprを使った特徴量管理](https://qiita.com/suikabar/items/7b0886cd88d9438ccc0c): 特徴量の変換処理を `pl.Expr` のコレクションとして一元管理し、必要な特徴量を柔軟に組み合わせる設計の提案。
- [Pytorch LightningでTabM学習・予測](https://qiita.com/gnbrganchan/items/b9009f87f4e85b50442e): 表データ向け NN「TabM」を PyTorch Lightning で実装する手順。複数モデル出力の平均化など実装上の要点を解説。
- [Introducing TabFM: A zero-shot foundation model for tabular data](https://research.google/blog/introducing-tabfm-a-zero-shot-foundation-model-for-tabular-data/): Google Research による表データ向け基盤モデルの紹介。ゼロショットで分類・回帰の予測を生成する。
- [Exploring TabPFN: A Foundation Model Built for Tabular Data](https://towardsdatascience.com/exploring-tabpfn-a-foundation-model-built-for-tabular-data/): 表データ向け基盤モデル TabPFN の紹介記事。TabPFN-2.5 までの発展を解説。
- [Accurate predictions on small data with a tabular foundation model](https://www.nature.com/articles/s41586-024-08328-6): TabPFN を提案した Nature 掲載論文。
- [深層学習VS決定木：テーブルデータ分析の未来](https://voice.pkshatech.com/n/n2f125daeb9da): 表データで決定木系が深層学習を上回る理由を論じた論文の解説記事。
- [テーブルデータ用ニューラルネットワークは勾配ブースティング木にどこまで迫れるのか？（本編）](https://note.com/japan_d2/n/nf8023bf90f8f): LightGBM と NN 系モデルを実データで比較検証した記事。
- [LightGBM予測モデル実装ハンドブック](https://www.amazon.co.jp/dp/479806761X): LightGBM の実装を体系的に扱うハンドブック書籍。
- [Ensemble Metrics](https://github.com/hitachi-nlp/ensemble-metrics): アンサンブルの強み・弱みを精度・多様性・情報損失の観点で要因分析するライブラリ。
- [事例で学ぶ特徴量エンジニアリング](https://amzn.asia/d/1qdK69i): NLP・画像・時系列など 5 つの実例で特徴量エンジニアリングを学ぶ書籍。
- [コンペで使える！？LightGBMで実装する３つの弱教師あり学習](https://tech-blog.abeja.asia/entry/lightgbm-weakly-supervised-learning-202309): 弱教師あり学習 3 設定の解き方と LightGBM 実装の紹介。
- [sklearn.preprocessing.TargetEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html): sklearn v1.3 で追加された target encoding の公式ドキュメント。
- [Python: scikit-learn の LabelEncoder を説明変数の変換に使うのは誤り](https://blog.amedama.jp/entry/sklearn-label-and-ordinal-encoder): 未知の値に対応できる OrdinalEncoder の正しい使い方の解説。
- [人工知能学会２０２３ランチョンセミナー「アンサンブル学習における基礎理論の構築」](https://speakerdeck.com/morishtr/ren-gong-zhi-neng-xue-hui-2023rantiyonsemina-ansanburuxue-xi-niokeruji-chu-li-lun-nogou-zhu): アンサンブルの強み・弱みを分析できる理論の提案資料。
- [最新のテーブルデータ向けNNモデルをまとめてみた](https://zenn.dev/mkj/articles/f7939cb221da14): ベンチマーク TabArena 上位を中心に表データ向け NN を紹介する記事。
- [LightGBM のランク学習における正規化の効果](https://zenn.dev/suk1yak1/articles/0ef5d77b84ac80): lambdarank_norm の効果を検証し、正規化が学習の安定性と精度に寄与すると報告する記事。
- [Train with Terabyte-Scale Datasets on a Single NVIDIA Grace Hopper Superchip Using XGBoost 3.0](https://developer.nvidia.com/blog/train-with-terabyte-scale-datasets-on-a-single-nvidia-grace-hopper-superchip-using-xgboost-3-0/): XGBoost 3.0 で GPU による大規模データ学習を行う方法の紹介。
- [pandasでよくやる操作、Polarsでどうやるの？（Polars: 1.12.0）](https://docs.google.com/presentation/d/1wTOMTL7TreqE4uTyp0msCxhCDqmMRD4MmB10idZs5xA/edit)
- [Polars を Kaggle コンペで使ってみた(LMSYS Chatbot Arena)](https://speakerdeck.com/kohecchi/polars-wo-kaggle-konpedeshi-tutemita-lmsys-chatbot-arena-bcc79d2a-baba-421e-835c-3ddb2e4049f6)
- [プロダクトのコードをpandasからPolarsへ書き換えた話](https://speakerdeck.com/yudai00/purodakutonokodowopandaskarapolarsheshu-kihuan-etahua)
- [polars 1.1.0以降の使える新機能](https://speakerdeck.com/ghibney/polars-1-dot-1-0yi-jiang-noshi-eruxin-ji-neng)
- [Introduction to rpolars](https://rpolars.github.io/articles/rpolars.html): Polars の R 言語版の紹介。
- [Python: Polars で各種エンコーダを実装したライブラリ「Shirokumas」を作った](https://blog.amedama.jp/entry/shirokumas): Target Encoding などを Polars でまとめた特徴量エンジニアリングライブラリの紹介。
- [Polars, 旬の13のお役立ち機能](https://qiita.com/hkzm/items/8427829f6aa7853e6ad8): Polars の便利機能 13 選の紹介記事。
- [pandas vs polars vs cudf 速度比較](https://zakopilo.hatenablog.jp/entry/2023/02/04/220552): 定番 3 ライブラリの処理速度を比較した記事。
- [Target Encoding のスムージングについて](https://blog.amedama.jp/entry/target-encoding-smoothing): Target Encoding のスムージング処理を論文の記載をもとに解説する記事。
- [1月新刊情報『SQLではじめるデータ分析』](https://www.oreilly.co.jp/blog/2022/12/40020_sql_for_data_analysis.html): SQL による前処理・時系列・異常検知などを扱う書籍。
- [評価指標入門〜データサイエンスとビジネスをつなぐ架け橋](https://amzn.asia/d/fsYciY8): 評価指標を軸にビジネス課題をデータサイエンスの問題に落とし込む書籍。
- [Optunaによるブラックボックス最適化](https://amzn.asia/d/6aUSXdB): Optuna 開発者らによるハイパーパラメータ最適化の書籍。
- [『Rユーザのためのtidymodels[実践]入門』という本が出ます。](https://y-mattu.hatenablog.com/entry/tidymodels_book): R 言語の機械学習ライブラリ tidymodels を扱う日本語初の書籍。
- [表形式データライブラリの比較検証（PyCon JP 2022）](https://speakerdeck.com/mhrtech/pyconjp2022-hpc): 大規模な表形式データを処理するライブラリの比較資料。
- [RAPIDS が pip でインストール可能に](https://rapids.ai/pip.html): GPU 機械学習ライブラリ RAPIDS の pip 対応の公式告知。
- [Pandas[GPU] vs Polars[CPU] vs Polars[GPU]](https://zenn.dev/parfait/articles/dedb8c0bda00f8): 表データ処理ライブラリの速度を GPU の有無を含めて比較した記事。
- [Announcing Polars 1.0](https://pola.rs/posts/announcing-polars-1/): Polars の Python 版 v1.0 公開の公式発表。設計刷新と GPU 高速化の展望つき。
- [RAPIDS cuDF Instantly Accelerates pandas up to 50x on Google Colab](https://developer.nvidia.com/blog/rapids-cudf-instantly-accelerates-pandas-up-to-50x-on-google-colab/): GPU 版 pandas「cuDF」が Colab に組み込まれた発表。
- [Accelerating Polars DataFrames](https://pola.rs/posts/polars-on-gpu/): NVIDIA との連携による Polars の GPU 高速化の発表。
- [改訂新版 前処理大全〜SQL/pandas/Polars実践テクニック](https://www.amazon.co.jp/dp/4297141388/): Polars を採用した『前処理大全』の改訂新版。
- [PolarsとPanderaで実現する高速でロバストなデータ処理](https://speakerdeck.com/chimuichimu/polarstopanderadeshi-xian-suru-gao-su-derobasutonadetachu-li): 高速処理の Polars とデータ検証の Pandera を組み合わせる発表資料。
- [テーブル形式のデータセットに対する決定木と深層学習の性能比較論文](https://arxiv.org/abs/2207.08815): 決定木を基にした手法と深層学習手法を比較して議論する論文。
- [テーブルデータを扱う際の特徴量管理の方法を考察する記事](https://teyoblog.hatenablog.com/entry/2022/06/09/193005): 数値かカテゴリかの情報も管理する方法を紹介。
- [不均衡データ分類に関する応用例・解説・手法のリンク集](https://www.jstage.jst.go.jp/article/jjsai/37/3/37_376/_article/-char/ja/): 人工知能学会誌に掲載されたリンク集記事。
- [『データサイエンス100本ノック（構造化データ加工編）』書籍](https://www.socym.co.jp/book/1356): SQL・Python・R の 3 言語に対応した演習書籍。
- [テーブル形式データセットの探索的データ分析の方法を紹介する記事](https://medium.com/epfl-extension-school/advanced-exploratory-data-analysis-eda-with-python-536fa83c578a): さまざまな切り口での集計・可視化の実践例。
- [TabNetのハイパーパラメータ調整方法まとめ](https://zenn.dev/nishimoto/articles/f2af21c24413d3): Kaggle での事例や元論文の記述に基づく調整方法の解説。
- [p値を使ったTarget Encodingの方法紹介記事](https://kuruton.hatenablog.com/entry/2022/02/24/092716): atmaCup のデータで性能向上を確認した検証記事。
- [特徴量エンジニアリングライブラリ「xfeat」の紹介記事](https://blog.amedama.jp/entry/xfeat): 具体的な使い方をコードとともに解説。
- [クリック予測問題を題材にしたデータ分析インターン教材](https://fan-adn.github.io/ist-textbook-open/): データ可視化や過学習への対応など実践的な内容を扱う教材。
- [決定境界付近のサンプル重み調整による不均衡データ対応論文の解説記事](https://qiita.com/koshian2/items/52e4bdc682fc152fe05e): 通常学習後に特殊な損失でファインチューニングする手法を紹介。
- [LightGBMのパラメータ「extra_trees」の紹介記事](https://note.com/j26/n/n64d9c37167a6): 過学習抑制効果のあるパラメータの解説記事。
- [テーブルコンペ頻出の特徴量エンジニアリング技法まとめ記事](https://zenn.dev/colum2131/articles/fffac4654e7c7c): 数値データとカテゴリデータの処理方法を中心に紹介。
- [Pandasの「遅くない書き方」まとめ記事](https://naotaka1128.hatenadiary.jp/entry/2021/12/07/083000): 複数の観点で高速化 Tips を紹介する記事。
- [欠損データ補完手法「MCFlow」の解説資料](https://pseudo-theory-of-everything.hatenablog.com/entry/2021/11/07/143102): 欠損補完とネットワーク更新を繰り返す枠組みの提案。
- [表形式データに対する深層学習の検証記事](https://tech.preferred.jp/ja/blog/deep-table/): 比較用ライブラリを開発・公開した検証記事。
- [カルマンフィルタのアルゴリズム概要とパラメータ影響の解説資料](https://www.slideshare.net/ssuserf7b6ad/ss-250284912/ssuserf7b6ad/ss-250284912): Kaggle「Indoor Location & Navigation」などで利用される手法の解説。
- [scikit-learn v1.0.0の更新内容紹介記事](https://future-architect.github.io/articles/20211008a/): キーワード引数の強制や可視化用クラスなどを抜粋して紹介。
- [特徴量生成ライブラリ「Featuretools」v1.0.0公開](https://github.com/alteryx/featuretools/releases/tag/v1.0.0): テーブル形式データセットに対する自動特徴量生成ライブラリ。
- [Python 3.10.0・CatBoost v1.0.0リリース](https://www.python.org/downloads/release/python-3100/): 両ライブラリの同時期リリースを紹介する記事。
- [Long-tail learning via logit adjustment 紹介資料（ICLR 2021）](https://speakerdeck.com/eumesy/long-tail-learning-via-logit-adjustment): 不均衡データの分類問題に対応する手法の議論。
- [画像向け「TTA」をテーブルデータに適用した論文（WiDS Datathon 2020 1位解法）](https://ieeexplore.ieee.org/document/9462159): テーブルデータでの Test Time Augmentation の応用論文。
- [GBDTのハイパーパラメータを図示しながら解説する記事](https://knknkn.hatenablog.com/entry/2021/06/29/125226): 調整方法についても紹介する記事。
- [決定木系アルゴリズム推論高速化ライブラリの解説記事（RAPIDS FIL）](https://medium.com/rapids-ai/rapids-forest-inference-library-prediction-at-100-million-rows-per-second-19558890bc35): 「Shopee - Price Match Guarantee」金メダルチームも利用したライブラリ。
- [自然言語列を含むテーブルデータの特徴量エンジニアリング技法まとめ記事](https://zenn.dev/koukyo1994/articles/9b1da2482d8ba1): 具体的な実装とともに技法を紹介。
- [LightGBMの損失関数「Focal Loss」の活用記事](https://developers.microad.co.jp/entry/2021/04/26/060000): 不均衡データに有効な損失関数を数式・実装・実験結果付きで解説。
- [表形式の複数データセットでXGBoostと深層学習を比較した研究](https://arxiv.org/abs/2106.03253): XGBoost の優位性とアンサンブルによる性能向上を確認。
- [「Tabular Playground Series」の紹介記事](https://towardsdatascience.com/progressively-approaching-kaggle-f58db71a42a9?gi=32e36ede2a44): Titanic に代わる月次開催の練習用コンペを紹介する記事。
- [LightGBMのデータ量とイテレーション回数の関係を調査した記事](https://blog.amedama.jp/entry/lgbm-data-size-vs-best-iters): 概ね線形な関係にあることを実験的に確認。
- [テーブルデータにVariational Autoencoderを適用する記事](https://note.com/regonn314/n/n492ee6da4bd0): PyTorch での実装を公開。
- [小売予測のベストプラクティス記事（Instacart 2位解法者ら共著）](https://developer.nvidia.com/blog/best-practices-of-using-ai-to-develop-the-most-accurate-retail-forecasting-solution/): 具体的なコードと共にまとめたベストプラクティス。
- [順序関係を持つクラス分類「label distribution learning」の紹介記事](https://tech-blog.optim.co.jp/entry/2021/03/30/100000): 正解ラベルを中心とした正規分布でラベルのゆらぎを考慮する手法。
- [「Pandas」に代わるRust製ライブラリ「Pypolars」の紹介記事](https://medium.com/analytics-vidhya/is-pypolars-the-new-alternative-to-pandas-916400f03fd7): 結合などの速度で優位性を示す実験結果。
- [xfeatで集約特徴量を自作関数で作る方法の紹介記事](https://www.smartbowwow.com/2021/02/xfeataggregation.html): 生成後のカラム名を制御する方法も解説。
- [PyTorchでCatBoostのカスタム損失関数を定義する方法の解説記事](https://towardsdatascience.com/easy-custom-losses-for-tree-boosters-using-pytorch-57ffaa0b2eb3?gi=57a373d316f7): 損失関数の違いによる出力の変化も考察。
- [NODE: Neural Oblivious Decision Ensembles for Deep Learning on Tabular Data の紹介記事](https://towardsdatascience.com/modelling-tabular-data-with-catboost-and-node-929bfbaaeb08?gi=5d170809abeb): CatBoost で知られる Yandex による手法の紹介。実装も公開。
- [勾配ブースティングの学習にTensorFlowの損失関数を使う方法の記事](https://lab.astamuse.co.jp/entry/training-xgboost-with-tensorflow): GPU 対応による計算時間短縮の利点を紹介。
- [KaggleのNotebooks環境で使えるNVIDIA製ライブラリ「NVTabular」の紹介記事](https://medium.com/nvidia-merlin/faster-gpu-based-feature-engineering-and-tabular-deep-learning-training-with-nvtabular-on-kaggle-com-9791fa2f4b61): GPU でテーブルデータを処理する機能を紹介。
- [scikit-learn v0.24の更新内容まとめ記事](https://towardsdatascience.com/new-features-of-scikit-learn-fbbfe7652bfb?gi=df07ba9e078e): Sequential Feature Selector や半教師あり学習の分類器などを紹介。
- [Pandasの value_counts() のあまり知られていない引数を紹介する記事](https://towardsdatascience.com/getting-more-value-from-the-pandas-value-counts-aa17230907a6?gi=fb8fe3fcf37e): `dropna=False`・`bins=N` などを紹介。
- [XGBoost 1.3.0のGPU版SHAP「GPUTreeSHAP」の解説記事](https://medium.com/rapids-ai/gpu-accelerated-shap-values-with-xgboost-1-3-and-rapids-587fad6822): GPU でモデルを解釈する手法の紹介。
- [BigQuery上の機械学習機能「BQML」の検証資料](https://speakerdeck.com/shimacos/bqmlkotohazime): Kaggle「Otto Group Product Classification Challenge」のデータを用いた検証結果。
- [Pandas v1.2.0・SciPy v1.6.0公開](https://pandas.pydata.org/pandas-docs/version/1.2.0/whatsnew/v1.2.0.html): 両ライブラリの同時期リリースを紹介。
- [Tabular Playground Series 2021年4月分開始](https://www.kaggle.com/c/tabular-playground-series-apr-2021/): Titanic データに GAN を用いて生成したデータセットを使用。
- [CatBoost v0.25リリース](https://github.com/catboost/catboost/releases/tag/v0.25): 特徴量重要度に基づく特徴選択機能や GPU 損失計算の変更を追加。
- [テーブルデータへのTransformer利用方法の紹介記事（Riiid実装）](https://future-architect.github.io/articles/20210325/): Kaggle「Riiid Answer Correctness Prediction」を題材に具体的な実装を公開。
- [Amazon製欠損値補完ライブラリ「DataWig」の紹介記事](https://zenn.dev/atfujita/articles/84e826f3b8e4f99d24cb): 深層学習を用いて欠損値を予測するライブラリの紹介。
- [xfeatの紹介記事（Optuna連携）](https://acro-engineer.hatenablog.com/entry/2020/12/15/120000): Optuna と連携した特徴量探索など各機能の使い方をまとめた記事。
- [TabTransformerの提案論文](https://arxiv.org/abs/2012.06678): カテゴリ変数の処理に Transformer 層を用い、勾配ブースティングに匹敵する性能を報告。
- [TabNetの解説記事](https://zenn.dev/sinchir0/articles/9228eccebfbf579bfdf4): 論文の概説と使い方を紹介する記事。
- [Julia言語とPythonを併用したデータ処理方法の提案記事](https://tech.mntsq.co.jp/entry/2020/12/07/154854): Pandas 相当の Julia ライブラリ「DataFrames.jl」などを紹介。
- [GPUデータ処理ライブラリ「cuDF」の紹介記事](https://acro-engineer.hatenablog.com/entry/2020/12/10/120000): Pandas との違いや注意点を具体的なコードと共に紹介。
- [SageMaker上でcuDF・cuMLを用いた前処理記事](https://aws.amazon.com/jp/blogs/news/rapids-on-amazon-sagemaker-processing/): 必要な場合のみ GPU を利用する計算資源の使い分けを紹介。
- [探索的データ分析（EDA）用Pythonライブラリ4選の紹介記事](https://towardsdatascience.com/4-libraries-that-can-perform-eda-in-one-line-of-python-code-b13938a06ae?gi=e0adfce1f1a0): 簡単な使い方と実行結果を GIF で紹介。
- [CatBoostの「Uncertainty estimation」機能の紹介記事](https://towardsdatascience.com/tutorial-uncertainty-estimation-with-catboost-255805ff217e?gi=eb19c92aff1b): コードと共に使い方を解説。
- [Pandasを効率的に学ぶための問題集](https://qiita.com/kunishou/items/bd5fad9a334f4f5be51c): データ集計・抽出・可視化など基本操作を扱う演習問題集。
- [CRANにLightGBMが登場](https://cran.r-project.org/web/packages/lightgbm/index.html): R 言語向け LightGBM パッケージの公開。

## 関連概念

- [時系列予測コンペ](./time-series.md) / [性能評価と検証](./evaluation-validation.md) / [実験管理](./experiment-management.md)
