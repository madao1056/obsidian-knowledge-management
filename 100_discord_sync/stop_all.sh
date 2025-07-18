#!/bin/bash
echo "🛑 すべてのシステムを停止します..."

# Discord Botを停止
if [ -f .bot.pid ]; then
    kill $(cat .bot.pid) 2>/dev/null
    rm .bot.pid
    echo "✅ Discord Botを停止しました"
fi

# Obsidianサーバーを停止
./stop.sh

echo "✨ すべてのシステムが停止しました"