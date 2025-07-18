#!/bin/bash
echo "🛑 Discord-Obsidian連携システムを停止します..."

if [ -f .webhook.pid ]; then
    kill $(cat .webhook.pid) 2>/dev/null
    rm .webhook.pid
    echo "✅ Webhookサーバーを停止しました"
fi

if [ -f .processor.pid ]; then
    kill $(cat .processor.pid) 2>/dev/null
    rm .processor.pid
    echo "✅ プロセッサーを停止しました"
fi

echo "✨ システムが停止しました"
