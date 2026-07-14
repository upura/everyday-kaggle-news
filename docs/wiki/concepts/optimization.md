# 数理最適化コンペ

Kaggle の Santa コンペに代表される、機械学習ではなく組合せ最適化やヒューリスティックで競う形式です。
AtCoder のヒューリスティックコンテスト（AHC）と技術的な親和性が高い領域です。

## 押さえどころ

- Santa 系コンペは巡回セールスマン問題などの組合せ最適化が題材で、焼きなまし法やビームサーチなどのヒューリスティックと、ソルバー（混合整数計画など）の使い分けが軸になる
- AtCoder（特に AHC）での経験と練習がそのまま役立つ。入門には AtCoder Heuristic First-step の講義スライドが充実している
- 機械学習コンペとは評価や提出の性質が異なり、探索の実装力と計算資源の使い方が効く

## 資料

### 入門・基礎

- [Kaggleスコアアップセミナー～数理最適化コンテスト Santa 編（2023/06/02）](https://www.docswell.com/s/fixstars/ZVV6JL-20230602)
- [AtCoder Heuristic First-step Vol.1 講義スライド](https://speakerdeck.com/terryu16/atcoder-heuristic-first-step-vol-dot-1-jiang-yi-suraido)
- [AHC (AtCoder Heuristic Contest) 攻略法をレッドコーダーにインタビュー](https://shindannin.hatenadiary.com/entry/2025/12/28/223052): レッドコーダー 4 人に取材したヒューリスティックコンペ攻略のインタビュー。
- [AtCoderはKaggleの役に立つ](https://speakerdeck.com/chettub/di-3hui-guan-dong-kagglerhui-atcoderhakagglenoyi-nili-tu)
- [ゲームで学ぶ探索アルゴリズム実践入門～木探索とメタヒューリスティクス](https://amzn.asia/d/4U4n6VD): ゲーム AI を題材にした探索アルゴリズムの入門書。
- [数理最適化の入門用資料](https://speakerdeck.com/e869120/introduction-to-mathematical-optimization-5cdef842-50f6-4e46-ab2d-549cf85c1b81): 線形計画問題など基本的な問題と解き方を紹介する、競技プログラミング書籍著者による資料。
- [ヒューリスティック・マラソン形式コンテストの入門記事](https://qiita.com/tanaka-a/items/3c2a1bca63759ec71e7f): Kaggle「Santa 2021 - The Merry Movie Montage」も当てはまる形式の入門解説。

### AHC/Santa攻略

- [ヒューリスティックコンテストで機械学習しよう](https://speakerdeck.com/nagiss/hiyurisuteitukukontesutodeji-jie-xue-xi-siyou): AHC での統計的手法の活用事例と特有の難しさを紹介する資料。
- [SantaとAHCと遺伝的アルゴリズム](https://speakerdeck.com/nagiss/santatoahctoyi-chuan-de-arugorizumu): Santa 2022 上位 4 チームの遺伝的アルゴリズムを AHC と絡めて解説する資料。
- [HACK TO THE FUTURE 2023 予選 1位解法解説](https://engineering.dena.com/blog/2022/12/httf-2023-qual/): NN を用いたヒューリスティックコンテストの優勝解法。
- [最適化問題コンテストに取り組む上での指針](https://qiita.com/square1001/items/84604f79f55ff10d99b0): 代表的な手法として貪欲法と山登り法を解説する記事。
- [SIGNATE「タダノ クレーン旋回操作最適化チャレンジ」参加者向けイベント](https://us02web.zoom.us/webinar/register/WN_VNbxaRUsQeihoUkjvHe0cA): SIGNATE 初のシミュレーション形式コンペのイベント。

### Optuna・ハイパーパラメータ最適化

- [Kaggle Happywhaleコンペ優勝解法でのOptuna使用事例 - 2022/12/10 Optuna Meetup #2](https://www.slideshare.net/pfi/kaggle-happywhaleoptuna-20221210-optuna-meetup-2): 優勝チームによる Optuna 活用事例の発表資料。
- [Optuna 3.0 リリース](https://medium.com/optuna/optuna-3-part-1-4c6a9022a648): ハイパーパラメータ最適化ツール Optuna v3.0 の公式リリースノート。
- [Optuna v3.0.0-a0 最初のリリース候補公開](https://github.com/optuna/optuna/releases/tag/v3.0.0-a0): 「LightGBMTuner.best_booster」の変更なども含むリリースノート。
- [Optuna v2.4.0リリース](https://github.com/optuna/optuna/releases/tag/v2.4.0): Python 3.9 サポートを開始したリリース。
- [Optunaチュートリアルページ刷新](https://optuna.readthedocs.io/en/latest/tutorial/index.html): Python・Jupyter Notebook 形式でダウンロードして実行できる公式チュートリアル。
- [Optuna v2.3.0リリース](https://github.com/optuna/optuna/releases/tag/v2.3.0): LightGBMTunerCV からの個別モデル取得や多目的 TPE sampler などを追加。
- [Optuna v2.2.0リリース（TPE改善）](https://medium.com/optuna/multivariate-tpe-makes-optuna-even-more-powerful-63c4bfbaebe2): デフォルト探索アルゴリズム TPE の改善機能を実装。
- [Optunaの実装を丁寧に解説する記事（Minituna）](https://cyberagent.ai/optuna-from-scratch): 簡略化版「Minituna」で各モジュールの役割を分かりやすく解説。
- [Optuna v1.4.0リリース](https://github.com/optuna/optuna/releases/tag/v1.4.0): 多目的最適化や MLFlow・AllenNLP とのインテグレーション機能を追加。
- [Optuna v1.3.0リリース](https://github.com/optuna/optuna/releases/tag/v1.3.0): ハイパーパラメータの重要度を可視化する機能などを追加。
- [OptunaでQWKを最適化する記事](https://blog.amedama.jp/entry/optuna-qwk-optimization): 連続値を離散値に変換する閾値の探索を紹介。
- [OptunaのHyperband実装解説記事](https://medium.com/optuna/optuna-supports-hyperband-93b0cae1a137): v1.1.0 で導入された探索アルゴリズムの実装方法と実験結果を報告。
- [Optuna拡張機能「LightGBM Tuner」の紹介記事](https://tech.preferred.jp/ja/blog/hyperparameter-tuning-with-optuna-integration-lightgbm-tuner/): 「重要なハイパーパラメータから順に調整する」という Kaggler の経験則を実装。

### 最適化手法・アルゴリズム研究

- [最適化手法「SAM」の性能変化を検証する記事](https://dajiro.com/entry/2021/03/14/124435): 「Sharpness-Aware Minimization」の効果をソースコード付きで検証。
- [PyTorch Lightningで「SAM」を利用する方法の紹介記事](https://chizuchizu.com/blog/sam_lightning/): 画像分類タスクで最高性能を示し話題となった手法の実装方法。
- [最適化アルゴリズム「AdaBelief」の解説記事（NeurIPS 2020）](https://qiita.com/z-lai/items/b4d02f1050e99c59ad37): Adam と比較しながら特徴を紹介する記事。

## 関連概念

- [表データコンペ](./tabular.md) / [コードコンペティション](./code-competition.md)
