#!/bin/bash
echo "📚 Discord履歴収集（バッチ版）を開始します"
echo ""
echo "📅 2024年5月1日以降のメッセージを収集します"
echo "💾 Webhookサーバーなしで直接JSONファイルに保存します"
echo ""

cd "$(dirname "$0")"
node discord_history_batch.js