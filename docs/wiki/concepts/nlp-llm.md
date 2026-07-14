# 自然言語処理コンペ

自然言語処理のコンペは、BERT/DeBERTa 系の fine-tuning を定跡としつつ、近年は LLM の活用（生成、データ拡張、RAG）へと重心が移っています。
コードコンペ形式が多く、推論の高速化や省メモリ化もスコアに直結します。

## 押さえどころ

- BERT 系 fine-tuning の定跡は、custom header（pooling、1D convolution、層別 [CLS] 連結）、層ごとの学習率設定、最終層付近の再初期化（[AI Shift の Tips 記事](https://www.ai-shift.co.jp/techblog/2145)）
- 2023〜24 年の NLP コンペでは「LLM によるデータ生成や水増し」「DeBERTa-v3」「損失関数や Pooling の工夫」が主要な精度向上手段。金と銀の差はタスク固有の後処理やデータ処理にあり、普遍的な必勝法はない
- LLM コンペはエンジニアリング要素が強い。小さなデータで LLM の出力を確認してから、プロンプト最適化、モデル選択、RAG へ段階的に取り組む（[LLMコンペの戦い方](https://qiita.com/Isaka-code/items/82e73fb6e77ac62a2287)）
- 推論高速化は vLLM が定番。量子化（AWQ）や Auto Prefix Caching の併用で、コードコンペの実行時間制限に対応できる
- 2025 年にはエンコーダ型からデコーダ型 LLM への移行が明確になり、大型賞金コンペの優勝解法は Qwen 系が席巻した。評価環境内での学習（テスト時 fine-tuning）やタスクあたりの金銭コストといった新しい制約も登場している（[The State of Machine Learning Competitions 2025](https://mlcontests.com/state-of-machine-learning-competitions-2025/)）

## 資料

### 入門・基礎

- [大規模言語モデル (LLM) 入門](https://speakerdeck.com/rist/da-gui-mo-yan-yu-moderu-llm-ru-men): Kaggle Grandmaster による大学講義向けの LLM 入門資料。
- [CMU Advanced NLP Fall 2024](https://www.youtube.com/playlist?list=PL8PYTP1V4I8D4BeyjwWczukWq9d8PNyZp): カーネギーメロン大学の NLP 講義動画。講義資料も公開されている。
- [LLM 大規模言語モデル講座 2023コンテンツ 公開ページ](https://weblab.t.u-tokyo.ac.jp/llm_contents/): 事前学習から強化学習まで扱う東大松尾研の講義資料。
- [大規模言語モデル](https://speakerdeck.com/chokkan/llm): LLM の進展をまとめた 167 ページのチュートリアル資料。
- [大規模言語モデル入門](https://www.amazon.co.jp/dp/4297136333): LLM の基礎から要約・質問応答モデルの作成までを扱う書籍。
- [情報処理学会関西支部2024年度定期講演会「自然言語処理と大規模言語モデルの基礎」](https://speakerdeck.com/ksudoh/qing-bao-chu-li-xue-hui-guan-xi-zhi-bu-2024nian-du-ding-qi-jiang-yan-hui-zi-ran-yan-yu-chu-li-toda-gui-mo-yan-yu-moderunoji-chu): LLM 登場までの自然言語処理の潮流と課題を解説する講演資料。
- [大規模言語モデル (LLM) の技術と最新動向](https://speakerdeck.com/ikuyamada/da-gui-mo-yan-yu-moderu-llm-noji-shu-tozui-xin-dong-xiang): LLM 構築の流れと技術背景を解説する資料。『大規模言語モデル入門Ⅱ』著者による。
- [言語処理100本ノック 2025](https://nlp100.github.io/2025/ja/index.html)
- [文書分類からはじめる自然言語処理入門 基本からBERTまで](https://www.amazon.co.jp/%E6%96%87%E6%9B%B8%E5%88%86%E9%A1%9E%E3%81%8B%E3%82%89%E3%81%AF%E3%81%98%E3%82%81%E3%82%8B%E8%87%AA%E7%84%B6%E8%A8%80%E8%AA%9E%E5%87%A6%E7%90%86%E5%85%A5%E9%96%80-%E5%9F%BA%E6%9C%AC%E3%81%8B%E3%82%89BERT%E3%81%BE%E3%81%A7-%E8%A8%AD%E8%A8%88%E6%8A%80%E8%A1%93%E3%82%B7%E3%83%AA%E3%83%BC%E3%82%BA108-%E6%96%B0%E7%B4%8D-%E6%B5%A9%E5%B9%B8/dp/4910558144): 伝統的な手法から BERT まで幅広く扱う文書分類の書籍。
- [自然言語処理の基礎（深層学習編）](https://www.ohmsha.co.jp/book/9784274229008/): 深層学習に基づく自然言語処理の基礎知識・考え方をまとめた書籍。
- [最先端の自然言語処理ライブラリのためのTransformers（日本語版）](https://www.amazon.co.jp/%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%8B%E3%82%A2%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AETransformers-%E2%80%95%E6%9C%80%E5%85%88%E7%AB%AF%E3%81%AE%E8%87%AA%E7%84%B6%E8%A8%80%E8%AA%9E%E5%87%A6%E7%90%86%E3%83%A9%E3%82%A4%E3%83%96%E3%83%A9%E3%83%AA%E3%81%AB%E3%82%88%E3%82%8B%E3%83%A2%E3%83%87%E3%83%AB%E9%96%8B%E7%99%BA-Lewis-Tunstall/dp/4873119952): Hugging Face 共同創業者らによる Transformers 解説書の日本語版。
- [Hugging Faceが公開する学習講座の紹介](https://hiromu-nlp.com/huggingface-course-intro/): 自然言語処理ライブラリを開発する Hugging Face の公式学習講座の紹介記事。
- [NLPとVision-and-Languageの基礎・最新動向をまとめたチュートリアル](https://speakerdeck.com/kyoun/a-tutorial-on-nlp-and-vision-and-language): 自然言語処理と、画像と合わせて扱う領域への発展をまとめた資料。
- [深層学習と自然言語処理の研究動向（東大講座資料）](https://speakerdeck.com/verypluming/dong-jing-da-xue-shen-ceng-xue-xi-deep-learningji-chu-jiang-zuo-2022-shen-ceng-xue-xi-tozi-ran-yan-yu-chu-li): 深層学習と自然言語処理の研究動向を概説する講座資料。
- [Transformers for Natural Language Processing（日本語訳書）](https://www.amazon.co.jp/Transformer%E3%81%AB%E3%82%88%E3%82%8B%E8%87%AA%E7%84%B6%E8%A8%80%E8%AA%9E%E5%87%A6%E7%90%86-Denis-Rothman/dp/4254122659): アーキテクチャ紹介から GPT-3 によるテキスト生成まで扱う書籍。
- [Natural Language Processing with Transformers（原著）](https://transformersbook.com/): Hugging Face 共同創業者らによる Transformers 解説書。サンプルコードを GitHub で公開。
- [系列ラベリングの理論とJAX実装を扱う技術書（技術書典12）](https://techbookfest.org/product/6195059194068992): 数式の展開も含めて系列ラベリングを解説する同人技術書。
- [RAG開発の超入門【RaggleのQuickStart Pythonのソースコードあり】](https://zenn.dev/galirage/articles/raggle_quickstart)
- [Kaggle自然言語処理コンペ向けローカルLLM活用入門](https://speakerdeck.com/k951286/kagglezi-ran-yan-yu-chu-li-konpexiang-kerokarullmhuo-yong-ru-men)
- [検索システム なぜ検索システムは欲しい情報を見つけられるのか、あるいはなぜ見つけられないのか](https://www.amazon.co.jp/dp/4065429714/): 検索の基本原理からランキング学習・検索拡張生成までを扱う書籍。
- [機械学習による検索ランキング改善ガイド](https://www.ohmsha.co.jp/book/9784814400300/): ランキング学習の導入と改善をハンズオンで学ぶ書籍。
- [30分で完全理解するTransformerの世界](https://zenn.dev/zenkigen/articles/2023-01-shimizu): サーベイ論文をもとに Transformer 機構を解説する記事。
- [イントロダクション（Hugging Face Course 日本語訳）](https://huggingface.co/course/ja/chapter1/1): Hugging Face 公式コースの日本語訳。東北大学の学生による翻訳プロジェクト。
- [情報検索100本ノック](https://github.com/ir100/ir100): 情報検索の課題を集めた「100 本ノック」形式の演習教材。
- [『深層学習』改訂第2版（講談社）発売告知](https://www.hanmoto.com/bd/isbn/9784065133323): Transformer やグラフニューラルネットワークなどを大幅加筆した定番書籍の改訂版。
- [「Approaching (Almost) Any Natural Language Processing Problem」公開予告](https://github.com/abhishekkrthakur/approaching_almost_nlp): Abhishek Thakur さんによる NLP 実践書の構想公開ページ。
- [Hugging Face入門講座公開](https://huggingface.co/course/chapter1): ライブラリの使い方を中心に基礎的な内容を紹介する公式講座。
- [BERTによる日本語自然言語処理の書籍出版予告（Transformers活用）](https://www.ohmsha.co.jp/book/9784274227264/): 学習コードに PyTorch Lightning を利用する書籍の出版告知。
- [Transformer解説資料（図解中心）](https://speakerdeck.com/yusuketakagi/transformerhahe-woyatuteirufalseka): データの流れを図で説明する解説資料。
- [Transformer機構の調査資料（基礎解説・画像認識応用）](https://www.slideshare.net/cvpaperchallenge/transformer-247407256): 基礎的な解説から画像認識分野への応用までをまとめた資料。
- [Transformers書籍のプレビュー版公開（O'Reilly）](https://www.oreilly.com/library/view/natural-language-processing/9781098103231/): Hugging Face 共同創設者 Thomas Wolf さんも共著者に名を連ねる書籍。
- [Transformerの解説記事（RNNとの比較）](https://blog.brainpad.co.jp/entry/2021/01/06/113000): 応用例も含めて紹介する入門記事。
- [自然言語処理タスク向けGoogle Colabリンク集「Super Duper NLP Repo」](https://medium.com/towards-artificial-intelligence/nlp-colab-repository-65136d3e45da): 41 ファイルの新規追加を含む紹介記事。
- [東大松尾研「Deep Learning基礎講座」招待講演資料（自然言語処理領域）](https://www.slideshare.net/HitomiYanaka/2020deep-learning-9-236561673): 深層学習前後の NLP 領域を概観し近年の研究課題までまとめた資料。
- [BERTを中心にした自然言語処理モデル解説Podcast](https://anchor.fm/pod-de-engineer/episodes/BERT-with-agatan-ebijrr/a-a1n58q9): 音声のみで端的に BERT を紹介する分かりやすい構成。
- [Attention機構の解説動画](https://www.youtube.com/watch?v=g5DSLeJozdw&feature=youtu.be): ニューラルネットワークの基本構造をわかりやすく解説する動画。
- [自然言語処理のEmbedding手法解説記事（USE・BERTなど）](https://yukoishizaki.hatenablog.com/entry/2020/01/03/175156): 学習済みモデルからベクトルを取得するサンプルコードつき。
- [BERTの特徴・Pre-training・モデル構造の可視化資料](https://www.slideshare.net/matsukenbook/bert-217710964): transformers ライブラリの実装をもとにした丁寧な図解資料。

### コンペの定跡

- [Kaggleで学んだBERTをfine-tuningする際のTips②〜精度改善編〜](https://www.ai-shift.co.jp/techblog/2145): custom header・層別学習率・再初期化など、fine-tuning の精度改善テクニックを実験付きで解説。
- [Kaggleで学んだBERTをfine-tuningする際のTips⑥〜LLMでも使える学習効率化編〜](https://www.ai-shift.co.jp/techblog/3609): LLM にも使える学習効率化手法を実験付きで紹介する連載第 6 回。
- [BERT系モデルで文章をEmbeddingする際のTips](https://qiita.com/anyai_corp/items/1d66feea6102c28dd077): BERT による文章埋め込みの手法をコード付きで検証する記事。
- [LLMとLoRAを用いたテキスト分類](https://github.com/hppRC/llm-lora-classification): LoRA で fine-tuning した GPT 系モデルの日本語分類性能の報告。
- [BERT Classification Tutorial](https://github.com/hppRC/bert-classification-tutorial): 日本語データでの BERT 分類チュートリアル。事前学習済みモデルの性能比較つき。
- [sparse_dot_topnを使った高速なcos類似度計算](https://www.ai-shift.co.jp/techblog/3557): 検索タスクのコサイン類似度計算を高速化する手法の紹介。コンペ優勝解法でも利用。
- [Scikit-LLM: Sklearn Meets Large Language Models](https://medium.com/@fareedkhandev/scikit-llm-sklearn-meets-large-language-models-11fc6f30e530): scikit-learn 風のインターフェースで LLM テキスト分類ができるライブラリの紹介。
- [2023-24年（上期）のKaggleコンペから学ぶ、NLPコンペの精度の上げ方](https://zenn.dev/nishimoto/articles/974f2a445f9d74): 複数の NLP コンペ上位解法を横断し、精度向上の共通パターンを抽出した記事。
- [LLMコンペの戦い方](https://qiita.com/Isaka-code/items/82e73fb6e77ac62a2287): LLM コンペの特徴と、初心者が段階的に取り組むためのロードマップ。
- [vLLMを利用したLLM推論高速化テクニック](https://acro-engineer.hatenablog.com/entry/2024/12/24/120000): vLLM・量子化・Prefix Caching による推論高速化を実測値付きで紹介。
- [第4回 関東Kaggler会 [Training LLMs with Limited VRAM]](https://speakerdeck.com/tascj/di-4hui-guan-dong-kagglerhui-training-llms-with-limited-vram): 限られた VRAM で LLM を学習する技法をまとめた Kaggle Grandmaster の発表資料。
- [プロンプトエンジニアリングの手法、Kaggleでの使われ方 まとめ](https://speakerdeck.com/sinchir0/puronputoenziniaringunoshou-fa-kaggledenoshi-warefang-matome)
- [KaggleのNLPコンペで初手に使える可視化 〜BERTopicを用いた文書クラスタリングと可視化〜](https://zenn.dev/nishimoto/articles/74fddcb5c67960): NLP コンペの EDA を想定した BERTopic による文書可視化の紹介。
- [学習なし！遺伝的アルゴリズムと反省（？）でLLMを強化する話](https://speakerdeck.com/analokmaus/xue-xi-nasi-yi-chuan-arugorizumutozi-ji-dui-hua-de-llmwoqiang-hua-suruhua): 遺伝的アルゴリズムによるプロンプト最適化手法の紹介資料。
- [LogitsProcessorZoo で LLM の出力をコントロールする](https://zenn.dev/prgckwb/articles/logits-processor-zoo-explain): 多肢選択問題での出力候補の絞り込みなど、LLM の出力制御ライブラリの紹介。
- [Kaggle Kernel で Gemma 2 × vLLM を動かす。](https://speakerdeck.com/kohecchi/kaggle-kernel-de-gemma-2-x-vllm-wodong-kasu): Kaggle 環境上で Gemma 2 を vLLM で高速に動かす方法の紹介。公開 Notebook つき。
- [airllmを使ってT4で70B LLMの推論を実行してみる](https://www.ai-shift.co.jp/techblog/4162): 層ごとの推論で小規模 GPU でも大規模 LLM を動かすライブラリの紹介。
- [Transformers高速化ライブラリvLLMのAsyncLLMEngineを利用した非同期高速文章生成](https://hashicco.hatenablog.com/entry/2024/07/06/165959): AIMO コンペの Discussion を題材にした vLLM の非同期生成の紹介。
- [LLM性能改善の実践知 Kaggleでの学びを現場に活かす思考法](https://speakerdeck.com/sinchir0/llmxing-neng-gai-shan-noshi-jian-zhi-kaggledenoxue-biwoxian-chang-nihuo-kasusi-kao-fa): 『Kaggleではじめる大規模言語モデル入門』4・5 章を題材にした LLM 性能改善の発表資料。
- [【第3回】関東Kaggler会「NLPの変遷とNLPコンペの最新事情 〜進化する技術と変化する戦い方〜」](https://speakerdeck.com/takaito/di-3hui-guan-dong-kagglerhui-nlpnobian-qian-tonlpkonpenozui-xin-shi-qing-jin-hua-suruji-shu-tobian-hua-suruzhan-ifang)
- [敵対的学習手法「FGM」「AWP」の解説記事](https://blog.brainpad.co.jp/entry/2022/08/23/153001): NLP コンペで頻出する敵対的学習手法を解説。
- [Nishika 個人情報固有表現抽出データセット・モデル公開](https://info.nishika.com/solution-cl-data/personal-inquiry): 判例の個人情報自動マスキング向けに、商用利用可のデータセットとコンペ解法を基にしたモデル・ソースコードを公開。
- [Hugging Faceのモデル評価ライブラリ「evaluate」の紹介](https://hiromu-nlp.com/huggingface-evaluate/): 具体的な使い方をソースコードと共に紹介。
- [自然言語処理コンペの上位解法に登場する「敵対的学習」の調査資料](https://www.slideshare.net/ssuserc45ddf/adversarial-trainingpptx): 過学習を防ぎモデルの頑健性を高める効果を整理した資料。
- [Adversarial Training（敵対的学習）に関する近年の動向まとめ](https://speakerdeck.com/hirokiadachi/sabei-adversarial-training): 実験に用いたソースコードも公開する動向まとめ資料。
- [Transformers ライブラリでの推論をONNX形式で高速化する記事](https://tech.retrieva.jp/entry/20220228): 約 2.4 倍の高速化を報告する検証記事。
- [Transformers に強化学習モデル「Decision Transformer」が追加](https://huggingface.co/blog/decision-transformers): チュートリアル用のソースコードと解説も公開。
- [Data2vec: A General Framework for Self-supervised Learning in Speech, Vision, and Language 解説資料](https://www.slideshare.net/DeepLearningJP2016/dldata2vec-a-general-framework-for-selfsupervised-learning-in-speech-vision-and-language-251106954): 音声・画像・自然言語を同一枠組みで扱う自己教師あり学習手法の解説。
- [日本語データ拡張ライブラリ](https://kajyuuen.hatenablog.com/entry/2022/02/14/094602): 置換や削除といった処理で文を拡張するライブラリの紹介記事。
- [2021年のML/NLP研究動向まとめ（15の観点）](https://ruder.io/ml-highlights-2021/): 何が起きたか・なぜ重要か・次は何かを観点別に整理した記事。
- [Transformer モデルの仕組みを JAX/Flax で実装しながら解説してみる（パート１）](https://enakai00.hatenablog.com/entry/2023/02/10/102036): Transformer を JAX/Flax で実装しながら解説する連載記事。
- [ファインチューンせずに高速に学習できる RAPIDS SVR (SVC) の紹介と MARC-ja の評価](https://secon.dev/entry/2022/12/13/090000-rapids-svr-svc-marc-ja/): Feedback Prize 上位解法で使われた RAPIDS SVR の紹介と日本語データでの検証。
- [scikit-learnで5行でできる類似テキスト検索](https://zenn.dev/colum2131/articles/e178e20be6171e): scikit-learn による類似テキスト検索と GPU 活用の紹介記事。
- [【AI Shift/Kaggle Advent Calendar 2022】Kaggleで学んだBERTをfine-tuningする際のTips④〜Adversarial Training編〜](https://www.ai-shift.co.jp/techblog/2985): NLP コンペで使われる Adversarial Training の解説記事。
- [【AI Shift Advent Calendar 2022】SetFitによるfew-shotテキスト分類](https://www.ai-shift.co.jp/techblog/2931): 少量データで学習できる SetFit の紹介記事。Disaster Tweets で検証。
- [敵対学習手法(AWP)の論文解説と実装解説](https://speakerdeck.com/masakiaota/kaggledeshi-yong-sarerudi-dui-xue-xi-fang-fa-awpnolun-wen-jie-shuo-toshi-zhuang-jie-shuo-adversarial-weight-perturbation-helps-robust-generalization): NLP コンペで使われる敵対学習手法 AWP の解説と実装。
- [Kaggleで学んだBERTをfine-tuningする際のTips⑤〜ラベルなしデータ活用編〜](https://www.ai-shift.co.jp/techblog/3161): Pseudo Labeling と追加事前学習によるラベルなしデータ活用の連載第 5 回。
- [2021年NLPコンペ上位解法に共通する手法・方針の解説記事](https://qiita.com/cfiken/items/0890269721fb78bd9683): アンサンブルや外部データ利用などの事例をまとめた記事。
- [FlaxでTPU上のBERTをファインチューニングする解説記事](https://www.ai-shift.co.jp/techblog/2209): Kaggle「CommonLit Readability Prize」を題材にした解説記事。
- [CommonLit Readability Prizeを題材にしたBERT学習効率化Tips記事](https://www.ai-shift.co.jp/techblog/2138): 近年のコンペで使われる効率化手法を紹介。
- [BERTファインチューニングでの過学習抑制Tips記事（CommonLit）](https://www.ai-shift.co.jp/techblog/2170): ドロップアウト関連の手法や議論を紹介。
- [学習済みTransformerモデルを用いたデータ拡張の記事](https://www.ai-shift.co.jp/techblog/1939): 隠された単語を予測する仕組みで新しい文を生成する手法の紹介。
- [日本語対応ライブラリ「AutoNLP」での文書分類記事](https://www.ai-shift.co.jp/techblog/1880): 線形回帰・BERT との性能比較も掲載。
- [Transformer解説記事（Riiid実装例つき）](https://qiita.com/birdwatcher/items/b3e4428f63f708db37b7): 丁寧な図解と、Kaggle「Riiid Answer Correctness Prediction」を題材にした実装例。
- [NVIDIA Kaggle Grandmasterによる自然言語処理コンペ解説動画](https://www.youtube.com/watch?v=PXc_SlnT2g0&feature=youtu.be): Transformers ライブラリの解説と直近コンペの解法紹介。
- [日本語データ水増し手法の実装記事（EDA）](https://qiita.com/tchih11/items/aef9505d26d1bf06a04c): 英文向け手法「Easy Data Augmentation」を日本語に応用。
- [Rustを用いた自然言語処理・機械学習の取り組み記事](https://vaaaaaanquish.hatenablog.com/entry/2020/12/14/192246): ニュース本文から媒体を分類するタスクへの挑戦。
- [Real or Not? NLP with Disaster Tweetsを題材にしたFastaiチュートリアル](https://harish3110.github.io/through-tinted-lenses/natural%20language%20processing/sentiment%20analysis/2020/06/27/Introduction-to-NLP-using-Fastai.html): データ可視化から予測までの流れをまとめた記事。
- [KerasのCNNで文書2値分類の特徴を可視化するチュートリアル](https://towardsdatascience.com/viewing-text-through-the-eyes-of-a-machine-db30c744ee17?gi=c98845badcb6): 予測結果分析に使える可視化手法。
- [NLPにおけるデータ水増し手法のまとめ記事](https://amitness.com/2020/05/data-augmentation-for-nlp/): 語彙変換・翻訳・表層・交叉などを図示。
- [文書分類コンペ5つを題材にしたTipsまとめ記事](https://neptune.ai/blog/text-classification-tips-and-tricks-kaggle-competitions): 前処理・モデリング・アンサンブルの観点別に整理。
- [BERT質問応答モデルのデータ前処理解説動画](https://www.youtube.com/watch?v=6a6L_9USZxg&feature=youtu.be): RoBERTa などへの切り替え方法も紹介。
- [日本語BERTモデルをPyTorchでfine-tuningするチュートリアル](https://radiology-nlp.hatenablog.com/entry/2020/01/18/013039): SentencePiece ベースモデルを題材にした各ステップの丁寧な解説。
- [「Real or Not? NLP with Disaster Tweets」BERTベースラインNotebook](https://www.kaggle.com/bibek777/bert-baseline): PyTorch の transformers ライブラリによる Fine-tuning から予測までの一連の流れ。

### モデル・技術動向

- [Introducing LFM2.5: The Next Generation of On-Device AI](https://www.liquid.ai/blog/introducing-lfm2-5-the-next-generation-of-on-device-ai): 日本語特化モデルや視覚言語モデルを含む小規模モデル群 LFM2.5 の公開告知。
- [LoRAの進化：基礎から最新のLoRA-Proまで](https://zenn.dev/mkj/articles/11168509d10eb4): fine-tuning で頻出の LoRA の基礎と研究動向のまとめ。
- [[輪講資料] LoRA: Low-Rank Adaptation of Large Language Models](https://speakerdeck.com/hpprc/lun-jiang-zi-liao-lora-low-rank-adaptation-of-large-language-models): LoRA の原論文の解説資料。NLP の変遷の紹介つき。
- [T5Gemma: A new collection of encoder-decoder Gemma models](https://developers.googleblog.com/en/t5gemma/): デコーダ LLM の成果を還元したエンコーダ・デコーダモデル群の公開告知。
- [Evolutionary Optimization of Model Merging Recipes (2024/04/17, NLPコロキウム)](https://speakerdeck.com/iwiwi/17-nlpkorokiumu): 進化的アルゴリズムでモデルの重みを混ぜる手法の発表資料。
- [Deep State Space Models 101 / Mamba](https://speakerdeck.com/kurita/mamba): 長系列処理に秀でたアーキテクチャ Mamba の解説資料。
- [ディープラーニングによる自然言語処理](https://www.kyoritsu-pub.co.jp/book/b10030620.html): 事前学習済みモデル LUKE の著者らによる自然言語処理の書籍。
- [DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing](https://retarfi.hatenablog.jp/entry/2022/12/15/090815): NLP コンペ頻出モデル DeBERTaV3 の論文解説記事。
- [Word Tour: One-dimensional Word Embeddings via the Traveling Salesman Problem](https://www.jstage.jst.go.jp/article/jnlp/29/4/29_1297/_article/-char/ja): 単語を 1 次元に埋め込む手法の論文解説。Kaggle での活用例に言及。
- [世界最高精度を達成した言語モデルLUKEの論文を徹底解説](https://qiita.com/Mizuiro__sakura/items/9ccbd655501e78df5cc6): 言語モデル LUKE の論文解説。日本語 large モデル公開時の記事。
- [hppRC / simple-simcse](https://github.com/hppRC/simple-simcse): 文埋め込み手法 SimCSE の再現実装。複数モデルでの性能比較つき。
- [BERTを用いた教師なし文表現の発展](https://tech.retrieva.jp/entry/20221028): SimCSE の発展系 DiffCSE の紹介記事。
- [Box Embeddingの解説](https://ja.stateofaiguides.com/20221013-box-embeddings/): データを箱として表現し埋め込みを学習する Box Embedding の解説記事。
- [Improving Text Embeddings with Large Language Models](https://arxiv.org/abs/2401.00368): LLM の合成データで埋め込みモデルを改善する論文。e5-mistral モデル公開つき。
- [Word Tour: One-dimensional Word Embeddings via the Traveling Salesman Problem（NAACL 2022 発表資料）](https://www.slideshare.net/joisino/word-tour-onedimensional-word-embeddings-via-the-traveling-salesman-problem-naacl-2022): 高次元の単語埋め込みを巡回セールスマン問題で 1 次元に変換する手法の発表資料。
- [Transformerの汎用的な性能向上に向けた方法論](https://speakerdeck.com/butsugiri/yoriliang-itransformerwotukuru): 位置表現や注意機構、追試結果に言及した資料。
- [OPT-175B 公開](https://ai.facebook.com/blog/democratizing-access-to-large-scale-language-models-with-opt-175b/): Meta AI による 175B パラメータの言語モデル公開。構築の試行錯誤の過程も公開。
- [Data2vec: 音声・画像・自然言語を統一的に扱う自己教師あり学習の解説記事（Meta AI公式）](https://ai.facebook.com/blog/the-first-high-performance-self-supervised-algorithm-that-works-for-speech-vision-and-text): 事前学習済みモデルも公開。
- [マルチタスク学習で有用なタスクを選ぶ手法の解説記事（NeurIPS 2021）](https://ai.googleblog.com/2021/10/deciding-which-tasks-should-train.html): 「Efficiently Identifying Task Groupings for Multi-Task Learning」の紹介。
- [教師なし文表現作成手法「SimCSE」の解説記事](https://tech.retrieva.jp/entry/2021/10/12/130850): 日本語ニュース記事での実験結果も掲載。
- [新たな言語モデル「FLAN」の発表（Google Research）](https://ai.googleblog.com/2021/10/introducing-flan-more-generalizable.html): 実験で GPT-3 を上回る性能を報告。
- [BERT推論高速化手法の検証記事（量子化・蒸留・剪定）](https://tech.jxpress.net/entry/2021/08/26/170000): 詳細な実験結果と共に紹介する記事。
- [SparseBERT: Rethinking the Importance Analysis in Self-attention 解説記事（ICML2021）](https://tech.retrieva.jp/entry/2021/07/29/094758): BERT の注意機構の軽量化に取り組む論文の解説。
- [Transformerのサーベイ論文（体系的分類）](https://arxiv.org/abs/2106.04554): Transformer の解説と派生系の分類方法を提唱する論文。
- [Transformerの一種「Big Bird」の紹介記事](https://tech.retrieva.jp/entry/2021/04/28/172553): 長文を扱うための注意機構の工夫を解説。
- [Transformerのスケーリング則を主張する論文の紹介](https://deeplearning.hatenablog.com/entry/scaling_law): パラメータ数・データセットサイズ・計算予算の冪乗則を論じる OpenAI の論文。同時期に DALL·E も公開。
- [SBERT-WKの紹介記事](https://ai-scholar.tech/articles/natural-language-processing/sbert-wk): BERT の各層出力・分散を用いた文ベクトル生成手法の改良を背景から解説。
- [BERTOverflow公開（StackOverflowデータで事前学習）](https://huggingface.co/lanwuwei/BERTOverflow_stackoverflow_github): ACL 2020 採択論文が提案するモデルの公開。
- [Googleの多言語埋め込みモデル「LaBSE」に関する記事](https://hironsan.hatenablog.com/entry/text-classification-with-labse): 文章分類問題での性能を検証。Universal Sentence Encoder との比較記事も別途公開。
- [AMBERTの解説記事（バイトダンス）](https://towardsdatascience.com/ambert-a-multi-grained-bert-6564ed24bcc3?source=social.tw&gi=f0496fcb4092): 2 種類の粒度の tokenizer を使い分ける BERT 拡張モデルの解説。
- [Quoraの重複質問特定を題材にした論文](https://arxiv.org/abs/2004.11694): tf-idf ベクトル化 + XGBoost・深層学習など Kaggle でも馴染み深い手法を検証。
- [wikipediaの文化差異を捉えるBERT fine-tuning論文](https://arxiv.org/abs/2004.04938): 逆翻訳によるデータ拡張を用いた手法の紹介。

### 日本語モデル・リソース

- [とても小さく速く実用的な日本語リランカー japanese-reranker-tiny と xsmall v2 を公開](https://secon.dev/entry/2025/05/08/100000-japanese-reranker-v2/): 軽量な日本語リランカーの公開告知。性能と推論速度の比較つき。
- [単文字トークナイザ版日本語ModernBERTリリース](https://qiita.com/KoichiYasuoka/items/a402d8111f7e3a69a54f): 文字単位トークナイザの日本語 ModernBERT の公開告知。
- [sbintuitions/modernbert-ja-130m](https://huggingface.co/sbintuitions/modernbert-ja-130m): 従来の最良水準を 3 分の 1 のサイズで達成した日本語 ModernBERT モデル。
- [新手法「TAID」を用いた小規模日本語言語モデル「TinySwallow-1.5B」の公開](https://sakana.ai/taid-jp/): 知識蒸留の新手法 TAID による小規模日本語 LLM の公開告知。
- [100倍速で実用的な文章ベクトルを作れる、日本語 StaticEmbedding モデルを公開](https://secon.dev/entry/2025/01/21/060000-static-embedding-japanese/): CPU でも高速な日本語文章ベクトルモデルの紹介。性能比較とコードつき。
- [日本語版 Gemma 2 2B を公開](https://blog.google/intl/ja-jp/company-news/technology/gemma-2-2b/): Gemma Developer Day in Tokyo で発表された日本語版 Gemma 2 の公開告知。
- [日本語テキスト埋め込みベンチマークJMTEBの構築](https://www.sbintuitions.co.jp/blog/entry/2024/05/16/130848): 6 タスク・16 データセットの日本語埋め込みベンチマークの紹介。
- [ku-nlp/deberta-v3-base-japanese](https://huggingface.co/ku-nlp/deberta-v3-base-japanese): 日本語・英語・コードで事前学習された DeBERTa v3 モデルの公開。
- [Swallow](https://tokyotech-llm.github.io/swallow-llama): 公開当時に日本語最高性能を報告した東工大・産総研による日本語 LLM。
- [izumi-lab/deberta-v2-base-japanese](https://huggingface.co/izumi-lab/deberta-v2-base-japanese): 日本語で事前学習された DeBERTa v2 モデル（base / small）。
- [日英2言語対応の大規模言語モデルPLaMo-13Bを研究・商用利用可能なオープンソースソフトウェアライセンスで公開](https://www.preferred.jp/ja/news/pr20230928/): PFN による日英 LLM の公開告知。
- [Metaの「Llama 2」をベースとした商用利用可能な日本語LLM「ELYZA-japanese-Llama-2-7b」を公開しました](https://note.com/elyza/n/na405acaca130): Llama 2 を日本語で追加事前学習したモデルの公開告知。
- [日本語大規模言語モデル OpenCALM の知識でクイズ王に挑戦する](https://aws.amazon.com/jp/blogs/news/open-calm-and-openai-chatgpt-accuracy-on-jaqket-experiment-in-amazon-sagemaker/): クイズデータセットで日本語 LLM の性能と fine-tuning 費用を検証した記事。
- [サイバーエージェント、最大68億パラメータの日本語LLM（大規模言語モデル）を一般公開](https://www.cyberagent.co.jp/news/detail/id=28817): 商用利用可能な日本語 LLM（OpenCALM）の公開告知。同日に rinna も 36 億パラメータのモデルを公開。
- [cl-tohoku / bert-japanese](https://github.com/cl-tohoku/bert-japanese): 東北大学の日本語 BERT。コンペの定番モデルとして広く使われた。
- [日本語T5モデルの公開](https://note.com/retrieva/n/n7b4186dc5ada): レトリバによる 10 種の日本語 T5 モデルの公開告知。
- [roberta-long-japanese](https://huggingface.co/megagonlabs/roberta-long-japanese): 512 トークンを超える長系列を扱える日本語 RoBERTa モデル。
- [huggingface.co/abeja](https://huggingface.co/abeja): ABEJA が構築した日本語大規模言語モデルの公開。
- [ku-nlp/deberta-v2-large-japanese](https://huggingface.co/ku-nlp/deberta-v2-large-japanese): 京大黒橋研による日本語 DeBERTa V2（large）。当時最大級のコーパスで学習。
- [ku-nlp/deberta-v2-base-japanese](https://huggingface.co/ku-nlp/deberta-v2-base-japanese): 同モデルの base / tiny サイズ版。
- [ABEJAによる日本語版大規模言語モデル構築プロジェクト](https://tech-blog.abeja.asia/entry/abeja-gpt-project-202207): 一部モデルの一般公開を予定した日本語 LLM 構築の発表。
- [日本語言語理解ベンチマーク「JGLUE」公開](https://randd.yahoo.co.jp/jp/softwaredata#jglue): 日本語の事前学習済みモデルの性能比較も掲載。
- [deberta-large-japanese-aozora](https://huggingface.co/KoichiYasuoka): 青空文庫の文章などで事前学習された、日本語では珍しい DeBERTa のモデル。
- [日本語版 RoBERTa Large モデル公開](https://huggingface.co/nlp-waseda/roberta-large-japanese): 形態素解析器 Juman++ での分かち書きが必要な日本語 RoBERTa。
- [rinna 日本語GPT言語モデル公開](https://prtimes.jp/main/html/rd/p/000000025.000070041.html): 13 億パラメータの日本語特化 GPT モデルを MIT ライセンスで公開。
- [日本語Wikipediaで事前学習されたRoBERTa・GPT-2公開](https://huggingface.co/nlp-waseda/roberta-base-japanese): 形態素解析に Juman++ を利用する早稲田大学研究グループのモデル。
- [rinna日本語GPT-2・BERT公開、Megagon日本語T5公開](https://prtimes.jp/main/html/rd/p/000000017.000070041.html): 日本語特化の事前学習済みモデル群の公開告知。
- [日本語自然言語処理ライブラリ「GiNZA」開発者による日本語言語モデル構築の取り組み資料](https://docs.google.com/presentation/d/1zOUTIXBdw8MhGqCdvq3wn0n2UCfQ99gpkQDsvjb-Xbs/edit): 「WAP NLP Tech Talk #3 With GiNZA」での発表資料。
- [東北大学の日本語BERT largeがTransformersに追加](https://huggingface.co/cl-tohoku): 従来の BERT base より層数の多いモデルが利用可能に。
- [ELECTRAの日本語版モデル](https://cinnamon.is/ideas/2020/06/22/20200619_research_001/): ICLR 2020 発表モデルの日本語版公開。
- [日本語Wikipedia・青空文庫で事前学習されたBERTモデル公開（NICT）](https://alaginrc.nict.go.jp/nict-bert/index.html): 情報通信研究機構による日本語 BERT モデルの公開。
- [日本語word2vecモデルの評価記事](https://blog.hoxo-m.com/entry/2020/02/20/090000): 複数の学習済みモデルを日本語データセットで比較評価。

### ライブラリ・ツール

- [Transformers v5.0.0rc0](https://github.com/huggingface/transformers/releases/tag/v5.0.0rc0): Transformers ライブラリ 5 年ぶりのメジャー更新のプレビュー版リリースノート。
- [fast-bunkai](https://github.com/hotchpotch/fast-bunkai): 日本語文境界判定器 Bunkai の高速版。Rust 実装で大幅な高速化を実現。
- [Hugging Faceでload_dataset()できなくなったときの対処](https://qiita.com/tetsuro731/items/783afb42f9a36787262b): datasets ライブラリの仕様変更で発生するエラーへの対処記事。
- [Training and Finetuning Embedding Models with Sentence Transformers v3](https://huggingface.co/blog/train-sentence-transformers): 文埋め込みライブラリ v3 での学習方法の解説記事。
- [KWJA](https://github.com/ku-nlp/kwja): 形態素解析・構文解析などを統一インターフェースで扱う日本語処理ライブラリ。
- [近似最近傍探索ライブラリVoyagerで類似単語検索を試す](https://zenn.dev/chimuichimu/articles/bab071c182784c): Spotify 公開の ANN ライブラリを Annoy と比較する検証記事。
- [Transformers v4.19.0リリース](https://github.com/huggingface/transformers/releases/tag/v4.19.0): Meta 公開の OPT (Open Pre-trained Transformer Language Models) などを追加。
- [Transformers v4.18.0リリース](https://github.com/huggingface/transformers/releases/tag/v4.18.0): 画像認識分野の ResNet などが新たに追加。
- [Transformers v4.16.0リリース](https://github.com/huggingface/transformers/releases/tag/v4.16.0): 画像認識分野の Swin Transformer が新たに追加。
- [Transformer用最適化ライブラリ「xFormers」公開（Facebook Research）](https://github.com/facebookresearch/xformers): PyTorch ベースの Transformer 最適化実装ライブラリ。
- [テキスト前処理・可視化ライブラリ「Texthero」の紹介記事](https://buildersbox.corp-sansan.com/entry/2021/06/29/110000): 日本語対応のためのコードも掲載。
- [Hugging FaceとAmazonの提携発表](https://huggingface.co/blog/the-partnership-amazon-sagemaker-and-hugging-face): Amazon SageMaker 上に言語モデル構築向けインスタンスを提供。
- [Hugging Face「AutoNLP」ウェブサイト公開](https://huggingface.co/autonlp): 開発に関わる Kaggle Grandmaster Abhishek Thakur さんの解説動画も公開。
- [テキスト前処理ライブラリ「NLPretext」の紹介記事](https://medium.com/artefact-engineering-and-data-science/introducing-nlpretext-a8bb7c03df89): basic・social・token・augmentation の 4 要素で構成。
- [Transformers v4.3.0公開（Wav2Vec2）](https://github.com/huggingface/transformers/releases/tag/v4.3.0): Facebook の音声事前学習モデル Wav2Vec2 などを実装。
- [AllenNLP v2.0.0リリース](https://github.com/allenai/allennlp/releases/tag/v2.0.0): PyTorch ベースで構築された NLP ライブラリの大型更新。
- [Hugging Face「AutoNLP」公開予告](https://huggingface.typeform.com/to/FAtsVfbg): Kaggle 史上初の全 4 カテゴリ Grandmaster Abhishek Thakur さんによるプロジェクト。
- [Transformers v4.0.0-rc-1公開](https://github.com/huggingface/transformers/releases/tag/v4.0.0-rc-1): デフォルト tokenizer が高速な Rust 製に切り替わるなどの変更。
- [Transformers Trainerにハイパーパラメータ調整機能が実装](https://twitter.com/GuggerSylvain/status/1297948214214221825?s=20): Optuna・Ray Tune を利用可能に。
- [Hugging Faceがニューズレターを開始](https://huggingface.curated.co/issues/1): 21 日朝に配信された初回号。
- [日本語形態素解析器比較ライブラリ「toiro」](https://github.com/taishi-i/toiro): テキストダウンロードや分類器機能も備えるライブラリ。
- [自然言語処理モデル学習時間短縮の検証記事（transformers）](https://app.wandb.ai/pommedeterresautee/speed_training/reports/Train-HuggingFace-models-twice-as-fast--VmlldzoxMDgzOTI): トークン化バッチの工夫による高速化を検証。
- [「flair」ライブラリの紹介記事（日本語文書分類）](https://nmoriyama.hatenablog.com/entry/2020/07/10/160031): livedoor ニュースコーパスを用いた分類タスクの実践。
- [Sudachi・MeCabの形態素解析結果を比較する記事](http://tdual.hatenablog.com/entry/2020/07/13/162151): livedoor ニュースコーパスでの分類タスクを通じた比較。
- [Transformers v3.0リリース](https://github.com/huggingface/transformers/releases/tag/v3.0.0): ドキュメント刷新と新トークナイズ API を追加。
- [AllenNLP v1.0.0リリース](https://github.com/allenai/allennlp/releases/tag/v1.0.0): PyTorch ベースの NLP ライブラリ。Optuna との連携機能も用意。
- [spaCy v2.3.0リリース（日本語モデル追加）](https://explosion.ai/blog/spacy-v2-3/): 日本語向けチュートリアルも公開。
- [NLTKによる英語テキストの文分割・単語分割の解説記事](https://eieito.hatenablog.com/entry/2020/05/27/100000): スペース区切りでは対応できないケースを含めた詳細な解析。
- [Transformers v2.9.0リリース](https://github.com/huggingface/transformers/releases/tag/v2.9.0): PyTorch・TensorFlow 2 を同一インターフェースで扱う Trainer クラスが登場。
- [Hugging Faceがトークン化ライブラリ「Tokenizers」を公開](https://medium.com/dair-ai/hugging-face-introduces-tokenizers-d792482db360): Transformers と合わせて BERT などのモデルを使いやすくするライブラリ。
- [GPUでのNLP時「CUDA out of memory」回避Tips記事](https://qiita.com/shinochin/items/8b6b7e76bf426ab86444): Embedding layer を CPU に載せるなどのアイディアを列挙。

### 研究動向・サーベイ・イベント

- [DeepSeek-R1の論文読んだ？](https://zenn.dev/asap/articles/34237ad87f8511)
- [ModernBERT のブログを読んでみた感想](https://zenn.dev/dev_commune/articles/3f5ab431abdea1)
- [【2026年版】 ベクトル検索と Embedding 最前線](https://speakerdeck.com/mocobeta/2026nian-ban-bekutorujian-suo-embeddingzui-qian-xian): ベクトル検索と埋め込みモデルの動向をまとめた資料。次元削減や量子化などの技法にも触れる。
- [LLM×強化学習の新しいパラダイム: Agentic RLの研究紹介](https://zenn.dev/kuto5046/articles/agentic_rl_2025): サーベイ論文をもとに LLM への強化学習の最新動向を紹介する記事。
- [Generative or Discriminative? Revisiting Text Classification in the Era of Transformers](https://aclanthology.org/2025.emnlp-main.486/): テキスト分類の識別的・生成的アプローチを包括比較した EMNLP 2025 Outstanding Paper。
- [ChatGPT vs BERT：どちらが日本語をより理解できるのか？](https://fintan.jp/page/9126/): JGLUE ベンチマークで ChatGPT と BERT 系を比較した検証記事。
- [最先端の質問応答技術の研究開発と迅速な実用化ーStudio Ousiaでの取り組みー](https://speakerdeck.com/ikuyamada/zui-xian-duan-nozhi-wen-ying-da-ji-shu-noyan-jiu-kai-fa-toxun-su-nashi-yong-hua-studio-ousiadenoqu-rizu-mi): 質問応答技術の研究開発とコンペでの取り組みの解説資料。
- [NLPとVision-and-Languageの基礎・最新動向 (1) / DEIM Tutorial Part 1: NLP](https://speakerdeck.com/kyoun/deim-tutorial-part-1-nlp): NLP と Vision & Language の基礎・最新動向を扱うチュートリアル資料。
- [AI 激動の年！2022年の人工知能10大トレンドと必読論文](https://ja.stateofaiguides.com/20221231-ai-trends-2022/): 2022 年の AI 研究動向と参考文献のまとめ。基盤モデル関連の話題を多数含む。
- [Cohereの多言語用の埋め込みモデルを日本語で評価してみる](https://hironsan.hatenablog.com/entry/2023/11/06/133504): 多言語埋め込みモデルの日本語性能を文類似度と検索で評価した記事。
- [広範なデータで学習される「基盤モデル」のサーベイ資料](https://www.slideshare.net/cvpaperchallenge/foundation-models): 自然言語処理を起点に画像領域への展開などをまとめた資料。
- [大規模データで学習された「基盤モデル」の解説記事](https://blog.recruit.co.jp/data/articles/foundation_models/): BERT などの基盤モデルの概要・活用事例・課題を紹介。
- [医療分野のテキストで事前学習されたTransformersモデルの紹介](https://hiromu-nlp.com/transfomers-bio-models/): 医療関連コンペで活用できる事前学習モデルをまとめた記事。
- [自然言語処理領域での転移学習の進展と近年の動向まとめ](https://www.slideshare.net/techblogyahoo/ss-251672433): 132 ページにわたり多岐の話題を扱うサーベイ資料。
- [2021年の深層学習関連10大トピックまとめ](https://ja.stateofaiguides.com/20211230-ai-trends-2021/): 参考文献と共に大まかな流れを紹介する記事。
- [ニューラルネットワークによる自然言語処理の概観資料](https://www.slideshare.net/shotakase33/ss-250870067): 系列を扱う構造や学習方法、動向を紹介する資料。
- [ACL 2021ベストペーパーを日本語文書で検証する記事](https://tech.retrieva.jp/entry/2021/08/25/185920): 適切な語彙サイズを自動決定する枠組みの日本語検証。
- [近年の自然言語処理動向まとめ資料（汎用事前学習言語モデル観点）](https://speakerdeck.com/karakurist/nlp-survey): 様々な提案手法を簡単な説明と共に列挙した資料。
- [自然言語処理の事前学習済みモデルの動向まとめ記事](https://elyza-inc.hatenablog.com/entry/2021/03/25/160727): 研究の方向性を分類し、学習方法の観点で改良の流れを紹介。
- [2020年の機械学習・自然言語処理領域の総括記事（DeepMind研究者）](https://ruder.io/research-highlights-2020/): 言語モデルの巨大化・軽量化や少データ学習の展望も含めてまとめた記事。
- [「最先端NLP勉強会2020」発表資料集](https://sites.google.com/view/snlp-jp/home/2020): 著名な国際会議採択論文の紹介資料 30 件以上を公開。
- [ACL2020読み会 招待講演「半教師あり学習・疑似データ学習法の進展」](https://www.slideshare.net/AkihiroFujii2/2020-0906-acl2020readingshared): 不完全なデータを活用した性能向上手法をまとめた資料。
- [Yann LeCunさんによるself-supervised learning講演の要約記事（AAAI 2020）](https://bdtechtalks.com/2020/03/23/yann-lecun-self-supervised-learning/): BERT に代表される Transformers の成果と、深層学習研究が抱える課題を議論。
- [BERT応用勉強会の聴講メモ](https://upura.hatenablog.com/entry/2020/05/15/211833): 5 件の興味深い発表内容をまとめた記事。アーカイブ動画も公開。
- [BERT応用勉強会の開催告知](https://nlpaper-challenge.connpass.com/event/174957/?utm_campaign=event_participate_to_follower&utm_medium=twitter&utm_source=notifications): ドメイン活用事例やフロントエンド利用例を LT 形式で発表。

## 関連概念

- [AI エージェント活用](./ai-agent.md) / [コードコンペティション](./code-competition.md) / [画像認識コンペ](./image-recognition.md) / [音声コンペ](./audio.md)
