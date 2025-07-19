---
notion_id: b0ed0d5f-33fd-46ed-a309-53ebc5c5b648
account: Secondary
title: @keyframes にradial-gradient（グラデーション）は効かない
url: https://www.notion.so/keyframes-radial-gradient-b0ed0d5f33fd46eda30953ebc5c5b648
created_time: 2023-05-07T07:52:00.000Z
last_edited_time: 2023-05-07T08:03:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.448413
---
# @keyframes にradial-gradient（グラデーション）は効かない

解決策としては
グラデーション自体の幅を広くし、見えている位置を移動させる
```scss
.c-loginBtn {
  display: inline-block;
  background: linear-gradient(90deg, rgba(162, 99, 223, 1) 0%, rgba(50, 61, 186, 1) 40%, rgba(71, 68, 192, 1) 60%, rgba(162, 99, 223, 1) 100%);
  border: 1px solid rgba(170, 118, 255, 0.5);
  background-position: 99% 50%;
  background-size: 200% auto;
  transition: all .3s;
}
.c-loginBtn:hover {
  background-position: 1% 50%;
}
```
```php
<a href="<?php echo $login ?>" class="c-loginBtn">ログアウト<span class="c-loginBtn__icon"></span></a>
```