# 性能評価と検証

モデルの性能を正しく測る仕組み（バリデーション設計、リーク防止、データセット品質）は、あらゆるコンペの土台です。
「CV と LB の乖離」への向き合い方は、コンペ経験から実務に持ち帰れる代表的な知見でもあります。

## 押さえどころ

- リークとは「本来使えない情報を学習に使ってしまうこと」。運用時に入手できない情報の混入や、データ定義の誤解が典型例で、ドメイン知識、データ定義の正確な理解、可視化で防ぐ（[機械学習の落とし穴 リーク問題について](https://tech-blog.abeja.asia/entry/advent-2023-day15)）
- 時系列データでは時間分割のバリデーションが必須（[時系列予測コンペ](./time-series.md)）
- 評価の観点はコンペ参加だけでなく、データセット構築やコンペ開催の側にも及ぶ。「コンペ形式の評価こそ生成 AI 評価の gold standard」という立場の論文もある
- Kaggle 自体が「Kaggle Benchmarks」やモデル対戦の「Game Arena」を通じて、フロンティアモデルの評価基盤へと機能を広げている（[エージェント対戦コンペ](./agent-competition.md)も参照）
- 信頼できる CV が作れたら、あとは CV を信じて[実験を回す](./experiment-management.md)のが定跡

## 資料

- [機械学習の落とし穴 リーク問題について](https://tech-blog.abeja.asia/entry/advent-2023-day15): リークの定義と実例、回避のための実践的な観点を整理した記事。
- ["良い"データセット構築を考える](https://speakerdeck.com/kentaroy47/detasetutogou-zhu-nituite)
- [学習データって増やせばいいんですか？](https://speakerdeck.com/ftakahashi/xue-xi-detatutezeng-yasebaiindesuka): データを増やすべきか絞るべきかを、絞り込みが有効な条件とともに論じる発表資料。
- [Determining the K in K-fold cross-validation](https://arxiv.org/abs/2511.12698): 交差検証の K を慣習ではなく効用最大化の観点で決める枠組みを提案する論文。
- [shake-upを科学する](https://speakerdeck.com/rsakata/shake-upwoke-xue-suru): コンペ終了時の大きな順位変動の要因を、実体験とシミュレーションから考察する資料。
- [リーダーボードという名の幻影：LMArenaは信じられるのか？](https://jiwasawa.github.io/blog_jp/posts/lmarena/): LLM 対戦評価「Chatbot Arena」の信頼性を指摘した論文の紹介記事。
- [第3回関東kaggler会 🤔 妙だな... (Jun Koda)](https://speakerdeck.com/junkoda/di-3hui-guan-dong-kagglerhui-miao-dana-dot-dot-dot-jun-koda): データへの違和感をきっかけに潜んだ特徴を発見した経験を紹介する発表資料。
- [トラブルがあったコンペに学ぶデータ分析](https://speakerdeck.com/tereka114/toraburugaatutakonpenixue-budetafen-xi): ライセンスやデータ漏洩など、コンペで実際に起きた問題を参加者目線で紹介する資料。
- [機械学習におけるEDAって結局何するの？](https://tech-blog.abeja.asia/entry/advent-2023-day25): 探索的データ分析の目的と心構えを整理した記事。
- [Data-centric視点で過去コンペを振り返る](https://speakerdeck.com/inoichan/data-centricshi-dian-deguo-qu-konpewozhen-rifan-ru): データに着目した視点で過去コンペを振り返る発表資料。
- [Feature Importanceによる特徴量選択とリーク](https://speakerdeck.com/rsakata/feature-importanceniyorute-zheng-liang-xuan-ze-toriku): 変数重要度による特徴量選択でのデータ分割の注意点を人工データで検証した資料。
- [今までにKaggleコンペで使ったLB Probing手法について](https://zenn.dev/bilzard/articles/lb-probing-technique): 提出スコアから評価データの情報を引き出す LB Probing の紹介。
- [Confident Learning](https://speakerdeck.com/asei/confident-learning): 多クラス分類でラベル誤りを効率的に発見する手法の解説資料。
- [Position: AI Competitions Provide the Gold Standard for Empirical Rigor in GenAI Evaluation](https://arxiv.org/abs/2505.00612): データ汚染が避けにくい生成 AI の評価において、コンペ形式の厳密さを gold standard と位置づける position paper。
- [AIモデルのベンチマークや評価の環境としてKaggleがひっそりと進化している話](https://ho.lc/blog/kaggle-benchmark): コンペ運営で培った対不正技術を活かした「Kaggle Benchmark」による独立したモデル評価環境の紹介。
- [Data-Centric AI（Andrew Ng提唱）をまとめた資料](https://www.slideshare.net/KazuyukiMiyazawa/datacentric-ai): 「Data-Centric AI Competition」の解法も紹介する資料。
- [機械学習モデル構築時のデータ漏洩問題を紹介する記事](https://towardsdatascience.com/data-leakage-in-machine-learning-how-it-can-be-detected-and-minimize-the-risk-8ef4e3a97562?gi=1a3ddeb0b0f0): リークの検知方法と対応方法を事例付きで解説。
- [深層学習の予測不確実性をまとめた調査論文の紹介資料](https://www.slideshare.net/ssuser8672d7/uncertainty-in-deep-neural-networks-250505655): 学習・評価データセットの特性差やアンサンブル手法などを取り上げる資料。
- [Uncertainty Baselines: Benchmarks for Uncertainty & Robustness in Deep Learning 解説記事](https://ai.googleblog.com/2021/10/baselines-for-uncertainty-and.html): 標準的な深層学習手法の実装集を公開する取り組みの紹介。
- [ニューラルネットや決定木を簡単なモデルで近似して説明する手法の解説記事](https://qiita.com/tmaehara/items/300e61e4a7a0907e441b): LIME などの専用ライブラリを使わずに説明する手続きを紹介。
- [金融業界での機械学習活用アンチパターン論文の要点まとめ記事](https://zenn.dev/atfujita/articles/35a546f083b69a): データ漏洩やサンプリングなどの問題を扱う論文の解説。
- [金融持株会社を題材にした機械学習アンチパターン論文](https://arxiv.org/abs/2107.00079): コロナ禍での性能悪化やデータ漏洩の問題を扱う原論文。
- [ホールドアウト検証に対する交差検証の理論的優位性を報告する論文の解説記事](https://iblog.ridge-i.com/entry/2021/05/26/110000): 見積もられる誤差の違いを議論する記事。
- [NeurIPS2020「Dataset Shift」論文まとめ資料](https://speakerdeck.com/mkimura/neurips2020-papers-on-dataset-shift-and-machine-learning): 学習・評価データセットの条件が異なる問題設計を扱う論文のまとめ。
- [混同行列ライブラリ「PyCM」の紹介記事](https://tech-blog.optim.co.jp/entry/2020/12/08/100000): 画像分類やセグメンテーションを例に具体的な使い方を解説。
- [ROC曲線の解説記事](https://zenn.dev/jackthekaggler/articles/64b4e32cce7d34022ae3): 図を用いて丁寧に説明する入門記事。
- ["adversarial validation"に関する2016年の記事](https://www.kdnuggets.com/2016/10/adversarial-validation-explained.html): Kaggler の間で言葉の定義や使い方が議論された記事。
- [順序分類タスクの評価指標を提案する論文の解説（ACL2020読み会）](https://speakerdeck.com/diracdiego/20200906-acl2020-metric-for-ordinal-classification-yoheikikuta): 評価指標が満たすべき性質の定義と実験的検証を紹介。
- [Kaggle「COVID19 Global Forecasting」から派生した検証研究](https://github.com/h2oai/covid19-backtesting-publication): 時系列モデルの予測誤差が感染拡大の段階に応じて異なる点を確認し、段階を問わない検証の重要性を強調。

## 関連概念

- [時系列予測コンペ](./time-series.md) / [表データコンペ](./tabular.md) / [実験管理](./experiment-management.md) / [エージェント対戦コンペ](./agent-competition.md)
