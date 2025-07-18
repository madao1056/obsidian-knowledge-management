#!/usr/bin/env python3
"""
Discord連携を1コマンドで実行
これを実行するだけで、セットアップ→起動→テストまで全自動
"""

import subprocess
import os
import time
from pathlib import Path

def main():
    os.chdir(Path(__file__).parent / "100_discord_sync")
    
    print("🚀 Discord-Obsidian連携システムを起動します\n")
    
    # 1. セットアップが必要かチェック
    if not (Path("venv").exists() and Path("config.json").exists()):
        print("📦 初回セットアップを実行します...")
        subprocess.run(["python3", "setup.py"])
        print("\n")
    
    # 2. npmパッケージがインストールされているかチェック
    if not Path("node_modules").exists():
        print("📦 Discord Bot用パッケージをインストールします...")
        subprocess.run(["npm", "install"])
        print("\n")
    
    # 2. すべてのシステムを起動
    print("🌟 システムを起動しています...")
    subprocess.run(["bash", "start_all.sh"])
    
    print("\n✨ 準備完了！")
    print("📌 すべてのDiscordメッセージがObsidianに記録されます")
    print("📌 停止するには: ./100_discord_sync/stop_all.sh")
    
    # Discord Bot設定確認
    print("\n⚠️  Discord Developer Portalでボットの設定を完了してください：")
    print("1. https://discord.com/developers/applications")
    print("2. discord_bot.js の BOT_TOKEN を設定")
    print("3. Botをサーバーに招待")

if __name__ == "__main__":
    main()