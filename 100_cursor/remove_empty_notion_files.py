#!/usr/bin/env python3
"""
空のNotionページファイルを削除するスクリプト
"""

import os
import re
from datetime import datetime
from pathlib import Path

# 設定
DIRECTORIES_TO_CHECK = [
    "/Users/hashiguchimasaki/project/obsidian/20_Literature/25_Notion",
    "/Users/hashiguchimasaki/project/obsidian/10_Projects/Knowledge_Base"
]

def is_empty_notion_file(filepath: str) -> bool:
    """
    ファイルが空のNotionページかどうかを判定
    
    Args:
        filepath: チェックするファイルパス
    
    Returns:
        空のNotionページの場合True
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # パターン1: プレースホルダーファイル
        if 'This is a placeholder file' in content:
            return True
        
        # パターン2: メタデータのみでコンテンツが空
        if '---' in content:
            parts = content.split('---', 2)
            if len(parts) >= 3:
                actual_content = parts[2].strip()
                
                # タイトル行を除外
                lines = actual_content.split('\n')
                if lines:
                    # 最初の行がタイトル（#で始まる）の場合、それを除外
                    content_without_title = []
                    for i, line in enumerate(lines):
                        if i == 0 and line.startswith('#'):
                            continue
                        content_without_title.append(line)
                    
                    remaining_content = '\n'.join(content_without_title).strip()
                    
                    # 空のコンテンツマーカーがある場合
                    if '*(コンテンツが空のページ)*' in remaining_content:
                        return True
                    
                    # 実質的なコンテンツがない場合（空行や空白のみ）
                    if len(remaining_content) == 0:
                        return True
                    
                    # ごく短いコンテンツ（10文字以下）
                    if len(remaining_content) <= 10 and not remaining_content.strip():
                        return True
        
        return False
        
    except Exception as e:
        print(f"Error checking {filepath}: {e}")
        return False

def find_empty_notion_files(directories: list) -> list:
    """
    指定ディレクトリ内の空のNotionファイルを検索
    
    Args:
        directories: 検索対象ディレクトリのリスト
    
    Returns:
        空のNotionファイルのリスト
    """
    empty_files = []
    
    for directory in directories:
        if not os.path.exists(directory):
            print(f"⚠️  ディレクトリが存在しません: {directory}")
            continue
            
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.md'):
                    filepath = os.path.join(root, file)
                    
                    if is_empty_notion_file(filepath):
                        empty_files.append(filepath)
    
    return empty_files

def get_file_info(filepath: str) -> dict:
    """
    ファイルの詳細情報を取得
    
    Args:
        filepath: ファイルパス
    
    Returns:
        ファイル情報の辞書
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        info = {
            'path': filepath,
            'name': os.path.basename(filepath),
            'size': os.path.getsize(filepath),
            'type': 'unknown'
        }
        
        # ファイルタイプを判定
        if 'This is a placeholder file' in content:
            info['type'] = 'placeholder'
        elif '*(コンテンツが空のページ)*' in content:
            info['type'] = 'empty_content'
        else:
            info['type'] = 'empty_after_metadata'
        
        # Notion IDを抽出
        notion_id_match = re.search(r'notion_id:\s*([a-f0-9-]+)', content)
        if notion_id_match:
            info['notion_id'] = notion_id_match.group(1)
        
        return info
        
    except Exception as e:
        print(f"Error getting info for {filepath}: {e}")
        return {'path': filepath, 'name': os.path.basename(filepath), 'error': str(e)}

def main():
    """
    メイン処理
    """
    print("🔍 空のNotionファイルを検索中...")
    print(f"検索対象ディレクトリ:")
    for dir in DIRECTORIES_TO_CHECK:
        print(f"  - {dir}")
    
    # 空のファイルを検索
    empty_files = find_empty_notion_files(DIRECTORIES_TO_CHECK)
    
    if not empty_files:
        print("\n✅ 空のNotionファイルは見つかりませんでした")
        return
    
    print(f"\n📄 {len(empty_files)}個の空のNotionファイルが見つかりました")
    
    # ファイルタイプ別に分類
    file_types = {}
    for filepath in empty_files:
        info = get_file_info(filepath)
        file_type = info.get('type', 'unknown')
        if file_type not in file_types:
            file_types[file_type] = []
        file_types[file_type].append(info)
    
    # タイプ別に表示
    print("\n📊 ファイルタイプ別内訳:")
    for file_type, files in file_types.items():
        print(f"  - {file_type}: {len(files)}ファイル")
    
    # 削除対象の詳細を表示（最初の10件）
    print("\n🗑️  削除対象ファイル:")
    for i, filepath in enumerate(empty_files[:10]):
        print(f"  {i+1}. {os.path.basename(filepath)}")
        if i == 9 and len(empty_files) > 10:
            print(f"  ... 他 {len(empty_files) - 10} ファイル")
    
    # 削除前にバックアップディレクトリを作成
    backup_dir = f"/Users/hashiguchimasaki/project/obsidian/100_cursor/deleted_empty_files_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    os.makedirs(backup_dir, exist_ok=True)
    
    # 削除リストを保存
    list_file = os.path.join(backup_dir, "deleted_files_list.txt")
    with open(list_file, 'w', encoding='utf-8') as f:
        f.write(f"削除日時: {datetime.now().isoformat()}\n")
        f.write(f"削除ファイル数: {len(empty_files)}\n")
        f.write("=" * 50 + "\n\n")
        
        for info in empty_files:
            file_info = get_file_info(info) if isinstance(info, str) else info
            f.write(f"ファイル: {file_info.get('name', 'unknown')}\n")
            f.write(f"パス: {file_info.get('path', info)}\n")
            f.write(f"タイプ: {file_info.get('type', 'unknown')}\n")
            if 'notion_id' in file_info:
                f.write(f"Notion ID: {file_info['notion_id']}\n")
            f.write("-" * 30 + "\n")
    
    print(f"\n💾 削除リストを保存しました: {list_file}")
    
    # ファイルを削除
    print("\n🗑️  ファイルを削除中...")
    success_count = 0
    error_count = 0
    
    for filepath in empty_files:
        try:
            os.remove(filepath)
            success_count += 1
            print(f"  ✅ 削除: {os.path.basename(filepath)}")
        except Exception as e:
            error_count += 1
            print(f"  ❌ エラー: {os.path.basename(filepath)} - {e}")
    
    # 結果サマリー
    print(f"\n✨ 削除完了:")
    print(f"  - 成功: {success_count}ファイル")
    print(f"  - 失敗: {error_count}ファイル")
    print(f"  - 合計: {len(empty_files)}ファイル")
    
    print(f"\n📝 削除リストは以下に保存されています:")
    print(f"  {list_file}")

if __name__ == "__main__":
    main()