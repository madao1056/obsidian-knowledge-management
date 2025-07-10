# Obsidian Knowledge Management System

ObsidianとCursorを連携させた自動化された知識管理システムです。

## 🎯 特徴

- **自動整理**: Webクリップを自動的に分類・整理
- **タグ管理**: 包括的なタグ分析システム
- **リンクチェック**: 内部リンクの整合性を自動チェック
- **Daily Note**: 毎日のノートを自動生成
- **Git統合**: バージョン管理とバックアップ

## 📁 フォルダ構造

```
obsidian/
├── 00_Inbox/          # 一時的な情報保管
│   └── clip/         # Webクリップ用（自動整理対象）
├── 20_Literature/     # 外部情報ストック
│   ├── 21_Books/     # 書籍情報
│   ├── 22_Articles/  # 記事・ブログ
│   ├── 23_Videos/    # 動画コンテンツ
│   ├── 24_SNS/       # SNS情報
│   └── 29_Other/     # その他
├── 30_Permanent/      # 自分の言葉で再構築
│   ├── 31_Philosophy/# 哲学・思想
│   ├── 32_Tech/      # 技術関連
│   ├── 33_Productivity/# 生産性
│   ├── 34_Product/   # プロダクト
│   └── 35_AI/        # AI関連
├── 70_Share/          # 公開用コンテンツ
│   ├── 71_Internal/  # 内部共有
│   ├── 75_Blog/      # ブログ記事
│   ├── 78_Personal/  # 個人用
│   └── 79_Public/    # 公開用
├── 90_Index/          # MOC・タグ一覧
├── 100_cursor/        # ルール・ワークフロー
└── attachments/       # 添付ファイル
```

## 🚀 クイックスタート

### 1. リポジトリのクローン
```bash
git clone https://github.com/madao1056/obsidian-knowledge-management.git
cd obsidian-knowledge-management
```

### 2. Obsidianで開く
Obsidianを起動し、クローンしたフォルダをVaultとして開きます。

### 3. 自動整理の実行
```bash
# Clipフォルダの自動整理
python3 100_cursor/process_clip.py

# または、Claude Codeで
"クリップを整理して"
```

## 🔧 主要機能

### 1. Clip自動整理（process_clip.py）
- `00_Inbox/clip`内のファイルを自動分類
- メタデータ抽出とサマリー生成
- 適切な`20_Literature`サブフォルダへ移動

### 2. タグ分析（tag_analyzer.py）
```bash
python3 100_cursor/tag_analyzer.py
```
- タグ使用頻度分析
- 類似タグの検出
- 階層構造の可視化

### 3. リンクチェック（link_checker.py）
```bash
python3 100_cursor/link_checker.py
```
- 内部リンクの整合性チェック
- 壊れたリンクの検出と修正案提示

### 4. Daily Note生成（daily_note_generator.py）
```bash
python3 100_cursor/daily_note_generator.py
```
- テンプレートベースの日次ノート作成
- 前後の日付へのリンク自動生成

## 📝 ワークフロー

### 基本フロー
1. **収集**: 情報を`00_Inbox/clip`に保存
2. **整理**: 自動スクリプトで`20_Literature`へ分類
3. **昇華**: 学習内容を`30_Permanent`へ手動昇華
4. **活用**: `70_Share`で記事やコンテンツ作成

### 日次タスク
- Daily Note作成
- Inbox整理（clipフォルダ処理）
- Literature読み返し

### 週次タスク
- タグ分析実行
- リンクチェック
- MOC更新

## 🛠 カスタマイズ

### テンプレート
`100_cursor/templates/`内のテンプレートをカスタマイズ可能：
- daily_note_template.md
- literature_template.md
- permanent_template.md
- project_template.md
- meeting_template.md
- moc_template.md

### 自動化ルール
`100_cursor/`内のPythonスクリプトを編集して動作をカスタマイズできます。

## 📚 ドキュメント

詳細なドキュメントは`100_cursor/`フォルダ内にあります：
- 101シリーズ: フォルダ構造とルール
- 102シリーズ: ワークフローと効率化
- 103-105シリーズ: 自動化・Git・タグ管理
- 110シリーズ: 具体的なワークフロー

## 🔍 トラブルシューティング

### ログ確認
```bash
ls 100_cursor/logs/
```

### バックアップ確認
```bash
ls 100_cursor/backup/
```

### レポート確認
```bash
ls 100_cursor/reports/
```

## 🤝 貢献

プルリクエストや改善提案を歓迎します！

## 📄 ライセンス

MIT License

## 🙏 謝辞

このシステムはObsidianの強力な機能とPythonの自動化を組み合わせて構築されています。

---

**作成者**: [@madao1056](https://github.com/madao1056)  
**最終更新**: 2025-07-11