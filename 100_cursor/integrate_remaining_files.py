#!/usr/bin/env python3
"""
Knowledge_Baseに未統合のNotionファイルを統合するスクリプト
"""
import os
import shutil
import re
import hashlib
from pathlib import Path
from datetime import datetime

# 設定
BASE_DIR = "/Users/hashiguchimasaki/project/obsidian"
NOTION_DIR = os.path.join(BASE_DIR, "20_Literature/25_Notion")
KNOWLEDGE_BASE_DIR = os.path.join(BASE_DIR, "10_Projects/Knowledge_Base")

# 既存カテゴリ定義
CATEGORIES = {
    "よしなに対応": {
        "keywords": ["よしなに", "対応", "巻き取", "先回り", "相手目線", "提案", "質問力"],
        "dir": "01_よしなに対応",
        "priority": 1
    },
    "Web制作": {
        "keywords": ["WordPress", "HTML", "CSS", "JavaScript", "PHP", "コーディング", "デザイン", "実装", "レスポンシブ", "サイト"],
        "dir": "02_Web制作",
        "priority": 2
    },
    "マーケティング": {
        "keywords": ["マーケティング", "集客", "SNS", "SEO", "広告", "分析", "戦略", "アクセス", "CVR", "CTR"],
        "dir": "03_マーケティング",
        "priority": 3
    },
    "ビジネス": {
        "keywords": ["ビジネス", "経営", "単価", "営業", "契約", "案件", "クライアント", "売上", "収益", "請求"],
        "dir": "04_ビジネス",
        "priority": 4
    },
    "学習・成長": {
        "keywords": ["学習", "成長", "スキル", "勉強", "習慣", "改善", "PDCA", "目標", "計画", "振り返り"],
        "dir": "05_学習・成長",
        "priority": 5
    },
    "グッサポ・ラボ": {
        "keywords": ["グッサポ", "ラボ", "サポート", "コミュニティ", "Discord", "メンバー", "運営", "コンサル"],
        "dir": "06_グッサポ・ラボ",
        "priority": 6
    },
    "プロジェクト": {
        "keywords": ["プロジェクト", "案件", "制作", "納品", "修正", "進捗", "管理", "スケジュール"],
        "dir": "07_プロジェクト",
        "priority": 7
    },
    "日記・雑記": {
        "keywords": ["日記", "雑記", "思考", "メモ", "アイデア", "備忘録", "記録"],
        "dir": "08_日記・雑記",
        "priority": 8
    },
    "その他": {
        "keywords": [],
        "dir": "99_その他",
        "priority": 99
    }
}

class RemainingFilesIntegrator:
    def __init__(self):
        self.integrated_files = set()
        self.remaining_files = []
        self.integration_stats = {}
        
    def find_integrated_files(self):
        """既に統合済みのファイル名を収集"""
        print("統合済みファイルを確認中...")
        
        for root, dirs, files in os.walk(KNOWLEDGE_BASE_DIR):
            for filename in files:
                if filename.endswith('.md') and filename != 'README.md':
                    self.integrated_files.add(filename)
        
        print(f"統合済みファイル数: {len(self.integrated_files)}")
    
    def find_remaining_files(self):
        """未統合のファイルを特定"""
        print("未統合ファイルを特定中...")
        
        for root, dirs, files in os.walk(NOTION_DIR):
            for filename in files:
                if filename.endswith('.md') and not filename.startswith('.'):
                    if filename not in self.integrated_files:
                        filepath = os.path.join(root, filename)
                        self.remaining_files.append(filepath)
        
        print(f"未統合ファイル数: {len(self.remaining_files)}")
        return len(self.remaining_files)
    
    def analyze_file_content(self, filepath):
        """ファイル内容を分析してカテゴリを決定"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            filename = os.path.basename(filepath)
            
            # プレースホルダーファイルかチェック
            if len(content) < 200 or 'placeholder file from Notion' in content:
                return None, 0  # スキップ
            
            # 日付パターンをチェック（日記系）
            date_patterns = [
                r'\d{4}\.\d{1,2}\.\d{1,2}',
                r'\d{4}-\d{1,2}-\d{1,2}',
                r'\d{4}\年\d{1,2}\月\d{1,2}\日',
                r'\d{1,2}月\d{1,2}日'
            ]
            
            for pattern in date_patterns:
                if re.search(pattern, filename):
                    return "日記・雑記", 5
            
            # カテゴリスコアリング
            best_category = "その他"
            best_score = 0
            
            for category, cat_info in CATEGORIES.items():
                if category == "その他":
                    continue
                
                score = 0
                for keyword in cat_info["keywords"]:
                    # ファイル名での一致（重み大）
                    if keyword.lower() in filename.lower():
                        score += 10
                    # 内容での一致
                    if keyword.lower() in content.lower():
                        score += 1
                
                # 優先度を考慮
                adjusted_score = score / cat_info["priority"]
                
                if adjusted_score > best_score:
                    best_score = adjusted_score
                    best_category = category
            
            return best_category, best_score
            
        except Exception as e:
            print(f"ファイル分析エラー {filepath}: {e}")
            return None, 0
    
    def integrate_files(self):
        """ファイルを適切なカテゴリに統合"""
        print("\nファイル統合を開始...")
        
        # カテゴリディレクトリ作成
        for category, info in CATEGORIES.items():
            category_dir = os.path.join(KNOWLEDGE_BASE_DIR, info["dir"])
            os.makedirs(category_dir, exist_ok=True)
        
        integrated_count = 0
        skipped_count = 0
        
        for i, filepath in enumerate(self.remaining_files):
            if i % 50 == 0:
                print(f"進捗: {i}/{len(self.remaining_files)} ({i/len(self.remaining_files)*100:.1f}%)")
            
            category, score = self.analyze_file_content(filepath)
            
            if category is None:
                skipped_count += 1
                continue
            
            # ファイルをコピー
            filename = os.path.basename(filepath)
            category_info = CATEGORIES[category]
            target_dir = os.path.join(KNOWLEDGE_BASE_DIR, category_info["dir"])
            target_path = os.path.join(target_dir, filename)
            
            try:
                # 重複チェック
                if os.path.exists(target_path):
                    # ファイル内容を比較
                    if self.files_are_identical(filepath, target_path):
                        skipped_count += 1
                        continue
                    else:
                        # 異なる内容の場合は番号付きで保存
                        base_name, ext = os.path.splitext(filename)
                        counter = 1
                        while os.path.exists(target_path):
                            new_filename = f"{base_name}_{counter}{ext}"
                            target_path = os.path.join(target_dir, new_filename)
                            counter += 1
                
                shutil.copy2(filepath, target_path)
                integrated_count += 1
                
                # 統計更新
                if category not in self.integration_stats:
                    self.integration_stats[category] = 0
                self.integration_stats[category] += 1
                
            except Exception as e:
                print(f"コピーエラー {filepath}: {e}")
        
        print(f"\n統合完了:")
        print(f"  統合済み: {integrated_count}ファイル")
        print(f"  スキップ: {skipped_count}ファイル")
        
        return integrated_count
    
    def files_are_identical(self, file1, file2):
        """2つのファイルが同一かチェック"""
        try:
            with open(file1, 'r', encoding='utf-8') as f1:
                content1 = f1.read()
            with open(file2, 'r', encoding='utf-8') as f2:
                content2 = f2.read()
            
            # コンテンツハッシュで比較
            hash1 = hashlib.md5(content1.encode()).hexdigest()
            hash2 = hashlib.md5(content2.encode()).hexdigest()
            
            return hash1 == hash2
        except:
            return False
    
    def update_category_indexes(self):
        """カテゴリ別READMEを更新"""
        print("\nカテゴリインデックスを更新中...")
        
        for category, info in CATEGORIES.items():
            category_dir = os.path.join(KNOWLEDGE_BASE_DIR, info["dir"])
            if not os.path.exists(category_dir):
                continue
            
            # カテゴリ内のファイル一覧取得
            category_files = []
            for filename in os.listdir(category_dir):
                if filename.endswith('.md') and filename != 'README.md':
                    category_files.append(filename)
            
            if not category_files:
                continue
            
            # README.md更新
            readme_path = os.path.join(category_dir, "README.md")
            
            content = f"# {category}\n\n"
            content += f"このカテゴリには {len(category_files)} 件のドキュメントがあります。\n\n"
            
            if info['keywords']:
                content += f"**関連キーワード**: {', '.join(info['keywords'])}\n\n"
            
            content += "## ドキュメント一覧\n\n"
            
            # ファイルリスト（アルファベット順）
            category_files.sort()
            for filename in category_files:
                title = filename.replace('.md', '')
                content += f"- [[{filename}|{title}]]\n"
            
            content += f"\n---\n最終更新: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(content)
    
    def update_main_index(self):
        """メインインデックスを更新"""
        print("メインインデックスを更新中...")
        
        # カテゴリ別統計
        category_stats = {}
        total_files = 0
        
        for category, info in CATEGORIES.items():
            category_dir = os.path.join(KNOWLEDGE_BASE_DIR, info["dir"])
            if os.path.exists(category_dir):
                count = len([f for f in os.listdir(category_dir) 
                           if f.endswith('.md') and f != 'README.md'])
                category_stats[category] = count
                total_files += count
        
        # メインREADME更新
        index_path = os.path.join(KNOWLEDGE_BASE_DIR, "00_Index", "README.md")
        
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 統計部分を更新
        stats_pattern = r'- \*\*総統合ファイル数\*\*: \d+ファイル'
        new_stats = f"- **総統合ファイル数**: {total_files}ファイル"
        content = re.sub(stats_pattern, new_stats, content)
        
        # カテゴリ別統計も更新
        for category, count in category_stats.items():
            if count > 0:
                info = CATEGORIES[category]
                pattern = f'- \\*\\*\\[\\[\\.\\./{re.escape(info["dir"])}/README\\.md\\|{re.escape(category)}\\]\\]\\*\\* \\(\\d+ファイル\\)'
                replacement = f'- **[[../{info["dir"]}/README.md|{category}]]** ({count}ファイル)'
                content = re.sub(pattern, replacement, content)
        
        # 更新日時を更新
        content = re.sub(r'最終更新: \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', 
                        f'最終更新: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}', content)
        
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    def generate_integration_report(self):
        """統合レポートを生成"""
        report_path = os.path.join(KNOWLEDGE_BASE_DIR, "00_Index", "Remaining_Files_Integration_Report.md")
        
        content = f"""# 未統合ファイル統合レポート

生成日時: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 統合結果

### カテゴリ別統合数
"""
        
        for category, count in sorted(self.integration_stats.items(), key=lambda x: x[1], reverse=True):
            content += f"- {category}: {count}ファイル\n"
        
        total_integrated = sum(self.integration_stats.values())
        content += f"\n**総統合数**: {total_integrated}ファイル\n"
        
        content += f"""
## 統合前後の状況

- **統合前**: 約639ファイルが未統合
- **統合後**: {total_integrated}ファイルを統合
- **Knowledge Base総ファイル数**: 更新済み

## 今回の統合で追加されたカテゴリ

- **日記・雑記**: 日付形式ファイルや個人的メモ
- 既存カテゴリの拡充

---
この統合により、Notionから取得したほぼ全てのファイルがKnowledge_Baseに整理されました。
"""
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"統合レポート作成: {report_path}")

def main():
    print("=" * 60)
    print("未統合Notionファイルの統合処理")
    print("=" * 60)
    
    integrator = RemainingFilesIntegrator()
    
    # 1. 統合済みファイルを特定
    integrator.find_integrated_files()
    
    # 2. 未統合ファイルを特定
    remaining_count = integrator.find_remaining_files()
    
    if remaining_count == 0:
        print("未統合ファイルは見つかりませんでした。")
        return
    
    # 3. ファイル統合
    integrated_count = integrator.integrate_files()
    
    # 4. インデックス更新
    integrator.update_category_indexes()
    integrator.update_main_index()
    
    # 5. レポート生成
    integrator.generate_integration_report()
    
    print("\n" + "=" * 60)
    print(f"統合処理完了！ {integrated_count}ファイルを統合しました。")
    print("=" * 60)

if __name__ == "__main__":
    main()