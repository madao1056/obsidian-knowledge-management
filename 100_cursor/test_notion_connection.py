#!/usr/bin/env python3
"""Notion接続テスト"""
import requests

# Notion API設定
NOTION_TOKEN = "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"
HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28"
}

# ユーザー情報を取得
url = "https://api.notion.com/v1/users/me"
response = requests.get(url, headers=HEADERS)

print(f"Status: {response.status_code}")
if response.status_code == 200:
    data = response.json()
    print(f"Connected as: {data.get('name', 'Unknown')}")
    print(f"Type: {data.get('type')}")
else:
    print(f"Error: {response.text}")

# 簡単な検索を実行
print("\nTrying to search pages...")
search_url = "https://api.notion.com/v1/search"
search_response = requests.post(search_url, headers=HEADERS, json={})

if search_response.status_code == 200:
    results = search_response.json()
    print(f"Found {len(results.get('results', []))} items")
    for item in results.get('results', [])[:3]:  # 最初の3件だけ表示
        title = "Untitled"
        if 'properties' in item and 'title' in item['properties']:
            title_prop = item['properties']['title']
            if title_prop.get('title'):
                title = title_prop['title'][0].get('plain_text', 'Untitled')
        print(f"- {title}")
else:
    print(f"Search error: {search_response.text}")