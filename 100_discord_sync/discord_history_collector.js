/**
 * Discord履歴収集スクリプト
 * 既存のメッセージを遡って収集します
 */

const { Client, GatewayIntentBits } = require('discord.js');
const axios = require('axios');
const fs = require('fs').promises;
const path = require('path');

// 設定（discord_bot.jsと同じ）
const BOT_TOKEN = process.env.DISCORD_BOT_TOKEN;

if (!BOT_TOKEN) {
    console.error('❌ DISCORD_BOT_TOKEN環境変数が設定されていません');
    process.exit(1);
}
const OBSIDIAN_WEBHOOK_URL = 'http://localhost:8000/webhook/discord';
const OBSIDIAN_AUTH_TOKEN = 'FE4-kAi0Hga4JZpMaip7yDlTm7Xj9w8f6P1aW9zuF60';

// 収集設定
const DAYS_TO_COLLECT = 365; // 1年分（5月から確実に含む）
const BATCH_SIZE = 100; // 一度に取得するメッセージ数
const DELAY_MS = 1000; // API制限を避けるための遅延
const START_DATE = new Date('2024-05-01'); // 5月1日以降のメッセージを取得

const client = new Client({
    intents: [
        GatewayIntentBits.Guilds,
        GatewayIntentBits.GuildMessages,
        GatewayIntentBits.MessageContent
    ]
});

// メッセージタイプ判定（discord_bot.jsと同じロジック）
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

// Obsidianに送信
async function sendToObsidian(message, type) {
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

    try {
        const response = await axios.post(OBSIDIAN_WEBHOOK_URL, payload, {
            headers: {
                'Authorization': `Bearer ${OBSIDIAN_AUTH_TOKEN}`,
                'Content-Type': 'application/json'
            },
            timeout: 10000
        });
        return { success: true, data: response.data };
    } catch (error) {
        // エラーの詳細を返す
        if (error.response) {
            return { 
                success: false, 
                error: `HTTP ${error.response.status}: ${error.response.data?.detail || error.response.statusText}`
            };
        } else if (error.request) {
            return { 
                success: false, 
                error: `サーバーに接続できません: ${error.code || error.message}`
            };
        } else {
            return { 
                success: false, 
                error: error.message 
            };
        }
    }
}

// チャンネルの履歴を収集
async function collectChannelHistory(channel) {
    console.log(`\n📂 チャンネル: ${channel.name}`);
    
    // 5月1日以降のメッセージを取得
    const cutoffDate = START_DATE;
    
    let lastId = null;
    let totalMessages = 0;
    let successCount = 0;
    let hasMore = true;
    
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
            
            // 古い順に処理
            const sortedMessages = Array.from(messages.values()).reverse();
            
            for (const message of sortedMessages) {
                // 日付チェック
                if (message.createdAt < cutoffDate) {
                    hasMore = false;
                    break;
                }
                
                // Botのメッセージはスキップ
                if (message.author.bot) continue;
                
                // システムメッセージはスキップ
                if (!message.content || message.content.length === 0) continue;
                
                totalMessages++;
                
                // メッセージタイプを判定
                const type = detectMessageType(message.content);
                
                // Obsidianに送信
                const result = await sendToObsidian(message, type);
                
                if (result.success) {
                    successCount++;
                    process.stdout.write(`\r  📝 処理中: ${successCount}/${totalMessages} メッセージ`);
                } else {
                    console.error(`\n  ❌ エラー [${message.author.username}]: ${result.error || '不明なエラー'}`);
                    console.error(`     メッセージ: ${message.content.substring(0, 50)}...`);
                }
                
                // API制限を避けるため少し待機
                await new Promise(resolve => setTimeout(resolve, 100));
            }
            
            lastId = sortedMessages[sortedMessages.length - 1].id;
            
            // バッチ間の待機
            await new Promise(resolve => setTimeout(resolve, DELAY_MS));
            
        } catch (error) {
            console.error(`\n  ❌ チャンネル履歴取得エラー: ${error.message}`);
            hasMore = false;
        }
    }
    
    console.log(`\n  ✅ 完了: ${successCount}/${totalMessages} メッセージを保存`);
    return { total: totalMessages, success: successCount };
}

// 進捗状況を保存
async function saveProgress(data) {
    const progressPath = path.join(__dirname, 'collection_progress.json');
    await fs.writeFile(progressPath, JSON.stringify(data, null, 2));
}

// メイン処理
client.on('ready', async () => {
    console.log(`🤖 Discord履歴収集Bot: ${client.user.tag}`);
    console.log(`📅 2024年5月1日以降のメッセージを収集します\n`);
    
    const startTime = Date.now();
    const stats = {
        startTime: new Date().toISOString(),
        channels: {},
        totalMessages: 0,
        totalSuccess: 0
    };
    
    try {
        // すべてのギルドを処理
        for (const guild of client.guilds.cache.values()) {
            console.log(`\n🏢 サーバー: ${guild.name}`);
            
            // テキストチャンネルのみ処理
            const textChannels = guild.channels.cache
                .filter(channel => channel.type === 0) // GUILD_TEXT
                .filter(channel => channel.permissionsFor(guild.members.me).has('ViewChannel'));
            
            console.log(`  📊 ${textChannels.size} 個のチャンネルを処理します`);
            
            for (const channel of textChannels.values()) {
                const result = await collectChannelHistory(channel);
                stats.channels[channel.name] = result;
                stats.totalMessages += result.total;
                stats.totalSuccess += result.success;
                
                // 進捗を保存
                await saveProgress(stats);
            }
        }
        
        const duration = Math.round((Date.now() - startTime) / 1000);
        
        console.log('\n' + '='.repeat(50));
        console.log('📊 収集完了！');
        console.log('='.repeat(50));
        console.log(`⏱️  処理時間: ${duration}秒`);
        console.log(`📝 総メッセージ数: ${stats.totalMessages}`);
        console.log(`✅ 保存成功: ${stats.totalSuccess}`);
        console.log(`❌ 保存失敗: ${stats.totalMessages - stats.totalSuccess}`);
        
        stats.endTime = new Date().toISOString();
        stats.duration = duration;
        await saveProgress(stats);
        
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
console.log('🚀 Discord履歴収集を開始します...');
client.login(BOT_TOKEN);