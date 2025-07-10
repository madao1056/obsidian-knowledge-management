#!/usr/bin/env python3
"""
リンクチェッカー
Obsidian vault内の内部リンクの整合性をチェックします。
"""

import re
import logging
from datetime import datetime
from pathlib import Path
from collections import defaultdict

class LinkChecker:
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
        log_file = self.log_dir / f"link_checker_{datetime.now().strftime('%Y%m%d')}.log"
        
        self.logger = logging.getLogger('LinkChecker')
        self.logger.setLevel(logging.INFO)
        
        # ファイルハンドラー
        fh = logging.FileHandler(log_file, encoding='utf-8')
        fh.setLevel(logging.INFO)
        
        # フォーマット
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        
        self.logger.addHandler(fh)
    
    def get_all_files(self):
        """vault内のすべてのMarkdownファイルを取得"""
        files = {}
        for file_path in self.vault_path.glob("**/*.md"):
            if ".obsidian" in str(file_path):
                continue
            
            # ファイル名（拡張子なし）をキーとして保存
            stem = file_path.stem
            relative_path = file_path.relative_to(self.vault_path)
            files[stem] = {
                'path': file_path,
                'relative_path': relative_path
            }
        
        return files
    
    def extract_links_from_file(self, file_path):
        """ファイルから内部リンクを抽出"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # [[リンク]]形式のリンクを抽出
            wiki_links = re.findall(r'\[\[([^\]]+)\]\]', content)
            
            # [テキスト](リンク)形式でローカルファイルを抽出
            md_links = []
            for match in re.finditer(r'\[([^\]]+)\]\(([^)]+)\)', content):
                link_url = match.group(2)
                # ローカルファイルのみ（http://やhttps://で始まらない）
                if not link_url.startswith(('http://', 'https://', 'mailto:')):
                    md_links.append(link_url)
            
            return wiki_links, md_links
            
        except Exception as e:
            self.logger.error(f"Error reading file {file_path}: {e}")
            return [], []
    
    def normalize_link(self, link):
        """リンクを正規化"""
        # エイリアス部分を削除（|の後）
        if '|' in link:
            link = link.split('|')[0]
        
        # #アンカー部分を削除
        if '#' in link:
            link = link.split('#')[0]
        
        # .md拡張子を削除
        if link.endswith('.md'):
            link = link[:-3]
        
        return link.strip()
    
    def check_links(self):
        """すべてのリンクをチェック"""
        self.logger.info("Starting link check")
        
        all_files = self.get_all_files()
        broken_links = []
        working_links = []
        file_count = 0
        
        print(f"Checking links in {len(all_files)} files...")
        
        for file_info in all_files.values():
            file_path = file_info['path']
            file_count += 1
            
            wiki_links, md_links = self.extract_links_from_file(file_path)
            
            # Wikiリンクをチェック
            for link in wiki_links:
                normalized_link = self.normalize_link(link)
                
                if normalized_link and normalized_link not in all_files:
                    broken_links.append({
                        'file': file_info['relative_path'],
                        'link': link,
                        'normalized': normalized_link,
                        'type': 'wiki'
                    })
                elif normalized_link:
                    working_links.append({
                        'file': file_info['relative_path'],
                        'link': link,
                        'target': all_files[normalized_link]['relative_path'],
                        'type': 'wiki'
                    })
            
            # Markdownリンクをチェック
            for link in md_links:
                # 相対パスを解決
                target_path = (file_path.parent / link).resolve()
                
                if not target_path.exists():
                    broken_links.append({
                        'file': file_info['relative_path'],
                        'link': link,
                        'type': 'markdown'
                    })
                else:
                    try:
                        relative_target = target_path.relative_to(self.vault_path)
                        working_links.append({
                            'file': file_info['relative_path'],
                            'link': link,
                            'target': relative_target,
                            'type': 'markdown'
                        })
                    except ValueError:
                        # vault外のファイル
                        broken_links.append({
                            'file': file_info['relative_path'],
                            'link': link,
                            'type': 'external'
                        })
        
        self.logger.info(f"Link check complete: {len(working_links)} working, {len(broken_links)} broken")
        
        return broken_links, working_links, file_count
    
    def generate_report(self, broken_links, working_links, file_count):
        """リンクチェックレポートを生成"""
        report_path = self.reports_dir / f"link_check_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write("# Link Check Report\n\n")
            f.write(f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"**Files checked**: {file_count}\n")
            f.write(f"**Working links**: {len(working_links)}\n")
            f.write(f"**Broken links**: {len(broken_links)}\n\n")
            
            if broken_links:
                f.write("## Broken Links\n\n")
                
                # ファイル別にグループ化
                by_file = defaultdict(list)
                for link in broken_links:
                    by_file[str(link['file'])].append(link)
                
                for file_path, links in sorted(by_file.items()):
                    f.write(f"### {file_path}\n\n")
                    for link in links:
                        f.write(f"- `{link['link']}` ({link['type']})\n")
                        if 'normalized' in link:
                            f.write(f"  - Normalized: `{link['normalized']}`\n")
                    f.write("\n")
            else:
                f.write("## ✅ No Broken Links Found\n\n")
                f.write("All internal links are working correctly!\n\n")
            
            if working_links:
                f.write("## Working Links Summary\n\n")
                wiki_count = len([l for l in working_links if l['type'] == 'wiki'])
                md_count = len([l for l in working_links if l['type'] == 'markdown'])
                
                f.write(f"- Wiki links (`[[]]`): {wiki_count}\n")
                f.write(f"- Markdown links (`[]()`): {md_count}\n")
        
        self.logger.info(f"Report generated: {report_path}")
        return report_path
    
    def suggest_fixes(self, broken_links, all_files):
        """壊れたリンクの修正案を提案"""
        suggestions = []
        
        for broken_link in broken_links:
            if broken_link['type'] == 'wiki' and 'normalized' in broken_link:
                # 類似ファイル名を検索
                target = broken_link['normalized'].lower()
                matches = []
                
                for file_name in all_files.keys():
                    if target in file_name.lower() or file_name.lower() in target:
                        matches.append(file_name)
                
                if matches:
                    suggestions.append({
                        'broken': broken_link,
                        'suggestions': matches[:3]  # 上位3つ
                    })
        
        return suggestions
    
    def run_check(self):
        """完全なリンクチェックを実行"""
        print("Starting link check...")
        
        # すべてのファイルを取得
        all_files = self.get_all_files()
        
        # リンクをチェック
        broken_links, working_links, file_count = self.check_links()
        
        # レポートを生成
        report_path = self.generate_report(broken_links, working_links, file_count)
        
        # 修正案を生成
        suggestions = self.suggest_fixes(broken_links, all_files)
        
        print(f"✓ Link check complete!")
        print(f"  - Files checked: {file_count}")
        print(f"  - Working links: {len(working_links)}")
        print(f"  - Broken links: {len(broken_links)}")
        print(f"  - Report: {report_path}")
        
        if broken_links:
            print(f"\n⚠️  Found {len(broken_links)} broken links:")
            for link in broken_links[:5]:  # 最初の5つを表示
                print(f"   - {link['file']}: {link['link']}")
            if len(broken_links) > 5:
                print(f"   ... and {len(broken_links) - 5} more")
        
        if suggestions:
            print(f"\n💡 Suggested fixes for {len(suggestions)} links:")
            for suggestion in suggestions[:3]:
                print(f"   - '{suggestion['broken']['link']}' → {suggestion['suggestions']}")
        
        return {
            'broken_links': broken_links,
            'working_links': working_links,
            'suggestions': suggestions,
            'report_path': report_path
        }


if __name__ == "__main__":
    vault_path = "/Users/hashiguchimasaki/project/obsidian"
    checker = LinkChecker(vault_path)
    results = checker.run_check()
    
    # 終了コード（CIで使用）
    exit_code = 0 if not results['broken_links'] else 1
    exit(exit_code)