# 話題別 Wiki

Kaggle に関する話題を横断的に整理した概念ページの一覧です。
各ページは複数の資料から得られる知見を統合したもので、LLM が [CLAUDE.md](https://github.com/upura/everyday-kaggle-news/blob/main/CLAUDE.md) の規約に従って維持しています。
網羅的なリンク一覧は[話題別一覧](../materials.md)などの各一覧ページを参照してください。

## 概念ページ

| ページ | 概要 | 関連 |
| --- | --- | --- |
| [表データコンペ](./concepts/tabular.md) | GBDT・特徴量エンジニアリング・Polars・表向け NN | 時系列 / 評価・検証 / 実験管理 |
| [画像認識コンペ](./concepts/image-recognition.md) | バックボーン選択・公開モデルの活用と高速化 | 音声 / NLP・LLM / 実験管理 |
| [自然言語処理・LLM コンペ](./concepts/nlp-llm.md) | BERT 系 fine-tuning の定跡と LLM 活用・推論高速化 | AI エージェント / コードコンペ / 画像 |
| [時系列予測コンペ](./concepts/time-series.md) | 時間分割バリデーション・損失設計・時系列基盤モデル | 表 / 評価・検証 |
| [音声・音響コンペ](./concepts/audio.md) | メルスペクトログラム化と画像モデル適用・異常音検知 | 画像 / NLP・LLM |
| [数理最適化・ヒューリスティック](./concepts/optimization.md) | Santa 系コンペ・AtCoder ヒューリスティックとの親和性 | 表 / コードコンペ |
| [コードコンペティション](./concepts/code-competition.md) | 提出形式の制約と作業フロー・提出自動化 | 実験管理 / NLP・LLM |
| [実験管理](./concepts/experiment-management.md) | 試行回数の最大化・再現性・チームでの体制づくり | コードコンペ / AI エージェント |
| [AI エージェント活用](./concepts/ai-agent.md) | LLM エージェントによるコンペ作業の自動化と限界 | NLP・LLM / 実験管理 |
| [性能評価・検証](./concepts/evaluation-validation.md) | リーク防止・バリデーション設計・データセット品質 | 時系列 / 表 / 実験管理 |

## Query ページ

質問と回答を資産化したページです。まだありません。

## 運用

- 更新履歴は [log.md](./log.md) を参照
- 新しい URL の取り込み(ingest)・質問(query)・整合性チェック(lint)の手順はリポジトリの CLAUDE.md と `.claude/skills/` に定義
