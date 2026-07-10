# 表データコンペ

表(テーブル)データのコンペは、GBDT を軸に特徴量エンジニアリングとバリデーション設計で競う、Kaggle で最も歴史のある形式です。
近年はニューラルネットワーク(TabM など)の併用や、Polars による高速なデータ処理も定着しつつあります。

## 押さえどころ

- 定跡は、分布シフトを意識した EDA、多様なベースラインの迅速な構築、大量の特徴量生成、ヒルクライミングによるアンサンブルとスタッキング、疑似ラベルとシード平均、という流れで進む。「高速な実験」と「慎重な検証」の両輪が原則([The Kaggle Grandmasters Playbook](https://developer.nvidia.com/blog/the-kaggle-grandmasters-playbook-7-battle-tested-modeling-techniques-for-tabular-data/))
- データ処理は pandas から Polars への移行が進んでいる。特徴量の変換処理を `pl.Expr` で宣言的に定義し、計算と切り離してマスター管理する手法も提案されている
- NN 系は GBDT と誤りの傾向が異なり、アンサンブルの多様性源になる。TabM は「GBDT 的なアンサンブルを NN で実現する」アプローチ
- 表データにも基盤モデルの波が来ている。TabFM のようなゼロショット予測モデルは、特徴量設計もチューニングもしないベースラインという新しい選択肢
- バリデーション設計とリーク防止は[性能評価と検証](./evaluation-validation.md)を参照

## 資料

- [The Kaggle Grandmasters Playbook: 7 Battle-Tested Modeling Techniques for Tabular Data](https://developer.nvidia.com/blog/the-kaggle-grandmasters-playbook-7-battle-tested-modeling-techniques-for-tabular-data/): NVIDIA の Grandmaster 陣による表データコンペの定跡 7 選。EDA からアンサンブル・疑似ラベルまでの流れを GPU 高速化前提でまとめている。
- [polars.Exprを使った特徴量管理](https://qiita.com/suikabar/items/7b0886cd88d9438ccc0c): 特徴量の変換処理を `pl.Expr` のコレクションとして一元管理し、必要な特徴量を柔軟に組み合わせる設計の提案。
- [Pytorch LightningでTabM学習・予測](https://qiita.com/gnbrganchan/items/b9009f87f4e85b50442e): 表データ向け NN「TabM」を PyTorch Lightning で実装する手順。複数モデル出力の平均化など実装上の要点を解説。
- [Introducing TabFM: A zero-shot foundation model for tabular data](https://research.google/blog/introducing-tabfm-a-zero-shot-foundation-model-for-tabular-data/): Google Research による表データ向け基盤モデルの紹介。ゼロショットで分類・回帰の予測を生成する。
- [Exploring TabPFN: A Foundation Model Built for Tabular Data](https://towardsdatascience.com/exploring-tabpfn-a-foundation-model-built-for-tabular-data/): 表データ向け基盤モデル TabPFN の紹介記事。TabPFN-2.5 までの発展を解説。
- [LightGBM のランク学習における正規化の効果](https://zenn.dev/suk1yak1/articles/0ef5d77b84ac80): lambdarank_norm の効果を検証し、正規化が学習の安定性と精度に寄与すると報告する記事。
- [pandasでよくやる操作、Polarsでどうやるの？（Polars: 1.12.0）](https://docs.google.com/presentation/d/1wTOMTL7TreqE4uTyp0msCxhCDqmMRD4MmB10idZs5xA/edit)
- [Polars を Kaggle コンペで使ってみた(LMSYS Chatbot Arena)](https://speakerdeck.com/kohecchi/polars-wo-kaggle-konpedeshi-tutemita-lmsys-chatbot-arena-bcc79d2a-baba-421e-835c-3ddb2e4049f6)
- [プロダクトのコードをpandasからPolarsへ書き換えた話](https://speakerdeck.com/yudai00/purodakutonokodowopandaskarapolarsheshu-kihuan-etahua)
- [polars 1.1.0以降の使える新機能](https://speakerdeck.com/ghibney/polars-1-dot-1-0yi-jiang-noshi-eruxin-ji-neng)

## 関連概念

- [時系列予測コンペ](./time-series.md) / [性能評価と検証](./evaluation-validation.md) / [実験管理](./experiment-management.md)
