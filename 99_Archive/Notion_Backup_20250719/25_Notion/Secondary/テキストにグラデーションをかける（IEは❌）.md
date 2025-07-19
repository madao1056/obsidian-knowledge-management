---
notion_id: ab10ffe1-8fbf-417f-9438-cbc7bf8714fd
account: Secondary
title: テキストにグラデーションをかける（IEは❌）
url: https://www.notion.so/IE-ab10ffe18fbf417f9438cbc7bf8714fd
created_time: 2023-07-29T00:45:00.000Z
last_edited_time: 2023-07-29T00:55:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.432482
---
# テキストにグラデーションをかける（IEは❌）

```html
<h2 class="c-txtGrad">movie</h2>
```
```scss
.c-txtGrad {
//グラデーションの範囲を文字幅に
  display: inline-block;
//背景にグラデーションを適用する
  background: linear-gradient(270deg, rgba(104, 149, 253, 1) 0%, rgba(227, 106, 123, 1) 100%);
//背景を文字の形に切り取る
  -webkit-background-clip: text;
//文字を透明にする
  -webkit-text-fill-color: transparent;
}
```