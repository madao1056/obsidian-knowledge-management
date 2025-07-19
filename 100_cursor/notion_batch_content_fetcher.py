#!/usr/bin/env python3
"""
Notionプレースホルダーファイルの内容をバッチで取得して更新するスクリプト
"""
import os
import json
import sys
from datetime import datetime
import re
import time
from pathlib import Path

try:
    import requests
except ImportError:
    print("requestsモジュールが見つかりません。仮想環境を有効化してください:")
    print("source notion_sync_env/bin/activate")
    sys.exit(1)

# 設定
NOTION_TOKEN = "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"
NOTION_VERSION = "2022-06-28"
HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": NOTION_VERSION,
    "Content-Type": "application/json"
}
OUTPUT_DIR = "/Users/hashiguchimasaki/project/obsidian/20_Literature/25_Notion"
BATCH_SIZE = 10  # 一度に処理するファイル数
STATE_FILE = "/Users/hashiguchimasaki/project/obsidian/100_cursor/.batch_fetch_state.json"

def load_state():
    """前回の処理状態を読み込む"""
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'r') as f:
            return json.load(f)
    return {
        "processed_files": [],
        "total_updated": 0,
        "total_failed": 0,
        "last_processed_index": 0
    }

def save_state(state):
    """処理状態を保存"""
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2)

def is_placeholder_file(filepath):
    """ファイルがプレースホルダーかどうかを判定"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # コンテンツの長さで判定（メタデータ除く）
        lines = content.strip().split('\n')
        metadata_ended = False
        content_lines = 0
        
        for line in lines:
            if line.strip() == '---':
                if not metadata_ended:
                    metadata_ended = True
                    continue
            elif metadata_ended:
                if line.strip():
                    content_lines += 1
        
        # コンテンツ行が10行以下ならプレースホルダー
        return content_lines <= 10
    except:
        return False

def extract_notion_id(filepath):
    """ファイルからNotion IDを抽出"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        match = re.search(r'notion_id:\s*([a-f0-9-]+)', content)
        if match:
            return match.group(1)
    except:
        pass
    return None

def get_page_content_simple(page_id):
    """ページ内容を取得（シンプル版）"""
    url = f"https://api.notion.com/v1/blocks/{page_id}/children"
    
    try:
        response = requests.get(url, headers=HEADERS, params={"page_size": 50})
        if response.status_code == 200:
            data = response.json()
            return data.get("results", [])
    except Exception as e:
        print(f"    API Error: {e}")
    
    return []

def simple_block_to_markdown(block):
    """ブロックをシンプルなマークダウンに変換"""
    block_type = block.get("type")
    
    # テキストを抽出する関数
    def get_text(block_data):
        texts = block_data.get("rich_text", [])
        return "".join([t.get("plain_text", "") for t in texts])
    
    # ブロックタイプごとの処理
    if block_type == "paragraph":
        return get_text(block.get("paragraph", {}))
    elif block_type == "heading_1":
        return f"# {get_text(block.get('heading_1', {}))}"
    elif block_type == "heading_2":
        return f"## {get_text(block.get('heading_2', {}))}"
    elif block_type == "heading_3":
        return f"### {get_text(block.get('heading_3', {}))}"
    elif block_type == "bulleted_list_item":
        return f"- {get_text(block.get('bulleted_list_item', {}))}"
    elif block_type == "numbered_list_item":
        return f"1. {get_text(block.get('numbered_list_item', {}))}"
    elif block_type == "to_do":
        checked = block.get("to_do", {}).get("checked", False)
        return f"- [{'x' if checked else ' '}] {get_text(block.get('to_do', {}))}"
    elif block_type == "quote":
        return f"> {get_text(block.get('quote', {}))}"
    elif block_type == "divider":
        return "---"
    elif block_type == "code":
        code = get_text(block.get("code", {}))
        language = block.get("code", {}).get("language", "")
        return f"```{language}\n{code}\n```"
    
    return ""

def update_file_content(filepath, notion_id):
    """ファイルのコンテンツを更新"""
    try:
        # 既存のメタデータを保持
        with open(filepath, 'r', encoding='utf-8') as f:
            existing_content = f.read()
        
        # メタデータ部分を抽出
        metadata_match = re.search(r'^---\n(.*?)\n---\n', existing_content, re.DOTALL)
        if not metadata_match:
            return False
        
        metadata = metadata_match.group(0)
        
        # タイトルを取得
        title = os.path.basename(filepath).replace('.md', '')
        
        # Notion APIからコンテンツを取得
        blocks = get_page_content_simple(notion_id)
        
        if not blocks:
            print(f"    No content retrieved")
            return False
        
        # ブロックをマークダウンに変換
        content_lines = [f"# {title}", ""]
        for block in blocks:
            line = simple_block_to_markdown(block)
            if line:
                content_lines.append(line)
        
        # 新しい内容を構築
        new_content = metadata + "\n" + "\n".join(content_lines)
        
        # ファイルを更新
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"    ✓ Updated with {len(blocks)} blocks")
        return True
        
    except Exception as e:
        print(f"    ✗ Error: {str(e)}")
        return False

def main():
    """メイン処理"""
    print("=" * 60)
    print("Notion Batch Content Fetcher")
    print("=" * 60)
    
    # 状態を読み込む
    state = load_state()
    
    # プレースホルダーファイルをスキャン
    print("\n1. Scanning for placeholder files...")
    
    all_files = []
    for filename in sorted(os.listdir(OUTPUT_DIR)):
        if filename.endswith('.md') and not filename.startswith('.'):
            filepath = os.path.join(OUTPUT_DIR, filename)
            
            # 既に処理済みならスキップ
            if filepath in state["processed_files"]:
                continue
                
            if is_placeholder_file(filepath):
                notion_id = extract_notion_id(filepath)
                if notion_id:
                    all_files.append((filepath, notion_id))
    
    if not all_files:
        print("No placeholder files found to process!")
        return
    
    print(f"Found {len(all_files)} placeholder files to process")
    print(f"Previously processed: {len(state['processed_files'])} files")
    
    # バッチで処理
    batch_files = all_files[:BATCH_SIZE]
    print(f"\n2. Processing batch of {len(batch_files)} files...")
    print("-" * 60)
    
    batch_success = 0
    batch_failed = 0
    
    for i, (filepath, notion_id) in enumerate(batch_files):
        filename = os.path.basename(filepath)
        print(f"\n[{i+1}/{len(batch_files)}] {filename}")
        
        if update_file_content(filepath, notion_id):
            batch_success += 1
            state["total_updated"] += 1
        else:
            batch_failed += 1
            state["total_failed"] += 1
        
        # 処理済みリストに追加
        state["processed_files"].append(filepath)
        
        # レート制限対策
        time.sleep(0.3)
    
    # 状態を保存
    save_state(state)
    
    # サマリー表示
    print("\n" + "=" * 60)
    print("BATCH SUMMARY")
    print("=" * 60)
    print(f"This batch:     {batch_success} success, {batch_failed} failed")
    print(f"Total updated:  {state['total_updated']}")
    print(f"Total failed:   {state['total_failed']}")
    print(f"Remaining:      {len(all_files) - len(batch_files)} files")
    
    if len(all_files) > len(batch_files):
        print(f"\nTo process next batch, run this script again.")

if __name__ == "__main__":
    main()