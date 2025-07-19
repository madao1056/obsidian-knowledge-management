#!/usr/bin/env python3
"""
カテゴリ別統合処理スクリプト
"""
import os
import shutil
import re
from pathlib import Path
from datetime import datetime

# 設定
BASE_DIR = "/Users/hashiguchimasaki/project/obsidian"
NOTION_DIR = os.path.join(BASE_DIR, "20_Literature/25_Notion")
KNOWLEDGE_BASE_DIR = os.path.join(BASE_DIR, "10_Projects/Knowledge_Base")

# カテゴリ定義
CATEGORIES = {
    "Web制作": {
        "keywords": ["WordPress", "HTML", "CSS", "JavaScript", "PHP", "コーディング", "デザイン", "実装", "レスポンシブ", "サイト"],
        "dir": "02_Web制作",
        "priority": 2
    },
    "マーケティング": {
        "keywords": ["マーケティング", "集客", "SNS", "SEO", "広告", "分析", "戦略", "アクセス", "CVR", "CTR"],
        "dir": "03_マーケティング",
        "priority": 3
    },
    "ビジネス": {
        "keywords": ["ビジネス", "経営", "単価", "営業", "契約", "案件", "クライアント", "売上", "収益", "請求"],
        "dir": "04_ビジネス",
        "priority": 4
    },
    "学習・成長": {
        "keywords": ["学習", "成長", "スキル", "勉強", "習慣", "改善", "PDCA", "目標", "計画", "振り返り"],
        "dir": "05_学習・成長",
        "priority": 5
    },
    "グッサポ・ラボ": {
        "keywords": ["グッサポ", "ラボ", "サポート", "コミュニティ", "Discord", "メンバー", "運営", "コンサル"],
        "dir": "06_グッサポ・ラボ",
        "priority": 6
    },
    "プロジェクト": {
        "keywords": ["プロジェクト", "案件", "制作", "納品", "修正", "進捗", "管理", "スケジュール"],
        "dir": "07_プロジェクト",
        "priority": 7
    }
}

def integrate_category(category_name, category_info):
    """指定カテゴリのファイルを統合"""
    print(f"\n=== {category_name} 統合開始 ===")
    
    # ディレクトリ作成
    category_dir = os.path.join(KNOWLEDGE_BASE_DIR, category_info["dir"])
    os.makedirs(category_dir, exist_ok=True)
    
    # ファイル収集
    matching_files = []
    keywords = category_info["keywords"]
    
    for root, dirs, files in os.walk(NOTION_DIR):
        for filename in files:
            if filename.endswith('.md') and not filename.startswith('.'):
                filepath = os.path.join(root, filename)
                
                # ファイル名チェック
                name_score = sum(1 for keyword in keywords if keyword.lower() in filename.lower())
                
                # 内容チェック（軽量）
                content_score = 0
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read(1000)  # 最初の1000文字
                    content_score = sum(1 for keyword in keywords if keyword.lower() in content.lower())
                except:
                    pass
                
                total_score = name_score * 5 + content_score  # ファイル名により重み
                
                if total_score >= 1:  # スコア1以上なら候補
                    matching_files.append((filepath, total_score))
    
    # スコア順にソート
    matching_files.sort(key=lambda x: x[1], reverse=True)
    
    print(f"見つかったファイル数: {len(matching_files)}")
    
    # ファイルコピー
    copied_count = 0
    for filepath, score in matching_files:
        filename = os.path.basename(filepath)
        new_path = os.path.join(category_dir, filename)
        
        # 既に存在する場合はスキップ
        if os.path.exists(new_path):
            continue
            
        try:
            shutil.copy2(filepath, new_path)
            copied_count += 1
            if copied_count <= 5:  # 最初の5件だけ表示
                print(f"  コピー済み: {filename} (スコア: {score})")
        except Exception as e:
            print(f"  エラー: {filename} - {e}")
    
    # インデックス作成
    create_category_index(category_name, category_info, category_dir, copied_count)
    
    print(f"{category_name} 統合完了: {copied_count}ファイル")
    return copied_count

def create_category_index(category_name, category_info, category_dir, file_count):
    """カテゴリインデックス作成"""
    index_path = os.path.join(category_dir, "README.md")
    
    content = f"""# {category_name}

このカテゴリには {file_count} 件のドキュメントがあります。

## 🔍 関連キーワード
{', '.join(category_info['keywords'])}

## 📚 ドキュメント一覧

"""
    
    # ディレクトリ内のファイルをリスト化
    if os.path.exists(category_dir):
        files = [f for f in os.listdir(category_dir) if f.endswith('.md') and f != 'README.md']
        files.sort()
        
        for filename in files:
            title = filename.replace('.md', '')
            content += f"- [[{filename}|{title}]]\n"
    
    content += f"""
## 🔗 関連カテゴリ

- [[../01_よしなに対応/README.md|よしなに対応]]
- [[../00_Index/README.md|メインインデックス]]

---
最終更新: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    print("=" * 60)
    print("カテゴリ別統合プロセス")
    print("=" * 60)
    
    total_integrated = 0
    
    for category_name, category_info in CATEGORIES.items():
        count = integrate_category(category_name, category_info)
        total_integrated += count
    
    print("\n" + "=" * 60)
    print(f"全カテゴリ統合完了！ 総計: {total_integrated}ファイル")
    print("=" * 60)

if __name__ == "__main__":
    main()