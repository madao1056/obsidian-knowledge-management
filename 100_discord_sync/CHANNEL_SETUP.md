# 既存のDiscordチャンネルを使う設定方法

## 方法1: チャンネル名で判定（簡単）

`discord_bot.js` の以下の部分を編集してください：

```javascript
const CHANNEL_CONFIG = {
    daily_report: ['ここに日報チャンネル名を追加'],
    question: ['ここに質問チャンネル名を追加'],
    progress: ['ここに進捗チャンネル名を追加']
};
```

### 例1: 一般的なチャンネル名の場合
```javascript
const CHANNEL_CONFIG = {
    daily_report: ['general', '雑談', '全体'],
    question: ['help', 'サポート', '相談'],
    progress: ['完了報告', '成果']
};
```

### 例2: すべて同じチャンネルを使う場合
```javascript
const CHANNEL_CONFIG = {
    daily_report: ['general'],
    question: ['general'],
    progress: ['general']
};
```

## 方法2: チャンネルIDで判定（確実）

1. Discordでチャンネルを右クリック
2. 「IDをコピー」を選択（開発者モードが必要）
3. `discord_bot.js` の以下の部分に貼り付け：

```javascript
const CHANNEL_IDS = {
    daily_report: '1234567890123456789', // 日報チャンネルのID
    question: '1234567890123456790',     // 質問チャンネルのID
    progress: '1234567890123456791'      // 進捗チャンネルのID
};
```

## 方法3: タグで判定（どのチャンネルでもOK）

チャンネルに関係なく、メッセージに以下のタグを付けるだけ：
- `#日報` または `#daily` → 日報として処理
- `#質問` または `#question` → 質問として処理
- `#進捗` または `#progress` → 進捗として処理

## 方法4: すべてのメッセージを特定タイプとして扱う

例：すべてのメッセージを日報として扱う場合

`discord_bot.js` の72行目のコメントを外す：
```javascript
// どのチャンネルでも強制的に日報として扱う設定（オプション）
return 'daily_report';  // すべてを日報として扱う場合はコメントを外す
```

## 開発者モードの有効化（チャンネルIDを取得する場合）

1. Discord設定を開く（歯車アイコン）
2. 「詳細設定」をクリック
3. 「開発者モード」をONにする
4. チャンネルを右クリック → 「IDをコピー」が表示される

## おすすめ設定

既存のチャンネル構成に応じて：

### パターンA: 専用チャンネルがある場合
```javascript
const CHANNEL_CONFIG = {
    daily_report: ['日報', '作業報告'],
    question: ['質問', 'ヘルプ'],
    progress: ['進捗', '成果']
};
```

### パターンB: 1つのチャンネルで運用する場合
タグ（#日報、#質問、#進捗）で判定するのがおすすめ

### パターンC: 特定のメンバー専用チャンネルがある場合
チャンネルIDで確実に指定するのがおすすめ