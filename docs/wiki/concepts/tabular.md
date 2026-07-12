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
- [Ensemble Metrics](https://github.com/hitachi-nlp/ensemble-metrics): アンサンブルの強み・弱みを精度・多様性・情報損失の観点で要因分析するライブラリ。
- [事例で学ぶ特徴量エンジニアリング](https://amzn.asia/d/1qdK69i): NLP・画像・時系列など 5 つの実例で特徴量エンジニアリングを学ぶ書籍。
- [コンペで使える！？LightGBMで実装する３つの弱教師あり学習](https://tech-blog.abeja.asia/entry/lightgbm-weakly-supervised-learning-202309): 弱教師あり学習 3 設定の解き方と LightGBM 実装の紹介。
- [sklearn.preprocessing.TargetEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html): sklearn v1.3 で追加された target encoding の公式ドキュメント。
- [人工知能学会２０２３ランチョンセミナー「アンサンブル学習における基礎理論の構築」](https://speakerdeck.com/morishtr/ren-gong-zhi-neng-xue-hui-2023rantiyonsemina-ansanburuxue-xi-niokeruji-chu-li-lun-nogou-zhu): アンサンブルの強み・弱みを分析できる理論の提案資料。
- [最新のテーブルデータ向けNNモデルをまとめてみた](https://zenn.dev/mkj/articles/f7939cb221da14): ベンチマーク TabArena 上位を中心に表データ向け NN を紹介する記事。
- [LightGBM のランク学習における正規化の効果](https://zenn.dev/suk1yak1/articles/0ef5d77b84ac80): lambdarank_norm の効果を検証し、正規化が学習の安定性と精度に寄与すると報告する記事。
- [Train with Terabyte-Scale Datasets on a Single NVIDIA Grace Hopper Superchip Using XGBoost 3.0](https://developer.nvidia.com/blog/train-with-terabyte-scale-datasets-on-a-single-nvidia-grace-hopper-superchip-using-xgboost-3-0/): XGBoost 3.0 で GPU による大規模データ学習を行う方法の紹介。
- [pandasでよくやる操作、Polarsでどうやるの？（Polars: 1.12.0）](https://docs.google.com/presentation/d/1wTOMTL7TreqE4uTyp0msCxhCDqmMRD4MmB10idZs5xA/edit)
- [Polars を Kaggle コンペで使ってみた(LMSYS Chatbot Arena)](https://speakerdeck.com/kohecchi/polars-wo-kaggle-konpedeshi-tutemita-lmsys-chatbot-arena-bcc79d2a-baba-421e-835c-3ddb2e4049f6)
- [プロダクトのコードをpandasからPolarsへ書き換えた話](https://speakerdeck.com/yudai00/purodakutonokodowopandaskarapolarsheshu-kihuan-etahua)
- [polars 1.1.0以降の使える新機能](https://speakerdeck.com/ghibney/polars-1-dot-1-0yi-jiang-noshi-eruxin-ji-neng)
- [Pandas[GPU] vs Polars[CPU] vs Polars[GPU]](https://zenn.dev/parfait/articles/dedb8c0bda00f8): 表データ処理ライブラリの速度を GPU の有無を含めて比較した記事。
- [Announcing Polars 1.0](https://pola.rs/posts/announcing-polars-1/): Polars の Python 版 v1.0 公開の公式発表。設計刷新と GPU 高速化の展望つき。
- [RAPIDS cuDF Instantly Accelerates pandas up to 50x on Google Colab](https://developer.nvidia.com/blog/rapids-cudf-instantly-accelerates-pandas-up-to-50x-on-google-colab/): GPU 版 pandas「cuDF」が Colab に組み込まれた発表。
- [Accelerating Polars DataFrames](https://pola.rs/posts/polars-on-gpu/): NVIDIA との連携による Polars の GPU 高速化の発表。
- [改訂新版 前処理大全〜SQL/pandas/Polars実践テクニック](https://www.amazon.co.jp/dp/4297141388/): Polars を採用した『前処理大全』の改訂新版。
- [PolarsとPanderaで実現する高速でロバストなデータ処理](https://speakerdeck.com/chimuichimu/polarstopanderadeshi-xian-suru-gao-su-derobasutonadetachu-li): 高速処理の Polars とデータ検証の Pandera を組み合わせる発表資料。

## 関連概念

- [時系列予測コンペ](./time-series.md) / [性能評価と検証](./evaluation-validation.md) / [実験管理](./experiment-management.md)
