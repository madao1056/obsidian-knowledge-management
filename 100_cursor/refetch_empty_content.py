#!/usr/bin/env python3
"""
空のコンテンツを持つNotionページを再取得するスクリプト
"""

import os
import json
import re
import time
from datetime import datetime
from pathlib import Path
from notion_client import Client

# 設定
NOTION_TOKEN = "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"
LITERATURE_DIR = "/Users/hashiguchimasaki/project/obsidian/20_Literature"

# Notionクライアントを初期化
notion = Client(auth=NOTION_TOKEN)

def find_empty_content_files(directory: str, max_content_length: int = 100) -> list:
    """
    指定ディレクトリ内で、コンテンツが空または短いファイルを検索
    
    Args:
        directory: 検索対象ディレクトリ
        max_content_length: コンテンツの最大文字数（これ以下を空とみなす）
    
    Returns:
        空のコンテンツファイルのリスト
    """
    empty_files = []
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # メタデータ部分を除外してコンテンツ部分のみを取得
                    if '---' in content:
                        parts = content.split('---', 2)
                        if len(parts) >= 3:
                            metadata = parts[1]
                            actual_content = parts[2].strip()
                            
                            # notion_idを抽出
                            notion_id_match = re.search(r'notion_id:\s*([a-f0-9-]+)', metadata)
                            if notion_id_match and len(actual_content) <= max_content_length:
                                # タイトル行を除外した実際のコンテンツを確認
                                lines = actual_content.split('\n')
                                content_without_title = '\n'.join(lines[2:]).strip() if len(lines) > 2 else ''
                                
                                if len(content_without_title) == 0:
                                    empty_files.append({
                                        'filepath': filepath,
                                        'notion_id': notion_id_match.group(1),
                                        'content_length': len(content_without_title)
                                    })
                                    
                except Exception as e:
                    print(f"Error reading {filepath}: {e}")
    
    return empty_files

def fetch_notion_content(page_id: str) -> str:
    """
    Notion APIを使用してページコンテンツを取得
    
    Args:
        page_id: NotionページID
    
    Returns:
        ページコンテンツのマークダウン形式
    """
    try:
        # ブロックの子要素を取得
        blocks = []
        has_more = True
        start_cursor = None
        
        while has_more:
            response = notion.blocks.children.list(
                block_id=page_id,
                start_cursor=start_cursor,
                page_size=100
            )
            blocks.extend(response.get('results', []))
            has_more = response.get('has_more', False)
            start_cursor = response.get('next_cursor')
        
        # ブロックをマークダウンに変換
        content = convert_blocks_to_markdown(blocks)
        return content
        
    except Exception as e:
        print(f"Error fetching content for {page_id}: {e}")
        return ""

def convert_blocks_to_markdown(blocks: list) -> str:
    """
    Notionブロックをマークダウンに変換
    """
    markdown_lines = []
    
    for block in blocks:
        block_type = block.get('type')
        
        if block_type == 'paragraph':
            text = get_text_from_rich_text(block.get('paragraph', {}).get('rich_text', []))
            markdown_lines.append(text)
            markdown_lines.append('')  # 空行を追加
            
        elif block_type == 'heading_1':
            text = get_text_from_rich_text(block.get('heading_1', {}).get('rich_text', []))
            markdown_lines.append(f'# {text}')
            markdown_lines.append('')
            
        elif block_type == 'heading_2':
            text = get_text_from_rich_text(block.get('heading_2', {}).get('rich_text', []))
            markdown_lines.append(f'## {text}')
            markdown_lines.append('')
            
        elif block_type == 'heading_3':
            text = get_text_from_rich_text(block.get('heading_3', {}).get('rich_text', []))
            markdown_lines.append(f'### {text}')
            markdown_lines.append('')
            
        elif block_type == 'bulleted_list_item':
            text = get_text_from_rich_text(block.get('bulleted_list_item', {}).get('rich_text', []))
            markdown_lines.append(f'- {text}')
            
        elif block_type == 'numbered_list_item':
            text = get_text_from_rich_text(block.get('numbered_list_item', {}).get('rich_text', []))
            markdown_lines.append(f'1. {text}')
            
        elif block_type == 'quote':
            text = get_text_from_rich_text(block.get('quote', {}).get('rich_text', []))
            markdown_lines.append(f'> {text}')
            markdown_lines.append('')
            
        elif block_type == 'code':
            text = get_text_from_rich_text(block.get('code', {}).get('rich_text', []))
            language = block.get('code', {}).get('language', '')
            markdown_lines.append(f'```{language}')
            markdown_lines.append(text)
            markdown_lines.append('```')
            markdown_lines.append('')
    
    return '\n'.join(markdown_lines)

def get_text_from_rich_text(rich_text: list) -> str:
    """
    リッチテキストからプレーンテキストを抽出
    """
    text_parts = []
    
    for text_obj in rich_text:
        text = text_obj.get('plain_text', '')
        annotations = text_obj.get('annotations', {})
        
        # アノテーションに基づいてマークダウン形式に変換
        if annotations.get('bold'):
            text = f'**{text}**'
        if annotations.get('italic'):
            text = f'*{text}*'
        if annotations.get('code'):
            text = f'`{text}`'
        
        text_parts.append(text)
    
    return ''.join(text_parts)

def update_file_with_content(filepath: str, new_content: str):
    """
    ファイルを新しいコンテンツで更新（メタデータは保持）
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            current_content = f.read()
        
        # メタデータとタイトルを保持
        if '---' in current_content:
            parts = current_content.split('---', 2)
            if len(parts) >= 3:
                metadata = parts[1]
                old_content = parts[2].strip()
                
                # タイトル行を取得
                lines = old_content.split('\n')
                title_line = lines[0] if lines else ''
                
                # 新しいコンテンツでファイルを更新
                updated_content = f"---{metadata}---\n\n{title_line}\n\n{new_content}"
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                
                return True
                
    except Exception as e:
        print(f"Error updating {filepath}: {e}")
        return False

def main():
    """
    メイン処理
    """
    print("🔍 空のコンテンツファイルを検索中...")
    
    # 25_Notionディレクトリを検索
    notion_dir = os.path.join(LITERATURE_DIR, '25_Notion')
    empty_files = find_empty_content_files(notion_dir)
    
    print(f"\n📄 {len(empty_files)}個の空のコンテンツファイルが見つかりました")
    
    if not empty_files:
        print("✅ 全てのファイルにコンテンツが存在します")
        return
    
    # 確認
    print("\n以下のファイルのコンテンツを再取得します:")
    for file_info in empty_files[:10]:  # 最初の10件を表示
        print(f"  - {os.path.basename(file_info['filepath'])}")
    
    if len(empty_files) > 10:
        print(f"  ... 他 {len(empty_files) - 10} ファイル")
    
    # 自動実行モード
    print("\n🚀 コンテンツの再取得を開始します...")
    
    # コンテンツを再取得
    success_count = 0
    for i, file_info in enumerate(empty_files):
        filepath = file_info['filepath']
        notion_id = file_info['notion_id']
        
        print(f"\n[{i+1}/{len(empty_files)}] 処理中: {os.path.basename(filepath)}")
        
        # Notionからコンテンツを取得
        content = fetch_notion_content(notion_id)
        
        if content:
            # ファイルを更新
            if update_file_with_content(filepath, content):
                print(f"  ✅ コンテンツを取得・更新しました")
                success_count += 1
            else:
                print(f"  ❌ ファイルの更新に失敗しました")
        else:
            print(f"  ⚠️  コンテンツが取得できませんでした")
        
        # レート制限対策
        time.sleep(0.5)
    
    print(f"\n✨ 完了: {success_count}/{len(empty_files)} ファイルを更新しました")

if __name__ == "__main__":
    main()