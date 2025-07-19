---
notion_id: e6b71dc4-d52b-4a0a-8dc1-9fcb43db3adb
account: Secondary
title: Favicon (ファビコン) 設定方法
url: https://www.notion.so/Favicon-e6b71dc4d52b4a0a8dc19fcb43db3adb
created_time: 2022-09-16T08:03:00.000Z
last_edited_time: 2022-09-16T08:04:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.472696
---
# Favicon (ファビコン) 設定方法

functions.php
```php
// 使用例：テーマ内の /img/favicon.png を指定
add_filter ( 'get_site_icon_url', 'my_site_icon_url' );

function my_site_icon_url( $url ) {
  return get_theme_file_uri ( 'img/favicon.png' );
}
```

## タグ

#Web制作 

## 関連ドキュメント

- [[../99_その他/y.md|y]]
