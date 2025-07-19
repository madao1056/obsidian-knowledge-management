---
notion_id: 7f4d589f-130e-426a-bde2-52a137192e4b
account: Secondary
title: Contact Form7の自動挿入されるpタグ削除
url: https://www.notion.so/Contact-Form7-p-7f4d589f130e426abde252a137192e4b
created_time: 2022-05-08T23:54:00.000Z
last_edited_time: 2022-05-08T23:54:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.507874
---
# Contact Form7の自動挿入されるpタグ削除

functions.phpに以下のコードを追記
```php
// ContactForm7で自動挿入されるPタグ、brタグを削除
  add_filter('wpcf7_autop_or_not', 'wpcf7_autop_return_false');
  function wpcf7_autop_return_false() {
    return false;
  }
```