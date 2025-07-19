---
notion_id: 772f7401-4cda-496d-b617-fcf587f96598
account: Secondary
title: アンカーリンクが設定したidの位置とズレる
url: https://www.notion.so/id-772f74014cda496db617fcf587f96598
created_time: 2024-02-28T13:26:00.000Z
last_edited_time: 2024-02-28T13:31:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.396993
---
# アンカーリンクが設定したidの位置とズレる

- エラー
  別ページへ遷移した時のアンカーリンクがズレてしまう。
- 現状（状態）
  画像の高さをCSSで固定していない
  HTMLファイルには幅と高さを書いている
- 解決策
  画像に以下をつけて比率で高さを管理する
  ```css
max-width:〇〇;
width:100%;
aspect-ratio:〇/〇;
  ```

## タグ

#Web制作 

## 関連ドキュメント

- [[../99_その他/x.md|x]]
- [[../99_その他/y.md|y]]
