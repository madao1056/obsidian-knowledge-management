#!/bin/bash
echo "📚 Discord履歴収集を開始します"
echo ""
echo "⚠️  この処理は時間がかかる場合があります"
echo "過去30日分のメッセージを収集します"
echo ""

# Obsidianサーバーが起動しているか確認
curl -s http://localhost:8000/ > /dev/null
if [ $? -ne 0 ]; then
    echo "❌ Obsidianサーバーが起動していません"
    echo "先に ./start.sh を実行してください"
    exit 1
fi

echo "✅ Obsidianサーバーが稼働中です"
echo ""
echo "📥 履歴収集を開始します..."
echo ""

# 履歴収集スクリプトを実行
node discord_history_collector.js