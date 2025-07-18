/**
 * Discord履歴収集 バッチ処理版
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
const START_DATE = new Date('2024-05-01');
const BATCH_SIZE = 100;
const DELAY_MS = 500; // API制限を避けるための遅延

// ディレクトリ作成
async function ensureDirectory() {
    try {
        await fs.mkdir(INBOX_PATH, { recursive: true });
        console.log(`📁 保存先: ${INBOX_PATH}`);
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

// メッセージタイプ判定（discord_bot_batch.jsと同じ）
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

// メッセージをバッチ保存
async function saveMessagesBatch(messages) {
    const messagesByFile = {};
    
    // ファイル別にグループ化
    for (const message of messages) {
        const type = detectMessageType(message.content);
        const date = message.createdAt.toISOString().split('T')[0];
        const filename = `${message.author.username}_${date}_${type}.json`;
        
        if (!messagesByFile[filename]) {
            messagesByFile[filename] = [];
        }
        
        messagesByFile[filename].push({
            type: type,
            author: message.author.username,
            date: date,
            timestamp: message.createdAt.toISOString(),
            content: message.content,
            raw_data: {
                author: {
                    username: message.author.username,
                    id: message.author.id
                },
                channel: {
                    name: message.channel.name,
                    id: message.channel.id
                }
            }
        });
    }
    
    // 各ファイルに保存
    let savedCount = 0;
    for (const [filename, data] of Object.entries(messagesByFile)) {
        const filepath = path.join(INBOX_PATH, filename);
        
        try {
            // 既存データを読み込む
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
            
            // 重複を除いて追加
            const existingTimestamps = new Set(existingData.map(item => item.timestamp));
            const newData = data.filter(item => !existingTimestamps.has(item.timestamp));
            
            if (newData.length > 0) {
                existingData.push(...newData);
                await fs.writeFile(filepath, JSON.stringify(existingData, null, 2), 'utf8');
                savedCount += newData.length;
                console.log(`  💾 ${filename}: ${newData.length}件追加`);
            }
            
        } catch (error) {
            console.error(`  ❌ 保存エラー (${filename}):`, error.message);
        }
    }
    
    return savedCount;
}

// スレッド内のメッセージを収集
async function collectThreadMessages(thread) {
    const threadMessages = [];
    let lastId = null;
    let hasMore = true;
    
    while (hasMore) {
        try {
            const options = { limit: 100 };
            if (lastId) options.before = lastId;
            
            const messages = await thread.messages.fetch(options);
            if (messages.size === 0) {
                hasMore = false;
                break;
            }
            
            const validMessages = Array.from(messages.values())
                .filter(msg => msg.createdAt >= START_DATE && !msg.author.bot && msg.content);
            
            threadMessages.push(...validMessages);
            lastId = messages.last().id;
            
            // 開始日より前に到達
            if (messages.last().createdAt < START_DATE) {
                hasMore = false;
            }
            
            await new Promise(resolve => setTimeout(resolve, 200)); // API制限対策
        } catch (error) {
            console.error(`    ❌ スレッドエラー: ${error.message}`);
            hasMore = false;
        }
    }
    
    return threadMessages;
}

// チャンネルの履歴を収集（スレッドを含む）
async function collectChannelHistory(channel) {
    console.log(`\n📂 チャンネル: ${channel.name}`);
    
    let lastId = null;
    let totalMessages = 0;
    let savedMessages = 0;
    let threadCount = 0;
    let hasMore = true;
    const messageBatch = [];
    
    // アクティブなスレッドを取得
    try {
        const threads = await channel.threads.fetchActive();
        const archivedThreads = await channel.threads.fetchArchived();
        
        const allThreads = [...threads.threads.values(), ...archivedThreads.threads.values()];
        
        if (allThreads.length > 0) {
            console.log(`  🧵 ${allThreads.length}個のスレッドを検出`);
            
            // 各スレッドのメッセージを収集
            for (const thread of allThreads) {
                process.stdout.write(`\r  🧵 スレッド処理中: ${thread.name}`);
                const threadMessages = await collectThreadMessages(thread);
                
                if (threadMessages.length > 0) {
                    messageBatch.push(...threadMessages);
                    totalMessages += threadMessages.length;
                    threadCount++;
                }
            }
            
            if (threadCount > 0) {
                console.log(`\n  ✅ ${threadCount}個のスレッドから${messageBatch.length}件のメッセージを収集`);
            }
        }
    } catch (error) {
        console.error(`\n  ⚠️  スレッド取得エラー: ${error.message}`);
    }
    
    // 通常のメッセージを収集
    while (hasMore) {
        try {
            // メッセージを取得
            const options = { limit: BATCH_SIZE };
            if (lastId) options.before = lastId;
            
            const messages = await channel.messages.fetch(options);
            if (messages.size === 0) {
                hasMore = false;
                break;
            }
            
            // 日付でフィルタリング（スレッドのスターターメッセージも含む）
            const validMessages = Array.from(messages.values())
                .filter(msg => msg.createdAt >= START_DATE && !msg.author.bot && msg.content);
            
            if (validMessages.length === 0) {
                // 開始日より前に到達
                hasMore = false;
                break;
            }
            
            // スレッドがあるメッセージを検出
            for (const msg of validMessages) {
                if (msg.hasThread && msg.thread) {
                    try {
                        process.stdout.write(`\r  🧵 追加スレッド処理中: ${msg.thread.name}`);
                        const threadMessages = await collectThreadMessages(msg.thread);
                        
                        if (threadMessages.length > 0) {
                            messageBatch.push(...threadMessages);
                            totalMessages += threadMessages.length;
                        }
                    } catch (error) {
                        // スレッドアクセスエラーは無視
                    }
                }
            }
            
            // バッチに追加
            messageBatch.push(...validMessages);
            totalMessages += validMessages.length;
            
            // 100件ごとに保存
            if (messageBatch.length >= 100) {
                const saved = await saveMessagesBatch(messageBatch);
                savedMessages += saved;
                messageBatch.length = 0; // バッチをクリア
                
                process.stdout.write(`\r  📊 処理中: ${totalMessages}件取得, ${savedMessages}件保存`);
            }
            
            lastId = messages.last().id;
            
            // API制限を避けるため待機
            await new Promise(resolve => setTimeout(resolve, DELAY_MS));
            
        } catch (error) {
            console.error(`\n  ❌ エラー: ${error.message}`);
            hasMore = false;
        }
    }
    
    // 残りのメッセージを保存
    if (messageBatch.length > 0) {
        const saved = await saveMessagesBatch(messageBatch);
        savedMessages += saved;
    }
    
    console.log(`\n  ✅ 完了: ${totalMessages}件取得, ${savedMessages}件保存`);
    return { total: totalMessages, saved: savedMessages };
}

// メイン処理
client.on('ready', async () => {
    console.log(`🤖 Discord履歴収集Bot (バッチ版): ${client.user.tag}`);
    console.log(`📅 2024年5月1日以降のメッセージを収集します`);
    console.log(`💾 JSONファイルに直接保存（Webhookサーバー不要）\n`);
    
    await ensureDirectory();
    
    const startTime = Date.now();
    const stats = {
        channels: {},
        totalMessages: 0,
        totalSaved: 0
    };
    
    try {
        // すべてのギルドを処理
        for (const guild of client.guilds.cache.values()) {
            console.log(`\n🏢 サーバー: ${guild.name}`);
            
            // テキストチャンネルのみ処理
            const textChannels = guild.channels.cache
                .filter(channel => channel.type === 0)
                .filter(channel => channel.permissionsFor(guild.members.me).has('ViewChannel'));
            
            console.log(`  📊 ${textChannels.size} 個のチャンネルを処理します`);
            
            for (const channel of textChannels.values()) {
                const result = await collectChannelHistory(channel);
                stats.channels[channel.name] = result;
                stats.totalMessages += result.total;
                stats.totalSaved += result.saved;
            }
        }
        
        const duration = Math.round((Date.now() - startTime) / 1000);
        
        console.log('\n' + '='.repeat(50));
        console.log('📊 収集完了！');
        console.log('='.repeat(50));
        console.log(`⏱️  処理時間: ${duration}秒`);
        console.log(`📝 取得メッセージ数: ${stats.totalMessages}`);
        console.log(`💾 保存メッセージ数: ${stats.totalSaved}`);
        console.log(`📁 保存先: ${INBOX_PATH}`);
        
        // 統計情報を保存
        const statsPath = path.join(__dirname, 'collection_stats.json');
        await fs.writeFile(statsPath, JSON.stringify({
            ...stats,
            startTime: new Date(startTime).toISOString(),
            endTime: new Date().toISOString(),
            duration: duration
        }, null, 2));
        
        console.log('\n📝 次のステップ:');
        console.log('1. 処理を実行:');
        console.log('   cd 100_discord_sync');
        console.log('   venv/bin/python main_processor.py --once');
        
    } catch (error) {
        console.error('\n❌ エラーが発生しました:', error);
    }
    
    console.log('\n👋 収集完了。プロセスを終了します。');
    process.exit(0);
});

// エラーハンドリング
client.on('error', console.error);
process.on('unhandledRejection', console.error);

// Bot起動
console.log('🚀 Discord履歴収集（バッチ版）を開始します...');
client.login(BOT_TOKEN);