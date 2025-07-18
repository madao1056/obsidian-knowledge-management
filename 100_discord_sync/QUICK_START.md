
# 🎉 セットアップ完了！

## 📌 使い方（超簡単！）

### Obsidianディレクトリで実行するだけ：
```bash
cd /Users/hashiguchimasaki/project/obsidian
python3 run_discord_sync.py
```

これだけで全部自動で起動します！

### 停止する時：
```bash
./100_discord_sync/stop_all.sh
```

## 📡 Discord側の設定

### 超簡単セットアップ（Discord Bot）

1. **Discord Developer Portalでボット作成**
   - https://discord.com/developers/applications にアクセス
   - 「New Application」をクリック → 名前を入力（例：Obsidian連携）
   - 左メニューの「Bot」をクリック → 「Add Bot」
   - 「TOKEN」の下の「Copy」をクリック

2. **discord_bot.js を編集**（1行だけ！）
   ```javascript
   const BOT_TOKEN = 'ここにコピーしたトークンを貼り付け';
   ```

3. **Botを起動**
   ```bash
   npm install    # 初回のみ
   npm start      # Bot起動
   ```

4. **Discordサーバーに招待**
   - Developer Portalの「OAuth2」→「URL Generator」
   - Scopes: 「bot」にチェック
   - Bot Permissions: 「Read Messages」「Send Messages」にチェック
   - 生成されたURLをブラウザで開いてサーバーに招待

### 使用するチャンネル
**全チャンネルのメッセージを自動的に記録します！**

メッセージは内容によって自動分類されます：
- ❓ 質問として記録: 「？」「教えて」「どうすれば」を含む
- ✅ 進捗として記録: 「完了」「できました」「終了」を含む  
- 📝 日報として記録: 「時間」「作業」「本日」を含む、またはその他すべて

特定のタイプにしたい場合はタグを使用：
- `#日報` → 日報として記録
- `#質問` → 質問として記録
- `#進捗` → 進捗として記録

## 🔄 自動実行

システムは毎日 9:00 と 21:00 に自動的に処理を実行します。

## 📁 生成されるファイル

- `03_Support/グッサポ・ラボ/メンバー管理/` - メンバー情報
- `30_Permanent/34_Product/グッサポ・ラボ/` - ナレッジベース

---
詳細は README.md をご覧ください。
