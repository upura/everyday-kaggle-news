# 推薦

推薦システムを題材にした話題のページです。
候補生成とリランキングの 2 段構成など、推薦特有の問題設計を押さえると取り組みやすくなります。

## 押さえどころ

- 協調フィルタリングから始まる推薦アルゴリズムの基礎を一巡しておくと、コンペの解法（候補生成 + 特徴量 + リランキング）が読み解きやすい
- リランキング段階は実質的に表データの問題になるため、[表データコンペ](./tabular.md)の知見が活きる

## 資料

- [レコメンドアルゴリズム入門：基礎から応用まで実装に必要な知識を解説](https://qiita.com/birdwatcher/items/b60822bdf9be267e1328)
- [レコメンドコンペ入門](https://speakerdeck.com/t88/rekomendokonperu-men): 推薦コンペの一般的な解法を紹介する発表資料。
- [N=1 の推薦系コンペの戦い方](https://speakerdeck.com/unonao/n-equals-1-notui-jian-xi-konpenozhan-ifang): 推薦コンペでの優勝経験者による前処理からモデル学習までの発表資料。
- [使い回しやすい 2-stage recommender systemの デザインパターンを考えて実装した話](https://speakerdeck.com/zerebom/recommender): 2 段階推薦のための自作パイプラインの紹介。コード公開つき。
- [【Kaggleブログ】 OTTOコンペを題材に、レコメンドタスクの一般的なアプローチをご紹介！](https://blog.brainpad.co.jp/entry/2023/04/06/151913): OTTO コンペを題材にした推薦タスクの定跡の解説記事。
- [Building a Recommender System using Machine Learning](https://medium.com/towards-data-science/building-a-recommender-system-using-machine-learning-2eefba9a692e): OTTO コンペを題材にした「Kaggle Blueprints」シリーズの解説記事。
- [レコメンド系kaggleコンペまとめ](https://zenn.dev/mina_moto/articles/6ff668f34fa557): Kaggle の推薦コンペを横断してコンペ概要と上位解法をまとめた記事。
- [Transformers4Recで簡単にセッションベースなレコメンデーションを試してみた](https://acro-engineer.hatenablog.com/entry/2022/12/14/130000): NVIDIA 製セッション推薦ライブラリの紹介記事。
- [RecSys Challenge 2022 3位解法（NVIDIA）](https://medium.com/nvidia-merlin/building-a-diverse-models-ensemble-for-fashion-session-based-recommendation-for-recsys2022-2419d2182c4c): ファッション推薦を題材にした RecSys 併設コンペの 3 位解法。
- [『推薦システム実践入門――仕事で使える導入ガイド』書評](https://upura.hatenablog.com/entry/2022/05/03/165903): 映画推薦を題材とした Netflix Prize コンペの話題にも言及する書評記事。
- [推薦システムの演習問題集 recsys-python](https://recsyslab.github.io/recsys-python/): 13 章構成・全 163 問でコードと出力結果つきの演習教材。
- [Netflixの推薦システムに深層学習を導入した際の課題と教訓をまとめた論文](https://ojs.aaai.org/index.php/aimagazine/article/view/18140): アーキテクチャ・特徴量・オフライン/オンライン評価の乖離など幅広い話題に言及。
- [Transformer構造を推薦に応用した「Transformer4Rec」の紹介記事](https://recruit.gmo.jp/engineer/jisedai/blog/nlp-recsys-relation/): 時系列性を考慮した推薦と自然言語処理の繋がりを議論。
- [ウェブ上でのユーザ行動分析まとめ記事](https://speakerdeck.com/karakurist/user-behaviour-vol2): 国際学会で開催されたコンペの解法も紹介する資料。
- [埋め込み表現の活用方法紹介資料（検索・推薦、KaggleライクなCI環境構築）](https://speakerdeck.com/nadare881/embeddingwoyong-itafen-xi-jian-suo-tui-jian-falseji-shu): ニューラルネットワークで獲得した埋め込み表現の活用手法をまとめた資料。
- [セッションベース推薦ライブラリ「Transformers4Rec」公開（NVIDIA）](https://medium.com/nvidia-merlin/transformers4rec-4523cc7d8fa8): Hugging Face Transformers を活用した実装。RecSys 2021 に論文採択。
- [深層学習を用いたクリック予測ライブラリ「DeepCTR」の解説記事](https://qiita.com/guglilac/items/028ba8e156e5c74f650a): 主要モデルを既存解説記事へのリンクと共に紹介。
- [深層学習推薦システムの概要・有名構造まとめ記事](https://developer.nvidia.com/blog/using-neural-networks-for-your-recommender-system/): 「Deep Learning Recommender Summit」開催告知も合わせて掲載。
- [SIGIR eCom 2021併設コンペの解法（Transformerによるセッションベース推薦）](https://medium.com/nvidia-merlin/winning-the-sigir-ecommerce-challenge-on-session-based-recommendation-with-transformers-v2-793f6fac2994): 国際学会ワークショップ併設コンペの優勝解法。
- [Booking.com Data Challenge NVIDIAチーム優勝解法の講演動画](https://www.youtube.com/watch?v=bHuww-l_Sq0&feature=youtu.be): ACM WSDM ワークショップ併設コンペの旅程推薦優勝解法。
- [Booking.com Data Challenge NVIDIAチーム優勝解法の記事](https://developer.nvidia.com/blog/how-to-build-a-winning-deep-learning-powered-recommender-system-part-3/): 深層学習を用いた旅程推薦の優勝解法を解説する記事。
- [Netflix Prizeの意義を振り返る記事](https://xamat.medium.com/on-the-usefulness-of-the-netflix-prize-403d360aaf2): 優勝モデルの本番実装にも取り組んだ Xavier Amatriain さんによる振り返り。
- [購買データコンペ振り返り会でのword2vec活用発表資料](https://www.takapy.work/entry/2021/02/27/122300): 商品・ユーザの埋め込み表現を word2vec で獲得する手法の紹介。
- [「RecSys」特徴量エンジニアリングのチュートリアル資料（Chris Deotte）](https://github.com/rapidsai/deeplearning/tree/main/RecSys2020Tutorial): GPU を用いた高速化にも言及する充実したチュートリアル。
- [「RecSys Challenge 2020」優勝解法の講演告知](https://www.nvidia.com/en-us/gtc/session-catalog/?ncid=so-twit-74735&search=A21139&search.language=1594320459782001LCjF&tab.catalogtabfields=1600209910618001TWM3): GPU で大規模データを前処理・学習した取り組みの講演。

## 関連概念

- [表データコンペ](./tabular.md) / [グラフ](./graph.md)
