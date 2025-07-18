#!/usr/bin/env python3
"""
notion_sync_env環境でのNotion連携テスト
"""

import os
import sys
from pathlib import Path

def test_notion_env():
    """notion_sync_env環境のテスト"""
    
    print("🔍 Python環境の確認")
    print(f"Python実行パス: {sys.executable}")
    print(f"Python バージョン: {sys.version}")
    
    print("\n📦 インストール済みパッケージの確認")
    try:
        import pkg_resources
        installed_packages = [d.project_name for d in pkg_resources.working_set]
        
        # Notion関連パッケージをチェック
        notion_packages = [pkg for pkg in installed_packages if 'notion' in pkg.lower()]
        if notion_packages:
            print(f"✅ Notion関連パッケージ: {notion_packages}")
        else:
            print("❌ Notion関連パッケージが見つかりません")
        
        # 主要パッケージをチェック
        important_packages = ['requests', 'urllib3', 'certifi']
        for pkg in important_packages:
            if pkg in installed_packages:
                print(f"✅ {pkg}")
            else:
                print(f"❌ {pkg}")
                
    except ImportError:
        print("❌ pkg_resourcesが利用できません")
    
    print("\n🔑 環境変数の確認")
    notion_api_key = os.getenv('NOTION_API_KEY')
    if notion_api_key:
        masked_key = notion_api_key[:10] + "..." + notion_api_key[-4:]
        print(f"✅ NOTION_API_KEY: {masked_key}")
    else:
        print("❌ NOTION_API_KEY が設定されていません")
    
    print("\n🧪 Notion連携テスト")
    try:
        # notion_integration.pyを現在のディレクトリから読み込み
        current_dir = Path(__file__).parent
        sys.path.insert(0, str(current_dir))
        
        from notion_integration import NotionIntegration
        
        # 初期化テスト
        notion = NotionIntegration()
        
        if notion.client:
            print("✅ NotionIntegration 初期化成功")
            
            # テストメッセージでリンク抽出
            test_message = """
            プロジェクト進捗: https://www.notion.so/test-page-123abc456def
            詳細資料: https://notion.so/project-details-789xyz
            """
            
            links = notion.extract_notion_links(test_message)
            print(f"✅ リンク抽出テスト: {len(links)}個のリンクを検出")
            for link in links:
                print(f"   - URL: {link['url']}")
                print(f"   - ID: {link['page_id']}")
            
        else:
            print("❌ NotionIntegration 初期化失敗")
            
    except ImportError as e:
        print(f"❌ notion-client インポートエラー: {e}")
        print("💡 以下のコマンドでインストールしてください:")
        print("   pip install notion-client")
        
    except Exception as e:
        print(f"❌ 予期しないエラー: {e}")
    
    print("\n📝 使用方法")
    print("この環境でNotion連携を使用するには:")
    print("1. 仮想環境をアクティベート:")
    print("   source /Users/hashiguchimasaki/project/obsidian/notion_sync_env/bin/activate")
    print("2. 必要なパッケージをインストール:")
    print("   pip install notion-client")
    print("3. 環境変数を設定:")
    print("   export NOTION_API_KEY='your-api-key'")
    print("4. スクリプトを実行:")
    print("   python3 monthly_report_analyzer.py 2025 7")

if __name__ == "__main__":
    test_notion_env()