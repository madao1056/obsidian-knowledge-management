#!/usr/bin/env python3
"""
Notion全体同期スクリプト（統計情報付き）
"""
import os
import json
import requests
from datetime import datetime
import re
import time

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
    "total_pages": 0,
    "synced_pages": 0,
    "failed_pages": 0,
    "total_blocks": 0,
    "start_time": None,
    "end_time": None,
    "errors": []
}

def sanitize_filename(filename):
    """ファイル名をサニタイズ"""
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    return filename.strip()[:200] or "Untitled"  # 最大200文字

def get_page_title(page):
    """ページタイトルを取得"""
    try:
        if 'properties' in page:
            for prop_name, prop_value in page['properties'].items():
                if prop_value['type'] == 'title' and prop_value.get('title'):
                    return prop_value['title'][0]['plain_text']
    except:
        pass
    return "Untitled"

def count_all_pages():
    """全ページ数をカウント"""
    url = "https://api.notion.com/v1/search"
    payload = {
        "filter": {"property": "object", "value": "page"},
        "page_size": 100
    }
    
    total = 0
    has_more = True
    start_cursor = None
    
    while has_more:
        if start_cursor:
            payload["start_cursor"] = start_cursor
        
        response = requests.post(url, headers=HEADERS, json=payload)
        if response.status_code == 200:
            data = response.json()
            results = data.get("results", [])
            total += len(results)
            has_more = data.get("has_more", False)
            start_cursor = data.get("next_cursor")
        else:
            print(f"Error counting pages: {response.status_code}")
            break
    
    return total

def search_all_pages():
    """全ページを取得"""
    url = "https://api.notion.com/v1/search"
    payload = {
        "filter": {"property": "object", "value": "page"},
        "page_size": 100
    }
    
    all_pages = []
    has_more = True
    start_cursor = None
    
    while has_more:
        if start_cursor:
            payload["start_cursor"] = start_cursor
        
        response = requests.post(url, headers=HEADERS, json=payload)
        if response.status_code == 200:
            data = response.json()
            results = data.get("results", [])
            all_pages.extend(results)
            has_more = data.get("has_more", False)
            start_cursor = data.get("next_cursor")
            print(f"  Fetched {len(all_pages)} pages so far...")
        else:
            print(f"Error fetching pages: {response.status_code}")
            break
    
    return all_pages

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
    """ブロックをマークダウンに変換（ネスト対応）"""
    block_type = block.get("type")
    indent = "  " * indent_level
    
    if block_type == "paragraph":
        texts = block.get("paragraph", {}).get("rich_text", [])
        text = "".join([t.get("plain_text", "") for t in texts])
        return f"{indent}{text}"
    
    elif block_type == "heading_1":
        texts = block.get("heading_1", {}).get("rich_text", [])
        text = "".join([t.get("plain_text", "") for t in texts])
        return f"{indent}# {text}"
    
    elif block_type == "heading_2":
        texts = block.get("heading_2", {}).get("rich_text", [])
        text = "".join([t.get("plain_text", "") for t in texts])
        return f"{indent}## {text}"
    
    elif block_type == "heading_3":
        texts = block.get("heading_3", {}).get("rich_text", [])
        text = "".join([t.get("plain_text", "") for t in texts])
        return f"{indent}### {text}"
    
    elif block_type == "bulleted_list_item":
        texts = block.get("bulleted_list_item", {}).get("rich_text", [])
        text = "".join([t.get("plain_text", "") for t in texts])
        return f"{indent}- {text}"
    
    elif block_type == "numbered_list_item":
        texts = block.get("numbered_list_item", {}).get("rich_text", [])
        text = "".join([t.get("plain_text", "") for t in texts])
        return f"{indent}1. {text}"
    
    elif block_type == "to_do":
        texts = block.get("to_do", {}).get("rich_text", [])
        text = "".join([t.get("plain_text", "") for t in texts])
        checked = block.get("to_do", {}).get("checked", False)
        checkbox = "[x]" if checked else "[ ]"
        return f"{indent}- {checkbox} {text}"
    
    elif block_type == "toggle":
        texts = block.get("toggle", {}).get("rich_text", [])
        text = "".join([t.get("plain_text", "") for t in texts])
        return f"{indent}<details>\n{indent}<summary>{text}</summary>\n{indent}</details>"
    
    elif block_type == "code":
        texts = block.get("code", {}).get("rich_text", [])
        code = "".join([t.get("plain_text", "") for t in texts])
        language = block.get("code", {}).get("language", "")
        return f"{indent}```{language}\n{code}\n{indent}```"
    
    elif block_type == "quote":
        texts = block.get("quote", {}).get("rich_text", [])
        text = "".join([t.get("plain_text", "") for t in texts])
        return f"{indent}> {text}"
    
    elif block_type == "divider":
        return f"{indent}---"
    
    elif block_type == "table_of_contents":
        return f"{indent}[[TOC]]"
    
    return ""

def main():
    """メイン処理"""
    stats["start_time"] = time.time()
    
    # ディレクトリ作成
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    print("=" * 60)
    print("Notion Full Sync - Starting")
    print("=" * 60)
    
    # 全ページ数をカウント
    print("\n1. Counting total pages...")
    total_count = count_all_pages()
    print(f"   Total pages found: {total_count}")
    stats["total_pages"] = total_count
    
    # 全ページを取得
    print("\n2. Fetching all pages...")
    pages = search_all_pages()
    print(f"   Successfully fetched: {len(pages)} pages")
    
    # 各ページを処理
    print("\n3. Processing pages...")
    print("-" * 60)
    
    for i, page in enumerate(pages):
        page_id = page['id']
        title = get_page_title(page)
        print(f"\n[{i+1}/{len(pages)}] {title}")
        
        try:
            # ページ内容を取得
            blocks = get_page_content(page_id)
            stats["total_blocks"] += len(blocks)
            print(f"  - Fetched {len(blocks)} blocks")
            
            # マークダウンに変換
            content_lines = []
            for block in blocks:
                line = block_to_markdown(block)
                if line:
                    content_lines.append(line)
            
            # メタデータとコンテンツを結合
            metadata = f"""---
notion_id: {page_id}
created_time: {page.get('created_time', '')}
last_edited_time: {page.get('last_edited_time', '')}
url: {page.get('url', '')}
parent_type: {page.get('parent', {}).get('type', 'unknown')}
archived: {page.get('archived', False)}
sync_time: {datetime.now().isoformat()}
---

# {title}

"""
            
            full_content = metadata + "\n".join(content_lines)
            
            # ファイルに保存
            filename = f"{sanitize_filename(title)}.md"
            filepath = os.path.join(OUTPUT_DIR, filename)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(full_content)
            
            stats["synced_pages"] += 1
            print(f"  ✓ Saved successfully")
            
        except Exception as e:
            stats["failed_pages"] += 1
            stats["errors"].append(f"{title}: {str(e)}")
            print(f"  ✗ Error: {str(e)}")
    
    stats["end_time"] = time.time()
    
    # 統計情報を表示
    print("\n" + "=" * 60)
    print("SYNC SUMMARY")
    print("=" * 60)
    print(f"Total pages in Notion:  {stats['total_pages']}")
    print(f"Successfully synced:    {stats['synced_pages']}")
    print(f"Failed:                 {stats['failed_pages']}")
    print(f"Total blocks processed: {stats['total_blocks']}")
    print(f"Time elapsed:           {stats['end_time'] - stats['start_time']:.2f} seconds")
    print(f"Output directory:       {OUTPUT_DIR}")
    
    if stats["errors"]:
        print("\nErrors:")
        for error in stats["errors"][:5]:  # 最初の5個のエラーを表示
            print(f"  - {error}")
        if len(stats["errors"]) > 5:
            print(f"  ... and {len(stats['errors']) - 5} more errors")
    
    # 統計情報をファイルに保存
    stats_file = os.path.join(OUTPUT_DIR, ".sync_stats.json")
    with open(stats_file, 'w') as f:
        json.dump({
            "last_sync": datetime.now().isoformat(),
            "pages_synced": stats["synced_pages"],
            "pages_failed": stats["failed_pages"],
            "total_blocks": stats["total_blocks"],
            "duration_seconds": stats["end_time"] - stats["start_time"],
            "errors": stats["errors"]
        }, f, indent=2)
    
    print(f"\nStats saved to: {stats_file}")

if __name__ == "__main__":
    main()