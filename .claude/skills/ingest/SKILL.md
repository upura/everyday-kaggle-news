---
name: ingest
description: Kaggle 関連の URL をリンク集と wiki に取り込む。記事 URL のほか、Weekly Kaggle News の号 URL を渡すと紹介リンクを一括で展開して取り込む。「この URL を追加して」「最新号を ingest して」のような依頼で使う。
---

# Ingest — URL の取り込み

引数として 1 つ以上の URL を受け取り、リンク集と wiki に取り込む。規約はルートの `CLAUDE.md` に従う。

## Weekly Kaggle News の号 URL の場合

`https://weeklykagglenews.substack.com/p/...` 形式の URL は「号」として扱う。

1. 号ページを WebFetch し、紹介されている記事・資料の「タイトル | URL」一覧を抽出する
2. 抽出した各 URL に対して下記の「記事 URL ごとの手順」を実施する(重複はスキップ)
3. `docs/wiki/log.md` には号単位で 1 行記録する: `- YYYY-MM-DD ingest: WKN #NNN → 新規 M 件(変更ページ一覧)`
4. 号番号のみ(例: `#343`)を渡された場合は、アーカイブ(`/archive`)から該当号の URL を特定する

## 記事 URL ごとの手順

1. **重複確認**: `grep -rF "<URL>" docs/` で既掲載でないか確認する。URL 末尾スラッシュの有無や `http/https` の揺れも考慮する。既掲載なら報告してスキップ
2. **内容確認**: WebFetch で本文を取得し、主題・要点を把握する。タイトルだけで推測して注釈を書かない。取得できない場合は注釈なしで追加し、その旨を報告する
3. **分類**: CLAUDE.md のタクソノミーに従い掲載先を判定する
   - コンペの解法・参加録 → `docs/solutions.md`(既存の competition-entry div 形式。該当コンペの div が既にあればそこに追記、なければ div ごと新規作成し `data-year` / `data-datatype` / `data-platform` を設定)
   - 書籍 → `docs/books.md`(表形式)
   - イベント → `docs/events.md`
   - 称号振り返り・インタビュー → `docs/milestones.md`
   - サービス・ツール → `docs/service.md`
   - プラットフォーム → `docs/platform.md`
   - 上記以外の技術記事・話題 → 該当する概念ページ(`docs/wiki/concepts/`)の「資料」。`docs/materials.md` は目次のため直接エントリを置かない
4. **エントリ追加**: 既存形式で `- [タイトル](URL): 1〜2 文の注釈` を追記する
5. **概念ページへの統合**: 「押さえどころ」に反映すべき新しい知見があれば自分の言葉で統合する。該当する概念ページが無く、資料が 3 件以上見込める話題なら新規作成し(テンプレートは CLAUDE.md 参照)、`docs/materials.md` の目次に行を追記する
6. **log 更新**: `docs/wiki/log.md` の先頭に追記する: `- YYYY-MM-DD ingest: <URL> → <変更ページ一覧>`。`docs/materials.md` の「最近の更新」を直近 5 件程度に維持する(同日の複数 ingest は 1 行にまとめて良い)
7. **報告**: 追加したエントリ・変更したページ・新規作成した概念ページを一覧で報告する

## 注意

- 注釈は短いオリジナルの紹介文に限る(転載・長文要約をしない)
- 既存ページの構成(見出し・形式)は変えない
- コミットは指示があった場合のみ行う
