---
notion_id: 808de166-2172-4b8e-9770-336f22ed8ebf
account: Secondary
title: ログイン画面のWPアイコンカスタム（リンクも）
url: https://www.notion.so/WP-808de16621724b8e9770336f22ed8ebf
created_time: 2022-09-22T16:07:00.000Z
last_edited_time: 2023-07-27T15:30:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.435994
---
# ログイン画面のWPアイコンカスタム（リンクも）

functions.phpに書く
```php
//=======================
//ログイン画面のカスタマイズ
//=======================
function my_login_logo() {
  ?>
<style type="text/css">
#login h1 a {
background-image: url(<?php echo get_stylesheet_directory_uri();
?>/assets/images/common/logo.webp);
    background-size: auto;
    height: 53px;
    width: 300px;
    background-size: contain;
}
body.login {
		background-image: url(<?php echo get_stylesheet_directory_uri();
														?>/assets/images/top/top-fv.jpg);
		background-size: cover;
		background-position: center;
}
</style>
<?php
}
add_action( 'login_enqueue_scripts', 'my_login_logo' );

//ロゴ画像のリンク先変更
function login_logo_url() {
  return get_bloginfo( 'url' );
}
add_filter( 'login_headerurl', 'login_logo_url' );
```

## タグ

#login #Web制作 

## 関連ドキュメント

- [[../99_その他/top.md|top]]
- [[../99_その他/x.md|x]]
- [[../99_その他/y.md|y]]
