#!/usr/bin/env python3
"""
共通ユーティリティ関数
すべてのプロセッサーで使用される共通関数
"""

import re
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any
import subprocess
import sys

from config import (
    CONTENT_TYPE_KEYWORDS,
    CATEGORY_KEYWORDS,
    MAX_FILENAME_LENGTH
)


def extract_metadata_from_content(content: str) -> Dict[str, Any]:
    """コンテンツからメタデータを抽出
    
    Args:
        content: Markdownコンテンツ
    
    Returns:
        抽出されたメタデータの辞書
    """
    metadata = {
        "title": "",
        "source": "",
        "owner": "",
        "date": "",
        "tags": [],
        "summary": ""
    }
    
    # YAMLフロントマターをチェック
    yaml_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if yaml_match:
        yaml_content = yaml_match.group(1)
        
        # タイトルを抽出
        title_match = re.search(r'title:\s*"([^"]+)"', yaml_content)
        if title_match:
            metadata["title"] = title_match.group(1)
        
        # ソースを抽出
        source_match = re.search(r'source:\s*"([^"]+)"', yaml_content)
        if source_match:
            metadata["source"] = source_match.group(1)
        
        # 著者を抽出
        author_match = re.search(r'author:\s*\n\s*-\s*"([^"]+)"', yaml_content)
        if author_match:
            metadata["owner"] = author_match.group(1).replace('[[', '').replace(']]', '')
        
        # タグを抽出
        tags_match = re.search(r'tags:\s*\n((?:\s*-\s*"[^"]+"\s*\n)+)', yaml_content)
        if tags_match:
            tag_lines = tags_match.group(1)
            yaml_tags = re.findall(r'-\s*"([^"]+)"', tag_lines)
            metadata["tags"].extend([f"#{tag}" if not tag.startswith('#') else tag for tag in yaml_tags])
        
        # コンテンツ本文を更新
        content = content[yaml_match.end():]
    
    # Markdownからメタデータを抽出（フォールバック）
    # タイトル
    if not metadata["title"]:
        title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
        if title_match:
            metadata["title"] = title_match.group(1).strip()
    
    # ソース
    if not metadata["source"]:
        source_match = re.search(r'- \*\*ソース\*\*: (.+)$', content, re.MULTILINE)
        if source_match:
            metadata["source"] = source_match.group(1)
        else:
            # URLパターンを検索
            urls = re.findall(r'https?://[^\s]+', content)
            if urls:
                metadata["source"] = urls[0]
    
    # オーナー
    if not metadata["owner"]:
        owner_match = re.search(r'- \*\*オーナー\*\*: (.+)$', content, re.MULTILINE)
        if owner_match:
            metadata["owner"] = owner_match.group(1)
    
    # 日付
    date_match = re.search(r'- \*\*日付\*\*: (.+)$', content, re.MULTILINE)
    if date_match:
        metadata["date"] = date_match.group(1)
    
    # 既存のタグを検索
    existing_tags = re.findall(r'#[\w/]+', content)
    metadata["tags"].extend(existing_tags)
    
    # 重複を削除
    metadata["tags"] = list(set(metadata["tags"]))
    
    # 記事の概要
    summary_match = re.search(r'## 記事の概要\n(.+?)(?=\n##|\Z)', content, re.DOTALL)
    if summary_match:
        metadata["summary"] = summary_match.group(1).strip()
    
    # デフォルト値を設定
    if not metadata["title"]:
        metadata["title"] = "Untitled"
    
    return metadata


def extract_sections(content: str, section_name: str) -> List[str]:
    """特定のセクションから箇条書きを抽出
    
    Args:
        content: Markdownコンテンツ
        section_name: セクション名（例: "主要ポイント"）
    
    Returns:
        箇条書きのリスト
    """
    section_pattern = rf'## {re.escape(section_name)}\n(.*?)(?=##|\Z)'
    section_match = re.search(section_pattern, content, re.DOTALL)
    
    if section_match:
        section_content = section_match.group(1)
        # 箇条書きを抽出
        return re.findall(r'^- (.+)$', section_content, re.MULTILINE)
    
    return []


def clean_filename(title: str, max_length: int = MAX_FILENAME_LENGTH) -> str:
    """ファイル名として使える形式にタイトルをクリーニング
    
    Args:
        title: 元のタイトル
        max_length: 最大文字数
    
    Returns:
        クリーンなファイル名
    """
    # 特殊文字を削除
    clean = re.sub(r'[^\w\s-]', '', title)
    # スペースをアンダースコアに置換
    clean = clean.replace(' ', '_')
    # 長さを制限
    clean = clean[:max_length]
    # 前後の空白文字を削除
    clean = clean.strip('_')
    
    return clean if clean else "untitled"


def determine_category(content: str, tags: List[str]) -> str:
    """コンテンツのカテゴリを判定
    
    Args:
        content: コンテンツ本文
        tags: タグのリスト
    
    Returns:
        カテゴリディレクトリ名
    """
    content_lower = content.lower()
    
    # タグベースの判定
    for category, config in CATEGORY_KEYWORDS.items():
        tag_keywords = config.get('tags', [])
        if any(keyword in tag.lower() for tag in tags for keyword in tag_keywords):
            return category
    
    # コンテンツベースの判定
    for category, config in CATEGORY_KEYWORDS.items():
        content_keywords = config.get('content', [])
        if any(keyword in content_lower for keyword in content_keywords):
            return category
    
    # デフォルト
    return '32_Tech'


def detect_content_type(content: str) -> str:
    """コンテンツタイプを判定（Literature用）
    
    Args:
        content: コンテンツ本文
    
    Returns:
        コンテンツタイプディレクトリ名
    """
    content_lower = content.lower()
    
    for content_type, keywords in CONTENT_TYPE_KEYWORDS.items():
        if any(keyword in content_lower for keyword in keywords):
            return content_type
    
    return "29_Other"


def run_python_script(script_path: Path, cwd: Optional[Path] = None) -> Tuple[bool, str, str]:
    """Pythonスクリプトを実行
    
    Args:
        script_path: 実行するスクリプトのパス
        cwd: 作業ディレクトリ（省略時はスクリプトの親ディレクトリ）
    
    Returns:
        (成功フラグ, 標準出力, 標準エラー出力)
    """
    if cwd is None:
        cwd = script_path.parent
    
    try:
        result = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=True,
            text=True,
            cwd=str(cwd)
        )
        
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)


def extract_tags_from_content(content: str) -> List[str]:
    """コンテンツからタグを抽出
    
    Args:
        content: Markdownコンテンツ
    
    Returns:
        タグのリスト（重複なし）
    """
    # #で始まるタグを抽出
    tags = re.findall(r'#[\w/]+', content)
    
    # YAMLフロントマターからもタグを抽出
    yaml_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if yaml_match:
        yaml_content = yaml_match.group(1)
        tags_match = re.search(r'tags:\s*\n((?:\s*-\s*"[^"]+"\s*\n)+)', yaml_content)
        if tags_match:
            tag_lines = tags_match.group(1)
            yaml_tags = re.findall(r'-\s*"([^"]+)"', tag_lines)
            for tag in yaml_tags:
                if not tag.startswith('#'):
                    tag = '#' + tag
                tags.append(tag)
    
    # 重複を削除
    return list(set(tags))


def create_unique_filename(directory: Path, base_name: str, extension: str = ".md") -> Path:
    """重複しないファイル名を生成
    
    Args:
        directory: 保存先ディレクトリ
        base_name: 基本ファイル名
        extension: ファイル拡張子
    
    Returns:
        重複しないファイルパス
    """
    counter = 1
    file_path = directory / f"{base_name}{extension}"
    
    while file_path.exists():
        file_path = directory / f"{base_name}_{counter}{extension}"
        counter += 1
    
    return file_path