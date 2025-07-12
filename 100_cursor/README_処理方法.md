# クリップ処理方法

## 🚀 手動処理（推奨）
パソコンに負荷をかけずに、必要な時だけ処理したい場合：

```bash
# クリップフォルダに記事を追加後、以下を実行
python3 100_cursor/manual_processor.py
```

これで全てのクリップが自動的に処理され、記事が生成されます。

## 🌿 軽量自動監視
パソコンへの負荷を最小限にしつつ自動化したい場合：

```bash
# 30秒ごとにチェックする軽量版
python3 100_cursor/lightweight_watcher.py
```

特徴：
- CPU使用率が極めて低い
- チェック間隔が30秒（変更可能）
- メモリ使用量も最小限

## ⚡ 通常の自動監視
リアルタイムで処理したい場合：

```bash
# 5秒ごとにチェック
python3 100_cursor/simple_auto_watcher.py
```

## 📝 使い分けの目安

| 方法 | こんな時におすすめ | CPU負荷 |
|------|-------------------|---------|
| 手動処理 | まとめて処理したい時 | なし |
| 軽量監視 | 常時監視したいが負荷は避けたい | 極小 |
| 通常監視 | すぐに処理したい | 小 |

## エイリアス設定（オプション）
毎回コマンドを打つのが面倒な場合は、~/.zshrcに以下を追加：

```bash
# Obsidianクリップ処理
alias clip-process='cd /Users/hashiguchimasaki/project/obsidian && python3 100_cursor/manual_processor.py'
alias clip-watch='cd /Users/hashiguchimasaki/project/obsidian && python3 100_cursor/lightweight_watcher.py'
```

設定後、`source ~/.zshrc`を実行すれば、以下のコマンドで実行可能：
- `clip-process` - 手動処理
- `clip-watch` - 軽量監視開始