# エージェント対戦コンペ

予測値ではなく「エージェント」を提出し、参加者同士やモデル同士の対戦で順位を競う形式のコンペです。
Kaggle のシミュレーションコンペとして以前からある形式ですが、LLM 時代に入り大型対戦コンペやモデル評価基盤としての活用が広がっています。

## 押さえどころ

- Kaggle のシミュレーションコンペでは、提出したエージェントが他の参加者のエージェントと対戦し、レーティングで順位が決まる。通常のコンペとは提出物も評価の仕組みも異なる（[公式ドキュメント](https://github.com/Kaggle/kaggle-cli/blob/main/docs/simulation_competitions.md)）
- 2026 年にはポケモンカードゲームを題材にした「[The Pokémon Company - PTCG AI Battle Challenge](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle)」のような、公式ゲームエンジン提供・2 トラック構成・トーナメント決勝という大型対戦コンペが登場した
- Kaggle 自体もチェス・ポーカー・人狼などでモデル同士を対戦させる評価基盤「Game Arena」を展開しており、ゲームを agentic な振る舞いの統制されたサンドボックスと位置づけている（[Google 公式ブログ](https://blog.google/innovation-and-ai/products/kaggle-game-arena/)）。プラットフォームの評価基盤化は[性能評価と検証](./evaluation-validation.md)も参照
- 国内でも SIGNATE「空戦AIチャレンジ」など対戦型コンペが継続的に開催されている（[コンペ解法](../../solutions.md)に優勝解法を掲載）
- 解法はヒューリスティック・強化学習・LLM の組み合わせが主戦場。ヒューリスティックの基礎は[数理最適化コンペ](./optimization.md)と地続き
- 「エージェントを道具として使って通常のコンペを戦う」話題は[AI エージェント活用](./ai-agent.md)へ

## 資料

- [Kaggle Game Arena evaluates AI models through games](https://blog.google/innovation-and-ai/products/kaggle-game-arena/): モデル同士をゲームで対戦させる評価基盤 Game Arena の公式発表。
- [Game Arena: Poker and Werewolf, and Gemini 3 tops chess](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/kaggle-game-arena-updates/): ポーカー・人狼ベンチマークの追加とチェストーナメント結果の続報。
- [Simulation Competitions(kaggle-cli ドキュメント)](https://github.com/Kaggle/kaggle-cli/blob/main/docs/simulation_competitions.md): エージェント提出・対戦評価の仕組みの公式解説。
- [The Pokémon Company - PTCG AI Battle Challenge Simulation](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle): ポケモンカードゲームの対戦 AI を競う大型コンペ（Simulation Track）。
- [第４回空戦AIチャレンジ最終一位チームの「最終解法」](https://qiita.com/TaroKawa_Spakona/items/0a2f110216f4d00f295c): 対戦型空戦コンペの優勝解法。
- [The State of Machine Learning Competitions 2025 Edition](https://mlcontests.com/state-of-machine-learning-competitions-2025/): 対戦トーナメント形式の導入を含む 2025 年のコンペ動向の年次まとめ。
- [ALE-Bench：AIの長期的推論能力を測るコーディングベンチマーク](https://speakerdeck.com/imjk/w-and-b-meetup-number-24-in-tokyo): AtCoder Heuristic Contest 40 問で AI の長期的な問題解決能力を測るベンチマークの紹介資料。
- [AtCoder World Tour Finals 2025 に OpenAI がスポンサーとして参画](https://prtimes.jp/main/html/rd/p/000000059.000028415.html): 「人間 vs AI」のエキシビションが行われた競技プログラミングイベントの発表。
- [誰でもわかる強化学習](https://speakerdeck.com/imai_eruel/reinforcement-learning-for-everyone): Q 学習から DQN までを扱う初学者向けの強化学習資料。
- [Kaggleシミュレーションコンペで強化学習に取り組むときのTips](https://speakerdeck.com/kuto5046/kagglesimiyuresiyonkonpedeqiang-hua-xue-xi-niqu-rizu-mutokinotips): 対戦形式コンペでの強化学習の知見と関連資料のまとめ。
- [Lux AI Season 2が始まったので Season 1を振り返る。](https://speakerdeck.com/kenmatsu4/lux-ai-season-2gashi-matutanode-season-1wozhen-rifan-ru): シミュレーションコンペ Lux AI 初回の概要と上位解法の振り返り資料。
- [『ゼロから作るDeep Learning ❹ 強化学習編』100問解説動画](https://www.youtube.com/playlist?list=PLfEIaAl7qmZqLEvo3fE1wP0bSZ7jWA9u5): 強化学習の問題集を解説する動画シリーズ。
- [『ゼロから作るDeep Learning ❹ 強化学習編』サポートサイト](https://github.com/oreilly-japan/deep-learning-from-scratch-4): サンプルコードを Kaggle Notebook 形式などで公開。
- [『ゼロから作るDeep Learning ❹ 強化学習編』原稿の公開レビュー](https://tree-radius-a8e.notion.site/Deep-Learning-d47ea41a980c492c8ab3cddccb36ba83): 発売前の原稿を公開してのレビュー募集。
- [Minecraftを題材にした強化学習コンペのワークショップ動画](https://www.youtube.com/playlist?list=PLLZt5dr4aQLmkkIWkON-To3F3TEZO4Okq): 上位 3 チームの解法発表とパネルディスカッションを収録。
- [ゲームAIの探索アルゴリズム・実装方法の紹介記事](https://qiita.com/thun-c/items/058743a25c37c87b8aa4): ルールに応じた探索手法を C++ サンプルコード付きで解説。
- [並列強化学習ライブラリ「HandyRL」の紹介記事](https://engineering.dena.com/blog/2021/12/distributed-reinforcement-learning-with-handyrl/): Kaggle「Google Research Football with Manchester City F.C.」5 位、「Hungry Geese」優勝の実績。
- [対戦形式コンペに役立つ強化学習まとめ記事](https://kutohonn.hatenablog.com/entry/2021/12/16/230644): 基本概念から主流の取り組み方、便利なライブラリまでを紹介。
- [Kaggle「Lux AI」参加録](https://teyoblog.hatenablog.com/entry/2021/12/12/220835): 資源を集め街を発展させる対戦形式コンペの参加記録。
- [Kaggle「Hungry Geese」暫定上位チームが使うライブラリ「HandyRL」の紹介記事](https://nonbiri-tereka.hatenablog.com/entry/2021/07/29/072301): PyTorch で使える軽量な深層分散強化学習フレームワークの紹介。

## 関連概念

- [AI エージェント活用](./ai-agent.md) / [性能評価と検証](./evaluation-validation.md) / [数理最適化コンペ](./optimization.md)
