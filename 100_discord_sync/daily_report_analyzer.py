#!/usr/bin/env python3
"""
Discord日報解析システム
日報から構造化情報を抽出してObsidianナレッジベースに変換
"""

import json
import re
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import logging

# ログ設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DailyReportAnalyzer:
    def __init__(self):
        self.inbox_path = Path(__file__).parent.parent / "00_Inbox" / "discord"
        self.support_path = Path(__file__).parent.parent / "03_Support" / "グッサポ・ラボ"
        self.members_path = self.support_path / "メンバー管理"
        self.members_path.mkdir(parents=True, exist_ok=True)
        
        # 正規表現パターン
        self.patterns = {
            "working_hours": re.compile(r'(?:稼働|作業|活動).*?(\d+\.?\d*)\s*(?:時間|h)', re.IGNORECASE),
            "tasks_completed": re.compile(r'(?:完了|終了|できた|した).*?[:：](.+?)(?:\n|$)', re.MULTILINE),
            "tasks_planned": re.compile(r'(?:予定|やる|する).*?[:：](.+?)(?:\n|$)', re.MULTILINE),
            "challenges": re.compile(r'(?:課題|問題|困った|詰まった).*?[:：](.+?)(?:\n|$)', re.MULTILINE),
            "revenue": re.compile(r'(?:売上|収入|報酬).*?(\d+(?:,\d{3})*)\s*円', re.IGNORECASE),
            "projects": re.compile(r'(?:案件|プロジェクト|制作).*?[:：](.+?)(?:\n|$)', re.MULTILINE),
            "営業": re.compile(r'営業.*?(\d+)\s*件', re.IGNORECASE)
        }
    
    def analyze_report(self, report_data: Dict) -> Dict:
        """日報を解析して構造化データを抽出"""
        content = report_data.get("content", "")
        author = report_data.get("author", "unknown")
        date = report_data.get("date", datetime.now().strftime("%Y-%m-%d"))
        
        # 稼働時間の抽出
        working_hours = self._extract_working_hours(content)
        
        # タスク情報の抽出
        tasks_completed = self._extract_tasks(content, "completed")
        tasks_planned = self._extract_tasks(content, "planned")
        
        # 課題・問題の抽出
        challenges = self._extract_challenges(content)
        
        # 売上情報の抽出
        revenue = self._extract_revenue(content)
        
        # プロジェクト情報の抽出
        projects = self._extract_projects(content)
        
        # 営業活動の抽出
        sales_activities = self._extract_sales_activities(content)
        
        # 感情分析（簡易版）
        sentiment = self._analyze_sentiment(content)
        
        return {
            "author": author,
            "date": date,
            "working_hours": working_hours,
            "tasks_completed": tasks_completed,
            "tasks_planned": tasks_planned,
            "challenges": challenges,
            "revenue": revenue,
            "projects": projects,
            "sales_activities": sales_activities,
            "sentiment": sentiment,
            "raw_content": content
        }
    
    def _extract_working_hours(self, content: str) -> Optional[float]:
        """稼働時間を抽出"""
        matches = self.patterns["working_hours"].findall(content)
        if matches:
            try:
                return float(matches[0])
            except ValueError:
                pass
        return None
    
    def _extract_tasks(self, content: str, task_type: str) -> List[str]:
        """タスクを抽出"""
        pattern = self.patterns[f"tasks_{task_type}"]
        matches = pattern.findall(content)
        tasks = []
        for match in matches:
            # 箇条書きや番号付きリストを分割
            items = re.split(r'[・\n]\s*', match)
            tasks.extend([item.strip() for item in items if item.strip()])
        return tasks
    
    def _extract_challenges(self, content: str) -> List[str]:
        """課題・問題を抽出"""
        matches = self.patterns["challenges"].findall(content)
        challenges = []
        for match in matches:
            items = re.split(r'[・\n]\s*', match)
            challenges.extend([item.strip() for item in items if item.strip()])
        return challenges
    
    def _extract_revenue(self, content: str) -> Optional[int]:
        """売上情報を抽出"""
        matches = self.patterns["revenue"].findall(content)
        if matches:
            try:
                # カンマを除去して数値に変換
                return int(matches[0].replace(",", ""))
            except ValueError:
                pass
        return None
    
    def _extract_projects(self, content: str) -> List[str]:
        """プロジェクト情報を抽出"""
        matches = self.patterns["projects"].findall(content)
        projects = []
        for match in matches:
            items = re.split(r'[・\n]\s*', match)
            projects.extend([item.strip() for item in items if item.strip()])
        return projects
    
    def _extract_sales_activities(self, content: str) -> Optional[int]:
        """営業活動件数を抽出"""
        matches = self.patterns["営業"].findall(content)
        if matches:
            try:
                return int(matches[0])
            except ValueError:
                pass
        return None
    
    def _analyze_sentiment(self, content: str) -> str:
        """感情分析（簡易版）"""
        positive_words = ["完了", "達成", "できた", "良かった", "嬉しい", "順調"]
        negative_words = ["困った", "詰まった", "難しい", "厳しい", "大変", "疲れ"]
        
        positive_count = sum(1 for word in positive_words if word in content)
        negative_count = sum(1 for word in negative_words if word in content)
        
        if positive_count > negative_count:
            return "positive"
        elif negative_count > positive_count:
            return "negative"
        else:
            return "neutral"
    
    def save_to_obsidian(self, analysis: Dict):
        """解析結果をObsidian形式で保存"""
        author = analysis["author"]
        date = analysis["date"]
        
        # メンバーディレクトリ作成
        member_dir = self.members_path / author
        member_dir.mkdir(exist_ok=True)
        
        # 日報ディレクトリ作成
        daily_reports_dir = member_dir / "日報"
        daily_reports_dir.mkdir(exist_ok=True)
        
        # 日報ファイル作成
        report_path = daily_reports_dir / f"{date}_日報.md"
        
        # マークダウン形式で保存
        content = self._generate_markdown(analysis)
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # メンバープロファイルを更新
        self._update_member_profile(author, analysis)
        
        logger.info(f"Saved daily report: {report_path}")
        return report_path
    
    def _generate_markdown(self, analysis: Dict) -> str:
        """解析結果をマークダウン形式に変換"""
        md = f"# 日報 - {analysis['author']}\n"
        md += f"## {analysis['date']}\n\n"
        
        # 稼働時間
        if analysis["working_hours"]:
            md += f"### 稼働時間\n"
            md += f"- {analysis['working_hours']}時間\n\n"
        
        # 完了タスク
        if analysis["tasks_completed"]:
            md += f"### 完了したタスク\n"
            for task in analysis["tasks_completed"]:
                md += f"- {task}\n"
            md += "\n"
        
        # 予定タスク
        if analysis["tasks_planned"]:
            md += f"### 予定しているタスク\n"
            for task in analysis["tasks_planned"]:
                md += f"- {task}\n"
            md += "\n"
        
        # プロジェクト
        if analysis["projects"]:
            md += f"### プロジェクト・案件\n"
            for project in analysis["projects"]:
                md += f"- {project}\n"
            md += "\n"
        
        # 営業活動
        if analysis["sales_activities"]:
            md += f"### 営業活動\n"
            md += f"- 送信件数: {analysis['sales_activities']}件\n\n"
        
        # 売上
        if analysis["revenue"]:
            md += f"### 売上\n"
            md += f"- {analysis['revenue']:,}円\n\n"
        
        # 課題・困ったこと
        if analysis["challenges"]:
            md += f"### 課題・困ったこと\n"
            for challenge in analysis["challenges"]:
                md += f"- {challenge}\n"
            md += "\n"
        
        # 感情状態
        sentiment_map = {
            "positive": "😊 ポジティブ",
            "negative": "😟 ネガティブ",
            "neutral": "😐 ニュートラル"
        }
        md += f"### 感情状態\n"
        md += f"- {sentiment_map.get(analysis['sentiment'], '不明')}\n\n"
        
        # 原文
        md += f"### 原文\n"
        md += f"```\n{analysis['raw_content']}\n```\n"
        
        return md
    
    def _update_member_profile(self, author: str, analysis: Dict):
        """メンバープロファイルを更新"""
        profile_path = self.members_path / author / "プロファイル.md"
        
        # 既存のプロファイルを読み込むか新規作成
        if profile_path.exists():
            with open(profile_path, 'r', encoding='utf-8') as f:
                content = f.read()
        else:
            content = self._create_initial_profile(author)
        
        # 最新情報を追加
        updated_content = self._update_profile_content(content, analysis)
        
        # 保存
        with open(profile_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
    
    def _create_initial_profile(self, author: str) -> str:
        """初期プロファイルを作成"""
        return f"""# {author} プロファイル

## 基本情報
- 名前: {author}
- 参加日: {datetime.now().strftime("%Y-%m-%d")}

## 活動サマリー
### 稼働時間
- 今月の合計: 0時間
- 先月の合計: 0時間
- 平均稼働時間: 0時間/日

### 営業活動
- 今月の送信数: 0件
- 累計送信数: 0件
- 返信率: 0%

### 売上
- 今月: 0円
- 累計: 0円

## 最近の活動
### 直近の日報
- [リンクなし]

## スキル・専門分野
- 

## 課題・サポート履歴
### よくある課題
- 

### 解決済み課題
- 

## メモ・特記事項
- 
"""
    
    def _update_profile_content(self, content: str, analysis: Dict) -> str:
        """プロファイルの内容を更新"""
        # TODO: より洗練された更新ロジックを実装
        # 現在は最新の日報へのリンクを更新するだけ
        date = analysis["date"]
        link = f"- [[{date}_日報]]"
        
        # 直近の日報セクションを探して更新
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if "### 直近の日報" in line:
                if i + 1 < len(lines):
                    lines[i + 1] = link
                break
        
        return '\n'.join(lines)
    
    def process_all_reports(self):
        """すべての未処理日報を処理"""
        json_files = list(self.inbox_path.glob("*_日報.json"))
        processed_count = 0
        
        for json_file in json_files:
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    report_data = json.load(f)
                
                # 解析
                analysis = self.analyze_report(report_data)
                
                # Obsidianに保存
                self.save_to_obsidian(analysis)
                
                # 処理済みファイルを削除
                json_file.unlink()
                
                processed_count += 1
                logger.info(f"Processed: {json_file.name}")
                
            except Exception as e:
                logger.error(f"Error processing {json_file}: {str(e)}")
        
        return processed_count

if __name__ == "__main__":
    # テスト実行
    analyzer = DailyReportAnalyzer()
    count = analyzer.process_all_reports()
    print(f"処理完了: {count}件の日報を処理しました")