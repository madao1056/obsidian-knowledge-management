#!/bin/bash
echo "🚀 Discord Botバッチ処理版を起動します"
echo ""
echo "💾 Webhookサーバーなしで直接JSONファイルに保存します"
echo "⏰ 30分ごとに自動的にObsidian形式に変換します"
echo ""

cd "$(dirname "$0")"

# 既存のBotを停止
if [ -f .bot.pid ]; then
    kill $(cat .bot.pid) 2>/dev/null
    rm .bot.pid
fi

# バッチ処理版Botを起動
node discord_bot_batch.js &
BOT_PID=$!
echo $BOT_PID > .bot.pid

echo ""
echo "✅ Bot起動完了 (PID: $BOT_PID)"
echo "📁 保存先: ../00_Inbox/discord/"
echo ""
echo "停止するには: kill $BOT_PID"