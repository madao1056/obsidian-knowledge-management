---
notion_id: 9381b77d-a201-4f1f-8836-a35bf6ac437a
account: Secondary
title: PCとSPの表示切り替え
url: https://www.notion.so/PC-SP-9381b77da2014f1f8836a35bf6ac437a
created_time: 2022-05-08T23:54:00.000Z
last_edited_time: 2022-05-08T23:54:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.511974
---
# PCとSPの表示切り替え

```php
<?php
  $ua=$_SERVER['HTTP_USER_AGENT'];
  $browser = ((strpos($ua,'iPhone')!==false)||(strpos($ua,'iPod')!==false)||(strpos($ua,'Android')!==false));
  if ($browser == true){
  $browser = 'sp';
  }
  if($browser == 'sp'){
?>
<!-- SPで表示したいものを書く-->
<?php }else{ ?>
<!-- PCで表示したいものを書く-->
<?php } ?>
```
cssで** display: none; **を使って切り替えるより読み込み速度が早い

## タグ

#Web制作 

## 関連ドキュメント

- [[../99_その他/y.md|y]]
