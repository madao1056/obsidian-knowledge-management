#!/usr/bin/env python3
"""
超軽量なクリップ監視スクリプト
- チェック間隔を長めに設定（30秒）
- CPU使用率を最小限に
- メモリ使用量を削減
"""

import os
import sys
import time
import subprocess
from pathlib import Path
from datetime import datetime

class LightweightWatcher:
    def __init__(self, vault_path):
        self.vault_path = Path(vault_path)
        self.clip_path = self.vault_path / "00_Inbox" / "clip"
        self.processed_files = set()
        self.check_interval = 30  # 30秒ごとにチェック（CPU負荷軽減）
        
        # 初期ファイルを記録
        if self.clip_path.exists():
            for f in self.clip_path.glob("*.md"):
                self.processed_files.add(f.name)
    
    def check_and_process(self):
        """新しいファイルをチェックして処理"""
        if not self.clip_path.exists():
            return
        
        new_files = []
        for file_path in self.clip_path.glob("*.md"):
            if file_path.name not in self.processed_files:
                # ファイルが完全に書き込まれたか確認
                try:
                    size1 = file_path.stat().st_size
                    time.sleep(1)
                    size2 = file_path.stat().st_size
                    
                    if size1 == size2 and size1 > 0:
                        new_files.append(file_path)
                except:
                    pass
        
        if new_files:
            print(f"\n🔔 {len(new_files)} new clip(s) detected!")
            
            # auto_article_generator.pyを実行
            script_path = self.vault_path / "100_cursor" / "auto_article_generator.py"
            
            try:
                result = subprocess.run(
                    [sys.executable, str(script_path)],
                    capture_output=True,
                    text=True,
                    cwd=str(self.vault_path)
                )
                
                if result.returncode == 0:
                    print("✅ Processed successfully!")
                    # 処理済みとして記録
                    for f in new_files:
                        self.processed_files.add(f.name)
                else:
                    print("❌ Processing failed")
                    
            except Exception as e:
                print(f"❌ Error: {str(e)}")
    
    def run(self):
        """監視を開始"""
        print(f"""
🌿 Lightweight Watcher Started
==============================
📁 Watching: {self.clip_path}
⏱  Check interval: {self.check_interval} seconds
💡 Low CPU usage mode

Press Ctrl+C to stop.
""")
        
        try:
            while True:
                self.check_and_process()
                time.sleep(self.check_interval)
                
        except KeyboardInterrupt:
            print("\n\n👋 Watcher stopped.")

def main():
    vault_path = "/Users/hashiguchimasaki/project/obsidian"
    watcher = LightweightWatcher(vault_path)
    watcher.run()

if __name__ == "__main__":
    main()