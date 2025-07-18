/**
 * Discord増分収集システム
 * 前回収集時刻以降のメッセージのみを取得
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
const PROGRESS_FILE = path.join(__dirname, 'last_collection.json');
const BATCH_SIZE = 50;
const DELAY_MS = 1000;

class IncrementalCollector {
    constructor() {
        this.client = new Client({
            intents: [
                GatewayIntentBits.Guilds,
                GatewayIntentBits.GuildMessages,
                GatewayIntentBits.MessageContent
            ]
        });
        
        this.lastCollection = null;
        this.stats = {
            totalCollected: 0,
            newMessages: 0,
            skippedMessages: 0,
            startTime: new Date().toISOString()
        };
    }

    /**
     * 前回収集時刻をロード
     */
    async loadLastCollection() {
        try {
            const data = await fs.readFile(PROGRESS_FILE, 'utf8');
            this.lastCollection = JSON.parse(data);
            console.log(`📅 前回収集: ${this.lastCollection.timestamp}`);
            console.log(`📊 前回統計: ${this.lastCollection.totalMessages}件収集済み`);
        } catch (error) {
            console.log('🆕 初回収集を開始します');
            this.lastCollection = {
                timestamp: new Date('2024-05-01').toISOString(),
                totalMessages: 0,
                channels: {}
            };
        }
    }

    /**
     * 収集進捗を保存
     */
    async saveProgress() {
        const progress = {
            timestamp: new Date().toISOString(),
            totalMessages: this.lastCollection.totalMessages + this.stats.newMessages,
            channels: this.lastCollection.channels || {},
            lastStats: {
                newMessages: this.stats.newMessages,
                skippedMessages: this.stats.skippedMessages,
                collectionTime: this.stats.startTime
            }
        };

        await fs.writeFile(PROGRESS_FILE, JSON.stringify(progress, null, 2));
        console.log(`💾 進捗保存: ${progress.totalMessages}件（新規${this.stats.newMessages}件）`);
    }

    /**
     * メッセージが新しいかチェック
     */
    isNewMessage(message) {
        const messageTime = new Date(message.createdTimestamp);
        const lastTime = new Date(this.lastCollection.timestamp);
        return messageTime > lastTime;
    }

    /**
     * メッセージタイプ判定
     */
    detectMessageType(content) {
        content = content.toLowerCase();
        
        if (content.includes('？') || content.includes('?') || 
            content.includes('教えて') || content.includes('どうすれば') ||
            content.includes('わからない') || content.includes('できない')) {
            return 'question';
        }
        
        if (content.includes('完了') || content.includes('終了') || 
            content.includes('できました') || content.includes('終わりました') ||
            content.includes('完成') || content.includes('#進捗')) {
            return 'progress';
        }
        
        if (content.includes('日報') || content.includes('今日の作業') ||
            content.includes('本日の') || content.includes('作業時間') ||
            content.includes('#日報')) {
            return 'daily_report';
        }
        
        return 'daily_report'; // デフォルト
    }

    /**
     * メンバー名を正規化
     */
    normalizeMemberName(displayName, username) {
        // gussanは除外
        if (displayName && displayName.toLowerCase().includes('gussan')) return null;
        if (username && username.toLowerCase().includes('gussan')) return null;
        
        // 既知のマッピング
        const nameMap = {
            'prog.ji': 'ログジ',
            'takanori07': 'タカノリ',
            'yukari_web': 'yukari',
            'yukari': 'yukari'
        };
        
        return nameMap[username] || nameMap[displayName] || username || displayName;
    }

    /**
     * 増分収集実行
     */
    async collectIncremental() {
        console.log('🚀 Discord増分収集を開始...');
        
        await this.loadLastCollection();
        await fs.mkdir(INBOX_PATH, { recursive: true });

        try {
            await this.client.login(BOT_TOKEN);
            console.log(`✅ Discordにログインしました`);

            const guilds = this.client.guilds.cache;
            console.log(`🏰 ${guilds.size}個のサーバーを確認中...`);

            for (const [guildId, guild] of guilds) {
                console.log(`📡 サーバー: ${guild.name}`);
                
                const channels = guild.channels.cache.filter(ch => ch.isTextBased());
                
                for (const [channelId, channel] of channels) {
                    try {
                        await this.collectChannelMessages(channel);
                        await this.delay(DELAY_MS);
                    } catch (error) {
                        console.error(`❌ チャンネル ${channel.name} エラー:`, error.message);
                    }
                }
            }

            await this.saveProgress();
            console.log('\n📊 収集完了統計:');
            console.log(`   新規メッセージ: ${this.stats.newMessages}件`);
            console.log(`   スキップ: ${this.stats.skippedMessages}件`);
            console.log(`   合計時間: ${Date.now() - new Date(this.stats.startTime)}ms`);

        } catch (error) {
            console.error('❌ 収集エラー:', error);
        } finally {
            this.client.destroy();
        }
    }

    /**
     * チャンネルメッセージの増分収集
     */
    async collectChannelMessages(channel) {
        const channelName = channel.name;
        let lastMessageId = this.lastCollection.channels[channelName]?.lastMessageId;
        let newMessagesCount = 0;
        
        console.log(`📝 チャンネル: ${channelName}`);

        try {
            const options = { limit: BATCH_SIZE };
            if (lastMessageId) {
                options.after = lastMessageId;
            }

            const messages = await channel.messages.fetch(options);
            
            if (messages.size === 0) {
                console.log(`   ↳ 新しいメッセージなし`);
                return;
            }

            const sortedMessages = Array.from(messages.values())
                .sort((a, b) => a.createdTimestamp - b.createdTimestamp);

            for (const message of sortedMessages) {
                if (this.isNewMessage(message)) {
                    await this.processMessage(message, channelName);
                    newMessagesCount++;
                    
                    // 最新のメッセージIDを記録
                    if (!this.lastCollection.channels[channelName]) {
                        this.lastCollection.channels[channelName] = {};
                    }
                    this.lastCollection.channels[channelName].lastMessageId = message.id;
                } else {
                    this.stats.skippedMessages++;
                }
            }

            console.log(`   ↳ 新規: ${newMessagesCount}件`);

        } catch (error) {
            console.error(`   ❌ ${channelName} 収集エラー:`, error.message);
        }
    }

    /**
     * メッセージ処理
     */
    async processMessage(message, channelName) {
        const author = message.member || message.author;
        const displayName = author.displayName || author.globalName || author.username;
        const username = author.username || author.user?.username;
        
        const memberName = this.normalizeMemberName(displayName, username);
        
        // gussan除外
        if (!memberName) return;

        const messageData = {
            id: message.id,
            content: message.content,
            author: {
                id: author.id,
                username: username,
                displayName: displayName,
                normalizedName: memberName
            },
            channel: channelName,
            timestamp: message.createdAt.toISOString(),
            type: this.detectMessageType(message.content),
            url: message.url
        };

        // ファイル保存
        const date = message.createdAt.toISOString().split('T')[0];
        const filename = `${memberName}_${date}_${messageData.type}.json`;
        const filepath = path.join(INBOX_PATH, filename);

        try {
            // 既存ファイルがあれば配列に追加、なければ新規作成
            let existingData = [];
            try {
                const existing = await fs.readFile(filepath, 'utf8');
                existingData = JSON.parse(existing);
                if (!Array.isArray(existingData)) {
                    existingData = [existingData];
                }
            } catch (e) {
                // ファイルが存在しない場合は空配列
            }

            existingData.push(messageData);
            await fs.writeFile(filepath, JSON.stringify(existingData, null, 2));
            
            this.stats.newMessages++;
            
        } catch (error) {
            console.error(`❌ ファイル保存エラー: ${filename}`, error);
        }
    }

    /**
     * 遅延処理
     */
    async delay(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
}

// 実行
if (require.main === module) {
    const collector = new IncrementalCollector();
    collector.collectIncremental().catch(console.error);
}

module.exports = IncrementalCollector;