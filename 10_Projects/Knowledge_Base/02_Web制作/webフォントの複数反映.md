---
notion_id: 37bfbb80-071d-4814-b814-fd0fd3d66955
account: Secondary
title: webフォントの複数反映
url: https://www.notion.so/web-37bfbb80071d4814b814fd0fd3d66955
created_time: 2023-08-17T05:40:00.000Z
last_edited_time: 2023-09-07T15:14:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.425224
---
# webフォントの複数反映

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