---
notion_id: 2f725789-fa67-45b5-a5c1-4e6de7f13266
account: Secondary
title: Gulp環境でメディアクエリをまとめて生成したcssファイルを作成する
url: https://www.notion.so/Gulp-css-2f725789fa6745b5a5c14e6de7f13266
created_time: 2023-05-27T15:42:00.000Z
last_edited_time: 2024-05-27T20:05:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.394388
---
# Gulp環境でメディアクエリをまとめて生成したcssファイルを作成する

全体説明動画
参考画像
---
### 🔹背景
- 生成されるcssファイルのメディアクエリを一つにまとめたい
- 先方の仕様が絡むと、時々必要になる
---
### 🔹考え方
- ファイルのサイズはさほど変わらない。20KB〜40KB少なくなる程度
---
### 🔹実装方法
1. 動画もつける
### 🔹コード
- gulpfile.js
  ```javascript
const mqpacker = require('css-mquery-packer'); //メディアクエリまとめ

//適切な箇所に追加"},browsers)"直後
,mqpacker()
  ```
- package.json
  ```javascript
//devDependenciesに追加
"css-mquery-packer": "^1.2.0",
  ```
  

## タグ

#Web制作 

## 関連ドキュメント

- [[../99_その他/y.md|y]]
- [[../02_Web制作/Brain購入特典.md|Brain購入特典]]
- [[../02_Web制作/管理画面の「投稿」名を変更したり、使わないカテゴリーやタグを非表示にする.md|管理画面の「投稿」名を変更したり、使わないカテゴリーやタグを非表示にする]]
- [[../02_Web制作/ブログ系サイト制作.md|ブログ系サイト制作]]
- [[../02_Web制作/MIS様.md|MIS様]]
