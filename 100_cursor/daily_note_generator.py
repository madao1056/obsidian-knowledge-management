#!/usr/bin/env python3
"""
Daily Note自動生成スクリプト
毎日のDaily Noteを自動生成します。
"""

from datetime import datetime, timedelta, date
from pathlib import Path
from typing import List, Optional, Dict

from base_processor import BaseProcessor


class DailyNoteGenerator(BaseProcessor):
    def __init__(self, vault_path: str):
        super().__init__(vault_path, 'daily_note_generator')
    
    def get_daily_note_template(self) -> str:
        """Daily Noteテンプレートを取得"""
        template_path = self.templates_dir / "daily_note_template.md"
        
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
        
        if template_path.exists():
            content = self.read_file_safe(template_path)
            if content:
                return content
        
        # デフォルトテンプレートを保存
        if self.write_file_safe(template_path, default_template):
            self.log_info(f"Created default template: {template_path}")
        
        return default_template
    
    def create_daily_note(self, target_date: Optional[date] = None) -> Optional[Path]:
        """Daily Noteを作成"""
        if target_date is None:
            target_date = datetime.now().date()
        
        # ファイル名とパス
        filename = f"{target_date.strftime('%Y%m%d')}_daily.md"
        file_path = self.inbox_path / filename
        
        # 既に存在する場合はスキップ
        if file_path.exists():
            self.log_info(f"Daily note already exists: {filename}")
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
        content = content.replace('{{datetime}}', self.format_timestamp())
        content = content.replace('{{year}}', target_date.strftime('%Y'))
        content = content.replace('{{month}}', target_date.strftime('%m'))
        
        # ファイルを作成
        if self.write_file_safe(file_path, content):
            self.log_info(f"Created daily note: {filename}")
            print(f"✓ Created daily note: {filename}")
            return file_path
        else:
            print(f"✗ Error creating daily note: {filename}")
            return None
    
    def create_weekly_notes(self) -> List[Path]:
        """今週のDaily Noteを一括作成"""
        today = datetime.now().date()
        
        # 今週の月曜日を取得
        monday = today - timedelta(days=today.weekday())
        
        created_notes: List[Path] = []
        for i in range(7):  # 月曜日から日曜日まで
            target_date = monday + timedelta(days=i)
            note_path = self.create_daily_note(target_date)
            if note_path:
                created_notes.append(note_path)
        
        return created_notes
    
    def get_daily_note_stats(self) -> Dict[str, int]:
        """Daily Noteの統計を取得"""
        daily_notes = list(self.inbox_path.glob("*_daily.md"))
        
        stats: Dict[str, int] = {
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


def main() -> None:
    """メイン関数"""
    vault_path = "/Users/hashiguchimasaki/project/obsidian"
    generator = DailyNoteGenerator(vault_path)
    
    print("Daily Note Generator")
    print("===================")
    
    # 今日のDaily Noteを作成
    generator.create_daily_note()
    
    # 統訨を表示
    stats = generator.get_daily_note_stats()
    print(f"\nDaily Note Statistics:")
    print(f"  - Total notes: {stats['total_notes']}")
    print(f"  - This month: {stats['this_month']}")
    print(f"  - This year: {stats['this_year']}")


if __name__ == "__main__":
    main()