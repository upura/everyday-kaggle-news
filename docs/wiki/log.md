# 操作ログ

LLM Wiki としての操作履歴です(新しいものが上)。

- 2026-07-10 restructure: materials.md の目次を単一の話題分類に統合(「用途別一覧」セクションを解消し、一覧ページ 8 本を「学び方」「情報収集・コミュニティ」「データ種別・タスク」の各見出しに配置)。README 冒頭に Kaggler Ja Wiki と比べた特徴(LLM Wiki 運用、Weekly Kaggle News がソース、PR レビューでの反映)を追記し、サイト案内を目次中心に一本化
- 2026-07-10 restructure: 管理境界を変更し用途別一覧ページ 8 本を LLM 管理に移行(CLAUDE.md)。materials.md を「目次」としてサイト全体の入口に再定義し用途別一覧セクションを追加。README のサイト案内を話題別 Wiki 中心に再構成
- 2026-07-10 lint: 概念ページ改名(入門者向け / 自然言語処理コンペ / 音声コンペ / 数理最適化コンペ / 性能評価と検証)に合わせて materials.md の目次と参照ラベルを同期。CLAUDE.md の data-datatype タクソノミーを solutions.md のフィルタ UI と一致する 9 値に修正。相対リンク・孤立ページ・目次同期・solutions.md 形式・URL 重複の検査はすべて問題なし
- 2026-07-10 restructure: 話題別 Wiki と話題別一覧を統合(1 話題 1 ページ化)。概念ページ 8 本を新設(getting-started / pytorch / graph / recommendation / mindset / environment / academic-competition / competition-hosting)し全リンクを概念ページに集約、materials.md を目次化、wiki/index.md を廃止。Weekly Kaggle News 周年記事は recent.md へ移設
- 2026-07-10 fix: ho.lc の URL 形式変更(アンダースコア→ハイフン)に伴うリンク切れを修正(materials.md / solutions.md / milestones.md / service.md / concepts/code-competition.md / concepts/evaluation-validation.md)
- 2026-07-10 ingest: https://research.google/blog/introducing-tabfm-a-zero-shot-foundation-model-for-tabular-data/ → materials.md(表)、concepts/tabular.md
- 2026-07-10 seed: 概念ページ 10 本(tabular / image-recognition / nlp-llm / time-series / audio / optimization / code-competition / experiment-management / ai-agent / evaluation-validation)と index.md を初期構築
