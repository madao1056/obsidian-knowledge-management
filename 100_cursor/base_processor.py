#!/usr/bin/env python3
"""
共通基底クラス
すべてのプロセッサーが継承する基本クラス
"""

import logging
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, Any


class BaseProcessor:
    """すべてのプロセッサーの基底クラス"""
    
    def __init__(self, vault_path: str, processor_name: str):
        """
        Args:
            vault_path: Obsidian vaultのパス
            processor_name: プロセッサーの名前（ログファイル名に使用）
        """
        self.vault_path = Path(vault_path)
        self.processor_name = processor_name
        
        # 共通ディレクトリ
        self.inbox_path = self.vault_path / "00_Inbox"
        self.inbox_clip = self.inbox_path / "clip"
        self.literature = self.vault_path / "20_Literature"
        self.permanent = self.vault_path / "30_Permanent"
        self.share = self.vault_path / "70_Share" / "78_Personal"
        self.cursor_dir = self.vault_path / "100_cursor"
        self.log_dir = self.cursor_dir / "logs"
        self.reports_dir = self.cursor_dir / "reports"
        self.backup_dir = self.cursor_dir / "backup"
        self.templates_dir = self.cursor_dir / "templates"
        
        # 必要なディレクトリを作成
        self._create_directories()
        
        # ロガーを設定
        self.logger = self._setup_logger()
    
    def _create_directories(self) -> None:
        """必要なディレクトリを作成"""
        directories = [
            self.log_dir,
            self.reports_dir,
            self.backup_dir,
            self.templates_dir,
            self.share
        ]
        
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
    
    def _setup_logger(self) -> logging.Logger:
        """ログシステムを設定"""
        log_file = self.log_dir / f"{self.processor_name}_{datetime.now().strftime('%Y%m%d')}.log"
        
        logger = logging.getLogger(self.processor_name)
        logger.setLevel(logging.INFO)
        
        # 既存のハンドラーをクリア（重複防止）
        logger.handlers.clear()
        
        # ファイルハンドラー
        fh = logging.FileHandler(log_file, encoding='utf-8')
        fh.setLevel(logging.INFO)
        
        # フォーマット
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        fh.setFormatter(formatter)
        
        logger.addHandler(fh)
        
        return logger
    
    def log_info(self, message: str) -> None:
        """情報レベルのログを記録"""
        self.logger.info(message)
    
    def log_error(self, message: str, error: Optional[Exception] = None) -> None:
        """エラーレベルのログを記録"""
        if error:
            self.logger.error(f"{message}: {str(error)}")
        else:
            self.logger.error(message)
    
    def log_warning(self, message: str) -> None:
        """警告レベルのログを記録"""
        self.logger.warning(message)
    
    def generate_report_path(self, report_name: str) -> Path:
        """レポートファイルのパスを生成"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        return self.reports_dir / f"{report_name}_{timestamp}.md"
    
    def get_recent_files(self, directory: Path, minutes: int = 5, pattern: str = "**/*.md") -> list[Path]:
        """最近作成/更新されたファイルを取得
        
        Args:
            directory: 検索対象ディレクトリ
            minutes: 何分以内のファイルを対象とするか
            pattern: ファイルパターン（glob形式）
        
        Returns:
            最近のファイルのリスト
        """
        recent_files = []
        cutoff_time = datetime.now().timestamp() - (minutes * 60)
        
        for file_path in directory.glob(pattern):
            if file_path.stat().st_mtime > cutoff_time:
                recent_files.append(file_path)
        
        return recent_files
    
    def read_file_safe(self, file_path: Path) -> Optional[str]:
        """ファイルを安全に読み込む
        
        Args:
            file_path: 読み込むファイルのパス
        
        Returns:
            ファイルの内容、エラーの場合はNone
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            self.log_error(f"Failed to read file {file_path}", e)
            return None
    
    def write_file_safe(self, file_path: Path, content: str) -> bool:
        """ファイルを安全に書き込む
        
        Args:
            file_path: 書き込むファイルのパス
            content: 書き込む内容
        
        Returns:
            成功した場合True、失敗した場合False
        """
        try:
            file_path.parent.mkdir(parents=True, exist_ok=True)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        except Exception as e:
            self.log_error(f"Failed to write file {file_path}", e)
            return False
    
    def format_timestamp(self, format_string: str = '%Y-%m-%d %H:%M:%S') -> str:
        """現在のタイムスタンプをフォーマット"""
        return datetime.now().strftime(format_string)