#!/usr/bin/env python3
"""
Notion段階的同期スクリプト（バッチ処理）
"""
import os
import json
import requests
from datetime import datetime
import time

# 設定
NOTION_TOKEN = "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"
HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}
OUTPUT_DIR = "/Users/hashiguchimasaki/project/obsidian/20_Literature/25_Notion"
BATCH_SIZE = 50  # 1回あたりのページ数
MAX_RETRIES = 3

def save_progress(batch_num, total_synced, total_pages, errors):
    """進捗を保存"""
    progress = {
        "last_batch": batch_num,
        "total_synced": total_synced,
        "total_pages": total_pages,
        "completion_rate": (total_synced / total_pages) * 100,
        "last_sync": datetime.now().isoformat(),
        "errors": errors[-10:]  # 直近10個のエラーのみ
    }
    
    with open(os.path.join(OUTPUT_DIR, ".sync_progress.json"), 'w') as f:
        json.dump(progress, f, indent=2)

def load_progress():
    """進捗を読み込み"""
    try:
        with open(os.path.join(OUTPUT_DIR, ".sync_progress.json"), 'r') as f:
            return json.load(f)
    except:
        return {"last_batch": 0, "total_synced": 0}

def get_all_page_ids():
    """全ページIDを取得（軽量）"""
    url = "https://api.notion.com/v1/search"
    payload = {
        "filter": {"property": "object", "value": "page"},
        "page_size": 100
    }
    
    all_page_ids = []
    has_more = True
    start_cursor = None
    
    while has_more:
        if start_cursor:
            payload["start_cursor"] = start_cursor
        
        response = requests.post(url, headers=HEADERS, json=payload)
        if response.status_code == 200:
            data = response.json()
            for page in data.get("results", []):
                all_page_ids.append({
                    "id": page["id"],
                    "title": get_page_title(page),
                    "url": page.get("url", "")
                })
            has_more = data.get("has_more", False)
            start_cursor = data.get("next_cursor")
        else:
            print(f"Error: {response.status_code}")
            break
        
        # 進捗表示
        if len(all_page_ids) % 100 == 0:
            print(f"  Collected {len(all_page_ids)} page IDs...")
    
    return all_page_ids

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

def sync_batch(page_ids, batch_num, start_idx, end_idx):
    """バッチ同期"""
    print(f"\n=== Batch {batch_num}: Pages {start_idx+1}-{end_idx} ===")
    
    batch_pages = page_ids[start_idx:end_idx]
    synced = 0
    errors = []
    
    for i, page_info in enumerate(batch_pages):
        page_id = page_info["id"]
        title = page_info["title"]
        
        print(f"[{start_idx + i + 1}/{len(page_ids)}] {title[:50]}...")
        
        try:
            # ファイルが既に存在するかチェック
            filename = f"{title.replace('/', '_')[:100]}.md"
            filepath = os.path.join(OUTPUT_DIR, filename)
            
            if os.path.exists(filepath):
                print("  ⏭️  Already exists, skipping")
                synced += 1
                continue
            
            # 簡易メタデータのみでファイル作成（高速化）
            metadata = f"""---
notion_id: {page_id}
title: {title}
url: {page_info.get('url', '')}
sync_status: placeholder
sync_time: {datetime.now().isoformat()}
---

# {title}

*This is a placeholder. Full content will be synced later.*

[Open in Notion]({page_info.get('url', '')})
"""
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(metadata)
            
            synced += 1
            print("  ✅ Placeholder created")
            
        except Exception as e:
            error_msg = f"{title}: {str(e)}"
            errors.append(error_msg)
            print(f"  ❌ Error: {str(e)}")
    
    return synced, errors

def main():
    """メイン処理"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    print("🚀 Notion Batch Sync - Starting")
    print("=" * 60)
    
    # 進捗を確認
    progress = load_progress()
    start_batch = progress.get("last_batch", 0)
    
    if start_batch > 0:
        print(f"📋 Resuming from batch {start_batch + 1}")
    
    # 全ページIDを取得
    print("\n1. Collecting all page IDs...")
    all_page_ids = get_all_page_ids()
    total_pages = len(all_page_ids)
    
    print(f"   Total pages: {total_pages}")
    print(f"   Batch size: {BATCH_SIZE}")
    print(f"   Estimated batches: {(total_pages + BATCH_SIZE - 1) // BATCH_SIZE}")
    
    # バッチ処理
    print("\n2. Starting batch sync...")
    total_synced = progress.get("total_synced", 0)
    all_errors = []
    
    for batch_num in range(start_batch, (total_pages + BATCH_SIZE - 1) // BATCH_SIZE):
        start_idx = batch_num * BATCH_SIZE
        end_idx = min(start_idx + BATCH_SIZE, total_pages)
        
        batch_synced, batch_errors = sync_batch(all_page_ids, batch_num + 1, start_idx, end_idx)
        
        total_synced += batch_synced
        all_errors.extend(batch_errors)
        
        # 進捗保存
        save_progress(batch_num, total_synced, total_pages, all_errors)
        
        completion_rate = (total_synced / total_pages) * 100
        print(f"\n📊 Progress: {total_synced}/{total_pages} ({completion_rate:.1f}%)")
        
        # エラー表示
        if batch_errors:
            print(f"❌ Batch errors: {len(batch_errors)}")
        
        # API制限を考慮した待機時間
        if batch_num < ((total_pages + BATCH_SIZE - 1) // BATCH_SIZE) - 1:
            print("⏳ Waiting 2 seconds to respect API limits...")
            time.sleep(2)
    
    # 最終結果
    print("\n" + "=" * 60)
    print("🎉 BATCH SYNC COMPLETED")
    print("=" * 60)
    print(f"📈 Total synced: {total_synced}/{total_pages}")
    print(f"🎯 Completion rate: {(total_synced/total_pages)*100:.1f}%")
    print(f"❌ Total errors: {len(all_errors)}")
    print(f"📁 Output directory: {OUTPUT_DIR}")
    
    if all_errors:
        print(f"\n⚠️  Last few errors:")
        for error in all_errors[-5:]:
            print(f"   • {error}")

if __name__ == "__main__":
    main()