#!/usr/bin/env python3
"""
Notionプレースホルダーファイルを自動的にすべて処理するスクリプト
"""
import os
import sys
import time
import subprocess
from datetime import datetime

# 設定
SCRIPT_PATH = "/Users/hashiguchimasaki/project/obsidian/100_cursor/notion_batch_content_fetcher_v2.py"
VENV_ACTIVATE = "/Users/hashiguchimasaki/project/obsidian/notion_sync_env/bin/activate"
LOG_FILE = "/Users/hashiguchimasaki/project/obsidian/100_cursor/auto_sync.log"
MAX_ITERATIONS = 100  # 最大実行回数（無限ループ防止）
BATCH_DELAY = 5  # バッチ間の待機時間（秒）

def log_message(message):
    """ログメッセージを出力"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}"
    print(log_entry)
    
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(log_entry + "\n")

def run_batch_sync():
    """バッチ同期を実行"""
    cmd = f"source {VENV_ACTIVATE} && python3 {SCRIPT_PATH}"
    
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=300  # 5分でタイムアウト
        )
        
        if result.returncode == 0:
            output = result.stdout
            
            # 残りファイル数を抽出
            remaining = None
            for line in output.split('\n'):
                if "Remaining:" in line:
                    try:
                        remaining = int(line.split("Remaining:")[1].split("files")[0].strip())
                    except:
                        pass
            
            # 成功/失敗数を抽出
            success = 0
            failed = 0
            for line in output.split('\n'):
                if "This batch:" in line:
                    try:
                        parts = line.split("This batch:")[1].strip()
                        success = int(parts.split("success")[0].strip())
                        failed = int(parts.split("success,")[1].split("failed")[0].strip())
                    except:
                        pass
            
            return True, remaining, success, failed, output
        else:
            error_msg = f"Error: {result.stderr}"
            return False, None, 0, 0, error_msg
            
    except subprocess.TimeoutExpired:
        return False, None, 0, 0, "Timeout expired"
    except Exception as e:
        return False, None, 0, 0, str(e)

def main():
    """メイン処理"""
    log_message("=" * 60)
    log_message("Auto Notion Sync Started")
    log_message("=" * 60)
    
    iteration = 0
    total_success = 0
    total_failed = 0
    start_time = time.time()
    
    while iteration < MAX_ITERATIONS:
        iteration += 1
        log_message(f"\nIteration {iteration} starting...")
        
        # バッチ同期を実行
        success, remaining, batch_success, batch_failed, output = run_batch_sync()
        
        if not success:
            log_message(f"Error in iteration {iteration}: {output}")
            break
        
        # 統計を更新
        total_success += batch_success
        total_failed += batch_failed
        
        log_message(f"Iteration {iteration} completed: {batch_success} success, {batch_failed} failed")
        
        # 残りファイルがない場合は終了
        if remaining is None or remaining == 0:
            log_message("\nAll files processed!")
            break
        
        log_message(f"Remaining files: {remaining}")
        
        # 進捗率を計算して表示
        if total_success + total_failed > 0:
            progress = (total_success + total_failed) / (total_success + total_failed + remaining) * 100
            log_message(f"Progress: {progress:.1f}%")
        
        # レート制限を考慮して待機
        log_message(f"Waiting {BATCH_DELAY} seconds before next batch...")
        time.sleep(BATCH_DELAY)
    
    # 最終統計
    elapsed_time = time.time() - start_time
    log_message("\n" + "=" * 60)
    log_message("FINAL SUMMARY")
    log_message("=" * 60)
    log_message(f"Total iterations: {iteration}")
    log_message(f"Total success: {total_success}")
    log_message(f"Total failed: {total_failed}")
    log_message(f"Total time: {elapsed_time/60:.1f} minutes")
    
    if total_success > 0:
        log_message(f"Average time per file: {elapsed_time/total_success:.1f} seconds")

if __name__ == "__main__":
    # プロセスの実行確認
    print("This script will automatically process all Notion placeholder files.")
    print("It may take several hours to complete.")
    print("Progress will be logged to:", LOG_FILE)
    print("\nPress Ctrl+C to stop at any time.")
    
    response = input("\nDo you want to continue? (y/n): ")
    if response.lower() == 'y':
        try:
            main()
        except KeyboardInterrupt:
            print("\n\nProcess interrupted by user.")
            log_message("Process interrupted by user.")
    else:
        print("Process cancelled.")