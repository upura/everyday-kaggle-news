# グラフ

グラフ構造データ（ネットワーク、分子、関係データなど）を扱う話題のページです。
表やテキストとは異なるモデリング（グラフニューラルネットワークなど）が必要になります。

## 押さえどころ

- グラフデータは「ノードとエッジ」という構造そのものが情報を持つため、GBDT に落とすための特徴量化（集約や埋め込み）か、GNN による直接のモデリングかが最初の分岐になる
- 体系的な学習にはグラフアルゴリズムの演習教材が役立つ

## 資料

- [グラフ道場 (Graph Dojo)](https://yuya-s.github.io/GraphDojo/)
- [データのつながりを活かす技術〜ネットワーク／グラフデータの機械学習から得られる新視点](https://gihyo.jp/book/2025/978-4-297-14784-6): グラフ構造データの特徴抽出と機械学習活用を解説する書籍。
- [僕たちがグラフニューラルネットワークを学ぶ理由](https://speakerdeck.com/joisino/pu-tatigagurahuniyurarunetutowakuwoxue-buli-you): 『グラフニューラルネットワーク』著者による導入と応用の紹介資料。
- [グラフニューラルネットワーク(GNN)徹底解説！用途と仕組みからPyGでの実装まで](https://zenn.dev/kami/articles/83c2daff760f5d): 前提知識から PyG 実装までを扱う GNN の解説記事。
- [グラフニューラルネットワーク（PyTorch実装つき書籍）](https://www.ohmsha.co.jp/book/9784274228872/): 基本的な知識や研究事例を PyTorch 実装と共に紹介する書籍。
- [大規模グラフデータを題材にしたNeurIPS 2022コンペ](https://ogb.stanford.edu/neurips2022/): 「KDD Cup 2021」に続き 2 度目の開催となった国際学会併設コンペ。
- [グラフニューラルネットワークの解説記事](https://theaisummer.com/gnn-architectures/): グラフの基礎から著名なアーキテクチャまでを扱う解説記事。
- [GPU上でグラフデータを分析するライブラリ「cuGraph」の紹介記事](https://acro-engineer.hatenablog.com/entry/2021/05/21/120000): ページランクの計算速度を比較する記事。
- [スタンフォード大学「Machine Learning with Graphs」講義動画](https://www.youtube.com/playlist?list=PLoROMvodv4rPLKxIpqhjhPgdQy7imNkDn): 埋め込み表現やニューラルネットワークを扱う講義動画。
- [GCNを用いた企業格付け予測手法（SIG-FIN発表）](https://www.slideshare.net/MasakazuMori2/gcn-230165927): 取引関係の有向グラフから特徴を獲得する手法を LightGBM 比較付きで提案。
- [グラフのデータ分析に関する概説資料](https://www.slideshare.net/ssuser0c8361/20200212-227754437): グラフ表現学習・グラフ畳み込みニューラルネットワーク・学会動向をまとめた資料。
- [ネットワークデータに対する深層学習の紹介記事](https://buildersbox.corp-sansan.com/entry/2021/02/19/114000): 数式を使わずタスクの概観とモデルを紹介する記事。
- [Graph Neural Networks: Foundations, Frontiers, and Applications](https://graph-neural-networks.github.io/): 27 章にわたる無料公開のグラフニューラルネットワーク書籍。

## 関連概念

- [表データコンペ](./tabular.md) / [推薦](./recommendation.md)
