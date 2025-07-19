---
notion_id: c60aa7d6-4fc3-4a96-9eba-672141a3c346
account: Secondary
title: ACFのカスタムフィールドでYoutube動画を表示させる
url: https://www.notion.so/ACF-Youtube-c60aa7d64fc34a969eba672141a3c346
created_time: 2022-07-31T06:43:00.000Z
last_edited_time: 2022-07-31T06:44:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.484223
---
# ACFのカスタムフィールドでYoutube動画を表示させる

ACF：フィールドタイプ→URL
```php
<?php if (get_field('movie_url')) : ?>
          <div class="single__movie">
            <?php echo $embed_code = wp_oembed_get(get_field('movie_url')); ?>
          </div>
        <?php endif; ?>
```

## タグ

#Web制作 

## 関連ドキュメント

- [[../99_その他/カスタムフィールド.md|カスタムフィールド]]
- [[../99_その他/y.md|y]]
