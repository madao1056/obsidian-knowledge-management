/**
 * Discord Bot for Obsidian連携
 * 
 * このBotを使うことで、Discordの投稿を自動的にObsidianに送信できます
 * 
 * セットアップ手順:
 * 1. npm install discord.js axios
 * 2. BOT_TOKENを設定
 * 3. node discord_bot.js
 */

const { Client, GatewayIntentBits } = require('discord.js');
const axios = require('axios');

// ========== 設定 ==========
const BOT_TOKEN = process.env.DISCORD_BOT_TOKEN;

if (!BOT_TOKEN) {
    console.error('❌ DISCORD_BOT_TOKEN環境変数が設定されていません');
    process.exit(1);
}
const OBSIDIAN_WEBHOOK_URL = 'http://localhost:8000/webhook/discord';
const OBSIDIAN_AUTH_TOKEN = 'FE4-kAi0Hga4JZpMaip7yDlTm7Xj9w8f6P1aW9zuF60'; // config.jsonから

// チャンネル設定（チャンネル名またはIDで指定）
// 既存のチャンネル名に合わせて自由に変更してください
const CHANNEL_CONFIG = {
    daily_report: ['日報', 'daily-report', '日報チャンネル', '報告', 'report', '作業報告', '業務報告'],
    question: ['質問', 'question', '質問チャンネル', 'help', 'サポート', 'support', '相談', 'ヘルプ'],
    progress: ['進捗報告', 'progress', '進捗', '成果報告', '完了報告', 'done', '成果', '実績']
};

// 特定のチャンネルIDでも指定可能（より確実）
// Discord でチャンネルを右クリック → 「IDをコピー」で取得
const CHANNEL_IDS = {
    daily_report: '', // 例: '1234567890123456789'
    question: '',     // 例: '1234567890123456790'
    progress: ''      // 例: '1234567890123456791'
};

// ========== Bot初期化 ==========
const client = new Client({
    intents: [
        GatewayIntentBits.Guilds,
        GatewayIntentBits.GuildMessages,
        GatewayIntentBits.MessageContent
    ]
});

// ========== ヘルパー関数 ==========
function detectMessageType(message) {
    const content = message.content.toLowerCase();
    
    // メッセージ内容で判定（どのチャンネルでもOK）
    // 質問パターン
    if (content.includes('？') || content.includes('?') || 
        content.includes('教えて') || content.includes('どうすれば') ||
        content.includes('わからない') || content.includes('できない') ||
        content.includes('#質問') || content.includes('#question')) {
        return 'question';
    }
    
    // 進捗・完了報告パターン
    if (content.includes('完了') || content.includes('終了') || 
        content.includes('できました') || content.includes('終わりました') ||
        content.includes('完成') || content.includes('#進捗') || 
        content.includes('#progress') || content.includes('#done')) {
        return 'progress';
    }
    
    // 日報パターン（時間や作業内容を含む）
    if (content.includes('時間') || content.includes('作業') || 
        content.includes('本日') || content.includes('今日') ||
        content.includes('営業') || content.includes('稼働') ||
        content.includes('#日報') || content.includes('#daily')) {
        return 'daily_report';
    }
    
    // デフォルト：すべてのメッセージを日報として記録
    // （重要な情報を逃さないため）
    return 'daily_report';
}

async function sendToObsidian(message, type) {
    const payload = {
        type: type,
        data: {
            author: {
                username: message.author.username,
                id: message.author.id,
                discriminator: message.author.discriminator
            },
            content: message.content,
            timestamp: message.createdAt.toISOString(),
            channel: {
                name: message.channel.name,
                id: message.channel.id
            },
            attachments: message.attachments.map(att => ({
                name: att.name,
                url: att.url,
                size: att.size
            })),
            embeds: message.embeds.map(embed => ({
                title: embed.title,
                description: embed.description,
                url: embed.url
            }))
        }
    };

    try {
        const response = await axios.post(OBSIDIAN_WEBHOOK_URL, payload, {
            headers: {
                'Authorization': `Bearer ${OBSIDIAN_AUTH_TOKEN}`,
                'Content-Type': 'application/json'
            },
            timeout: 10000 // 10秒タイムアウト
        });

        console.log(`✅ ${type} sent successfully:`, {
            author: message.author.username,
            channel: message.channel.name,
            response: response.data
        });
        
        return { success: true, data: response.data };
        
    } catch (error) {
        console.error('❌ Error sending to Obsidian:', {
            error: error.message,
            response: error.response?.data
        });
        
        return { success: false, error: error.message };
    }
}

// ========== イベントハンドラー ==========
client.on('ready', () => {
    console.log(`🤖 Discord Bot logged in as ${client.user.tag}`);
    console.log(`📡 Connected to ${client.guilds.cache.size} servers`);
    console.log(`🔗 Obsidian Webhook: ${OBSIDIAN_WEBHOOK_URL}`);
    
    // ステータス設定
    client.user.setActivity('Obsidianと連携中', { type: 'WATCHING' });
});

client.on('messageCreate', async (message) => {
    // Bot自身のメッセージは無視
    if (message.author.bot) return;
    
    // システムメッセージやコマンドは無視
    if (message.content.startsWith('!') || message.content.startsWith('/')) return;
    
    // メッセージタイプを判定（すべてのメッセージが対象）
    const type = detectMessageType(message);
    
    console.log(`📨 [${message.channel.name}] ${type} from ${message.author.username}: ${message.content.substring(0, 50)}...`);
    
    // Obsidianに送信
    const result = await sendToObsidian(message, type);
    
    // リアクションで結果を通知
    if (result.success) {
        await message.react('📝'); // すべてのメッセージに記録済みマーク
        
        // 特定のタイプの場合は追加のリアクション
        if (type === 'question') {
            await message.react('❓');
        } else if (type === 'progress') {
            await message.react('✅');
        }
    } else {
        await message.react('❌');
        console.error('Failed to sync:', result.error);
    }
});

// ========== エラーハンドリング ==========
client.on('error', (error) => {
    console.error('Discord client error:', error);
});

process.on('unhandledRejection', (error) => {
    console.error('Unhandled promise rejection:', error);
});

// ========== Bot起動 ==========
console.log('🚀 Starting Discord-Obsidian sync bot...');

// トークンチェック
if (BOT_TOKEN === 'YOUR_DISCORD_BOT_TOKEN') {
    console.error('❌ Error: BOT_TOKENを設定してください！');
    console.log('1. Discord Developer Portal (https://discord.com/developers/applications)');
    console.log('2. アプリケーション作成 → Bot → Token をコピー');
    console.log('3. このファイルのBOT_TOKENに貼り付け');
    process.exit(1);
}

// Obsidianサーバーの起動確認（リトライ付き）
async function checkObsidianServer(retries = 3) {
    for (let i = 0; i < retries; i++) {
        try {
            await axios.get(OBSIDIAN_WEBHOOK_URL.replace('/webhook/discord', '/'), {
                timeout: 5000
            });
            console.log('✅ Obsidian server is running');
            return true;
        } catch (error) {
            console.log(`⏳ Obsidianサーバーの確認中... (${i + 1}/${retries})`);
            await new Promise(resolve => setTimeout(resolve, 2000));
        }
    }
    return false;
}

// Bot起動
checkObsidianServer().then(isRunning => {
    if (isRunning) {
        client.login(BOT_TOKEN);
    } else {
        console.error('❌ Obsidian server is not responding!');
        console.log('サーバーが起動していることを確認してください');
        // サーバーが応答しなくても起動を試みる
        console.log('🔄 Botを起動します...');
        client.login(BOT_TOKEN);
    }
});