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

## 関連概念

- [表データコンペ](./tabular.md) / [コードコンペティション](./code-competition.md)
