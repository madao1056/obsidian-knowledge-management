#!/usr/bin/env python3
"""
進捗報告から思考プロセスを抽出してプロファイルに追加
"""

import shutil
from pathlib import Path
import re
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ThinkingProcessExtractor:
    def __init__(self):
        self.support_path = Path(__file__).parent.parent / "03_Support" / "グッサポ・ラボ"
        self.members_path = self.support_path / "メンバー管理"
        
    def extract_and_consolidate(self):
        """日付別フォルダから思考プロセスを抽出して統合"""
        logger.info("思考プロセスの抽出を開始...")
        
        # メンバーごとの思考プロセスデータ
        member_thinking = {
            "yukari": [],
            "ログジ": [],
            "タカノリ": []
        }
        
        # 日付別フォルダを探索
        for folder in self.members_path.glob("*_2025-*"):
            if not folder.is_dir():
                continue
                
            # メンバー名を特定
            member_raw = folder.name.split("_")[0]
            member = self._normalize_member(member_raw)
            
            if not member:
                continue
                
            # 進捗報告を読み込み
            progress_files = list(folder.glob("進捗報告/*.md"))
            for progress_file in progress_files:
                try:
                    content = progress_file.read_text(encoding='utf-8')
                    
                    # 思考プロセスを抽出
                    thinking_data = self._extract_thinking_patterns(content)
                    if thinking_data:
                        thinking_data['date'] = folder.name.split("_")[-1]
                        member_thinking[member].append(thinking_data)
                        
                except Exception as e:
                    logger.error(f"エラー: {progress_file} - {e}")
        
        # プロファイルを更新
        for member, thinking_list in member_thinking.items():
            if thinking_list:
                self._update_profile(member, thinking_list)
        
        # 日付別フォルダを削除
        self._cleanup_date_folders()
        
        logger.info("✅ 思考プロセスの抽出と統合が完了")
    
    def _normalize_member(self, raw_name: str) -> str:
        """メンバー名を正規化"""
        if raw_name in ["yukari_web", "yukari"]:
            return "yukari"
        elif raw_name == "prog.ji":
            return "ログジ"
        elif raw_name == "takanori07":
            return "タカノリ"
        elif raw_name in ["gussan", "gussan_yoshinani"]:
            return None  # 除外
        return None
    
    def _extract_thinking_patterns(self, content: str) -> dict:
        """進捗報告から思考パターンを抽出"""
        patterns = {
            'pdca_approach': [],
            'problem_solving': [],
            'learning_points': [],
            'improvement_actions': [],
            'reflection_depth': 0
        }
        
        # PDCAアプローチの抽出
        if "PDCAサマリー" in content:
            patterns['pdca_approach'].append("PDCA思考を実践")
            patterns['reflection_depth'] += 2
        
        # 問題解決パターン
        if re.search(r'(課題|問題|詰まった|エラー|難しい)', content):
            problem_section = self._extract_section(content, r'(課題|問題|詰まった|エラー|難しい)')
            if problem_section:
                patterns['problem_solving'].append(problem_section[:100])
        
        # 学習ポイント
        if re.search(r'(学び|理解|わかった|気づき|発見)', content):
            learning_section = self._extract_section(content, r'(学び|理解|わかった|気づき|発見)')
            if learning_section:
                patterns['learning_points'].append(learning_section[:100])
                patterns['reflection_depth'] += 1
        
        # 改善アクション
        if re.search(r'(改善|次回|今後|対策|工夫)', content):
            improvement_section = self._extract_section(content, r'(改善|次回|今後|対策|工夫)')
            if improvement_section:
                patterns['improvement_actions'].append(improvement_section[:100])
                patterns['reflection_depth'] += 1
        
        # 振り返りの深さを評価
        if "録画" in content and "振り返り" in content:
            patterns['reflection_depth'] += 2
            patterns['pdca_approach'].append("録画による客観的振り返り")
        
        return patterns if any(patterns.values()) else None
    
    def _extract_section(self, content: str, pattern: str) -> str:
        """特定パターン周辺のテキストを抽出"""
        match = re.search(pattern, content)
        if match:
            start = max(0, match.start() - 50)
            end = min(len(content), match.end() + 150)
            return content[start:end].strip()
        return ""
    
    def _update_profile(self, member: str, thinking_list: list):
        """メンバープロファイルを更新"""
        profile_path = self.members_path / member / f"{member}_思考プロセス.md"
        
        content = f"""# {member} - 思考プロセス分析

## 🧠 思考の特徴

### PDCAサイクルの実践度
"""
        
        # PDCA実践の分析
        pdca_count = sum(1 for t in thinking_list if t.get('pdca_approach'))
        if pdca_count > 5:
            content += "- **高い**: PDCAサイクルを意識的に実践し、継続的改善を行っている\n"
        elif pdca_count > 2:
            content += "- **中程度**: PDCAを時々意識し、改善に取り組んでいる\n"
        else:
            content += "- **発展途上**: PDCAサイクルの定着に向けて成長中\n"
        
        content += "\n### 問題解決アプローチ\n"
        
        # 問題解決パターンの集約
        all_problems = []
        for t in thinking_list:
            all_problems.extend(t.get('problem_solving', []))
        
        if all_problems:
            unique_patterns = list(set([p[:50] for p in all_problems]))[:5]
            for pattern in unique_patterns:
                content += f"- {pattern}...\n"
        
        content += "\n### 学習と成長の傾向\n"
        
        # 学習ポイントの集約
        all_learnings = []
        for t in thinking_list:
            all_learnings.extend(t.get('learning_points', []))
        
        if all_learnings:
            content += "#### 主な学習テーマ:\n"
            unique_learnings = list(set([l[:50] for l in all_learnings]))[:5]
            for learning in unique_learnings:
                content += f"- {learning}...\n"
        
        # 振り返りの深さ
        avg_reflection = sum(t.get('reflection_depth', 0) for t in thinking_list) / max(len(thinking_list), 1)
        
        content += f"\n### 振り返りの深さ\n"
        if avg_reflection > 3:
            content += "- **深い**: 客観的な視点で詳細な振り返りを実施\n"
        elif avg_reflection > 1.5:
            content += "- **標準的**: 定期的な振り返りを実施\n"
        else:
            content += "- **浅い**: より深い振り返りの習慣化が必要\n"
        
        content += "\n## 💡 成長のための提案\n\n"
        
        # 個別アドバイス
        if avg_reflection < 2:
            content += "1. **振り返りの習慣化**: 毎日の活動後に5分間の振り返りタイムを設定\n"
        
        if pdca_count < 3:
            content += "2. **PDCAサイクルの強化**: Plan→Do→Check→Actionを意識的に実践\n"
        
        if len(all_problems) > len(all_learnings):
            content += "3. **学習の言語化**: 問題解決から得た学びを明文化する習慣をつける\n"
        
        content += f"\n---\n*分析日: {datetime.now().strftime('%Y年%m月%d日')}*\n"
        
        with open(profile_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        logger.info(f"💭 {member}_思考プロセス.md を作成")
    
    def _cleanup_date_folders(self):
        """日付別フォルダを削除"""
        for folder in self.members_path.glob("*_2025-*"):
            if folder.is_dir():
                try:
                    shutil.rmtree(folder)
                    logger.info(f"🗑️  {folder.name} を削除")
                except Exception as e:
                    logger.error(f"削除エラー: {folder} - {e}")

if __name__ == "__main__":
    extractor = ThinkingProcessExtractor()
    extractor.extract_and_consolidate()