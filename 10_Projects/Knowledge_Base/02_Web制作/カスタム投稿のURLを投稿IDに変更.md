---
notion_id: 42b8fefd-8c8a-4fa4-b727-d0cff06a6508
account: Secondary
title: カスタム投稿のURLを投稿IDに変更
url: https://www.notion.so/URL-ID-42b8fefd8c8a4fa4b727d0cff06a6508
created_time: 2023-09-07T14:59:00.000Z
last_edited_time: 2023-09-07T15:12:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.425418
---
# カスタム投稿のURLを投稿IDに変更

直書きのカスタム投稿の場合、以下に注意（赤字の記載を必ず行う）
```plain text
function add_custom_post_type() {
  $args = array(
    'label' => 'ブック',
    'hierarchical' => false,
    'public' => true,
    'menu_position' => 5,
    'has_archive' => true,
    'show_in_rest' => true,
    'rewrite' => array('with_front' => false),
    'supports' => array(
      'title',
      'editor',
      'thumbnail'
    )
  );
  register_post_type( 'book', $args );
}
add_action( 'init', 'add_custom_post_type' );
```
**カスタム投稿タイプのパーマリンクを数字ベース(投稿ID)に変更する方法**
記述後は設定からパーマリンクの空更新を行うこと
※カスタム投稿スラッグが”book”の場合
```plain text
function book_post_type_link( $link, $post ){
  if ( $post->post_type === 'book' ) {
    return home_url( '/book/' . $post->ID );
  } else {
    return $link;
  }
}
add_filter( 'post_type_link', 'book_post_type_link', 1, 2 );

function book_rewrite_rules_array( $rules ) {
  $new_rewrite_rules = array( 
    'book/([0-9]+)/?$' => 'index.php?post_type=book&p=$matches[1]',
  );
  return $new_rewrite_rules + $rules;
}
add_filter( 'rewrite_rules_array', 'book_rewrite_rules_array' );
```

## タグ

#Web制作 

## 関連ドキュメント

- [[../02_Web制作/index.php.md|index.php]]
- [[../02_Web制作/カスタム投稿.md|カスタム投稿]]
- [[../99_その他/リンク.md|リンク]]
- [[../99_その他/x.md|x]]
- [[../99_その他/y.md|y]]
