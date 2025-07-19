#!/usr/bin/env python3
"""
Notionプレースホルダーファイルの内容を取得して更新するスクリプト
"""
import os
import json
import requests
from datetime import datetime
import re
import time
from pathlib import Path

# 設定
NOTION_TOKEN = "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"
NOTION_VERSION = "2022-06-28"
HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": NOTION_VERSION,
    "Content-Type": "application/json"
}
OUTPUT_DIR = "/Users/hashiguchimasaki/project/obsidian/20_Literature/25_Notion"

# 統計情報
stats = {
    "total_placeholder_files": 0,
    "successfully_updated": 0,
    "failed_updates": 0,
    "already_complete": 0,
    "start_time": None,
    "end_time": None,
    "errors": []
}

def is_placeholder_file(filepath):
    """ファイルがプレースホルダーかどうかを判定"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # ファイルの行数をカウント
    lines = content.strip().split('\n')
    
    # メタデータ部分を除いた実際のコンテンツ部分を取得
    content_start = False
    content_lines = []
    for line in lines:
        if line.strip() == '---' and content_start:
            content_start = False
            continue
        elif line.strip() == '---' and not content_start:
            content_start = True
            continue
        elif not content_start and line.strip():
            content_lines.append(line)
    
    # コンテンツが少ない（5行以下）場合はプレースホルダーと判定
    return len(content_lines) <= 5

def extract_notion_id(filepath):
    """ファイルからNotion IDを抽出"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = re.search(r'notion_id:\s*([a-f0-9-]+)', content)
    if match:
        return match.group(1)
    return None

def get_page_content(page_id):
    """ページ内容を取得（ページネーション対応）"""
    url = f"https://api.notion.com/v1/blocks/{page_id}/children"
    
    all_blocks = []
    has_more = True
    start_cursor = None
    
    while has_more:
        params = {"page_size": 100}
        if start_cursor:
            params["start_cursor"] = start_cursor
        
        response = requests.get(url, headers=HEADERS, params=params)
        if response.status_code == 200:
            data = response.json()
            blocks = data.get("results", [])
            all_blocks.extend(blocks)
            has_more = data.get("has_more", False)
            start_cursor = data.get("next_cursor")
        else:
            break
    
    return all_blocks

def block_to_markdown(block, indent_level=0):
    """ブロックをマークダウンに変換"""
    block_type = block.get("type")
    indent = "  " * indent_level
    
    converters = {
        "paragraph": lambda b: f"{indent}{extract_text(b, 'paragraph')}",
        "heading_1": lambda b: f"{indent}# {extract_text(b, 'heading_1')}",
        "heading_2": lambda b: f"{indent}## {extract_text(b, 'heading_2')}",
        "heading_3": lambda b: f"{indent}### {extract_text(b, 'heading_3')}",
        "bulleted_list_item": lambda b: f"{indent}- {extract_text(b, 'bulleted_list_item')}",
        "numbered_list_item": lambda b: f"{indent}1. {extract_text(b, 'numbered_list_item')}",
        "to_do": lambda b: f"{indent}- [{'x' if b.get('to_do', {}).get('checked', False) else ' '}] {extract_text(b, 'to_do')}",
        "toggle": lambda b: f"{indent}<details>\n{indent}<summary>{extract_text(b, 'toggle')}</summary>\n{indent}</details>",
        "code": lambda b: format_code_block(b, indent),
        "quote": lambda b: f"{indent}> {extract_text(b, 'quote')}",
        "divider": lambda b: f"{indent}---",
        "table_of_contents": lambda b: f"{indent}[[TOC]]",
        "callout": lambda b: f"{indent}> 💡 {extract_text(b, 'callout')}",
        "image": lambda b: format_image(b, indent),
        "video": lambda b: format_video(b, indent),
        "file": lambda b: format_file(b, indent),
        "bookmark": lambda b: format_bookmark(b, indent),
        "equation": lambda b: f"{indent}$${b.get('equation', {}).get('expression', '')}$$"
    }
    
    converter = converters.get(block_type)
    if converter:
        return converter(block)
    return ""

def extract_text(block, block_type):
    """ブロックからテキストを抽出"""
    texts = block.get(block_type, {}).get("rich_text", [])
    return "".join([format_rich_text(t) for t in texts])

def format_rich_text(text_obj):
    """リッチテキストをフォーマット"""
    text = text_obj.get("plain_text", "")
    annotations = text_obj.get("annotations", {})
    
    if annotations.get("bold"):
        text = f"**{text}**"
    if annotations.get("italic"):
        text = f"*{text}*"
    if annotations.get("strikethrough"):
        text = f"~~{text}~~"
    if annotations.get("code"):
        text = f"`{text}`"
    
    if text_obj.get("href"):
        text = f"[{text}]({text_obj['href']})"
    
    return text

def format_code_block(block, indent):
    """コードブロックをフォーマット"""
    texts = block.get("code", {}).get("rich_text", [])
    code = "".join([t.get("plain_text", "") for t in texts])
    language = block.get("code", {}).get("language", "")
    return f"{indent}```{language}\n{code}\n{indent}```"

def format_image(block, indent):
    """画像ブロックをフォーマット"""
    image = block.get("image", {})
    if image.get("type") == "external":
        url = image.get("external", {}).get("url", "")
    else:
        url = image.get("file", {}).get("url", "")
    
    caption = "".join([t.get("plain_text", "") for t in image.get("caption", [])])
    if caption:
        return f"{indent}![{caption}]({url})"
    return f"{indent}![]({url})"

def format_video(block, indent):
    """ビデオブロックをフォーマット"""
    video = block.get("video", {})
    if video.get("type") == "external":
        url = video.get("external", {}).get("url", "")
        return f"{indent}[Video: {url}]({url})"
    return ""

def format_file(block, indent):
    """ファイルブロックをフォーマット"""
    file = block.get("file", {})
    if file.get("type") == "external":
        url = file.get("external", {}).get("url", "")
    else:
        url = file.get("file", {}).get("url", "")
    
    name = file.get("name", "File")
    return f"{indent}[{name}]({url})"

def format_bookmark(block, indent):
    """ブックマークブロックをフォーマット"""
    bookmark = block.get("bookmark", {})
    url = bookmark.get("url", "")
    caption = "".join([t.get("plain_text", "") for t in bookmark.get("caption", [])])
    
    if caption:
        return f"{indent}[{caption}]({url})"
    return f"{indent}[Bookmark]({url})"

def update_file_with_content(filepath, notion_id):
    """ファイルに完全なコンテンツを追加"""
    try:
        # 既存のメタデータを保持
        with open(filepath, 'r', encoding='utf-8') as f:
            existing_content = f.read()
        
        # メタデータ部分を抽出
        metadata_match = re.search(r'^---\n(.*?)\n---\n', existing_content, re.DOTALL)
        if not metadata_match:
            print(f"  ✗ メタデータが見つかりません: {filepath}")
            return False
        
        metadata = metadata_match.group(0)
        
        # Notion APIから完全なコンテンツを取得
        blocks = get_page_content(notion_id)
        
        if not blocks:
            print(f"  ✗ コンテンツが取得できませんでした")
            return False
        
        # ブロックをマークダウンに変換
        content_lines = []
        for block in blocks:
            line = block_to_markdown(block)
            if line:
                content_lines.append(line)
                
            # ネストされたブロックも処理
            if block.get("has_children"):
                child_blocks = get_page_content(block["id"])
                for child_block in child_blocks:
                    child_line = block_to_markdown(child_block, indent_level=1)
                    if child_line:
                        content_lines.append(child_line)
        
        # タイトルを取得
        title = os.path.basename(filepath).replace('.md', '')
        
        # 新しい内容を構築
        new_content = metadata + f"\n# {title}\n\n" + "\n".join(content_lines)
        
        # ファイルを更新
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"  ✓ 更新完了: {len(blocks)} blocks")
        return True
        
    except Exception as e:
        print(f"  ✗ エラー: {str(e)}")
        stats["errors"].append(f"{filepath}: {str(e)}")
        return False

def main():
    """メイン処理"""
    stats["start_time"] = time.time()
    
    print("=" * 60)
    print("Notion Placeholder Content Fetcher")
    print("=" * 60)
    
    # プレースホルダーファイルを検索
    print("\n1. プレースホルダーファイルを検索中...")
    
    placeholder_files = []
    for filename in os.listdir(OUTPUT_DIR):
        if filename.endswith('.md'):
            filepath = os.path.join(OUTPUT_DIR, filename)
            if is_placeholder_file(filepath):
                notion_id = extract_notion_id(filepath)
                if notion_id:
                    placeholder_files.append((filepath, notion_id))
    
    stats["total_placeholder_files"] = len(placeholder_files)
    print(f"   見つかったプレースホルダー: {len(placeholder_files)} files")
    
    # 各ファイルを処理
    print("\n2. コンテンツを取得して更新中...")
    print("-" * 60)
    
    for i, (filepath, notion_id) in enumerate(placeholder_files):
        filename = os.path.basename(filepath)
        print(f"\n[{i+1}/{len(placeholder_files)}] {filename}")
        print(f"  Notion ID: {notion_id}")
        
        if update_file_with_content(filepath, notion_id):
            stats["successfully_updated"] += 1
        else:
            stats["failed_updates"] += 1
        
        # レート制限対策
        time.sleep(0.5)
    
    stats["end_time"] = time.time()
    
    # 統計情報を表示
    print("\n" + "=" * 60)
    print("FETCH SUMMARY")
    print("=" * 60)
    print(f"プレースホルダーファイル数: {stats['total_placeholder_files']}")
    print(f"更新成功:                   {stats['successfully_updated']}")
    print(f"更新失敗:                   {stats['failed_updates']}")
    print(f"処理時間:                   {stats['end_time'] - stats['start_time']:.2f} seconds")
    
    if stats["errors"]:
        print("\nエラー詳細:")
        for error in stats["errors"][:10]:
            print(f"  - {error}")
        if len(stats["errors"]) > 10:
            print(f"  ... 他 {len(stats['errors']) - 10} 件のエラー")
    
    # 統計情報を保存
    stats_file = os.path.join(OUTPUT_DIR, ".content_fetch_stats.json")
    with open(stats_file, 'w') as f:
        json.dump({
            "last_fetch": datetime.now().isoformat(),
            "placeholder_files": stats["total_placeholder_files"],
            "updated": stats["successfully_updated"],
            "failed": stats["failed_updates"],
            "duration_seconds": stats["end_time"] - stats["start_time"],
            "errors": stats["errors"]
        }, f, indent=2)
    
    print(f"\n統計情報を保存: {stats_file}")

if __name__ == "__main__":
    main()