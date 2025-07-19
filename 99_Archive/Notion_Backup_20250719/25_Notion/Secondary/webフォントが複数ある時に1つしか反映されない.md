---
notion_id: b77a583b-006b-4875-ac51-3859b2a1ac10
account: Secondary
title: webフォントが複数ある時に1つしか反映されない
url: https://www.notion.so/web-1-b77a583b006b4875ac513859b2a1ac10
created_time: 2023-05-07T07:52:00.000Z
last_edited_time: 2023-07-12T13:06:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.439571
---
# webフォントが複数ある時に1つしか反映されない

Webフォントを複数読み込む際に、Google fontsでまとめて1つのコードが生成されるが、そのまま使うと、先頭に書かれているものだけしか反映されない。
【原因】該当の読み込み部分
最後の部分に`array(), '1.0.1', 'all’`と書いていたのが原因だったみたい（cssの読み込みなどに使用しているもの）
```php
function my_script_init()
{

wp_register_style( 'googleFonts',
	'https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700&family=Noto+Serif+JP:wght@300;400;500&display=swap'
	array(), '1.0.1', 'all');
}
add_action('wp_enqueue_scripts', 'my_script_init');
```
【解決策】`array()〜`を削除、もしくは`array(),null`とする
```php
function add_google_fonts() {
	wp_register_style( 'googleFonts',
	'https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700&family=Noto+Serif+JP:wght@300;400;500&display=swap');
	wp_enqueue_style( 'googleFonts');
	}
	add_action( 'wp_enqueue_scripts', 'add_google_fonts' );


または
function my_script_init()
{
wp_enqueue_style( 'googleFonts');( 'googleFonts',
	'https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700&family=Noto+Serif+JP:wght@300;400;500&display=swap', array(), null);
}
add_action('wp_enqueue_scripts', 'my_script_init');
```