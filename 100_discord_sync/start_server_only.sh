#!/bin/bash
# サーバーだけを起動（履歴収集用）

echo "📡 Obsidianサーバーのみ起動します..."

# 既存のサーバーを停止
if [ -f .webhook.pid ]; then
    kill $(cat .webhook.pid) 2>/dev/null
    rm .webhook.pid
fi

# Pythonパスを設定
cd "$(dirname "$0")"
PYTHON_BIN="venv/bin/python"

# サーバーを起動
echo "🚀 Webhookサーバーを起動中..."
nohup $PYTHON_BIN webhook_server.py > server.log 2>&1 &
SERVER_PID=$!
echo $SERVER_PID > .webhook.pid

# 起動を待つ
sleep 3

# 確認
if kill -0 $SERVER_PID 2>/dev/null; then
    echo "✅ サーバーが起動しました (PID: $SERVER_PID)"
    echo "📌 URL: http://localhost:8000/"
    echo ""
    echo "📚 履歴収集を実行できます："
    echo "   ./collect_all_history.sh"
else
    echo "❌ サーバーの起動に失敗しました"
    cat server.log
fi