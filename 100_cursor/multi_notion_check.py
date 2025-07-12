#!/usr/bin/env python3
"""
複数Notionアカウントのボリューム確認スクリプト
"""
import requests
import time

# 設定
NOTION_ACCOUNTS = {
    "Main": "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",
    "Secondary": "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"
}

NOTION_VERSION = "2022-06-28"

def get_headers(token):
    return {
        "Authorization": f"Bearer {token}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json"
    }

def test_connection(account_name, token):
    """接続テスト"""
    headers = get_headers(token)
    url = "https://api.notion.com/v1/users/me"
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return True, data.get('name', 'Unknown')
        else:
            return False, f"Error {response.status_code}: {response.text}"
    except Exception as e:
        return False, str(e)

def count_pages(token):
    """ページ数をカウント"""
    headers = get_headers(token)
    url = "https://api.notion.com/v1/search"
    payload = {
        "filter": {"property": "object", "value": "page"},
        "page_size": 100
    }
    
    total = 0
    has_more = True
    start_cursor = None
    
    try:
        while has_more:
            if start_cursor:
                payload["start_cursor"] = start_cursor
            
            response = requests.post(url, headers=headers, json=payload)
            if response.status_code == 200:
                data = response.json()
                results = data.get("results", [])
                total += len(results)
                has_more = data.get("has_more", False)
                start_cursor = data.get("next_cursor")
                
                # 進捗表示
                if total % 100 == 0:
                    print(f"    ... {total} pages counted so far")
                    
            else:
                print(f"    Error: {response.status_code}")
                break
                
    except Exception as e:
        print(f"    Error counting: {str(e)}")
        return 0
    
    return total

def get_sample_pages(token, limit=5):
    """サンプルページを取得"""
    headers = get_headers(token)
    url = "https://api.notion.com/v1/search"
    payload = {
        "filter": {"property": "object", "value": "page"},
        "page_size": limit
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            data = response.json()
            pages = []
            for page in data.get("results", []):
                title = "Untitled"
                try:
                    if 'properties' in page:
                        for prop_name, prop_value in page['properties'].items():
                            if prop_value['type'] == 'title' and prop_value.get('title'):
                                title = prop_value['title'][0]['plain_text']
                                break
                except:
                    pass
                pages.append(title)
            return pages
        return []
    except:
        return []

def estimate_sync_time(total_pages):
    """同期時間を推定"""
    # 実測値：約1ページ/秒
    pages_per_minute = 60
    
    # API制限を考慮（Notion無料プランは3リクエスト/分の制限）
    # ただし、実際は1ページあたり複数リクエストが必要
    realistic_pages_per_minute = 30  # 保守的な見積もり
    
    estimated_minutes = total_pages / realistic_pages_per_minute
    
    return {
        "minutes": estimated_minutes,
        "hours": estimated_minutes / 60,
        "display": f"{int(estimated_minutes)}分 ({estimated_minutes/60:.1f}時間)"
    }

def main():
    """メイン処理"""
    print("🔍 Multiple Notion Accounts Volume Check")
    print("=" * 60)
    
    total_pages_all_accounts = 0
    account_stats = {}
    
    for account_name, token in NOTION_ACCOUNTS.items():
        print(f"\n📊 Checking {account_name} Account")
        print("-" * 40)
        
        # 接続テスト
        print("1. Testing connection...")
        is_connected, connection_info = test_connection(account_name, token)
        
        if is_connected:
            print(f"   ✅ Connected as: {connection_info}")
            
            # ページ数カウント
            print("2. Counting pages...")
            page_count = count_pages(token)
            print(f"   📄 Total pages: {page_count}")
            
            # サンプルページ
            print("3. Getting sample pages...")
            sample_pages = get_sample_pages(token)
            for i, title in enumerate(sample_pages, 1):
                print(f"   {i}. {title[:50]}...")
            
            # 統計に追加
            total_pages_all_accounts += page_count
            account_stats[account_name] = {
                "pages": page_count,
                "connection": connection_info,
                "sample_pages": sample_pages
            }
            
        else:
            print(f"   ❌ Connection failed: {connection_info}")
            account_stats[account_name] = {
                "pages": 0,
                "connection": f"Failed: {connection_info}",
                "sample_pages": []
            }
    
    # 全体サマリー
    print("\n" + "=" * 60)
    print("📋 VOLUME SUMMARY")
    print("=" * 60)
    
    for account_name, stats in account_stats.items():
        percentage = (stats["pages"] / total_pages_all_accounts * 100) if total_pages_all_accounts > 0 else 0
        print(f"{account_name:12}: {stats['pages']:5} pages ({percentage:5.1f}%)")
    
    print("-" * 30)
    print(f"{'TOTAL':12}: {total_pages_all_accounts:5} pages")
    
    # 同期時間推定
    if total_pages_all_accounts > 0:
        time_estimate = estimate_sync_time(total_pages_all_accounts)
        
        print(f"\n⏱️  ESTIMATED SYNC TIME")
        print("-" * 30)
        print(f"Total pages to sync: {total_pages_all_accounts}")
        print(f"Estimated time:      {time_estimate['display']}")
        print(f"Rate assumption:     ~30 pages/minute")
        
        # 段階的同期の提案
        print(f"\n💡 SYNC STRATEGY RECOMMENDATIONS")
        print("-" * 40)
        
        if total_pages_all_accounts > 1000:
            print("🔄 Batch sync recommended (50-100 pages at a time)")
            print("📅 Schedule during low-usage hours")
            print("⏸️  Consider pause/resume capability")
        elif total_pages_all_accounts > 500:
            print("🚀 Direct sync feasible but may take a while")
            print("📊 Monitor progress closely")
        else:
            print("✅ Direct sync recommended - manageable size")
        
        # 優先度付けの提案
        print(f"\n🎯 PRIORITIZATION SUGGESTIONS")
        print("-" * 40)
        print("1. Identify frequently accessed pages first")
        print("2. Sync main workspace before secondary")
        print("3. Consider filtering by last modified date")

if __name__ == "__main__":
    main()