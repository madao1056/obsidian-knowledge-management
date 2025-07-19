#!/usr/bin/env python3
"""
MainフォルダとルートのNotionファイルから「よしなに対応」関連を優先取得
（Secondaryは別ワークスペースのため一旦除外）
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

# MainとルートのみでSecondaryは除外
TARGET_DIRS = [
    "/Users/hashiguchimasaki/project/obsidian/20_Literature/25_Notion",
    "/Users/hashiguchimasaki/project/obsidian/20_Literature/25_Notion/Main"
]

# よしなに関連キーワード（優先度順）
YOSHINANI_KEYWORDS = [
    "よしなに",
    "ヨシナニ",
    "よしなに対応",
    "よしなに力",
    "判断",
    "先回り",
    "適切に",
    "自動化",
    "思考コスト",
    "気遣い",
    "対応",
    "選択肢"
]

BATCH_SIZE = 20
STATE_FILE = "/Users/hashiguchimasaki/project/obsidian/100_cursor/.yoshinani_main_state.json"

def load_state():
    """前回の処理状態を読み込む"""
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'r') as f:
            return json.load(f)
    return {
        "processed_files": [],
        "total_updated": 0,
        "total_failed": 0,
        "last_processed_index": 0,
        "errors": []
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
        
        # プレースホルダーの特徴的な文字列をチェック
        if "placeholder file from Notion" in content:
            return True
            
        # または、コンテンツの長さで判定
        lines = content.strip().split('\n')
        metadata_ended = False
        content_lines = 0
        
        for line in lines:
            if line.strip() == '---':
                if not metadata_ended:
                    metadata_ended = True
                    continue
            elif metadata_ended:
                if line.strip() and not line.startswith('*') and not line.startswith('**'):
                    content_lines += 1
        
        return content_lines <= 10
    except:
        return False

def extract_notion_id(filepath):
    """ファイルからNotion IDを抽出"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Page ID形式も考慮
        match = re.search(r'(?:notion_id|Page ID):\s*`?([a-f0-9-]+)`?', content)
        if match:
            return match.group(1)
    except:
        pass
    return None

def calculate_yoshinani_score(filename):
    """ファイル名から「よしなに」関連度スコアを計算"""
    score = 0
    filename_lower = filename.lower()
    
    for i, keyword in enumerate(YOSHINANI_KEYWORDS):
        if keyword.lower() in filename_lower:
            # 優先度の高いキーワードほど高得点
            score += (len(YOSHINANI_KEYWORDS) - i) * 10
    
    return score

def get_page_content_with_retry(page_id, max_retries=3):
    """ページ内容を取得（リトライ付き）"""
    url = f"https://api.notion.com/v1/blocks/{page_id}/children"
    
    for attempt in range(max_retries):
        try:
            response = requests.get(
                url, 
                headers=HEADERS, 
                params={"page_size": 100},
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                return data.get("results", [])
            elif response.status_code == 429:  # Rate limit
                wait_time = int(response.headers.get('Retry-After', 60))
                print(f"    Rate limited. Waiting {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                print(f"    API Error: {response.status_code}")
                return []
                
        except requests.exceptions.Timeout:
            print(f"    Timeout (attempt {attempt + 1}/{max_retries})")
            if attempt < max_retries - 1:
                time.sleep(5)
        except Exception as e:
            print(f"    Error: {e}")
            return []
    
    return []

def block_to_markdown(block, indent_level=0):
    """ブロックをマークダウンに変換（改良版）"""
    block_type = block.get("type")
    indent = "  " * indent_level
    
    # テキストを抽出する関数
    def get_text(block_data):
        texts = block_data.get("rich_text", [])
        result = []
        for text in texts:
            plain = text.get("plain_text", "")
            # リッチテキストの装飾を適用
            if text.get("annotations", {}).get("bold"):
                plain = f"**{plain}**"
            if text.get("annotations", {}).get("italic"):
                plain = f"*{plain}*"
            if text.get("annotations", {}).get("code"):
                plain = f"`{plain}`"
            if text.get("href"):
                plain = f"[{plain}]({text['href']})"
            result.append(plain)
        return "".join(result)
    
    # ブロックタイプごとの処理
    if block_type == "paragraph":
        return f"{indent}{get_text(block.get('paragraph', {}))}"
    elif block_type == "heading_1":
        return f"{indent}# {get_text(block.get('heading_1', {}))}"
    elif block_type == "heading_2":
        return f"{indent}## {get_text(block.get('heading_2', {}))}"
    elif block_type == "heading_3":
        return f"{indent}### {get_text(block.get('heading_3', {}))}"
    elif block_type == "bulleted_list_item":
        return f"{indent}- {get_text(block.get('bulleted_list_item', {}))}"
    elif block_type == "numbered_list_item":
        return f"{indent}1. {get_text(block.get('numbered_list_item', {}))}"
    elif block_type == "to_do":
        checked = block.get("to_do", {}).get("checked", False)
        return f"{indent}- [{'x' if checked else ' '}] {get_text(block.get('to_do', {}))}"
    elif block_type == "quote":
        return f"{indent}> {get_text(block.get('quote', {}))}"
    elif block_type == "callout":
        icon = block.get("callout", {}).get("icon", {}).get("emoji", "💡")
        return f"{indent}> {icon} {get_text(block.get('callout', {}))}"
    elif block_type == "divider":
        return f"{indent}---"
    elif block_type == "code":
        code = get_text(block.get("code", {}))
        language = block.get("code", {}).get("language", "")
        return f"{indent}```{language}\n{code}\n{indent}```"
    elif block_type == "image":
        image = block.get("image", {})
        url = ""
        if image.get("type") == "external":
            url = image.get("external", {}).get("url", "")
        elif image.get("type") == "file":
            url = image.get("file", {}).get("url", "")
        caption = get_text({"rich_text": image.get("caption", [])})
        if caption:
            return f"{indent}![{caption}]({url})"
        return f"{indent}![]({url})"
    elif block_type == "toggle":
        toggle_text = get_text(block.get("toggle", {}))
        return f"{indent}<details>\n{indent}<summary>{toggle_text}</summary>\n{indent}</details>"
    elif block_type == "bookmark":
        url = block.get("bookmark", {}).get("url", "")
        caption = get_text({"rich_text": block.get("bookmark", {}).get("caption", [])})
        if caption:
            return f"{indent}[{caption}]({url})"
        return f"{indent}[Bookmark]({url})"
    
    return ""

def update_file_content(filepath, notion_id):
    """ファイルのコンテンツを更新"""
    try:
        # 既存のメタデータを保持
        with open(filepath, 'r', encoding='utf-8') as f:
            existing_content = f.read()
        
        # メタデータ部分を抽出
        metadata_match = re.search(r'^---\n(.*?)\n---', existing_content, re.DOTALL)
        if not metadata_match:
            return False, "No metadata found"
        
        metadata = metadata_match.group(0)
        
        # タイトルを取得
        title = os.path.basename(filepath).replace('.md', '')
        
        # Notion APIからコンテンツを取得
        blocks = get_page_content_with_retry(notion_id)
        
        if not blocks:
            return False, "No content retrieved"
        
        # ブロックをマークダウンに変換
        content_lines = [f"# {title}", ""]
        
        for i, block in enumerate(blocks):
            line = block_to_markdown(block)
            if line:
                content_lines.append(line)
                
            # ネストされたブロックがある場合
            if block.get("has_children"):
                child_blocks = get_page_content_with_retry(block["id"])
                for child_block in child_blocks:
                    child_line = block_to_markdown(child_block, indent_level=1)
                    if child_line:
                        content_lines.append(child_line)
        
        # 新しい内容を構築
        new_content = metadata + "\n" + "\n".join(content_lines)
        
        # ファイルを更新
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True, f"Updated with {len(blocks)} blocks"
        
    except Exception as e:
        return False, str(e)

def main():
    """メイン処理"""
    print("=" * 60)
    print("Notion Yoshinani Main Folder Priority Fetcher")
    print("=" * 60)
    
    # 状態を読み込む
    state = load_state()
    
    # プレースホルダーファイルをスキャン
    print("\n1. Scanning for placeholder files...")
    print(f"Target directories: {len(TARGET_DIRS)}")
    
    all_files = []
    
    for target_dir in TARGET_DIRS:
        if not os.path.exists(target_dir):
            continue
            
        print(f"\nScanning: {target_dir}")
        dir_count = 0
        
        for filename in sorted(os.listdir(target_dir)):
            if filename.endswith('.md') and not filename.startswith('.'):
                filepath = os.path.join(target_dir, filename)
                
                # 既に処理済みならスキップ
                if filepath in state["processed_files"]:
                    continue
                    
                if is_placeholder_file(filepath):
                    notion_id = extract_notion_id(filepath)
                    if notion_id:
                        # よしなに関連度スコアを計算
                        score = calculate_yoshinani_score(filename)
                        all_files.append((filepath, notion_id, score, filename))
                        dir_count += 1
        
        print(f"  Found {dir_count} placeholder files")
    
    if not all_files:
        print("\nNo placeholder files found to process!")
        
        # 処理済みファイルをクリアするか確認
        if state["processed_files"]:
            print(f"\nNote: {len(state['processed_files'])} files marked as processed.")
            print("Run with --reset to clear processing history.")
        return
    
    # よしなに関連度でソート（スコアが高い順）
    all_files.sort(key=lambda x: x[2], reverse=True)
    
    print(f"\nTotal placeholder files to process: {len(all_files)}")
    
    # よしなに関連ファイルの数を表示
    yoshinani_files = [f for f in all_files if f[2] > 0]
    print(f"Yoshinani-related files: {len(yoshinani_files)}")
    
    if yoshinani_files:
        print("\nTop Yoshinani files:")
        for i, (path, _, score, name) in enumerate(yoshinani_files[:10]):
            print(f"  {i+1}. {name} (Score: {score})")
    
    # バッチで処理
    batch_files = all_files[:BATCH_SIZE]
    print(f"\n2. Processing batch of {len(batch_files)} files...")
    print("-" * 60)
    
    batch_success = 0
    batch_failed = 0
    
    for i, (filepath, notion_id, score, filename) in enumerate(batch_files):
        dir_name = os.path.basename(os.path.dirname(filepath))
        
        if score > 0:
            print(f"\n[{i+1}/{len(batch_files)}] {dir_name}/{filename} 🎯 (Score: {score})")
        else:
            print(f"\n[{i+1}/{len(batch_files)}] {dir_name}/{filename}")
        
        success, message = update_file_content(filepath, notion_id)
        
        if success:
            batch_success += 1
            state["total_updated"] += 1
            print(f"    ✓ {message}")
        else:
            batch_failed += 1
            state["total_failed"] += 1
            state["errors"].append(f"{filepath}: {message}")
            print(f"    ✗ {message}")
        
        # 処理済みリストに追加
        state["processed_files"].append(filepath)
        
        # レート制限対策
        time.sleep(0.5)
    
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
    
    # エラーがある場合は最新のものを表示
    if state["errors"] and batch_failed > 0:
        print("\nRecent errors:")
        for error in state["errors"][-5:]:
            print(f"  - {error}")

if __name__ == "__main__":
    # コマンドライン引数でリセットオプション
    if len(sys.argv) > 1 and sys.argv[1] == "--reset":
        if os.path.exists(STATE_FILE):
            os.remove(STATE_FILE)
            print("Processing history cleared.")
    
    main()