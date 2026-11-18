# エージェント対戦コンペ

予測値ではなくエージェントや攻撃プログラムを提出し、対戦や評価環境での振る舞いで順位を競う形式のコンペです。
Kaggle のシミュレーションコンペとして以前から存在する形式ですが、LLM の登場以降は開発・分析エージェントの評価やモデル評価基盤としても広がっています。

## 押さえどころ

- Kaggle のシミュレーションコンペでは、提出したエージェントが他の参加者のエージェントと対戦し、レーティングで順位が決まる。通常のコンペとは提出物も評価の仕組みも異なる（[公式ドキュメント](https://github.com/Kaggle/kaggle-cli/blob/main/docs/simulation_competitions.md)）
- 2026 年にはポケモンカードゲームを題材にした「[The Pokémon Company - PTCG AI Battle Challenge](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle)」のような、公式ゲームエンジン提供、2 トラック構成、トーナメント決勝を備えた大型対戦コンペが登場した
- Kaggle 自体もチェス、ポーカー、人狼などでモデル同士を対戦させる評価基盤「Game Arena」を展開し、ゲームをエージェントの統制された評価環境と位置づけている（[Google 公式ブログ](https://blog.google/innovation-and-ai/products/kaggle-game-arena/)、[性能評価と検証](./evaluation-validation.md)）。
- 国内でも SIGNATE「空戦AIチャレンジ」など対戦型コンペが継続的に開催されている（[コンペ解法](../../solutions.md)に優勝解法を掲載）。
- 解法はヒューリスティック、強化学習、LLM の組み合わせが主流で、ヒューリスティックが強化学習に劣らない事例も多い（[「Halite」の知見まとめ](https://www.twosigma.com/insights/article/best-practices-from-building-a-machine-learning-bot-for-halite/)、[数理最適化コンペ](./optimization.md)）。
- 強化学習ライブラリでは HandyRL が複数のコンペで優勝・上位入賞の実績を持つ定番となっている。
- 対戦環境では相手、先攻後攻、乱数シードを揃えて評価用エージェントを複数用意しないと改善を見誤るため、条件を固定した専用の検証手順が必要になる（[ポケカコンペの参加録](../../solutions.md)）。
- 解法は、ルールベース → 数手先の探索 → 自己対戦データからの価値関数 → 行動クローン・自己対戦による微調整 → 公開情報からの相手推定、と段階的に拡張するのが定石である。
- エージェント同士の対戦だけでなく、LLM エージェントへの多段階攻撃を生成する「[AI Agent Security](https://www.kaggle.com/competitions/ai-agent-security-multi-step-tool-attacks)」や、分析・開発エージェントの実装一式を評価する「[KDD Cup 2026: Data Agents](https://dataagent.top/)」「[Gemma 4 Developer Agent Competition](https://www.kaggle.com/competitions/gemma-4-developer-agent)」など、エージェントの安全性や開発能力を競う形式も広がっている（[コンペ形式・技術動向の変遷](./competition-evolution.md)）。
- 「エージェントを道具として使って通常のコンペを戦う」話題は[AI エージェント活用](./ai-agent.md)へ。

## 資料

### Kaggle公式・評価基盤・大型対戦コンペ

- [Kaggle Game Arena evaluates AI models through games](https://blog.google/innovation-and-ai/products/kaggle-game-arena/): モデル同士をゲームで対戦させる評価基盤 Game Arena の公式発表。
- [Game Arena: Poker and Werewolf, and Gemini 3 tops chess](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/kaggle-game-arena-updates/): ポーカーや人狼ベンチマークの追加と、チェストーナメント結果の続報。
- [Simulation Competitions(kaggle-cli ドキュメント)](https://github.com/Kaggle/kaggle-cli/blob/main/docs/simulation_competitions.md): エージェント提出や対戦評価の仕組みを解説した公式ドキュメント。
- [The Pokémon Company - PTCG AI Battle Challenge Simulation](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle): ポケモンカードゲームの対戦 AI を競う大型コンペ（Simulation Track）。
- [AI Agent Security - Multi-Step Tool Attacks](https://www.kaggle.com/competitions/ai-agent-security-multi-step-tool-attacks): ツールを使う LLM エージェントへの多段階攻撃を設計するコンペ。予測値ではなく攻撃候補を生成するコードを提出する形式で、4,000 チーム超が参加した。
- [Google - The Gemma 4 Developer Agent Competition](https://www.kaggle.com/competitions/gemma-4-developer-agent): Gemma 4 を自律型ソフトウェアエンジニアリングエージェントとして事後学習させるコンペ。モデル重み（LoRA アダプタ）だけでなく、システムプロンプト、ツール定義、エージェントハーネスの構成（agent.yaml）を一括で提出して実リポジトリの課題解決力を競う形式で、論文審査のみの [Paper Track](https://www.kaggle.com/competitions/gemma-4-developer-agent-paper) も併設されている。
- [KDD Cup 2026: Data Agents for Complex Data Analysis](https://dataagent.top/): 表、文書、ログ、API、知識グラフが混在するデータ束と自然言語の問いを渡し、分析の段取りを自律的に組み立てさせる KDD Cup の公式サイト。評価は DataAgent-Bench のタスク群で行い、順位を競う Leaderboard Track とシステムの完成度や新規性を評価する Creative Track の 2 本立てになっている。
- [KDD Cup 2026 Data Agents: Presentation Archive](https://dataagent.top/presentations): 上記コンペの最終順位と上位チームのシステムや発表資料を公開するアーカイブ。
- [Kaggriculture](https://www.kaggle.com/competitions/kaggriculture): 農業シミュレーション上で収益の最大化を競う 2 人対戦のターン制コンペ。2026 年 7 月開始のメダル対象コンペで、8,000 チーム超が参加した。
- [The State of Machine Learning Competitions 2025 Edition](https://mlcontests.com/state-of-machine-learning-competitions-2025/): 対戦トーナメント形式の導入を含む 2025 年のコンペ動向の年次まとめ。
- [ALE-Bench：AIの長期的推論能力を測るコーディングベンチマーク](https://speakerdeck.com/imjk/w-and-b-meetup-number-24-in-tokyo): AtCoder Heuristic Contest 40 問で AI の長期的な問題解決能力を測るベンチマークの紹介資料。
- [AtCoder World Tour Finals 2025 に OpenAI がスポンサーとして参画](https://prtimes.jp/main/html/rd/p/000000059.000028415.html): 「人間 vs AI」のエキシビションが行われた競技プログラミングイベントの発表。

### 対戦形式コンペの解法・参加録

- [Kaggleシミュレーションコンペで強化学習に取り組むときのTips](https://speakerdeck.com/kuto5046/kagglesimiyuresiyonkonpedeqiang-hua-xue-xi-niqu-rizu-mutokinotips): 対戦形式コンペでの強化学習の知見と関連資料のまとめ。
- [Lux AI Season 2が始まったので Season 1を振り返る。](https://speakerdeck.com/kenmatsu4/lux-ai-season-2gashi-matutanode-season-1wozhen-rifan-ru): シミュレーションコンペ Lux AI 初回の概要と上位解法の振り返り資料。
- [ゲームAIの探索アルゴリズム・実装方法の紹介記事](https://qiita.com/thun-c/items/058743a25c37c87b8aa4): ルールに応じた探索手法を、C++ サンプルコード付きで解説した記事。
- [対戦形式コンペに役立つ強化学習まとめ記事](https://kutohonn.hatenablog.com/entry/2021/12/16/230644): 基本概念から主流のアプローチ、有用なライブラリまでを解説した記事。
- [Kaggle「Lux AI」参加録](https://teyoblog.hatenablog.com/entry/2021/12/12/220835): 資源を集め街を発展させる対戦形式コンペの参加記録。
- [Kaggle「Hungry Geese」暫定上位チームが使うライブラリ「HandyRL」の紹介記事](https://nonbiri-tereka.hatenablog.com/entry/2021/07/29/072301): PyTorch で利用できる軽量な深層分散強化学習フレームワークの紹介。
- [「KDD CUP 2020」強化学習コンペ3位解法（タクシー配車最適化）](https://qiita.com/dcm_demizu/items/9a3bc6e54afc5008bb2b): 配車最適化タスクにおける強化学習解法と関連リソースのまとめ。
- [Kaggle「Halite by Two Sigma」強化学習体験談](https://threecourse.hatenablog.com/entry/2020/09/17/014155): ルールベース手法との比較や、強化学習特有の難しさを記した参加記事。
- [コンピュータ将棋大会「電竜戦」でディープラーニングソフト「GCT」が優勝](https://tadaoyamaoka.hatenablog.com/entry/2020/11/22/220015): 将棋大会で深層学習ソフトが優勝した事例。学習用データセットとコードも公開されている。
- [Kaggle「Connect X」強化学習コンペの実装解説体験記](https://yukoishizaki.hatenablog.com/entry/2020/04/05/202935): 『Pythonで学ぶ強化学習』の内容をもとにした実装と参加体験記。

### 強化学習ライブラリ・学習リソース

- [誰でもわかる強化学習](https://speakerdeck.com/imai_eruel/reinforcement-learning-for-everyone): Q 学習から DQN までを扱う初学者向けの強化学習資料。
- [『ゼロから作るDeep Learning ❹ 強化学習編』100問解説動画](https://www.youtube.com/playlist?list=PLfEIaAl7qmZqLEvo3fE1wP0bSZ7jWA9u5): 強化学習の問題集を解説する動画シリーズ。
- [『ゼロから作るDeep Learning ❹ 強化学習編』サポートサイト](https://github.com/oreilly-japan/deep-learning-from-scratch-4): サンプルコードを Kaggle Notebook 形式などで公開している公式リポジトリ。
- [『ゼロから作るDeep Learning ❹ 強化学習編』原稿の公開レビュー](https://tree-radius-a8e.notion.site/Deep-Learning-d47ea41a980c492c8ab3cddccb36ba83): 発売前の原稿を公開してのレビュー募集。
- [Minecraftを題材にした強化学習コンペのワークショップ動画](https://www.youtube.com/playlist?list=PLLZt5dr4aQLmkkIWkON-To3F3TEZO4Okq): 上位 3 チームの解法発表とパネルディスカッションを収録。
- [並列強化学習ライブラリ「HandyRL」の紹介記事](https://engineering.dena.com/blog/2021/12/distributed-reinforcement-learning-with-handyrl/): Kaggle『Google Research Football』5 位、『Hungry Geese』優勝などの実績を持つライブラリの解説。
- [ソニー深層強化学習ライブラリ「nnablaRL」の紹介動画](https://www.youtube.com/watch?v=xjwrPjJebBg&feature=youtu.be): 実装済みアルゴリズムやチュートリアルについて解説した紹介動画。
- [DeNAエンジニアによる強化学習ライブラリ「HandyRL」公開](https://dena.ai/news/202103-handyrl/): 分散強化学習フレームワーク HandyRL の公開告知とコンペ実績の紹介。
- [強化学習を題材としたKaggleコンペの概説記事](https://zenn.dev/regonn/articles/kaggle-rl-competitions): コンペの具体例、評価方法、利用ライブラリを紹介した解説記事。
- [「MineRL Competition 2020」概要とPFRLベースライン実装の紹介記事](https://tech.preferred.jp/ja/blog/pfrl-baselines-for-the-minerl-competition/): Minecraft を題材にした強化学習コンペのベースライン実装。
- [Preferred Networksの深層強化学習ライブラリ「PFRL」の紹介記事](https://medium.com/pytorch/pfrl-a-pytorch-based-deep-rl-library-22cd048cf49c): 再現性を重視したライブラリの特徴をコードと共に紹介。
- [「Halite」AIコンペからの知見まとめ記事（2018年）](https://www.twosigma.com/insights/article/best-practices-from-building-a-machine-learning-bot-for-halite/): ルールベースと強化学習の比較など、実務的な設計指針をまとめた記事。
- [強化学習のデバッグ方法チェックリスト記事](https://higepon.hatenablog.com/entry/2020/07/13/193620): 強化学習の実装やコンペで役立つデバッグ手順をまとめたチェックリスト。

## 関連概念

- [AI エージェント活用](./ai-agent.md) / [性能評価と検証](./evaluation-validation.md) / [数理最適化コンペ](./optimization.md) / [コンペ形式・技術動向の変遷](./competition-evolution.md)
