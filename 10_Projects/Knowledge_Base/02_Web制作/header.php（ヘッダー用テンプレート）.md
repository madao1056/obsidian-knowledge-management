---
notion_id: f6f48555-fae4-45da-856a-509f1f81a144
account: Secondary
title: header.php（ヘッダー用テンプレート）
url: https://www.notion.so/header-php-f6f48555fae445da856a509f1f81a144
created_time: 2022-05-08T23:54:00.000Z
last_edited_time: 2022-05-08T23:54:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.506902
---
# header.php（ヘッダー用テンプレート）

```php
<!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
	<meta charset="<?php bloginfo( 'charset' ); ?>" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="format-detection" content="telephone=no" />
  <?php wp_head(); ?> <!-- これがないと色々な不具合が起きる　-->
</head>
<body <?php body_class(); ?>><?php wp_body_open(); ?>
  <header class="header">
  </header>
```

## タグ

#Web制作 

## 関連ドキュメント

- [[../02_Web制作/header.php.md|header.php]]
- [[../99_その他/scale.md|scale]]
- [[../99_その他/header.md|header]]
- [[../99_その他/y.md|y]]
- [[../99_その他/テンプレート.md|テンプレート]]
