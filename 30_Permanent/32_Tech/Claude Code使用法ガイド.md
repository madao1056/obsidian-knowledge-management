# Claude Code使用法ガイド

#ClaudeCode #AI開発ツール #コーディング支援 #開発効率化

## Claude Codeとは

Claude Codeは、Anthropic社が提供する開発者向けのAIコーディングアシスタントツールです。ターミナル内で直接動作し、自然言語での指示からコード生成、バグ修正、プロジェクト分析まで幅広い開発タスクを支援します。

## 主要機能

### 1. コード生成
- プレーンな日本語や英語での説明から直接コードを作成
- 既存のコードベースのパターンを理解し、一貫性のあるコードを生成
- 複数のプログラミング言語に対応

### 2. バグ分析と修正
- コードベース内のバグを自動的に検出
- 修正案を提示し、実装まで実行
- エラーメッセージから問題を診断

### 3. プロジェクト理解
- プロジェクト全体の構造を把握
- コードベースに関する質問に回答
- ドキュメント生成支援

### 4. 作業の自動化
- リントエラーの修正
- マージコンフリクトの解決
- リファクタリング作業
- テストコードの生成

## インストール方法

### 前提条件
- Node.js 18以降がインストールされていること
- npmまたはyarnが使用可能であること

### インストール手順
```bash
# グローバルインストール
npm install -g @anthropic-ai/claude-code

# プロジェクトディレクトリに移動
cd your-project-directory

# Claude Codeを起動
claude
```

## 基本的な使い方

### 1. プロジェクトでの起動
```bash
# プロジェクトのルートディレクトリで実行
claude
```

### 2. コマンド例

#### 新機能の実装
```
「ユーザー認証機能を実装してください。JWTトークンを使用し、ログイン、ログアウト、トークンリフレッシュ機能を含めてください」
```

#### バグ修正
```
「TypeError: Cannot read property 'name' of undefinedというエラーが発生しています。修正してください」
```

#### コードの説明
```
「src/utils/auth.jsファイルの処理内容を説明してください」
```

#### リファクタリング
```
「UserControllerクラスのメソッドを責任ごとに分割してリファクタリングしてください」
```

## ベストプラクティス

### 1. 明確な指示を出す
- 具体的な要件を含める
- 期待する動作を明確に説明
- 使用したい技術やライブラリを指定

### 2. コンテキストを提供
- 関連ファイルへの参照を含める
- プロジェクトの規約やスタイルガイドを説明
- 既存のパターンに従うよう指示

### 3. 段階的なアプローチ
- 大きなタスクは小さなステップに分割
- 各ステップで動作確認を実施
- 必要に応じて修正を依頼

### 4. セキュリティへの配慮
- 機密情報を含むファイルには注意
- APIキーやパスワードは環境変数で管理
- セキュリティベストプラクティスの遵守を指示

## VS Code拡張機能

### インストールと使用
Claude CodeはVS Code、Cursor、Windsurfなどの主要なエディタで使用可能です。VS Code拡張機能をインストールすることで、エディタ内から直接起動できます。

```bash
# VS Code拡張機能から起動
# 複数のインスタンスを並列実行可能（異なるプロジェクト部分で作業する場合）
```

## ターミナルUI機能

### 基本操作
- **@タグ**: ファイルを簡単に参照
- **スラッシュコマンド**: `/clear`で履歴クリア、`/init`でプロジェクト初期化
- **モデル選択**: Opus（高性能）とSonnet（効率的）を選択可能
- **使用量管理**: 50%使用でOpusからSonnetに自動切り替え

### キーボードショートカット（追加）
- **Shift+Enter**: 新しい行（`/terminal-setup`で設定）
- **Shift+ドラッグ**: ファイルを参照として追加
- **Control+V**: 画像貼り付け（Command+Vではない）
- **Escape**: Claude停止（Control+Cは完全終了）
- **Escape×2**: 過去のメッセージ一覧表示

### 危険なスキップオプション
```bash
# 毎回の権限確認をスキップ（自己責任）
claude --dangerously-skip-permissions
```
**注意**: ファイル編集やコマンド実行の都度確認をスキップします。便利ですが、リスクを理解した上で使用してください。

## 高度な機能

### GitHubインテグレーション
```bash
# GitHub連携アプリをインストール
/install-github-app
```

PRレビューの自動化設定（`claude-code-review.yml`）：
```yaml
# 簡潔で重要な指摘のみに絞る設定例
review_prompt: |
  Focus on bugs and security vulnerabilities.
  Be concise and skip minor style issues.
  Only comment on critical problems.
```

### メモリ管理（CLAUDE.md）
プロジェクトルートに`CLAUDE.md`ファイルを作成することで、プロジェクト固有の情報を記憶させることができます：

```markdown
# プロジェクト概要
このプロジェクトはECサイトのバックエンドAPIです。

## コーディング規約
- TypeScriptを使用
- ESLint設定に従う
- テストはJestで記述

## アーキテクチャ
- Clean Architectureを採用
- DIコンテナはTsyringe使用
```

### カスタムフック（`.claude/hooks.mjs`）
```javascript
// 編集前に実行されるフック
export async function preEdit({ filePath, oldContent, newContent }) {
  // ファイルのフォーマットチェック
  if (filePath.match(/\.(ts|tsx|js|jsx)$/)) {
    execSync(`yarn prettier --check "${filePath}"`, { stdio: 'pipe' });
  }
  return { proceed: true };
}

// 編集後に実行されるフック
export async function postEdit({ filePath, oldContent, newContent, success }) {
  if (!success) return;
  // TypeScriptの型チェック
  if (filePath.match(/\.(ts|tsx)$/)) {
    execSync(`npx tsc --noEmit --skipLibCheck "${filePath}"`, { stdio: 'pipe' });
  }
}
```

### カスタムスラッシュコマンド
`.claude/commands/`ディレクトリに`.md`ファイルを作成：

```bash
# .claude/commands/test.md
Generate comprehensive tests for $ARGUMENTS with the following requirements:
- Use our testing framework conventions
- Include edge cases
- Mock external dependencies
```

使用例：`/test MyButton`

### メモリシステム
- **#記号**: 簡単にメモリ追加（例：`#always use MUI components`）
- **階層的CLAUDE.md**: プロジェクトレベルとディレクトリレベルで設定可能
- **グローバル/ローカル設定**: ユーザー全体または特定プロジェクトの設定

### ツール連携
- Git操作の自動化
- テスト実行とカバレッジ確認
- デプロイスクリプトの実行
- CI/CDパイプラインとの統合
- Pull Requestへの自動コメント・修正

## トラブルシューティング

### よくある問題と解決方法

#### 1. Node.jsバージョンエラー
```bash
# Node.jsバージョンを確認
node --version

# 18以降でない場合はアップデート
nvm install 18
nvm use 18
```

#### 2. 権限エラー
```bash
# npmの権限を修正
sudo npm install -g @anthropic-ai/claude-code
```

#### 3. プロジェクト認識エラー
- プロジェクトのルートディレクトリで実行しているか確認
- .gitディレクトリが存在するか確認
- package.jsonが存在するか確認

## 活用シナリオ

### 1. 新規プロジェクトの立ち上げ
```
「Express.jsとTypeScriptを使用したREST APIプロジェクトを作成してください。
基本的なCRUD操作、認証、エラーハンドリングを含めてください」
```

### 2. 既存コードのリファクタリング
```
「controllers/userController.jsをTypeScriptに変換し、
型安全性を確保してください」
```

### 3. テストの追加
```
「src/services/authService.tsに対するユニットテストを
Jestを使用して作成してください。モックも適切に設定してください」
```

### 4. ドキュメント生成
```
「APIエンドポイントのSwaggerドキュメントを生成してください」
```

## 注意事項

### プライバシーとセキュリティ
- コードはAnthropicのサーバーで処理されますが、保存されません
- 機密情報を含むコードを扱う場合は注意が必要
- 企業での使用時は、セキュリティポリシーを確認

### 制限事項
- インターネット接続が必要
- 大規模なコードベースでは処理時間がかかる場合がある
- 一部の特殊な開発環境では動作しない可能性

## 関連リンク
- [[AI活用による効率化]]
- [[開発ツール統合ガイド]]
- [[コーディング・アニメーション統合ガイド]]

---
*最終更新: 2025-07-15*
*公式ドキュメント: https://docs.anthropic.com/en/docs/claude-code*