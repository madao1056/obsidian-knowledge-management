# Cursorフォルダ

## 目的
100_cursorフォルダは、CursorとObsidianの連携に関するすべての設定、ルール、ワークフローを管理する場所です。自動化、効率化、品質管理の中枢を担います。

## コンテンツ構成

### ドキュメント体系
```
101_フォルダ構造.md
├── 101-01_Inboxフォルダ.md
├── 101-02_Literatureフォルダ.md
├── 101-03_Permanentフォルダ.md
├── 101-04_Shareフォルダ.md
├── 101-05_Indexフォルダ.md
├── 101-06_Cursorフォルダ.md
├── 101-07_添付ファイル管理.md
└── 101-08_ファイル命名規則.md
```

### ワークフロー管理
```
102_ワークフロー.md
├── 102-01_ユースケース.md
└── 102-02_効率化テクニック.md

110_ワークフロー.md
├── 110-01_InboxをLiteratureに整理するワークフロー.md
├── 110-02_LiteratureをPermanentに昇華するワークフロー.md
└── 110-03_記事執筆ワークフロー.md
```

### 自動化・管理
```
103_自動化ルール.md
104_Git管理.md
105_タグ管理.md
└── 105-01_タグリスト.md
```

## スクリプト・ツール

### process_clip.py
- **機能**: clipフォルダの自動整理
- **処理**:
  - コンテンツタイプ判定
  - メタデータ抽出
  - サマリー生成
  - 適切なフォルダへ移動

### clip_workflow.md
- clip自動整理の詳細ドキュメント
- 使用方法とファイルフォーマット

## Cursor連携のメリット

### 1. 自動化
- 繰り返しタスクの自動化
- コンテンツ整理の効率化
- メタデータの一貫性

### 2. 品質管理
- フォーマットの統一
- タグ付けの一貫性
- 構造化データの維持

### 3. スケーラビリティ
- 大量コンテンツの処理
- ワークフローの拡張性
- AI統合の可能性

## 今後の拡張計画

### 短期（0-3ヶ月）
- AI API統合によるサマリー品質向上
- バッチ処理機能
- エラーハンドリング強化

### 中期（3-6ヶ月）
- バージョン管理統合
- コラボレーション機能
- テンプレートシステム

### 長期（6ヶ月以上）
- 機械学習による分類精度向上
- ナレッジグラフ構築
- インテリジェントリコメンデーション

## ベストプラクティス

1. **ドキュメントファースト**
   - すべてのルールを文書化
   - 変更履歴の記録
   - テンプレートの活用

2. **漸進的改善**
   - 小さな改善の積み重ね
   - フィードバックループ
   - 定期的な見直し

3. **再利用性**
   - モジュール化
   - パラメータ化
   - 抽象化

## 関連ドキュメント
- [[README]] - ルートディレクトリ
- [[process_clip.py]] - 自動整理スクリプト
- [[clip_workflow.md]] - clipワークフロー