# 🚀 Discord連携 クイックガイド（簡易版）

## よく使うコマンド 3つだけ！

### 1️⃣ 過去のメッセージを全部取る（最初だけ）
```bash
cd 100_discord_sync
./collect_history_batch.sh
```
→ 5月からの全メッセージ（スレッド含む）を取得

### 2️⃣ 新しいメッセージを自動保存開始
```bash
cd 100_discord_sync  
./start_batch.sh
```
→ これ以降のメッセージを自動でObsidianに保存

### 3️⃣ すぐObsidianで見たい時
```bash
cd 100_discord_sync
venv/bin/python main_processor.py --once
```
→ 保存したデータを今すぐマークダウンに変換

---

## 📁 保存される場所
```
03_Support/グッサポ・ラボ/メンバー管理/
└── [メンバー名]/
    ├── 日報/
    ├── 質問履歴/
    └── 進捗報告/
```

## 💡 覚えておくこと
- メッセージに💾マークが付いたら保存完了
- 30分ごとに自動でObsidian形式に変換される
- スレッドの中も全部取れる！

詳しくは → `100_discord_sync/使い方ガイド.md`