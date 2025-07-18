# Notion連携セットアップガイド

## 📋 概要

Discord月報で共有されたNotionリンクの内容を自動的に取得し、メンバー管理フォルダに保存する機能です。

## 🔧 セットアップ手順

### 1. Notion APIキーの取得

1. [https://www.notion.so/my-integrations](https://www.notion.so/my-integrations) にアクセス
2. 「New integration」をクリック
3. 以下を入力：
   - **Name**: グッサポ・ラボ連携（任意の名前）
   - **Associated workspace**: 対象のワークスペースを選択
4. 「Submit」をクリック
5. **Internal Integration Token**をコピー

### 2. 環境変数の設定

#### Macの場合
```bash
# ~/.zshrcまたは~/.bash_profileに追加
export NOTION_API_KEY="secret_xxxxxxxxxxxxxxxxxxxxx"
```

#### 一時的に設定する場合
```bash
export NOTION_API_KEY="secret_xxxxxxxxxxxxxxxxxxxxx"
```

### 3. 必要なライブラリのインストール

```bash
pip install notion-client
```

### 4. Notionページへのアクセス許可

各Notionページでインテグレーションを許可する必要があります：

1. 共有したいNotionページを開く
2. 右上の「...」メニューをクリック
3. 「Add connections」を選択
4. 作成したインテグレーション（グッサポ・ラボ連携）を選択
5. 「Confirm」をクリック

## 🚀 使用方法

### 自動処理（月報生成時）

月報生成時に自動的にNotionリンクが処理されます：

```bash
python3 monthly_report_analyzer.py 2025 7
```

### 手動処理

特定のメッセージからNotionリンクを抽出する場合：

```python
from notion_integration import NotionIntegration

# 初期化
notion = NotionIntegration()

# メッセージからリンクを処理
message = "詳細はこちら: https://notion.so/page-123abc"
results = notion.process_discord_message(message)

# メンバーフォルダに保存
notion.save_notion_content("yukari", results)
```

## 📁 出力ファイル構造

```
メンバー管理/
└── yukari/
    └── Notion資料/
        ├── Notion資料_サマリー.md    # 資料一覧
        ├── 01_案件進捗表.md          # 個別ページ
        └── 02_月次レポート.md        # 個別ページ
```

## ⚠️ 注意事項

1. **APIキーの管理**
   - APIキーは絶対に公開しないでください
   - Gitにコミットしないよう注意

2. **アクセス権限**
   - 各ページで明示的にインテグレーションを許可する必要があります
   - プライベートページは許可しない限りアクセスできません

3. **レート制限**
   - Notion APIには制限があります（3リクエスト/秒）
   - 大量のページを処理する場合は時間がかかります

## 🔍 トラブルシューティング

### "unauthorized"エラーが出る場合

1. APIキーが正しく設定されているか確認
2. 対象ページでインテグレーションが許可されているか確認

### notion-clientがインストールできない場合

```bash
# 仮想環境を使用
python3 -m venv venv
source venv/bin/activate
pip install notion-client
```

### 環境変数が認識されない場合

```bash
# 設定を再読み込み
source ~/.zshrc
# または
source ~/.bash_profile
```

## 📝 メンテナンス

### ログの確認

処理状況は標準出力に表示されます。詳細なログが必要な場合：

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### 定期的な確認事項

1. APIキーの有効性
2. インテグレーションの権限
3. 処理エラーの有無

---
*最終更新: 2025年7月18日*