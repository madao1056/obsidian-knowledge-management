# 🚀 Discord → Obsidian 自動連携システム

## これは何？
Discordの**全チャンネル**のメッセージを自動的にObsidianに保存するシステムです。

## 起動方法（1コマンドだけ！）

```bash
# Obsidianフォルダで実行
cd /Users/hashiguchimasaki/project/obsidian
python3 run_discord_sync.py
```

以上！これだけで全部動きます。

## Discord側の設定（5分で完了）

1. **Discord Developer Portal** を開く
   - https://discord.com/developers/applications

2. **New Application** → 名前を入力 → **Create**

3. 左メニューの **Bot** → **Add Bot**

4. **TOKEN** の下の **Copy** ボタンをクリック

5. `100_discord_sync/discord_bot.js` の16行目に貼り付け：
   ```javascript
   const BOT_TOKEN = 'ここにトークンを貼り付け';
   ```

6. **OAuth2** → **URL Generator**
   - Scopes: `bot` にチェック
   - Bot Permissions: `Read Messages`, `Send Messages` にチェック
   - 生成されたURLでサーバーに招待

## 自動分類される内容

- 📝 **日報**: 時間、作業、本日などを含む
- ❓ **質問**: ？、教えて、どうすればなどを含む
- ✅ **進捗**: 完了、できました、終了などを含む

## 保存場所

- `03_Support/グッサポ・ラボ/メンバー管理/[ユーザー名]/`
  - 日報/
  - 質問履歴/
  - 進捗報告/

## 停止方法

```bash
./100_discord_sync/stop_all.sh
```

## トラブルシューティング

### Botが動かない
→ Discord Developer PortalでBotトークンをコピーして設定

### メッセージが記録されない
→ Botがサーバーに参加しているか確認

### サーバーが起動しない
→ `python3 run_discord_sync.py` を再実行

---
詳細は `100_discord_sync/README.md` を参照