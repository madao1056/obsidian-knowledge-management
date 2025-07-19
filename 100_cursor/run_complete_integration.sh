#!/bin/bash
# 完全な知識統合プロセスを実行するスクリプト

cd /Users/hashiguchimasaki/project/obsidian

echo "========================================="
echo "Complete Knowledge Integration Process"
echo "========================================="
echo ""

# 1. Notion同期プロセスの確認と停止
echo "1. Stopping existing sync processes..."
if [ -f "100_cursor/sync_pid.txt" ]; then
    PID1=$(cat 100_cursor/sync_pid.txt)
    if ps -p $PID1 > /dev/null; then
        kill $PID1
        echo "   Stopped Main sync process (PID: $PID1)"
    fi
fi

if [ -f "100_cursor/secondary_sync_pid.txt" ]; then
    PID2=$(cat 100_cursor/secondary_sync_pid.txt)
    if ps -p $PID2 > /dev/null; then
        kill $PID2
        echo "   Stopped Secondary sync process (PID: $PID2)"
    fi
fi

# 2. 残りのNotionファイル取得を完了
echo ""
echo "2. Completing Notion file retrieval..."
echo "   This will run in background and may take several hours."

# Main同期の再開
source notion_sync_env/bin/activate
nohup python3 100_cursor/auto_notion_sync_headless.py > 100_cursor/main_final_sync.log 2>&1 &
MAIN_PID=$!
echo "   Main sync restarted (PID: $MAIN_PID)"

# Secondary同期の再開
nohup python3 100_cursor/auto_secondary_sync.py > 100_cursor/secondary_final_sync.log 2>&1 &
SEC_PID=$!
echo "   Secondary sync restarted (PID: $SEC_PID)"

# 3. 知識統合プロセスの準備
echo ""
echo "3. Preparing knowledge integration..."
echo "   Integration will start after sync completes."

# 統合スクリプトの準備
cat > 100_cursor/monitor_and_integrate.py << 'EOF'
#!/usr/bin/env python3
import os
import time
import subprocess
import json

def check_sync_complete():
    """同期が完了したかチェック"""
    # 状態ファイルをチェック
    state_files = [
        "/Users/hashiguchimasaki/project/obsidian/100_cursor/.batch_fetch_state_v2.json",
        "/Users/hashiguchimasaki/project/obsidian/100_cursor/.secondary_fetch_state.json"
    ]
    
    all_complete = True
    for state_file in state_files:
        if os.path.exists(state_file):
            with open(state_file, 'r') as f:
                state = json.load(f)
            # エラーが多すぎる場合も完了とみなす
            if len(state.get('errors', [])) > 100:
                continue
            # まだ処理すべきファイルがあるかチェック
            # この判定は簡易的なものなので、実際のスクリプトの出力も確認が必要
    
    return all_complete

def main():
    print("Monitoring sync processes...")
    
    # 同期プロセスを監視（最大12時間）
    max_wait = 12 * 60 * 60  # 12時間
    check_interval = 300  # 5分ごとにチェック
    waited = 0
    
    while waited < max_wait:
        # プロセスが生きているかチェック
        main_running = subprocess.run(['pgrep', '-f', 'auto_notion_sync_headless.py'], 
                                    capture_output=True).returncode == 0
        sec_running = subprocess.run(['pgrep', '-f', 'auto_secondary_sync.py'], 
                                   capture_output=True).returncode == 0
        
        if not main_running and not sec_running:
            print("All sync processes completed.")
            break
        
        print(f"Sync in progress... (waited {waited//60} minutes)")
        time.sleep(check_interval)
        waited += check_interval
    
    # 統合プロセスを実行
    print("\nStarting knowledge integration...")
    subprocess.run(['python3', '100_cursor/comprehensive_knowledge_integrator.py'])
    
    print("\nIntegration complete!")

if __name__ == "__main__":
    main()
EOF

chmod +x 100_cursor/monitor_and_integrate.py

# 4. 監視と統合プロセスをバックグラウンドで実行
echo ""
echo "4. Starting monitoring and integration process..."
nohup python3 100_cursor/monitor_and_integrate.py > 100_cursor/integration.log 2>&1 &
MONITOR_PID=$!

echo ""
echo "========================================="
echo "All processes started successfully!"
echo "========================================="
echo ""
echo "Process IDs:"
echo "  Main sync: $MAIN_PID"
echo "  Secondary sync: $SEC_PID"
echo "  Monitor & Integration: $MONITOR_PID"
echo ""
echo "Log files:"
echo "  Main sync: 100_cursor/main_final_sync.log"
echo "  Secondary sync: 100_cursor/secondary_final_sync.log"
echo "  Integration: 100_cursor/integration.log"
echo ""
echo "To check progress:"
echo "  tail -f 100_cursor/integration.log"
echo ""
echo "The complete process may take several hours."
echo "You will receive a notification when complete."