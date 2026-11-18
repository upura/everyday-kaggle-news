# AI エージェント活用

Claude Code などの LLM エージェントを道具としてコンペ作業に活用する手法をまとめます。
ベースライン構築や過去解法の調査を自動化できる一方、上位入賞には人間による問題定義や改善方針の判断が求められます。
エージェント自体を提出して競わせる形式は[エージェント対戦コンペ](./agent-competition.md)を参照してください。

## 押さえどころ

- 2023 年の ChatGPT Code Interpreter による初期の挑戦は惨敗に終わったものの、2025 年には Claude Code 主体で上位 30% に到達する事例が登場し、エージェント支援の実用性が急速に高まった（[Code Interpreter での挑戦](https://zenn.dev/karaage0703/articles/1fa0a14d4cdd63)、[Claude Code での上位 30% 事例](https://zenn.dev/genda_jp/articles/20250909_kaggle_with_claude_code)）。
- 2025 年の年次レポートでも完全自律のエージェントによる単独上位入賞は未報告だが、人間との協働による金メダル獲得事例は国内でも複数出ている（[The State of Machine Learning Competitions 2025](https://mlcontests.com/state-of-machine-learning-competitions-2025/)）。
- ベースライン作成が効率化された結果、人間の役割は「何がスコアを左右するか」の見極め、CV（交差検証）設計やリーク検知の妥当性検証、改善方針の決定へ移っている（[コーディングエージェント時代の Kaggle](https://note.com/currypurin/n/n93de6df91535)）。
- 「方針決定と採否の判定は人間、実装と確認はエージェント」という役割分担が定着しつつある（[AI エージェント時代の取り組み方](https://speakerdeck.com/takanao/ai-ejento-jidai-kaggle-ni-dou-torikumu-ka)）。
- 実験結果をリポジトリと指示ファイルに集約すればコンテキスト切れの後も引き継げるため、ローカル GPU 1 枚とスマートフォンからの指示だけで金メダルを獲得した事例もある（[生成 AI にどこまで任せられるか](https://speakerdeck.com/k951286/ima-seisei-ai-ni-kaggle-o-doko-made-makaserareru-ka-rogii-konpe-deno-susumekata-to-tips)）。
- エージェントへの依存度が高まるほど、有望な仮説の早すぎる棄却や探索の行き詰まりを防ぐ人間の判定基準が重要になり、肥大化した構成を定期的に簡潔へ戻す整理も欠かせない。
- Claude Code のほか Cursor、Manus AI、Cline、Devin などの比較検証や、過去コンペの上位解法を調査・要約させる用途、skills / agents 設定の共有も進んでいる。
- エージェントとの協働には実験の再現性と記録が前提になる（[実験管理](./experiment-management.md)）。エージェントの自律性を測る MLE-Bench やノートブックのクラッシュを集めた JunoBench など、評価基盤の整備も進んでいる。
- エージェントそのものを提出・評価するコンペは[エージェント対戦コンペ](./agent-competition.md)を参照。

## 資料

### ツール活用・協働の設計

- [AIエージェント時代、Kaggleにどう取り組むか](https://speakerdeck.com/takanao/ai-ejento-jidai-kaggle-ni-dou-torikumu-ka): AI エージェント時代の Kaggle への取り組み方について、人間とツールの役割分担などの指針を整理した発表資料。
- [コーディングエージェント時代のKaggle──人間の役割がより本質へ](https://note.com/currypurin/n/n93de6df91535): 実装の壁が下がったぶん人間の仕事が前段に移ったと論じる記事。学習コードの作成、EDA、実験実行と結果のレポート化は任せ、次にどの実験を優先するかは自分で決める、という役割分担を具体例で述べている。
- [Agent時代のKaggleで、人間は何を見るべきか (関西kaggler会 2026.5.22)](https://speakerdeck.com/chihironakayama/agentshi-dai-nokagglede-ren-jian-hahe-wojian-rubekika-guan-xi-kagglerhui-2026-dot-5-22): エージェントによるコーディングが普及した時代の Kaggle の変化と人間の役割を論じる発表資料。
- [Claude Codeはどこまで戦えるのか？Kaggle金メダルで見えた現在地](https://speakerdeck.com/chihironakayama/claude-codehadokomadezhan-erunoka-kagglejin-medarudejian-etaxian-zai-di): Claude Code を用いたコンペ参加録。金メダル獲得までの活用実態を紹介する LT 資料。
- [Claude Code と Kaggle をやったら何も考えずに上位30%になれた話](https://zenn.dev/genda_jp/articles/20250909_kaggle_with_claude_code): エージェントに任せた場合の到達点と限界、MLflow や GitHub を使った協働体制の実験報告。
- [Winning a Kaggle Competition with Generative AI–Assisted Coding](https://developer.nvidia.com/blog/winning-a-kaggle-competition-with-generative-ai-assisted-coding/): Kaggle Grandmaster の Chris Deotte 氏による、テーブルコンペでの AI 支援コーディングの活用事例。
- [【Claude Code】Kaggle上位勢が設定するClaude Codeのskillsとagentsをチェックする](https://zenn.dev/nakakiiro/articles/kaggle_claude_code_boilerplate): 公開されている Kaggler 3 人の Claude Code 構成（skills / agents）を比較し解説した記事。
- [Kaggle過去コンペ上位解法をAIエージェントでレポートする](https://speakerdeck.com/kuto5046/kaggleguo-qu-konpeshang-wei-jie-fa-woaiezientoderepotosuru): 過去コンペの上位解法を AI エージェントに調査・要約させるアプローチの紹介資料。
- [NVIDIA Kaggle Plugin](https://github.com/NVIDIA/nvidia-kaggle): Kaggle の公開解法を収集するコーディングエージェント向けプラグイン。過去解法サーベイの自動化に使える。
- [AIコーディングツール実践比較：Kaggleタスクで見えたClaude Code・Manus AI・Cline・Devinの最適な活用場面](https://zenn.dev/mkj/articles/fbb48ba58c77a1): Kaggle コンペを題材に 4 つの AI コーディングツールを比較検証した記事。
- [AI搭載エディタCursorの紹介と機械学習コンペでの使用レビュー](https://speakerdeck.com/k951286/aida-zai-eteitacursornoshao-jie-toji-jie-xue-xi-konhetenoshi-yong-rehiyu): AI 支援エディタ Cursor の機能紹介とコンペでの使用レビュー。

### 評価ベンチマーク・初期事例

- [KaggleはAIに解けるか？ MLE-Benchのいま (2025/08/23; 第4回 関東Kaggler会)](https://speakerdeck.com/iwiwi/23-di-4hui-guan-dong-kagglerhui): Kaggle の問題を AI エージェントに解かせるベンチマーク MLE-Bench の動向をまとめた発表資料。
- [MLE-Benchの論文とコードを読んで](https://ho.lc/blog/openai-mle-bench/): MLE-bench の論文とコードを Kaggle 参加者の視点で読み解いた考察記事。
- [JunoBench: Crashes in Python ML Jupyter Notebooks](https://arxiv.org/abs/2510.18013v1): Kaggle 由来の再現可能なノートブックのクラッシュ 111 件を集めたベンチマークの論文。
- [データコンペでCode Interpreter片手に戦ってみたけど惨敗でした](https://zenn.dev/karaage0703/articles/1fa0a14d4cdd63): ChatGPT の Code Interpreter でコミュニティコンペに挑んだ 2023 年の初期事例。

## 関連概念

- [エージェント対戦コンペ](./agent-competition.md) / [自然言語処理コンペ](./nlp-llm.md) / [実験管理](./experiment-management.md) / [サービス・ツール](../../service.md) / [コンペ形式・技術動向の変遷](./competition-evolution.md)
