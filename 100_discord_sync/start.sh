#!/bin/bash
echo "🚀 Discord-Obsidian連携システムを起動します..."

# 仮想環境をアクティベート
source venv/bin/activate

# Webhookサーバーを起動
echo "📡 Webhookサーバーを起動中..."
venv/bin/python webhook_server.py &
WEBHOOK_PID=$!
echo "✅ WebhookサーバーPID: $WEBHOOK_PID"

# 少し待機
sleep 3

# メインプロセッサーをデーモンモードで起動
echo "🔄 自動処理デーモンを起動中..."
venv/bin/python main_processor.py --daemon &
PROCESSOR_PID=$!
echo "✅ プロセッサーPID: $PROCESSOR_PID"

echo ""
echo "✨ システムが正常に起動しました！"
echo ""
echo "📌 Webhook URL: http://localhost:8000/webhook/discord"
echo "📌 ステータス確認: http://localhost:8000/"
echo ""
echo "停止するには: ./stop.sh または kill $WEBHOOK_PID $PROCESSOR_PID"
echo ""

# PIDをファイルに保存
echo "$WEBHOOK_PID" > .webhook.pid
echo "$PROCESSOR_PID" > .processor.pid
