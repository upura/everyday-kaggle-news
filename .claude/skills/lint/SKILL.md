---
name: lint
description: リンク集と wiki の整合性チェック。外部リンク切れ・URL 重複・solutions.md の形式・相対リンク切れ・孤立概念ページ・index の同期を検査して報告する。「lint して」「ヘルスチェックして」のような依頼で使う。
---

# Lint — 整合性チェック

リポジトリ全体の健全性を検査し、結果を報告する。**検出のみ行い、修正は管理者の確認後**。規約はルートの `CLAUDE.md` に従う。

自動化済みの部分: 内部整合性（`tools/verify_wiki.py`）は CI（`.github/workflows/lint.yml`）が PR・push ごとに実行する。外部リンク切れは月次の `.github/workflows/monthly-linkcheck.yml` が検査して Issue を起票する。手動で lint を依頼された場合も、まず両ツールを実行し、結果の解釈と修正提案に注力する。

## 検査項目

### 1. 外部リンク切れ

`python3 tools/check_external_links.py <report.md>` を実行する（全件で 5〜10 分）。

- HEAD が 405/403 を返すサイトは GET で再確認される
- x.com / linkedin.com / amazon 系はボット対策で誤判定しやすいため「要手動確認」として分けて報告される
- 404/410 のみ「リンク切れ」と断定する

### 2〜5. 内部整合性（`python3 tools/verify_wiki.py`）

以下をまとめて検査し、参考情報として注釈カバレッジ（ページ別の注釈付与率、低い順）も表示する。カバレッジは注釈バックフィルの優先度付けに使う。

### 2. URL 重複

全ページ横断で同一 URL の重複を検出する（末尾スラッシュ・`http/https` の揺れを正規化して比較）。次の 2 つは意図的な再掲なので対象外: （a） 概念ページの「押さえどころ」での引用と同ページ「資料」への掲載、（b） 概念ページと一覧ページの重複。報告するのは、一覧ページ同士の重複と、同一セクション内の重複のみ。

### 3. solutions.md の形式

- `<div class="competition-entry" markdown="1" ...>` に `data-year` / `data-datatype` / `data-platform` が揃っているか
- `data-datatype` が CLAUDE.md のタクソノミー（solutions.md のフィルタ UI の選択肢と同一）の値か
- div の開閉が対応しているか、badge の year と `data-year` が一致するか

### 4. 相対リンク・孤立ページ

- サイト内相対リンク（`./`, `../`）の参照先ファイルが実在するか
- `docs/wiki/concepts/` の各ページが README.md の目次または他ページからリンクされているか（孤立検出）
- 「関連概念」のリンク先が実在するか

### 5. 目次の同期

`README.md` の目次と `docs/wiki/concepts/` の実ファイルが一致するか。

## 報告形式

検査項目ごとに「問題なし」または問題の一覧（ファイル・行・内容）を報告し、最後に修正の提案をまとめる。実施後 `docs/wiki/log.md` に追記する: `- YYYY-MM-DD lint: 検出 N 件(内訳)`
