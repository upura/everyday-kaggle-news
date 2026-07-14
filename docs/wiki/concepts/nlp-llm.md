# 自然言語処理コンペ

自然言語処理のコンペは、BERT/DeBERTa 系の fine-tuning を定跡としつつ、近年は LLM の活用（生成、データ拡張、RAG）へと重心が移っています。
コードコンペ形式が多く、推論の高速化や省メモリ化もスコアに直結します。技術動向やモデル・ライブラリの一覧は [LLM・自然言語処理の技術動向](./nlp-llm-trends.md) を参照してください。

## 押さえどころ

- BERT 系 fine-tuning の定跡は、custom header（pooling、1D convolution、層別 [CLS] 連結）、層ごとの学習率設定、最終層付近の再初期化（[AI Shift の Tips 記事](https://www.ai-shift.co.jp/techblog/2145)）。加えて敵対的学習（FGM・AWP、[調査資料](https://www.slideshare.net/ssuserc45ddf/adversarial-trainingpptx)）や back-translation・EDA（Easy Data Augmentation）によるデータ拡張、ラベルなしデータへの Pseudo Labeling も上位解法で繰り返し登場する精度向上の定番手法
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

## 関連概念

- [LLM・自然言語処理の技術動向](./nlp-llm-trends.md) / [AI エージェント活用](./ai-agent.md) / [コードコンペティション](./code-competition.md) / [画像認識コンペ](./image-recognition.md) / [音声コンペ](./audio.md) / [コンペ形式・技術動向の変遷](./competition-evolution.md)
