#!/bin/bash
echo "🚀 サーバー起動と履歴収集を一括実行します"
echo ""

# サーバーを起動
echo "📡 Webhookサーバーを起動中..."
cd "$(dirname "$0")"
venv/bin/python webhook_server.py &
SERVER_PID=$!
echo "✅ サーバーPID: $SERVER_PID"

# サーバーの起動を待つ
echo "⏳ サーバーの起動を待っています..."
sleep 5

# サーバーの確認
curl -s http://localhost:8000/ > /dev/null
if [ $? -eq 0 ]; then
    echo "✅ サーバーが正常に起動しました"
    echo ""
    echo "📚 履歴収集を開始します..."
    echo ""
    
    # 履歴収集を実行
    node discord_history_collector.js
    
    # サーバーを停止
    echo ""
    echo "🛑 サーバーを停止します..."
    kill $SERVER_PID 2>/dev/null
    
else
    echo "❌ サーバーの起動に失敗しました"
    kill $SERVER_PID 2>/dev/null
fi