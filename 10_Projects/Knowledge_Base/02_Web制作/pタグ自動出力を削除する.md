---
notion_id: b5909b2d-57f7-405a-b5ad-32a200c50485
account: Secondary
title: pタグ自動出力を削除する
url: https://www.notion.so/p-b5909b2d57f7405ab5ad32a200c50485
created_time: 2022-04-30T01:20:00.000Z
last_edited_time: 2023-07-27T15:41:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.434015
---
# pタグ自動出力を削除する

<details>
<summary>目次</summary>
</details>
### **固定・投稿ページ共に自動挿入を解除する**
以下のコードをfunctions.phpに追加
```php
add_action('init', function() {
remove_filter('the_excerpt', 'wpautop');
remove_filter('the_content', 'wpautop');
});
add_filter('tiny_mce_before_init', function($init) {
$init['wpautop'] = false;
$init['apply_source_formatting'] = ture;
return $init;
});
```
### **自動挿入解除を個別に指定する**
- 例)
  > 固定ページ毎に違うテンプレートを使っていて、そのテンプレートによってはpタグ挿入を解除したいというケース
  
以下のコードをそのテンプレートファイル上のpタグの自動挿入を停止させたい箇所の直前に追加
```php
<?php remove_filter('the_content', 'wpautop'); ?>
以下に下の様なコードが続きます
<?php the_content(); ?> //この本文のpタグが削除される
```
### **特定の投稿タイプでpタグの自動挿入を停止させる方法**
- 例)
  > 固定ページのみpタグの自動挿入を停止させたいケース
  
  以下のコードをfunctions.phpに追加　※「固定ページのみ」pタグの自動挿入が解除
  ```php
add_filter('the_content', 'wpautop_filter', 9);
function wpautop_filter($content) {
global $post;
$remove_filter = false;
$arr_types = array('page');//※解説に詳細記載
$post_type = get_post_type( $post->ID );
if (in_array($post_type, $arr_types)) $remove_filter = true;
if ( $remove_filter ) {
remove_filter('the_content', 'wpautop');
remove_filter('the_excerpt', 'wpautop');
}
return $content;
}
  ```
  - **コードの解説**