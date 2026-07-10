# 操作ログ

LLM Wiki としての操作履歴です(新しいものが上)。

- 2026-07-11 restructure: 最新動向の調査(mlcontests 年次レポート、Kaggle Game Arena 公式発表)を踏まえ、概念ページ「エージェント対戦コンペ」(agent-competition)を新設。ai-agent を「道具としての活用」に位置づけ直し、evaluation-validation に Kaggle のベンチマーク基盤化、nlp-llm に 2025 年のデコーダ型 LLM への移行・テスト時学習の潮流を追記
- 2026-07-11 ingest: WKN #315 → 新規 1 件(concepts/mindset)。他 4 件は既掲載
- 2026-07-11 ingest: WKN #316 → 新規 3 件(concepts/optimization, image-recognition, tabular)
- 2026-07-11 ingest: WKN #317 → 新規 3 件(events.md / concepts/tabular, nlp-llm)
- 2026-07-11 ingest: WKN #318 → 新規 0 件(3 件すべて既掲載)
- 2026-07-11 ingest: WKN #319 → 新規 0 件(4 件すべて既掲載)
- 2026-07-11 ingest: WKN #320 → 新規 4 件(solutions.md ×3 / concepts/environment, experiment-management)
- 2026-07-11 ingest: WKN #321 → 新規 4 件(solutions.md / events.md / concepts/competition-hosting, experiment-management)
- 2026-07-11 ingest: WKN #322 → 新規 2 件(solutions.md / events.md)
- 2026-07-11 ingest: WKN #323 → 新規 2 件(solutions.md)
- 2026-07-11 ingest: WKN #324 → 新規 7 件(solutions.md ×4 / platform.md / concepts/optimization, academic-competition, competition-hosting)。解法動画公開のニュース 2 件はスキップ
- 2026-07-10 ingest: WKN #325 → 新規 5 件(solutions.md / events.md / concepts/mindset, nlp-llm, academic-competition)
- 2026-07-10 ingest: WKN #326 → 新規 2 件(milestones.md)
- 2026-07-10 ingest: WKN #327 → 新規 1 件(solutions.md、concepts/ai-agent にも掲載)
- 2026-07-10 ingest: WKN #328 → 新規 6 件(solutions.md ×2 / events.md / concepts/environment, ai-agent, academic-competition)
- 2026-07-10 ingest: WKN #329 → 新規 4 件(solutions.md ×2 / milestones.md / concepts/time-series)。Nishika のコンペサービス終了を platform.md に反映
- 2026-07-10 ingest: WKN #330 → 新規 2 件(solutions.md / events.md)
- 2026-07-10 ingest: WKN #331 → 新規 3 件(events.md / concepts/ai-agent, academic-competition)
- 2026-07-10 ingest: WKN #332 → 新規 2 件(events.md / concepts/competition-hosting)。開催中コンペの告知 1 件はスキップ
- 2026-07-10 ingest: WKN #333 → 新規 1 件(concepts/ai-agent)。終了済み講座の告知 1 件はスキップ
- 2026-07-10 ingest: WKN #334 → 新規 1 件(solutions.md)。行政事業の告知 1 件は時限性のためスキップ
- 2026-07-10 ingest: WKN #335 → 新規 2 件(events.md / concepts/image-recognition)
- 2026-07-10 ingest: WKN #336 → 新規 3 件(solutions.md / concepts/ai-agent, mindset)
- 2026-07-10 ingest: WKN #337 → 新規 4 件(solutions.md ×2 / concepts/image-recognition, mindset)
- 2026-07-10 ingest: WKN #338 → 新規 2 件(solutions.md / events.md)
- 2026-07-10 ingest: WKN #339 → 新規 3 件(solutions.md「Kaggle 公式」/ concepts/nlp-llm, mindset)
- 2026-07-10 ingest: WKN #340 → 新規 2 件(solutions.md / events.md)。学生コンペの開催告知 1 件は時限性のためスキップ
- 2026-07-10 ingest: WKN #341 → 新規 1 件(concepts/nlp-llm)。ハッカソン支援・コンペ開催の告知 2 件は時限性のためスキップ
- 2026-07-10 ingest: WKN #342 → 新規 8 件(solutions.md / books.md / events.md / quickstart.md / service.md / concepts: competition-hosting, audio, academic-competition, mindset, ai-agent)。TabFM は既掲載のためスキップ

- 2026-07-10 restructure: 概念ページ getting-started を quickstart.md(入門者・初学者向けガイド)に統合し削除(定番資料を「定番資料」セクションとして移設)。Q&A(Query ページの資産化機構)を廃止し、materials.md・CLAUDE.md・query / lint スキルから関連記述を除去

- 2026-07-10 restructure: materials.md の目次を単一の話題分類に統合(「用途別一覧」セクションを解消し、一覧ページ 8 本を「学び方」「情報収集・コミュニティ」「データ種別・タスク」の各見出しに配置)。README 冒頭に Kaggler Ja Wiki と比べた特徴(LLM Wiki 運用、Weekly Kaggle News がソース、PR レビューでの反映)を追記し、サイト案内を目次中心に一本化
- 2026-07-10 restructure: 管理境界を変更し用途別一覧ページ 8 本を LLM 管理に移行(CLAUDE.md)。materials.md を「目次」としてサイト全体の入口に再定義し用途別一覧セクションを追加。README のサイト案内を話題別 Wiki 中心に再構成
- 2026-07-10 lint: 概念ページ改名(入門者向け / 自然言語処理コンペ / 音声コンペ / 数理最適化コンペ / 性能評価と検証)に合わせて materials.md の目次と参照ラベルを同期。CLAUDE.md の data-datatype タクソノミーを solutions.md のフィルタ UI と一致する 9 値に修正。相対リンク・孤立ページ・目次同期・solutions.md 形式・URL 重複の検査はすべて問題なし
- 2026-07-10 restructure: 話題別 Wiki と話題別一覧を統合(1 話題 1 ページ化)。概念ページ 8 本を新設(getting-started / pytorch / graph / recommendation / mindset / environment / academic-competition / competition-hosting)し全リンクを概念ページに集約、materials.md を目次化、wiki/index.md を廃止。Weekly Kaggle News 周年記事は recent.md へ移設
- 2026-07-10 fix: ho.lc の URL 形式変更(アンダースコア→ハイフン)に伴うリンク切れを修正(materials.md / solutions.md / milestones.md / service.md / concepts/code-competition.md / concepts/evaluation-validation.md)
- 2026-07-10 ingest: https://research.google/blog/introducing-tabfm-a-zero-shot-foundation-model-for-tabular-data/ → materials.md(表)、concepts/tabular.md
- 2026-07-10 seed: 概念ページ 10 本(tabular / image-recognition / nlp-llm / time-series / audio / optimization / code-competition / experiment-management / ai-agent / evaluation-validation)と index.md を初期構築
