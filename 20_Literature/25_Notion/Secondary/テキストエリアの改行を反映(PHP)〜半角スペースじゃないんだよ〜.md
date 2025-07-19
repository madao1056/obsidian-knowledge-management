---
notion_id: 75ceea60-3c04-4b0e-b6f3-22ee11e4d83d
account: Secondary
title: テキストエリアの改行を反映(PHP)〜半角スペースじゃないんだよ〜
url: https://www.notion.so/PHP-75ceea603c044b0eb6f322ee11e4d83d
created_time: 2023-01-14T01:17:00.000Z
last_edited_time: 2023-07-27T15:33:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.435381
---
# テキストエリアの改行を反映(PHP)〜半角スペースじゃないんだよ〜

```php
<!-- 例：繰り返しフィールド（SCF）のタイプ→テキストエリア['item-desc']に実装 -->
<?php
	$product_info = SCF::get('product-item-list_always');
  foreach ($product_info as $detail) {
?>
  <tr>
	  <th><?php echo $detail['item-name']; ?></th>
			 	<!-- echo nl2br(該当するカスタムフィールドの変数) -->
    <td><?php echo nl2br($detail['item-desc']); ?></td>
  </tr>
 <?php } ?>
```