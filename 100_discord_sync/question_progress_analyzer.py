#!/usr/bin/env python3
"""
Discord質問・進捗報告解析システム
質問と進捗報告から構造化情報を抽出してナレッジベースを構築
"""

import json
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Set
import logging

# ログ設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class QuestionProgressAnalyzer:
    def __init__(self):
        self.inbox_path = Path(__file__).parent.parent / "00_Inbox" / "discord"
        self.support_path = Path(__file__).parent.parent / "03_Support" / "グッサポ・ラボ"
        self.members_path = self.support_path / "メンバー管理"
        self.knowledge_path = Path(__file__).parent.parent / "30_Permanent" / "34_Product" / "グッサポ・ラボ"
        
        # ディレクトリ作成
        self.members_path.mkdir(parents=True, exist_ok=True)
        self.knowledge_path.mkdir(parents=True, exist_ok=True)
        
        # 質問カテゴリ
        self.question_categories = {
            "技術": ["エラー", "実装", "コード", "バグ", "動作", "設定"],
            "営業": ["営業文", "返信", "クライアント", "提案", "見積"],
            "デザイン": ["figma", "デザイン", "UI", "UX", "レイアウト"],
            "案件管理": ["納期", "スケジュール", "進捗", "タスク"],
            "ツール": ["AI", "ChatGPT", "ツール", "効率化"],
            "その他": []
        }
    
    def analyze_questions(self, questions_data: List[Dict]) -> List[Dict]:
        """質問リストを解析"""
        analyzed_questions = []
        
        for question in questions_data:
            content = question.get("content", "")
            timestamp = question.get("timestamp", "")
            
            # カテゴリ分類
            category = self._categorize_question(content)
            
            # キーワード抽出
            keywords = self._extract_keywords(content)
            
            # 緊急度判定
            urgency = self._assess_urgency(content)
            
            # 関連技術の抽出
            technologies = self._extract_technologies(content)
            
            analyzed = {
                "content": content,
                "timestamp": timestamp,
                "category": category,
                "keywords": keywords,
                "urgency": urgency,
                "technologies": technologies,
                "status": question.get("status", "open")
            }
            
            analyzed_questions.append(analyzed)
        
        return analyzed_questions
    
    def analyze_progress(self, progress_data: List[Dict]) -> List[Dict]:
        """進捗報告リストを解析"""
        analyzed_progress = []
        
        for progress in progress_data:
            content = progress.get("content", "")
            timestamp = progress.get("timestamp", "")
            
            # 達成事項の抽出
            achievements = self._extract_achievements(content)
            
            # 学習ポイントの抽出
            learnings = self._extract_learnings(content)
            
            # 使用技術の抽出
            technologies = self._extract_technologies(content)
            
            # 数値データの抽出
            metrics = self._extract_metrics(content)
            
            analyzed = {
                "content": content,
                "timestamp": timestamp,
                "achievements": achievements,
                "learnings": learnings,
                "technologies": technologies,
                "metrics": metrics
            }
            
            analyzed_progress.append(analyzed)
        
        return analyzed_progress
    
    def _categorize_question(self, content: str) -> str:
        """質問をカテゴリに分類"""
        content_lower = content.lower()
        
        for category, keywords in self.question_categories.items():
            if any(keyword in content_lower for keyword in keywords):
                return category
        
        return "その他"
    
    def _extract_keywords(self, content: str) -> List[str]:
        """重要キーワードを抽出"""
        # 技術用語や重要な名詞を抽出（簡易版）
        keywords = []
        
        # 技術用語パターン
        tech_patterns = [
            r'[A-Z][a-z]+(?:[A-Z][a-z]+)*',  # CamelCase
            r'[A-Z]{2,}',  # 略語
            r'\b(?:エラー|バグ|問題|課題|実装|設定)\b'
        ]
        
        for pattern in tech_patterns:
            matches = re.findall(pattern, content)
            keywords.extend(matches)
        
        # 重複を除去
        return list(set(keywords))[:10]  # 最大10個
    
    def _assess_urgency(self, content: str) -> str:
        """緊急度を判定"""
        urgent_words = ["緊急", "至急", "すぐ", "今すぐ", "ASAP", "困っています", "止まって"]
        high_words = ["早め", "なるべく", "できれば"]
        
        content_lower = content.lower()
        
        if any(word in content_lower for word in urgent_words):
            return "urgent"
        elif any(word in content_lower for word in high_words):
            return "high"
        else:
            return "normal"
    
    def _extract_technologies(self, content: str) -> List[str]:
        """使用技術を抽出"""
        tech_list = [
            "JavaScript", "TypeScript", "React", "Vue", "Next.js", "Nuxt",
            "HTML", "CSS", "Sass", "Tailwind", "Bootstrap",
            "WordPress", "PHP", "Python", "Django", "FastAPI",
            "Git", "GitHub", "Docker", "AWS", "Vercel",
            "Figma", "Photoshop", "Illustrator",
            "ChatGPT", "Claude", "GitHub Copilot"
        ]
        
        found_techs = []
        content_lower = content.lower()
        
        for tech in tech_list:
            if tech.lower() in content_lower:
                found_techs.append(tech)
        
        return found_techs
    
    def _extract_achievements(self, content: str) -> List[str]:
        """達成事項を抽出"""
        patterns = [
            r'(?:完了|完成|できた|実装した|作成した).*?[:：](.+?)(?:\n|$)',
            r'(?:達成|クリア|解決).*?[:：](.+?)(?:\n|$)'
        ]
        
        achievements = []
        for pattern in patterns:
            matches = re.findall(pattern, content, re.MULTILINE)
            achievements.extend(matches)
        
        return achievements
    
    def _extract_learnings(self, content: str) -> List[str]:
        """学習ポイントを抽出"""
        patterns = [
            r'(?:学んだ|分かった|理解した|気づいた).*?[:：](.+?)(?:\n|$)',
            r'(?:ポイント|コツ|TIP).*?[:：](.+?)(?:\n|$)'
        ]
        
        learnings = []
        for pattern in patterns:
            matches = re.findall(pattern, content, re.MULTILINE)
            learnings.extend(matches)
        
        return learnings
    
    def _extract_metrics(self, content: str) -> Dict[str, any]:
        """数値データを抽出"""
        metrics = {}
        
        # 時間
        time_match = re.search(r'(\d+\.?\d*)\s*(?:時間|h)', content)
        if time_match:
            metrics["hours"] = float(time_match.group(1))
        
        # 件数
        count_match = re.search(r'(\d+)\s*件', content)
        if count_match:
            metrics["count"] = int(count_match.group(1))
        
        # パーセンテージ
        percent_match = re.search(r'(\d+\.?\d*)\s*%', content)
        if percent_match:
            metrics["percentage"] = float(percent_match.group(1))
        
        return metrics
    
    def save_questions_to_obsidian(self, author: str, questions: List[Dict]):
        """質問をObsidian形式で保存"""
        member_dir = self.members_path / author
        member_dir.mkdir(exist_ok=True)
        
        questions_dir = member_dir / "質問履歴"
        questions_dir.mkdir(exist_ok=True)
        
        # 月別ファイルに保存
        for question in questions:
            timestamp = question.get("timestamp", "")
            try:
                dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
                month = dt.strftime("%Y-%m")
            except:
                month = datetime.now().strftime("%Y-%m")
            
            file_path = questions_dir / f"{month}_質問.md"
            
            # 既存の内容を読み込む
            if file_path.exists():
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            else:
                content = f"# {author} - {month} 質問履歴\n\n"
            
            # 新しい質問を追加
            content += self._format_question(question)
            
            # 保存
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
        
        # FAQ/ナレッジベースを更新
        self._update_faq(questions)
    
    def save_progress_to_obsidian(self, author: str, progress_list: List[Dict]):
        """進捗報告をObsidian形式で保存"""
        member_dir = self.members_path / author
        member_dir.mkdir(exist_ok=True)
        
        progress_dir = member_dir / "進捗報告"
        progress_dir.mkdir(exist_ok=True)
        
        # 月別ファイルに保存
        for progress in progress_list:
            timestamp = progress.get("timestamp", "")
            try:
                dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
                month = dt.strftime("%Y-%m")
            except:
                month = datetime.now().strftime("%Y-%m")
            
            file_path = progress_dir / f"{month}_進捗.md"
            
            # 既存の内容を読み込む
            if file_path.exists():
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            else:
                content = f"# {author} - {month} 進捗報告\n\n"
            
            # 新しい進捗を追加
            content += self._format_progress(progress)
            
            # 保存
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
        
        # 成功事例集を更新
        self._update_success_stories(author, progress_list)
    
    def _format_question(self, question: Dict) -> str:
        """質問をマークダウン形式にフォーマット"""
        timestamp = question.get("timestamp", "")
        try:
            dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
            date_str = dt.strftime("%Y-%m-%d %H:%M")
        except:
            date_str = "日時不明"
        
        md = f"\n## {date_str}\n"
        md += f"**カテゴリ**: {question['category']}\n"
        md += f"**緊急度**: {question['urgency']}\n"
        md += f"**ステータス**: {question['status']}\n"
        
        if question['keywords']:
            md += f"**キーワード**: {', '.join(question['keywords'])}\n"
        
        if question['technologies']:
            md += f"**関連技術**: {', '.join(question['technologies'])}\n"
        
        md += f"\n### 質問内容\n"
        md += f"{question['content']}\n"
        md += f"\n---\n"
        
        return md
    
    def _format_progress(self, progress: Dict) -> str:
        """進捗報告をマークダウン形式にフォーマット"""
        timestamp = progress.get("timestamp", "")
        try:
            dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
            date_str = dt.strftime("%Y-%m-%d %H:%M")
        except:
            date_str = "日時不明"
        
        md = f"\n## {date_str}\n"
        
        if progress['achievements']:
            md += f"\n### 達成事項\n"
            for achievement in progress['achievements']:
                md += f"- {achievement}\n"
        
        if progress['learnings']:
            md += f"\n### 学んだこと\n"
            for learning in progress['learnings']:
                md += f"- {learning}\n"
        
        if progress['technologies']:
            md += f"\n### 使用技術\n"
            md += f"{', '.join(progress['technologies'])}\n"
        
        if progress['metrics']:
            md += f"\n### 数値データ\n"
            for key, value in progress['metrics'].items():
                md += f"- {key}: {value}\n"
        
        md += f"\n### 詳細\n"
        md += f"{progress['content']}\n"
        md += f"\n---\n"
        
        return md
    
    def _update_faq(self, questions: List[Dict]):
        """FAQを更新"""
        faq_path = self.knowledge_path / "よくある質問と回答.md"
        
        # カテゴリ別に質問を整理
        categorized = {}
        for q in questions:
            category = q['category']
            if category not in categorized:
                categorized[category] = []
            categorized[category].append(q)
        
        # 既存のFAQを読み込むか新規作成
        if faq_path.exists():
            # TODO: 既存のFAQとマージする高度なロジック
            pass
        else:
            content = "# グッサポ・ラボ よくある質問と回答\n\n"
            content += f"最終更新: {datetime.now().strftime('%Y-%m-%d')}\n\n"
            
            for category, questions in categorized.items():
                content += f"## {category}\n\n"
                for q in questions[:5]:  # 各カテゴリ最新5件
                    content += f"### Q: {q['content'][:100]}...\n"
                    content += f"- カテゴリ: {q['category']}\n"
                    content += f"- キーワード: {', '.join(q['keywords'][:5])}\n"
                    content += "\n"
            
            with open(faq_path, 'w', encoding='utf-8') as f:
                f.write(content)
    
    def _update_success_stories(self, author: str, progress_list: List[Dict]):
        """成功事例集を更新"""
        success_path = self.knowledge_path / "成功事例集.md"
        
        # 既存の成功事例を読み込むか新規作成
        if success_path.exists():
            with open(success_path, 'r', encoding='utf-8') as f:
                content = f.read()
        else:
            content = "# グッサポ・ラボ 成功事例集\n\n"
        
        # 新しい成功事例を追加
        for progress in progress_list:
            if progress['achievements']:
                content += f"\n## {author} - {datetime.now().strftime('%Y-%m-%d')}\n"
                content += "### 達成内容\n"
                for achievement in progress['achievements']:
                    content += f"- {achievement}\n"
                if progress['learnings']:
                    content += "\n### 学び\n"
                    for learning in progress['learnings']:
                        content += f"- {learning}\n"
                content += "\n---\n"
        
        with open(success_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    def process_all_questions_progress(self):
        """すべての未処理質問・進捗を処理"""
        processed_count = 0
        
        # 質問ファイルを処理
        question_files = list(self.inbox_path.glob("*_questions.json"))
        for file_path in question_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    questions = json.load(f)
                
                author = file_path.stem.replace("_questions", "")
                
                # 解析
                analyzed = self.analyze_questions(questions)
                
                # Obsidianに保存
                self.save_questions_to_obsidian(author, analyzed)
                
                # 処理済みファイルを削除
                file_path.unlink()
                
                processed_count += 1
                logger.info(f"Processed questions for {author}")
                
            except Exception as e:
                logger.error(f"Error processing {file_path}: {str(e)}")
        
        # 進捗ファイルを処理
        progress_files = list(self.inbox_path.glob("*_progress.json"))
        for file_path in progress_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    progress_list = json.load(f)
                
                author = file_path.stem.replace("_progress", "")
                
                # 解析
                analyzed = self.analyze_progress(progress_list)
                
                # Obsidianに保存
                self.save_progress_to_obsidian(author, analyzed)
                
                # 処理済みファイルを削除
                file_path.unlink()
                
                processed_count += 1
                logger.info(f"Processed progress for {author}")
                
            except Exception as e:
                logger.error(f"Error processing {file_path}: {str(e)}")
        
        return processed_count

if __name__ == "__main__":
    # テスト実行
    analyzer = QuestionProgressAnalyzer()
    count = analyzer.process_all_questions_progress()
    print(f"処理完了: {count}件のファイルを処理しました")