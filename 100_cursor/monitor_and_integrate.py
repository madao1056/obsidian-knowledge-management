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
