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
- [Position: AI Competitions Provide the Gold Standard for Empirical Rigor in GenAI Evaluation](https://arxiv.org/abs/2505.00612): データ汚染が避けにくい生成 AI の評価において、コンペ形式の厳密さを gold standard と位置づける position paper。
- [AIモデルのベンチマークや評価の環境としてKaggleがひっそりと進化している話](https://ho.lc/blog/kaggle-benchmark): コンペ運営で培った対不正技術を活かした「Kaggle Benchmark」による独立したモデル評価環境の紹介。

## 関連概念

- [時系列予測コンペ](./time-series.md) / [表データコンペ](./tabular.md) / [実験管理](./experiment-management.md) / [エージェント対戦コンペ](./agent-competition.md)
