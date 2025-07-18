#!/bin/bash
echo "📚 Discord履歴収集を開始します"
echo ""
echo "📅 2024年5月1日以降のメッセージを収集します"
echo "⚠️  この処理は時間がかかる場合があります（10分〜1時間）"
echo ""

# Node.jsで直接実行
cd "$(dirname "$0")"
node discord_history_collector.js