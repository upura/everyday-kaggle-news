# 自然言語処理コンペ

自然言語処理のコンペは、BERT/DeBERTa 系の fine-tuning を定跡としつつ、近年は LLM の活用(生成、データ拡張、RAG)へと重心が移っています。
コードコンペ形式が多く、推論の高速化や省メモリ化もスコアに直結します。

## 押さえどころ

- BERT 系 fine-tuning の定跡は、custom header(pooling、1D convolution、層別 [CLS] 連結)、層ごとの学習率設定、最終層付近の再初期化([AI Shift の Tips 記事](https://www.ai-shift.co.jp/techblog/2145))
- 2023〜24 年の NLP コンペでは「LLM によるデータ生成や水増し」「DeBERTa-v3」「損失関数や Pooling の工夫」が主要な精度向上手段。金と銀の差はタスク固有の後処理やデータ処理にあり、普遍的な必勝法はない
- LLM コンペはエンジニアリング要素が強い。小さなデータで LLM の出力を確認してから、プロンプト最適化、モデル選択、RAG へ段階的に取り組む([LLMコンペの戦い方](https://qiita.com/Isaka-code/items/82e73fb6e77ac62a2287))
- 推論高速化は vLLM が定番。量子化(AWQ)や Auto Prefix Caching の併用で、コードコンペの実行時間制限に対応できる
- 2025 年にはエンコーダ型からデコーダ型 LLM への移行が明確になり、大型賞金コンペの優勝解法は Qwen 系が席巻した。評価環境内での学習(テスト時 fine-tuning)やタスクあたりの金銭コストといった新しい制約も登場している([The State of Machine Learning Competitions 2025](https://mlcontests.com/state-of-machine-learning-competitions-2025/))

## 資料

- [Kaggleで学んだBERTをfine-tuningする際のTips②〜精度改善編〜](https://www.ai-shift.co.jp/techblog/2145): custom header・層別学習率・再初期化など、fine-tuning の精度改善テクニックを実験付きで解説。
- [2023-24年（上期）のKaggleコンペから学ぶ、NLPコンペの精度の上げ方](https://zenn.dev/nishimoto/articles/974f2a445f9d74): 複数の NLP コンペ上位解法を横断し、精度向上の共通パターンを抽出した記事。
- [LLMコンペの戦い方](https://qiita.com/Isaka-code/items/82e73fb6e77ac62a2287): LLM コンペの特徴と、初心者が段階的に取り組むためのロードマップ。
- [vLLMを利用したLLM推論高速化テクニック](https://acro-engineer.hatenablog.com/entry/2024/12/24/120000): vLLM・量子化・Prefix Caching による推論高速化を実測値付きで紹介。
- [Kaggle自然言語処理コンペ向けローカルLLM活用入門](https://speakerdeck.com/k951286/kagglezi-ran-yan-yu-chu-li-konpexiang-kerokarullmhuo-yong-ru-men)
- [【第3回】関東Kaggler会「NLPの変遷とNLPコンペの最新事情 〜進化する技術と変化する戦い方〜」](https://speakerdeck.com/takaito/di-3hui-guan-dong-kagglerhui-nlpnobian-qian-tonlpkonpenozui-xin-shi-qing-jin-hua-suruji-shu-tobian-hua-suruzhan-ifang)
- [プロンプトエンジニアリングの手法、Kaggleでの使われ方 まとめ](https://speakerdeck.com/sinchir0/puronputoenziniaringunoshou-fa-kaggledenoshi-warefang-matome)
- [DeepSeek-R1の論文読んだ？](https://zenn.dev/asap/articles/34237ad87f8511)
- [ModernBERT のブログを読んでみた感想](https://zenn.dev/dev_commune/articles/3f5ab431abdea1)
- [Introducing LFM2.5: The Next Generation of On-Device AI](https://www.liquid.ai/blog/introducing-lfm2-5-the-next-generation-of-on-device-ai): 日本語特化モデルや視覚言語モデルを含む小規模モデル群 LFM2.5 の公開告知。
- [RAG開発の超入門【RaggleのQuickStart Pythonのソースコードあり】](https://zenn.dev/galirage/articles/raggle_quickstart)
- [【2026年版】 ベクトル検索と Embedding 最前線](https://speakerdeck.com/mocobeta/2026nian-ban-bekutorujian-suo-embeddingzui-qian-xian): ベクトル検索と埋め込みモデルの動向をまとめた資料。次元削減や量子化などの技法にも触れる。
- [検索システム なぜ検索システムは欲しい情報を見つけられるのか、あるいはなぜ見つけられないのか](https://www.amazon.co.jp/dp/4065429714/): 検索の基本原理からランキング学習・検索拡張生成までを扱う書籍。
- [LLM性能改善の実践知 Kaggleでの学びを現場に活かす思考法](https://speakerdeck.com/sinchir0/llmxing-neng-gai-shan-noshi-jian-zhi-kaggledenoxue-biwoxian-chang-nihuo-kasusi-kao-fa): 『Kaggleではじめる大規模言語モデル入門』4・5 章を題材にした LLM 性能改善の発表資料。
- [言語処理100本ノック 2025](https://nlp100.github.io/2025/ja/index.html)
- [Transformers v5.0.0rc0](https://github.com/huggingface/transformers/releases/tag/v5.0.0rc0): Transformers ライブラリ 5 年ぶりのメジャー更新のプレビュー版リリースノート。

## 関連概念

- [AI エージェント活用](./ai-agent.md) / [コードコンペティション](./code-competition.md) / [画像認識コンペ](./image-recognition.md) / [音声コンペ](./audio.md)
