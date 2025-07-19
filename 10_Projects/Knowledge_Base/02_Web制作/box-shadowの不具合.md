---
notion_id: 25d3bee6-3f4b-48cb-b476-693d6593653f
account: Secondary
title: box-shadowの不具合
url: https://www.notion.so/box-shadow-25d3bee63f4b48cbb476693d6593653f
created_time: 2023-07-26T02:46:00.000Z
last_edited_time: 2023-07-26T02:51:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.436529
---
# box-shadowの不具合

box-shadowをアニメーションにて透過させたりしていたのですが、Firefoxにて確認した際に以下のようにちらつきが。。
同じようなプロパティでdrop-shadowというものがありますが、こちらを使用することでちらつきもなくなりました！
サンプルコードはこちら
```scss
//修正前
box-shadow: 0 0 rem(20) #ffb069;

//修正後
filter: drop-shadow(0 0 rem(20) #ffb069);
```

## タグ

#ffb069); #Web制作 #ffb069; 

## 関連ドキュメント

- [[../99_その他/y.md|y]]
