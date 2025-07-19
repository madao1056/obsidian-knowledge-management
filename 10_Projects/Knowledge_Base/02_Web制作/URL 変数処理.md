---
notion_id: 03933e30-d31d-4dcf-879e-78833b3b8999
account: Secondary
title: URL 変数処理
url: https://www.notion.so/URL-03933e30d31d4dcf879e78833b3b8999
created_time: 2022-04-29T00:12:00.000Z
last_edited_time: 2023-07-27T15:41:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.434805
---
# URL 変数処理

```php
<?php
$home = esc_url( home_url( '/' ) );
$about = esc_url( home_url( '/about/' ) );
$works = esc_url( home_url( '/works/' ) );
$culture = esc_url( home_url( '/culture/' ) );
$topics = esc_url( home_url( '/topics/' ) );
$contact = esc_url( home_url( '/contact/' ) );
?>

<a href="<?php echo $about ?>" class="c-btn">read more</a>
```

## タグ

#Web制作 

## 関連ドキュメント

- [[../99_その他/top.md|top]]
- [[../99_その他/y.md|y]]
