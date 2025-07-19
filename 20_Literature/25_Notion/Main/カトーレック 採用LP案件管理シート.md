---
notion_id: e881db90-7744-4fe6-bc42-030b1cde5be8
account: Main
title: カトーレック 採用LP案件管理シート
url: https://www.notion.so/LP-e881db9077444fe6bc42030b1cde5be8
created_time: 2023-08-22T04:13:00.000Z
last_edited_time: 2023-09-08T12:45:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:15.089549
---
# カトーレック 採用LP案件管理シート

※「▶︎」をクリックすると**トグルが開きます**
<details>
<summary>目次</summary>
</details>
# 基本情報
<details>
<summary>FTP情報</summary>
</details>
---
---
## 案件仕様情報一覧
- [Untitled](https://www.notion.so/e5a37bc7c5fd4f5fbe12592e7560ef36) 
### 要件抜粋
  - 完全別ドメイン→独自で
  - アコーディオンメニュー / モーダルウィンドウあり
  - zipファイル納品
  **Google フォント**
  Noto Sans JP / 全丸ゴシック
  [https://fonts.google.com/noto/specimen/Noto+Sans+JP?query=noto+sans](https://fonts.google.com/noto/specimen/Noto+Sans+JP?query=noto%20sans)
  [https://fonts.google.com/specimen/Zen+Maru+Gothic](https://fonts.google.com/specimen/Zen+Maru+Gothic)
  **※筑紫ゴシック→画像で表現する**
  **そのほか実装要件**
  - 右下のトップに戻るボタンは青いセクションに入ってからふわっと表示させる
  - ヘッダー追従
  - **「Why？」なぜかトーレックに入社したの？**
  - **「Where？」働く場所ってどんなとこ？**
  - SPファースト（ブレイクポイント768px）
---
# 進捗管理
## スクリーンショット
## パーツ管理（FLOCSS）※チーム制作
---
# 確認事項一覧（対応履歴）
---
## 未対応事項メモ（なし）
持ってるボールがあれば追加
---
# 品質管理
## 納品データ
Gulp環境含む
## 各ブラウザ検証
【検証内容】
- フォントが反映されているか
- 表示崩れはないか
- 挙動がおかしい箇所はないか（アニメーション、ホバー時、JS実装箇所）
## 品質チェック項目
- **仕様の抜け漏れ**
  - [x] Noto Sans JP / 全丸ゴシック
  - [x] 右下のトップに戻るボタンは青いセクションに入ってからふわっと表示させる
  - [x] ヘッダー追従
  - [x] SPファースト
- **コンソールエラー**
  - [x] 検証ツールで確認
- **表示崩れ**
  - [x] インナー幅以上(1920px)
  - [x] ブレイクポイント+1px
  - [x] ブレイクポイント-1px
  - [x] 375px
  - [x] 320px
- **フォントの反映**
  - [x] 「WhatFont（Chromeのプラグイン）」で確認
- **画像について**
  - [x] 画像最適化（最適な形式で書き出されているかどうか）
写真などはwebp、jpg、png、ロゴなどベクター画像にすべきものはsvg
  - [x] FV、MV以外に遅延処理を行なっているか
  - [x] 2倍書き出し→圧縮して表示（Retinaディスプレイ対応）
  - [x] alt確認（figureタグ内）
  - [x] 不要な画像の削除
- **スクリプトタグ**
  - [x] 最初の表示に関係のないスクリプトタグについて遅延処理を行なっているか
- **アニメーション**
  - [x] 動きが仕様通りになっている
  - [x] 不自然な動きがない
  - [x] ホバー時のカーソルはポインター
  - [x] リンクチェック
- **metaタグ**
  - [ ] OGPタグ
  - [x] faviconの有無
- **閉じタグチェック**
  - [x] 「HTMLエラーチェッカー（Chromeのプラグイン）」で確認
- **HTML・CSSの文法**
  - [x] HTML
  - [x] CSS