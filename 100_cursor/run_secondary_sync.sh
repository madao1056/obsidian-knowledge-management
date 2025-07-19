#!/bin/bash
# Secondary Notion自動同期をバックグラウンドで実行するスクリプト

cd /Users/hashiguchimasaki/project/obsidian
source notion_sync_env/bin/activate

# ログファイルのパス
LOG_FILE="/Users/hashiguchimasaki/project/obsidian/100_cursor/secondary_sync_background.log"

echo "Starting Secondary Notion auto sync in background..." > "$LOG_FILE"
echo "Started at: $(date)" >> "$LOG_FILE"

# nohupでバックグラウンド実行
nohup python3 100_cursor/auto_secondary_sync.py >> "$LOG_FILE" 2>&1 &

# プロセスIDを記録
PID=$!
echo "Process ID: $PID" >> "$LOG_FILE"
echo "$PID" > /Users/hashiguchimasaki/project/obsidian/100_cursor/secondary_sync_pid.txt

echo "Secondary Notion auto sync started in background with PID: $PID"
echo "Check progress with: tail -f $LOG_FILE"
echo "Stop with: kill $PID"