#!/usr/bin/env python3
"""
Notion同期プロセスのリアルタイム監視ツール
"""
import os
import json
import time
import subprocess
from datetime import datetime
from pathlib import Path

# 設定
BASE_DIR = "/Users/hashiguchimasaki/project/obsidian"
LOG_FILES = {
    "main": "100_cursor/main_final_sync.log",
    "secondary": "100_cursor/secondary_final_sync.log",
    "integration": "100_cursor/integration.log"
}
STATE_FILES = {
    "main": "100_cursor/.batch_fetch_state_v2.json",
    "secondary": "100_cursor/.secondary_fetch_state.json"
}

class SyncMonitor:
    def __init__(self):
        self.last_positions = {}
        
    def check_processes(self):
        """実行中のプロセスをチェック"""
        processes = {}
        
        try:
            # Mainプロセスチェック
            result = subprocess.run(['pgrep', '-f', 'auto_notion_sync_headless.py'], 
                                  capture_output=True, text=True)
            processes['main'] = result.returncode == 0
            
            # Secondaryプロセスチェック
            result = subprocess.run(['pgrep', '-f', 'auto_secondary_sync.py'], 
                                  capture_output=True, text=True)
            processes['secondary'] = result.returncode == 0
            
            # Monitorプロセスチェック
            result = subprocess.run(['pgrep', '-f', 'monitor_and_integrate.py'], 
                                  capture_output=True, text=True)
            processes['monitor'] = result.returncode == 0
            
        except Exception as e:
            print(f"プロセスチェックエラー: {e}")
            
        return processes
    
    def read_state_file(self, state_file):
        """状態ファイルを読み込み"""
        try:
            state_path = os.path.join(BASE_DIR, state_file)
            if os.path.exists(state_path):
                with open(state_path, 'r') as f:
                    return json.load(f)
        except Exception as e:
            print(f"状態ファイル読み込みエラー {state_file}: {e}")
        return {}
    
    def get_sync_statistics(self):
        """同期統計を取得"""
        stats = {}
        
        for sync_type, state_file in STATE_FILES.items():
            state = self.read_state_file(state_file)
            if state:
                stats[sync_type] = {
                    "total_files": len(state.get("processed", [])) + len(state.get("failed", [])) + len(state.get("remaining", [])),
                    "processed": len(state.get("processed", [])),
                    "failed": len(state.get("failed", [])),
                    "remaining": len(state.get("remaining", [])),
                    "success_rate": 0
                }
                
                total = stats[sync_type]["processed"] + stats[sync_type]["failed"]
                if total > 0:
                    stats[sync_type]["success_rate"] = (stats[sync_type]["processed"] / total) * 100
                    
                # 進捗率計算
                if stats[sync_type]["total_files"] > 0:
                    stats[sync_type]["progress"] = ((stats[sync_type]["processed"] + stats[sync_type]["failed"]) / stats[sync_type]["total_files"]) * 100
                else:
                    stats[sync_type]["progress"] = 0
        
        return stats
    
    def get_latest_log_entries(self, log_file, lines=5):
        """ログファイルの最新エントリを取得"""
        try:
            log_path = os.path.join(BASE_DIR, log_file)
            if os.path.exists(log_path):
                with open(log_path, 'r', encoding='utf-8') as f:
                    all_lines = f.readlines()
                    return all_lines[-lines:] if all_lines else []
        except Exception as e:
            print(f"ログ読み込みエラー {log_file}: {e}")
        return []
    
    def display_status(self):
        """現在のステータスを表示"""
        os.system('clear')  # ターミナルをクリア
        
        print("=" * 80)
        print("🚀 Notion同期プロセス リアルタイム監視")
        print("=" * 80)
        print(f"更新時刻: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        
        # プロセス状況
        processes = self.check_processes()
        print("📊 プロセス状況:")
        for process_name, is_running in processes.items():
            status = "🟢 実行中" if is_running else "🔴 停止中"
            print(f"  {process_name.title()}: {status}")
        print()
        
        # 同期統計
        stats = self.get_sync_statistics()
        print("📈 同期進捗:")
        
        for sync_type, stat in stats.items():
            print(f"\n  {sync_type.title()}アカウント:")
            print(f"    総ファイル数: {stat['total_files']:,}")
            print(f"    処理済み: {stat['processed']:,}")
            print(f"    失敗: {stat['failed']:,}")
            print(f"    残り: {stat['remaining']:,}")
            print(f"    進捗率: {stat['progress']:.1f}%")
            print(f"    成功率: {stat['success_rate']:.1f}%")
            
            # プログレスバー
            progress_width = 40
            filled = int(progress_width * stat['progress'] / 100)
            bar = "█" * filled + "░" * (progress_width - filled)
            print(f"    [{bar}] {stat['progress']:.1f}%")
        
        print()
        
        # 最新ログ
        print("📋 最新ログ:")
        for log_name, log_file in LOG_FILES.items():
            if os.path.exists(os.path.join(BASE_DIR, log_file)):
                print(f"\n  {log_name.title()}:")
                recent_logs = self.get_latest_log_entries(log_file, 3)
                for log_line in recent_logs:
                    print(f"    {log_line.strip()}")
        
        print()
        print("=" * 80)
        print("💡 Ctrl+C で監視を終了")
        print("=" * 80)
    
    def monitor_loop(self):
        """監視ループ"""
        try:
            while True:
                self.display_status()
                time.sleep(10)  # 10秒ごとに更新
        except KeyboardInterrupt:
            print("\n\n監視を終了しました。")

def main():
    monitor = SyncMonitor()
    monitor.monitor_loop()

if __name__ == "__main__":
    main()