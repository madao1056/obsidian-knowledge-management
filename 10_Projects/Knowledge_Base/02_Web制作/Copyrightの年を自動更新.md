---
notion_id: cadd896f-e9a3-42fc-bc06-4c53490f2ba6
account: Secondary
title: Copyrightの年を自動更新
url: https://www.notion.so/Copyright-cadd896fe9a342fcbc064c53490f2ba6
created_time: 2022-05-08T23:54:00.000Z
last_edited_time: 2022-05-08T23:54:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.512247
---
# Copyrightの年を自動更新

```php
<!-- 自動更新なし -->
<small class="">©2019 - 2022 じゅんぺいブログ</small>

<!-- 自動更新あり -->
<small class="">©2019 - <?php echo date('Y'); ?> じゅんぺいブログ</small>
```
Yが小文字でyだと、2022の場合は22となるので注意。
開設した年は残しておくので、後ろの年だけ自動更新する。

## タグ

#Web制作 

## 関連ドキュメント

- [[../99_その他/ブログ.md|ブログ]]
- [[../99_その他/じゅんぺいブログ.md|じゅんぺいブログ]]
- [[../99_その他/y.md|y]]
