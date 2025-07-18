# Discord側の設定手順

## 方法1: Discord Webhooks（サーバー管理者向け）

### 1. Webhookを作成
1. Discordサーバーの設定を開く
2. 「連携サービス」→「ウェブフック」を選択
3. 「新しいウェブフック」をクリック
4. 名前を設定（例：Obsidian連携）
5. チャンネルを選択（日報チャンネルなど）
6. 「ウェブフックURLをコピー」

### 2. 問題点
- 標準のDiscord Webhookは**送信専用**
- メッセージを**受信**することはできない
- つまり、このままでは日報を自動取得できない

## 方法2: Discord Bot（推奨）

### 1. Discord Developer Portalでボット作成

1. [Discord Developer Portal](https://discord.com/developers/applications)にアクセス
2. 「New Application」をクリック
3. アプリ名を入力（例：グッサポ・ラボ連携Bot）
4. 「Bot」タブを選択
5. 「Add Bot」をクリック
6. 「Token」の下の「Copy」でトークンをコピー

### 2. 権限設定
1. 「OAuth2」→「URL Generator」を選択
2. Scopesで「bot」にチェック
3. Bot Permissionsで以下にチェック：
   - Read Messages/View Channels
   - Read Message History
   - Send Messages

4. 生成されたURLをコピー

### 3. サーバーに招待
1. 生成されたURLをブラウザで開く
2. 対象のサーバーを選択
3. 「認証」をクリック

### 4. Botコード例

```javascript
// discord_bot.js
const { Client, GatewayIntentBits } = require('discord.js');
const axios = require('axios');

const client = new Client({
    intents: [
        GatewayIntentBits.Guilds,
        GatewayIntentBits.GuildMessages,
        GatewayIntentBits.MessageContent
    ]
});

// Obsidian連携サーバーの設定
const WEBHOOK_URL = 'http://localhost:8000/webhook/discord';
const AUTH_TOKEN = 'FE4-kAi0Hga4JZpMaip7yDlTm7Xj9w8f6P1aW9zuF60'; // config.jsonのトークン

// メッセージ受信時の処理
client.on('messageCreate', async (message) => {
    // Botのメッセージは無視
    if (message.author.bot) return;

    let type = null;
    
    // チャンネル名で判定
    if (message.channel.name === '日報' || message.content.includes('#日報')) {
        type = 'daily_report';
    } else if (message.channel.name === '質問' || message.content.includes('#質問')) {
        type = 'question';
    } else if (message.channel.name === '進捗報告' || message.content.includes('#進捗')) {
        type = 'progress';
    }

    if (type) {
        // Obsidianサーバーに送信
        try {
            const payload = {
                type: type,
                data: {
                    author: {
                        username: message.author.username,
                        id: message.author.id
                    },
                    content: message.content,
                    timestamp: message.createdAt.toISOString(),
                    channel: {
                        name: message.channel.name,
                        id: message.channel.id
                    }
                }
            };

            const response = await axios.post(WEBHOOK_URL, payload, {
                headers: {
                    'Authorization': `Bearer ${AUTH_TOKEN}`,
                    'Content-Type': 'application/json'
                }
            });

            console.log(`✅ ${type} sent to Obsidian:`, response.data);
            
            // リアクションで通知
            await message.react('✅');
            
        } catch (error) {
            console.error('❌ Error:', error.message);
            await message.react('❌');
        }
    }
});

// Bot起動
client.login('YOUR_BOT_TOKEN'); // Discord Developer Portalで取得したトークン

console.log('🤖 Discord Bot started!');
```

### 5. Bot実行方法

```bash
# 必要なパッケージインストール
npm install discord.js axios

# Bot起動
node discord_bot.js
```

## 方法3: Zapier/Make（ノーコード）

### Zapierの場合
1. [Zapier](https://zapier.com)でアカウント作成
2. 「Make a Zap」をクリック
3. Trigger: Discord → New Message Posted to Channel
4. Action: Webhooks by Zapier → POST
5. URL: `http://localhost:8000/webhook/discord`
6. Headers: `Authorization: Bearer FE4-kAi0Hga4JZpMaip7yDlTm7Xj9w8f6P1aW9zuF60`

### 問題点
- localhostには送信できない（外部公開が必要）
- ngrokなどでトンネリングが必要

## 推奨構成

1. **開発/テスト**: Discord Bot（方法2）
2. **本番運用**: 
   - サーバーをクラウドにデプロイ
   - Discord BotまたはZapier/Make使用

## チャンネル設定の推奨

以下のチャンネルを作成することを推奨：

- 📝 #日報
- ❓ #質問
- 📊 #進捗報告

メンバーがこれらのチャンネルに投稿すると、自動的にObsidianに連携されます。

## セキュリティ注意事項

- BotトークンとWebhookトークンは絶対に公開しない
- 本番環境ではHTTPSを使用
- 定期的にトークンを更新