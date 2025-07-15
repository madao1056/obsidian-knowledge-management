#!/usr/bin/env python3
"""
クリップ処理システム
InboxのクリップをLiteratureに整理
"""

import shutil
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any

from base_processor import BaseProcessor
from utils import (
    extract_metadata_from_content,
    clean_filename,
    detect_content_type,
    create_unique_filename
)


class ClipProcessor(BaseProcessor):
    def __init__(self, obsidian_root: str):
        super().__init__(obsidian_root, 'clip_processor')
    
    def backup_file(self, file_path: Path) -> Path:
        """操作前にファイルをバックアップ"""
        timestamp = self.format_timestamp('%Y%m%d_%H%M%S')
        backup_filename = f"{file_path.stem}_{timestamp}{file_path.suffix}"
        backup_path = self.backup_dir / backup_filename
        
        try:
            shutil.copy2(file_path, backup_path)
            self.log_info(f"Backup created: {backup_path}")
            return backup_path
        except Exception as e:
            self.log_error(f"Failed to create backup for {file_path}", e)
            raise
        
    
    def extract_metadata(self, content: str) -> Dict[str, Any]:
        """メタデータを抽出（日本語形式）"""
        # 共通関数で基本的なメタデータを抽出
        base_metadata = extract_metadata_from_content(content)
        
        # 日本語形式に変換
        metadata = {
            "タイトル": base_metadata.get('title', 'Untitled'),
            "ソース": base_metadata.get('source', ''),
            "オーナー": base_metadata.get('owner', ''),
            "日付": base_metadata.get('date', self.format_timestamp('%Y-%m-%d')),
            "タグ": base_metadata.get('tags', [])
        }
        
        # literature タグを追加
        if "#literature" not in metadata["タグ"]:
            metadata["タグ"].append("#literature")
        
        # コンテンツタイプに基づいてタグを追加
        if metadata["ソース"]:
            if "youtube.com" in metadata["ソース"] or "youtu.be" in metadata["ソース"]:
                metadata["タグ"].append("#literature/video")
            elif "twitter.com" in metadata["ソース"] or "x.com" in metadata["ソース"]:
                metadata["タグ"].append("#literature/sns")
            elif any(domain in metadata["ソース"] for domain in ["zenn.dev", "medium.com", "qiita.com"]) or "blog" in metadata["ソース"]:
                metadata["タグ"].append("#literature/article")
        
        # 重複を削除
        metadata["タグ"] = list(set(metadata["タグ"]))
        
        return metadata
    
    def generate_summary(self, content: str) -> Dict[str, Any]:
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
    
    def process_file(self, file_path: Path) -> Tuple[Optional[Path], Dict[str, Any], Dict[str, Any]]:
        """ファイルを処理して適切なフォルダに移動"""
        self.log_info(f"Processing file: {file_path}")
        
        try:
            # バックアップを作成
            self.backup_file(file_path)
            
            # ファイルを読み込み
            content = self.read_file_safe(file_path)
            if not content:
                raise ValueError(f"Failed to read file: {file_path}")
            
            # コンテンツタイプを判定
            content_type = detect_content_type(content)
            target_folder = self.literature / content_type
            
            # メタデータを抽出
            metadata = self.extract_metadata(content)
            
            # サマリーを生成
            summary = self.generate_summary(content)
            
            # 新しいファイル名を生成
            date_prefix = self.format_timestamp("%Y%m%d")
            title_clean = clean_filename(metadata["タイトル"])
            base_filename = f"{date_prefix}_{title_clean}"
            target_path = create_unique_filename(target_folder, base_filename)
            
            # ファイルの内容を更新
            updated_content = self.format_content(content, metadata, summary)
            
            # ファイルを保存
            if not self.write_file_safe(target_path, updated_content):
                raise ValueError(f"Failed to write file: {target_path}")
            
            self.log_info(f"File processed successfully: {file_path} -> {target_path}")
            
            # 元のファイルを削除
            file_path.unlink()
            
            return target_path, metadata, summary
            
        except Exception as e:
            self.log_error(f"Error processing file {file_path}", e)
            raise
    
    def format_content(self, original_content: str, metadata: Dict[str, Any], summary: Dict[str, Any]) -> str:
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
    
    def process_all_clips(self) -> List[Dict[str, Any]]:
        """clipフォルダ内のすべてのファイルを処理"""
        if not self.inbox_clip.exists():
            self.log_warning(f"Clip folder not found: {self.inbox_clip}")
            print(f"Clip folder not found: {self.inbox_clip}")
            return []
        
        clip_files = list(self.inbox_clip.glob("*.md"))
        if not clip_files:
            self.log_info("No clip files found to process")
            print("No clip files found to process")
            return []
        
        self.log_info(f"Found {len(clip_files)} files to process")
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
                self.log_error(f"Error processing {file_path}", e)
                print(f"✗ Error processing {file_path.name}: {e}")
        
        # 処理結果をレポート
        self.generate_report(processed, failed)
        
        return processed
    
    def generate_report(self, processed: List[Dict[str, Any]], failed: List[Dict[str, Any]]) -> None:
        """処理結果のレポートを生成"""
        report_path = self.generate_report_path("clip_processing")
        
        content = f"""# Clip Processing Report

**Date**: {self.format_timestamp()}
**Processed**: {len(processed)} files
**Failed**: {len(failed)} files

"""
        
        if processed:
            content += "## Successfully Processed\n\n"
            for item in processed:
                content += f"""- {Path(item['original']).name} → {Path(item['target']).parent.name}/{Path(item['target']).name}
  - Title: {item['metadata']['タイトル']}
  - Source: {item['metadata']['ソース']}

"""
        
        if failed:
            content += "## Failed to Process\n\n"
            for item in failed:
                content += f"- {Path(item['file']).name}: {item['error']}\n"
        
        if self.write_file_safe(report_path, content):
            self.log_info(f"Report generated: {report_path}")
            print(f"Report generated: {report_path}")


def main():
    """メイン関数"""
    # Obsidianのルートディレクトリを指定
    obsidian_root = "/Users/hashiguchimasaki/project/obsidian"
    
    processor = ClipProcessor(obsidian_root)
    processed_files = processor.process_all_clips()
    
    if processed_files:
        print(f"\nProcessed {len(processed_files)} files:")
        for file_info in processed_files:
            print(f"  - {file_info['metadata']['タイトル']} -> {Path(file_info['target']).parent.name}")


if __name__ == "__main__":
    main()