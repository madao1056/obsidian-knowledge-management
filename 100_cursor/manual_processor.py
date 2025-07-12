#!/usr/bin/env python3
"""
手動実行用の軽量クリップ処理スクリプト
コマンド一発で全自動処理を実行
"""

import sys
import subprocess
from pathlib import Path
from datetime import datetime

def process_clips():
    """クリップを処理して記事まで生成"""
    vault_path = Path("/Users/hashiguchimasaki/project/obsidian")
    clip_path = vault_path / "00_Inbox" / "clip"
    
    # クリップファイルの確認
    clips = list(clip_path.glob("*.md"))
    if not clips:
        print("📭 No clips to process.")
        return
    
    print(f"📋 Found {len(clips)} clip(s) to process")
    for clip in clips:
        print(f"  - {clip.name}")
    
    print("\n⚙️  Starting processing...")
    
    # auto_article_generator.pyを実行
    script_path = vault_path / "100_cursor" / "auto_article_generator.py"
    
    try:
        result = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=True,
            text=True,
            cwd=str(vault_path)
        )
        
        if result.returncode == 0:
            print("✅ Processing completed successfully!")
            # 結果を表示
            output_lines = result.stdout.strip().split('\n')
            for line in output_lines[-5:]:
                if "Generated" in line or "Created" in line:
                    print(f"   {line}")
        else:
            print("❌ Processing failed:")
            print(result.stderr)
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")

def main():
    """メイン関数"""
    print(f"""
🚀 Manual Clip Processor
=======================
Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
""")
    
    process_clips()
    print("\n✨ Done!")

if __name__ == "__main__":
    main()