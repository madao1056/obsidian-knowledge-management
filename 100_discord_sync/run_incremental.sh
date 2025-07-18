#!/bin/bash

# Discord増分収集スクリプト

echo "🔄 Discord増分収集を開始します..."

# プロジェクトディレクトリに移動
cd "$(dirname "$0")"

# Node.jsで増分収集実行
node incremental_collector.js

# 収集後の統計表示
if [ -f "last_collection.json" ]; then
    echo ""
    echo "📊 収集統計:"
    cat last_collection.json | jq '.lastStats' 2>/dev/null || echo "jqコマンドがインストールされていません"
fi

# 月報生成（オプション）
read -p "📋 月報を生成しますか？ (y/N): " generate_report
if [[ $generate_report =~ ^[Yy]$ ]]; then
    echo "📈 月報生成中..."
    python3 monthly_report_analyzer.py
fi

echo "✅ 増分収集完了"