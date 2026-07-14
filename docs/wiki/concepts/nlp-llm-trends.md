# LLM・自然言語処理の技術動向

LLM・自然言語処理分野のモデル公開、日本語リソース、ライブラリ、研究サーベイの動向をまとめます。
コンペでの実践的な戦い方・定跡は [自然言語処理コンペ](./nlp-llm.md) を参照してください。

## 押さえどころ

- 日本語 LLM・埋め込みモデルのエコシステムは、大学・企業の研究機関による公開が牽引してきた（東北大 BERT、Swallow、PLaMo、rinna、ELYZA など）。近年は軽量・高速なモデル（TinySwallow、StaticEmbedding、日本語リランカー）の公開も増えている
- Hugging Face Transformers を中心にライブラリのメジャーバージョンが積み重なっており、新しいアーキテクチャ（Wav2Vec2、xFormers、Mamba 系など）の追加が動向を追う目安になる
- モデルサイズや学習コストのスケーリング則、モデルマージ・LoRA などのパラメータ効率的な適応手法が継続的な研究テーマになっている

## 資料

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

- [自然言語処理コンペ](./nlp-llm.md) / [画像認識・視覚モデルの技術動向](./image-recognition-trends.md) / [PyTorch](./pytorch.md)
