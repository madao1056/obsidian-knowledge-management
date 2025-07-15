#!/usr/bin/env python3
"""
自動記事生成システム
クリップから記事まで完全自動化
"""

from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

from base_processor import BaseProcessor
from utils import (
    extract_metadata_from_content,
    extract_sections,
    clean_filename,
    determine_category,
    run_python_script,
    create_unique_filename
)
from config import VAULT_PATH, INSIGHT_KEYWORDS


class AutoArticleGenerator(BaseProcessor):
    def __init__(self, vault_path: str):
        super().__init__(vault_path, 'auto_article_generator')
    
    def process_clip_to_literature(self) -> List[Path]:
        """Step 1: ClipをLiteratureに処理"""
        self.log_info("Step 1: Processing clips to Literature")
        
        # process_clip.pyを実行
        script_path = self.cursor_dir / 'process_clip.py'
        success, stdout, stderr = run_python_script(script_path, self.vault_path)
        
        if success:
            self.log_info("Clips processed successfully")
            # 処理されたファイルのリストを取得
            return self.get_recent_files(self.literature)
        else:
            self.log_error(f"Failed to process clips: {stderr}")
            return []
    
    
    def extract_key_insights(self, file_path: Path) -> Dict[str, any]:
        """Step 2: Literatureから重要な洞察を抽出"""
        self.log_info(f"Step 2: Extracting insights from {file_path}")
        
        content = self.read_file_safe(file_path)
        if not content:
            return None
        
        # メタデータを抽出
        metadata = extract_metadata_from_content(content)
        
        # 主要ポイントを抽出
        main_points = extract_sections(content, "主要ポイント")
        
        # 活用例を抽出
        use_cases = extract_sections(content, "活用例")
        
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
    
    
    def _generate_insights(self, content: str, main_points: List[str], use_cases: List[str]) -> List[str]:
        """洞察を生成（簡易版）"""
        insights = []
        
        # キーワードベースの簡易分析
        content_lower = content.lower()
        for keyword, insight_template in INSIGHT_KEYWORDS.items():
            if keyword.lower() in content_lower:
                insights.append(f"{insight_template}が示唆される")
        
        # 主要ポイントから洞察を生成
        if len(main_points) > 3:
            insights.append("多面的なアプローチが必要な複雑なトピック")
        
        # 活用例から洞察を生成
        if use_cases:
            insights.append(f"{len(use_cases)}つの具体的な活用方法が存在")
        
        return insights[:3]  # 上位3つの洞察
    
    def create_permanent_note(self, literature_data: Dict[str, any]) -> Tuple[Optional[Path], Optional[str]]:
        """Step 3: Permanentノートを作成"""
        self.log_info("Step 3: Creating Permanent note")
        
        # カテゴリを決定
        category = determine_category(
            literature_data['original_content'],
            literature_data['metadata'].get('tags', [])
        )
        
        # Permanentノートの内容を生成
        permanent_content = self._generate_permanent_content(literature_data)
        
        # ファイル名を生成
        title_clean = clean_filename(literature_data['metadata'].get('title', 'Untitled'))
        base_filename = f"{title_clean}_洞察"
        file_path = create_unique_filename(self.permanent / category, base_filename)
        
        # ファイルを保存
        if self.write_file_safe(file_path, permanent_content):
            self.log_info(f"Permanent note created: {file_path}")
            return file_path, permanent_content
        else:
            return None, None
    
    
    def _generate_permanent_content(self, literature_data: Dict[str, any]) -> str:
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

**作成日**: {self.format_timestamp('%Y-%m-%d')}  
**タグ**: #permanent {' '.join(metadata.get('tags', []))}  
**参考文献**: [[{Path(literature_data['file_path']).stem}]]
"""
        
        return content
    
    def create_article(self, permanent_data: Dict[str, any], literature_data: Dict[str, any]) -> Optional[Path]:
        """Step 4: 記事を生成"""
        self.log_info("Step 4: Creating article")
        
        # 記事の内容を生成
        article_content = self._generate_article_content(permanent_data, literature_data)
        
        # ファイル名を生成
        date_prefix = self.format_timestamp('%Y%m%d')
        title = literature_data['metadata'].get('title', 'Untitled')
        title_clean = clean_filename(title)
        base_filename = f"{date_prefix}_{title_clean}_記事"
        file_path = create_unique_filename(self.share, base_filename)
        
        # ファイルを保存
        if self.write_file_safe(file_path, article_content):
            self.log_info(f"Article created: {file_path}")
            return file_path
        else:
            return None
    
    def _generate_article_content(self, permanent_data: Dict[str, any], literature_data: Dict[str, any]) -> str:
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

**公開日**: {self.format_timestamp('%Y-%m-%d')}  
**カテゴリ**: 学習ノート  
**タグ**: #share/blog {' '.join(metadata.get('tags', []))}  
**参考資料**: 
- [[{Path(literature_data['file_path']).stem}]]
- {metadata.get('source', '')}
"""
        
        return content
    
    def process_all_clips(self) -> List[Dict[str, any]]:
        """すべてのクリップを処理して記事まで生成"""
        self.log_info("Starting full automation process")
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
                if not literature_data:
                    continue
                
                # Step 3: Permanentノート作成
                permanent_path, permanent_content = self.create_permanent_note(literature_data)
                if not permanent_path:
                    continue
                    
                print(f"  ✓ Permanent note created: {permanent_path.name}")
                
                # Step 4: 記事生成
                article_path = self.create_article(
                    {'path': permanent_path, 'content': permanent_content},
                    literature_data
                )
                if article_path:
                    print(f"  ✓ Article created: {article_path.name}")
                    
                    generated_articles.append({
                        'literature': lit_file,
                        'permanent': permanent_path,
                        'article': article_path,
                        'metadata': literature_data['metadata']
                    })
                
            except Exception as e:
                self.log_error(f"Error processing {lit_file}", e)
                print(f"  ✗ Error: {str(e)}")
        
        # 最終レポート
        self._generate_automation_report(generated_articles)
        
        return generated_articles
    
    def _generate_automation_report(self, generated_articles: List[Dict[str, any]]) -> None:
        """自動化処理のレポートを生成"""
        report_path = self.generate_report_path("automation")
        
        content = f"""# Automation Report

**Date**: {self.format_timestamp()}
**Articles Generated**: {len(generated_articles)}

"""
        
        if generated_articles:
            content += "## Generated Articles\n\n"
            for item in generated_articles:
                content += f"""### {item['metadata'].get('title', 'Untitled')}
- Literature: `{item['literature'].name}`
- Permanent: `{item['permanent'].name}`
- Article: `{item['article'].name}`
- Source: {item['metadata'].get('source', 'Unknown')}

"""
        
        if self.write_file_safe(report_path, content):
            print(f"\n📊 Report generated: {report_path.name}")
            print(f"✅ Total articles generated: {len(generated_articles)}")


def main():
    """メイン関数"""
    vault_path = VAULT_PATH
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