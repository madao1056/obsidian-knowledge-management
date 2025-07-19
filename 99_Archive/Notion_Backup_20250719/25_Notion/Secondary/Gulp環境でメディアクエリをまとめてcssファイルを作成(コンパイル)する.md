---
notion_id: f2a0ebd1-5b50-41d6-990c-8ab72b7fa54c
account: Secondary
title: Gulp環境でメディアクエリをまとめてcssファイルを作成(コンパイル)する
url: https://www.notion.so/Gulp-css-f2a0ebd15b5041d6990c8ab72b7fa54c
created_time: 2023-05-27T13:52:00.000Z
last_edited_time: 2023-06-13T03:30:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.442601
---
# Gulp環境でメディアクエリをまとめてcssファイルを作成(コンパイル)する

---
### 🔹背景
- 生成されるcssファイルのメディアクエリを一つにまとめたい
- 先方の仕様が絡むと、時々必要になる
---
### 🔹考え方
- ファイルのサイズはさほど変わらない。20KB〜40KB少なくなる程度
---
### 🔹実装方法
### 🔹コード
- gulpfile.js
  ```javascript
const mqpacker = require('css-mquery-packer'); //メディアクエリまとめ

//適切な箇所に追加  →  "},browsers)"直後
,mqpacker()
  ```
- package.json
  ```javascript
//devDependenciesに追加
"css-mquery-packer": "^1.2.0",
  ```