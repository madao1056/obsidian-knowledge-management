---
notion_id: 56a44388-a50f-471e-8836-58675491ae39
account: Secondary
title: safariの青い線を消す
url: https://www.notion.so/safari-56a44388a50f471e883658675491ae39
created_time: 2022-05-08T23:54:00.000Z
last_edited_time: 2022-05-08T23:54:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.498779
---
# safariの青い線を消す

クリックやタップする箇所でsafariだと青い線が表示されます。
これを消す方法が以下になります。
```css
/* safariの青い線を消す */
*:focus {
  outline: none;
}
```