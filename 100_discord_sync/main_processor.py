#!/usr/bin/env python3
"""
Discord-Obsidian連携メインプロセッサー
定期的に実行して、Discordデータを解析しObsidianナレッジベースを更新
"""

import schedule
import time
import logging
from pathlib import Path
from datetime import datetime
import subprocess
import sys
from typing import Dict, List, Optional

# 各解析モジュールをインポート
from daily_report_analyzer import DailyReportAnalyzer
from question_progress_analyzer import QuestionProgressAnalyzer

# ログ設定
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('discord_sync.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class DiscordObsidianProcessor:
    def __init__(self):
        self.daily_analyzer = DailyReportAnalyzer()
        self.qp_analyzer = QuestionProgressAnalyzer()
        self.stats_path = Path(__file__).parent / "processing_stats.json"
        
    def process_all(self):
        """すべてのDiscordデータを処理"""
        logger.info("Discord-Obsidian同期処理を開始します")
        
        try:
            # 日報を処理
            daily_count = self.daily_analyzer.process_all_reports()
            logger.info(f"日報処理完了: {daily_count}件")
            
            # 質問・進捗を処理
            qp_count = self.qp_analyzer.process_all_questions_progress()
            logger.info(f"質問・進捗処理完了: {qp_count}件")
            
            # 統計情報を更新
            self._update_stats(daily_count, qp_count)
            
            # サマリーレポートを生成
            self._generate_summary_report()
            
            logger.info("Discord-Obsidian同期処理が完了しました")
            
        except Exception as e:
            logger.error(f"処理中にエラーが発生しました: {str(e)}")
            raise
    
    def _update_stats(self, daily_count: int, qp_count: int):
        """処理統計を更新"""
        import json
        
        stats = {}
        if self.stats_path.exists():
            with open(self.stats_path, 'r', encoding='utf-8') as f:
                stats = json.load(f)
        
        # 今日の統計を追加
        today = datetime.now().strftime("%Y-%m-%d")
        if today not in stats:
            stats[today] = {
                "daily_reports": 0,
                "questions_progress": 0,
                "executions": 0
            }
        
        stats[today]["daily_reports"] += daily_count
        stats[today]["questions_progress"] += qp_count
        stats[today]["executions"] += 1
        
        # 保存
        with open(self.stats_path, 'w', encoding='utf-8') as f:
            json.dump(stats, f, ensure_ascii=False, indent=2)
    
    def _generate_summary_report(self):
        """サマリーレポートを生成"""
        summary_path = Path(__file__).parent.parent / "03_Support" / "グッサポ・ラボ" / "Discord同期サマリー.md"
        
        # メンバー情報を収集
        members_path = Path(__file__).parent.parent / "03_Support" / "グッサポ・ラボ" / "メンバー管理"
        members = []
        
        if members_path.exists():
            for member_dir in members_path.iterdir():
                if member_dir.is_dir():
                    member_info = self._get_member_summary(member_dir)
                    if member_info:
                        members.append(member_info)
        
        # サマリー作成
        content = f"# Discord同期サマリー\n"
        content += f"最終更新: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
        
        content += "## アクティブメンバー\n"
        for member in members:
            content += f"\n### {member['name']}\n"
            content += f"- 最新日報: {member.get('latest_report', 'なし')}\n"
            content += f"- 今月の稼働時間: {member.get('monthly_hours', 0)}時間\n"
            content += f"- 未解決の質問: {member.get('open_questions', 0)}件\n"
            content += f"- 最近の活動: {member.get('recent_activity', 'なし')}\n"
        
        # アラート
        content += "\n## 要注意事項\n"
        alerts = self._check_alerts(members)
        if alerts:
            for alert in alerts:
                content += f"- ⚠️ {alert}\n"
        else:
            content += "- 特になし\n"
        
        # 保存
        with open(summary_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    def _get_member_summary(self, member_dir: Path) -> Optional[Dict]:
        """メンバーのサマリー情報を取得"""
        member_name = member_dir.name
        summary = {"name": member_name}
        
        # 最新の日報を確認
        daily_reports_dir = member_dir / "日報"
        if daily_reports_dir.exists():
            reports = sorted(daily_reports_dir.glob("*.md"), reverse=True)
            if reports:
                latest = reports[0]
                summary["latest_report"] = latest.stem.replace("_日報", "")
                
                # 今月の稼働時間を計算（簡易版）
                # TODO: より正確な集計ロジックを実装
                summary["monthly_hours"] = 0
        
        # 未解決の質問を確認
        questions_dir = member_dir / "質問履歴"
        if questions_dir.exists():
            # TODO: 未解決質問のカウントロジック
            summary["open_questions"] = 0
        
        return summary
    
    def _check_alerts(self, members: List[Dict]) -> List[str]:
        """アラートをチェック"""
        alerts = []
        today = datetime.now()
        
        for member in members:
            # 3日以上日報がない場合
            if "latest_report" in member:
                try:
                    report_date = datetime.strptime(member["latest_report"], "%Y-%m-%d")
                    days_diff = (today - report_date).days
                    if days_diff > 3:
                        alerts.append(f"{member['name']}さんの日報が{days_diff}日間ありません")
                except:
                    pass
            
            # 稼働時間が少ない場合
            if member.get("monthly_hours", 0) < 40 and today.day > 15:
                alerts.append(f"{member['name']}さんの今月の稼働時間が少ないです（{member.get('monthly_hours', 0)}時間）")
        
        return alerts

def run_once():
    """1回だけ実行"""
    processor = DiscordObsidianProcessor()
    processor.process_all()

def run_scheduled():
    """スケジュール実行"""
    processor = DiscordObsidianProcessor()
    
    # 毎日定期実行（朝9時と夜9時）
    schedule.every().day.at("09:00").do(processor.process_all)
    schedule.every().day.at("21:00").do(processor.process_all)
    
    logger.info("Discord-Obsidian同期スケジューラーを開始しました")
    logger.info("実行スケジュール: 毎日 9:00, 21:00")
    
    while True:
        schedule.run_pending()
        time.sleep(60)  # 1分ごとにチェック

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Discord-Obsidian同期処理")
    parser.add_argument("--once", action="store_true", help="1回だけ実行")
    parser.add_argument("--daemon", action="store_true", help="デーモンとして実行")
    
    args = parser.parse_args()
    
    if args.once:
        run_once()
    elif args.daemon:
        run_scheduled()
    else:
        # デフォルトは1回実行
        run_once()