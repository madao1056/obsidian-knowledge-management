---
notion_id: 5609b08f-7ea9-40aa-902b-5a436fe04f89
account: Secondary
title: Contact Form 7で、メールアドレスの確認用入力と一致チェック機能をつける
url: https://www.notion.so/Contact-Form-7-5609b08f7ea940aa902b5a436fe04f89
created_time: 2024-03-26T14:50:00.000Z
last_edited_time: 2024-03-26T14:53:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.395621
---
# Contact Form 7で、メールアドレスの確認用入力と一致チェック機能をつける

```plain text
プラグイン内の記述
<th>メールアドレス <span class="required">必須</span></th>
<td>[email* your-email]</td>
</tr>
<tr>
<th>メールアドレス確認 <span class="required">必須</span></th>
<td>[email* your-email_confirm placeholder "確認のためもう一度入力してください"]</td>
</tr>
```
```php
add_filter( 'wpcf7_validate_email', 'wpcf7_validate_email_filter_extend', 11, 2 );
add_filter( 'wpcf7_validate_email*', 'wpcf7_validate_email_filter_extend', 11, 2 );
function wpcf7_validate_email_filter_extend( $result, $tag ) {
    $type = $tag['type'];
    $name = $tag['name'];
    $_POST[$name] = trim( strtr( (string) $_POST[$name], "n", " " ) );
    if ( 'email' == $type || 'email*' == $type ) {
        if (preg_match('/(.*)_confirm$/', $name, $matches)){ //確認用メルアド入力フォーム名を ○○○_confirm としています。
            $target_name = $matches[1];
            if ($_POST[$name] != $_POST[$target_name]) {
                if (method_exists($result, 'invalidate')) {
                    $result->invalidate( $tag,"確認用のメールアドレスが一致していません");
                } else {
                    $result['valid'] = false;
                    $result['reason'][$name] = '確認用のメールアドレスが一致していません';
                }
            }
        }
    }
    return $result;
}
```

## タグ

#Web制作 

## 関連ドキュメント

- [[../02_Web制作/Contact Form 7.md|Contact Form 7]]
- [[../99_その他/x.md|x]]
- [[../99_その他/y.md|y]]
