#!/usr/bin/env python3
"""
シンプルなNotion to Obsidian同期スクリプト
"""
import os
import json
import requests
from datetime import datetime
import re

# 設定
NOTION_TOKEN = "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"
NOTION_VERSION = "2022-06-28"
HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": NOTION_VERSION,
    "Content-Type": "application/json"
}
OUTPUT_DIR = "/Users/hashiguchimasaki/project/obsidian/20_Literature/25_Notion"

def sanitize_filename(filename):
    """ファイル名をサニタイズ"""
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    return filename.strip() or "Untitled"

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

def search_pages(limit=10):
    """ページを検索（制限付き）"""
    url = "https://api.notion.com/v1/search"
    payload = {
        "filter": {"property": "object", "value": "page"},
        "page_size": limit
    }
    
    response = requests.post(url, headers=HEADERS, json=payload)
    if response.status_code == 200:
        return response.json().get("results", [])
    return []

def get_page_content(page_id):
    """ページ内容を簡易的に取得"""
    url = f"https://api.notion.com/v1/blocks/{page_id}/children"
    response = requests.get(url, headers=HEADERS, params={"page_size": 100})
    
    if response.status_code == 200:
        return response.json().get("results", [])
    return []

def block_to_markdown(block):
    """ブロックを簡易的にマークダウンに変換"""
    block_type = block.get("type")
    
    if block_type == "paragraph":
        texts = block.get("paragraph", {}).get("rich_text", [])
        return "".join([t.get("plain_text", "") for t in texts])
    
    elif block_type == "heading_1":
        texts = block.get("heading_1", {}).get("rich_text", [])
        text = "".join([t.get("plain_text", "") for t in texts])
        return f"# {text}"
    
    elif block_type == "heading_2":
        texts = block.get("heading_2", {}).get("rich_text", [])
        text = "".join([t.get("plain_text", "") for t in texts])
        return f"## {text}"
    
    elif block_type == "heading_3":
        texts = block.get("heading_3", {}).get("rich_text", [])
        text = "".join([t.get("plain_text", "") for t in texts])
        return f"### {text}"
    
    elif block_type == "bulleted_list_item":
        texts = block.get("bulleted_list_item", {}).get("rich_text", [])
        text = "".join([t.get("plain_text", "") for t in texts])
        return f"- {text}"
    
    elif block_type == "numbered_list_item":
        texts = block.get("numbered_list_item", {}).get("rich_text", [])
        text = "".join([t.get("plain_text", "") for t in texts])
        return f"1. {text}"
    
    elif block_type == "code":
        texts = block.get("code", {}).get("rich_text", [])
        code = "".join([t.get("plain_text", "") for t in texts])
        language = block.get("code", {}).get("language", "")
        return f"```{language}\n{code}\n```"
    
    elif block_type == "divider":
        return "---"
    
    return ""

def main():
    """メイン処理"""
    # ディレクトリ作成
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    print("Searching for pages...")
    pages = search_pages(limit=20)  # 最初は20ページだけ
    print(f"Found {len(pages)} pages to sync")
    
    for i, page in enumerate(pages):
        page_id = page['id']
        title = get_page_title(page)
        print(f"\n[{i+1}/{len(pages)}] Processing: {title}")
        
        # ページ内容を取得
        blocks = get_page_content(page_id)
        
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
        
        print(f"  ✓ Saved to: {filename}")
    
    print(f"\n✅ Sync completed! {len(pages)} pages saved to {OUTPUT_DIR}")
    
    # 今後の同期用の設定ファイルを作成
    sync_info = {
        "last_sync": datetime.now().isoformat(),
        "pages_synced": len(pages),
        "output_dir": OUTPUT_DIR
    }
    
    with open(os.path.join(OUTPUT_DIR, ".sync_info.json"), 'w') as f:
        json.dump(sync_info, f, indent=2)

if __name__ == "__main__":
    main()