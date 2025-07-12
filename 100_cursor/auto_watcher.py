#!/usr/bin/env python3
"""
クリップフォルダ監視 & 自動記事生成システム
新しいファイルが追加されたら自動的に処理を開始
"""

import os
import sys
import time
import logging
from pathlib import Path
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

class ClipWatcher(FileSystemEventHandler):
    def __init__(self, vault_path):
        self.vault_path = Path(vault_path)
        self.clip_path = self.vault_path / "00_Inbox" / "clip"
        self.log_dir = self.vault_path / "100_cursor" / "logs"
        self.processing = set()  # 処理中のファイルを追跡
        
        # ログ設定
        self.setup_logger()
        
    def setup_logger(self):
        """ログシステムを設定"""
        self.log_dir.mkdir(exist_ok=True)
        log_file = self.log_dir / f"auto_watcher_{datetime.now().strftime('%Y%m%d')}.log"
        
        self.logger = logging.getLogger('AutoWatcher')
        self.logger.setLevel(logging.INFO)
        
        # ファイルハンドラー
        fh = logging.FileHandler(log_file, encoding='utf-8')
        fh.setLevel(logging.INFO)
        
        # コンソールハンドラー
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        
        # フォーマット
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
    
    def on_created(self, event):
        """ファイルが作成されたときの処理"""
        if event.is_directory:
            return
            
        file_path = Path(event.src_path)
        
        # .mdファイルのみ処理
        if file_path.suffix != '.md':
            return
        
        # 処理中のファイルはスキップ
        if str(file_path) in self.processing:
            return
            
        self.logger.info(f"New file detected: {file_path.name}")
        print(f"\n🔔 New clip detected: {file_path.name}")
        
        # ファイルが完全に書き込まれるまで待機
        time.sleep(2)
        
        # ファイルサイズをチェック（書き込み完了確認）
        if not self.is_file_ready(file_path):
            self.logger.warning(f"File not ready: {file_path.name}")
            return
        
        # 自動処理を開始
        self.process_new_clip(file_path)
    
    def on_modified(self, event):
        """ファイルが変更されたときの処理"""
        # 新規作成時にもmodifiedイベントが発生することがあるため
        # ここでは特に処理しない
        pass
    
    def is_file_ready(self, file_path):
        """ファイルが完全に書き込まれたかチェック"""
        try:
            # ファイルサイズを2回チェック
            size1 = file_path.stat().st_size
            time.sleep(0.5)
            size2 = file_path.stat().st_size
            
            # サイズが変わっていなければ書き込み完了
            return size1 == size2 and size1 > 0
        except:
            return False
    
    def process_new_clip(self, file_path):
        """新しいクリップを処理"""
        try:
            self.processing.add(str(file_path))
            
            print("⚙️  Starting automatic processing...")
            self.logger.info(f"Processing file: {file_path.name}")
            
            # auto_article_generator.pyを実行
            script_path = self.vault_path / "100_cursor" / "auto_article_generator.py"
            
            result = subprocess.run(
                [sys.executable, str(script_path)],
                capture_output=True,
                text=True,
                cwd=str(self.vault_path)
            )
            
            if result.returncode == 0:
                self.logger.info("Processing completed successfully")
                print("✅ Processing completed successfully!")
                
                # 成功メッセージを解析
                if "Generated" in result.stdout:
                    print(result.stdout.split('\n')[-2])  # 結果サマリーを表示
            else:
                self.logger.error(f"Processing failed: {result.stderr}")
                print(f"❌ Processing failed. Check logs for details.")
                
        except Exception as e:
            self.logger.error(f"Error processing file: {str(e)}")
            print(f"❌ Error: {str(e)}")
        finally:
            self.processing.discard(str(file_path))
    
    def start_watching(self):
        """監視を開始"""
        observer = Observer()
        observer.schedule(self, str(self.clip_path), recursive=False)
        observer.start()
        
        print(f"""
🚀 Auto Watcher Started
========================
📁 Watching: {self.clip_path}
📝 Log file: {self.log_dir}/auto_watcher_{datetime.now().strftime('%Y%m%d')}.log

Waiting for new clips...
Press Ctrl+C to stop.
""")
        
        self.logger.info(f"Started watching: {self.clip_path}")
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
            print("\n👋 Watcher stopped.")
            self.logger.info("Watcher stopped by user")
        
        observer.join()


def check_dependencies():
    """依存関係をチェック"""
    try:
        import watchdog
    except ImportError:
        print("❌ watchdog package not installed.")
        print("Please run: pip install watchdog")
        return False
    
    # auto_article_generator.pyの存在確認
    vault_path = Path("/Users/hashiguchimasaki/project/obsidian")
    script_path = vault_path / "100_cursor" / "auto_article_generator.py"
    
    if not script_path.exists():
        print(f"❌ auto_article_generator.py not found at {script_path}")
        return False
    
    return True


def main():
    """メイン関数"""
    if not check_dependencies():
        return
    
    vault_path = "/Users/hashiguchimasaki/project/obsidian"
    watcher = ClipWatcher(vault_path)
    
    try:
        watcher.start_watching()
    except Exception as e:
        print(f"❌ Error starting watcher: {str(e)}")
        return


if __name__ == "__main__":
    main()