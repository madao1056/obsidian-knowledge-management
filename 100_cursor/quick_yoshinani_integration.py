#!/usr/bin/env python3
"""
よしなに対応関連ファイルの優先統合スクリプト
"""
import os
import shutil
import re
from pathlib import Path

# 設定
BASE_DIR = "/Users/hashiguchimasaki/project/obsidian"
NOTION_DIR = os.path.join(BASE_DIR, "20_Literature/25_Notion")
YOSHINANI_DIR = os.path.join(BASE_DIR, "10_Projects/Knowledge_Base/01_よしなに対応")

def collect_yoshinani_files():
    """よしなに関連ファイルを収集"""
    yoshinani_files = []
    keywords = ['よしなに', 'ヨシナニ', '相手目線', '先回り', '巻き取', '気遣い']
    
    print("よしなに関連ファイルを収集中...")
    
    for root, dirs, files in os.walk(NOTION_DIR):
        for filename in files:
            if filename.endswith('.md') and not filename.startswith('.'):
                filepath = os.path.join(root, filename)
                
                # ファイル名チェック
                name_match = any(keyword in filename for keyword in keywords)
                
                # 内容チェック（軽量）
                content_match = False
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read(500)  # 最初の500文字のみ
                    content_match = any(keyword in content for keyword in keywords)
                except:
                    pass
                
                if name_match or content_match:
                    yoshinani_files.append(filepath)
    
    print(f"見つかったファイル数: {len(yoshinani_files)}")
    return yoshinani_files

def copy_files_to_knowledge_base(files):
    """ファイルを知識ベースにコピー"""
    print("ファイルをコピー中...")
    
    os.makedirs(YOSHINANI_DIR, exist_ok=True)
    copied_count = 0
    
    for filepath in files:
        filename = os.path.basename(filepath)
        new_path = os.path.join(YOSHINANI_DIR, filename)
        
        try:
            shutil.copy2(filepath, new_path)
            copied_count += 1
            print(f"  コピー済み: {filename}")
        except Exception as e:
            print(f"  エラー: {filename} - {e}")
    
    print(f"コピー完了: {copied_count}件")
    return copied_count

def create_yoshinani_index():
    """よしなに対応インデックス作成"""
    index_path = os.path.join(YOSHINANI_DIR, "README.md")
    
    content = """# よしなに対応 ナレッジベース

## 📖 よしなに対応とは

**よしなに対応 = 相手目線で"手間"や"面倒"を巻き取る力**

### 3つの柱

1. **信頼構築力** - 「迅速・厳守・誠実・安心・温度」
2. **情報編集力** - 「相手の意図を読み解き、2.3手先回りした対応」
3. **当事者意識** - 「自分ごととしてプロジェクトを捉える」

## 📚 ドキュメント一覧

"""
    
    # ディレクトリ内のファイルをリスト化
    if os.path.exists(YOSHINANI_DIR):
        files = [f for f in os.listdir(YOSHINANI_DIR) if f.endswith('.md') and f != 'README.md']
        files.sort()
        
        for filename in files:
            title = filename.replace('.md', '')
            content += f"- [[{filename}|{title}]]\n"
    
    content += """
## 💡 重要な考え方

### 感謝×相手目線のPDCA
- 相手の立場・目的・抱えている負担を読み取り、**こちらから動く姿勢**
- 「何が手間か？」を想像し、巻き取る意識を常に持つ
- その繰り返しが、他者にはない"余裕"と"自信"につながる

### 成長のステップ
1. **感謝の気持ちを持つ** - すべての起点
2. **相手目線で考える** - 何が手間か？を想像
3. **先回りして動く** - 2,3手先を読む
4. **PDCAを回す** - 常に改善し続ける
5. **自信を持つ** - 積み重ねが余裕を生む

---
最終更新: """ + str(Path(__file__).stat().st_mtime)

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"インデックス作成完了: {index_path}")

def main():
    print("=" * 50)
    print("よしなに対応 優先統合プロセス")
    print("=" * 50)
    
    # 1. よしなに関連ファイル収集
    yoshinani_files = collect_yoshinani_files()
    
    if not yoshinani_files:
        print("よしなに関連ファイルが見つかりませんでした。")
        return
    
    # 2. ファイルコピー
    copied_count = copy_files_to_knowledge_base(yoshinani_files)
    
    # 3. インデックス作成
    create_yoshinani_index()
    
    print("\n" + "=" * 50)
    print(f"よしなに対応統合完了！ ({copied_count}ファイル)")
    print(f"場所: {YOSHINANI_DIR}")
    print("=" * 50)

if __name__ == "__main__":
    main()