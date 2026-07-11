# AI エージェント活用

Claude Code などの LLM エージェントを「道具」としてコンペ作業に使う潮流です。
ベースライン構築や過去解法の調査は自動化が進む一方、上位に食い込むには人間による問題定義とモデル改善がまだ必要とされています。
エージェント自体を提出して競わせる形式は[エージェント対戦コンペ](./agent-competition.md)を参照してください。

## 押さえどころ

- エージェント任せでも「上位 30% 程度」のモデルは作れるが、メダル圏には届かない。人間の役割はデータ整備、問題定義、モデル改善へシフトする（[Claude Code と Kaggle をやったら何も考えずに上位30%になれた話](https://zenn.dev/genda_jp/articles/20250909_kaggle_with_claude_code)）
- 2025 年時点の年次レポートでも、完全自律のエージェントが上位入賞した事例はまだ報告されていない（[The State of Machine Learning Competitions 2025](https://mlcontests.com/state-of-machine-learning-competitions-2025/)）。一方、人間とエージェントの協働による金メダル事例は国内でも複数出ている
- 過去コンペの上位解法を調査してレポートさせる使い方は、コンペ序盤のサーベイを大きく効率化する
- エージェントと協働するには、実験の再現性と記録が前提になる（[実験管理](./experiment-management.md)）
- ノートブックのクラッシュを集めたベンチマーク（JunoBench）など、エージェントの評価基盤も整備されつつある

## 資料

- [Claude Code と Kaggle をやったら何も考えずに上位30%になれた話](https://zenn.dev/genda_jp/articles/20250909_kaggle_with_claude_code): エージェントに任せた場合の到達点と限界、MLflow・GitHub を使った協働体制の実験報告。
- [Winning a Kaggle Competition with Generative AI–Assisted Coding](https://developer.nvidia.com/blog/winning-a-kaggle-competition-with-generative-ai-assisted-coding/): Kaggle Grandmaster の Chris Deotte さんによる、テーブルコンペでの AI 支援コーディングの活用事例。
- [Kaggle過去コンペ上位解法をAIエージェントでレポートする](https://speakerdeck.com/kuto5046/kaggleguo-qu-konpeshang-wei-jie-fa-woaiezientoderepotosuru)
- [NVIDIA Kaggle Plugin](https://github.com/NVIDIA/nvidia-kaggle): Kaggle の公開解法を収集するコーディングエージェント向けプラグイン。過去解法サーベイの自動化に使える。
- [Agent時代のKaggleで、人間は何を見るべきか (関西kaggler会 2026.5.22)](https://speakerdeck.com/chihironakayama/agentshi-dai-nokagglede-ren-jian-hahe-wojian-rubekika-guan-xi-kagglerhui-2026-dot-5-22): エージェントによるコーディングが普及した時代の Kaggle の変化と人間の役割を論じる発表資料。
- [Claude Codeはどこまで戦えるのか？Kaggle金メダルで見えた現在地](https://speakerdeck.com/chihironakayama/claude-codehadokomadezhan-erunoka-kagglejin-medarudejian-etaxian-zai-di): Claude Code を用いたコンペ参加録。金メダル獲得までの活用実態を紹介する LT 資料。
- [【Claude Code】Kaggle上位勢が設定するClaude Codeのskillsとagentsをチェックする](https://zenn.dev/nakakiiro/articles/kaggle_claude_code_boilerplate): 公開されている Kaggler 3 人の Claude Code 構成（skills / agents）を比較・解説する記事。
- [Claude Code / CodexでKaggle金メダルを取った話](https://zenn.dev/chiman/articles/b233cc808d6af3): 画像コンペでの金メダル獲得者による、AI と人間の役割分担を含む生成 AI 活用開発の紹介。
- [AIコーディングツール実践比較：Kaggleタスクで見えたClaude Code・Manus AI・Cline・Devinの最適な活用場面](https://zenn.dev/mkj/articles/fbb48ba58c77a1): Kaggle コンペを題材に 4 つの AI コーディングツールを比較検証した記事。
- [KaggleはAIに解けるか？ MLE-Benchのいま (2025/08/23; 第4回 関東Kaggler会)](https://speakerdeck.com/iwiwi/23-di-4hui-guan-dong-kagglerhui): Kaggle の問題を AI エージェントに解かせるベンチマーク MLE-Bench の動向をまとめた発表資料。
- [JunoBench: Crashes in Python ML Jupyter Notebooks](https://arxiv.org/abs/2510.18013v1): Kaggle 由来の再現可能なノートブックのクラッシュ 111 件を集めたベンチマークの論文。

## 関連概念

- [エージェント対戦コンペ](./agent-competition.md) / [自然言語処理コンペ](./nlp-llm.md) / [実験管理](./experiment-management.md)
