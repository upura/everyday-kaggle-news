# Everyday Kaggle News

データサイエンスコンペティション「[Kaggle](https://www.kaggle.com/)」に関する非公式リンク集です。
有志による記事やサービスなども対象に、用途や話題別にまとめています。
毎週金曜日配信のニューズレター「[Weekly Kaggle News](https://weeklykagglenews.substack.com/)」の関連サイトです。
競技プログラミングサイト「[AtCoder](https://atcoder.jp/)」における「[AtCoder Clans](https://kato-hiro.github.io/AtCoderClans/)」のような立ち位置を意識しています。
なお既存の類似サイトとして、日本人 Kaggler コミュニティ「kaggler-ja」による「[Kaggler Ja Wiki](https://kaggler-ja.wiki/)」があります。

## サイト案内

- [入門者・初学者向け](./docs/quickstart.md)
- [最新情報の確認](./docs/recent.md)
- [コンペ解法](./docs/solutions.md)
- [称号振り返り](./docs/milestones.md)
- [書籍](./docs/books.md)
- [イベント](./docs/events.md)
- [サービス・ツール](./docs/service.md)
- [コンペプラットフォーム](./docs/platform.md)
- [話題別一覧](./docs/materials.md)

## 更新フロー

本リポジトリは LLM Wiki として運用しており、規約は [CLAUDE.md](./CLAUDE.md) に定義しています。

- 週次: Weekly Kaggle News の配信後、Claude Code で `/ingest <最新号の URL>` を実行します。号に含まれる URL が展開され、重複を除いて各話題ページ・一覧ページに追加されます。変更を確認してコミット・push すると GitHub Pages に反映されます
- 月次: `/lint` でリンク切れ・重複・形式の検査を実行します

## 貢献

Issue や Pull Request を歓迎しています。詳しくは [CONTRIBUTING.md](https://github.com/upura/everyday-kaggle-news/blob/main/CONTRIBUTING.md) をご覧ください。
