#!/usr/bin/env python3
"""
Obsidianナレッジベース内の関連性を分析し、タグとリンクを自動生成するスクリプト
"""
import os
import re
import json
from datetime import datetime
from collections import defaultdict, Counter
import sys

# 日本語の形態素解析
try:
    import MeCab
    mecab_available = True
    mecab = MeCab.Tagger()
except ImportError:
    mecab_available = False
    print("MeCabが利用できません。基本的なキーワード抽出のみ行います。")

# 設定
KNOWLEDGE_DIR = "/Users/hashiguchimasaki/project/obsidian"
NOTION_DIR = os.path.join(KNOWLEDGE_DIR, "20_Literature/25_Notion")
OUTPUT_DIR = os.path.join(KNOWLEDGE_DIR, "100_cursor/knowledge_analysis")

# キーワードカテゴリ定義
KEYWORD_CATEGORIES = {
    "営業・ビジネス": [
        "営業", "セールス", "クロージング", "顧客", "提案", "商談",
        "リード", "マーケティング", "集客", "成約", "契約", "売上",
        "収益", "利益", "ビジネス", "事業", "起業", "経営"
    ],
    "スキル・能力": [
        "スキル", "能力", "技術", "ノウハウ", "知識", "経験",
        "学習", "成長", "向上", "改善", "習得", "マスター",
        "プロフェッショナル", "専門", "エキスパート"
    ],
    "コミュニケーション": [
        "コミュニケーション", "対話", "会話", "やり取り", "返信",
        "メッセージ", "連絡", "相談", "質問", "回答", "フィードバック",
        "プレゼン", "説明", "伝える", "聞く", "理解"
    ],
    "マインドセット": [
        "マインド", "思考", "考え方", "意識", "姿勢", "態度",
        "モチベーション", "やる気", "情熱", "目標", "目的",
        "ビジョン", "価値観", "信念", "哲学"
    ],
    "Web制作・技術": [
        "Web", "サイト", "ホームページ", "デザイン", "コーディング",
        "プログラミング", "開発", "実装", "WordPress", "HTML", "CSS",
        "JavaScript", "React", "TypeScript", "API", "データベース"
    ],
    "AI・自動化": [
        "AI", "人工知能", "ChatGPT", "Claude", "自動化", "効率化",
        "DX", "デジタル", "テクノロジー", "イノベーション",
        "機械学習", "ディープラーニング", "プロンプト"
    ],
    "教育・コーチング": [
        "教育", "指導", "コーチング", "メンタリング", "サポート",
        "アドバイス", "カウンセリング", "相談", "壁打ち", "個別",
        "セミナー", "講座", "研修", "トレーニング"
    ]
}

def ensure_output_dir():
    """出力ディレクトリを作成"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

def extract_keywords_basic(text):
    """基本的なキーワード抽出"""
    keywords = []
    
    # カテゴリキーワードをチェック
    for category, words in KEYWORD_CATEGORIES.items():
        for word in words:
            if word in text:
                keywords.append(word)
    
    # 数字を含むパターン（金額、年数など）
    numbers = re.findall(r'\d+[万円年月日時間人個]', text)
    keywords.extend(numbers)
    
    # カタカナ語（専門用語の可能性）
    katakana = re.findall(r'[ァ-ヴー]{3,}', text)
    keywords.extend(katakana)
    
    return list(set(keywords))

def extract_keywords_mecab(text):
    """MeCabを使用した高度なキーワード抽出"""
    if not mecab_available:
        return extract_keywords_basic(text)
    
    keywords = []
    
    try:
        # 形態素解析
        parsed = mecab.parse(text)
        
        for line in parsed.split('\n'):
            if line == 'EOS' or line == '':
                continue
            
            parts = line.split('\t')
            if len(parts) < 2:
                continue
            
            word = parts[0]
            features = parts[1].split(',')
            
            # 名詞を抽出（固有名詞、一般名詞、サ変接続）
            if features[0] == '名詞' and features[1] in ['固有名詞', '一般', 'サ変接続']:
                if len(word) >= 2:  # 2文字以上
                    keywords.append(word)
    except:
        # エラー時は基本抽出にフォールバック
        return extract_keywords_basic(text)
    
    # 基本抽出の結果も追加
    keywords.extend(extract_keywords_basic(text))
    
    return list(set(keywords))

def analyze_file(filepath):
    """ファイルを分析してメタデータを抽出"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # タイトルを取得
        title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        title = title_match.group(1) if title_match else os.path.basename(filepath).replace('.md', '')
        
        # メタデータを抽出
        metadata = {}
        metadata_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
        if metadata_match:
            metadata_text = metadata_match.group(1)
            for line in metadata_text.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    metadata[key.strip()] = value.strip()
        
        # コンテンツ部分を抽出
        content_without_metadata = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
        
        # キーワードを抽出
        keywords = extract_keywords_mecab(content_without_metadata)
        
        # カテゴリを判定
        categories = []
        for category, cat_keywords in KEYWORD_CATEGORIES.items():
            if any(kw in keywords for kw in cat_keywords):
                categories.append(category)
        
        return {
            'title': title,
            'filepath': filepath,
            'keywords': keywords,
            'categories': categories,
            'metadata': metadata,
            'content_length': len(content_without_metadata),
            'has_content': len(content_without_metadata.strip()) > 100
        }
    
    except Exception as e:
        print(f"Error analyzing {filepath}: {e}")
        return None

def find_related_files(file_data, all_files_data, top_n=5):
    """関連ファイルを見つける"""
    if not file_data['keywords']:
        return []
    
    scores = []
    
    for other_file in all_files_data:
        if other_file['filepath'] == file_data['filepath']:
            continue
        
        # キーワードの共通度を計算
        common_keywords = set(file_data['keywords']) & set(other_file['keywords'])
        keyword_score = len(common_keywords)
        
        # カテゴリの共通度
        common_categories = set(file_data['categories']) & set(other_file['categories'])
        category_score = len(common_categories) * 3  # カテゴリの重みを高く
        
        total_score = keyword_score + category_score
        
        if total_score > 0:
            scores.append({
                'file': other_file,
                'score': total_score,
                'common_keywords': list(common_keywords),
                'common_categories': list(common_categories)
            })
    
    # スコアでソートして上位を返す
    scores.sort(key=lambda x: x['score'], reverse=True)
    return scores[:top_n]

def generate_tags(file_data):
    """ファイルに適したタグを生成"""
    tags = []
    
    # カテゴリタグ
    for category in file_data['categories']:
        tags.append(f"#{category.replace('・', '_')}")
    
    # 重要キーワードタグ（頻出するもの）
    keyword_counter = Counter(file_data['keywords'])
    for keyword, count in keyword_counter.most_common(5):
        if count >= 2 and len(keyword) >= 3:
            tags.append(f"#{keyword}")
    
    return list(set(tags))

def update_file_with_relations(file_data, related_files, tags):
    """ファイルに関連情報とタグを追加"""
    try:
        with open(file_data['filepath'], 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 既存の関連セクションを削除
        content = re.sub(r'\n## 🔗 関連ナレッジ\n.*?(?=\n##|\n#|$)', '', content, flags=re.DOTALL)
        content = re.sub(r'\n## 🏷️ タグ\n.*?(?=\n##|\n#|$)', '', content, flags=re.DOTALL)
        
        # 新しいセクションを追加
        additions = []
        
        # タグセクション
        if tags:
            tag_section = "\n## 🏷️ タグ\n"
            tag_section += " ".join(tags) + "\n"
            additions.append(tag_section)
        
        # 関連ナレッジセクション
        if related_files:
            relation_section = "\n## 🔗 関連ナレッジ\n"
            for rel in related_files:
                rel_file = rel['file']
                rel_title = rel_file['title']
                rel_path = os.path.relpath(rel_file['filepath'], os.path.dirname(file_data['filepath']))
                
                # Obsidianスタイルのリンク
                relation_section += f"- [[{rel_title}]] - "
                
                # 共通要素を表示
                if rel['common_categories']:
                    relation_section += f"カテゴリ: {', '.join(rel['common_categories'])} "
                if rel['common_keywords'][:3]:  # 最初の3つのキーワード
                    relation_section += f"キーワード: {', '.join(rel['common_keywords'][:3])}"
                
                relation_section += "\n"
            
            additions.append(relation_section)
        
        # コンテンツの最後に追加
        if additions:
            content = content.rstrip() + "\n" + "".join(additions)
            
            with open(file_data['filepath'], 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True
    
    except Exception as e:
        print(f"Error updating {file_data['filepath']}: {e}")
        return False

def main():
    """メイン処理"""
    print("=" * 60)
    print("Knowledge Relation Builder")
    print("=" * 60)
    
    ensure_output_dir()
    
    # ステップ1: すべてのマークダウンファイルを分析
    print("\n1. Analyzing all markdown files...")
    
    all_files_data = []
    
    # Notionディレクトリのファイル
    for filename in os.listdir(NOTION_DIR):
        if filename.endswith('.md') and not filename.startswith('.'):
            filepath = os.path.join(NOTION_DIR, filename)
            file_data = analyze_file(filepath)
            if file_data and file_data['has_content']:
                all_files_data.append(file_data)
    
    print(f"Analyzed {len(all_files_data)} files with content")
    
    # ステップ2: 関連性を計算してファイルを更新
    print("\n2. Building relations and updating files...")
    
    updated_count = 0
    
    for i, file_data in enumerate(all_files_data):
        print(f"\n[{i+1}/{len(all_files_data)}] {file_data['title']}")
        
        # 関連ファイルを見つける
        related_files = find_related_files(file_data, all_files_data)
        
        # タグを生成
        tags = generate_tags(file_data)
        
        # ファイルを更新
        if update_file_with_relations(file_data, related_files, tags):
            updated_count += 1
            print(f"  ✓ Added {len(tags)} tags and {len(related_files)} relations")
        else:
            print(f"  ✗ Failed to update")
    
    # ステップ3: 分析結果を保存
    print("\n3. Saving analysis results...")
    
    # カテゴリ別統計
    category_stats = defaultdict(list)
    for file_data in all_files_data:
        for category in file_data['categories']:
            category_stats[category].append(file_data['title'])
    
    # キーワード統計
    all_keywords = []
    for file_data in all_files_data:
        all_keywords.extend(file_data['keywords'])
    keyword_stats = Counter(all_keywords).most_common(50)
    
    # 統計情報を保存
    stats = {
        'analysis_date': datetime.now().isoformat(),
        'total_files': len(all_files_data),
        'updated_files': updated_count,
        'category_distribution': {k: len(v) for k, v in category_stats.items()},
        'top_keywords': keyword_stats,
        'files_by_category': dict(category_stats)
    }
    
    stats_file = os.path.join(OUTPUT_DIR, 'knowledge_analysis.json')
    with open(stats_file, 'w', encoding='utf-8') as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)
    
    print(f"\nAnalysis saved to: {stats_file}")
    
    # サマリー表示
    print("\n" + "=" * 60)
    print("ANALYSIS SUMMARY")
    print("=" * 60)
    print(f"Total files analyzed: {len(all_files_data)}")
    print(f"Files updated: {updated_count}")
    print(f"\nCategory distribution:")
    for category, count in sorted(stats['category_distribution'].items(), key=lambda x: x[1], reverse=True):
        print(f"  - {category}: {count} files")
    print(f"\nTop 10 keywords:")
    for keyword, count in keyword_stats[:10]:
        print(f"  - {keyword}: {count} occurrences")

if __name__ == "__main__":
    main()