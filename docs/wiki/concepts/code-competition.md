# コードコンペティション

学習済みモデルと推論コードをノートブックとして提出する形式のコンペです。
実行時間制限やインターネット接続の遮断といった制約があるなかで、開発と提出のサイクルをいかに効率化するかが成果を左右します。

## 押さえどころ

- 提出ノートブックには実行時間の制限、インターネット遮断、依存ライブラリの事前準備といった制約があり、学習と推論のコードを分離したワークフローの設計が求められる
- ローカル開発の生産性を上げる工夫が定番化している。VS Code や Kaggle CLI を使ってブラウザ操作を減らし、実装コードを Dataset として管理する方法（[効率的なコードコンペティションの作業フロー](https://ho.lc/blog/kaggle-code-submission)）や、GitHub Actions で学習済みモデルや推論コードの提出を自動化する KaggleOps 的なアプローチ（[code competition も楽したい KaggleOps](https://osushinekotan.hatenablog.com/entry/2025/12/06/072458)）によって、手作業のアップロードを排除できる
- メモリや実行時間の制約が厳しいコンペでは、C++ など Python 以外の言語を部分的に組み込む工夫も有効である（[Riiid Answer Correctness Prediction でのC++メモリ節約記事](https://takkyu.net/ja/riiid-cpp/)）
- LLM を扱うコードコンペでは、制限時間内に推論を終えるために vLLM の利用や量子化による高速化が求められる（[自然言語処理コンペ](./nlp-llm.md)）
- 実験の再現性や管理体制と併せて整備すると運用効率が高まる（[実験管理](./experiment-management.md)）

## 資料

- [効率的なコードコンペティションの作業フロー](https://ho.lc/blog/kaggle-code-submission): VS Code と Kaggle CLI でブラウザ操作を削減し、実装コードを Dataset として管理して提出ノートブックから呼び出す設計パターンの提案。
- [code competition も楽したい KaggleOps](https://osushinekotan.hatenablog.com/entry/2025/12/06/072458): 学習済みモデルと推論コードの提出を GitHub Actions で自動化する構成の紹介。
- [Kaggle「Riiid Answer Correctness Prediction」でのC++メモリ節約記事](https://takkyu.net/ja/riiid-cpp/): C++ を活用してメモリ消費量を抑える方法と、Python からの呼び出し手法を解説した記事。
- [Code Competitionsでの推論・提出方法を解説する記事](https://towardsdatascience.com/submitting-model-predictions-to-kaggle-competition-ccb64b17132e?gi=8f7f83f11330): インターネット接続が制限された環境でのライブラリ導入方法や、推論結果の提出手順を解説した記事。
- [「Code Competitions」形式のTipsまとめ記事](https://nonbiri-tereka.hatenablog.com/entry/2020/09/03/091530): コード提出形式のコンペにおける実践的なノウハウや注意点をまとめた記事。

## 関連概念

- [実験管理](./experiment-management.md) / [自然言語処理コンペ](./nlp-llm.md) / [コンペ形式・技術動向の変遷](./competition-evolution.md)
