---
name: query
description: Kaggle に関する質問に、このリンク集と wiki の内容を根拠に回答する。再利用価値のある回答は Query ページとして docs/wiki/queries/ に資産化する。「〜についてこのリポジトリから教えて」「query して」のような依頼で使う。
---

# Query — wiki への質問

質問を受け取り、リポジトリ内の知識を根拠に回答する。規約はルートの `CLAUDE.md` に従う。

## 手順

1. **探索**: `docs/wiki/concepts/` と `docs/wiki/queries/` を最初に確認し、次に `docs/` 直下の一覧ページを Grep で探索する。既存の Query ページで回答済みならそれを提示して終了
2. **回答**: 見つかった資料・概念ページを根拠に回答を組み立てる。根拠となるページ・外部リンクを必ず添える。リポジトリ内に根拠が無い部分は「本リンク集には未掲載」と明示する(一般知識で埋めない)
3. **資産化の判断**: 再利用価値がある回答(他の人も聞きそうな質問、複数ソースの統合が必要だった質問)は `docs/wiki/queries/<kebab-case>.md` に保存する。単純な検索で済んだ質問は保存しない
4. **Query ページの形式**:

```markdown
# (質問文)

(回答。根拠へのリンクを含める)

## 参照

- [ページ名](../concepts/page.md)
- [外部資料タイトル](URL)
```

5. **index / log 更新**: 保存した場合は `docs/wiki/index.md` の Query 一覧と `docs/wiki/log.md` に追記する: `- YYYY-MM-DD query: <質問の要約> → queries/<file>.md`
