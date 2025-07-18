/**
 * Discord Bot バッチ処理版
 * Webhookサーバーを使わずに直接JSONファイルに保存
 */

const { Client, GatewayIntentBits } = require('discord.js');
const fs = require('fs').promises;
const path = require('path');

// 設定
const BOT_TOKEN = process.env.DISCORD_BOT_TOKEN;

if (!BOT_TOKEN) {
    console.error('❌ DISCORD_BOT_TOKEN環境変数が設定されていません');
    process.exit(1);
}
const INBOX_PATH = path.join(__dirname, '..', '00_Inbox', 'discord');

// ディレクトリ作成
async function ensureDirectory() {
    try {
        await fs.mkdir(INBOX_PATH, { recursive: true });
    } catch (error) {
        console.error('ディレクトリ作成エラー:', error);
    }
}

const client = new Client({
    intents: [
        GatewayIntentBits.Guilds,
        GatewayIntentBits.GuildMessages,
        GatewayIntentBits.MessageContent
    ]
});

// メッセージタイプ判定
function detectMessageType(content) {
    content = content.toLowerCase();
    
    if (content.includes('？') || content.includes('?') || 
        content.includes('教えて') || content.includes('どうすれば') ||
        content.includes('わからない') || content.includes('できない') ||
        content.includes('#質問') || content.includes('#question')) {
        return 'question';
    }
    
    if (content.includes('完了') || content.includes('終了') || 
        content.includes('できました') || content.includes('終わりました') ||
        content.includes('完成') || content.includes('#進捗') || 
        content.includes('#progress') || content.includes('#done')) {
        return 'progress';
    }
    
    if (content.includes('時間') || content.includes('作業') || 
        content.includes('本日') || content.includes('今日') ||
        content.includes('営業') || content.includes('稼働') ||
        content.includes('#日報') || content.includes('#daily')) {
        return 'daily_report';
    }
    
    return 'daily_report';
}

// JSONファイルに保存
async function saveToJSON(message, type) {
    const date = message.createdAt.toISOString().split('T')[0];
    const timestamp = message.createdAt.toISOString();
    
    const data = {
        type: type,
        author: message.author.username,
        date: date,
        timestamp: timestamp,
        content: message.content,
        raw_data: {
            author: {
                username: message.author.username,
                id: message.author.id
            },
            channel: {
                name: message.channel.name,
                id: message.channel.id
            },
            attachments: message.attachments.map(att => ({
                name: att.name,
                url: att.url
            }))
        }
    };
    
    // ファイル名を生成
    const filename = `${message.author.username}_${date}_${type}.json`;
    const filepath = path.join(INBOX_PATH, filename);
    
    try {
        // 既存のデータがある場合は配列に追加
        let existingData = [];
        try {
            const existing = await fs.readFile(filepath, 'utf8');
            existingData = JSON.parse(existing);
            if (!Array.isArray(existingData)) {
                existingData = [existingData];
            }
        } catch (err) {
            // ファイルが存在しない場合は新規作成
        }
        
        // 重複チェック（同じタイムスタンプのメッセージは追加しない）
        const isDuplicate = existingData.some(item => 
            item.timestamp === timestamp && item.content === message.content
        );
        
        if (!isDuplicate) {
            existingData.push(data);
            await fs.writeFile(filepath, JSON.stringify(existingData, null, 2), 'utf8');
            return { success: true, filepath: filename };
        } else {
            return { success: false, reason: 'duplicate' };
        }
        
    } catch (error) {
        console.error('保存エラー:', error);
        return { success: false, error: error.message };
    }
}

// Bot起動時
client.on('ready', () => {
    console.log(`🤖 Discord Bot (バッチ処理版) logged in as ${client.user.tag}`);
    console.log(`📡 Connected to ${client.guilds.cache.size} servers`);
    console.log(`📁 保存先: ${INBOX_PATH}`);
    console.log('✅ すべてのメッセージをJSONファイルに保存します');
    console.log('🧵 スレッド内のメッセージも監視します');
    
    // ディレクトリ確認
    ensureDirectory();
    
    client.user.setActivity('JSONに記録中', { type: 'WATCHING' });
});

// メッセージ受信時（通常チャンネルとスレッド両方）
client.on('messageCreate', async (message) => {
    // Bot自身のメッセージは無視
    if (message.author.bot) return;
    
    // システムメッセージやコマンドは無視
    if (message.content.startsWith('!') || message.content.startsWith('/')) return;
    
    // メッセージタイプを判定
    const type = detectMessageType(message.content);
    
    // チャンネル名を取得（スレッドの場合は親チャンネル名も含める）
    let channelInfo = message.channel.name;
    if (message.channel.isThread()) {
        const parentChannel = message.channel.parent;
        channelInfo = `${parentChannel.name} > ${message.channel.name}`;
    }
    
    // JSONファイルに保存
    const result = await saveToJSON(message, type);
    
    if (result.success) {
        console.log(`📝 [${channelInfo}] ${type} from ${message.author.username} → ${result.filepath}`);
        await message.react('💾'); // 保存済みマーク
        
        if (type === 'question') {
            await message.react('❓');
        } else if (type === 'progress') {
            await message.react('✅');
        }
    } else if (result.reason === 'duplicate') {
        // 重複の場合は何もしない（ログも出さない）
    } else {
        console.error('❌ 保存失敗:', result.error);
        await message.react('❌');
    }
});

// エラーハンドリング
client.on('error', console.error);
process.on('unhandledRejection', console.error);

// 定期的に処理を実行するタイマー
setInterval(async () => {
    console.log('\n⏰ バッチ処理を実行します...');
    
    try {
        // main_processor.pyを実行
        const { exec } = require('child_process');
        const venvPython = path.join(__dirname, 'venv', 'bin', 'python');
        
        exec(`${venvPython} main_processor.py --once`, (error, stdout, stderr) => {
            if (error) {
                console.error('❌ バッチ処理エラー:', error);
                return;
            }
            if (stdout) {
                console.log('📊 処理結果:', stdout);
            }
        });
    } catch (error) {
        console.error('❌ バッチ処理実行エラー:', error);
    }
    
}, 30 * 60 * 1000); // 30分ごとに実行

// Bot起動
console.log('🚀 Discord Bot (バッチ処理版) を起動します...');
console.log('💾 Webhookサーバーなしで直接JSONファイルに保存します');
console.log('⏰ 30分ごとに自動処理を実行します');

client.login(BOT_TOKEN);