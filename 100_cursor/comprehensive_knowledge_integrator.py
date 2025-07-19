#!/usr/bin/env python3
"""
Notionから取得したすべての知識を統合し、最適な知識ベースを構築するスクリプト
"""
import os
import re
import json
import shutil
from datetime import datetime
from pathlib import Path
import hashlib

# 設定
BASE_DIR = "/Users/hashiguchimasaki/project/obsidian"
NOTION_DIR = os.path.join(BASE_DIR, "20_Literature/25_Notion")
KNOWLEDGE_BASE_DIR = os.path.join(BASE_DIR, "10_Projects/Knowledge_Base")
BACKUP_DIR = os.path.join(BASE_DIR, "99_Archive/Notion_Backup_" + datetime.now().strftime("%Y%m%d"))

# カテゴリ定義
CATEGORIES = {
    "よしなに対応": {
        "keywords": ["よしなに", "対応", "巻き取", "先回り", "相手目線", "提案", "質問力"],
        "dir": "01_よしなに対応",
        "priority": 1
    },
    "Web制作": {
        "keywords": ["WordPress", "HTML", "CSS", "JavaScript", "PHP", "コーディング", "デザイン", "実装"],
        "dir": "02_Web制作",
        "priority": 2
    },
    "マーケティング": {
        "keywords": ["マーケティング", "集客", "SNS", "SEO", "広告", "分析", "戦略"],
        "dir": "03_マーケティング",
        "priority": 3
    },
    "ビジネス": {
        "keywords": ["ビジネス", "経営", "単価", "営業", "契約", "案件", "クライアント"],
        "dir": "04_ビジネス",
        "priority": 4
    },
    "学習・成長": {
        "keywords": ["学習", "成長", "スキル", "勉強", "習慣", "改善", "PDCA"],
        "dir": "05_学習・成長",
        "priority": 5
    },
    "グッサポ・ラボ": {
        "keywords": ["グッサポ", "ラボ", "サポート", "コミュニティ", "Discord"],
        "dir": "06_グッサポ・ラボ",
        "priority": 6
    },
    "プロジェクト": {
        "keywords": ["プロジェクト", "案件", "制作", "納品", "修正", "進捗"],
        "dir": "07_プロジェクト",
        "priority": 7
    },
    "その他": {
        "keywords": [],
        "dir": "99_その他",
        "priority": 99
    }
}

class KnowledgeIntegrator:
    def __init__(self):
        self.file_index = {}
        self.content_hashes = {}
        self.relations = {}
        self.tags = {}
        
    def create_directories(self):
        """必要なディレクトリ構造を作成"""
        print("Creating directory structure...")
        
        # バックアップディレクトリ
        os.makedirs(BACKUP_DIR, exist_ok=True)
        
        # 知識ベースディレクトリ
        os.makedirs(KNOWLEDGE_BASE_DIR, exist_ok=True)
        
        # カテゴリディレクトリ
        for category, info in CATEGORIES.items():
            category_dir = os.path.join(KNOWLEDGE_BASE_DIR, info["dir"])
            os.makedirs(category_dir, exist_ok=True)
        
        # 特別なディレクトリ
        os.makedirs(os.path.join(KNOWLEDGE_BASE_DIR, "00_Index"), exist_ok=True)
        os.makedirs(os.path.join(KNOWLEDGE_BASE_DIR, "00_Templates"), exist_ok=True)
        
    def backup_existing_files(self):
        """既存のNotionファイルをバックアップ"""
        print("Backing up existing files...")
        
        if os.path.exists(NOTION_DIR):
            # Notionディレクトリ全体をバックアップ
            backup_path = os.path.join(BACKUP_DIR, "25_Notion")
            shutil.copytree(NOTION_DIR, backup_path, dirs_exist_ok=True)
            print(f"  Backed up to: {backup_path}")
    
    def scan_all_files(self):
        """すべてのマークダウンファイルをスキャン"""
        print("\nScanning all markdown files...")
        
        file_count = 0
        for root, dirs, files in os.walk(NOTION_DIR):
            for filename in files:
                if filename.endswith('.md') and not filename.startswith('.'):
                    filepath = os.path.join(root, filename)
                    relative_path = os.path.relpath(filepath, NOTION_DIR)
                    
                    # ファイルの内容を読み込み
                    try:
                        with open(filepath, 'r', encoding='utf-8') as f:
                            content = f.read()
                        
                        # コンテンツハッシュを計算（重複チェック用）
                        content_hash = hashlib.md5(content.encode()).hexdigest()
                        
                        # メタデータを抽出
                        metadata = self.extract_metadata(content)
                        
                        # インデックスに追加
                        self.file_index[filepath] = {
                            "relative_path": relative_path,
                            "filename": filename,
                            "content_hash": content_hash,
                            "metadata": metadata,
                            "category": None,
                            "tags": [],
                            "relations": []
                        }
                        
                        file_count += 1
                        
                    except Exception as e:
                        print(f"  Error reading {filepath}: {e}")
        
        print(f"  Found {file_count} files")
        return file_count
    
    def extract_metadata(self, content):
        """ファイルからメタデータを抽出"""
        metadata = {}
        
        # YAMLフロントマターを抽出
        yaml_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
        if yaml_match:
            yaml_content = yaml_match.group(1)
            
            # 簡易的なYAMLパース
            for line in yaml_content.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    metadata[key.strip()] = value.strip()
        
        # タイトルを抽出
        title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if title_match:
            metadata['title'] = title_match.group(1).strip()
        
        # プレースホルダーかどうか
        metadata['is_placeholder'] = 'placeholder file from Notion' in content
        
        # コンテンツの長さ
        metadata['content_length'] = len(content)
        
        return metadata
    
    def categorize_files(self):
        """ファイルをカテゴリに分類"""
        print("\nCategorizing files...")
        
        for filepath, file_info in self.file_index.items():
            filename = file_info['filename']
            content = self.read_file_content(filepath)
            
            # 最も適切なカテゴリを決定
            best_category = "その他"
            best_score = 0
            
            for category, cat_info in CATEGORIES.items():
                if category == "その他":
                    continue
                
                score = 0
                for keyword in cat_info["keywords"]:
                    if keyword.lower() in filename.lower():
                        score += 10
                    if keyword.lower() in content.lower():
                        score += 1
                
                # 優先度を考慮
                score = score / cat_info["priority"]
                
                if score > best_score:
                    best_score = score
                    best_category = category
            
            file_info['category'] = best_category
            file_info['score'] = best_score
    
    def read_file_content(self, filepath):
        """ファイルの内容を読み込む"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        except:
            return ""
    
    def extract_tags_and_relations(self):
        """タグと関連性を抽出"""
        print("\nExtracting tags and relations...")
        
        # すべてのファイルからキーワードを抽出
        all_keywords = set()
        
        for filepath, file_info in self.file_index.items():
            content = self.read_file_content(filepath)
            
            # タグを抽出
            tags = []
            
            # #タグ形式
            tag_matches = re.findall(r'#([^\s#]+)', content)
            tags.extend(tag_matches)
            
            # カテゴリをタグに追加
            if file_info['category']:
                tags.append(file_info['category'])
            
            # よしなに関連の特別タグ
            if 'よしなに' in content:
                tags.append('よしなに対応')
            
            file_info['tags'] = list(set(tags))
            
            # キーワードを収集
            words = re.findall(r'[ぁ-んァ-ン一-龥ー]+|[a-zA-Z]+', content)
            all_keywords.update(words)
        
        # 関連性を計算
        self.calculate_relations(all_keywords)
    
    def calculate_relations(self, all_keywords):
        """ファイル間の関連性を計算"""
        print("  Calculating file relations...")
        
        # 重要キーワードを定義
        important_keywords = {
            'よしなに', '対応', 'クライアント', '提案', '質問',
            'WordPress', 'デザイン', 'コーディング', '実装',
            'マーケティング', '集客', '単価', '案件'
        }
        
        file_paths = list(self.file_index.keys())
        
        for i, filepath1 in enumerate(file_paths):
            content1 = self.read_file_content(filepath1)
            relations = []
            
            for j, filepath2 in enumerate(file_paths):
                if i >= j:  # 自分自身と既に計算済みのペアはスキップ
                    continue
                
                content2 = self.read_file_content(filepath2)
                
                # 関連性スコアを計算
                score = 0
                
                # 共通の重要キーワード
                for keyword in important_keywords:
                    if keyword in content1 and keyword in content2:
                        score += 10
                
                # 相互参照
                filename1 = self.file_index[filepath1]['filename']
                filename2 = self.file_index[filepath2]['filename']
                
                if filename2.replace('.md', '') in content1:
                    score += 20
                if filename1.replace('.md', '') in content2:
                    score += 20
                
                # 同じカテゴリ
                if self.file_index[filepath1]['category'] == self.file_index[filepath2]['category']:
                    score += 5
                
                if score >= 15:  # 閾値以上なら関連ありとする
                    relations.append({
                        'file': filepath2,
                        'score': score
                    })
            
            # スコアの高い順にソートして上位を保存
            relations.sort(key=lambda x: x['score'], reverse=True)
            self.file_index[filepath1]['relations'] = relations[:10]  # 上位10件
    
    def remove_duplicates(self):
        """重複ファイルを処理"""
        print("\nProcessing duplicate files...")
        
        # コンテンツハッシュごとにファイルをグループ化
        hash_groups = {}
        for filepath, file_info in self.file_index.items():
            content_hash = file_info['content_hash']
            if content_hash not in hash_groups:
                hash_groups[content_hash] = []
            hash_groups[content_hash].append(filepath)
        
        # 重複を処理
        duplicates_removed = 0
        for content_hash, filepaths in hash_groups.items():
            if len(filepaths) > 1:
                # 最も情報量の多いファイルを保持
                best_file = max(filepaths, key=lambda f: self.file_index[f]['metadata'].get('content_length', 0))
                
                for filepath in filepaths:
                    if filepath != best_file:
                        self.file_index[filepath]['duplicate_of'] = best_file
                        duplicates_removed += 1
        
        print(f"  Found {duplicates_removed} duplicate files")
        return duplicates_removed
    
    def reorganize_files(self):
        """ファイルを新しい構造に再編成"""
        print("\nReorganizing files...")
        
        files_moved = 0
        
        for filepath, file_info in self.file_index.items():
            # 重複ファイルはスキップ
            if 'duplicate_of' in file_info:
                continue
            
            # プレースホルダーファイルはスキップ
            if file_info['metadata'].get('is_placeholder', False):
                if file_info['metadata'].get('content_length', 0) < 1000:
                    continue
            
            # 新しいパスを決定
            category = file_info['category']
            category_info = CATEGORIES[category]
            
            # ファイル名をクリーンアップ
            clean_filename = self.clean_filename(file_info['filename'])
            
            # 新しいパス
            new_dir = os.path.join(KNOWLEDGE_BASE_DIR, category_info['dir'])
            new_path = os.path.join(new_dir, clean_filename)
            
            # ファイルをコピー（既存のファイルは残す）
            try:
                os.makedirs(os.path.dirname(new_path), exist_ok=True)
                shutil.copy2(filepath, new_path)
                
                # ファイル内のリンクを更新
                self.update_file_links(new_path, filepath, new_path)
                
                files_moved += 1
                
            except Exception as e:
                print(f"  Error moving {filepath}: {e}")
        
        print(f"  Reorganized {files_moved} files")
        return files_moved
    
    def clean_filename(self, filename):
        """ファイル名をクリーンアップ"""
        # 不要な文字を削除
        filename = re.sub(r'[<>:"/\\|?*]', '', filename)
        
        # 長すぎる場合は短縮
        if len(filename) > 100:
            name, ext = os.path.splitext(filename)
            filename = name[:97] + '...' + ext
        
        return filename
    
    def update_file_links(self, filepath, old_path, new_path):
        """ファイル内のリンクを更新"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 関連ファイルへのリンクを追加
            file_info = self.file_index.get(old_path, {})
            relations = file_info.get('relations', [])
            
            if relations:
                # 関連リンクセクションを追加
                related_section = "\n\n## 関連ドキュメント\n\n"
                
                for relation in relations[:5]:  # 上位5件
                    related_file = relation['file']
                    related_info = self.file_index.get(related_file, {})
                    related_title = related_info.get('metadata', {}).get('title', os.path.basename(related_file))
                    
                    # 相対パスを計算
                    related_category = related_info.get('category', 'その他')
                    related_filename = self.clean_filename(os.path.basename(related_file))
                    related_path = f"../{CATEGORIES[related_category]['dir']}/{related_filename}"
                    
                    related_section += f"- [[{related_path}|{related_title}]]\n"
                
                # タグセクションを追加
                tags = file_info.get('tags', [])
                if tags:
                    tag_section = "\n\n## タグ\n\n"
                    for tag in tags:
                        tag_section += f"#{tag} "
                    content += tag_section
                
                content += related_section
                
                # ファイルを更新
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                    
        except Exception as e:
            print(f"  Error updating links in {filepath}: {e}")
    
    def create_index_files(self):
        """インデックスファイルを作成"""
        print("\nCreating index files...")
        
        # メインインデックス
        self.create_main_index()
        
        # カテゴリ別インデックス
        self.create_category_indexes()
        
        # よしなに対応特別インデックス
        self.create_yoshinani_index()
    
    def create_main_index(self):
        """メインインデックスファイルを作成"""
        index_path = os.path.join(KNOWLEDGE_BASE_DIR, "00_Index", "README.md")
        
        content = """# 📚 ナレッジベース インデックス

このナレッジベースは、Notionから統合されたすべての知識を体系的に整理したものです。

## 🗂️ カテゴリ

"""
        
        # カテゴリ別統計
        category_stats = {}
        for file_info in self.file_index.values():
            if 'duplicate_of' not in file_info:
                category = file_info['category']
                category_stats[category] = category_stats.get(category, 0) + 1
        
        # カテゴリリスト
        for category, info in sorted(CATEGORIES.items(), key=lambda x: x[1]['priority']):
            count = category_stats.get(category, 0)
            if count > 0:
                content += f"### [[../{info['dir']}/README.md|{category}]] ({count}件)\n"
                content += f"{', '.join(info['keywords'][:5])}\n\n"
        
        content += """
## 🔍 クイックアクセス

- [[../01_よしなに対応/よしなに対応_完全ガイド.md|よしなに対応 完全ガイド]]
- [[../02_Web制作/WordPress_ベストプラクティス.md|WordPress ベストプラクティス]]
- [[../04_ビジネス/単価UP戦略.md|単価UP戦略]]

## 📊 統計情報

"""
        
        # 統計情報
        total_files = len([f for f in self.file_index.values() if 'duplicate_of' not in f])
        total_duplicates = len([f for f in self.file_index.values() if 'duplicate_of' in f])
        
        content += f"- 総ファイル数: {total_files}\n"
        content += f"- 重複ファイル: {total_duplicates}\n"
        content += f"- カテゴリ数: {len([c for c in category_stats.values() if c > 0])}\n"
        content += f"\n更新日時: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    def create_category_indexes(self):
        """カテゴリ別インデックスを作成"""
        for category, info in CATEGORIES.items():
            category_dir = os.path.join(KNOWLEDGE_BASE_DIR, info['dir'])
            index_path = os.path.join(category_dir, "README.md")
            
            # カテゴリ内のファイルを収集
            category_files = []
            for filepath, file_info in self.file_index.items():
                if file_info['category'] == category and 'duplicate_of' not in file_info:
                    category_files.append((filepath, file_info))
            
            if not category_files:
                continue
            
            # インデックス内容を生成
            content = f"# {category}\n\n"
            content += f"このカテゴリには {len(category_files)} 件のドキュメントがあります。\n\n"
            
            # キーワード
            if info['keywords']:
                content += f"**関連キーワード**: {', '.join(info['keywords'])}\n\n"
            
            content += "## ドキュメント一覧\n\n"
            
            # ファイルリスト（スコア順）
            category_files.sort(key=lambda x: x[1].get('score', 0), reverse=True)
            
            for filepath, file_info in category_files:
                title = file_info['metadata'].get('title', os.path.basename(filepath))
                filename = self.clean_filename(os.path.basename(filepath))
                tags = ' '.join([f'#{tag}' for tag in file_info.get('tags', [])[:3]])
                
                content += f"- [[{filename}|{title}]] {tags}\n"
            
            with open(index_path, 'w', encoding='utf-8') as f:
                f.write(content)
    
    def create_yoshinani_index(self):
        """よしなに対応の特別インデックスを作成"""
        yoshinani_path = os.path.join(KNOWLEDGE_BASE_DIR, "01_よしなに対応", "よしなに対応_完全ガイド.md")
        
        content = """# よしなに対応 完全ガイド

## 📖 よしなに対応とは

**よしなに対応 = 相手目線で"手間"や"面倒"を巻き取る力**

### 3つの柱

1. **信頼構築力** - 「迅速・厳守・誠実・安心・温度」
2. **情報編集力** - 「相手の意図を読み解き、2.3手先回りした対応」
3. **当事者意識** - 「自分ごととしてプロジェクトを捉える」

## 📚 学習パス

### 基礎編
1. [[第1回 よしなに基礎理解講座 〜よしなにって何？〜.md|第1回 よしなに基礎理解講座]]
2. [[よしなに力の本質.md|よしなに力の本質]]
3. [[よしなに対応を構造化.md|よしなに対応を構造化]]

### 実践編
1. [[よしなに対応鉄板ポイント（やり取り編）.md|よしなに対応鉄板ポイント（やり取り編）]]
2. [[よしなに対応鉄板ポイント（実装編）.md|よしなに対応鉄板ポイント（実装編）]]
3. [[実案件のよしなに対応例（提案と報告書）.md|実案件のよしなに対応例]]

### 応用編
1. [[アニメーションよしなに対応（その１）.md|アニメーションよしなに対応]]
2. [[請求書を出す時のよしなにポイント.md|請求書を出す時のよしなにポイント]]
3. [[進捗管理をまるっと巻き取る〝よしなに管理シート〟.md|よしなに管理シート]]

## 🛠️ ツール・テンプレート

- [[よしなにチェックシート.md|よしなにチェックシート]]
- [[よしなにチェックシート（毎週）.md|よしなにチェックシート（毎週）]]
- [[よしなにチェックシート（毎月）.md|よしなにチェックシート（毎月）]]
- [[よしなにチェックシート（案件対応）.md|よしなにチェックシート（案件対応）]]

## 💡 重要な考え方

### 感謝×相手目線のPDCA
- 相手の立場・目的・抱えている負担を読み取り、**こちらから動く姿勢**
- 「何が手間か？」を想像し、巻き取る意識を常に持つ
- その繰り返しが、他者にはない"余裕"と"自信"につながる

### 疲弊しないための"線引き力"
- 必要最低限のやりとり（省エネ対応）
- 「この会社と1年後も付き合いたいか？」で判断
- フルコミットする相手は自分で選ぶ

## 📈 成長のステップ

1. **感謝の気持ちを持つ** - すべての起点
2. **相手目線で考える** - 何が手間か？を想像
3. **先回りして動く** - 2,3手先を読む
4. **PDCAを回す** - 常に改善し続ける
5. **自信を持つ** - 積み重ねが余裕を生む

---

このガイドは随時更新されます。
最終更新: """ + datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        with open(yoshinani_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    def generate_report(self):
        """処理レポートを生成"""
        report_path = os.path.join(KNOWLEDGE_BASE_DIR, "00_Index", "Integration_Report.md")
        
        content = f"""# Knowledge Base Integration Report

Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Summary

- Total files processed: {len(self.file_index)}
- Files reorganized: {len([f for f in self.file_index.values() if 'duplicate_of' not in f])}
- Duplicates found: {len([f for f in self.file_index.values() if 'duplicate_of' in f])}

## Category Distribution

"""
        
        # カテゴリ分布
        category_dist = {}
        for file_info in self.file_index.values():
            if 'duplicate_of' not in file_info:
                category = file_info['category']
                category_dist[category] = category_dist.get(category, 0) + 1
        
        for category, count in sorted(category_dist.items(), key=lambda x: x[1], reverse=True):
            percentage = (count / sum(category_dist.values())) * 100
            content += f"- {category}: {count} files ({percentage:.1f}%)\n"
        
        content += "\n## Processing Details\n\n"
        content += f"- Backup location: {BACKUP_DIR}\n"
        content += f"- Knowledge base location: {KNOWLEDGE_BASE_DIR}\n"
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"\nReport saved to: {report_path}")

def main():
    """メイン処理"""
    print("=" * 60)
    print("Comprehensive Knowledge Integration")
    print("=" * 60)
    
    integrator = KnowledgeIntegrator()
    
    # 1. ディレクトリ構造を作成
    integrator.create_directories()
    
    # 2. 既存ファイルをバックアップ
    integrator.backup_existing_files()
    
    # 3. すべてのファイルをスキャン
    file_count = integrator.scan_all_files()
    
    if file_count == 0:
        print("No files found to process.")
        return
    
    # 4. ファイルをカテゴリに分類
    integrator.categorize_files()
    
    # 5. タグと関連性を抽出
    integrator.extract_tags_and_relations()
    
    # 6. 重複を処理
    integrator.remove_duplicates()
    
    # 7. ファイルを再編成
    integrator.reorganize_files()
    
    # 8. インデックスファイルを作成
    integrator.create_index_files()
    
    # 9. レポートを生成
    integrator.generate_report()
    
    print("\n" + "=" * 60)
    print("Integration completed successfully!")
    print("=" * 60)

if __name__ == "__main__":
    main()