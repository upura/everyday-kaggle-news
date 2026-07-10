# 自然言語処理・LLM コンペ

自然言語処理のコンペは、BERT/DeBERTa 系の fine-tuning を定跡としつつ、近年は LLM の活用(生成・データ拡張・RAG)へと重心が移っています。
コードコンペ形式が多く、推論の高速化・省メモリ化もスコアに直結します。

## 押さえどころ

- BERT 系 fine-tuning の定跡: custom header(pooling・1D convolution・層別 [CLS] 連結)、層ごとの学習率設定、最終層付近の再初期化([AI Shift の Tips 記事](https://www.ai-shift.co.jp/techblog/2145))
- 2023〜24 年の NLP コンペでは「LLM によるデータ生成・水増し」「DeBERTa-v3」「損失関数・Pooling の工夫」が主要な精度向上手段。金と銀の差はタスク固有の後処理・データ処理にあり、普遍的な必勝法はない
- LLM コンペはエンジニアリング要素が強い。小さなデータで LLM の出力を確認してから、プロンプト最適化・モデル選択・RAG へ段階的に取り組む([LLMコンペの戦い方](https://qiita.com/Isaka-code/items/82e73fb6e77ac62a2287))
- 推論高速化は vLLM が定番。量子化(AWQ)や Auto Prefix Caching の併用で、コードコンペの実行時間制限に対応できる

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
- [RAG開発の超入門【RaggleのQuickStart Pythonのソースコードあり】](https://zenn.dev/galirage/articles/raggle_quickstart)
- [言語処理100本ノック 2025](https://nlp100.github.io/2025/ja/index.html)

## 関連概念

- [AI エージェント活用](./ai-agent.md) / [コードコンペティション](./code-competition.md) / [画像認識コンペ](./image-recognition.md)
