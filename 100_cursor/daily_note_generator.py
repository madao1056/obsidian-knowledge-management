#!/usr/bin/env python3
"""
Daily Note自動生成スクリプト
毎日のDaily Noteを自動生成します。
"""

import logging
from datetime import datetime, timedelta
from pathlib import Path

class DailyNoteGenerator:
    def __init__(self, vault_path):
        self.vault_path = Path(vault_path)
        self.inbox_path = self.vault_path / "00_Inbox"
        self.templates_path = self.vault_path / "100_cursor" / "templates"
        self.log_dir = self.vault_path / "100_cursor" / "logs"
        
        # ディレクトリを作成
        self.log_dir.mkdir(exist_ok=True)
        self.templates_path.mkdir(exist_ok=True)
        
        # ロガーを設定
        self.setup_logger()
        
    def setup_logger(self):
        """ログシステムを設定"""
        log_file = self.log_dir / f"daily_note_generator_{datetime.now().strftime('%Y%m%d')}.log"
        
        self.logger = logging.getLogger('DailyNoteGenerator')
        self.logger.setLevel(logging.INFO)
        
        # ファイルハンドラー
        fh = logging.FileHandler(log_file, encoding='utf-8')
        fh.setLevel(logging.INFO)
        
        # フォーマット
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        
        self.logger.addHandler(fh)
    
    def get_daily_note_template(self):
        """Daily Noteテンプレートを取得"""
        template_path = self.templates_path / "daily_note_template.md"
        
        # デフォルトテンプレート
        default_template = """# {{date}}

## 今日の目標
- [ ] 

## タスク

### 🔥 緊急かつ重要
- [ ] 

### ⭐ 重要だが緊急ではない
- [ ] 

### ⚡ 緊急だが重要ではない
- [ ] 

### 📝 その他
- [ ] 

## Inbox処理
- [ ] clipフォルダ確認
- [ ] 未処理アイテム整理

## 学び・インサイト
- 

## 振り返り
### よかったこと
- 

### 改善点
- 

### 明日への申し送り
- 

## リンク
- [[{{yesterday}}|昨日]] / [[{{tomorrow}}|明日]]

---

**作成日時**: {{datetime}}  
**タグ**: #daily #{{year}} #{{month}}
"""
        
        try:
            if template_path.exists():
                with open(template_path, 'r', encoding='utf-8') as f:
                    return f.read()
            else:
                # デフォルトテンプレートを保存
                with open(template_path, 'w', encoding='utf-8') as f:
                    f.write(default_template)
                self.logger.info(f"Created default template: {template_path}")
                return default_template
        except Exception as e:
            self.logger.error(f"Error loading template: {e}")
            return default_template
    
    def create_daily_note(self, target_date=None):
        """Daily Noteを作成"""
        if target_date is None:
            target_date = datetime.now().date()
        
        # ファイル名とパス
        filename = f"{target_date.strftime('%Y%m%d')}_daily.md"
        file_path = self.inbox_path / filename
        
        # 既に存在する場合はスキップ
        if file_path.exists():
            self.logger.info(f"Daily note already exists: {filename}")
            print(f"Daily note already exists: {filename}")
            return file_path
        
        # テンプレートを取得
        template = self.get_daily_note_template()
        
        # 日付変数を置換
        yesterday = target_date - timedelta(days=1)
        tomorrow = target_date + timedelta(days=1)
        
        content = template.replace('{{date}}', target_date.strftime('%Y-%m-%d'))
        content = content.replace('{{yesterday}}', yesterday.strftime('%Y%m%d_daily'))
        content = content.replace('{{tomorrow}}', tomorrow.strftime('%Y%m%d_daily'))
        content = content.replace('{{datetime}}', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        content = content.replace('{{year}}', target_date.strftime('%Y'))
        content = content.replace('{{month}}', target_date.strftime('%m'))
        
        # ファイルを作成
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            self.logger.info(f"Created daily note: {filename}")
            print(f"✓ Created daily note: {filename}")
            return file_path
            
        except Exception as e:
            self.logger.error(f"Error creating daily note: {e}")
            print(f"✗ Error creating daily note: {e}")
            raise
    
    def create_weekly_notes(self):
        """今週のDaily Noteを一括作成"""
        today = datetime.now().date()
        
        # 今週の月曜日を取得
        monday = today - timedelta(days=today.weekday())
        
        created_notes = []
        for i in range(7):  # 月曜日から日曜日まで
            date = monday + timedelta(days=i)
            try:
                note_path = self.create_daily_note(date)
                created_notes.append(note_path)
            except Exception as e:
                self.logger.error(f"Failed to create note for {date}: {e}")
        
        return created_notes
    
    def get_daily_note_stats(self):
        """Daily Noteの統計を取得"""
        daily_notes = list(self.inbox_path.glob("*_daily.md"))
        
        stats = {
            'total_notes': len(daily_notes),
            'this_month': 0,
            'this_year': 0
        }
        
        current_month = datetime.now().strftime('%Y%m')
        current_year = datetime.now().strftime('%Y')
        
        for note in daily_notes:
            if note.stem.startswith(current_month):
                stats['this_month'] += 1
            if note.stem.startswith(current_year):
                stats['this_year'] += 1
        
        return stats


def main():
    """メイン関数"""
    vault_path = "/Users/hashiguchimasaki/project/obsidian"
    generator = DailyNoteGenerator(vault_path)
    
    print("Daily Note Generator")
    print("===================")
    
    # 今日のDaily Noteを作成
    generator.create_daily_note()
    
    # 統計を表示
    stats = generator.get_daily_note_stats()
    print(f"\nDaily Note Statistics:")
    print(f"  - Total notes: {stats['total_notes']}")
    print(f"  - This month: {stats['this_month']}")
    print(f"  - This year: {stats['this_year']}")


if __name__ == "__main__":
    main()