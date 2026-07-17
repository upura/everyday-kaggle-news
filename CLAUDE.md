# Everyday Kaggle News — LLM Wiki スキーマ定義

本リポジトリは、Kaggle に関する非公式リンク集を LLM Wiki（LLM が要約・概念ページ・相互リンクを持続的に維持する知識ベース）として運用します。
このファイルは人間（管理者）が管理するスキーマ層で、ページ種別・形式・オペレーションの規約を定義します。

## 3 層構造

| 層 | 対応 | 管理者 |
| --- | --- | --- |
| Raw sources | 外部 URL（記事・スライド・動画・論文）。リポジトリには保存しない | 人間が投入 |
| Wiki | `docs/` 配下の全ページ（目次・概念ページ・Query ページ・一覧ページ・log） | LLM |
| Schema | `CLAUDE.md` と `.claude/skills/`（ingest / query / lint） | 人間 |

## ページ種別と管理境界

### 人間が管理（変更は管理者判断）

- `README.md` の「目次」「最近の更新」以外のセクション / `CONTRIBUTING.md` / `LICENSE`

### LLM が管理（オペレーションを通じて更新）

- `README.md` の「目次」セクション — サイト全体の入口。話題ごとの見出しの下に Wiki ページと一覧ページを混在させて案内する。概念ページの新設・改名時に目次行を追記・修正する
- `README.md` の「最近の更新」セクション — 直近 5 件程度のダイジェストを維持する
- `docs/wiki/log.md` — 操作ログ（新しいものを上に追記）
- `docs/wiki/concepts/*.md` — 概念ページ（話題ごとの統合知識と資料の全リスト）
- `docs/` 直下の一覧ページ 9 本: quickstart / recent / solutions / milestones / books / events / service / platform / calendar
  - エントリ追記・注釈付与は通常のオペレーションとして実施
  - 見出し・ページの分割統合などの構成変更も可能だが、9 ページの役割分担（分類）とエントリ形式は保ち、構成変更は log.md に `restructure` として記録する
  - calendar（コンペ開催カレンダー）は例外的にデータ駆動のページ: GitHub Actions の `update-competitions` が毎日生成する `docs/competitions.json` を表示する。エントリの手動追記や ingest の掲載先にはしない

## エントリ形式

- 一覧ページ・概念ページの資料: `- [タイトル](URL): 1〜2 文の注釈`
  - 注釈は任意（段階的にバックフィル）。付ける場合は内容を確認した上で書く
- `docs/solutions.md` のコンペ参加録: 既存の `<div class="competition-entry" markdown="1" data-year data-datatype data-platform>` + `<h3>` + badge 形式を厳守
- `docs/books.md` / `docs/platform.md`: 既存の表形式を維持
- リンク: サイト内は相対 Markdown リンク（`./page.md`、`../../README.md` など）。wikilink `[[...]]` は Jekyll で動かないため使用しない

## 分類タクソノミー

- データ種別（solutions.md の `data-datatype`）: `tabular` / `text` / `image` / `audio` / `timeseries` / `video` / `3d` / `multimodal` / `other`（フィルタ UI の選択肢と一致させる）
- プラットフォーム（`data-platform`）: `kaggle` / `signate` / `probspace` / `nishika` / `atmacup` / `solafune` ほか
- 話題カテゴリ: `README.md` の「目次」の見出しと行に準拠（概念ページは目次の行と 1 対 1 対応）

新しい話題は、まず既存の概念ページに収まらないか検討する。収まらず資料が 3 件以上見込めるなら概念ページを新設し、README.md の目次に追記する。

## 概念ページの規約

- 場所: `docs/wiki/concepts/<kebab-case>.md`（例: `image-recognition.md`）
- テンプレート:

```markdown
# ページ名

（この話題の 2〜3 文の概説）

## 押さえどころ

（複数ソースを横断した気づき・定番の流れを箇条書きで統合）

## 資料

- [タイトル](URL): 1〜2 文の注釈

## 関連概念

- [ページ名](./page.md) / [一覧ページ名](../../milestones.md)
```

- 「押さえどころ」は自分の言葉で書く。出典が特定の資料に依存する主張はその資料へリンクする
- 「資料」はその話題の資料を網羅的に掲載する（注釈は内容を確認したものから段階的に付与）
- 「資料」が 15 件を超えたら「入門・基礎」「コンペの定跡」「モデル・技術動向」などの小見出し（`###`）で整理する。30 件を超えたらサブトピックへの分割を検討する
- 「関連概念」は必ず実在するページのみ。孤立ページ（どこからもリンクされないページ）を作らない
- 新規作成・改名時は `README.md` の目次を必ず更新する

## オペレーション

### Ingest（`/ingest <URL>`）

1. URL を WebFetch し内容を確認（タイトルだけで推測しない）
2. 分類して掲載先を決める（重複確認必須）
   - コンペの解法・参加録 → `docs/solutions.md`（既存形式）
   - 書籍 → `docs/books.md`、イベント → `docs/events.md`、称号振り返り → `docs/milestones.md`、サービス・ツール → `docs/service.md`、プラットフォーム → `docs/platform.md`
   - 上記以外の技術記事・話題 → 該当する概念ページの「資料」（README.md の目次には直接エントリを置かない）
3. 概念ページの「押さえどころ」に反映すべき知見があれば統合。該当概念が無く資料が 3 件以上見込めるなら新規作成し、README.md の目次に追記
4. `log.md` を更新し、README.md の「最近の更新」を直近 5 件程度に維持する。変更したページの一覧を報告
5. Weekly Kaggle News の号 URL を受け取った場合は、号ページから紹介 URL を抽出し、各 URL に対して上記を実施する（log には号単位で記録）

### Query（`/query <質問>`）

1. `docs/wiki/` と既存一覧ページを根拠に回答（根拠ページへのリンクを付ける）。リポジトリ内に根拠が無い部分は「本リンク集には未掲載」と明示する

### Lint（`/lint`）

1. 外部リンク切れ検査（curl HEAD、レート制御付き）
2. URL 重複検出（全ページ横断）
3. solutions.md の div / badge 形式検査
4. 相対リンク切れ・孤立概念ページ検出
5. README.md の目次と `docs/wiki/concepts/` の実ファイルの同期確認
6. 検出結果を報告。修正は管理者の確認後に行う

## 文章規約

- 日本語の文中の括弧は全角（）を使う。対象は概説・押さえどころ・注釈・見出し・ログなどの地の文
- リンクタイトル（原題）・URL・コード・HTML・YAML は原文のままとし、変換しない
- そのほかの文体・整形は `.claude/skills/japanese-tech-writing/` の規範に従う

## 権利面の規約

- 注釈・概念ページは短いオリジナルの紹介文・自分の言葉での統合に限る。本文の転載・長文要約はしない
- 著作者・権利者から掲載を希望しない旨の連絡があった場合は速やかに削除する（CONTRIBUTING.md の方針に準拠）

## 運用サイクル（目安）

- 週次: Weekly Kaggle News 配信後、最新号を ingest（GitHub Actions の `weekly-ingest` が自動で PR を作成し、編集者のレビュー・マージで反映。手動 ingest も可）
- 月次: lint 実行（外部リンク切れは `monthly-linkcheck` ワークフローが Issue を起票）。既存リンクの注釈バックフィルは、lint が表示する注釈カバレッジの低いページから 1 回あたり 1 ページ程度
