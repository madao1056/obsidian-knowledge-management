#!/usr/bin/env python3
import os
import re
import shutil
import logging
from datetime import datetime
from pathlib import Path
import json

class ClipProcessor:
    def __init__(self, obsidian_root):
        self.obsidian_root = Path(obsidian_root)
        self.inbox_clip = self.obsidian_root / "00_Inbox" / "clip"
        self.literature = self.obsidian_root / "20_Literature"
        self.log_dir = self.obsidian_root / "100_cursor" / "logs"
        self.backup_dir = self.obsidian_root / "100_cursor" / "backup"
        
        # ディレクトリを作成
        self.log_dir.mkdir(exist_ok=True)
        self.backup_dir.mkdir(exist_ok=True)
        
        # ロガーを設定
        self.setup_logger()
    
    def setup_logger(self):
        """ログシステムを設定"""
        log_file = self.log_dir / f"clip_processor_{datetime.now().strftime('%Y%m%d')}.log"
        
        self.logger = logging.getLogger('ClipProcessor')
        self.logger.setLevel(logging.INFO)
        
        # ファイルハンドラー
        fh = logging.FileHandler(log_file, encoding='utf-8')
        fh.setLevel(logging.INFO)
        
        # フォーマット
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        
        self.logger.addHandler(fh)
    
    def backup_file(self, file_path):
        """操作前にファイルをバックアップ"""
        backup_path = self.backup_dir / f"{file_path.stem}_{datetime.now().strftime('%Y%m%d_%H%M%S')}{file_path.suffix}"
        shutil.copy2(file_path, backup_path)
        self.logger.info(f"Backup created: {backup_path}")
        return backup_path
        
    def detect_content_type(self, content):
        """コンテンツタイプを判定"""
        content_lower = content.lower()
        
        if any(word in content_lower for word in ['book', '書籍', '本', 'isbn', '著者']):
            return "21_Books"
        elif any(word in content_lower for word in ['article', '記事', 'blog', 'ブログ', 'news']):
            return "22_Articles"
        elif any(word in content_lower for word in ['video', 'youtube', '動画', 'vimeo']):
            return "23_Videos"
        elif any(word in content_lower for word in ['twitter', 'x.com', 'facebook', 'instagram', 'sns']):
            return "24_SNS"
        else:
            return "29_Other"
    
    def extract_metadata(self, content):
        """メタデータを抽出"""
        metadata = {
            "タイトル": "",
            "ソース": "",
            "オーナー": "",
            "日付": datetime.now().strftime("%Y-%m-%d"),
            "タグ": ["#literature"]
        }
        
        # URLパターンを検索
        url_pattern = r'https?://[^\s]+'
        urls = re.findall(url_pattern, content)
        if urls:
            metadata["ソース"] = urls[0]
            
            # URLから著者情報を推測
            if "youtube.com" in urls[0] or "youtu.be" in urls[0]:
                metadata["オーナー"] = "YouTube Channel"
                metadata["タグ"].append("#literature/video")
            elif "twitter.com" in urls[0] or "x.com" in urls[0]:
                metadata["オーナー"] = "Twitter User"
                metadata["タグ"].append("#literature/sns")
            elif "medium.com" in urls[0] or "blog" in urls[0]:
                metadata["オーナー"] = "Blog Author"
                metadata["タグ"].append("#literature/article")
        
        # 最初の行をタイトルとして使用
        lines = content.split('\n')
        if lines:
            title = lines[0].strip('#').strip()
            metadata["タイトル"] = title if title else "Untitled"
        
        # 既存のタグを検索
        existing_tags = re.findall(r'#[\w/]+', content)
        metadata["タグ"].extend(existing_tags)
        
        # 重複を削除
        metadata["タグ"] = list(set(metadata["タグ"]))
        
        return metadata
    
    def generate_summary(self, content):
        """コンテンツのサマリーを生成"""
        summary = {
            "記事の概要": "",
            "主要ポイント": [],
            "活用例": [],
            "原文と引用": [],
            "疑問点・考察": []
        }
        
        # 簡易的な要約生成（実際の使用時はAI APIを使用することを推奨）
        lines = content.split('\n')
        content_lines = [line for line in lines if line.strip() and not line.startswith('#')]
        
        if content_lines:
            summary["記事の概要"] = ' '.join(content_lines[:3])[:200] + "..."
        
        # 箇条書きを抽出
        bullet_points = [line.strip('- ').strip() for line in lines if line.strip().startswith('-')]
        if bullet_points:
            summary["主要ポイント"] = bullet_points[:5]
        
        # 引用を抽出（>で始まる行）
        quotes = [line.strip('> ').strip() for line in lines if line.strip().startswith('>')]
        if quotes:
            summary["原文と引用"] = quotes[:3]
        
        return summary
    
    def process_file(self, file_path):
        """ファイルを処理して適切なフォルダに移動"""
        self.logger.info(f"Processing file: {file_path}")
        
        try:
            # バックアップを作成
            self.backup_file(file_path)
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # コンテンツタイプを判定
            content_type = self.detect_content_type(content)
            target_folder = self.literature / content_type
            
            # メタデータを抽出
            metadata = self.extract_metadata(content)
            
            # サマリーを生成
            summary = self.generate_summary(content)
            
            # 新しいファイル名を生成
            date_prefix = datetime.now().strftime("%Y%m%d")
            title_clean = re.sub(r'[^\w\s-]', '', metadata["タイトル"])[:50]
            title_clean = title_clean.replace(' ', '_')
            new_filename = f"{date_prefix}_{title_clean}.md"
            
            # 重複ファイル名の確認
            counter = 1
            original_filename = new_filename
            while (target_folder / new_filename).exists():
                name_part = original_filename.replace('.md', '')
                new_filename = f"{name_part}_{counter}.md"
                counter += 1
            
            # ファイルの内容を更新
            updated_content = self.format_content(content, metadata, summary)
            
            # ファイルを移動
            target_path = target_folder / new_filename
            with open(target_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            
            self.logger.info(f"File processed successfully: {file_path} -> {target_path}")
            
            # 元のファイルを削除
            os.remove(file_path)
            
            return target_path, metadata, summary
            
        except Exception as e:
            self.logger.error(f"Error processing file {file_path}: {str(e)}")
            raise
    
    def format_content(self, original_content, metadata, summary):
        """フォーマットされたコンテンツを生成"""
        formatted = f"""# {metadata['タイトル']}

## メタデータ
- **ソース**: {metadata['ソース']}
- **オーナー**: {metadata['オーナー']}
- **日付**: {metadata['日付']}
- **タグ**: {' '.join(metadata['タグ'])}

## 記事の概要
{summary['記事の概要']}

## 主要ポイント
"""
        for point in summary['主要ポイント']:
            formatted += f"- {point}\n"
        
        formatted += "\n## 活用例\n"
        for example in summary['活用例']:
            formatted += f"- {example}\n"
        
        formatted += "\n## 原文と引用\n"
        for quote in summary['原文と引用']:
            formatted += f"> {quote}\n"
        
        formatted += "\n## 疑問点・考察\n"
        for question in summary['疑問点・考察']:
            formatted += f"- {question}\n"
        
        formatted += f"\n---\n\n## 元のコンテンツ\n\n{original_content}"
        
        return formatted
    
    def process_all_clips(self):
        """clipフォルダ内のすべてのファイルを処理"""
        if not self.inbox_clip.exists():
            self.logger.warning(f"Clip folder not found: {self.inbox_clip}")
            print(f"Clip folder not found: {self.inbox_clip}")
            return []
        
        clip_files = list(self.inbox_clip.glob("*.md"))
        if not clip_files:
            self.logger.info("No clip files found to process")
            print("No clip files found to process")
            return []
        
        self.logger.info(f"Found {len(clip_files)} files to process")
        processed = []
        failed = []
        
        for file_path in clip_files:
            try:
                target_path, metadata, summary = self.process_file(file_path)
                processed.append({
                    "original": str(file_path),
                    "target": str(target_path),
                    "metadata": metadata,
                    "summary": summary
                })
                print(f"✓ Processed: {file_path.name} -> {target_path.parent.name}/{target_path.name}")
            except Exception as e:
                failed.append({
                    "file": str(file_path),
                    "error": str(e)
                })
                self.logger.error(f"Error processing {file_path}: {e}")
                print(f"✗ Error processing {file_path.name}: {e}")
        
        # 処理結果をレポート
        self.generate_report(processed, failed)
        
        return processed
    
    def generate_report(self, processed, failed):
        """処理結果のレポートを生成"""
        report_path = self.obsidian_root / "100_cursor" / "reports" / f"clip_processing_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        report_path.parent.mkdir(exist_ok=True)
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(f"# Clip Processing Report\n\n")
            f.write(f"**Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"**Processed**: {len(processed)} files\n")
            f.write(f"**Failed**: {len(failed)} files\n\n")
            
            if processed:
                f.write("## Successfully Processed\n\n")
                for item in processed:
                    f.write(f"- {Path(item['original']).name} → {Path(item['target']).parent.name}/{Path(item['target']).name}\n")
                    f.write(f"  - Title: {item['metadata']['タイトル']}\n")
                    f.write(f"  - Source: {item['metadata']['ソース']}\n\n")
            
            if failed:
                f.write("## Failed to Process\n\n")
                for item in failed:
                    f.write(f"- {Path(item['file']).name}: {item['error']}\n")
        
        self.logger.info(f"Report generated: {report_path}")
        print(f"Report generated: {report_path}")


if __name__ == "__main__":
    # Obsidianのルートディレクトリを指定
    obsidian_root = "/Users/hashiguchimasaki/project/obsidian"
    
    processor = ClipProcessor(obsidian_root)
    processed_files = processor.process_all_clips()
    
    if processed_files:
        print(f"\nProcessed {len(processed_files)} files:")
        for file_info in processed_files:
            print(f"  - {file_info['metadata']['タイトル']} -> {Path(file_info['target']).parent.name}")