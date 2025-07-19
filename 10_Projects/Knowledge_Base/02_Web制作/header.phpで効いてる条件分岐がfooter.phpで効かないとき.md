---
notion_id: b62369c1-224d-463f-ac69-261e2c2f14af
account: Secondary
title: header.phpで効いてる条件分岐がfooter.phpで効かないとき
url: https://www.notion.so/header-php-footer-php-b62369c1224d463fac69261e2c2f14af
created_time: 2022-05-08T23:54:00.000Z
last_edited_time: 2022-05-08T23:54:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.512711
---
# header.phpで効いてる条件分岐がfooter.phpで効かないとき

“header.php では条件分岐タグが適切に機能するのに、footer.php では正しく機能しないトラブルがよくあります。これを解決するにはフッターで条件分岐タグを使う前に wp_reset_query
 を実行します”（下記記事より）
```php
<a href="<?php **wp_reset_query();** if ( is_front_page() ) : ?>#about<?php else: ?>
<?php echo esc_url( home_url( '/' ) ); ?>#about<?php endif; ?>" class="">
	ABOUTセクション
</a>
```
[Bookmark](https://wpdocs.osdn.jp/%E6%9D%A1%E4%BB%B6%E5%88%86%E5%B2%90%E3%82%BF%E3%82%B0)

## タグ

#about<?php #Web制作 

## 関連ドキュメント

- [[../02_Web制作/footer.php.md|footer.php]]
- [[../99_その他/y.md|y]]
