#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import requests
import json
import time
from pathlib import Path
import subprocess

# 設定読み込み
config_path = Path(__file__).parent / "config.json"
with open(config_path, 'r') as f:
    config = json.load(f)

# テストデータ読み込み
test_path = Path(__file__).parent / "test_data.json"
with open(test_path, 'r') as f:
    test_data = json.load(f)

# Webhook URL
url = f"http://localhost:{config['server_port']}/webhook/discord"
headers = {
    "Authorization": f"Bearer {config['webhook_token']}",
    "Content-Type": "application/json"
}

print("🧪 テストを開始します...")
print(f"📡 送信先: {url}")

# 各種データを送信
for data_type, payload in test_data.items():
    print(f"\n📤 {data_type} を送信中...")
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            print(f"✅ {data_type} 送信成功: {response.json()}")
        else:
            print(f"❌ {data_type} 送信失敗: {response.status_code}")
    except Exception as e:
        print(f"❌ エラー: {e}")
    time.sleep(1)

print("\n⏳ 5秒後に処理を実行します...")
time.sleep(5)

# 処理実行
print("\n🔄 処理を実行中...")
venv_python = Path(__file__).parent / "venv" / "bin" / "python"
subprocess.run([str(venv_python), "main_processor.py", "--once"])

print("\n✨ テスト完了！")
print("📁 以下のディレクトリを確認してください:")
print("- 00_Inbox/discord/ (受信したJSON)")
print("- 03_Support/グッサポ・ラボ/メンバー管理/テストユーザー/")
