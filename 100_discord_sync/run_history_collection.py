#!/usr/bin/env python3
"""
Discord履歴収集を実行するPythonスクリプト
"""

import subprocess
import time
import sys
from pathlib import Path
import urllib.request
import urllib.error

def check_server():
    """Obsidianサーバーが起動しているか確認"""
    try:
        with urllib.request.urlopen("http://localhost:8000/", timeout=5) as response:
            return response.status == 200
    except:
        return False

def main():
    print("📚 Discord履歴収集を開始します")
    print("")
    
    # サーバー確認
    if not check_server():
        print("⚠️  Obsidianサーバーが起動していません")
        print("別のターミナルで以下を実行してください：")
        print("cd 100_discord_sync && ./start.sh")
        print("")
        print("または全体を起動：")
        print("python3 run_discord_sync.py")
        sys.exit(1)
    
    print("✅ Obsidianサーバーが稼働中です")
    print("")
    print("📅 2024年5月1日以降のメッセージを収集します")
    print("⚠️  この処理は時間がかかる場合があります（メッセージ数により10分〜1時間）")
    print("")
    
    # 履歴収集を実行
    try:
        process = subprocess.Popen(
            ["node", "discord_history_collector.js"],
            cwd=Path(__file__).parent,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            bufsize=1
        )
        
        # リアルタイムで出力を表示
        for line in iter(process.stdout.readline, ''):
            if line:
                print(line.rstrip())
        
        process.wait()
        
        if process.returncode == 0:
            print("\n✨ 履歴収集が完了しました！")
            print("📁 収集結果は以下に保存されています：")
            print("   03_Support/グッサポ・ラボ/メンバー管理/")
        else:
            print("\n❌ 履歴収集中にエラーが発生しました")
            
    except KeyboardInterrupt:
        print("\n⚠️  ユーザーによって中断されました")
        if 'process' in locals():
            process.terminate()
    except Exception as e:
        print(f"\n❌ エラー: {e}")

if __name__ == "__main__":
    main()