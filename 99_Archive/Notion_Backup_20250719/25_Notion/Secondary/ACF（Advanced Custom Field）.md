---
notion_id: 0d97cc66-c492-417d-8385-e0eeb2ea6da4
account: Secondary
title: ACF（Advanced Custom Field）
url: https://www.notion.so/ACF-Advanced-Custom-Field-0d97cc66c492417d8385e0eeb2ea6da4
created_time: 2022-04-29T05:59:00.000Z
last_edited_time: 2023-07-27T15:43:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.432707
---
# ACF（Advanced Custom Field）

[動的化は８から](/0d97cc66c492417d8385e0eeb2ea6da4#0223095cf0264f08aa0d839bbb7278c3)
[ACF便利な使い方](/0d97cc66c492417d8385e0eeb2ea6da4#70060941cc294c238c3d5aeb3c4c89eb)
[＋α投稿ページのACF条件分岐](/0d97cc66c492417d8385e0eeb2ea6da4#f6f4370987944077a995f39573a46105)
### 手順
---
---
２．トップページに表示させたいので下記スクショのようにする
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/d58fe38c-a9d4-4466-aed9-85604b7b2c6d/00e48050-3fbb-4286-a7f6-e31282b154a4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WV6NF3ZS%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T060428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA7D6udSJR9pNVdOIzNZw2j1BaIi0QNSrWhY7yfBp7ZxAiA9Jt9e%2BA0gsd2GDdKp6lxrVEfsFdEC9AD0ucgJVTpWUCqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMq3qZQWeUj2Eu4CMKKtwDbf7Mx5ne9Bt57WBoo9d3Fplyx44a1GtQPk%2FgOATkfyz%2Fv1rnqMS00DTU4mMPnJ4xmvZyBQg%2B7BAUAhf9CzfffmetLnwXWE4wAm4lrp0Y3H4mpT2TMx5U0PlJZNZ1nLNpxpzeBB4KK0Xo19KByYEx%2Bioy2h%2FjheOvPSnNDo64LXEqfZG2pVGtQklOeHjDszIgpppI%2FnTb9TfyitfjChAhoAoVMN77osd%2FMaODuWgV76LIoTv6dpS20ykmazY0iTMOxdk53FNf02e54%2FYvIXz7NnbzYn9IPmx6zqsg1tAvVE2m5smm71rodWn7zwCVlRPOK%2Bk9Y0mAmCJi1AfSJV58goMQY1GhY2q0RY7QNQ%2FrIFksPayUDlZo5fnbl0Ds8jj2w7M5z0%2FdlD9RIo2wBz4Dvq%2BYtfuKuaiTf38g%2BrfrmUseZKPppcHdSFnv2xywU%2FD%2F2pfKesZ9SVqDSUaJf7r%2BZmato%2FZnFMb5q2gyOGIywjcHKQzbdgjo%2Fy2xnj2tvWsXRgTQ3XjMvPTP8nyPt20NhVd%2BlFjmoRXHOQO74Jd6rqlCoUN076uJfT%2BdaZSHvr2SPfJdnAMMnQliHMBbzmWku0915rjTlox6XNs96vBfJdMq42wV9DDQp3LYASIwnMXswwY6pgH4s0L0z%2B5F1xo%2FH239ubN33DOCuS%2FVl%2FjPDSWXQO1dRmuy%2BcUwRlAqapRVVTIw0JW5j180HJAQ1M1cYyg5%2B6o6rvuQQ0Sr1D52yyot9gJGCVyNus7M68sD7E0jZYHCiJDrVvYlH%2B5MnZzCOp2AO6UDHDDR8Df88i%2ByfpHyMaJLwYZC7sGNrQsmIcytg8p1q%2BxCTM7TgP27%2B3%2BocJSMzf3SmxUrvlhS&X-Amz-Signature=3799a866cd9359440990a862875be2e66b2c0ee4c4cb350155a0e6733f4ba3cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
---
---
５．説明文追加
---
---
---
---
`about-description`は変数を使って表示
`about_title`は直接表示（どちらでも構わない）※getは取得、theは表示
```php
<?php $about_description = get_field('about-description', 8); ?>
<h2 class="c-section-title"><?php the_field('about_title'); ?></h2>
<div class="p-about__box">
  <p class="p-about__text"><?php echo $about_description ?></p>
</div>
```
投稿IDを使うメリット
今回は同じ投稿ページ内のACFを表示しているのでIDは不要
別の投稿ページの情報を取りたい時は情報元のIDを書く必要がある
---
管理画面（固定ページ）を見やすくするACFの使い方
---
＋α投稿ページのACF条件分岐
```php
<?php if (get_field('title-1')) : ?>//title-１に値が入っていた場合に表示させる
	<div class="p-single__box01 p-box01">
		<span class="p-box01__title"><?php the_field('title-1'); ?></span>
		<p class="p-box01__text"><?php the_field('text-1'); ?></p>
	</div>
<?php endif; ?>
<?php if (get_field('title-2')) : ?>//title-2に値が入っていた場合に表示させる
	<div class="p-single__box01 p-box01">
		<span class="p-box01__title"><?php the_field('title-2'); ?></span>
		<p class="p-box01__text"><?php the_field('text-2'); ?></p>
	</div>
<?php endif; ?>
```