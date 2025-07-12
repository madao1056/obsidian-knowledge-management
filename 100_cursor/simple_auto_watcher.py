#!/usr/bin/env python3
"""
シンプルなクリップフォルダ監視システム
watchdogなしで動作する軽量版
"""

import os
import sys
import time
import logging
import subprocess
from pathlib import Path
from datetime import datetime

class SimpleClipWatcher:
    def __init__(self, vault_path):
        self.vault_path = Path(vault_path)
        self.clip_path = self.vault_path / "00_Inbox" / "clip"
        self.log_dir = self.vault_path / "100_cursor" / "logs"
        self.processed_files = set()  # 処理済みファイルを記録
        self.check_interval = 5  # 5秒ごとにチェック
        
        # ログ設定
        self.setup_logger()
        
        # 初期ファイルリストを取得
        self.initialize_processed_files()
    
    def setup_logger(self):
        """ログシステムを設定"""
        self.log_dir.mkdir(exist_ok=True)
        log_file = self.log_dir / f"simple_watcher_{datetime.now().strftime('%Y%m%d')}.log"
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file, encoding='utf-8'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger('SimpleWatcher')
    
    def initialize_processed_files(self):
        """起動時に既存のファイルを処理済みとして記録"""
        if self.clip_path.exists():
            for file_path in self.clip_path.glob("*.md"):
                self.processed_files.add(str(file_path))
        self.logger.info(f"Initialized with {len(self.processed_files)} existing files")
    
    def check_new_files(self):
        """新しいファイルをチェック"""
        if not self.clip_path.exists():
            return []
        
        new_files = []
        for file_path in self.clip_path.glob("*.md"):
            if str(file_path) not in self.processed_files:
                # ファイルサイズが安定するまで待機
                if self.is_file_ready(file_path):
                    new_files.append(file_path)
        
        return new_files
    
    def is_file_ready(self, file_path):
        """ファイルが完全に書き込まれたかチェック"""
        try:
            # ファイルサイズをチェック
            size1 = file_path.stat().st_size
            time.sleep(1)
            size2 = file_path.stat().st_size
            
            # サイズが変わっていなく、0より大きければOK
            return size1 == size2 and size1 > 0
        except:
            return False
    
    def process_new_clip(self, file_path):
        """新しいクリップを処理"""
        try:
            print(f"\n🔔 New clip detected: {file_path.name}")
            self.logger.info(f"Processing: {file_path.name}")
            
            # auto_article_generator.pyを実行
            script_path = self.vault_path / "100_cursor" / "auto_article_generator.py"
            
            result = subprocess.run(
                [sys.executable, str(script_path)],
                capture_output=True,
                text=True,
                cwd=str(self.vault_path)
            )
            
            if result.returncode == 0:
                # 処理済みとして記録
                self.processed_files.add(str(file_path))
                
                print("✅ Processing completed successfully!")
                self.logger.info(f"Successfully processed: {file_path.name}")
                
                # 結果を表示
                if "Generated" in result.stdout:
                    lines = result.stdout.strip().split('\n')
                    for line in lines[-3:]:
                        if line.strip():
                            print(f"   {line}")
            else:
                self.logger.error(f"Processing failed: {result.stderr}")
                print(f"❌ Processing failed. Check logs.")
                
        except Exception as e:
            self.logger.error(f"Error: {str(e)}")
            print(f"❌ Error: {str(e)}")
    
    def start_watching(self):
        """監視を開始"""
        print(f"""
🚀 Simple Auto Watcher Started
================================
📁 Watching: {self.clip_path}
⏱  Check interval: {self.check_interval} seconds
📝 Log: {self.log_dir}/simple_watcher_{datetime.now().strftime('%Y%m%d')}.log

Waiting for new clips...
Press Ctrl+C to stop.
""")
        
        self.logger.info("Watcher started")
        
        try:
            while True:
                # 新しいファイルをチェック
                new_files = self.check_new_files()
                
                # 新しいファイルがあれば処理
                for file_path in new_files:
                    self.process_new_clip(file_path)
                
                # 次のチェックまで待機
                time.sleep(self.check_interval)
                
        except KeyboardInterrupt:
            print("\n\n👋 Watcher stopped.")
            self.logger.info("Watcher stopped by user")
        except Exception as e:
            self.logger.error(f"Unexpected error: {str(e)}")
            print(f"\n❌ Error: {str(e)}")


def main():
    """メイン関数"""
    vault_path = "/Users/hashiguchimasaki/project/obsidian"
    
    # auto_article_generator.pyの存在確認
    script_path = Path(vault_path) / "100_cursor" / "auto_article_generator.py"
    if not script_path.exists():
        print(f"❌ auto_article_generator.py not found at {script_path}")
        return
    
    # 監視開始
    watcher = SimpleClipWatcher(vault_path)
    watcher.start_watching()


if __name__ == "__main__":
    main()