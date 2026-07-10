# Everyday Kaggle News

データサイエンスコンペティション「[Kaggle](https://www.kaggle.com/)」に関する非公式リンク集です。
有志による記事やサービスなども対象に、用途や話題別にまとめています。
毎週金曜日配信のニューズレター「[Weekly Kaggle News](https://weeklykagglenews.substack.com/)」の関連サイトです。
競技プログラミングサイト「[AtCoder](https://atcoder.jp/)」における「[AtCoder Clans](https://kato-hiro.github.io/AtCoderClans/)」のような立ち位置を意識しています。
なお既存の類似サイトとして、日本人 Kaggler コミュニティ「kaggler-ja」による「[Kaggler Ja Wiki](https://kaggler-ja.wiki/)」があります。
Kaggler Ja Wiki と比べた本サイトの特徴は、LLM Wiki として運用している点です。
人間が選定を続けるニューズレター「Weekly Kaggle News」の紹介リンクをソースに、LLM が話題ごとの知見の統合と相互リンクを維持し、最新情報の反映は編集者が Pull Request のレビューを通じて確認しています。

## サイト案内

入口は「**[目次](./docs/materials.md)**」です。
「学び方」「情報収集・コミュニティ」「データ種別・タスク」「進め方・環境」「コンペの開催」の話題ごとに、[表データ](./docs/wiki/concepts/tabular.md)や[画像認識](./docs/wiki/concepts/image-recognition.md)などの Wiki ページ(全 18 話題)と、[コンペ解法](./docs/solutions.md)や[書籍](./docs/books.md)などの一覧ページ(全 8 ページ)を案内します。

## 更新フロー

本リポジトリは LLM Wiki として運用しており、規約は [CLAUDE.md](./CLAUDE.md) に定義しています。

- 週次: Weekly Kaggle News の配信後、Claude Code で `/ingest <最新号の URL>` を実行します。号に含まれる URL が展開され、重複を除いて各話題ページ・一覧ページに追加されます。変更を確認してコミット・push すると GitHub Pages に反映されます
- 月次: `/lint` でリンク切れ・重複・形式の検査を実行します

## 貢献

Issue や Pull Request を歓迎しています。詳しくは [CONTRIBUTING.md](https://github.com/upura/everyday-kaggle-news/blob/main/CONTRIBUTING.md) をご覧ください。
