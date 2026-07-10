# AI エージェント活用

Claude Code などの LLM エージェントにコンペ作業を任せる新しい潮流です。
ベースライン構築や過去解法の調査は自動化が進む一方、上位に食い込むには人間による問題定義とモデル改善がまだ必要とされています。

## 押さえどころ

- エージェント任せでも「上位 30% 程度」のモデルは作れるが、メダル圏には届かない。人間の役割はデータ整備、問題定義、モデル改善へシフトする([Claude Code と Kaggle をやったら何も考えずに上位30%になれた話](https://zenn.dev/genda_jp/articles/20250909_kaggle_with_claude_code))
- 過去コンペの上位解法を調査してレポートさせる使い方は、コンペ序盤のサーベイを大きく効率化する
- エージェントと協働するには、実験の再現性と記録が前提になる([実験管理](./experiment-management.md))
- ノートブックのクラッシュを集めたベンチマーク(JunoBench)など、エージェントの評価基盤も整備されつつある

## 資料

- [Claude Code と Kaggle をやったら何も考えずに上位30%になれた話](https://zenn.dev/genda_jp/articles/20250909_kaggle_with_claude_code): エージェントに任せた場合の到達点と限界、MLflow・GitHub を使った協働体制の実験報告。
- [Kaggle過去コンペ上位解法をAIエージェントでレポートする](https://speakerdeck.com/kuto5046/kaggleguo-qu-konpeshang-wei-jie-fa-woaiezientoderepotosuru)
- [NVIDIA Kaggle Plugin](https://github.com/NVIDIA/nvidia-kaggle): Kaggle の公開解法を収集するコーディングエージェント向けプラグイン。過去解法サーベイの自動化に使える。
- [JunoBench: Crashes in Python ML Jupyter Notebooks](https://arxiv.org/abs/2510.18013v1): Kaggle 由来の再現可能なノートブックのクラッシュ 111 件を集めたベンチマークの論文。

## 関連概念

- [自然言語処理コンペ](./nlp-llm.md) / [実験管理](./experiment-management.md)
