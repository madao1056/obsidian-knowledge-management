#!/usr/bin/env python3
"""
月報分析システム
日報データから月次レポートを生成し、PDCAサイクルの分析を行う
"""

import json
import re
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from collections import defaultdict
import logging

# Notionインテグレーションをインポート
try:
    from notion_integration import NotionIntegration
except ImportError:
    NotionIntegration = None

# ログ設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MonthlyReportAnalyzer:
    def __init__(self):
        self.inbox_path = Path(__file__).parent.parent / "00_Inbox" / "discord"
        self.support_path = Path(__file__).parent.parent / "03_Support" / "グッサポ・ラボ"
        self.members_path = self.support_path / "メンバー管理"
        self.members_path.mkdir(parents=True, exist_ok=True)
        
        # Notionインテグレーション
        self.notion = NotionIntegration() if NotionIntegration else None
        
    def analyze_member_monthly_data(self, member_name: str, year: int, month: int) -> Dict:
        """特定メンバーの月次データを分析"""
        
        # 該当月のデータを収集
        monthly_data = {
            "daily_reports": [],
            "questions": [],
            "progress": [],
            "working_hours": [],
            "revenues": [],
            "sales_activities": [],
            "completed_tasks": [],
            "challenges": []
        }
        
        # JSONファイルを読み込み
        for json_file in self.inbox_path.glob(f"{member_name}_*.json"):
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
                # 配列の場合は各要素を処理
                if isinstance(data, list):
                    for item in data:
                        self._process_data_item(item, year, month, monthly_data)
                else:
                    self._process_data_item(data, year, month, monthly_data)
                    
            except Exception as e:
                logger.error(f"Error reading {json_file}: {e}")
        
        # 月次分析を実行
        analysis = self._perform_monthly_analysis(monthly_data, member_name, year, month)
        
        return analysis
    
    def _process_data_item(self, item: Dict, year: int, month: int, monthly_data: Dict):
        """個別のデータアイテムを処理"""
        try:
            # タイムスタンプから日付を抽出
            timestamp = item.get("timestamp", "")
            dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
            
            # 該当月のデータのみ処理
            if dt.year != year or dt.month != month:
                return
            
            content = item.get("content", "")
            data_type = item.get("type", "")
            
            # データタイプに応じて分類
            if data_type == "daily_report":
                monthly_data["daily_reports"].append(item)
                
                # 稼働時間を抽出
                hours_match = re.search(r'(\d+\.?\d*)\s*時間', content)
                if hours_match:
                    monthly_data["working_hours"].append(float(hours_match.group(1)))
                
                # 売上を抽出
                revenue_match = re.search(r'(\d+(?:,\d{3})*)\s*円', content)
                if revenue_match:
                    revenue = int(revenue_match.group(1).replace(",", ""))
                    monthly_data["revenues"].append(revenue)
                
                # 営業活動を抽出
                sales_match = re.search(r'営業.*?(\d+)\s*件', content)
                if sales_match:
                    monthly_data["sales_activities"].append(int(sales_match.group(1)))
                
                # 完了タスクを抽出
                if "完了" in content or "できました" in content:
                    monthly_data["completed_tasks"].append(content)
                
                # 課題を抽出
                if "課題" in content or "困った" in content:
                    monthly_data["challenges"].append(content)
                    
            elif data_type == "question":
                monthly_data["questions"].append(item)
                
            elif data_type == "progress":
                monthly_data["progress"].append(item)
                
        except Exception as e:
            logger.error(f"Error processing data item: {e}")
    
    def _perform_monthly_analysis(self, data: Dict, member_name: str, year: int, month: int) -> Dict:
        """月次分析を実行"""
        
        # 基本統計
        total_working_hours = sum(data["working_hours"])
        avg_working_hours = sum(data["working_hours"]) / len(data["working_hours"]) if data["working_hours"] else 0
        total_revenue = sum(data["revenues"])
        total_sales = sum(data["sales_activities"])
        
        # PDCA分析
        pdca_analysis = self._analyze_pdca(data, total_working_hours, total_revenue, total_sales)
        
        # 成長指標
        growth_metrics = self._calculate_growth_metrics(data, member_name, year, month)
        
        return {
            "member_name": member_name,
            "year": year,
            "month": month,
            "summary": {
                "total_working_hours": total_working_hours,
                "average_daily_hours": avg_working_hours,
                "total_revenue": total_revenue,
                "total_sales_activities": total_sales,
                "daily_report_count": len(data["daily_reports"]),
                "question_count": len(data["questions"]),
                "progress_count": len(data["progress"])
            },
            "pdca_analysis": pdca_analysis,
            "growth_metrics": growth_metrics,
            "raw_data": data
        }
    
    def _analyze_pdca(self, data: Dict, working_hours: float, revenue: int, sales: int) -> Dict:
        """PDCAサイクルの分析"""
        
        pdca = {
            "plan": {
                "目標達成度": self._calculate_goal_achievement(working_hours, revenue),
                "計画の具体性": self._analyze_plan_quality(data["daily_reports"]),
                "改善ポイント": []
            },
            "do": {
                "実行率": self._calculate_execution_rate(data),
                "稼働効率": revenue / working_hours if working_hours > 0 else 0,
                "営業効率": sales / len(data["daily_reports"]) if data["daily_reports"] else 0,
                "強み": [],
                "課題": []
            },
            "check": {
                "振り返り頻度": self._analyze_review_frequency(data["daily_reports"]),
                "課題認識力": len(data["challenges"]),
                "質問積極性": len(data["questions"]),
                "気づき": []
            },
            "action": {
                "改善実施数": self._count_improvements(data),
                "次月への提案": [],
                "必要なサポート": []
            }
        }
        
        # 具体的な分析
        pdca["plan"]["改善ポイント"] = self._suggest_plan_improvements(data)
        pdca["do"]["強み"] = self._identify_strengths(data)
        pdca["do"]["課題"] = self._identify_challenges(data)
        pdca["check"]["気づき"] = self._extract_insights(data)
        pdca["action"]["次月への提案"] = self._generate_suggestions(pdca)
        pdca["action"]["必要なサポート"] = self._identify_support_needs(data)
        
        return pdca
    
    def _calculate_goal_achievement(self, hours: float, revenue: int) -> float:
        """目標達成度を計算（仮の目標値）"""
        # 目標: 月160時間、月30万円
        hour_achievement = min(hours / 160 * 100, 100) if hours > 0 else 0
        revenue_achievement = min(revenue / 300000 * 100, 100) if revenue > 0 else 0
        return (hour_achievement + revenue_achievement) / 2
    
    def _analyze_plan_quality(self, reports: List[Dict]) -> str:
        """計画の具体性を分析"""
        specific_keywords = ["時間", "件", "円", "まで", "完了"]
        specific_count = sum(
            1 for report in reports 
            if any(keyword in report.get("content", "") for keyword in specific_keywords)
        )
        
        ratio = specific_count / len(reports) if reports else 0
        
        if ratio > 0.7:
            return "高い（具体的な数値目標あり）"
        elif ratio > 0.4:
            return "中程度（一部具体的）"
        else:
            return "低い（抽象的な目標が多い）"
    
    def _calculate_execution_rate(self, data: Dict) -> float:
        """実行率を計算"""
        if not data["daily_reports"]:
            return 0
        
        # 予定に対する完了の割合を推定
        completed = len(data["completed_tasks"])
        total_planned = len(data["daily_reports"]) * 3  # 1日平均3タスクと仮定
        
        return min(completed / total_planned * 100, 100) if total_planned > 0 else 0
    
    def _analyze_review_frequency(self, reports: List[Dict]) -> str:
        """振り返り頻度を分析"""
        review_keywords = ["振り返り", "反省", "改善", "次回", "学び"]
        review_count = sum(
            1 for report in reports
            if any(keyword in report.get("content", "") for keyword in review_keywords)
        )
        
        ratio = review_count / len(reports) if reports else 0
        
        if ratio > 0.5:
            return "高い（定期的な振り返りあり）"
        elif ratio > 0.2:
            return "中程度（時々振り返り）"
        else:
            return "低い（振り返り不足）"
    
    def _count_improvements(self, data: Dict) -> int:
        """改善実施数をカウント"""
        improvement_keywords = ["改善", "変更", "修正", "効率化", "工夫"]
        count = 0
        
        for report in data["daily_reports"] + data["progress"]:
            content = report.get("content", "")
            if any(keyword in content for keyword in improvement_keywords):
                count += 1
        
        return count
    
    def _suggest_plan_improvements(self, data: Dict) -> List[str]:
        """計画の改善ポイントを提案"""
        suggestions = []
        
        if not data["working_hours"]:
            suggestions.append("稼働時間の記録を毎日行う")
        
        if len(data["daily_reports"]) < 20:
            suggestions.append("日報の投稿頻度を上げる（目標：毎日）")
        
        if not data["revenues"]:
            suggestions.append("売上目標と実績を明記する")
        
        return suggestions
    
    def _identify_strengths(self, data: Dict) -> List[str]:
        """強みを特定"""
        strengths = []
        
        if data["working_hours"] and sum(data["working_hours"]) / len(data["working_hours"]) > 5:
            strengths.append("安定した稼働時間の確保")
        
        if len(data["questions"]) > 5:
            strengths.append("積極的な質問姿勢")
        
        if data["sales_activities"] and sum(data["sales_activities"]) > 200:
            strengths.append("営業活動の継続性")
        
        return strengths
    
    def _identify_challenges(self, data: Dict) -> List[str]:
        """課題を特定"""
        challenges = []
        
        # 直接的な課題の抽出
        for item in data["challenges"]:
            # 最初の数語を抽出
            match = re.search(r'課題[:：]?\s*(.{10,50})', item)
            if match:
                challenges.append(match.group(1))
        
        return list(set(challenges))[:5]  # 重複を除いて最大5個
    
    def _extract_insights(self, data: Dict) -> List[str]:
        """気づきを抽出"""
        insights = []
        
        # 進捗報告から学びを抽出
        for progress in data["progress"]:
            content = progress.get("content", "")
            if "学び" in content or "気づき" in content or "わかった" in content:
                # 該当部分を抽出
                match = re.search(r'(?:学び|気づき|わかった)[:：]?\s*(.{10,50})', content)
                if match:
                    insights.append(match.group(1))
        
        return list(set(insights))[:5]
    
    def _generate_suggestions(self, pdca: Dict) -> List[str]:
        """次月への提案を生成"""
        suggestions = []
        
        # 目標達成度に基づく提案
        achievement = pdca["plan"]["目標達成度"]
        if achievement < 50:
            suggestions.append("小さな目標から始めて成功体験を積む")
        elif achievement < 80:
            suggestions.append("目標を10-20%上方修正してチャレンジ")
        
        # 実行率に基づく提案
        if pdca["do"]["実行率"] < 60:
            suggestions.append("タスクの優先順位を明確にする")
        
        # 効率に基づく提案
        if pdca["do"]["稼働効率"] < 2000:  # 時給2000円未満
            suggestions.append("高単価案件の獲得に注力")
        
        return suggestions
    
    def _identify_support_needs(self, data: Dict) -> List[str]:
        """必要なサポートを特定"""
        needs = []
        
        # 質問内容から判断
        tech_questions = sum(1 for q in data["questions"] if any(
            tech in q.get("content", "").lower() 
            for tech in ["実装", "エラー", "コード", "バグ"]
        ))
        
        if tech_questions > 3:
            needs.append("技術的なメンタリング")
        
        if len(data["questions"]) > 10:
            needs.append("定期的な1on1セッション")
        
        if not data["revenues"]:
            needs.append("営業・案件獲得のサポート")
        
        return needs
    
    def _calculate_growth_metrics(self, data: Dict, member_name: str, year: int, month: int) -> Dict:
        """成長指標を計算"""
        # 前月のデータと比較（簡易版）
        prev_month = month - 1 if month > 1 else 12
        prev_year = year if month > 1 else year - 1
        
        return {
            "稼働時間成長率": 0,  # TODO: 前月データとの比較
            "売上成長率": 0,
            "営業効率改善率": 0,
            "スキル習得数": len(set(self._extract_technologies(data))),
            "課題解決率": self._calculate_resolution_rate(data)
        }
    
    def _extract_technologies(self, data: Dict) -> List[str]:
        """使用技術を抽出"""
        tech_keywords = [
            "JavaScript", "TypeScript", "React", "Vue", "WordPress",
            "HTML", "CSS", "Git", "AI", "ChatGPT", "Python"
        ]
        
        found_techs = set()
        for item in data["daily_reports"] + data["progress"]:
            content = item.get("content", "").lower()
            for tech in tech_keywords:
                if tech.lower() in content:
                    found_techs.add(tech)
        
        return list(found_techs)
    
    def _calculate_resolution_rate(self, data: Dict) -> float:
        """課題解決率を計算"""
        if not data["challenges"]:
            return 100.0
        
        # 解決済みキーワード
        resolved_keywords = ["解決", "できた", "克服", "改善した"]
        resolved_count = sum(
            1 for challenge in data["challenges"]
            if any(keyword in challenge for keyword in resolved_keywords)
        )
        
        return (resolved_count / len(data["challenges"]) * 100) if data["challenges"] else 0
    
    def generate_monthly_report(self, analysis: Dict) -> str:
        """月報マークダウンを生成"""
        member = analysis["member_name"]
        year = analysis["year"]
        month = analysis["month"]
        summary = analysis["summary"]
        pdca = analysis["pdca_analysis"]
        growth = analysis["growth_metrics"]
        
        md = f"""# {member} - {year}年{month}月 月報

## 📊 月次サマリー

### 活動実績
- **総稼働時間**: {summary['total_working_hours']:.1f}時間
- **平均稼働時間**: {summary['average_daily_hours']:.1f}時間/日
- **総売上**: {summary['total_revenue']:,}円
- **営業活動**: {summary['total_sales_activities']}件
- **日報投稿数**: {summary['daily_report_count']}回
- **質問数**: {summary['question_count']}件
- **進捗報告**: {summary['progress_count']}件

### 効率指標
- **時給換算**: {int(summary['total_revenue'] / summary['total_working_hours']) if summary['total_working_hours'] > 0 else 0:,}円/時間
- **営業効率**: {summary['total_sales_activities'] / summary['daily_report_count'] if summary['daily_report_count'] > 0 else 0:.1f}件/日

## 🔄 PDCA分析

### Plan（計画）
- **目標達成度**: {pdca['plan']['目標達成度']:.1f}%
- **計画の具体性**: {pdca['plan']['計画の具体性']}

#### 改善ポイント
"""
        
        for point in pdca['plan']['改善ポイント']:
            md += f"- {point}\n"
        
        md += f"""
### Do（実行）
- **実行率**: {pdca['do']['実行率']:.1f}%
- **稼働効率**: {pdca['do']['稼働効率']:.0f}円/時間
- **営業効率**: {pdca['do']['営業効率']:.1f}件/日

#### 強み
"""
        
        for strength in pdca['do']['強み']:
            md += f"- ✅ {strength}\n"
        
        md += "\n#### 課題\n"
        for challenge in pdca['do']['課題']:
            md += f"- ⚠️ {challenge}\n"
        
        md += f"""
### Check（評価）
- **振り返り頻度**: {pdca['check']['振り返り頻度']}
- **課題認識力**: {pdca['check']['課題認識力']}件の課題を認識
- **質問積極性**: {pdca['check']['質問積極性']}件の質問

#### 主な気づき
"""
        
        for insight in pdca['check']['気づき']:
            md += f"- 💡 {insight}\n"
        
        md += f"""
### Action（改善）
- **改善実施数**: {pdca['action']['改善実施数']}件

#### 次月への提案
"""
        
        for suggestion in pdca['action']['次月への提案']:
            md += f"- 🎯 {suggestion}\n"
        
        md += "\n#### 必要なサポート\n"
        for support in pdca['action']['必要なサポート']:
            md += f"- 🤝 {support}\n"
        
        md += f"""
## 📈 成長指標

- **スキル習得数**: {growth['スキル習得数']}個の技術に触れた
- **課題解決率**: {growth['課題解決率']:.1f}%

## 💭 コーチングポイント

1. **継続すべき点**
   - 日々の活動記録の習慣
   - 積極的な質問姿勢
   - 営業活動の継続

2. **改善すべき点**
   - 目標設定の具体化
   - 振り返りの深掘り
   - 効率性の向上

3. **次月のフォーカス**
   - 高単価案件の獲得
   - スキルアップの時間確保
   - PDCAサイクルの高速化

---
*このレポートは自動生成されています。詳細な個別相談が必要な場合はお申し出ください。*
"""
        
        return md
    
    def _process_notion_links(self, member: str, year: int, month: int, analysis: Dict):
        """月報内のNotionリンクを処理"""
        if not self.notion or not self.notion.client:
            logger.info("Notion APIが設定されていないため、リンク処理をスキップします")
            return
        
        # 全日報からNotionリンクを抽出
        notion_links = []
        all_content = ""
        
        # 日報からコンテンツを収集
        for report in analysis.get('raw_data', {}).get('daily_reports', []):
            if 'content' in report:
                all_content += report['content'] + "\n"
        
        # 質問からもコンテンツを収集
        for question in analysis.get('raw_data', {}).get('questions', []):
            if 'content' in question:
                all_content += question['content'] + "\n"
        
        # Notionリンクを抽出して処理
        extracted_links = self.notion.extract_notion_links(all_content)
        
        if extracted_links:
            logger.info(f"{member}の月報から{len(extracted_links)}個のNotionリンクを検出")
            
            # Notionコンテンツを取得
            notion_data = []
            for link_info in extracted_links:
                try:
                    page_content = self.notion.get_page_content(link_info['page_id'])
                    if page_content:
                        notion_data.append({
                            'original_url': link_info['url'],
                            'page_data': page_content,
                            'extracted_at': datetime.now().isoformat()
                        })
                except Exception as e:
                    logger.error(f"Notionページ取得エラー: {e}")
            
            # メンバーフォルダに保存
            if notion_data:
                self.notion.save_notion_content(member, notion_data, 
                                              str(self.support_path / "メンバー管理"))
    
    def save_monthly_report(self, analysis: Dict):
        """月報を保存"""
        member = analysis["member_name"]
        year = analysis["year"]
        month = analysis["month"]
        
        # メンバーディレクトリ
        member_dir = self.members_path / member
        member_dir.mkdir(exist_ok=True)
        
        # 月報ディレクトリ
        monthly_dir = member_dir / "月報"
        monthly_dir.mkdir(exist_ok=True)
        
        # ファイルパス
        filename = f"{year}年{month:02d}月_月報.md"
        filepath = monthly_dir / filename
        
        # マークダウン生成
        content = self.generate_monthly_report(analysis)
        
        # 保存
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        logger.info(f"Saved monthly report: {filepath}")
        
        # Notionリンクを処理
        self._process_notion_links(member, year, month, analysis)
        
        return filepath

def process_all_members_monthly(year: int, month: int):
    """全メンバーの月報を処理"""
    analyzer = MonthlyReportAnalyzer()
    
    # メンバーリストを取得（JSONファイルから推定）
    members = set()
    for json_file in analyzer.inbox_path.glob("*_*.json"):
        member_name = json_file.stem.split("_")[0]
        members.add(member_name)
    
    processed = []
    for member in members:
        logger.info(f"Processing {member} for {year}/{month}...")
        
        # 分析実行
        analysis = analyzer.analyze_member_monthly_data(member, year, month)
        
        # 月報保存
        if analysis["summary"]["daily_report_count"] > 0:
            filepath = analyzer.save_monthly_report(analysis)
            processed.append({
                "member": member,
                "filepath": filepath,
                "summary": analysis["summary"]
            })
    
    return processed

if __name__ == "__main__":
    # 現在の年月で実行
    now = datetime.now()
    year = now.year
    month = now.month
    
    # 引数で年月を指定可能
    import sys
    if len(sys.argv) > 2:
        year = int(sys.argv[1])
        month = int(sys.argv[2])
    
    print(f"📊 {year}年{month}月の月報を生成します...")
    
    results = process_all_members_monthly(year, month)
    
    print(f"\n✅ 完了: {len(results)}名の月報を生成しました")
    for result in results:
        print(f"  - {result['member']}: {result['filepath']}")