---
notion_id: ad982f04-2d5c-4b98-b3ad-099d45d4a575
account: Secondary
title: Contact Form7（Thanksページ有り）
url: https://www.notion.so/Contact-Form7-Thanks-ad982f042d5c4b98b3ad099d45d4a575
created_time: 2022-04-30T00:28:00.000Z
last_edited_time: 2024-09-14T05:49:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.389715
---
# Contact Form7（Thanksページ有り）

### 手順
---
---
2．ショートコードをコピー→固定ページ（お問い合わせ用）を作成→ショートコードをペースト
---
3．コードを追加して情報を反映させる

```php
<?php if (have_posts()) : ?>
	<?php while (have_posts()) : the_post(); ?>
		<?php the_content(); ?>
	<?php endwhile; ?>
<?php endif; ?>
```
---
4．自作のフォームを入れたい時はclass名を記入する
　　CSSが崩れるのはしょうがない部分もあるので都度修正。
　　Contact From7のclass名使用で一つデザインを作っておくと便利かも
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/d58fe38c-a9d4-4466-aed9-85604b7b2c6d/1558d39c-395c-4421-ac5b-e48740e2f2bb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665OG2PBGE%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T060536Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCe%2Bt2VdJWtxIhWefdt8rS%2Bf5CyE11I0kR6coZnx6oFUAIhAJYt9xA0iLhvGYnXcYNugTd9SY2n3p8EMnOf2ulv3beBKogECJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy3XiAW9W%2FS7jhW2vQq3APP255p%2BFvgYQlSOIW7P539ud5jOm6mmRtOR7NbWLk2ktYa5S7Q3AA%2FzYH%2F4voytOLfaWjiqe%2FEQdb3m9r67p9bJaR1k6RjuOHPhfr%2BxLYmfAFW2tBu39kAwRUF83zQEMxNuzPiQf8jxOJWVY8ZaItrC4JDCE5CIuZfZ1ynP7c5U%2FMoGoGSV%2F3uW8bCRB%2BQ%2F5j3PBa%2BdeXCrc%2BLf9Q0pfVu0R2ARBDaX5uB%2BJdPJrA%2BvXpblUoKRJJOXqUg%2B6SiRmZUagFSB95jvWCBeRERMjnUfe7P6wLu6%2BtrAKmCQRG3lixr6JgqXH%2FasnE7bcQnUX0ElJrMmK8zK4zkGQ3rsrSGQ4H7WoYsIBF848ZjgWnor%2BQc89HIKWN06KFUuMvf%2BhJ7vzz3r%2Fr%2B%2FjMxLYeM4BBozIahs8%2FYFiSY9fiQTKmfidfHvsGmwKWo2ZAuT0xp7SpVMUtjb8zvsetKHW8lj9lzRNjKY4vfz1A4lSkDdh9ftB8Ub3jSxwHAIyjU19YfL6fav%2Fvq%2Fk4R1epBUfdG4OzVCSOAb9QEvo6Fvsp%2B7tMkplZR4p73OUeaIxkJ%2FmMIZ%2F3fdMkMTKCWxM83FKHlMyPIYLf6nKEtHyCcAyBCg3nSCLvpxXjol4Q26RXVSDD%2BxezDBjqkAe%2FV%2BooRcbafnwJFoCTmshWT4JwN%2FSRQL5AivCaY8XallgIT30VVmQwsu5FJ%2BcwNE8Qwak3uuR6Vy3Eq%2F6mq6zL4ZxjVutb2zWdaa0abH%2FkCQamWRKBIYzlqmwzIZ%2FFvj6TeRv9X1Q%2FquAd89DPC%2BsI3sNEG72BnWh8snr7tQwqZPMgo1FbvZ2PP5yjl%2F94OvNU9aPqMmxcbFuSTs4Pu6hVDANnA&X-Amz-Signature=34d88c9b1a6faaada7c339e5f74644123b25fb3a4964abb860e8b589d3ef5c54&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
5．Contact Form7内でスタイル調整
　管理画面内で書くとW3Cエラーになるので、通常通り、cssファイルに書いた方がよい。
---
functions.phpにて、thanksページに遷移させる方法。
```php
add_action('wp_footer', 'redirect_to_thanks_page');
function redirect_to_thanks_page() {
  $homeUrl = home_url();
  echo <<< EOD
    <script>
      document.addEventListener( 'wpcf7mailsent', function( event ) {
        location = '{$homeUrl}/thanks/';
      }, false );
    </script>
  EOD;
}
```
---
*contact form7 pタグ自動出力を削除*
```php
//===============================
// contact form7 pタグ削除
//===============================
add_filter('wpcf7_autop_or_not', 'wpcf7_autop_return_false');
function wpcf7_autop_return_false() {
  return false;
}
```

## タグ

#Web制作 

## 関連ドキュメント

- [[../02_Web制作/デザイン.md|デザイン]]
- [[../02_Web制作/contact form.md|contact form]]
- [[../02_Web制作/functions.php.md|functions.php]]
- [[../99_その他/Untitled.md|Untitled]]
- [[../99_その他/固定ページ.md|固定ページ]]
