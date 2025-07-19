#!/usr/bin/env python3
"""
プレースホルダーファイルの実際のコンテンツを取得するスクリプト
"""

import os
import json
import re
import time
import yaml
from datetime import datetime
from pathlib import Path
from notion_client import Client

# 設定
NOTION_TOKEN_MAIN = "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"
NOTION_TOKEN_SECONDARY = "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"
KNOWLEDGE_BASE_DIR = "/Users/hashiguchimasaki/project/obsidian/10_Projects/Knowledge_Base"

# Notionクライアントを初期化
notion_main = Client(auth=NOTION_TOKEN_MAIN)
notion_secondary = Client(auth=NOTION_TOKEN_SECONDARY)

def find_placeholder_files(directory: str) -> list:
    """
    プレースホルダーファイルを検索
    
    Args:
        directory: 検索対象ディレクトリ
    
    Returns:
        プレースホルダーファイルのリスト
    """
    placeholder_files = []
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # プレースホルダーマーカーを確認
                    if 'This is a placeholder file' in content:
                        # メタデータを解析
                        if '---' in content:
                            parts = content.split('---', 2)
                            if len(parts) >= 3:
                                metadata = yaml.safe_load(parts[1])
                                
                                placeholder_files.append({
                                    'filepath': filepath,
                                    'notion_id': metadata.get('notion_id'),
                                    'account': metadata.get('account', 'Main'),
                                    'title': metadata.get('title', os.path.basename(filepath))
                                })
                                    
                except Exception as e:
                    print(f"Error reading {filepath}: {e}")
    
    return placeholder_files

def fetch_notion_content(page_id: str, account: str = 'Main') -> dict:
    """
    Notion APIを使用してページコンテンツを取得
    
    Args:
        page_id: NotionページID
        account: アカウント（'Main' または 'Secondary'）
    
    Returns:
        ページ情報とコンテンツ
    """
    try:
        # 適切なクライアントを選択
        notion = notion_main if account == 'Main' else notion_secondary
        
        # ページ情報を取得
        page = notion.pages.retrieve(page_id=page_id)
        
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
        
        # 空のコンテンツでも成功とする
        return {
            'page': page,
            'content': content if content else '*(コンテンツが空のページ)*',
            'success': True
        }
        
    except Exception as e:
        print(f"Error fetching content for {page_id}: {e}")
        return {
            'page': None,
            'content': '',
            'success': False,
            'error': str(e)
        }

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
            
        elif block_type == 'divider':
            markdown_lines.append('---')
            markdown_lines.append('')
            
        elif block_type == 'image':
            image = block.get('image', {})
            url = image.get('external', {}).get('url') or image.get('file', {}).get('url', '')
            caption = get_text_from_rich_text(image.get('caption', []))
            markdown_lines.append(f'![{caption}]({url})')
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
        if annotations.get('strikethrough'):
            text = f'~~{text}~~'
        
        # リンクの処理
        href = text_obj.get('href')
        if href:
            text = f'[{text}]({href})'
        
        text_parts.append(text)
    
    return ''.join(text_parts)

def update_file_with_content(filepath: str, page_info: dict, new_content: str):
    """
    ファイルを新しいコンテンツで更新
    """
    try:
        # 現在のファイルからメタデータを取得
        with open(filepath, 'r', encoding='utf-8') as f:
            current_content = f.read()
        
        # メタデータを更新
        metadata = {}
        if '---' in current_content:
            parts = current_content.split('---', 2)
            if len(parts) >= 3:
                metadata = yaml.safe_load(parts[1]) or {}
        
        # ページ情報から更新
        if page_info:
            metadata['sync_status'] = 'synced'
            metadata['sync_time'] = datetime.now().isoformat()
            metadata['last_edited_time'] = page_info.get('last_edited_time', '')
        
        # タイトルを取得
        title = metadata.get('title', os.path.basename(filepath).replace('.md', ''))
        
        # 新しいコンテンツでファイルを更新
        updated_content = f"""---
{yaml.dump(metadata, default_flow_style=False, allow_unicode=True)}---

# {title}

{new_content}"""
        
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
    print("🔍 プレースホルダーファイルを検索中...")
    
    # Knowledge Baseディレクトリを検索
    placeholder_files = find_placeholder_files(KNOWLEDGE_BASE_DIR)
    
    print(f"\n📄 {len(placeholder_files)}個のプレースホルダーファイルが見つかりました")
    
    if not placeholder_files:
        print("✅ プレースホルダーファイルはありません")
        return
    
    # アカウント別に分類
    main_files = [f for f in placeholder_files if f['account'] == 'Main']
    secondary_files = [f for f in placeholder_files if f['account'] == 'Secondary']
    
    print(f"\n  - Mainアカウント: {len(main_files)}ファイル")
    print(f"  - Secondaryアカウント: {len(secondary_files)}ファイル")
    
    print("\n🚀 コンテンツの取得を開始します...")
    
    # コンテンツを取得
    success_count = 0
    error_count = 0
    
    for i, file_info in enumerate(placeholder_files):
        filepath = file_info['filepath']
        notion_id = file_info['notion_id']
        account = file_info['account']
        title = file_info['title']
        
        print(f"\n[{i+1}/{len(placeholder_files)}] 処理中: {title}")
        print(f"  Account: {account}, ID: {notion_id}")
        
        # Notionからコンテンツを取得
        result = fetch_notion_content(notion_id, account)
        
        if result['success'] and result['content']:
            # ファイルを更新
            if update_file_with_content(filepath, result['page'], result['content']):
                print(f"  ✅ コンテンツを取得・更新しました")
                success_count += 1
            else:
                print(f"  ❌ ファイルの更新に失敗しました")
                error_count += 1
        else:
            print(f"  ⚠️  コンテンツが取得できませんでした: {result.get('error', 'Unknown error')}")
            error_count += 1
        
        # レート制限対策
        time.sleep(0.5)
    
    print(f"\n✨ 完了:")
    print(f"  - 成功: {success_count}ファイル")
    print(f"  - 失敗: {error_count}ファイル")
    print(f"  - 合計: {len(placeholder_files)}ファイル")

if __name__ == "__main__":
    main()