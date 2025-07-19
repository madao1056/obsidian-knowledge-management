---
notion_id: 95e63736-67f9-469c-b0e1-0d24b91f9540
account: Secondary
title: backgroud-imageの設定
url: https://www.notion.so/backgroud-image-95e6373667f9469cb0e10d24b91f9540
created_time: 2022-05-08T23:54:00.000Z
last_edited_time: 2022-05-08T23:54:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.502683
---
# backgroud-imageの設定

フィールドタイプをURLにして以下のようにすれば可能
```php
<section style="background-image:url(<?php the_field('フィールド名'); ?>);">
</section>
```