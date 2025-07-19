---
notion_id: ac43d17a-2a5c-4165-b524-74900c1ef8a6
account: Secondary
title: WordPressのインポート時間を増やす
url: https://www.notion.so/WordPress-ac43d17a2a5c4165b52474900c1ef8a6
created_time: 2022-08-18T12:10:00.000Z
last_edited_time: 2022-08-18T12:11:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.475190
---
# WordPressのインポート時間を増やす

.htaccessファイルに以下を追加
```php
php_value max_execution_time 60
php_value max_input_time -1
php_value upload_max_filesize 20M
php_value post_max_size 20M
```
最後は改行すること！