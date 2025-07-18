#!/usr/bin/env python3
"""
特定メンバーの月報を生成（gussan以外）
"""

from monthly_report_analyzer import MonthlyReportAnalyzer, process_all_members_monthly
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def generate_reports_for_members():
    """gussan以外のメンバーの月報を生成"""
    
    # 対象メンバー
    target_members = ["yukari", "yukari_web", "prog.ji", "takanori07"]
    
    # 対象期間（2024年5月〜2025年7月）
    periods = [
        (2024, 5), (2024, 6), (2024, 7), (2024, 8), (2024, 9), (2024, 10),
        (2024, 11), (2024, 12), (2025, 1), (2025, 2), (2025, 3), (2025, 4),
        (2025, 5), (2025, 6), (2025, 7)
    ]
    
    analyzer = MonthlyReportAnalyzer()
    
    for year, month in periods:
        logger.info(f"\n{'='*50}")
        logger.info(f"📊 {year}年{month}月の月報を生成中...")
        logger.info(f"{'='*50}")
        
        for member in target_members:
            try:
                # メンバーのデータを分析
                analysis = analyzer.analyze_member_monthly_data(member, year, month)
                
                # データがある場合のみ月報を生成
                if analysis["summary"]["daily_report_count"] > 0 or \
                   analysis["summary"]["question_count"] > 0 or \
                   analysis["summary"]["progress_count"] > 0:
                    
                    filepath = analyzer.save_monthly_report(analysis)
                    
                    logger.info(f"✅ {member}: {filepath}")
                    logger.info(f"   - 日報: {analysis['summary']['daily_report_count']}件")
                    logger.info(f"   - 質問: {analysis['summary']['question_count']}件")
                    logger.info(f"   - 進捗: {analysis['summary']['progress_count']}件")
                    logger.info(f"   - 稼働時間: {analysis['summary']['total_working_hours']:.1f}時間")
                    logger.info(f"   - 売上: {analysis['summary']['total_revenue']:,}円")
                else:
                    logger.info(f"⏭️  {member}: データなし")
                    
            except Exception as e:
                logger.error(f"❌ {member}: エラー - {str(e)}")

if __name__ == "__main__":
    generate_reports_for_members()