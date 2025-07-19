---
notion_id: 29b733c3-a638-47f6-bc54-9f1fb9edbbeb
account: Secondary
title: 記事を公開してからn日間はNew!を表示
url: https://www.notion.so/n-New-29b733c3a63847f6bc549f1fb9edbbeb
created_time: 2022-08-24T23:19:00.000Z
last_edited_time: 2023-09-07T15:16:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.425127
---
# 記事を公開してからn日間はNew!を表示

```php
<?php
$days = 7; //Newを表示させたい期間の日数
$today = date_i18n('U');
$entry = get_the_time('U');
$kiji = date('U',($today - $entry)) / 86400 ;//86400秒＝60秒×60分×24時間＝１日
if( $days > $kiji ){
echo 'New!';
}
?>
```