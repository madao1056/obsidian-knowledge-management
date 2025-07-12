#!/bin/bash
# Notion全ページ同期スクリプト

cd /Users/hashiguchimasaki/project/obsidian

# 仮想環境を有効化
source venv/bin/activate

# 同期を実行
echo "Starting Notion sync at $(date)"
python 100_cursor/simple_notion_sync.py

# ログに記録
echo "Sync completed at $(date)" >> 100_cursor/logs/notion_sync.log

# Git に変更をコミット（オプション）
# git add 20_Literature/25_Notion/
# git commit -m "Auto-sync from Notion $(date +%Y%m%d_%H%M%S)"