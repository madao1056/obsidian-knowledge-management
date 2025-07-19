---
notion_id: c1b2a43f-0abc-42f1-a202-c338c23fc082
account: Secondary
title: aタグのhrefが空の時は非表示にする
url: https://www.notion.so/a-href-c1b2a43f0abc42f1a202c338c23fc082
created_time: 2022-05-08T23:54:00.000Z
last_edited_time: 2022-05-08T23:54:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.499061
---
# aタグのhrefが空の時は非表示にする

例えばカスタムフィールドでリンク付きのバナーを表示させる箇所があるとき、href内のリンクをカスタムフィールドで設定するとします。
ただバナーを表示させない時、**何も設定していないとhref内が空でもaタグは表示されてしまいます。**
そこで以下のような設定をすればリンクが空の時はaタグごと非表示になります。
```css
/* hrefが空の時は非表示 */
a[href=""]{
  display: none;
}
```