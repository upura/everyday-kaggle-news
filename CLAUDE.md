# Everyday Kaggle News — LLM Wiki スキーマ定義

本リポジトリは、Kaggle に関する非公式リンク集を LLM Wiki(LLM が要約・概念ページ・相互リンクを持続的に維持する知識ベース)として運用します。
このファイルは人間(管理者)が管理するスキーマ層で、ページ種別・形式・オペレーションの規約を定義します。

## 3 層構造

| 層 | 対応 | 管理者 |
| --- | --- | --- |
| Raw sources | 外部 URL(記事・スライド・動画・論文)。リポジトリには保存しない | 人間が投入 |
| Wiki | `docs/wiki/` 配下の概念ページ・Query ページ・index・log、既存一覧ページのリンク注釈 | LLM |
| Schema | `CLAUDE.md` と `.claude/skills/`(ingest / query / lint) | 人間 |

## ページ種別と管理境界

### 人間が管理(構成の変更は管理者判断)

- `README.md` / `CONTRIBUTING.md` / `LICENSE`
- `docs/` 直下の一覧ページ 9 本: quickstart / recent / solutions / milestones / books / events / service / platform / materials

### LLM が管理(オペレーションを通じて更新)

- `docs/wiki/index.md` — 概念ページのカタログと関連(隣接)一覧
- `docs/wiki/log.md` — 操作ログ(新しいものを上に追記)
- `docs/wiki/concepts/*.md` — 概念ページ(話題横断の統合知識)
- `docs/wiki/queries/*.md` — Q&A ページ(質問と回答の資産化)
- 既存一覧ページへのエントリ追記・注釈付与(ページ構成自体は変えない)

## エントリ形式

- 一覧ページ・概念ページの資料: `- [タイトル](URL): 1〜2 文の注釈`
  - 注釈は任意(段階的にバックフィル)。付ける場合は内容を確認した上で書く
- `docs/solutions.md` のコンペ参加録: 既存の `<div class="competition-entry" markdown="1" data-year data-datatype data-platform>` + `<h3>` + badge 形式を厳守
- `docs/books.md` / `docs/platform.md`: 既存の表形式を維持
- リンク: サイト内は相対 Markdown リンク(`./page.md`、`../materials.md` など)。wikilink `[[...]]` は Jekyll で動かないため使用しない

## 分類タクソノミー

- データ種別(solutions.md の `data-datatype`): `tabular` / `text` / `image` / `audio` / `3d` / `multimodal`
- プラットフォーム(`data-platform`): `kaggle` / `signate` / `probspace` / `nishika` / `atmacup` / `solafune` ほか
- 話題カテゴリ(materials.md の見出しに準拠): 入門者・初学者向け / PyTorch / 表 / 画像認識 / 自然言語処理 / 時系列予測 / 音声認識 / 数理最適化 / グラフ / 推薦 / コードコンペティション / 心構え / 実験管理 / 環境構築 / AI エージェント / 性能評価・検証 / 学会コンペ / コンペ開催

新カテゴリの追加は可能だが、既存カテゴリに収まらないか先に検討する。

## 概念ページの規約

- 場所: `docs/wiki/concepts/<kebab-case>.md`(例: `image-recognition.md`)
- テンプレート:

```markdown
# ページ名

(この話題の 2〜3 文の概説)

## 押さえどころ

(複数ソースを横断した気づき・定番の流れを箇条書きで統合)

## 資料

- [タイトル](URL): 1〜2 文の注釈

## 関連概念

- [ページ名](./page.md) / [一覧ページ名](../../materials.md)
```

- 「押さえどころ」は自分の言葉で書く。出典が特定の資料に依存する主張はその資料へリンクする
- 「資料」は主要なものを厳選して注釈付きで載せ、網羅は一覧ページに任せる
- 「関連概念」は必ず実在するページのみ。孤立ページ(どこからもリンクされないページ)を作らない
- 新規作成・改名時は `index.md` のカタログと隣接一覧を必ず更新する

## オペレーション

### Ingest(`/ingest <URL>`)

1. URL を WebFetch し内容を確認(タイトルだけで推測しない)
2. タクソノミーに従って話題を判定し、該当する一覧ページに既存形式でエントリ追加(重複確認必須)
3. 関連する概念ページの「資料」に追加。「押さえどころ」に反映すべき知見があれば統合。該当概念が無く資料が 3 件以上見込めるなら新規作成
4. `index.md` と `log.md` を更新
5. 変更したページの一覧を報告

### Query(`/query <質問>`)

1. `docs/wiki/` と既存一覧ページを根拠に回答(根拠ページへのリンクを付ける)
2. 再利用価値のある回答は `docs/wiki/queries/<kebab-case>.md` に保存し、index と log を更新

### Lint(`/lint`)

1. 外部リンク切れ検査(curl HEAD、レート制御付き)
2. URL 重複検出(全ページ横断)
3. solutions.md の div / badge 形式検査
4. 相対リンク切れ・孤立概念ページ検出
5. index.md と実ファイルの同期確認
6. 検出結果を報告。修正は管理者の確認後に行う

## 権利面の規約

- 注釈・概念ページは短いオリジナルの紹介文・自分の言葉での統合に限る。本文の転載・長文要約はしない
- 著作者・権利者から掲載を希望しない旨の連絡があった場合は速やかに削除する(CONTRIBUTING.md の方針に準拠)

## 運用サイクル(目安)

- 週次: Weekly Kaggle News 配信後、新規 URL を ingest
- 月次: lint 実行。既存リンクの注釈バックフィル(1 回あたり 1 ページ程度)
