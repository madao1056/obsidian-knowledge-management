#!/usr/bin/env python3
"""
タグ分析・整理スクリプト
Obsidian vault内のタグを分析し、使用頻度や関連性を調査します。
"""

import re
import logging
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
import json
# import matplotlib.pyplot as plt  # Optional: install with pip install matplotlib

class TagAnalyzer:
    def __init__(self, vault_path):
        self.vault_path = Path(vault_path)
        self.log_dir = self.vault_path / "100_cursor" / "logs"
        self.reports_dir = self.vault_path / "100_cursor" / "reports"
        
        # ディレクトリを作成
        self.log_dir.mkdir(exist_ok=True)
        self.reports_dir.mkdir(exist_ok=True)
        
        # ロガーを設定
        self.setup_logger()
        
    def setup_logger(self):
        """ログシステムを設定"""
        log_file = self.log_dir / f"tag_analyzer_{datetime.now().strftime('%Y%m%d')}.log"
        
        self.logger = logging.getLogger('TagAnalyzer')
        self.logger.setLevel(logging.INFO)
        
        # ファイルハンドラー
        fh = logging.FileHandler(log_file, encoding='utf-8')
        fh.setLevel(logging.INFO)
        
        # フォーマット
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        
        self.logger.addHandler(fh)
    
    def extract_tags_from_file(self, file_path):
        """ファイルからタグを抽出"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # タグパターンを検索
            tags = re.findall(r'#[\w/]+', content)
            return tags
        except Exception as e:
            self.logger.error(f"Error reading file {file_path}: {e}")
            return []
    
    def analyze_tags(self):
        """vault全体のタグを分析"""
        self.logger.info("Starting tag analysis")
        
        tag_counter = Counter()
        tag_locations = defaultdict(list)
        file_count = 0
        
        # すべてのMarkdownファイルを処理
        for file_path in self.vault_path.glob("**/*.md"):
            # .obsidianディレクトリはスキップ
            if ".obsidian" in str(file_path):
                continue
                
            file_count += 1
            tags = self.extract_tags_from_file(file_path)
            
            for tag in tags:
                tag_counter[tag] += 1
                tag_locations[tag].append(str(file_path.relative_to(self.vault_path)))
        
        self.logger.info(f"Analyzed {file_count} files")
        self.logger.info(f"Found {len(tag_counter)} unique tags")
        
        return tag_counter, tag_locations, file_count
    
    def find_unused_tags(self, tag_counter, min_usage=1):
        """使用頻度の低いタグを検出"""
        return [tag for tag, count in tag_counter.items() if count <= min_usage]
    
    def find_similar_tags(self, tag_counter):
        """類似タグを検出"""
        similar_pairs = []
        tags = list(tag_counter.keys())
        
        for i, tag1 in enumerate(tags):
            for tag2 in tags[i+1:]:
                # 類似性チェック（簡易版）
                tag1_clean = tag1.replace('#', '').replace('/', '').lower()
                tag2_clean = tag2.replace('#', '').replace('/', '').lower()
                
                if (tag1_clean in tag2_clean or tag2_clean in tag1_clean) and tag1 != tag2:
                    similar_pairs.append((tag1, tag2, tag_counter[tag1], tag_counter[tag2]))
        
        return similar_pairs
    
    def generate_tag_hierarchy(self, tag_counter):
        """タグ階層を分析"""
        hierarchy = defaultdict(list)
        
        for tag in tag_counter.keys():
            parts = tag.split('/')
            if len(parts) > 1:
                parent = '/'.join(parts[:-1])
                child = parts[-1]
                hierarchy[parent].append((child, tag_counter[tag]))
        
        return hierarchy
    
    def create_tag_report(self, tag_counter, tag_locations, file_count, similar_tags, hierarchy):
        """タグ分析レポートを生成"""
        report_path = self.reports_dir / f"tag_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write("# Tag Analysis Report\n\n")
            f.write(f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"**Files analyzed**: {file_count}\n")
            f.write(f"**Unique tags**: {len(tag_counter)}\n\n")
            
            # トップ20タグ
            f.write("## Top 20 Most Used Tags\n\n")
            for tag, count in tag_counter.most_common(20):
                f.write(f"- `{tag}`: {count} uses\n")
            
            # 未使用または低使用タグ
            unused_tags = self.find_unused_tags(tag_counter, 1)
            if unused_tags:
                f.write(f"\n## Unused Tags ({len(unused_tags)})\n\n")
                for tag in unused_tags[:10]:  # 最初の10個のみ表示
                    f.write(f"- `{tag}`\n")
            
            # 類似タグ
            if similar_tags:
                f.write(f"\n## Similar Tags ({len(similar_tags)})\n\n")
                for tag1, tag2, count1, count2 in similar_tags:
                    f.write(f"- `{tag1}` ({count1}) ↔ `{tag2}` ({count2})\n")
            
            # タグ階層
            if hierarchy:
                f.write("\n## Tag Hierarchy\n\n")
                for parent, children in hierarchy.items():
                    f.write(f"### {parent}\n")
                    for child, count in sorted(children, key=lambda x: x[1], reverse=True):
                        f.write(f"- {child}: {count}\n")
                    f.write("\n")
        
        self.logger.info(f"Report generated: {report_path}")
        return report_path
    
    def create_tag_frequency_chart(self, tag_counter):
        """タグ使用頻度のチャートを生成"""
        try:
            # matplotlibがインストールされているかチェック
            try:
                import matplotlib.pyplot as plt
            except ImportError:
                self.logger.warning("matplotlib not installed. Skipping chart generation.")
                print("📊 Chart generation skipped (matplotlib not installed)")
                return None
            
            top_tags = tag_counter.most_common(20)
            tags, counts = zip(*top_tags) if top_tags else ([], [])
            
            plt.figure(figsize=(12, 8))
            plt.barh(range(len(tags)), counts)
            plt.yticks(range(len(tags)), [tag.replace('#', '') for tag in tags])
            plt.xlabel('Usage Count')
            plt.title('Top 20 Tags by Usage Frequency')
            plt.gca().invert_yaxis()
            plt.tight_layout()
            
            chart_path = self.reports_dir / f"tag_frequency_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            plt.savefig(chart_path, dpi=300, bbox_inches='tight')
            plt.close()
            
            self.logger.info(f"Frequency chart saved: {chart_path}")
            return chart_path
        except Exception as e:
            self.logger.error(f"Error creating frequency chart: {e}")
            return None
    
    def update_tag_list_file(self, tag_counter, tag_locations):
        """タグリストファイルを更新"""
        tag_list_path = self.vault_path / "100_cursor" / "105-01_タグリスト.md"
        
        try:
            # 既存のファイルを読み込み
            with open(tag_list_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 統計セクションを更新
            stats_section = f"""
## タグ使用統計

_最終更新: {datetime.now().strftime('%Y-%m-%d')}_

### トップ10タグ
"""
            for i, (tag, count) in enumerate(tag_counter.most_common(10), 1):
                stats_section += f"{i}. {tag} ({count}回)\n"
            
            # 既存の統計セクションを置換
            pattern = r'## タグ使用統計.*?(?=##|\Z)'
            updated_content = re.sub(pattern, stats_section.strip(), content, flags=re.DOTALL)
            
            with open(tag_list_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            
            self.logger.info(f"Tag list file updated: {tag_list_path}")
            
        except Exception as e:
            self.logger.error(f"Error updating tag list file: {e}")
    
    def run_analysis(self):
        """完全なタグ分析を実行"""
        print("Starting tag analysis...")
        
        # タグを分析
        tag_counter, tag_locations, file_count = self.analyze_tags()
        
        # 類似タグを検出
        similar_tags = self.find_similar_tags(tag_counter)
        
        # 階層を分析
        hierarchy = self.generate_tag_hierarchy(tag_counter)
        
        # レポートを生成
        report_path = self.create_tag_report(tag_counter, tag_locations, file_count, similar_tags, hierarchy)
        
        # チャートを生成
        chart_path = self.create_tag_frequency_chart(tag_counter)
        
        # タグリストファイルを更新
        self.update_tag_list_file(tag_counter, tag_locations)
        
        print(f"✓ Analysis complete!")
        print(f"  - Files analyzed: {file_count}")
        print(f"  - Unique tags found: {len(tag_counter)}")
        print(f"  - Report: {report_path}")
        if chart_path:
            print(f"  - Chart: {chart_path}")
        
        return {
            'tag_counter': tag_counter,
            'similar_tags': similar_tags,
            'hierarchy': hierarchy,
            'report_path': report_path,
            'chart_path': chart_path
        }


if __name__ == "__main__":
    vault_path = "/Users/hashiguchimasaki/project/obsidian"
    analyzer = TagAnalyzer(vault_path)
    results = analyzer.run_analysis()