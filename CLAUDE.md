# Claude Customization for gussan

# 📚 学習モード有効（2025/07/09時点）

# Primary Language Focus
You are working with a developer who primarily uses TypeScript. 
Prioritize solutions and examples in this language.

# Communication Style
Use casual but professional tone in responses.

# Common Modification Patterns
This developer frequently makes modifications for:
- その他 (100 times)
Be proactive in addressing these concerns.

## Natural Language Patterns
gussanさんは以下のような自然言語での指示をよく使います：

### 修正依頼のパターン:
- その他に関する修正（100回）

## Code Style Preferences
```json
{
  "indentation": "2 spaces",
  "naming": "camelCase",
  "comments": "JSDoc",
  "formatting": [
    "Always specify types explicitly",
    "Use interfaces over type aliases for objects"
  ]
}
```

## Communication Preferences
- Response Length: 簡潔に
- Explanation Level: 適度な説明
- Language: 日本語
- Technical Level: 上級者向け

## Common Development Patterns
### よく編集するファイルタイプ
- .ts: 100回編集

### よくある修正理由
- その他: 100回の修正

## Context Awareness
- Recent Projects: reply, action
- Active Technologies: TypeScript
- Conventions: Indentation: 2 spaces, Naming: camelCase

## Response Guidelines
1. 自然言語での指示を重視し、ユーザーの意図を的確に理解する
2. 簡潔で要点を押さえた応答を心がける
3. 技術的な内容は専門用語を適切に使用
4. コードの修正や提案は、ユーザーの過去のパターンに基づいて行う

## Auto-generated from your coding history
This file was automatically generated based on your development patterns and preferences.
Last updated: 2025-07-10T14:14:55.053Z
Learning data through: 2025/07/09

# important-instruction-reminders
Do what has been asked; nothing more, nothing less.
NEVER create files unless they're absolutely necessary for achieving your goal.
ALWAYS prefer editing an existing file to creating a new one.
NEVER proactively create documentation files (*.md) or README files. Only create documentation files if explicitly requested by the User.

# Obsidian Knowledge Management System Instructions

## 自動実行トリガー
以下のような指示やニュアンスを検出した場合、自動的にクリップ処理を実行する：

### 実行トリガーとなる言葉・フレーズ
- 「記事作成」「記事を作って」「記事にして」
- 「実行して」「処理して」「やって」
- 「クリップを処理」「クリップから記事」
- 「自動化」「生成」「作成」
- その他、記事生成や処理実行の意図が読み取れる表現

### 自動実行コマンド
上記のトリガーを検出したら、以下を実行：
```bash
cd /Users/hashiguchimasaki/project/obsidian && python3 100_cursor/manual_processor.py
```

### 実行後の報告
- 生成された記事のパスを報告
- エラーが発生した場合は内容を説明
- 処理したクリップ数を報告

## 00_Inbox/clipフォルダの自動処理

### 処理フロー
1. **ファイル処理**
   - 00_Inbox/clipフォルダ内のファイルを読み込み
   - 内容を分析し、適切な場所にマークダウン形式で整理
   - 必要に応じてナレッジを抽出

2. **自動削除**
   - 処理が完了したファイルは自動的に削除
   - ユーザーからの削除指示を待たない
   - clipフォルダを常にクリーンな状態に保つ

### 注意事項
- この処理は00_Inbox/clipフォルダのファイルに対してのみ適用
- 処理前に必ずファイル内容を適切な場所に保存してから削除する