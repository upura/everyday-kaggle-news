# 画像認識・視覚モデルの技術動向

Vision Transformer・CLIP・自己教師あり学習など画像認識分野のモデル・研究動向と、国際会議のサーベイ・参加報告をまとめます。
コンペでの実践的な戦い方・定跡は [画像認識コンペ](./image-recognition.md) を参照してください。

## 押さえどころ

- CNN と Vision Transformer（ViT）は競合しつつ補完関係にもある。ViT はデータ・パラメータ規模を増やすほど性能が伸びる傾向がある一方、CNN 系（ConvNeXt など）は中規模データで依然強い
- CLIP に代表される画像・言語のマルチモーダル基盤モデルは、日本語特化版の公開が相次いでおり、ゼロショット分類やデータフィルタリングなど活用の幅が広がっている
- 自己教師あり学習（DINO、SimCLR 系など）はラベルなしデータからの事前学習手法として、医療画像など labeled data が乏しい領域で特に注目される
- CVPR・ICCV・ECCV などの国際会議動向は、翌年以降にコンペで使われるモデル・手法の先行指標になりやすい

## 資料

### Vision Transformer・Transformer動向


- [【DL輪読会】言語以外でのTransformerのまとめ](https://www.slideshare.net/DeepLearningJP2016/dltransformer-vit-perceiver-frozen-pretrained-transformer-etc)
- [DETR手法の変遷と最新動向（CVPR2025）](https://speakerdeck.com/tenten0727/detrshou-fa-nobian-qian-tozui-xin-dong-xiang-cvpr2025)
- [CNN vs ViT](https://speakerdeck.com/yushiku/cnn-vs-vit): CNN と ViT を複数観点で比較する発表資料。
- [Mobile-Former: Bridging MobileNet and Transformer（CVPR 2022 解説資料）](https://speakerdeck.com/tereka114/mobile-former-bridging-mobilenet-and-transformer): CVPR2022 論文読み会での発表資料。
- [画像認識分野でのTransformer応用解説（SSII2022）](https://speakerdeck.com/yushiku/20220608_ssii_transformer): Transformer の概要・応用範囲・近年の潮流を紹介。
- [階層的Vision Transformerの研究動向まとめ](https://www.slideshare.net/ren4yu/hierarchical-vision-transformer): Swin Transformer など Kaggle でも多用されるモデルの研究動向。
- [Swin Transformer V2 事前学習済み重み公開](https://github.com/microsoft/Swin-Transformer): Kaggle コンペの上位解法にも登場する画像認識モデルの公開重み。
- [Vision Transformerの注意機構に着目した論文の解説記事](https://tech.sensetime.jp/?p=2220): 「When Shift Operation Meets Vision Transformer」の解説。
- [Swin Transformer 解説資料（ICCV2021論文読み会）](https://www.slideshare.net/ren4yu/swin-transformer-iccv21-best-paper): Kaggle の画像コンペで頻繁に使われるモデルの解説資料。
- [Swin Transformerを用いた物体検出の実験記事](https://qiita.com/Abebe9849/items/47de3f77ed02ba6f242d): Kaggle「VinBigData Chest X-ray Abnormalities Detection」を題材にした実験まとめ。
- [Vision Transformerの仕組み解説資料](https://speakerdeck.com/himidev/vision-transformerfalsesikumi): Transformer 自体の仕組みと画像認識分野への応用事例をまとめた資料。
- [画像認識分野でのTransformer研究動向まとめ資料](https://www.slideshare.net/kuz44ma69/transformer-in): 歴史的な流れや畳込み層との違いを扱う資料。
- [画像認識向けMLP活用論文3本のまとめ記事](https://qiita.com/TeamN/items/4135f9a8971d5185ea74): 2021 年 5 月に arXiv 公開された論文をまとめた記事。
- [画像認識分野へのTransformer応用に関する洞察まとめ記事](https://note.com/akira_tosei/n/n3fb6dcd82b93): 弱点や改善の方向性についても議論する記事。
- [画像認識領域でのTransformer研究動向資料（SSII2021）](https://www.slideshare.net/SSII_Slides/ssii2021-ss1-transformer-x-computer-vision-transformercomputer-vision): 実活用の観点での CNN との比較と今後の展望を扱う資料。
- [Vision Transformer (ViT) の解説記事（衛星画像分類）](https://sorabatake.jp/20454/): 概要説明の後、衛星画像分類への適用を紹介。
- [MLP-Mixer・gMLP論文の解説資料](https://www.slideshare.net/KazuyukiMiyazawa/mlpmixer-an-allmlp-architecture-for-vision): 畳み込みや注意機構を使わない多層パーセプトロンによる画像分類の解説。
- [ViTに畳み込みを導入したモデルの解説記事](https://qiita.com/omiita/items/01687855d7891bcf5fed): 構造の概要と論文の実験結果をまとめた記事。
- [Transformer勉強会資料（第六回全日本コンピュータビジョン勉強会）](https://speakerdeck.com/sei88888/quan-ri-ben-cvmian-qiang-hui-fa-biao-zi-liao-learning-transformer-in-40-minutes): 画像領域における Transformer を題材にした勉強資料。
- [End-to-End Object Detection with Transformers（DETR）解説資料](https://speakerdeck.com/yushiku/end-to-end-object-detection-with-transformers): ECCV2020 を題材にした勉強会での発表資料。
- [Vision Transformer論文・実装公開](https://arxiv.org/abs/2010.11929): Transformer 機構を画像分類タスクに適用し高性能を報告。
- [Vision Transformerの解説記事](https://qiita.com/omiita/items/0049ade809c4817670d7): Transformer 機構の画像分類タスク適用を解説する記事。
- [Transformerの解説記事（歴史的流れを踏まえて）](https://aru47.hatenablog.com/entry/2020/08/18/175711): 上位解法に頻出する Transformer の特徴を紹介。
- [DETR（Transformerによる物体検出）の紹介記事](https://blog.seishin55.com/entry/2020/05/30/175811): モデル・損失関数・実験結果の概要をまとめた記事。

### CLIP・マルチモーダル


- [Large Vision Language Model (LVLM) に関する最新知見まとめ (Part 1)](https://speakerdeck.com/onely7/large-vision-language-model-lvlm-niguan-suruzui-xin-zhi-jian-matome-part-1): LLM と画像処理をつなぐ機構に焦点を当てた LVLM の知見まとめ。
- [自然言語とVision&Language](https://speakerdeck.com/kuehara/zi-ran-yan-yu-tovision-and-language): 深層学習初期から大規模モデルまでの Vision & Language 研究動向の概観資料。
- [大規模画像テキストデータのフィルタリング手法の紹介](https://speakerdeck.com/lyakaap/da-gui-mo-hua-xiang-tekisutodetanohuirutaringushou-fa-noshao-jie): データフィルタリングで性能を競うコンペを題材にした発表資料。
- [日本語CLIP 学習済みモデルと評価用データセットの公開](https://blog.recruit.co.jp/data/articles/japanese-clip/): 日本語特化 CLIP のモデルと評価データセットの公開記事。
- [最高性能の、日本語画像言語特徴抽出モデル「Japanese Stable CLIP」をリリースしました](https://ja.stability.ai/blog/japanese-stable-clip): Stability AI による日本語特化 CLIP の公開告知。
- [高性能な日本語マルチモーダル基盤モデル「clip-japanese-base」を公開しました](https://techblog.lycorp.co.jp/ja/20240514b): LINE ヤフーによる日本語 CLIP 初版の公開と開発手法の解説。
- [Vision Banana: Image Generators are Generalist Vision Learners](https://speakerdeck.com/kzykmyzw/vision-banana-image-generators-are-generalist-vision-learners): 画像生成モデルの微調整で汎用の画像認識モデルを作る Google DeepMind の取り組みの解説資料。
- [ドメイン特化なCLIPモデルとデータセットの紹介](https://speakerdeck.com/tattaka/domeinte-hua-na-clipmoderutodetasetutonoshao-jie)
- [高性能な日本語マルチモーダル基盤モデル「clip-japanese-base-v2」の公開](https://techblog.lycorp.co.jp/ja/20251218a): LINE ヤフーによる日本語特化 CLIP の公開告知。データフィルタリングと知識蒸留による改善を解説。
- [【論文紹介】Is CLIP ideal? No. Can we fix it? Yes!](https://speakerdeck.com/shun6211/lun-wen-shao-jie-is-clip-ideal-no-can-we-fix-it-yes-di-65hui-konpiyutabiziyonmian-qiang-hui-at-guan-dong): CLIP の埋め込み空間の課題と改善策を提案する論文の紹介資料。
- [Zero-shot Learning網羅的サーベイ：CLIPが切り開いたVision & Languageの新しい世界](https://techblog.exawizards.com/entry/2023/05/10/055218): CLIP 後続の研究 70 本程度を調査したサーベイ記事。
- [[輪講] SigLIP 2: Multilingual Vision-Language Encoders with Improved Semantic Understanding, Localization, and Dense Features](https://speakerdeck.com/nk35jk/lun-jiang-siglip-2-multilingual-vision-language-encoders-with-improved-semantic-understanding-localization-and-dense-features)
- [CLIP・CLOOBの日本語版学習済みモデル公開](https://prtimes.jp/main/html/rd/p/000000031.000070041.html): オープンソースデータで学習され商用利用も可能な日本語言語画像モデルの公開。
- [CLIP日本語版モデルの学習方法解説記事](https://qiita.com/sonoisa/items/00e8e2861147842f0237): 画像とテキストの埋め込み表現を学習する CLIP の日本語版モデルの学習方法を解説。
- [CLIPを模した日本語モデルの作成記事](https://www.ogis-ri.co.jp/otc/hiroba/technical/similar-document-search/part19.html): 画像とテキストを同じ多次元ベクトル空間に埋め込むモデルを Google Colaboratory 上で学習する記事。
- [言語と画像を組み合わせた領域でのTransformer活用総説論文](https://link.springer.com/article/10.1007/s11263-021-01547-8): Vision & Language 領域での Transformer 活用をまとめた総説論文。
- [OpenAI「CLIP」の解説記事（PyTorch実装つき）](https://sachinruk.github.io/blog/pytorch/pytorch%20lightning/loss%20function/gpu/2021/03/07/CLIP.html): 画像認識モデル CLIP を PyTorch 実装とともに紹介。
- [「DALL·E」解説Podcast（第3回）](https://anchor.fm/yoheikikuta/episodes/DALLE--part-3-DALLE-errr51): テキストから画像を生成するモデルの解説シリーズ最終回。要点メモも公開。
- [マルチモーダル深層学習「WIDeText」の記事（Airbnb）](https://medium.com/airbnb-engineering/widetext-a-multimodal-deep-learning-framework-31ce2565880c): 説明文・写真・メタデータを特徴量に活用する部屋タイプ分類の紹介。

### 自己教師あり学習


- [画像に対する自己教師あり表現学習手法について②](https://blog.recruit.co.jp/data/articles/ssl_vision_02/)
- [⾃⼰教師あり学習によるビジョン基盤モデルの事前学習](https://speakerdeck.com/hf149/jiao-shi-arixue-xi-niyorubiziyonji-pan-moderunoshi-qian-xue-xi): 画像の自己教師あり学習の代表的手法と発展的話題のまとめ。
- [自己教師あり学習による事前学習（CVIMチュートリアル）](https://speakerdeck.com/naok615/zi-ji-jiao-shi-arixue-xi-niyorushi-qian-xue-xi-cvimtiyutoriaru): 自己教師あり事前学習のサーベイチュートリアル資料。
- [少量データ・ラベルから効率的に学習する技術の最新研究動向（SSII2022）](https://www.slideshare.net/SSII_Slides/ssii2022-ss2): 不足情報を補うための手法を概観した資料。
- [画像を対象とした自己教師あり表現学習まとめ（連載第1回）](https://blog.recruit.co.jp/data/articles/ssl_vision_01/): 手法の基本的な考え方を紹介する 3 本立て連載の初回。
- [Big Self-Supervised Models Advance Medical Image Classification 解説記事（ICCV 2021）](https://ai.googleblog.com/2021/10/self-supervised-learning-advances.html): 医療画像の事前学習とメタデータによるデータ増強を併用し性能を向上。
- [MIRU2021チュートリアル「限られたデータからの深層学習」](https://twitter.com/CVpaperChalleng/status/1419906270643908613?s=20): 様々な学習の枠組みやラベルなしデータでの事前学習をまとめた資料。
- [自己教師あり学習「DINO」の解説記事](https://oumpy.github.io/blog/2021/05/dino.html): atmaCup 上位者が利用した手法の背景とモデル構造を解説。
- [少ないデータ・ラベルを効率活用する機械学習動画シリーズ第1弾](https://www.youtube.com/playlist?list=PLbtqZvaoOVPBF8MypuGdfMKuc_fHhjp9-): データ拡張・転移学習・半教師あり学習を扱う動画シリーズ。
- [自己教師あり学習の概説記事（Contrastive Learning）](https://qiita.com/omiita/items/a7429ec42e4eef4b6a4d): 画像分類を題材に手法を中心解説。
- [半教師あり学習・弱教師あり学習のサーベイ資料](https://www.slideshare.net/ren4yu/semi-supervised-weaklysupervised-unsupervised-and-active-learning): 画像処理の事例を中心に手法をまとめた資料。
- [半教師あり学習手法まとめ記事（Temporal ensembling・Mean teachers・UDA・MixMatch）](https://hotcocoastudy.hatenablog.jp/entry/2020/01/23/210357): 代表的な半教師あり学習手法を整理した記事。
- [半教師あり学習「FixMatch」の解説記事](https://medium.com/@akichan_f/1%E6%9E%9A%E3%81%97%E3%81%8B%E3%83%A9%E3%83%99%E3%83%AB%E3%83%87%E3%83%BC%E3%82%BF%E3%81%8C%E3%81%AA%E3%81%8F%E3%81%A6%E3%82%82%E5%AD%A6%E7%BF%92%E3%81%A7%E3%81%8D%E3%82%8Bfixmatch-982275853a88): 少量ラベルでも学習可能な手法を実験結果と共に紹介。

### 国際会議サーベイ・参加報告


- [第62回名古屋CV・PRML勉強会：CVPR2025論文紹介 (MambaOut)](https://speakerdeck.com/naok615/di-62hui-ming-gu-wu-cvprmlmian-qiang-hui-cvpr2025lun-wen-shao-jie-mambaout): 状態空間モデル Mamba が画像認識に必要かを分析した論文の紹介資料。
- [CVPR 2025 Report](https://x.com/HirokatuKataoka/status/1934663060200833392): 画像認識の国際会議 CVPR 2025 の研究潮流を 180 ページ超にまとめた参加報告資料。
- [ECCV 2024 速報 (PDF)](https://hirokatsukataoka.net/temp/presen/241004ECCV2024Report_finalized.pdf): 国際会議 ECCV 2024 の研究動向を 130 ページ超にまとめた報告資料。
- [ICCV 2023 速報 (PDF)](https://hirokatsukataoka.net/temp/presen/231006ICCV%202023%20Report%20(Release%20Ver.).pdf): 国際会議 ICCV 2023 の研究動向を 170 ページにまとめた報告資料。
- [「CVPR2023-速報-」ResearchPortトップカンファレンス定点観測 vol.9](https://research-p.com/column/1237): CVPR2023 の投稿状況とキーワードの分析記事。
- [ECCV 2022 参加記録](https://acro-engineer.hatenablog.com/entry/2022/10/28/123000): 面白かった論文 5 本を紹介する参加記録。
- [Image Matching Challenge 2022 国際会議ワークショップ報告](https://engineers.ntt.com/entry/2022/07/28/090254): 異なる視点から撮影された2画像のマッチング課題に関する報告記事。
- [MIRU2022特別企画「局所特徴量・AlexNet・カーネル法」](https://sites.google.com/view/miru2022/program/specialevent?authuser=0): 過去の著名な研究や時代背景に焦点を当てた講演資料。
- [CVPR 2022 論文の日本語まとめ](https://xpaperchallenge.org/cv/survey/cvpr2022_summaries/listall/): 有志による CVPR 2022 採択論文の日本語サマリ集。
- [NTIRE超解像コンペの紹介資料（CVPR併設）](https://speakerdeck.com/sansandsoc/ntire-2021-learning-the-super-resolution-space-challenge): 超解像分野の歴史と具体的な結果を解説する資料。
- [CVPR 2021 3次元物体検出サーベイ資料](https://speakerdeck.com/takarasawa_/monocular-3d-object-detection-at-cvpr2021): 各論文が扱う課題や提案手法の概要をまとめた資料。
- [2010年以降のコンピュータビジョン分野の動向まとめ記事](https://gihyo.jp/dev/column/newyear/2021/computer-vision-trends): 深層学習による画像認識コンペの革新から近年の潮流までを解説。
- [ECCV2020サーベイ資料](https://speakerdeck.com/mot_ai_tech/eccv2020-papers): 研究開発エンジニア 5 人が選定した論文 24 本を解説。
- [CVPR論文読み会資料（前半まとめ）](https://takmin.hatenablog.com/entry/2020/07/18/235337): コンピュータビジョン国際会議の論文読み会資料。
- [CVPR論文読み会資料（別回、前半）](https://takmin.hatenablog.com/entry/2020/07/05/000451): 後編は別日程で予定された論文読み会資料。

### モデル・技術動向


- [深層学習によるセマンティックセグメンテーションとその最新動向](https://speakerdeck.com/hf149/shen-ceng-xue-xi-niyorusemanteitukusegumentesiyontosofalsezui-xin-dong-xiang)
- [最新の深層学習技術による古典くずし字認識の現状と今後の展望](http://shunk031.hatenablog.com/entry/kuzushiji-recognition-survey-2020)
- [点群処理Backbone Networkと点群の事前学習/表現学習](https://speakerdeck.com/nnchiba/biao-xian-xue-xi): 点群を対象にした深層学習の研究動向のサーベイ資料。
- [最近のVisual Odometry with Deep Learning](https://speakerdeck.com/tattaka/zui-jin-novisual-odometry-with-deep-learning): 深層学習によるカメラ姿勢追跡の研究動向まとめ。
- [Segment Anything Model 2](https://speakerdeck.com/tenten0727/segment-anything-model-2): SAM 2 を初代との差分も含めて解説する資料。
- [Meta開発のセグメンテーションモデル Segment Anything Model(SAM) の解説](https://zenn.dev/fusic/articles/ml-segment-anything-meta): 初代 SAM の概要を端的にまとめた解説記事。
- [AI×医用画像の現状と可能性_2023年版](https://speakerdeck.com/tdys13/aixmedical-imaging-in-japan-2023): 医用画像 AI の研究・応用動向のまとめ資料。
- [論文まとめ: Local Feature Matching Using Deep Learning: A Survey(202401)](https://qiita.com/fam_taro/items/27f20ccf85fe86821fe6): 局所特徴量マッチングの総説論文の紹介記事。
- [Face Recognition @ ECCV2022](https://speakerdeck.com/takarasawa_/face-recognition-at-eccv2022): ArcFace を起点とした顔認証分野の ECCV2022 論文調査資料。
- [AI×医用画像の現状と可能性_2022年版](https://speakerdeck.com/tdys13/aixmedical-imaging-in-japan-2022): 医用画像 AI 領域の研究動向をまとめた資料。
- [動作認識に関するサーベイ資料](https://www.slideshare.net/ttamaki/ss-254290005): 動作認識の手法・タスク・データセットをまとめた資料。
- [『Vision Transformer入門』書評](https://note.com/maxwell/n/nbdda95bc01e0)
- [『Vision Transformer入門』著者による紹介記事](https://snowman-88888.hatenablog.com/entry/2022/09/17/090000): 執筆の背景と各章の概要のまとめ。
- [dethub](https://github.com/okotaku/dethub): 物体検出・セグメンテーションのベースラインと精度向上手法を検討するリポジトリ。
- [衛星データを題材にした機械学習タスクの紹介](https://sorabatake.jp/27897/): 物体検出・セグメンテーション・画像分類・超解像などの整理記事。
- [視覚基盤モデル（DINOv3）を使って衛星画像コンペで勝ちたい](https://www.docswell.com/s/motokimura/KVM382-dinov3-sat-bench): 衛星画像コンペでの視覚基盤モデル活用の実験報告。
- [LLMの効率化を支えるアルゴリズム](https://speakerdeck.com/taturabe/llmnoxiao-lu-hua-wozhi-eruarugorizumu)
- [局所特徴抽出における特徴表現の変遷まとめ](https://speakerdeck.com/hf149/ju-suo-te-zheng-liang-hua-xiang-ren-shi-niokerute-zheng-biao-xian-huo-de-falsebian-qian): SIFT から Vision Transformer まで幅広い変遷を紹介する資料。
- [ArcFace関連の距離学習手法サーベイ](https://speakerdeck.com/takarasawa_/face-recognition-and-arcface-papers): 顔認識タスクを題材に距離学習関連の関連研究をまとめた資料。
- [Awesome Deep Homographyの最新動向まとめ](https://tech-blog.abeja.asia/entry/awesome-deep-homography-202004): 2 つの異なる姿勢から撮影した平面間の変換推定について、SIFT と深層学習の手法を比較しながら解説する記事。
- [OpenVINOによる画像認識モデル最適化の実験記事](https://acro-engineer.hatenablog.com/entry/2022/05/12/000000): PyTorch モデルを変換し複数モデルで最適化効果を検証した記事。
- [デジタル技術を用いた「くずし字」資料解読の研究動向まとめ](https://current.ndl.go.jp/ca2015): Kaggle で開催されたくずし字コンペにも言及する記事。
- [「A ConvNet for the 2020s」解説記事](https://devblog.thebase.in/entry/2022/03/28/110000): 近年の画像認識の動向を振り返りながら ConvNeXt の性能改善の工夫を解説。
- [TensorFlow Image Models](https://github.com/martinsbruveris/tensorflow-image-models): PyTorch Image Models を模した TensorFlow 版の画像モデルライブラリ。
- [多重物体追跡（MOT）の技術発展の歴史紹介記事（前編）](https://tech.acesinc.co.jp/entry/2021/11/08/133336): NFL Helmet Assignment で使われた技術にも言及。
- [多重物体追跡（MOT）の技術発展の歴史紹介記事（後編）](https://tech.acesinc.co.jp/entry/2021/11/24/165628): より最新の技術を扱う続編記事。
- [2021年末時点で利用可能な物体検出ライブラリの紹介記事](https://aru47.hatenablog.com/entry/2022/01/01/123929): 参考記事・コードへのリンクと著者の所感をまとめた記事。
- [『コンピュータビジョン最前線』創刊号の先行公開原稿](https://www.kyoritsu-pub.co.jp/bookdetail/9784320125421): 自己教師あり学習や画像認識モデル構造など最先端の話題をまとめた書籍。
- [深層距離学習の解説記事（Shopeeコンペ例）](https://tech-blog.optim.co.jp/entry/2021/10/01/100000): Kaggle「Shopee - Price Match Guarantee」など多くの解法で使われる手法の解説。
- [EfficientNetV2・CoAtNetの紹介記事（Google Research）](https://ai.googleblog.com/2021/09/toward-fast-and-accurate-neural.html): 高速かつ高性能な画像認識モデル 2 つの紹介。
- [Torchvision物体検出モデルの比較記事](https://github.com/NobuoTsukamoto/benchmarks/blob/main/pytorch/torchvision/README.md): GTX 1070・Google Colaboratory での検証と動画リンクつき。
- [画像認識分野の学習効率化の調査資料](https://www.slideshare.net/cvpaperchallenge/efficient-training): ネットワーク探索・学習コスト削減の枠組みをまとめた資料。
- [EfficientNetV2の解説記事](https://dajiro.com/entry/2021/04/10/230416): EfficientNet の後継モデルの解説記事。
- [「NFNets」の解説動画](https://www.youtube.com/watch?v=rNkHjZtH0RQ&feature=youtu.be): Batch Normalization を使わない画像分類の最高性能モデルの解説。
- [動画認識コンペのサーベイ資料（ActivityNet Challenge等）](https://www.slideshare.net/cvpaperchallenge/towards-performant-video-recognition-231628214): さまざまなコンペの課題・解法をまとめた資料。
- [PyTorchによる画像分類の性能向上手法まとめ記事](https://twitter.com/omiita_atiimo/status/1362249066013335553?s=20): データ水増し手法などをソースコード付きで紹介。
- [Metric Learning「Supervised Contrastive Learning」の解説記事](https://towardsdatascience.com/how-to-use-metric-learning-embedding-is-all-you-need-f26e01597375?gi=95f213204ad5): 通常の画像分類との違いを中心に説明し実装も公開。
- [Vision Transformer (ViT) 解説教材（Notebook形式）](https://colab.research.google.com/github/hirotomusiker/schwert_colab_data_storage/blob/master/notebook/Vision_Transformer_Tutorial.ipynb): 段階的に実行しながら仕組みを学べる教材。
- [2020年のKaggle画像分類コンペ1位解法まとめ記事](https://qiita.com/inoichan/items/140cf018d31151d2701a): 8 コンペの概要と解法を端的に紹介。
- [Solafuneコンペ向けKerasサンプルコード](https://zenn.dev/beluga/articles/f2b7d94c0213680b3dc2): PyTorch 版に続く有志による情報共有。
- [KaggleのNotebookで画像読み込み・データ増幅を高速化する記事](https://qiita.com/hirune924/items/bfb099a704537b4e22ca): NVIDIA DALI と Kornia の組み合わせを紹介。
- [Kaggle Masterによる画像コンペTipsまとめ（phalanxさん）](https://github.com/phalanx-hk/kaggle_cv_pipeline/blob/master/kaggle_tips.md): 事前知識・取り組み方・参考リンク集をまとめた資料。
- [ディズニーがPyTorchでアニメキャラクター顔認識に取り組む記事](https://medium.com/pytorch/how-disney-uses-pytorch-for-animated-character-recognition-a1722a182627): データセット拡張や高速化のための試行錯誤を紹介。
- [画像データ水増し手法まとめ記事（TensorFlow実装）](https://app.wandb.ai/authors/tfaugmentation/reports/Modern-Data-Augmentation-Techniques-for-Computer-Vision--VmlldzoxODA3NTQ): 検証結果も掲載するデータ拡張手法の紹介。
- [画像認識のための深層学習サーベイ資料](https://www.slideshare.net/ren4yu/ss-234439652): モデルアーキテクチャの歴史や高速化手法を紹介。
- [「YOTO」を不均衡データ画像分類に適用する記事](https://st1990.hatenablog.com/entry/2020/05/04/012738): Class Balanced Loss に YOTO（ICLR2020, Google）を適用した検証。
- [「ReZero is All You Need」論文の概説記事](https://st1990.hatenablog.com/entry/2020/03/29/144230): CIFAR-10 で効果を確認した検証も掲載。
- [画像タスクの精度向上手法解説動画（U-Net・HRNetなど）](https://www.youtube.com/watch?v=05qlCP-xL9Y&feature=youtu.be): 複数解像度を扱う CNN アーキテクチャの紹介。
- [CNNが画像の位置情報を学習しているか検証した論文のまとめスライド](https://www.slideshare.net/KazuyukiMiyazawa/how-much-position-information-do-convolutional-neural-networks-encode): 位置情報学習に必要な要素を実験で指摘。

## 関連概念

- [画像認識コンペ](./image-recognition.md) / [LLM・自然言語処理の技術動向](./nlp-llm-trends.md) / [PyTorch](./pytorch.md)
