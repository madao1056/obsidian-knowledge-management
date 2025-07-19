---
notion_id: 60e067cb-caeb-4269-9fea-8abbfed23d57
account: Secondary
title: 固定ページ以外の繰り返し（header.phpやhome.phpなど）
url: https://www.notion.so/header-php-home-php-60e067cbcaeb42699fea8abbfed23d57
created_time: 2022-05-08T23:54:00.000Z
last_edited_time: 2022-05-08T23:54:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.503080
---
# 固定ページ以外の繰り返し（header.phpやhome.phpなど）

```php
//Smart Custom Fieldsのオプション繰り返し(functions.php)
  /**
   * @param string $page_title ページのtitle属性値
   * @param string $menu_title 管理画面のメニューに表示するタイトル
   * @param string $capability メニューを操作できる権限（manage_options とか）
   * @param string $menu_slug オプションページのスラッグ。ユニークな値にすること。
   * @param string|null $icon_url メニューに表示するアイコンの URL
   * @param int $position メニューの位置
   */
  SCF::add_options_page( 'ページタイトル', 'メニュータイトル', 'manage_options', 'theme-options' );
```
```php
<!-- ページテンプレート(header.phpなど) -->
<ul class="">
  <?php
    $repeat_item = SCF::get_option_meta( 'theme-options', 'フィールドグループ名' );
    foreach ( $repeat_item as $field_name => $field_value ) {
  ?>
  <li class="">
    <a href="" class="">
			<?php echo esc_html( $field_value['フィールド名'] ); ?>
		</a>
  </li>
  <?php } ?>
</ul>
```
詳細は以下の記事を参照
[Bookmark](https://junpei-sugiyama.com/smart-custom-fields-common/)

## タグ

#Web制作 

## 関連ドキュメント

- [[../02_Web制作/functions.php.md|functions.php]]
- [[../02_Web制作/header.php.md|header.php]]
- [[../02_Web制作/home.php.md|home.php]]
- [[../99_その他/固定ページ.md|固定ページ]]
- [[../99_その他/タイトル.md|タイトル]]
