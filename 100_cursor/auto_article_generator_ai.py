#!/usr/bin/env python3
"""
AI統合版自動記事生成システム
Claude APIを使用した高品質な記事生成
"""

import os
import re
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional
import subprocess

# Claude API設定（環境変数またはここに直接設定）
# export CLAUDE_API_KEY="your-api-key"

class AIArticleGenerator:
    def __init__(self, vault_path, api_key=None):
        self.vault_path = Path(vault_path)
        self.inbox_clip = self.vault_path / "00_Inbox" / "clip"
        self.literature = self.vault_path / "20_Literature"
        self.permanent = self.vault_path / "30_Permanent"
        self.share = self.vault_path / "70_Share" / "78_Personal"
        self.log_dir = self.vault_path / "100_cursor" / "logs"
        
        # API設定
        self.api_key = api_key or os.environ.get('CLAUDE_API_KEY')
        
        # ディレクトリを作成
        self.log_dir.mkdir(exist_ok=True)
        self.share.mkdir(exist_ok=True)
        
        # ロガーを設定
        self.setup_logger()
    
    def setup_logger(self):
        """ログシステムを設定"""
        log_file = self.log_dir / f"ai_article_{datetime.now().strftime('%Y%m%d')}.log"
        
        self.logger = logging.getLogger('AIArticleGenerator')
        self.logger.setLevel(logging.INFO)
        
        fh = logging.FileHandler(log_file, encoding='utf-8')
        fh.setLevel(logging.INFO)
        
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        
        self.logger.addHandler(fh)
    
    def check_claude_api(self):
        """Claude APIが利用可能かチェック"""
        if not self.api_key:
            self.logger.warning("Claude API key not found. Using basic mode.")
            return False
        
        try:
            import anthropic
            self.client = anthropic.Anthropic(api_key=self.api_key)
            return True
        except ImportError:
            self.logger.warning("anthropic package not installed. Run: pip install anthropic")
            return False
        except Exception as e:
            self.logger.error(f"Error initializing Claude API: {e}")
            return False
    
    def generate_with_claude(self, prompt: str, system_prompt: str = "") -> Optional[str]:
        """Claude APIを使用してテキストを生成"""
        if not hasattr(self, 'client'):
            return None
        
        try:
            message = self.client.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=4000,
                temperature=0.7,
                system=system_prompt,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return message.content[0].text
        except Exception as e:
            self.logger.error(f"Claude API error: {e}")
            return None
    
    def extract_and_enhance_content(self, file_path):
        """AIを使用してコンテンツを分析・強化"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 基本的なメタデータ抽出
        metadata = self._extract_basic_metadata(content)
        
        # AIが利用可能な場合は強化
        if hasattr(self, 'client'):
            enhanced_data = self._enhance_with_ai(content, metadata)
            return enhanced_data
        else:
            # AIなしの場合は基本版を使用
            from auto_article_generator import AutoArticleGenerator
            basic_generator = AutoArticleGenerator(self.vault_path)
            return basic_generator.extract_key_insights(file_path)
    
    def _extract_basic_metadata(self, content):
        """基本的なメタデータ抽出"""
        metadata = {}
        
        title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
        if title_match:
            metadata['title'] = title_match.group(1)
        
        source_match = re.search(r'- \*\*ソース\*\*: (.+)$', content, re.MULTILINE)
        if source_match:
            metadata['source'] = source_match.group(1)
        
        return metadata
    
    def _enhance_with_ai(self, content, metadata):
        """AIを使用してコンテンツを分析・強化"""
        self.logger.info("Enhancing content with AI")
        
        system_prompt = """あなたは知識管理の専門家です。
提供されたコンテンツを分析し、以下の形式でJSONを返してください：
{
    "title": "記事のタイトル",
    "summary": "200文字程度の要約",
    "key_insights": ["洞察1", "洞察2", "洞察3"],
    "practical_applications": ["応用1", "応用2", "応用3"],
    "questions": ["疑問1", "疑問2"],
    "connections": ["関連トピック1", "関連トピック2"],
    "category": "Tech/Philosophy/Productivity/AI/Product"
}"""
        
        prompt = f"""以下のコンテンツを分析してください：

{content}

上記のコンテンツから重要な洞察を抽出し、指定されたJSON形式で返してください。"""
        
        response = self.generate_with_claude(prompt, system_prompt)
        
        if response:
            try:
                analysis = json.loads(response)
                return {
                    'metadata': {**metadata, **analysis},
                    'insights': analysis.get('key_insights', []),
                    'applications': analysis.get('practical_applications', []),
                    'category': analysis.get('category', 'Tech')
                }
            except json.JSONDecodeError:
                self.logger.error("Failed to parse AI response as JSON")
        
        return None
    
    def generate_high_quality_article(self, data):
        """AIを使用して高品質な記事を生成"""
        if not hasattr(self, 'client'):
            # AIなしの場合は基本版を使用
            from auto_article_generator import AutoArticleGenerator
            basic_generator = AutoArticleGenerator(self.vault_path)
            return basic_generator._generate_article_content({}, data)
        
        system_prompt = """あなたは優れたテクニカルライターです。
以下の要件で記事を作成してください：
- 5000-7000文字程度
- 読者を引き込むフック文から開始
- 具体例を豊富に含める
- 実践的なアドバイスを提供
- 個人的な感想や考察を含める
- 日本語で執筆"""
        
        prompt = f"""以下の情報を基に、魅力的な記事を作成してください：

タイトル: {data['metadata'].get('title', 'Untitled')}
要約: {data['metadata'].get('summary', '')}
主要な洞察: {', '.join(data.get('insights', []))}
実践的応用: {', '.join(data.get('applications', []))}

記事は以下の構成にしてください：
1. フック文（読者の興味を引く導入）
2. 記事の概要
3. 主要ポイント（3-5個）
4. 実践的な活用例
5. 筆者の感想
6. 記事のポイント（まとめ）
7. 今後の展望

マークダウン形式で出力してください。"""
        
        article = self.generate_with_claude(prompt, system_prompt)
        
        if article:
            # メタデータを追加
            footer = f"""

---

**生成日**: {datetime.now().strftime('%Y-%m-%d')}  
**カテゴリ**: {data.get('category', 'Tech')}  
**タグ**: #share/blog #ai-generated #{data.get('category', 'tech').lower()}  
**ソース**: {data['metadata'].get('source', 'Unknown')}

🤖 この記事はAIを活用して生成されました。
"""
            return article + footer
        
        return None
    
    def process_with_ai(self):
        """AI統合版の完全自動処理"""
        print("🤖 AI-Powered Article Generation")
        
        # Claude APIチェック
        ai_available = self.check_claude_api()
        if ai_available:
            print("✓ Claude API connected")
        else:
            print("⚠️  Running in basic mode (no AI)")
        
        # Step 1: ClipをLiteratureに処理
        print("\n📋 Step 1: Processing clips...")
        result = subprocess.run(
            ['python3', str(self.vault_path / '100_cursor' / 'process_clip.py')],
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            print("✗ Failed to process clips")
            return []
        
        # 最近のLiteratureファイルを取得
        recent_files = []
        cutoff_time = datetime.now().timestamp() - (5 * 60)  # 5分以内
        
        for file_path in self.literature.glob("**/*.md"):
            if file_path.stat().st_mtime > cutoff_time:
                recent_files.append(file_path)
        
        if not recent_files:
            print("No new files to process")
            return []
        
        generated_articles = []
        
        for lit_file in recent_files:
            try:
                print(f"\n📄 Processing: {lit_file.name}")
                
                # Step 2: AIで分析
                print("  🔍 Analyzing content...")
                analysis = self.extract_and_enhance_content(lit_file)
                
                if not analysis:
                    print("  ✗ Analysis failed")
                    continue
                
                # Step 3: Permanentノート作成
                print("  💡 Creating permanent note...")
                permanent_path = self._create_enhanced_permanent(analysis)
                
                # Step 4: 記事生成
                print("  ✍️  Generating article...")
                article_content = self.generate_high_quality_article(analysis)
                
                if article_content:
                    # 記事を保存
                    date_prefix = datetime.now().strftime('%Y%m%d')
                    title = analysis['metadata'].get('title', 'Untitled')
                    title_clean = re.sub(r'[^\w\s-]', '', title)[:30].replace(' ', '_')
                    filename = f"{date_prefix}_{title_clean}_AI記事.md"
                    article_path = self.share / filename
                    
                    with open(article_path, 'w', encoding='utf-8') as f:
                        f.write(article_content)
                    
                    print(f"  ✓ Article saved: {article_path.name}")
                    
                    generated_articles.append({
                        'literature': lit_file,
                        'permanent': permanent_path,
                        'article': article_path,
                        'metadata': analysis['metadata']
                    })
                
            except Exception as e:
                self.logger.error(f"Error processing {lit_file}: {str(e)}")
                print(f"  ✗ Error: {str(e)}")
        
        # レポート生成
        self._generate_report(generated_articles)
        
        return generated_articles
    
    def _create_enhanced_permanent(self, analysis):
        """強化されたPermanentノート作成"""
        category_map = {
            'Tech': '32_Tech',
            'Philosophy': '31_Philosophy',
            'Productivity': '33_Productivity',
            'AI': '35_AI',
            'Product': '34_Product'
        }
        
        category = category_map.get(analysis.get('category', 'Tech'), '32_Tech')
        
        content = f"""# {analysis['metadata'].get('title', 'Untitled')} - 深い洞察

## 概要
{analysis['metadata'].get('summary', '')}

## 重要な洞察
"""
        
        for i, insight in enumerate(analysis.get('insights', []), 1):
            content += f"\n### {i}. {insight}\n"
        
        content += "\n## 実践への応用\n"
        
        for app in analysis.get('applications', []):
            content += f"- {app}\n"
        
        content += f"""

## 関連トピック
{', '.join(['[[' + conn + ']]' for conn in analysis['metadata'].get('connections', [])])}

---

**作成日**: {datetime.now().strftime('%Y-%m-%d')}  
**カテゴリ**: {analysis.get('category', 'Tech')}  
**タグ**: #permanent #{analysis.get('category', 'tech').lower()} #ai-enhanced
"""
        
        # ファイル保存
        title_clean = re.sub(r'[^\w\s-]', '', analysis['metadata'].get('title', 'Untitled'))[:30]
        filename = f"{title_clean}_深い洞察.md"
        file_path = self.permanent / category / filename
        file_path.parent.mkdir(exist_ok=True)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return file_path
    
    def _generate_report(self, articles):
        """処理レポート生成"""
        report_path = self.vault_path / "100_cursor" / "reports" / f"ai_generation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(f"# AI Article Generation Report\n\n")
            f.write(f"**Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"**AI Mode**: {'Enabled' if hasattr(self, 'client') else 'Disabled'}\n")
            f.write(f"**Articles Generated**: {len(articles)}\n\n")
            
            for item in articles:
                f.write(f"## {item['metadata'].get('title', 'Untitled')}\n")
                f.write(f"- Category: {item['metadata'].get('category', 'Unknown')}\n")
                f.write(f"- Summary: {item['metadata'].get('summary', 'N/A')[:100]}...\n\n")
        
        print(f"\n📊 Report: {report_path.name}")


def main():
    """メイン関数"""
    vault_path = "/Users/hashiguchimasaki/project/obsidian"
    
    # API keyの設定方法を表示
    if not os.environ.get('CLAUDE_API_KEY'):
        print("💡 Tip: Set CLAUDE_API_KEY environment variable for AI features")
        print("   export CLAUDE_API_KEY='your-api-key'")
        print("   Or install: pip install anthropic")
        print("")
    
    generator = AIArticleGenerator(vault_path)
    results = generator.process_with_ai()
    
    if results:
        print(f"\n🎉 Generated {len(results)} AI-powered articles!")
    else:
        print("\n📭 No clips to process")


if __name__ == "__main__":
    main()