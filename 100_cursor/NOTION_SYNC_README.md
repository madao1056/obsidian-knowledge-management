# Notion同期設定

## セットアップ完了

NotionからObsidianへの同期が設定されました。

### 同期されたファイル
- 保存先: `/20_Literature/25_Notion/`
- 同期数: 25ページ
- 形式: Markdown（Notionメタデータ付き）

### 手動同期の実行方法
```bash
cd /Users/hashiguchimasaki/project/obsidian
./100_cursor/sync_all_notion.sh
```

### 自動同期の設定（オプション）

1日1回自動同期する場合：
```bash
# crontabを編集
crontab -e

# 以下を追加（毎日午前9時に実行）
0 9 * * * /Users/hashiguchimasaki/project/obsidian/100_cursor/sync_all_notion.sh
```

### より多くのページを同期する場合

`simple_notion_sync.py`の20行目を編集：
```python
pages = search_pages(limit=20)  # 数値を増やす（例: limit=100）
```

### トラブルシューティング

1. **API制限エラーが出る場合**
   - Notionの無料プランはAPI呼び出し制限があります
   - 同期間隔を長くするか、ページ数を減らしてください

2. **特定のページが同期されない場合**
   - NotionでそのページにIntegrationのアクセス権限を付与してください
   - ページ右上の「...」→「Connections」→「Obsidian Sync」を追加

3. **文字化けする場合**
   - ファイルはUTF-8で保存されています
   - Obsidianの設定で文字コードを確認してください

### セキュリティ注意事項
- APIトークンは`.gitignore`に追加済みです
- トークンを共有しないでください
- 定期的にトークンを更新することを推奨します