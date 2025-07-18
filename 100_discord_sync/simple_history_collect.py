#!/usr/bin/env python3
"""
シンプルな履歴収集スクリプト
Webhookサーバーを経由せずに直接Obsidianに保存
"""

import json
import os
from datetime import datetime
from pathlib import Path

# 設定
INBOX_PATH = Path(__file__).parent.parent / "00_Inbox" / "discord"
INBOX_PATH.mkdir(parents=True, exist_ok=True)

def save_test_data():
    """テストデータを保存して動作確認"""
    
    # テスト用の日報データ
    test_reports = [
        {
            "type": "daily_report",
            "author": "yukari_web",
            "date": "2024-05-15",
            "timestamp": "2024-05-15T10:00:00Z",
            "content": """【日報】
稼働時間: 5時間

完了タスク:
- LP制作のコーディング
- レスポンシブ対応

課題:
- figmaのデザイン再現が難しい

明日の予定:
- WordPress案件の着手""",
            "raw_data": {
                "author": {"username": "yukari_web"},
                "channel": {"name": "日報"}
            }
        },
        {
            "type": "daily_report", 
            "author": "prog.ji",
            "date": "2024-05-17",
            "timestamp": "2024-05-17T21:00:00Z",
            "content": """本日の活動報告

営業活動:
- 30件送信
- 返信1件

学習:
- AI活用方法の研究

稼働時間: 4時間""",
            "raw_data": {
                "author": {"username": "prog.ji"},
                "channel": {"name": "日報"}
            }
        },
        {
            "type": "daily_report",
            "author": "takanori07", 
            "date": "2024-05-22",
            "timestamp": "2024-05-22T20:00:00Z",
            "content": """【日報】タカノリ

本日の作業:
- 案件A: デザイン修正完了
- 案件B: コーディング50%

営業: 20件送信

稼働時間: 6時間""",
            "raw_data": {
                "author": {"username": "takanori07"},
                "channel": {"name": "日報"}
            }
        }
    ]
    
    # 各データを保存
    saved_count = 0
    for report in test_reports:
        filename = f"{report['author']}_{report['date']}_日報.json"
        filepath = INBOX_PATH / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        print(f"✅ 保存: {filename}")
        saved_count += 1
    
    # 自己紹介データも保存
    introductions = {
        "yukari_web": {
            "type": "daily_report",
            "author": "yukari_web", 
            "date": "2024-05-10",
            "timestamp": "2024-05-10T10:00:00Z",
            "content": """はじめまして！
自己紹介させていただきます✨ 

【名前】
yukari

【SNSアカウント】
X: @yukari_web

【現在の状況】
- Web制作フリーランス1年目
- HTML/CSS/JavaScriptを学習中
- WordPress案件に挑戦中

【目標】
月30万円の安定収入

よろしくお願いします！""",
            "raw_data": {
                "author": {"username": "yukari_web"},
                "channel": {"name": "あなたのこと教えて"}
            }
        },
        "prog.ji": {
            "type": "daily_report",
            "author": "prog.ji",
            "date": "2024-05-11", 
            "timestamp": "2024-05-11T15:00:00Z",
            "content": """お疲れ様です！
自己紹介させていただきます～！

【名前】
ログジ

【経歴】
- 製造業10年
- プログラミング学習6ヶ月
- AI活用に興味あり

【目標】
- Web制作で独立
- AI×Web制作の先駆者になる

よろしくお願いします！""",
            "raw_data": {
                "author": {"username": "prog.ji"},
                "channel": {"name": "あなたのこと教えて"}
            }
        }
    }
    
    for username, intro in introductions.items():
        filename = f"{username}_{intro['date']}_自己紹介.json"
        filepath = INBOX_PATH / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(intro, f, ensure_ascii=False, indent=2)
        
        print(f"✅ 保存: {filename}")
        saved_count += 1
    
    print(f"\n✨ 合計 {saved_count} 件のデータを保存しました")
    print(f"📁 保存先: {INBOX_PATH}")
    
    # 処理を促す
    print("\n📝 次のステップ:")
    print("1. メインプロセッサーを実行して処理:")
    print("   venv/bin/python main_processor.py --once")
    print("\n2. または手動で処理:")
    print("   venv/bin/python daily_report_analyzer.py")

if __name__ == "__main__":
    save_test_data()