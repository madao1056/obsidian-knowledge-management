# notion_sync_env 仮想環境 使用ガイド

## 📋 概要

既存の`notion_sync_env`仮想環境を使ってNotion連携機能を利用する方法です。

## 🔧 セットアップ手順

### 1. 仮想環境のアクティベート

```bash
# プロジェクトディレクトリに移動
cd /Users/hashiguchimasaki/project/obsidian

# 仮想環境をアクティベート
source notion_sync_env/bin/activate
```

### 2. 必要なパッケージのインストール

```bash
# notion-clientをインストール
pip install notion-client

# その他の依存関係（必要に応じて）
pip install requests urllib3 certifi
```

### 3. 環境変数の設定

```bash
# Notion APIキーを設定
export NOTION_API_KEY="secret_1A2B3C4D5E6F7G8H9I0J..."

# 設定確認
echo $NOTION_API_KEY
```

### 4. 環境のテスト

```bash
# 環境テストを実行
python3 100_discord_sync/test_notion_env.py
```

## 🚀 使用方法

### 月報生成（Notion連携込み）

```bash
# 仮想環境をアクティベート
source notion_sync_env/bin/activate

# 2025年7月の月報を生成
python3 100_discord_sync/monthly_report_analyzer.py 2025 7
```

### 手動でNotionリンクを処理

```bash
# 仮想環境をアクティベート
source notion_sync_env/bin/activate

# Pythonスクリプトを実行
python3 -c "
from 100_discord_sync.notion_integration import NotionIntegration
notion = NotionIntegration()
print('Notion連携準備完了！')
"
```

## 📁 ディレクトリ構造

```
obsidian/
├── notion_sync_env/          # 仮想環境（既存）
│   ├── bin/
│   │   ├── activate          # アクティベートスクリプト
│   │   └── python3           # Python実行ファイル
│   ├── lib/
│   │   └── python3.13/
│   │       └── site-packages/ # インストール済みパッケージ
│   └── pyvenv.cfg
└── 100_discord_sync/         # Discord連携スクリプト
    ├── notion_integration.py
    ├── monthly_report_analyzer.py
    └── test_notion_env.py
```

## ⚙️ 自動化スクリプト例

### シェルスクリプトでの自動実行

```bash
#!/bin/bash
# run_notion_sync.sh

# プロジェクトディレクトリに移動
cd /Users/hashiguchimasaki/project/obsidian

# 仮想環境をアクティベート
source notion_sync_env/bin/activate

# 環境変数を設定（セキュアな場所から読み込み推奨）
export NOTION_API_KEY="$YOUR_NOTION_API_KEY"

# 月報生成
python3 100_discord_sync/monthly_report_analyzer.py 2025 7

echo "✅ Notion連携付き月報生成完了"
```

### crontabでの定期実行

```bash
# crontab -e で追加
# 毎月1日午前3時に実行
0 3 1 * * cd /Users/hashiguchimasaki/project/obsidian && source notion_sync_env/bin/activate && export NOTION_API_KEY="your-key" && python3 100_discord_sync/monthly_report_analyzer.py
```

## 🔍 トラブルシューティング

### 仮想環境がアクティベートできない

```bash
# パーミッションの確認
ls -la notion_sync_env/bin/activate

# 実行権限を付与
chmod +x notion_sync_env/bin/activate
```

### パッケージがインストールできない

```bash
# pipのアップグレード
pip install --upgrade pip

# 個別インストール
pip install --no-cache-dir notion-client
```

### 環境変数が認識されない

```bash
# 現在のシェルで確認
env | grep NOTION

# .zshrcや.bash_profileに追加
echo 'export NOTION_API_KEY="your-key"' >> ~/.zshrc
source ~/.zshrc
```

## 💡 Tips

### 1. 環境の切り替え

```bash
# 仮想環境を無効化
deactivate

# 別の仮想環境をアクティベート
source other_env/bin/activate
```

### 2. パッケージ一覧の確認

```bash
# インストール済みパッケージを確認
pip list

# 特定パッケージの確認
pip show notion-client
```

### 3. 環境のバックアップ

```bash
# requirements.txtを生成
pip freeze > requirements.txt

# 環境の再現
pip install -r requirements.txt
```

## 🔐 セキュリティ注意事項

1. **APIキーの管理**
   - 環境変数で管理
   - Gitにコミットしない
   - 定期的に更新

2. **仮想環境の保護**
   - 適切なパーミッション設定
   - 不要なパッケージは削除

---
*最終更新: 2025年7月18日*