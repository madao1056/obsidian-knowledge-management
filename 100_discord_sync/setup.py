#!/usr/bin/env python3
"""
Discord-Obsidian連携システム 自動セットアップスクリプト
実行するだけですべての設定が完了します
"""

import subprocess
import sys
import os
import json
import secrets
from pathlib import Path

def create_venv():
    """仮想環境を作成"""
    print("🐍 Python仮想環境を作成しています...")
    venv_path = Path(__file__).parent / "venv"
    
    if not venv_path.exists():
        subprocess.check_call([sys.executable, "-m", "venv", str(venv_path)])
        print("✅ 仮想環境作成完了")
    else:
        print("✅ 仮想環境は既に存在します")
    
    return venv_path

def install_requirements():
    """必要なパッケージをインストール"""
    print("📦 必要なパッケージをインストールしています...")
    packages = ["fastapi", "uvicorn", "schedule", "python-multipart"]
    
    venv_path = Path(__file__).parent / "venv"
    pip_path = venv_path / "bin" / "pip" if os.name != 'nt' else venv_path / "Scripts" / "pip.exe"
    
    for package in packages:
        try:
            subprocess.check_call([str(pip_path), "install", package])
            print(f"✅ {package} インストール完了")
        except subprocess.CalledProcessError:
            print(f"❌ {package} のインストールに失敗しました")
            return False
    return True

def create_config():
    """設定ファイルを自動生成"""
    print("\n🔧 設定ファイルを作成しています...")
    
    # ランダムなトークンを生成
    token = secrets.token_urlsafe(32)
    
    config = {
        "webhook_token": token,
        "server_port": 8000,
        "auto_start": True,
        "schedule": {
            "enabled": True,
            "times": ["09:00", "21:00"]
        }
    }
    
    config_path = Path(__file__).parent / "config.json"
    with open(config_path, 'w', encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 設定ファイル作成完了")
    print(f"📝 Webhook Token: {token}")
    print(f"   (このトークンは config.json に保存されました)")
    
    return config

def create_directories():
    """必要なディレクトリを作成"""
    print("\n📁 ディレクトリ構造を作成しています...")
    
    base_path = Path(__file__).parent.parent
    directories = [
        "00_Inbox/discord",
        "03_Support/グッサポ・ラボ/メンバー管理",
        "03_Support/グッサポ・ラボ/個別面談記録",
        "30_Permanent/34_Product/グッサポ・ラボ"
    ]
    
    for dir_path in directories:
        full_path = base_path / dir_path
        full_path.mkdir(parents=True, exist_ok=True)
        print(f"✅ {dir_path}")
    
    return True

def create_start_script():
    """起動スクリプトを作成"""
    print("\n🚀 起動スクリプトを作成しています...")
    
    venv_python = "venv/bin/python" if os.name != 'nt' else "venv\\Scripts\\python.exe"
    
    # start.sh for Unix/Mac
    start_sh = f"""#!/bin/bash
echo "🚀 Discord-Obsidian連携システムを起動します..."

# 仮想環境をアクティベート
source venv/bin/activate

# Webhookサーバーを起動
echo "📡 Webhookサーバーを起動中..."
{venv_python} webhook_server.py &
WEBHOOK_PID=$!
echo "✅ WebhookサーバーPID: $WEBHOOK_PID"

# 少し待機
sleep 3

# メインプロセッサーをデーモンモードで起動
echo "🔄 自動処理デーモンを起動中..."
{venv_python} main_processor.py --daemon &
PROCESSOR_PID=$!
echo "✅ プロセッサーPID: $PROCESSOR_PID"

echo ""
echo "✨ システムが正常に起動しました！"
echo ""
echo "📌 Webhook URL: http://localhost:8000/webhook/discord"
echo "📌 ステータス確認: http://localhost:8000/"
echo ""
echo "停止するには: ./stop.sh または kill $WEBHOOK_PID $PROCESSOR_PID"
echo ""

# PIDをファイルに保存
echo "$WEBHOOK_PID" > .webhook.pid
echo "$PROCESSOR_PID" > .processor.pid
"""
    
    start_path = Path(__file__).parent / "start.sh"
    with open(start_path, 'w') as f:
        f.write(start_sh)
    os.chmod(start_path, 0o755)
    
    # stop.sh
    stop_sh = """#!/bin/bash
echo "🛑 Discord-Obsidian連携システムを停止します..."

if [ -f .webhook.pid ]; then
    kill $(cat .webhook.pid) 2>/dev/null
    rm .webhook.pid
    echo "✅ Webhookサーバーを停止しました"
fi

if [ -f .processor.pid ]; then
    kill $(cat .processor.pid) 2>/dev/null
    rm .processor.pid
    echo "✅ プロセッサーを停止しました"
fi

echo "✨ システムが停止しました"
"""
    
    stop_path = Path(__file__).parent / "stop.sh"
    with open(stop_path, 'w') as f:
        f.write(stop_sh)
    os.chmod(stop_path, 0o755)
    
    print("✅ 起動/停止スクリプト作成完了")
    return True

def create_test_data():
    """テストデータを作成"""
    print("\n🧪 テストデータを作成しています...")
    
    test_data = {
        "daily_report": {
            "type": "daily_report",
            "data": {
                "author": {"username": "テストユーザー"},
                "content": """【本日の日報】
稼働時間: 6時間

完了タスク:
- Obsidian連携システムのテスト
- ドキュメント作成
- バグ修正3件

営業活動:
- 営業メール20件送信

課題:
- APIレスポンスが遅い時がある

明日の予定:
- パフォーマンス改善
- 新機能の実装""",
                "timestamp": "2025-07-18T21:00:00Z"
            }
        },
        "question": {
            "type": "question",
            "data": {
                "author": {"username": "テストユーザー"},
                "content": "FastAPIでCORS設定はどうすればいいですか？",
                "timestamp": "2025-07-18T20:30:00Z"
            }
        },
        "progress": {
            "type": "progress",
            "data": {
                "author": {"username": "テストユーザー"},
                "content": """【進捗報告】
Discord連携システムの基本機能が完成しました！

達成したこと:
- Webhook受信機能
- 自動解析機能
- Obsidian連携

学んだこと:
- FastAPIの使い方
- 非同期処理の重要性""",
                "timestamp": "2025-07-18T19:00:00Z"
            }
        }
    }
    
    test_path = Path(__file__).parent / "test_data.json"
    with open(test_path, 'w', encoding='utf-8') as f:
        json.dump(test_data, f, ensure_ascii=False, indent=2)
    
    print("✅ テストデータ作成完了")
    return test_data

def create_test_script():
    """テスト実行スクリプトを作成"""
    print("\n🧪 テストスクリプトを作成しています...")
    
    test_script = """#!/usr/bin/env python3
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
    print(f"\\n📤 {data_type} を送信中...")
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            print(f"✅ {data_type} 送信成功: {response.json()}")
        else:
            print(f"❌ {data_type} 送信失敗: {response.status_code}")
    except Exception as e:
        print(f"❌ エラー: {e}")
    time.sleep(1)

print("\\n⏳ 5秒後に処理を実行します...")
time.sleep(5)

# 処理実行
print("\\n🔄 処理を実行中...")
venv_python = Path(__file__).parent / "venv" / "bin" / "python"
subprocess.run([str(venv_python), "main_processor.py", "--once"])

print("\\n✨ テスト完了！")
print("📁 以下のディレクトリを確認してください:")
print("- 00_Inbox/discord/ (受信したJSON)")
print("- 03_Support/グッサポ・ラボ/メンバー管理/テストユーザー/")
"""
    
    test_script_path = Path(__file__).parent / "test.py"
    with open(test_script_path, 'w') as f:
        f.write(test_script)
    os.chmod(test_script_path, 0o755)
    
    print("✅ テストスクリプト作成完了")

def create_simple_guide():
    """簡単な使い方ガイドを作成"""
    guide = """
# 🎉 セットアップ完了！

## 📌 使い方

### 1. システムを起動
```bash
./start.sh
```

### 2. テストを実行（オプション）
```bash
python3 test.py
```

### 3. システムを停止
```bash
./stop.sh
```

## 📡 Discord側の設定

以下の情報をDiscord Botに設定してください：

- **Webhook URL**: http://localhost:8000/webhook/discord
- **認証トークン**: config.json を確認
- **送信形式**: README.md のサンプルを参照

## 🔄 自動実行

システムは毎日 9:00 と 21:00 に自動的に処理を実行します。

## 📁 生成されるファイル

- `03_Support/グッサポ・ラボ/メンバー管理/` - メンバー情報
- `30_Permanent/34_Product/グッサポ・ラボ/` - ナレッジベース

---
詳細は README.md をご覧ください。
"""
    
    guide_path = Path(__file__).parent / "QUICK_START.md"
    with open(guide_path, 'w') as f:
        f.write(guide)
    
    print("\n📖 クイックスタートガイドを作成しました: QUICK_START.md")

def main():
    print("🚀 Discord-Obsidian連携システム セットアップを開始します\n")
    
    # 0. 仮想環境作成
    venv_path = create_venv()
    
    # 1. パッケージインストール
    if not install_requirements():
        print("\n❌ セットアップに失敗しました")
        return
    
    # 2. 設定ファイル作成
    config = create_config()
    
    # 3. ディレクトリ作成
    create_directories()
    
    # 4. 起動スクリプト作成
    create_start_script()
    
    # 5. テストデータ作成
    create_test_data()
    
    # 6. テストスクリプト作成
    create_test_script()
    
    # 7. ガイド作成
    create_simple_guide()
    
    print("\n" + "="*50)
    print("✨ セットアップが完了しました！")
    print("="*50)
    print("\n📌 次のステップ:")
    print("1. ./start.sh でシステムを起動")
    print("2. python3 test.py でテスト実行（オプション）")
    print("3. QUICK_START.md で詳細を確認")
    print("\n🔑 Webhook Token:", config["webhook_token"])
    print("   (このトークンをDiscord側に設定してください)")

if __name__ == "__main__":
    main()