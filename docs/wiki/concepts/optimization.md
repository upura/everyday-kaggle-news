# 数理最適化コンペ

Kaggle の Santa コンペに代表される、機械学習ではなく組合せ最適化やヒューリスティックで競う形式です。
AtCoder のヒューリスティックコンテスト（AHC）と技術的な親和性が高い領域です。

## 押さえどころ

- Santa 系コンペは巡回セールスマン問題などの組合せ最適化が題材で、焼きなまし法やビームサーチなどのヒューリスティックと、ソルバー（混合整数計画など）の使い分けが軸になる
- AtCoder（特に AHC）での経験と練習がそのまま役立つ。入門には AtCoder Heuristic First-step の講義スライドが充実している
- 機械学習コンペとは評価や提出の性質が異なり、探索の実装力と計算資源の使い方が効く

## 資料

- [サンタコンペ2025完全攻略 ～お前らの焼きなましは遅すぎる～](https://speakerdeck.com/terryu16/santakonpe2025wan-quan-gong-lue-oqian-ranoshao-kinamasihachi-sugiru): Santa 2025 の 2 位解法。初期解の構築と巨大近傍焼きなましの高速化を詳説。
- [Kaggleスコアアップセミナー～数理最適化コンテスト Santa 編（2023/06/02）](https://www.docswell.com/s/fixstars/ZVV6JL-20230602)
- [AtCoder Heuristic First-step Vol.1 講義スライド](https://speakerdeck.com/terryu16/atcoder-heuristic-first-step-vol-dot-1-jiang-yi-suraido)
- [AHC (AtCoder Heuristic Contest) 攻略法をレッドコーダーにインタビュー](https://shindannin.hatenadiary.com/entry/2025/12/28/223052): レッドコーダー 4 人に取材したヒューリスティックコンペ攻略のインタビュー。
- [AtCoderはKaggleの役に立つ](https://speakerdeck.com/chettub/di-3hui-guan-dong-kagglerhui-atcoderhakagglenoyi-nili-tu)
- [ヒューリスティックコンテストで機械学習しよう](https://speakerdeck.com/nagiss/hiyurisuteitukukontesutodeji-jie-xue-xi-siyou): AHC での統計的手法の活用事例と特有の難しさを紹介する資料。
- [SantaとAHCと遺伝的アルゴリズム](https://speakerdeck.com/nagiss/santatoahctoyi-chuan-de-arugorizumu): Santa 2022 上位 4 チームの遺伝的アルゴリズムを AHC と絡めて解説する資料。
- [ゲームで学ぶ探索アルゴリズム実践入門～木探索とメタヒューリスティクス](https://amzn.asia/d/4U4n6VD): ゲーム AI を題材にした探索アルゴリズムの入門書。
- [Kaggle Happywhaleコンペ優勝解法でのOptuna使用事例 - 2022/12/10 Optuna Meetup #2](https://www.slideshare.net/pfi/kaggle-happywhaleoptuna-20221210-optuna-meetup-2): 優勝チームによる Optuna 活用事例の発表資料。
- [HACK TO THE FUTURE 2023 予選 1位解法解説](https://engineering.dena.com/blog/2022/12/httf-2023-qual/): NN を用いたヒューリスティックコンテストの優勝解法。
- [Optuna 3.0 リリース](https://medium.com/optuna/optuna-3-part-1-4c6a9022a648): ハイパーパラメータ最適化ツール Optuna v3.0 の公式リリースノート。
- [最適化問題コンテストに取り組む上での指針](https://qiita.com/square1001/items/84604f79f55ff10d99b0): 代表的な手法として貪欲法と山登り法を解説する記事。
- [数理最適化の入門用資料](https://speakerdeck.com/e869120/introduction-to-mathematical-optimization-5cdef842-50f6-4e46-ab2d-549cf85c1b81): 線形計画問題など基本的な問題と解き方を紹介する、競技プログラミング書籍著者による資料。
- [ヒューリスティック・マラソン形式コンテストの入門記事](https://qiita.com/tanaka-a/items/3c2a1bca63759ec71e7f): Kaggle「Santa 2021 - The Merry Movie Montage」も当てはまる形式の入門解説。
- [Optuna v3.0.0-a0 最初のリリース候補公開](https://github.com/optuna/optuna/releases/tag/v3.0.0-a0): 「LightGBMTuner.best_booster」の変更なども含むリリースノート。
- [SIGNATE「タダノ クレーン旋回操作最適化チャレンジ」参加者向けイベント](https://us02web.zoom.us/webinar/register/WN_VNbxaRUsQeihoUkjvHe0cA): SIGNATE 初のシミュレーション形式コンペのイベント。
- [最適化手法「SAM」の性能変化を検証する記事](https://dajiro.com/entry/2021/03/14/124435): 「Sharpness-Aware Minimization」の効果をソースコード付きで検証。
- [PyTorch Lightningで「SAM」を利用する方法の紹介記事](https://chizuchizu.com/blog/sam_lightning/): 画像分類タスクで最高性能を示し話題となった手法の実装方法。
- [Optuna v2.4.0リリース](https://github.com/optuna/optuna/releases/tag/v2.4.0): Python 3.9 サポートを開始したリリース。

## 関連概念

- [表データコンペ](./tabular.md) / [コードコンペティション](./code-competition.md)
