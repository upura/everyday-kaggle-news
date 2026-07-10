---
name: lint
description: リンク集と wiki の整合性チェック。外部リンク切れ・URL 重複・solutions.md の形式・相対リンク切れ・孤立概念ページ・index の同期を検査して報告する。「lint して」「ヘルスチェックして」のような依頼で使う。
---

# Lint — 整合性チェック

リポジトリ全体の健全性を検査し、結果を報告する。**検出のみ行い、修正は管理者の確認後**。規約はルートの `CLAUDE.md` に従う。

## 検査項目

### 1. 外部リンク切れ

`docs/` 配下の全 `http(s)` リンクを抽出し、curl で確認する。レート制御(1 件あたり 1 秒程度の間隔)を入れ、User-Agent を設定する。

```bash
curl -s -o /dev/null -w "%{http_code}" -I -L --max-time 10 -A "Mozilla/5.0" "<URL>"
```

- HEAD が 405/403 を返すサイトは GET で再確認してから判定する
- x.com / linkedin.com / amazon 系はボット対策で誤判定しやすいため「要手動確認」として分けて報告する
- 404/410 のみ「リンク切れ」と断定する

### 2. URL 重複

全ページ横断で同一 URL の重複を検出する(末尾スラッシュ・`http/https` の揺れを正規化して比較)。次の 2 つは意図的な再掲なので対象外: (a) 概念ページの「押さえどころ」での引用と同ページ「資料」への掲載、(b) 概念ページと一覧ページの重複。報告するのは、一覧ページ同士の重複と、同一セクション内の重複のみ。

### 3. solutions.md の形式

- `<div class="competition-entry" markdown="1" ...>` に `data-year` / `data-datatype` / `data-platform` が揃っているか
- `data-datatype` が CLAUDE.md のタクソノミー(solutions.md のフィルタ UI の選択肢と同一)の値か
- div の開閉が対応しているか、badge の year と `data-year` が一致するか

### 4. 相対リンク・孤立ページ

- サイト内相対リンク(`./`, `../`)の参照先ファイルが実在するか
- `docs/wiki/concepts/` の各ページが materials.md の目次または他ページからリンクされているか(孤立検出)
- 「関連概念」のリンク先が実在するか

### 5. 目次の同期

`docs/materials.md` の目次・「Q&A」一覧と `docs/wiki/concepts/`・`docs/wiki/queries/` の実ファイルが一致するか。

## 報告形式

検査項目ごとに「問題なし」または問題の一覧(ファイル・行・内容)を報告し、最後に修正の提案をまとめる。実施後 `docs/wiki/log.md` に追記する: `- YYYY-MM-DD lint: 検出 N 件(内訳)`
