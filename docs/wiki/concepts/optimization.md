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

## 関連概念

- [表データコンペ](./tabular.md) / [コードコンペティション](./code-competition.md)
