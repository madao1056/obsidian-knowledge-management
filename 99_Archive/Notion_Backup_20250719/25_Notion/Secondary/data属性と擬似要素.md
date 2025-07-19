---
notion_id: 2c1f0c96-cc21-408d-a841-83ac2de958fc
account: Secondary
title: data属性と擬似要素
url: https://www.notion.so/data-2c1f0c96cc21408da84183ac2de958fc
created_time: 2022-11-19T00:05:00.000Z
last_edited_time: 2024-02-05T06:44:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.402593
---
# data属性と擬似要素

```html
<h2 class="c-ttl" data-en="About">私たちについて</h2>
```
```scss
.c-ttl[data-en=""]{}

.c-ttl::after {
  content: attr(data-en) "";
  color: #fcb244;
  display: block;
  font-size: 40px;
  font-weight: 300;
  font-style: italic;
  letter-spacing: 0;
  line-height: calc(48 / 40);
}
```