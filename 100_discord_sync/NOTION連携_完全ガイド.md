# Notion連携 完全ガイド

## 🎯 概要

グッサポ・ラボのDiscord-Obsidian連携システムにNotionを統合し、月報で共有された資料を自動取得・整理します。

## 📚 目次

1. [Notion API基礎知識](#notion-api基礎知識)
2. [セットアップ手順](#セットアップ手順)
3. [使用方法](#使用方法)
4. [トラブルシューティング](#トラブルシューティング)
5. [高度な設定](#高度な設定)
6. [セキュリティ考慮事項](#セキュリティ考慮事項)

## 📖 Notion API基礎知識

### APIの仕組み
- **認証**: Internal Integration Tokenを使用
- **権限**: ページごとにインテグレーションを明示的に許可する必要
- **制限**: 3リクエスト/秒のレート制限
- **データ形式**: JSON形式でページ情報を取得

### 取得可能な情報
- ページタイトル
- プロパティ（メタデータ）
- ブロック内容（テキスト、リスト、コードなど）
- 最終更新日時
- 作成日時

## 🔧 セットアップ手順

### Step 1: Notion Developersでインテグレーション作成

1. **Notion Developersにアクセス**
   ```
   https://www.notion.so/my-integrations
   ```

2. **新しいインテグレーション作成**
   - 「New integration」をクリック
   - **Name**: `グッサポ・ラボ連携` （任意）
   - **Associated workspace**: 対象ワークスペースを選択
   - **Type**: Internal（推奨）

3. **設定詳細**
   ```
   Name: グッサポ・ラボ連携
   Description: Discord月報からNotionページを自動取得
   Logo: （任意）
   Organization: （あれば設定）
   ```

4. **権限設定（Capabilities）**
   ```
   ✅ Read content
   ✅ Read user information (optional)
   ❌ Update content (不要)
   ❌ Insert content (不要)
   ```

### Step 2: APIキーの取得と保存

1. **Internal Integration Tokenをコピー**
   ```
   secret_1A2B3C4D5E6F7G8H9I0J...（32文字のランダム文字列）
   ```

2. **環境変数として設定**

   **macOS/Linux (Bash/Zsh):**
   ```bash
   # ~/.zshrc または ~/.bash_profile に追加
   export NOTION_API_KEY="secret_1A2B3C4D5E6F7G8H9I0J..."
   
   # 設定を反映
   source ~/.zshrc
   ```

   **Windows (PowerShell):**
   ```powershell
   # 一時的な設定
   $env:NOTION_API_KEY="secret_1A2B3C4D5E6F7G8H9I0J..."
   
   # 永続的な設定
   [Environment]::SetEnvironmentVariable("NOTION_API_KEY", "secret_...", "User")
   ```

   **Windows (Command Prompt):**
   ```cmd
   set NOTION_API_KEY=secret_1A2B3C4D5E6F7G8H9I0J...
   ```

3. **設定の確認**
   ```bash
   echo $NOTION_API_KEY
   # または
   python3 -c "import os; print(os.getenv('NOTION_API_KEY'))"
   ```

### Step 3: 必要なライブラリのインストール

```bash
# 推奨：仮想環境の作成
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# notion-clientのインストール
pip install notion-client

# その他必要なライブラリ
pip install requests urllib3
```

### Step 4: ページアクセス権限の設定

共有したい各Notionページで個別に設定が必要：

1. **ページを開く**
2. **右上の「Share」または「共有」をクリック**
3. **「Add people, emails, groups, or integrations」に移動**
4. **作成したインテグレーション（グッサポ・ラボ連携）を検索**
5. **インテグレーションを選択して「Invite」**
6. **権限レベルを確認**：
   - `Can read` または `読み取り可能` に設定

## 🚀 使用方法

### 1. 自動処理（推奨）

月報生成時に自動的にNotionリンクが処理されます：

```bash
# 2025年7月の月報を生成（Notionリンクも自動処理）
python3 monthly_report_analyzer.py 2025 7
```

### 2. 手動処理

特定のメッセージからNotionコンテンツを抽出：

```python
from notion_integration import NotionIntegration

# 初期化
notion = NotionIntegration()

# Discordメッセージの例
message = """
今月の進捗です。
詳細資料: https://www.notion.so/project-progress-abc123
設計書: https://notion.so/design-doc-def456
"""

# Notionコンテンツを処理
results = notion.process_discord_message(message)

# メンバーフォルダに保存
if results:
    notion.save_notion_content("yukari", results)
    print(f"✅ {len(results)}件のNotionページを保存しました")
```

### 3. 個別ページの取得

```python
from notion_integration import NotionIntegration

notion = NotionIntegration()

# ページIDを指定して直接取得
page_id = "abc123def456789"
page_content = notion.get_page_content(page_id)

if page_content:
    print(f"タイトル: {page_content['title']}")
    print(f"内容: {page_content['content'][:100]}...")
else:
    print("ページを取得できませんでした")
```

## 📁 出力ファイル構造

```
メンバー管理/
└── メンバー名/
    └── Notion資料/
        ├── Notion資料_サマリー.md     # 全資料の一覧
        ├── 01_プロジェクト進捗表.md    # 個別ページ
        ├── 02_月次売上レポート.md      # 個別ページ
        └── 03_技術学習ノート.md        # 個別ページ
```

### サマリーファイルの例

```markdown
# yukari - Notion資料

## 📄 共有された資料一覧

### 1. [プロジェクト進捗表](01_プロジェクト進捗表.md)
- 最終更新: 2025-07-15
- ステータス: 進行中

### 2. [月次売上レポート](02_月次売上レポート.md)
- 最終更新: 2025-07-10
- 進捗: 目標達成済み
```

## 🚨 トラブルシューティング

### よくあるエラーと解決方法

#### 1. "unauthorized" エラー
```
Error: 401 Unauthorized
```
**原因と解決方法:**
- APIキーが間違っている → APIキーを再確認
- ページにアクセス権限がない → ページでインテグレーションを招待
- APIキーが有効期限切れ → 新しいキーを発行

#### 2. "not_found" エラー
```
Error: 404 Not Found
```
**原因と解決方法:**
- ページIDが間違っている → URLからIDを再抽出
- ページが削除されている → ページの存在を確認
- ワークスペースが違う → 正しいワークスペースで作成したか確認

#### 3. "rate_limited" エラー
```
Error: 429 Too Many Requests
```
**原因と解決方法:**
- リクエストが多すぎる → 処理間隔を空ける（0.5秒以上）
- 同時処理が多い → バッチサイズを小さくする

#### 4. ModuleNotFoundError
```
ModuleNotFoundError: No module named 'notion_client'
```
**解決方法:**
```bash
# ライブラリの再インストール
pip install notion-client

# 仮想環境の確認
which python3
pip list | grep notion
```

#### 5. 環境変数が読み込まれない
```bash
# 環境変数の確認
echo $NOTION_API_KEY

# シェルの再起動
exec $SHELL -l

# または手動設定
export NOTION_API_KEY="your-key-here"
```

### デバッグ用コード

```python
import logging
import os
from notion_integration import NotionIntegration

# デバッグログを有効化
logging.basicConfig(level=logging.DEBUG)

# 環境変数の確認
api_key = os.getenv('NOTION_API_KEY')
print(f"API Key: {'設定済み' if api_key else '未設定'}")

# 接続テスト
notion = NotionIntegration()
if notion.client:
    print("✅ Notionクライアント初期化成功")
else:
    print("❌ Notionクライアント初期化失敗")
```

## ⚙️ 高度な設定

### 1. カスタムフィルタリング

特定のプロパティを持つページのみ取得：

```python
def filter_pages_by_status(notion_data, target_status="完了"):
    """ステータスでページをフィルタリング"""
    filtered = []
    for data in notion_data:
        properties = data['page_data']['properties']
        if properties.get('Status') == target_status:
            filtered.append(data)
    return filtered
```

### 2. バッチ処理の最適化

```python
import time

def process_large_batch(page_ids, batch_size=5):
    """大量ページの効率的処理"""
    results = []
    
    for i in range(0, len(page_ids), batch_size):
        batch = page_ids[i:i+batch_size]
        
        for page_id in batch:
            result = notion.get_page_content(page_id)
            if result:
                results.append(result)
            
            # レート制限対策
            time.sleep(0.5)
        
        # バッチ間の待機
        time.sleep(2)
    
    return results
```

### 3. プロパティ別分析

```python
def analyze_project_status(notion_data):
    """プロジェクトステータスの分析"""
    status_count = {}
    
    for data in notion_data:
        properties = data['page_data']['properties']
        status = properties.get('Status', '不明')
        status_count[status] = status_count.get(status, 0) + 1
    
    return status_count
```

## 🔒 セキュリティ考慮事項

### 1. APIキーの管理

**✅ 良い例:**
```bash
# 環境変数での管理
export NOTION_API_KEY="secret_..."

# .envファイルでの管理（.gitignoreに追加）
echo "NOTION_API_KEY=secret_..." > .env
echo ".env" >> .gitignore
```

**❌ 悪い例:**
```python
# コードにAPIキーを直接記述（絶対にNG）
api_key = "secret_1A2B3C4D5E6F7G8H9I0J..."
```

### 2. アクセス権限の最小化

- 必要なページにのみインテグレーションを招待
- 読み取り専用権限を使用（Can read）
- 定期的にアクセス権限を見直し

### 3. ログの管理

```python
import logging

# 機密情報をログに出力しない
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('notion_sync.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# APIキーをログに出力しない
logger.info("Notion連携を開始")  # ✅ OK
logger.info(f"API Key: {api_key}")  # ❌ NG
```

### 4. エラーハンドリング

```python
def safe_notion_request(func, *args, **kwargs):
    """安全なNotion APIリクエスト"""
    try:
        return func(*args, **kwargs)
    except Exception as e:
        # エラー内容を記録（APIキーは含めない）
        logger.error(f"Notion API エラー: {type(e).__name__}")
        return None
```

## 🔄 定期メンテナンス

### 月次チェックリスト

- [ ] APIキーの有効性確認
- [ ] インテグレーション権限の確認
- [ ] エラーログの確認
- [ ] 取得データの品質確認

### 四半期チェックリスト

- [ ] アクセス権限の見直し
- [ ] 不要なページ権限の削除
- [ ] パフォーマンス指標の確認
- [ ] セキュリティ設定の見直し

---

## 📞 サポート

問題が発生した場合：

1. **まずはトラブルシューティングセクションを確認**
2. **ログファイルでエラー詳細を確認**
3. **必要に応じてNotion公式ドキュメントを参照**
   - [Notion API Reference](https://developers.notion.com/reference)
   - [Notion API Community](https://github.com/makenotion/notion-sdk-js/discussions)

---
*最終更新: 2025年7月18日*
*バージョン: 1.0.0*