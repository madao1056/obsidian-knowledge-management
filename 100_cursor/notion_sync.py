#!/usr/bin/env python3
"""
Notion to Obsidian 同期スクリプト
"""
import os
import json
import requests
from datetime import datetime
import re

# Notion API設定
NOTION_TOKEN = "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"
NOTION_VERSION = "2022-06-28"
HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": NOTION_VERSION,
    "Content-Type": "application/json"
}

# 出力先ディレクトリ
OUTPUT_DIR = "/Users/hashiguchimasaki/project/obsidian/20_Literature/25_Notion"

def get_user_info():
    """ユーザー情報を取得してワークスペースを確認"""
    url = "https://api.notion.com/v1/users/me"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None

def search_all_pages():
    """アクセス可能な全ページを検索"""
    url = "https://api.notion.com/v1/search"
    payload = {
        "filter": {
            "property": "object",
            "value": "page"
        }
    }
    
    all_results = []
    has_more = True
    start_cursor = None
    
    while has_more:
        if start_cursor:
            payload["start_cursor"] = start_cursor
            
        response = requests.post(url, headers=HEADERS, json=payload)
        if response.status_code == 200:
            data = response.json()
            all_results.extend(data.get("results", []))
            has_more = data.get("has_more", False)
            start_cursor = data.get("next_cursor")
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
            break
    
    return all_results

def get_page_content(page_id):
    """ページの内容を取得"""
    url = f"https://api.notion.com/v1/blocks/{page_id}/children"
    
    all_blocks = []
    has_more = True
    start_cursor = None
    
    while has_more:
        params = {}
        if start_cursor:
            params["start_cursor"] = start_cursor
            
        response = requests.get(url, headers=HEADERS, params=params)
        if response.status_code == 200:
            data = response.json()
            all_blocks.extend(data.get("results", []))
            has_more = data.get("has_more", False)
            start_cursor = data.get("next_cursor")
        else:
            print(f"Error getting page content: {response.status_code}")
            break
    
    return all_blocks

def blocks_to_markdown(blocks):
    """Notionブロックをマークダウンに変換"""
    markdown = []
    
    for block in blocks:
        block_type = block.get("type")
        
        if block_type == "paragraph":
            text = get_text_from_rich_text(block.get("paragraph", {}).get("rich_text", []))
            markdown.append(text + "\n")
            
        elif block_type == "heading_1":
            text = get_text_from_rich_text(block.get("heading_1", {}).get("rich_text", []))
            markdown.append(f"# {text}\n")
            
        elif block_type == "heading_2":
            text = get_text_from_rich_text(block.get("heading_2", {}).get("rich_text", []))
            markdown.append(f"## {text}\n")
            
        elif block_type == "heading_3":
            text = get_text_from_rich_text(block.get("heading_3", {}).get("rich_text", []))
            markdown.append(f"### {text}\n")
            
        elif block_type == "bulleted_list_item":
            text = get_text_from_rich_text(block.get("bulleted_list_item", {}).get("rich_text", []))
            markdown.append(f"- {text}\n")
            
        elif block_type == "numbered_list_item":
            text = get_text_from_rich_text(block.get("numbered_list_item", {}).get("rich_text", []))
            markdown.append(f"1. {text}\n")
            
        elif block_type == "code":
            code = get_text_from_rich_text(block.get("code", {}).get("rich_text", []))
            language = block.get("code", {}).get("language", "")
            markdown.append(f"```{language}\n{code}\n```\n")
            
        elif block_type == "divider":
            markdown.append("---\n")
    
    return "\n".join(markdown)

def get_text_from_rich_text(rich_text_array):
    """リッチテキストからプレーンテキストを抽出"""
    text = ""
    for rich_text in rich_text_array:
        text += rich_text.get("plain_text", "")
    return text

def sanitize_filename(filename):
    """ファイル名として使える形に変換"""
    # 特殊文字を置換
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    # 先頭末尾の空白を削除
    filename = filename.strip()
    # 空の場合はデフォルト名
    if not filename:
        filename = "Untitled"
    return filename

def main():
    """メイン処理"""
    # 出力ディレクトリを作成
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # ユーザー情報を取得
    print("Getting user info...")
    user_info = get_user_info()
    if user_info:
        print(f"Connected as: {user_info.get('name', 'Unknown')}")
    
    # 全ページを検索
    print("Searching for all pages...")
    pages = search_all_pages()
    print(f"Found {len(pages)} pages")
    
    # 各ページを処理
    for i, page in enumerate(pages):
        page_id = page.get("id")
        title = "Untitled"
        
        # タイトルを取得
        if "properties" in page and "title" in page["properties"]:
            title_prop = page["properties"]["title"]
            if title_prop.get("title"):
                title = get_text_from_rich_text(title_prop["title"])
        
        print(f"\nProcessing {i+1}/{len(pages)}: {title}")
        
        # ページ内容を取得
        blocks = get_page_content(page_id)
        
        # マークダウンに変換
        content = blocks_to_markdown(blocks)
        
        # メタデータを追加
        metadata = f"""---
notion_id: {page_id}
created_time: {page.get('created_time', '')}
last_edited_time: {page.get('last_edited_time', '')}
url: {page.get('url', '')}
---

# {title}

"""
        
        # ファイルに保存
        filename = f"{sanitize_filename(title)}.md"
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(metadata + content)
        
        print(f"Saved to: {filename}")
    
    print(f"\nSync completed! {len(pages)} pages saved to {OUTPUT_DIR}")

if __name__ == "__main__":
    main()