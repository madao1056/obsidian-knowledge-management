# Discord-Obsidian連携システム

グッサポ・ラボのDiscordから日報、質問、進捗報告を自動的に収集し、Obsidianナレッジベースに変換するシステムです。

## 機能

### 1. Webhook受信サーバー（webhook_server.py）
- Discord Webhookを受信
- 3種類のペイロード対応：
  - `daily_report`: 日報
  - `question`: 質問
  - `progress`: 進捗報告
- 認証機能付き
- 受信データをJSON形式で保存

### 2. 日報解析（daily_report_analyzer.py）
- 日報から自動抽出：
  - 稼働時間
  - 完了タスク
  - 予定タスク
  - 課題・困ったこと
  - 売上情報
  - 営業活動
  - 感情分析
- メンバー別にマークダウン形式で保存

### 3. 質問・進捗解析（question_progress_analyzer.py）
- 質問の分類とキーワード抽出
- 緊急度判定
- 進捗報告から成果と学びを抽出
- FAQ自動生成
- 成功事例集の更新

### 4. メインプロセッサー（main_processor.py）
- 全解析処理の統合実行
- 処理統計の記録
- サマリーレポート生成
- アラート機能（日報がない、稼働時間が少ない等）

## セットアップ

### 1. 依存関係のインストール
```bash
pip install fastapi uvicorn schedule
```

### 2. 設定ファイルの作成
`config.json`を作成：
```json
{
  "webhook_token": "your-secret-token-here"
}
```

### 3. Discord Webhook設定
Discordから送信する際の形式：
```javascript
// 日報の例
{
  "type": "daily_report",
  "data": {
    "author": {
      "username": "メンバー名"
    },
    "content": "今日の稼働時間: 5時間\n完了タスク:\n- A機能の実装\n- バグ修正",
    "timestamp": "2025-07-18T10:00:00Z"
  }
}
```

### 4. サーバー起動
```bash
# Webhookサーバー起動
python webhook_server.py

# 別ターミナルで処理実行
python main_processor.py --once
```

## 使い方

### 手動実行
```bash
# 1回だけ実行
python main_processor.py --once
```

### 自動実行
```bash
# デーモンとして起動（9:00と21:00に自動実行）
python main_processor.py --daemon
```

### systemdサービスとして登録（推奨）
`/etc/systemd/system/discord-obsidian-sync.service`:
```ini
[Unit]
Description=Discord-Obsidian Sync Service
After=network.target

[Service]
Type=simple
User=your-username
WorkingDirectory=/Users/hashiguchimasaki/project/obsidian/100_discord_sync
ExecStart=/usr/bin/python3 /Users/hashiguchimasaki/project/obsidian/100_discord_sync/main_processor.py --daemon
Restart=always

[Install]
WantedBy=multi-user.target
```

## ディレクトリ構造

```
obsidian/
├── 00_Inbox/
│   └── discord/          # Webhookで受信したJSONファイル
├── 03_Support/
│   └── グッサポ・ラボ/
│       ├── メンバー管理/
│       │   ├── メンバー名/
│       │   │   ├── プロファイル.md
│       │   │   ├── 日報/
│       │   │   ├── 質問履歴/
│       │   │   └── 進捗報告/
│       │   └── ...
│       └── Discord同期サマリー.md
└── 30_Permanent/
    └── 34_Product/
        └── グッサポ・ラボ/
            ├── よくある質問と回答.md
            └── 成功事例集.md
```

## カスタマイズ

### 解析パターンの追加
`daily_report_analyzer.py`の`patterns`辞書に正規表現を追加：
```python
self.patterns = {
    "新パターン": re.compile(r'パターン正規表現'),
    # ...
}
```

### 新しいペイロードタイプ
`webhook_server.py`に処理関数を追加：
```python
async def process_new_type(data: Dict):
    # 処理ロジック
    pass
```

## トラブルシューティング

### Webhookが受信できない
1. `config.json`のトークンを確認
2. ファイアウォール設定を確認
3. ポート8000が開いているか確認

### 解析が正しく動作しない
1. ログファイル`discord_sync.log`を確認
2. 正規表現パターンが日本語に対応しているか確認
3. JSONファイルの形式を確認

## 今後の拡張予定
- [ ] Slack連携
- [ ] 自動応答機能
- [ ] レポートのグラフ化
- [ ] メンバー間の相関分析
- [ ] AIによる自動アドバイス生成