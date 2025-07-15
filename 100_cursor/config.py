#!/usr/bin/env python3
"""
設定ファイル
すべてのプロセッサーで使用される共通設定
"""

import os
from pathlib import Path

# Obsidian Vaultのルートパス
VAULT_PATH = os.environ.get(
    'OBSIDIAN_VAULT_PATH',
    '/Users/hashiguchimasaki/project/obsidian'
)

# ディレクトリ構造
DIRECTORIES = {
    'inbox': '00_Inbox',
    'inbox_clip': '00_Inbox/clip',
    'inbox_ideas': '00_Inbox/Ideas',
    'literature': '20_Literature',
    'literature_books': '20_Literature/21_Books',
    'literature_articles': '20_Literature/22_Articles',
    'literature_videos': '20_Literature/23_Videos',
    'literature_sns': '20_Literature/24_SNS',
    'literature_other': '20_Literature/29_Other',
    'permanent': '30_Permanent',
    'permanent_philosophy': '30_Permanent/31_Philosophy',
    'permanent_tech': '30_Permanent/32_Tech',
    'permanent_productivity': '30_Permanent/33_Productivity',
    'permanent_product': '30_Permanent/34_Product',
    'permanent_ai': '30_Permanent/35_AI',
    'share': '70_Share',
    'share_personal': '70_Share/78_Personal',
    'index': '90_Index',
    'cursor': '100_cursor',
    'attachments': 'attachments'
}

# API設定
CLAUDE_API_KEY = os.environ.get('CLAUDE_API_KEY')
NOTION_API_KEY = os.environ.get('NOTION_API_KEY')

# タイムアウト設定（秒）
DEFAULT_TIMEOUT = 120

# 処理設定
RECENT_FILES_MINUTES = 5  # 最近のファイルとみなす時間（分）
MAX_FILENAME_LENGTH = 50  # ファイル名の最大長
REPORT_RETENTION_DAYS = 30  # レポートの保持日数

# デフォルトタグ
DEFAULT_TAGS = {
    'literature': '#literature',
    'permanent': '#permanent',
    'share': '#share/blog',
    'daily': '#daily'
}

# キーワードマッピング
INSIGHT_KEYWORDS = {
    '効率': '生産性向上の観点から重要',
    'AI': '人工知能の活用による革新',
    '自動化': 'プロセスの効率化に貢献',
    '学習': '継続的な成長の機会',
    'データ': 'データドリブンな意思決定',
    'システム': 'システム思考の適用',
    'ツール': '適切なツール選択の重要性',
    'プロセス': 'プロセス改善による価値創造',
    'イノベーション': '革新的なアプローチの必要性',
    'コラボレーション': 'チーム協働の重要性'
}

# コンテンツタイプ判定キーワード
CONTENT_TYPE_KEYWORDS = {
    '21_Books': ['book', '書籍', '本', 'isbn', '著者', 'author', '出版'],
    '22_Articles': ['article', '記事', 'blog', 'ブログ', 'news', 'post', 'qiita', 'zenn'],
    '23_Videos': ['video', 'youtube', '動画', 'vimeo', 'watch', '視聴'],
    '24_SNS': ['twitter', 'x.com', 'facebook', 'instagram', 'sns', 'social', 'tweet']
}

# カテゴリ判定キーワード
CATEGORY_KEYWORDS = {
    '32_Tech': {
        'tags': ['tech', 'technology', '技術', 'programming', 'coding'],
        'content': ['プログラ', 'コード', '開発', 'システム', 'アプリ', 'software', 'hardware']
    },
    '31_Philosophy': {
        'tags': ['philosophy', '哲学', 'thinking', '思考'],
        'content': ['哲学', '思考', '概念', 'philosophy', 'thinking', '原理', '本質']
    },
    '33_Productivity': {
        'tags': ['productivity', '生産性', 'efficiency', '効率'],
        'content': ['生産性', '効率', 'タスク', 'ワークフロー', 'productivity', 'GTD']
    },
    '35_AI': {
        'tags': ['ai', 'artificial-intelligence', '人工知能', 'machine-learning'],
        'content': ['ai', '人工知能', '機械学習', 'chatgpt', 'claude', 'llm', 'neural']
    },
    '34_Product': {
        'tags': ['product', 'プロダクト', 'サービス', 'service'],
        'content': ['プロダクト', 'サービス', 'ビジネス', 'product', 'service', 'マーケティング']
    }
}

# ログ設定
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'