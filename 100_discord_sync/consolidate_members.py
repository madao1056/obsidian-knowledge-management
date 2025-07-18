#!/usr/bin/env python3
"""
メンバー管理を整理・統合するスクリプト
- 同一人物（yukari_webとyukari）を統合
- 日付別ファイルを統合
- フォルダ構造をシンプル化
"""

import shutil
from pathlib import Path
import json
import re
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MemberConsolidator:
    def __init__(self):
        self.support_path = Path(__file__).parent.parent / "03_Support" / "グッサポ・ラボ"
        self.members_path = self.support_path / "メンバー管理"
        self.inbox_path = Path(__file__).parent.parent / "00_Inbox" / "discord"
        
        # 同一人物のマッピング
        self.member_mapping = {
            "yukari_web": "yukari",  # yukari_webをyukariに統合
            "gussan_yoshinani": "gussan",  # gussan関連は除外
            "prog.ji": "ログジ",
            "takanori07": "タカノリ"
        }
        
        # 除外するメンバー（gussanと関連アカウントは全て除外）
        self.exclude_members = ["gussan", "gussan_yoshinani"]
        
    def consolidate_all_members(self):
        """全メンバーのデータを統合"""
        logger.info("メンバー管理の整理を開始します...")
        
        # 1. 新しいフォルダ構造を作成
        self._create_new_structure()
        
        # 2. JSONファイルから統合データを作成
        self._consolidate_json_data()
        
        # 3. 既存の分散されたファイルを統合
        self._consolidate_existing_files()
        
        # 4. 統合レポートを生成
        self._generate_consolidated_reports()
        
        logger.info("✅ メンバー管理の整理が完了しました")
    
    def _create_new_structure(self):
        """新しいシンプルなフォルダ構造を作成"""
        target_members = ["yukari", "ログジ", "タカノリ"]
        
        for member in target_members:
            member_dir = self.members_path / member
            member_dir.mkdir(exist_ok=True)
            logger.info(f"📁 {member}フォルダを作成")
    
    def _consolidate_json_data(self):
        """JSONデータを統合"""
        # メンバーごとのデータを収集
        member_data = {
            "yukari": {
                "daily_reports": [],
                "questions": [],
                "progress": [],
                "self_introductions": []
            },
            "ログジ": {
                "daily_reports": [],
                "questions": [],
                "progress": [],
                "self_introductions": []
            },
            "タカノリ": {
                "daily_reports": [],
                "questions": [],
                "progress": [],
                "self_introductions": []
            }
        }
        
        # JSONファイルを読み込んで統合
        for json_file in self.inbox_path.glob("*.json"):
            try:
                # ファイル名からメンバー名を抽出
                filename_parts = json_file.stem.split("_")
                if len(filename_parts) < 3:
                    continue
                    
                raw_member = filename_parts[0]
                
                # 除外メンバーはスキップ（gussanを含む）
                if raw_member in self.exclude_members or "gussan" in raw_member.lower():
                    continue
                
                # メンバー名を正規化
                normalized_member = self._normalize_member_name(raw_member)
                if not normalized_member or normalized_member not in member_data:
                    continue
                
                # データを読み込み
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                # データタイプを判定
                data_type = self._determine_data_type(json_file.stem)
                
                # 配列の場合は展開
                if isinstance(data, list):
                    member_data[normalized_member][data_type].extend(data)
                else:
                    member_data[normalized_member][data_type].append(data)
                
                logger.info(f"📄 {json_file.name} → {normalized_member}/{data_type}")
                
            except Exception as e:
                logger.error(f"エラー: {json_file} - {e}")
        
        # 統合データを保存
        self._save_consolidated_data(member_data)
    
    def _normalize_member_name(self, raw_name: str) -> str:
        """メンバー名を正規化"""
        # gussanは除外
        if "gussan" in raw_name.lower():
            return None
        elif raw_name in ["yukari_web", "yukari"]:
            return "yukari"
        elif raw_name == "prog.ji":
            return "ログジ"
        elif raw_name == "takanori07":
            return "タカノリ"
        else:
            return None
    
    def _determine_data_type(self, filename: str) -> str:
        """ファイル名からデータタイプを判定"""
        if "daily_report" in filename or "日報" in filename:
            return "daily_reports"
        elif "question" in filename or "質問" in filename:
            return "questions"
        elif "progress" in filename or "進捗" in filename:
            return "progress"
        elif "自己紹介" in filename:
            return "self_introductions"
        else:
            return "daily_reports"  # デフォルト
    
    def _save_consolidated_data(self, member_data: dict):
        """統合データを各メンバーフォルダに保存"""
        for member, data in member_data.items():
            member_dir = self.members_path / member
            
            # 統合レポートを作成
            self._create_member_overview(member, data)
            
            # 全活動履歴を1つのファイルに
            self._create_activity_log(member, data)
            
            # 質問集を作成
            if data["questions"]:
                self._create_question_collection(member, data["questions"])
            
            # 進捗記録を作成
            if data["progress"]:
                self._create_progress_log(member, data["progress"])
    
    def _create_member_overview(self, member: str, data: dict):
        """メンバー概要ファイルを作成"""
        overview_path = self.members_path / member / f"{member}_概要.md"
        
        # 統計情報を計算
        total_reports = len(data["daily_reports"])
        total_questions = len(data["questions"])
        total_progress = len(data["progress"])
        
        # 活動期間を特定
        all_dates = []
        for category in data.values():
            for item in category:
                if isinstance(item, dict) and "timestamp" in item:
                    try:
                        dt = datetime.fromisoformat(item["timestamp"].replace('Z', '+00:00'))
                        all_dates.append(dt)
                    except:
                        pass
        
        if all_dates:
            start_date = min(all_dates).strftime("%Y年%m月%d日")
            end_date = max(all_dates).strftime("%Y年%m月%d日")
        else:
            start_date = end_date = "不明"
        
        # 概要マークダウンを生成
        content = f"""# {member} - メンバー概要

## 📊 活動サマリー

### 基本情報
- **活動期間**: {start_date} 〜 {end_date}
- **総日報数**: {total_reports}件
- **総質問数**: {total_questions}件
- **進捗報告**: {total_progress}件

### 主な活動内容
"""
        
        # 最近の活動を抽出
        recent_activities = self._extract_recent_activities(data)
        for activity in recent_activities[:5]:
            content += f"- {activity}\n"
        
        content += """
## 📈 成長の軌跡

### スキル・技術
"""
        # 技術キーワードを抽出
        tech_keywords = self._extract_tech_keywords(data)
        for tech in tech_keywords[:10]:
            content += f"- {tech}\n"
        
        content += """
## 🎯 サポートポイント

### よくある質問テーマ
"""
        # 質問の傾向を分析
        question_themes = self._analyze_question_themes(data["questions"])
        for theme in question_themes[:5]:
            content += f"- {theme}\n"
        
        content += """
## 📝 関連ドキュメント

- [活動履歴](活動履歴.md)
- [質問集](質問集.md)
- [進捗記録](進捗記録.md)
- [月報一覧](月報/)

---
*最終更新: """ + datetime.now().strftime("%Y年%m月%d日") + "*"
        
        with open(overview_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        logger.info(f"📋 {member}_概要.md を作成")
    
    def _create_activity_log(self, member: str, data: dict):
        """全活動履歴を1つのファイルに統合"""
        log_path = self.members_path / member / "活動履歴.md"
        
        content = f"# {member} - 活動履歴\n\n"
        
        # すべての活動を時系列でマージ
        all_activities = []
        
        for report in data["daily_reports"]:
            if isinstance(report, dict):
                all_activities.append({
                    "type": "日報",
                    "timestamp": report.get("timestamp", ""),
                    "content": report.get("content", ""),
                    "data": report
                })
        
        for question in data["questions"]:
            if isinstance(question, dict):
                all_activities.append({
                    "type": "質問",
                    "timestamp": question.get("timestamp", ""),
                    "content": question.get("content", ""),
                    "data": question
                })
        
        for progress in data["progress"]:
            if isinstance(progress, dict):
                all_activities.append({
                    "type": "進捗",
                    "timestamp": progress.get("timestamp", ""),
                    "content": progress.get("content", ""),
                    "data": progress
                })
        
        # タイムスタンプでソート
        all_activities.sort(key=lambda x: x["timestamp"], reverse=True)
        
        # 月ごとにグループ化
        monthly_groups = {}
        for activity in all_activities:
            try:
                dt = datetime.fromisoformat(activity["timestamp"].replace('Z', '+00:00'))
                month_key = dt.strftime("%Y年%m月")
                
                if month_key not in monthly_groups:
                    monthly_groups[month_key] = []
                monthly_groups[month_key].append(activity)
            except:
                pass
        
        # 月ごとに出力
        for month, activities in sorted(monthly_groups.items(), reverse=True):
            content += f"## {month}\n\n"
            
            for activity in activities:
                try:
                    dt = datetime.fromisoformat(activity["timestamp"].replace('Z', '+00:00'))
                    date_str = dt.strftime("%m/%d")
                    time_str = dt.strftime("%H:%M")
                    
                    content += f"### {date_str} {time_str} - {activity['type']}\n\n"
                    
                    # コンテンツを整形
                    activity_content = activity["content"]
                    if activity_content:
                        # 長すぎる場合は要約
                        if len(activity_content) > 500:
                            activity_content = activity_content[:500] + "..."
                        
                        content += activity_content + "\n\n"
                        
                        # 重要な数値を抽出
                        numbers = self._extract_important_numbers(activity_content)
                        if numbers:
                            content += "**数値データ**: " + ", ".join(numbers) + "\n\n"
                    
                    content += "---\n\n"
                    
                except Exception as e:
                    logger.error(f"活動ログエラー: {e}")
        
        with open(log_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        logger.info(f"📜 {member}/活動履歴.md を作成")
    
    def _create_question_collection(self, member: str, questions: list):
        """質問集を作成"""
        questions_path = self.members_path / member / "質問集.md"
        
        content = f"# {member} - 質問集\n\n"
        content += "これまでの質問とその解決状況をまとめています。\n\n"
        
        # カテゴリ別に分類
        categorized = {
            "技術": [],
            "営業": [],
            "案件": [],
            "その他": []
        }
        
        for q in questions:
            if isinstance(q, dict):
                q_content = q.get("content", "").lower()
                
                if any(word in q_content for word in ["実装", "エラー", "コード", "css", "javascript"]):
                    categorized["技術"].append(q)
                elif any(word in q_content for word in ["営業", "クライアント", "案件獲得"]):
                    categorized["営業"].append(q)
                elif any(word in q_content for word in ["納期", "案件", "対応"]):
                    categorized["案件"].append(q)
                else:
                    categorized["その他"].append(q)
        
        # カテゴリごとに出力
        for category, items in categorized.items():
            if items:
                content += f"## {category}関連（{len(items)}件）\n\n"
                
                for i, q in enumerate(items[:20], 1):  # 各カテゴリ最大20件
                    try:
                        dt = datetime.fromisoformat(q["timestamp"].replace('Z', '+00:00'))
                        date_str = dt.strftime("%Y/%m/%d")
                        
                        content += f"### {i}. {date_str}\n\n"
                        
                        q_content = q.get("content", "")
                        if len(q_content) > 300:
                            q_content = q_content[:300] + "..."
                        
                        content += f"{q_content}\n\n"
                        
                        # 解決状態
                        status = q.get("status", "open")
                        if status == "open":
                            content += "**状態**: 🔵 未解決\n\n"
                        else:
                            content += "**状態**: ✅ 解決済み\n\n"
                        
                    except:
                        pass
                
                content += "---\n\n"
        
        with open(questions_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        logger.info(f"❓ {member}/質問集.md を作成")
    
    def _create_progress_log(self, member: str, progress_list: list):
        """進捗記録を作成"""
        progress_path = self.members_path / member / "進捗記録.md"
        
        content = f"# {member} - 進捗記録\n\n"
        content += "完了した作業と成果をまとめています。\n\n"
        
        # 月ごとにグループ化
        monthly_progress = {}
        
        for p in progress_list:
            if isinstance(p, dict):
                try:
                    dt = datetime.fromisoformat(p["timestamp"].replace('Z', '+00:00'))
                    month_key = dt.strftime("%Y年%m月")
                    
                    if month_key not in monthly_progress:
                        monthly_progress[month_key] = []
                    monthly_progress[month_key].append(p)
                except:
                    pass
        
        # 月ごとに出力
        for month, items in sorted(monthly_progress.items(), reverse=True):
            content += f"## {month}\n\n"
            
            for p in items:
                try:
                    dt = datetime.fromisoformat(p["timestamp"].replace('Z', '+00:00'))
                    date_str = dt.strftime("%m/%d")
                    
                    content += f"### {date_str}\n\n"
                    
                    p_content = p.get("content", "")
                    if p_content:
                        content += p_content + "\n\n"
                    
                except:
                    pass
            
            content += "---\n\n"
        
        with open(progress_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        logger.info(f"✅ {member}/進捗記録.md を作成")
    
    def _consolidate_existing_files(self):
        """既存の分散されたファイルを統合"""
        # yukari_webフォルダの内容をyukariに移動
        yukari_web_path = self.members_path / "yukari_web"
        yukari_path = self.members_path / "yukari"
        
        if yukari_web_path.exists():
            # 月報を移動
            if (yukari_web_path / "月報").exists():
                for file in (yukari_web_path / "月報").glob("*.md"):
                    target_dir = yukari_path / "月報"
                    target_dir.mkdir(exist_ok=True)
                    shutil.copy2(file, target_dir / file.name)
                    logger.info(f"📋 {file.name} をyukariフォルダに統合")
            
            # yukari_webフォルダを削除
            shutil.rmtree(yukari_web_path)
            logger.info("🗑️  yukari_webフォルダを削除")
        
        # 日付別フォルダを統合（必要に応じて）
        for member_dir in self.members_path.iterdir():
            if (member_dir.is_dir() and 
                member_dir.name not in self.exclude_members and 
                "gussan" not in member_dir.name.lower()):
                self._cleanup_date_folders(member_dir)
    
    def _cleanup_date_folders(self, member_dir: Path):
        """日付別フォルダを統合"""
        # gussanフォルダがあれば削除
        if member_dir.name in ["gussan", "gussan_yoshinani"] or "gussan" in member_dir.name.lower():
            shutil.rmtree(member_dir)
            logger.info(f"🗑️  {member_dir.name}フォルダを削除")
            return
        
        # 日報、質問履歴、進捗報告などの日付別フォルダを確認
        date_pattern = re.compile(r'\d{4}-\d{2}-\d{2}')
        
        for subfolder in member_dir.iterdir():
            if subfolder.is_dir() and date_pattern.match(subfolder.name):
                # 日付フォルダの内容を親フォルダに移動
                for file in subfolder.glob("*"):
                    target = member_dir / file.name
                    if not target.exists():
                        shutil.move(str(file), str(target))
                
                # 空の日付フォルダを削除
                if not list(subfolder.iterdir()):
                    subfolder.rmdir()
                    logger.info(f"🗑️  {subfolder.name} を削除")
    
    def _extract_recent_activities(self, data: dict) -> list:
        """最近の活動を抽出"""
        activities = []
        
        # 最新の日報から
        for report in data["daily_reports"][-5:]:
            if isinstance(report, dict):
                content = report.get("content", "")
                # 最初の意味のある行を抽出
                lines = content.split('\n')
                for line in lines:
                    if line.strip() and len(line) > 10:
                        activities.append(line.strip()[:100])
                        break
        
        return activities
    
    def _extract_tech_keywords(self, data: dict) -> list:
        """技術キーワードを抽出"""
        tech_keywords = set()
        tech_list = [
            "HTML", "CSS", "JavaScript", "TypeScript", "React", "Vue", "Next.js",
            "WordPress", "PHP", "Python", "Git", "GitHub", "Figma", "AI", "ChatGPT"
        ]
        
        # すべてのテキストから技術キーワードを検索
        all_text = ""
        for category in data.values():
            for item in category:
                if isinstance(item, dict):
                    all_text += item.get("content", "") + " "
        
        all_text_lower = all_text.lower()
        for tech in tech_list:
            if tech.lower() in all_text_lower:
                tech_keywords.add(tech)
        
        return sorted(list(tech_keywords))
    
    def _analyze_question_themes(self, questions: list) -> list:
        """質問のテーマを分析"""
        themes = []
        theme_counts = {}
        
        theme_keywords = {
            "実装・コーディング": ["実装", "コード", "エラー", "動作", "書き方"],
            "デザイン・UI": ["デザイン", "figma", "レイアウト", "css"],
            "営業・クライアント対応": ["営業", "クライアント", "提案", "返信"],
            "WordPress関連": ["wordpress", "wp", "プラグイン"],
            "Git・バージョン管理": ["git", "github", "コミット", "プッシュ"],
            "AI活用": ["ai", "chatgpt", "gpt", "claude"]
        }
        
        for q in questions:
            if isinstance(q, dict):
                content = q.get("content", "").lower()
                for theme, keywords in theme_keywords.items():
                    if any(keyword in content for keyword in keywords):
                        theme_counts[theme] = theme_counts.get(theme, 0) + 1
        
        # 多い順にソート
        sorted_themes = sorted(theme_counts.items(), key=lambda x: x[1], reverse=True)
        return [f"{theme}（{count}件）" for theme, count in sorted_themes]
    
    def _extract_important_numbers(self, content: str) -> list:
        """重要な数値を抽出"""
        numbers = []
        
        # 時間
        time_matches = re.findall(r'(\d+\.?\d*)\s*時間', content)
        for match in time_matches:
            numbers.append(f"{match}時間")
        
        # 件数
        count_matches = re.findall(r'(\d+)\s*件', content)
        for match in count_matches:
            numbers.append(f"{match}件")
        
        # 金額
        money_matches = re.findall(r'(\d+(?:,\d{3})*)\s*円', content)
        for match in money_matches:
            numbers.append(f"{match}円")
        
        return numbers[:5]  # 最大5個
    
    def _generate_consolidated_reports(self):
        """統合レポートを生成"""
        summary_path = self.support_path / "メンバー管理サマリー.md"
        
        content = """# グッサポ・ラボ メンバー管理サマリー

## 📊 概要

このフォルダには、グッサポ・ラボのメンバー（gussanを除く）の活動記録が整理されています。

## 👥 メンバー一覧

### [yukari](メンバー管理/yukari/yukari_概要.md)
- Web制作フリーランス
- 主な活動: 営業活動、案件対応、技術学習

### [ログジ](メンバー管理/ログジ/ログジ_概要.md)
- 元製造業からWeb制作へ転向
- 主な活動: 積極的な営業活動、AI活用の研究

### [タカノリ](メンバー管理/タカノリ/タカノリ_概要.md)
- Web制作者
- 主な活動: 案件対応、技術向上

## 📁 フォルダ構成

```
メンバー管理/
├── yukari/
│   ├── yukari_概要.md      # メンバー概要
│   ├── 活動履歴.md         # 全活動の時系列記録
│   ├── 質問集.md           # 質問と回答の集約
│   ├── 進捗記録.md         # 完了タスクと成果
│   └── 月報/               # 月次レポート
├── ログジ/
│   └── （同様の構成）
└── タカノリ/
    └── （同様の構成）
```

## 🔄 更新方法

1. Discord連携で新しいデータを収集
2. `venv/bin/python consolidate_members.py` を実行
3. 月報は `venv/bin/python monthly_report_analyzer.py` で生成

---
*最終更新: """ + datetime.now().strftime("%Y年%m月%d日") + "*"
        
        with open(summary_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        logger.info("📊 メンバー管理サマリー.md を作成")

if __name__ == "__main__":
    consolidator = MemberConsolidator()
    consolidator.consolidate_all_members()