#!/usr/bin/env python3
"""
Notion API連携機能
Discord月報で共有されたNotionリンクの内容を取得
"""

import os
import re
import json
from datetime import datetime
from typing import List, Dict, Optional
import logging
from urllib.parse import urlparse
import time

# Notion APIライブラリのインポート（pip install notion-client が必要）
try:
    from notion_client import Client
except ImportError:
    Client = None
    print("⚠️  notion-clientがインストールされていません")
    print("実行: pip install notion-client")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class NotionIntegration:
    def __init__(self, api_key: Optional[str] = None):
        """
        Notion API統合の初期化
        
        Args:
            api_key: Notion APIキー（環境変数NOTION_API_KEYからも取得可能）
        """
        self.api_key = api_key or os.getenv('NOTION_API_KEY')
        
        if not self.api_key:
            logger.warning("⚠️  Notion APIキーが設定されていません")
            logger.info("以下の手順でAPIキーを取得してください：")
            logger.info("1. https://www.notion.so/my-integrations にアクセス")
            logger.info("2. 'New integration'をクリック")
            logger.info("3. 名前を入力して作成")
            logger.info("4. Internal Integration Tokenをコピー")
            logger.info("5. 環境変数 NOTION_API_KEY に設定")
            self.client = None
        else:
            self.client = Client(auth=self.api_key) if Client else None
    
    def extract_notion_links(self, content: str) -> List[Dict[str, str]]:
        """
        テキストからNotionリンクを抽出
        
        Args:
            content: 検索対象のテキスト
            
        Returns:
            抽出されたNotionリンク情報のリスト
        """
        notion_links = []
        
        # Notionリンクのパターン
        patterns = [
            r'https?://(?:www\.)?notion\.so/[a-zA-Z0-9-]+(?:/[a-zA-Z0-9-]+)?',
            r'https?://[a-zA-Z0-9-]+\.notion\.site/[a-zA-Z0-9-]+',
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, content)
            for match in matches:
                # IDを抽出
                parsed = urlparse(match)
                path_parts = parsed.path.strip('/').split('/')
                
                if path_parts:
                    # 最後の部分からIDを抽出（通常は最後の32文字）
                    last_part = path_parts[-1]
                    if '-' in last_part:
                        # タイトル付きURL（例: My-Page-123abc...）
                        page_id = last_part.split('-')[-1]
                    else:
                        page_id = last_part
                    
                    # ハイフンを除去
                    page_id = page_id.replace('-', '')
                    
                    notion_links.append({
                        'url': match,
                        'page_id': page_id,
                        'type': 'page'  # デフォルトはページとして扱う
                    })
        
        return notion_links
    
    def get_page_content(self, page_id: str) -> Optional[Dict]:
        """
        NotionページのコンテンツとプロパティをAPI経由で取得
        
        Args:
            page_id: NotionページのID
            
        Returns:
            ページ情報（タイトル、プロパティ、ブロック内容）
        """
        if not self.client:
            logger.error("Notion APIクライアントが初期化されていません")
            return None
        
        try:
            # ページ情報を取得
            page = self.client.pages.retrieve(page_id=page_id)
            
            # ページのブロック（コンテンツ）を取得
            blocks = []
            has_more = True
            start_cursor = None
            
            while has_more:
                response = self.client.blocks.children.list(
                    block_id=page_id,
                    start_cursor=start_cursor
                )
                blocks.extend(response.get('results', []))
                has_more = response.get('has_more', False)
                start_cursor = response.get('next_cursor')
                
                # レート制限対策
                time.sleep(0.1)
            
            # コンテンツを解析
            content_text = self._extract_text_from_blocks(blocks)
            
            # プロパティを解析
            properties = self._extract_properties(page.get('properties', {}))
            
            # タイトルを取得
            title = self._get_page_title(page)
            
            return {
                'id': page_id,
                'title': title,
                'url': page.get('url', ''),
                'properties': properties,
                'content': content_text,
                'created_time': page.get('created_time'),
                'last_edited_time': page.get('last_edited_time'),
                'blocks_count': len(blocks)
            }
            
        except Exception as e:
            logger.error(f"ページ取得エラー（{page_id}）: {e}")
            if "unauthorized" in str(e).lower():
                logger.info("💡 このページにアクセスするには：")
                logger.info("1. Notionでページを開く")
                logger.info("2. 右上の「...」メニューから「Add connections」を選択")
                logger.info("3. 作成したインテグレーションを選択して追加")
            return None
    
    def _extract_text_from_blocks(self, blocks: List[Dict]) -> str:
        """ブロックからテキストを抽出"""
        text_parts = []
        
        for block in blocks:
            block_type = block.get('type')
            
            if block_type in ['paragraph', 'heading_1', 'heading_2', 'heading_3']:
                rich_text = block.get(block_type, {}).get('rich_text', [])
                text = self._extract_rich_text(rich_text)
                if text:
                    text_parts.append(text)
            
            elif block_type == 'bulleted_list_item':
                rich_text = block.get('bulleted_list_item', {}).get('rich_text', [])
                text = self._extract_rich_text(rich_text)
                if text:
                    text_parts.append(f"• {text}")
            
            elif block_type == 'numbered_list_item':
                rich_text = block.get('numbered_list_item', {}).get('rich_text', [])
                text = self._extract_rich_text(rich_text)
                if text:
                    text_parts.append(f"- {text}")
            
            elif block_type == 'to_do':
                rich_text = block.get('to_do', {}).get('rich_text', [])
                checked = block.get('to_do', {}).get('checked', False)
                text = self._extract_rich_text(rich_text)
                if text:
                    checkbox = "✅" if checked else "☐"
                    text_parts.append(f"{checkbox} {text}")
            
            elif block_type == 'code':
                rich_text = block.get('code', {}).get('rich_text', [])
                language = block.get('code', {}).get('language', '')
                text = self._extract_rich_text(rich_text)
                if text:
                    text_parts.append(f"```{language}\n{text}\n```")
        
        return '\n\n'.join(text_parts)
    
    def _extract_rich_text(self, rich_text: List[Dict]) -> str:
        """リッチテキストからプレーンテキストを抽出"""
        return ''.join([rt.get('plain_text', '') for rt in rich_text])
    
    def _extract_properties(self, properties: Dict) -> Dict:
        """プロパティから重要な情報を抽出"""
        extracted = {}
        
        for key, value in properties.items():
            prop_type = value.get('type')
            
            if prop_type == 'title':
                title_items = value.get('title', [])
                extracted[key] = self._extract_rich_text(title_items)
            
            elif prop_type == 'rich_text':
                text_items = value.get('rich_text', [])
                extracted[key] = self._extract_rich_text(text_items)
            
            elif prop_type == 'number':
                extracted[key] = value.get('number')
            
            elif prop_type == 'select':
                select = value.get('select', {})
                if select:
                    extracted[key] = select.get('name')
            
            elif prop_type == 'multi_select':
                items = value.get('multi_select', [])
                extracted[key] = [item.get('name') for item in items]
            
            elif prop_type == 'date':
                date_obj = value.get('date', {})
                if date_obj:
                    extracted[key] = date_obj.get('start')
            
            elif prop_type == 'checkbox':
                extracted[key] = value.get('checkbox', False)
            
            elif prop_type == 'url':
                extracted[key] = value.get('url')
            
            elif prop_type == 'email':
                extracted[key] = value.get('email')
            
            elif prop_type == 'phone_number':
                extracted[key] = value.get('phone_number')
        
        return extracted
    
    def _get_page_title(self, page: Dict) -> str:
        """ページタイトルを取得"""
        properties = page.get('properties', {})
        
        # タイトルプロパティを探す
        for prop_name, prop_value in properties.items():
            if prop_value.get('type') == 'title':
                title_items = prop_value.get('title', [])
                return self._extract_rich_text(title_items)
        
        return "無題"
    
    def process_discord_message(self, message_content: str) -> List[Dict]:
        """
        Discordメッセージ内のNotionリンクを処理
        
        Args:
            message_content: Discordメッセージの内容
            
        Returns:
            処理されたNotionコンテンツのリスト
        """
        # Notionリンクを抽出
        links = self.extract_notion_links(message_content)
        
        if not links:
            return []
        
        results = []
        
        for link_info in links:
            logger.info(f"📄 Notionページを取得中: {link_info['url']}")
            
            # ページコンテンツを取得
            page_content = self.get_page_content(link_info['page_id'])
            
            if page_content:
                results.append({
                    'original_url': link_info['url'],
                    'page_data': page_content,
                    'extracted_at': datetime.now().isoformat()
                })
                logger.info(f"✅ ページ取得成功: {page_content['title']}")
            else:
                logger.warning(f"⚠️  ページ取得失敗: {link_info['url']}")
        
        return results
    
    def save_notion_content(self, member_name: str, notion_data: List[Dict], 
                          output_dir: str = "03_Support/グッサポ・ラボ/メンバー管理"):
        """
        取得したNotionコンテンツをメンバーフォルダに保存
        
        Args:
            member_name: メンバー名
            notion_data: Notionコンテンツデータ
            output_dir: 出力ディレクトリ
        """
        if not notion_data:
            return
        
        from pathlib import Path
        
        # 出力パスを設定
        base_path = Path(__file__).parent.parent / output_dir / member_name
        notion_dir = base_path / "Notion資料"
        notion_dir.mkdir(parents=True, exist_ok=True)
        
        # サマリーファイルを作成
        summary_path = notion_dir / "Notion資料_サマリー.md"
        
        summary_content = f"""# {member_name} - Notion資料

## 📄 共有された資料一覧

"""
        
        for idx, data in enumerate(notion_data, 1):
            page_info = data['page_data']
            
            # 個別ファイルを作成
            safe_title = re.sub(r'[<>:"/\\|?*]', '_', page_info['title'])
            page_file = notion_dir / f"{idx:02d}_{safe_title}.md"
            
            # ページ内容を整形
            page_content = f"""# {page_info['title']}

- **元URL**: {data['original_url']}
- **最終更新**: {page_info.get('last_edited_time', 'N/A')}
- **取得日時**: {data['extracted_at']}

## プロパティ
"""
            
            # プロパティを追加
            if page_info['properties']:
                for key, value in page_info['properties'].items():
                    if value:
                        page_content += f"- **{key}**: {value}\n"
            else:
                page_content += "（プロパティなし）\n"
            
            page_content += f"""
## 内容

{page_info['content']}
"""
            
            # ファイルに保存
            with open(page_file, 'w', encoding='utf-8') as f:
                f.write(page_content)
            
            # サマリーに追加
            summary_content += f"### {idx}. [{page_info['title']}]({page_file.name})\n"
            summary_content += f"- 最終更新: {page_info.get('last_edited_time', 'N/A')[:10]}\n"
            
            # 重要なプロパティをサマリーに追加
            important_props = ['ステータス', 'Status', '進捗', 'Progress', '締切', 'Due']
            for prop in important_props:
                if prop in page_info['properties'] and page_info['properties'][prop]:
                    summary_content += f"- {prop}: {page_info['properties'][prop]}\n"
            
            summary_content += "\n"
        
        # サマリーファイルを保存
        with open(summary_path, 'w', encoding='utf-8') as f:
            f.write(summary_content)
        
        logger.info(f"📚 {member_name}のNotion資料を保存しました（{len(notion_data)}件）")

# 使用例
if __name__ == "__main__":
    # APIキーを環境変数から取得
    notion = NotionIntegration()
    
    # テストメッセージ
    test_message = """
    今月の月報です。
    詳細はこちら: https://www.notion.so/My-Monthly-Report-abc123def456
    プロジェクト進捗: https://notion.so/project-status-789xyz
    """
    
    # Notionコンテンツを処理
    results = notion.process_discord_message(test_message)
    
    if results:
        # メンバーフォルダに保存
        notion.save_notion_content("テストメンバー", results)