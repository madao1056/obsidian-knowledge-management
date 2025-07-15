#!/usr/bin/env python3
"""
手動実行用の軽量クリップ処理スクリプト
コマンド一発で全自動処理を実行
"""

from pathlib import Path
from datetime import datetime
from typing import List

from utils import run_python_script


def process_clips() -> None:
    """クリップを処理して記事まで生成"""
    vault_path = Path("/Users/hashiguchimasaki/project/obsidian")
    clip_path = vault_path / "00_Inbox" / "clip"
    
    # クリップファイルの確認
    clips: List[Path] = list(clip_path.glob("*.md"))
    if not clips:
        print("📭 No clips to process.")
        return
    
    print(f"📋 Found {len(clips)} clip(s) to process")
    for clip in clips:
        print(f"  - {clip.name}")
    
    print("\n⚙️  Starting processing...")
    
    # auto_article_generator.pyを実行
    script_path = vault_path / "100_cursor" / "auto_article_generator.py"
    
    success, stdout, stderr = run_python_script(script_path, vault_path)
    
    if success:
        print("✅ Processing completed successfully!")
        # 結果を表示
        output_lines = stdout.strip().split('\n')
        for line in output_lines[-5:]:
            if "Generated" in line or "Created" in line:
                print(f"   {line}")
    else:
        print("❌ Processing failed:")
        print(stderr)

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