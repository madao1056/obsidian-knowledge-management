#!/bin/bash
echo "🚀 Discord-Obsidian連携システムとDiscord Botを起動します..."

# 既存のプロセスを停止
./stop_all.sh 2>/dev/null

# Obsidianサーバーを起動
echo ""
echo "📡 Obsidianサーバーを起動中..."
./start.sh

# サーバーが完全に起動するまで待機
echo "⏳ サーバーの起動を待っています..."
sleep 5

# サーバーの状態確認
curl -s http://localhost:8000/ > /dev/null
if [ $? -eq 0 ]; then
    echo "✅ Obsidianサーバーが正常に起動しました"
else
    echo "⚠️  Obsidianサーバーの起動に時間がかかっています"
fi

# Discord Botを起動
echo ""
echo "🤖 Discord Botを起動中..."
cd "$(dirname "$0")"
npm start &
BOT_PID=$!
echo "$BOT_PID" > .bot.pid

echo ""
echo "✨ すべてのシステムが起動しました！"
echo ""
echo "📌 Webhook URL: http://localhost:8000/webhook/discord"
echo "📌 Discord Bot: 全チャンネル監視中"
echo ""
echo "停止するには: ./stop_all.sh"