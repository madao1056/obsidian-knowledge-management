/**
 * Discord Webhook送信クライアントの例
 * Discord Botやクライアントアプリケーションから使用
 */

const axios = require('axios');

// 設定
const WEBHOOK_URL = 'http://localhost:8000/webhook/discord';
const AUTH_TOKEN = 'your-secret-token-here';

/**
 * 日報を送信
 */
async function sendDailyReport(username, content) {
    const payload = {
        type: 'daily_report',
        data: {
            author: {
                username: username
            },
            content: content,
            timestamp: new Date().toISOString(),
            channel: {
                name: '日報'
            }
        }
    };

    try {
        const response = await axios.post(WEBHOOK_URL, payload, {
            headers: {
                'Authorization': `Bearer ${AUTH_TOKEN}`,
                'Content-Type': 'application/json'
            }
        });
        console.log('日報送信成功:', response.data);
    } catch (error) {
        console.error('日報送信失敗:', error.response?.data || error.message);
    }
}

/**
 * 質問を送信
 */
async function sendQuestion(username, content) {
    const payload = {
        type: 'question',
        data: {
            author: {
                username: username
            },
            content: content,
            timestamp: new Date().toISOString(),
            channel: {
                name: '質問'
            }
        }
    };

    try {
        const response = await axios.post(WEBHOOK_URL, payload, {
            headers: {
                'Authorization': `Bearer ${AUTH_TOKEN}`,
                'Content-Type': 'application/json'
            }
        });
        console.log('質問送信成功:', response.data);
    } catch (error) {
        console.error('質問送信失敗:', error.response?.data || error.message);
    }
}

/**
 * 進捗報告を送信
 */
async function sendProgress(username, content) {
    const payload = {
        type: 'progress',
        data: {
            author: {
                username: username
            },
            content: content,
            timestamp: new Date().toISOString(),
            channel: {
                name: '進捗報告'
            }
        }
    };

    try {
        const response = await axios.post(WEBHOOK_URL, payload, {
            headers: {
                'Authorization': `Bearer ${AUTH_TOKEN}`,
                'Content-Type': 'application/json'
            }
        });
        console.log('進捗報告送信成功:', response.data);
    } catch (error) {
        console.error('進捗報告送信失敗:', error.response?.data || error.message);
    }
}

/**
 * Discord Botのメッセージイベントハンドラー例
 */
function handleDiscordMessage(message) {
    // 日報チャンネルの場合
    if (message.channel.name === '日報' || message.content.includes('#日報')) {
        sendDailyReport(message.author.username, message.content);
    }
    // 質問チャンネルの場合
    else if (message.channel.name === '質問' || message.content.includes('#質問')) {
        sendQuestion(message.author.username, message.content);
    }
    // 進捗報告チャンネルの場合
    else if (message.channel.name === '進捗報告' || message.content.includes('#進捗')) {
        sendProgress(message.author.username, message.content);
    }
}

// 使用例
if (require.main === module) {
    // テスト送信
    sendDailyReport('ログジさん', `
【本日の日報】
稼働時間: 5.5時間

完了タスク:
- LP制作のコーディング完了
- レスポンシブ対応実装
- クライアントへの納品

営業活動:
- 営業メール30件送信
- 返信1件獲得

課題:
- figmaのブレンドモードがCSSで再現できない

明日の予定:
- 新規案件のキックオフMTG
- WordPress案件の見積もり作成
    `);

    sendQuestion('ぽてちさん', `
Next.jsでSSGとSSRを使い分ける基準について教えてください。
特に、ECサイトを作る場合のベストプラクティスを知りたいです。
    `);

    sendProgress('タカ☆ノリさん', `
【進捗報告】
WordPress案件のカスタム投稿タイプ実装が完了しました！

学んだこと:
- register_post_typeの使い方
- カスタムタクソノミーの設定方法
- ACFとの連携方法

これでクライアントが自分でニュース記事を管理できるようになりました。
工数: 3時間
    `);
}

module.exports = {
    sendDailyReport,
    sendQuestion,
    sendProgress,
    handleDiscordMessage
};