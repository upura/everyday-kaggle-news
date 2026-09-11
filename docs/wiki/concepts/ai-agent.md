# AI エージェント活用

Claude Code などの LLM エージェントを「道具」としてコンペ作業に使う潮流です。
ベースライン構築や過去解法の調査は自動化が進む一方、上位に食い込むには人間による問題定義とモデル改善がまだ必要とされています。
エージェント自体を提出して競わせる形式は[エージェント対戦コンペ](./agent-competition.md)を参照してください。

## 押さえどころ

- 2023 年時点では ChatGPT の Code Interpreter でコミュニティコンペに挑んで「惨敗」した事例が報告されていたが、2025 年には Claude Code 主体で「上位 30% 程度」まで到達する事例が出ており、エージェント支援の実用性は短期間で急速に向上している（[データコンペでCode Interpreter片手に戦ってみたけど惨敗でした](https://zenn.dev/karaage0703/articles/1fa0a14d4cdd63)、[Claude Code と Kaggle をやったら何も考えずに上位30%になれた話](https://zenn.dev/genda_jp/articles/20250909_kaggle_with_claude_code)）
- とはいえメダル圏にはまだ届かず、人間の役割はデータ整備、問題定義、モデル改善へシフトする。実装が容易になったことでベースラインまでの距離は縮まり、勝負どころは「このコンペは何で決まるのか」を見抜く判断、エージェントの書いたコードの妥当性を検証できる CV 設計と評価指標の理解、分布差やリーク・時系列特性を読んで次の方向を決めるデータ解釈に移る（[コーディングエージェント時代のKaggle](https://note.com/currypurin/n/n93de6df91535)）
- 2025 年時点の年次レポートでも、完全自律のエージェントが上位入賞した事例はまだ報告されていない（[The State of Machine Learning Competitions 2025](https://mlcontests.com/state-of-machine-learning-competitions-2025/)）。一方、人間とエージェントの協働による金メダル事例は国内でも複数出ている
- Claude Code のほか Cursor・Manus AI・Cline・Devin など複数の AI コーディングツールが使われ始めており、用途に応じた比較検証が進んでいる
- 過去コンペの上位解法を調査してレポートさせる使い方は、コンペ序盤のサーベイを大きく効率化する。skills・agents の構成をコミュニティで共有・比較する動きも出てきている
- 協働の質を決めるのは分担の切り方で、「方針決定と採否の判定は人、実装と確認はエージェント」という線引きが繰り返し語られる。実験結果をリポジトリと指示ファイルに集約しておけばセッションが切れても引き継げるため、ローカル GPU 1 枚・スマホからの短い指示だけで金メダルに届いた事例もある（[いま、生成AIにKaggleをどこまで 任せられるか](https://speakerdeck.com/k951286/ima-seisei-ai-ni-kaggle-o-doko-made-makaserareru-ka-rogii-konpe-deno-susumekata-to-tips)）
- 委譲するほど、人が握る「判定基準」の設計が効いてくる。実験の足切り基準を誤ると有望な案を序盤で捨ててしまい、リークや行き詰まりはエージェント自身では検知できない。実装が速い分だけ構成が複雑になりやすく、定期的に単純な設計へ戻す見直しも要る
- エージェントと協働するには、実験の再現性と記録が前提になる（[実験管理](./experiment-management.md)）。ノートブックのクラッシュを集めたベンチマーク（JunoBench）や MLE-Bench など、エージェントの評価基盤も整備されつつある
- 「エージェントを道具として使う」話題の隣で、データ分析エージェントそのものを競わせるコンペも立ち上がっている。KDD Cup 2026 の「[Data Agents for Complex Data Analysis](https://dataagent.top/)」は、異種データの束と自然言語の問いからエージェントに分析の段取りを組ませる形式で、スコアだけを競うトラックとシステムの完成度・新規性を評価するトラックを併設している。単一スコアで測りにくい対象をどう評価するかという論点は[性能評価と検証](./evaluation-validation.md)と地続き

## 資料

- [Claude Code と Kaggle をやったら何も考えずに上位30%になれた話](https://zenn.dev/genda_jp/articles/20250909_kaggle_with_claude_code): エージェントに任せた場合の到達点と限界、MLflow・GitHub を使った協働体制の実験報告。
- [Winning a Kaggle Competition with Generative AI–Assisted Coding](https://developer.nvidia.com/blog/winning-a-kaggle-competition-with-generative-ai-assisted-coding/): Kaggle Grandmaster の Chris Deotte さんによる、テーブルコンペでの AI 支援コーディングの活用事例。
- [Kaggle過去コンペ上位解法をAIエージェントでレポートする](https://speakerdeck.com/kuto5046/kaggleguo-qu-konpeshang-wei-jie-fa-woaiezientoderepotosuru)
- [NVIDIA Kaggle Plugin](https://github.com/NVIDIA/nvidia-kaggle): Kaggle の公開解法を収集するコーディングエージェント向けプラグイン。過去解法サーベイの自動化に使える。
- [コーディングエージェント時代のKaggle──人間の役割がより本質へ](https://note.com/currypurin/n/n93de6df91535): 実装の壁が下がったぶん人間の仕事が前段に移ったと論じる記事。学習コード・EDA・実験の実行と結果のレポート化は任せ、次にどの実験を優先するかは自分で決める、という線引きを具体例で述べている。
- [Agent時代のKaggleで、人間は何を見るべきか (関西kaggler会 2026.5.22)](https://speakerdeck.com/chihironakayama/agentshi-dai-nokagglede-ren-jian-hahe-wojian-rubekika-guan-xi-kagglerhui-2026-dot-5-22): エージェントによるコーディングが普及した時代の Kaggle の変化と人間の役割を論じる発表資料。
- [Claude Codeはどこまで戦えるのか？Kaggle金メダルで見えた現在地](https://speakerdeck.com/chihironakayama/claude-codehadokomadezhan-erunoka-kagglejin-medarudejian-etaxian-zai-di): Claude Code を用いたコンペ参加録。金メダル獲得までの活用実態を紹介する LT 資料。
- [【Claude Code】Kaggle上位勢が設定するClaude Codeのskillsとagentsをチェックする](https://zenn.dev/nakakiiro/articles/kaggle_claude_code_boilerplate): 公開されている Kaggler 3 人の Claude Code 構成（skills / agents）を比較・解説する記事。
- [AI搭載エディタCursorの紹介と機械学習コンペでの使用レビュー](https://speakerdeck.com/k951286/aida-zai-eteitacursornoshao-jie-toji-jie-xue-xi-konhetenoshi-yong-rehiyu): AI 支援エディタ Cursor の機能紹介とコンペでの使用レビュー。
- [データコンペでCode Interpreter片手に戦ってみたけど惨敗でした](https://zenn.dev/karaage0703/articles/1fa0a14d4cdd63): ChatGPT の Code Interpreter でコミュニティコンペに挑んだ 2023 年の初期事例。
- [AIコーディングツール実践比較：Kaggleタスクで見えたClaude Code・Manus AI・Cline・Devinの最適な活用場面](https://zenn.dev/mkj/articles/fbb48ba58c77a1): Kaggle コンペを題材に 4 つの AI コーディングツールを比較検証した記事。
- [KaggleはAIに解けるか？ MLE-Benchのいま (2025/08/23; 第4回 関東Kaggler会)](https://speakerdeck.com/iwiwi/23-di-4hui-guan-dong-kagglerhui): Kaggle の問題を AI エージェントに解かせるベンチマーク MLE-Bench の動向をまとめた発表資料。
- [MLE-Benchの論文とコードを読んで](https://ho.lc/blog/openai-mle-bench/): MLE-bench の論文とコードを Kaggle 参加者の視点で読み解いた考察記事。
- [JunoBench: Crashes in Python ML Jupyter Notebooks](https://arxiv.org/abs/2510.18013v1): Kaggle 由来の再現可能なノートブックのクラッシュ 111 件を集めたベンチマークの論文。
- [KDD Cup 2026: Data Agents for Complex Data Analysis](https://dataagent.top/): 表・文書・ログ・API・知識グラフが混在するデータ束と自然言語の問いを渡し、分析の段取りを自律的に組み立てさせる KDD Cup の公式サイト。評価は DataAgent-Bench のタスク群で行い、順位を競う Leaderboard Track とシステムの完成度・新規性を評価する Creative Track の 2 本立てになっている。
- [KDD Cup 2026 Data Agents: Presentation Archive](https://dataagent.top/presentations): 上記コンペの最終順位と上位チームのシステム・発表資料を公開するアーカイブ。

## 関連概念

- [エージェント対戦コンペ](./agent-competition.md) / [自然言語処理コンペ](./nlp-llm.md) / [実験管理](./experiment-management.md) / [サービス・ツール](../../service.md) / [コンペ形式・技術動向の変遷](./competition-evolution.md)
