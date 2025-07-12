#!/usr/bin/env python3
"""
自動記事生成システム
クリップから記事まで完全自動化
"""

import os
import re
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple
import subprocess

class AutoArticleGenerator:
    def __init__(self, vault_path):
        self.vault_path = Path(vault_path)
        self.inbox_clip = self.vault_path / "00_Inbox" / "clip"
        self.literature = self.vault_path / "20_Literature"
        self.permanent = self.vault_path / "30_Permanent"
        self.share = self.vault_path / "70_Share" / "78_Personal"
        self.log_dir = self.vault_path / "100_cursor" / "logs"
        
        # ディレクトリを作成
        self.log_dir.mkdir(exist_ok=True)
        self.share.mkdir(exist_ok=True)
        
        # ロガーを設定
        self.setup_logger()
        
    def setup_logger(self):
        """ログシステムを設定"""
        log_file = self.log_dir / f"auto_article_{datetime.now().strftime('%Y%m%d')}.log"
        
        self.logger = logging.getLogger('AutoArticleGenerator')
        self.logger.setLevel(logging.INFO)
        
        # ファイルハンドラー
        fh = logging.FileHandler(log_file, encoding='utf-8')
        fh.setLevel(logging.INFO)
        
        # フォーマット
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        
        self.logger.addHandler(fh)
    
    def process_clip_to_literature(self):
        """Step 1: ClipをLiteratureに処理"""
        self.logger.info("Step 1: Processing clips to Literature")
        
        # process_clip.pyを実行
        result = subprocess.run(
            ['python3', str(self.vault_path / '100_cursor' / 'process_clip.py')],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            self.logger.info("Clips processed successfully")
            # 処理されたファイルのリストを取得
            return self._get_recent_literature_files()
        else:
            self.logger.error(f"Failed to process clips: {result.stderr}")
            return []
    
    def _get_recent_literature_files(self, minutes=5):
        """最近作成されたLiteratureファイルを取得"""
        recent_files = []
        cutoff_time = datetime.now().timestamp() - (minutes * 60)
        
        for file_path in self.literature.glob("**/*.md"):
            if file_path.stat().st_mtime > cutoff_time:
                recent_files.append(file_path)
        
        return recent_files
    
    def extract_key_insights(self, file_path):
        """Step 2: Literatureから重要な洞察を抽出"""
        self.logger.info(f"Step 2: Extracting insights from {file_path}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # メタデータを抽出
        metadata = self._extract_metadata_from_content(content)
        
        # 主要ポイントを抽出
        main_points = self._extract_main_points(content)
        
        # 活用例を抽出
        use_cases = self._extract_use_cases(content)
        
        # 洞察を生成（実際の実装ではAI APIを使用推奨）
        insights = self._generate_insights(content, main_points, use_cases)
        
        return {
            'file_path': file_path,
            'metadata': metadata,
            'main_points': main_points,
            'use_cases': use_cases,
            'insights': insights,
            'original_content': content
        }
    
    def _extract_metadata_from_content(self, content):
        """コンテンツからメタデータを抽出"""
        metadata = {}
        
        # 処理済みのLiteratureファイルの場合、メタデータセクションから抽出
        # タイトルを抽出
        title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
        if title_match:
            metadata['title'] = title_match.group(1)
        
        # ソースを抽出
        source_match = re.search(r'- \*\*ソース\*\*: (.+)$', content, re.MULTILINE)
        if source_match:
            metadata['source'] = source_match.group(1)
        
        # オーナーを抽出
        owner_match = re.search(r'- \*\*オーナー\*\*: (.+)$', content, re.MULTILINE)
        if owner_match:
            metadata['owner'] = owner_match.group(1)
        
        # 日付を抽出
        date_match = re.search(r'- \*\*日付\*\*: (.+)$', content, re.MULTILINE)
        if date_match:
            metadata['date'] = date_match.group(1)
        
        # タグを抽出
        tags = re.findall(r'#[\w/]+', content)
        metadata['tags'] = list(set(tags))
        
        # 記事の概要を抽出
        summary_match = re.search(r'## 記事の概要\n(.+?)(?=\n##|\Z)', content, re.DOTALL)
        if summary_match:
            metadata['summary'] = summary_match.group(1).strip()
        
        return metadata
    
    def _extract_main_points(self, content):
        """主要ポイントを抽出"""
        points = []
        
        # 主要ポイントセクションを探す
        section_match = re.search(r'## 主要ポイント\n(.*?)(?=##|\Z)', content, re.DOTALL)
        if section_match:
            section_content = section_match.group(1)
            # 箇条書きを抽出
            points = re.findall(r'^- (.+)$', section_content, re.MULTILINE)
        
        return points
    
    def _extract_use_cases(self, content):
        """活用例を抽出"""
        use_cases = []
        
        # 活用例セクションを探す
        section_match = re.search(r'## 活用例\n(.*?)(?=##|\Z)', content, re.DOTALL)
        if section_match:
            section_content = section_match.group(1)
            # 箇条書きを抽出
            use_cases = re.findall(r'^- (.+)$', section_content, re.MULTILINE)
        
        return use_cases
    
    def _generate_insights(self, content, main_points, use_cases):
        """洞察を生成（簡易版）"""
        insights = []
        
        # キーワードベースの簡易分析
        keywords = {
            '効率': '生産性向上の観点から重要',
            'AI': '人工知能の活用による革新',
            '自動化': 'プロセスの効率化に貢献',
            '学習': '継続的な成長の機会',
            'データ': 'データドリブンな意思決定',
            'システム': 'システム思考の適用',
            'ツール': '適切なツール選択の重要性'
        }
        
        content_lower = content.lower()
        for keyword, insight_template in keywords.items():
            if keyword.lower() in content_lower:
                insights.append(f"{insight_template}が示唆される")
        
        # 主要ポイントから洞察を生成
        if len(main_points) > 3:
            insights.append("多面的なアプローチが必要な複雑なトピック")
        
        # 活用例から洞察を生成
        if use_cases:
            insights.append(f"{len(use_cases)}つの具体的な活用方法が存在")
        
        return insights[:3]  # 上位3つの洞察
    
    def create_permanent_note(self, literature_data):
        """Step 3: Permanentノートを作成"""
        self.logger.info("Step 3: Creating Permanent note")
        
        # カテゴリを決定
        category = self._determine_category(literature_data)
        
        # Permanentノートの内容を生成
        permanent_content = self._generate_permanent_content(literature_data)
        
        # ファイル名を生成
        title_clean = re.sub(r'[^\w\s-]', '', literature_data['metadata'].get('title', 'Untitled'))[:30]
        filename = f"{title_clean}_洞察.md"
        file_path = self.permanent / category / filename
        
        # ディレクトリを作成
        file_path.parent.mkdir(exist_ok=True)
        
        # ファイルを保存
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(permanent_content)
        
        self.logger.info(f"Permanent note created: {file_path}")
        
        return file_path, permanent_content
    
    def _determine_category(self, literature_data):
        """カテゴリを自動判定"""
        content = literature_data['original_content'].lower()
        tags = literature_data['metadata'].get('tags', [])
        
        # タグベースの判定
        if any('tech' in tag for tag in tags):
            return '32_Tech'
        elif any('philosophy' in tag or '哲学' in tag for tag in tags):
            return '31_Philosophy'
        elif any('productivity' in tag or '生産性' in tag for tag in tags):
            return '33_Productivity'
        elif any('ai' in tag for tag in tags):
            return '35_AI'
        elif any('product' in tag for tag in tags):
            return '34_Product'
        
        # キーワードベースの判定
        if 'プログラ' in content or 'コード' in content or '開発' in content:
            return '32_Tech'
        elif '生産性' in content or '効率' in content:
            return '33_Productivity'
        elif 'ai' in content or '人工知能' in content:
            return '35_AI'
        else:
            return '32_Tech'  # デフォルト
    
    def _generate_permanent_content(self, literature_data):
        """Permanentノートの内容を生成"""
        metadata = literature_data['metadata']
        insights = literature_data['insights']
        main_points = literature_data['main_points']
        
        content = f"""# {metadata.get('title', 'Untitled')}の洞察

## 概要
{metadata.get('title', '')}から得られた知識を自分の言葉で再構築したノート。

## 核心概念

### 主要な洞察
"""
        
        for insight in insights:
            content += f"- {insight}\n"
        
        content += """

### 実践への応用
"""
        
        for i, point in enumerate(main_points[:3], 1):
            content += f"{i}. {point}\n"
        
        content += f"""

## 関連する概念
- [[{metadata.get('title', 'Original')}]] - 元のLiteratureノート

## 今後の展開
この洞察を基に、実践的なアプローチを検討し、具体的な行動計画を立てる。

---

**作成日**: {datetime.now().strftime('%Y-%m-%d')}  
**タグ**: #permanent {' '.join(metadata.get('tags', []))}  
**参考文献**: [[{Path(literature_data['file_path']).stem}]]
"""
        
        return content
    
    def create_article(self, permanent_data, literature_data):
        """Step 4: 記事を生成"""
        self.logger.info("Step 4: Creating article")
        
        # 記事の内容を生成
        article_content = self._generate_article_content(permanent_data, literature_data)
        
        # ファイル名を生成
        date_prefix = datetime.now().strftime('%Y%m%d')
        title = literature_data['metadata'].get('title', 'Untitled')
        title_clean = re.sub(r'[^\w\s-]', '', title)[:30]
        filename = f"{date_prefix}_{title_clean}_記事.md"
        file_path = self.share / filename
        
        # ファイルを保存
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(article_content)
        
        self.logger.info(f"Article created: {file_path}")
        
        return file_path
    
    def _generate_article_content(self, permanent_data, literature_data):
        """記事の内容を生成"""
        metadata = literature_data['metadata']
        insights = literature_data['insights']
        main_points = literature_data['main_points']
        use_cases = literature_data['use_cases']
        
        # 記事タイトル
        title = f"{metadata.get('title', 'タイトル')}から学ぶ実践的な知見"
        
        content = f"""# {title}

## はじめに

最近、{metadata.get('title', 'ある記事')}を読んで、いくつかの重要な気づきを得ました。
この記事では、その内容を整理し、実践的な観点から考察してみたいと思います。

## 記事の概要

元の記事では、以下のような点が議論されていました：

"""
        
        # 主要ポイントを記載
        for point in main_points[:3]:
            content += f"- {point}\n"
        
        content += """

## 重要な洞察

### 1. 実践的な視点

"""
        
        if insights:
            content += f"{insights[0]}ことが、この記事から読み取れます。"
        
        content += """

### 2. 応用の可能性

以下のような場面で活用できると考えられます：

"""
        
        for use_case in use_cases[:3]:
            content += f"- {use_case}\n"
        
        content += """

## 筆者の感想

個人的に最も印象的だったのは、"""
        
        if main_points:
            content += f"「{main_points[0]}」という点です。"
        
        content += """
これは日常の業務やプロジェクトにおいても、重要な示唆を与えてくれます。

## 記事のポイント

1. **知識の体系化**: 断片的な情報を構造化することの重要性
2. **実践への応用**: 理論を具体的な行動に落とし込む方法
3. **継続的な学習**: 新しい知識を既存の知識と結びつける

## まとめ

"""
        
        content += f"""{metadata.get('title', 'この記事')}から得られた知見は、単なる情報以上の価値があります。
重要なのは、これらの知識をどのように自分の文脈で活用するかということです。

今後も継続的に学習を続け、実践的な知識として昇華させていきたいと思います。

---

**公開日**: {datetime.now().strftime('%Y-%m-%d')}  
**カテゴリ**: 学習ノート  
**タグ**: #share/blog {' '.join(metadata.get('tags', []))}  
**参考資料**: 
- [[{Path(literature_data['file_path']).stem}]]
- {metadata.get('source', '')}
"""
        
        return content
    
    def process_all_clips(self):
        """すべてのクリップを処理して記事まで生成"""
        self.logger.info("Starting full automation process")
        print("🚀 Starting full automation: Clip → Literature → Permanent → Article")
        
        # Step 1: ClipをLiteratureに処理
        literature_files = self.process_clip_to_literature()
        
        if not literature_files:
            print("No clips to process or processing failed")
            return []
        
        generated_articles = []
        
        for lit_file in literature_files:
            try:
                print(f"\n📄 Processing: {lit_file.name}")
                
                # Step 2: 洞察を抽出
                literature_data = self.extract_key_insights(lit_file)
                
                # Step 3: Permanentノート作成
                permanent_path, permanent_content = self.create_permanent_note(literature_data)
                print(f"  ✓ Permanent note created: {permanent_path.name}")
                
                # Step 4: 記事生成
                article_path = self.create_article(
                    {'path': permanent_path, 'content': permanent_content},
                    literature_data
                )
                print(f"  ✓ Article created: {article_path.name}")
                
                generated_articles.append({
                    'literature': lit_file,
                    'permanent': permanent_path,
                    'article': article_path,
                    'metadata': literature_data['metadata']
                })
                
            except Exception as e:
                self.logger.error(f"Error processing {lit_file}: {str(e)}")
                print(f"  ✗ Error: {str(e)}")
        
        # 最終レポート
        self._generate_automation_report(generated_articles)
        
        return generated_articles
    
    def _generate_automation_report(self, generated_articles):
        """自動化処理のレポートを生成"""
        report_path = self.vault_path / "100_cursor" / "reports" / f"automation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        report_path.parent.mkdir(exist_ok=True)
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(f"# Automation Report\n\n")
            f.write(f"**Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"**Articles Generated**: {len(generated_articles)}\n\n")
            
            if generated_articles:
                f.write("## Generated Articles\n\n")
                for item in generated_articles:
                    f.write(f"### {item['metadata'].get('title', 'Untitled')}\n")
                    f.write(f"- Literature: `{item['literature'].name}`\n")
                    f.write(f"- Permanent: `{item['permanent'].name}`\n")
                    f.write(f"- Article: `{item['article'].name}`\n")
                    f.write(f"- Source: {item['metadata'].get('source', 'Unknown')}\n\n")
        
        print(f"\n📊 Report generated: {report_path.name}")
        print(f"✅ Total articles generated: {len(generated_articles)}")


def main():
    """メイン関数"""
    vault_path = "/Users/hashiguchimasaki/project/obsidian"
    generator = AutoArticleGenerator(vault_path)
    
    # すべてのクリップを処理
    results = generator.process_all_clips()
    
    if results:
        print("\n🎉 Automation complete!")
        print(f"Generated {len(results)} articles from clips")
    else:
        print("\n📭 No clips found to process")


if __name__ == "__main__":
    main()