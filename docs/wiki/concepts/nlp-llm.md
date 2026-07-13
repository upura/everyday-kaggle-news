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
- [RAG開発の超入門【RaggleのQuickStart Pythonのソースコードあり】](https://zenn.dev/galirage/articles/raggle_quickstart)
- [Kaggle自然言語処理コンペ向けローカルLLM活用入門](https://speakerdeck.com/k951286/kagglezi-ran-yan-yu-chu-li-konpexiang-kerokarullmhuo-yong-ru-men)
- [検索システム なぜ検索システムは欲しい情報を見つけられるのか、あるいはなぜ見つけられないのか](https://www.amazon.co.jp/dp/4065429714/): 検索の基本原理からランキング学習・検索拡張生成までを扱う書籍。
- [機械学習による検索ランキング改善ガイド](https://www.ohmsha.co.jp/book/9784814400300/): ランキング学習の導入と改善をハンズオンで学ぶ書籍。

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

### モデル・技術動向

- [DeepSeek-R1の論文読んだ？](https://zenn.dev/asap/articles/34237ad87f8511)
- [ModernBERT のブログを読んでみた感想](https://zenn.dev/dev_commune/articles/3f5ab431abdea1)
- [Introducing LFM2.5: The Next Generation of On-Device AI](https://www.liquid.ai/blog/introducing-lfm2-5-the-next-generation-of-on-device-ai): 日本語特化モデルや視覚言語モデルを含む小規模モデル群 LFM2.5 の公開告知。
- [【2026年版】 ベクトル検索と Embedding 最前線](https://speakerdeck.com/mocobeta/2026nian-ban-bekutorujian-suo-embeddingzui-qian-xian): ベクトル検索と埋め込みモデルの動向をまとめた資料。次元削減や量子化などの技法にも触れる。
- [Transformers v5.0.0rc0](https://github.com/huggingface/transformers/releases/tag/v5.0.0rc0): Transformers ライブラリ 5 年ぶりのメジャー更新のプレビュー版リリースノート。
- [fast-bunkai](https://github.com/hotchpotch/fast-bunkai): 日本語文境界判定器 Bunkai の高速版。Rust 実装で大幅な高速化を実現。
- [LLM×強化学習の新しいパラダイム: Agentic RLの研究紹介](https://zenn.dev/kuto5046/articles/agentic_rl_2025): サーベイ論文をもとに LLM への強化学習の最新動向を紹介する記事。
- [LoRAの進化：基礎から最新のLoRA-Proまで](https://zenn.dev/mkj/articles/11168509d10eb4): fine-tuning で頻出の LoRA の基礎と研究動向のまとめ。
- [[輪講資料] LoRA: Low-Rank Adaptation of Large Language Models](https://speakerdeck.com/hpprc/lun-jiang-zi-liao-lora-low-rank-adaptation-of-large-language-models): LoRA の原論文の解説資料。NLP の変遷の紹介つき。
- [Hugging Faceでload_dataset()できなくなったときの対処](https://qiita.com/tetsuro731/items/783afb42f9a36787262b): datasets ライブラリの仕様変更で発生するエラーへの対処記事。
- [Generative or Discriminative? Revisiting Text Classification in the Era of Transformers](https://aclanthology.org/2025.emnlp-main.486/): テキスト分類の識別的・生成的アプローチを包括比較した EMNLP 2025 Outstanding Paper。
- [T5Gemma: A new collection of encoder-decoder Gemma models](https://developers.googleblog.com/en/t5gemma/): デコーダ LLM の成果を還元したエンコーダ・デコーダモデル群の公開告知。
- [とても小さく速く実用的な日本語リランカー japanese-reranker-tiny と xsmall v2 を公開](https://secon.dev/entry/2025/05/08/100000-japanese-reranker-v2/): 軽量な日本語リランカーの公開告知。性能と推論速度の比較つき。
- [単文字トークナイザ版日本語ModernBERTリリース](https://qiita.com/KoichiYasuoka/items/a402d8111f7e3a69a54f): 文字単位トークナイザの日本語 ModernBERT の公開告知。
- [sbintuitions/modernbert-ja-130m](https://huggingface.co/sbintuitions/modernbert-ja-130m): 従来の最良水準を 3 分の 1 のサイズで達成した日本語 ModernBERT モデル。
- [新手法「TAID」を用いた小規模日本語言語モデル「TinySwallow-1.5B」の公開](https://sakana.ai/taid-jp/): 知識蒸留の新手法 TAID による小規模日本語 LLM の公開告知。
- [100倍速で実用的な文章ベクトルを作れる、日本語 StaticEmbedding モデルを公開](https://secon.dev/entry/2025/01/21/060000-static-embedding-japanese/): CPU でも高速な日本語文章ベクトルモデルの紹介。性能比較とコードつき。
- [日本語版 Gemma 2 2B を公開](https://blog.google/intl/ja-jp/company-news/technology/gemma-2-2b/): Gemma Developer Day in Tokyo で発表された日本語版 Gemma 2 の公開告知。
- [Training and Finetuning Embedding Models with Sentence Transformers v3](https://huggingface.co/blog/train-sentence-transformers): 文埋め込みライブラリ v3 での学習方法の解説記事。
- [日本語テキスト埋め込みベンチマークJMTEBの構築](https://www.sbintuitions.co.jp/blog/entry/2024/05/16/130848): 6 タスク・16 データセットの日本語埋め込みベンチマークの紹介。
- [ku-nlp/deberta-v3-base-japanese](https://huggingface.co/ku-nlp/deberta-v3-base-japanese): 日本語・英語・コードで事前学習された DeBERTa v3 モデルの公開。
- [Evolutionary Optimization of Model Merging Recipes (2024/04/17, NLPコロキウム)](https://speakerdeck.com/iwiwi/17-nlpkorokiumu): 進化的アルゴリズムでモデルの重みを混ぜる手法の発表資料。
- [Deep State Space Models 101 / Mamba](https://speakerdeck.com/kurita/mamba): 長系列処理に秀でたアーキテクチャ Mamba の解説資料。
- [Swallow](https://tokyotech-llm.github.io/swallow-llama): 公開当時に日本語最高性能を報告した東工大・産総研による日本語 LLM。
- [izumi-lab/deberta-v2-base-japanese](https://huggingface.co/izumi-lab/deberta-v2-base-japanese): 日本語で事前学習された DeBERTa v2 モデル（base / small）。
- [日英2言語対応の大規模言語モデルPLaMo-13Bを研究・商用利用可能なオープンソースソフトウェアライセンスで公開](https://www.preferred.jp/ja/news/pr20230928/): PFN による日英 LLM の公開告知。
- [Metaの「Llama 2」をベースとした商用利用可能な日本語LLM「ELYZA-japanese-Llama-2-7b」を公開しました](https://note.com/elyza/n/na405acaca130): Llama 2 を日本語で追加事前学習したモデルの公開告知。
- [日本語大規模言語モデル OpenCALM の知識でクイズ王に挑戦する](https://aws.amazon.com/jp/blogs/news/open-calm-and-openai-chatgpt-accuracy-on-jaqket-experiment-in-amazon-sagemaker/): クイズデータセットで日本語 LLM の性能と fine-tuning 費用を検証した記事。
- [サイバーエージェント、最大68億パラメータの日本語LLM（大規模言語モデル）を一般公開](https://www.cyberagent.co.jp/news/detail/id=28817): 商用利用可能な日本語 LLM（OpenCALM）の公開告知。同日に rinna も 36 億パラメータのモデルを公開。
- [cl-tohoku / bert-japanese](https://github.com/cl-tohoku/bert-japanese): 東北大学の日本語 BERT。コンペの定番モデルとして広く使われた。
- [日本語T5モデルの公開](https://note.com/retrieva/n/n7b4186dc5ada): レトリバによる 10 種の日本語 T5 モデルの公開告知。
- [ChatGPT vs BERT：どちらが日本語をより理解できるのか？](https://fintan.jp/page/9126/): JGLUE ベンチマークで ChatGPT と BERT 系を比較した検証記事。
- [最先端の質問応答技術の研究開発と迅速な実用化ーStudio Ousiaでの取り組みー](https://speakerdeck.com/ikuyamada/zui-xian-duan-nozhi-wen-ying-da-ji-shu-noyan-jiu-kai-fa-toxun-su-nashi-yong-hua-studio-ousiadenoqu-rizu-mi): 質問応答技術の研究開発とコンペでの取り組みの解説資料。
- [NLPとVision-and-Languageの基礎・最新動向 (1) / DEIM Tutorial Part 1: NLP](https://speakerdeck.com/kyoun/deim-tutorial-part-1-nlp): NLP と Vision & Language の基礎・最新動向を扱うチュートリアル資料。
- [ディープラーニングによる自然言語処理](https://www.kyoritsu-pub.co.jp/book/b10030620.html): 事前学習済みモデル LUKE の著者らによる自然言語処理の書籍。
- [Cohereの多言語用の埋め込みモデルを日本語で評価してみる](https://hironsan.hatenablog.com/entry/2023/11/06/133504): 多言語埋め込みモデルの日本語性能を文類似度と検索で評価した記事。
- [Improving Text Embeddings with Large Language Models](https://arxiv.org/abs/2401.00368): LLM の合成データで埋め込みモデルを改善する論文。e5-mistral モデル公開つき。
- [近似最近傍探索ライブラリVoyagerで類似単語検索を試す](https://zenn.dev/chimuichimu/articles/bab071c182784c): Spotify 公開の ANN ライブラリを Annoy と比較する検証記事。

## 関連概念

- [AI エージェント活用](./ai-agent.md) / [コードコンペティション](./code-competition.md) / [画像認識コンペ](./image-recognition.md) / [音声コンペ](./audio.md)
