---
notion_id: 70179b4c-3c2a-46a8-a229-386548451d21
account: Secondary
title: Advanced Custom Fields（ACF）
url: https://www.notion.so/Advanced-Custom-Fields-ACF-70179b4c3c2a46a8a229386548451d21
created_time: 2022-05-08T23:54:00.000Z
last_edited_time: 2022-05-08T23:54:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.507678
---
# Advanced Custom Fields（ACF）

  管理画面の設定では、返り値のフォーマットは「配列」がおすすめ
  ```php
<!-- 配列の場合 -->
<?php $image = get_field('フィールド名'); if( !empty($image) ): ?>
  <img src="<?php echo $image['url']; ?>" alt="<?php echo $image['alt']; ?>" />
<?php endif; ?>
  ```
  ```php
<!-- URLの場合 -->
<?php if( get_field('フィールド名') ): ?>
  <img src="<?php the_field('フィールド名'); ?>" />
<?php endif; ?>
  ```
  ```php
<!-- IDの場合 -->
<?php 
  $image = get_field('フィールド名');
  $size = 'full';
  if( $image ) {
    echo wp_get_attachment_image( $image, $size );
  }
?>
  ```
  関連記事とは、おすすめしたい記事などを自分で選択出来る機能。
  ```php
<!-- 関連記事 -->
<?php
	if( wp_is_mobile() ){
	  $num = 4; // スマホの表示数(全件は-1)
	} else {
	  $num = 8; // PCの表示数(全件は-1)
	}
  $related_posts = get_post_meta($post->ID, 'フィールド名', true);
  if ( $related_posts ) :
  $args = array(
		'post_type' => array( 'blog','news' ), // カスタム投稿タイプスラッグ(通常投稿のみならこの行は不要)
    'posts_per_page' => $num, // 表示件数
    'post__in'  => $related_posts,
  );
  $the_query = new WP_Query($args); 
  if ( $the_query -> have_posts() ) :
?>
<?php 
  while ( $the_query -> have_posts() ): $the_query -> the_post();
?>
<!-- ループさせたい処理 -->
<?php
  endwhile;
  wp_reset_postdata();
  endif;
  endif;
?>
  ```
  ```php
<div class="">
  <?php if( get_field('フィールド名') == "選択肢1") : ?>
  <div class="">
		選択肢1が選択された時に表示する内容
  </div>
  <?php elseif( get_field('フィールド名') == "選択肢2"): ?>
  <div class="">
		選択肢2が選択された時に表示する内容
	</div>
	<?php elseif( get_field('フィールド名') == "選択肢3"): ?>
  <div class="">
		選択肢3が選択された時に表示する内容
	</div>
  <?php endif; ?>
</div>
  ```
  
  ACFの編集画面が以下の場合、ページの編集画面とコードは次のようになります。
  ![](https://prod-files-secure.s3.us-west-2.amazonaws.com/d58fe38c-a9d4-4466-aed9-85604b7b2c6d/79d8ad6e-4d40-4dd0-9e11-dd085a827bea/ACF1.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAHCEQVT%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T060443Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCrKy73x06NXW31nPbhPAYvAbpqnxmBpeEhZmU4YHHX%2BgIgFW1YFBoqrJZ5V6cf0qZtPh9I%2FdCJaCurI26x8k7DWlcqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHVFOpyHsQgsbyZDyircA9nrbw6LU9GCAnhPsANWtKpVIjHghwNwC3hZACK3p%2FenFPMEVbEOPCpydyYTuxBieg2XeCE2zk4D6SrxFJvKMBiFQ4dO8WgrdELymRiL%2FtgnwVrr8zuMBkP9vjUeoXKhBpzwwtOuugvM0EVmtHZ8D5oNmBvETQL%2Bu9gy1GWVcbts2VEOP7YVZ95t%2BptriKmfNB%2Bv5AorxMYQ5w6Ub7b4Lb15BeXBuc6Y49HJ%2B6Wyh%2FL3VLHIWslHXpqBeoxJKhK9nDfWtTxZdNNIXL%2BGFqT1u6ace6y0XDwBMWWnxWeOq6jFwqODqqZDsjVxasqNEhbnsYojikm%2Bk%2BxH6xBvYD0Rx4KApM7pvgb4WRMm%2FUIU0GR%2BPk7V0EGhFqupVjGAbBxiDdGwahZAPPuSnE40gTRD2YhHR6Dchv4WQDocSUU%2FwWQ0YETpJiaC%2FTIanJG0NkSFbkl5Wz5LwQs2xP2kSRyjYf5ieMB%2BLrx%2FJpHMRyoxuUesKzX%2B7nSEtJPgFChD6V8Z5R2WhT%2F90tWP5yVB1LhBDutZQMI0X9HO0c2dCyWqEGo%2FDhmeolwT9%2BvX7tvIH4%2Fw86bqAqKSqfO5idaA0JwE3EO71b1oQ99PtifF0lzd%2FR7TSZu%2Fz4bfIFuoc4WtMJ3G7MMGOqUBuVFcb8xV8pcKxpO5aZ0hwLdNqNQSkYDfTDqD8KPTItL0qf5gxKAM%2BBImRX0XQHW7H1lEPzGznqisgU%2B6%2F8NGZ6OE15ABNyY%2FBlAERfaV72w10stXLrJ8OfTql5%2B2D%2FjWz1rTj27fzNp89zBIKkocgi%2FIcDVY%2Bg9YPA6KByVY9%2FY7x4xy%2FINKzw96WM32%2BrHHjzxrKcR1VS0qDuO0DX9o9JbmbCCm&X-Amz-Signature=32d40c989ec12c19e77b5658de9b1eac7e1433d0367fa36e798dad5e6d151e58&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
  
  これがページの編集画面。
  ![](https://prod-files-secure.s3.us-west-2.amazonaws.com/d58fe38c-a9d4-4466-aed9-85604b7b2c6d/088fae75-5aa6-4a5b-9fab-80a19825dda3/ACF2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAHCEQVT%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T060443Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCrKy73x06NXW31nPbhPAYvAbpqnxmBpeEhZmU4YHHX%2BgIgFW1YFBoqrJZ5V6cf0qZtPh9I%2FdCJaCurI26x8k7DWlcqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHVFOpyHsQgsbyZDyircA9nrbw6LU9GCAnhPsANWtKpVIjHghwNwC3hZACK3p%2FenFPMEVbEOPCpydyYTuxBieg2XeCE2zk4D6SrxFJvKMBiFQ4dO8WgrdELymRiL%2FtgnwVrr8zuMBkP9vjUeoXKhBpzwwtOuugvM0EVmtHZ8D5oNmBvETQL%2Bu9gy1GWVcbts2VEOP7YVZ95t%2BptriKmfNB%2Bv5AorxMYQ5w6Ub7b4Lb15BeXBuc6Y49HJ%2B6Wyh%2FL3VLHIWslHXpqBeoxJKhK9nDfWtTxZdNNIXL%2BGFqT1u6ace6y0XDwBMWWnxWeOq6jFwqODqqZDsjVxasqNEhbnsYojikm%2Bk%2BxH6xBvYD0Rx4KApM7pvgb4WRMm%2FUIU0GR%2BPk7V0EGhFqupVjGAbBxiDdGwahZAPPuSnE40gTRD2YhHR6Dchv4WQDocSUU%2FwWQ0YETpJiaC%2FTIanJG0NkSFbkl5Wz5LwQs2xP2kSRyjYf5ieMB%2BLrx%2FJpHMRyoxuUesKzX%2B7nSEtJPgFChD6V8Z5R2WhT%2F90tWP5yVB1LhBDutZQMI0X9HO0c2dCyWqEGo%2FDhmeolwT9%2BvX7tvIH4%2Fw86bqAqKSqfO5idaA0JwE3EO71b1oQ99PtifF0lzd%2FR7TSZu%2Fz4bfIFuoc4WtMJ3G7MMGOqUBuVFcb8xV8pcKxpO5aZ0hwLdNqNQSkYDfTDqD8KPTItL0qf5gxKAM%2BBImRX0XQHW7H1lEPzGznqisgU%2B6%2F8NGZ6OE15ABNyY%2FBlAERfaV72w10stXLrJ8OfTql5%2B2D%2FjWz1rTj27fzNp89zBIKkocgi%2FIcDVY%2Bg9YPA6KByVY9%2FY7x4xy%2FINKzw96WM32%2BrHHjzxrKcR1VS0qDuO0DX9o9JbmbCCm&X-Amz-Signature=83c0763d9d8618012274b38cb48765f0828a6dc16f37ca66cd67d26a5f60f28e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
  
  表示する内容はテキストや画像など何でもOK
  ```php
<div class="">
  <?php if( get_field('dog-size') == "大型犬") : ?>
  <div class="">
    大型犬が選択された時に表示する内容
  </div>
  <?php elseif( get_field('dog-size') == "中型犬"): ?>
  <div class="">
    中型犬が選択された時に表示する内容
  </div>
  <?php elseif( get_field('dog-size') == "小型犬"): ?>
  <div class="">
    小型犬が選択された時に表示する内容
  </div>
  <?php endif; ?>
</div>
  ```
  以下のコードだけではテキストなどがそのまま出力されるので、
  divタグやpタグで囲んでスタイルをあてやすくするのがおすすめ。
  ```php
<!-- テキスト -->
<?php the_field( 'フィールド名' ); ?>

<!-- テキストエリア -->
<?php the_field( 'フィールド名' ); ?>
※ 編集画面の改行で「**自動的に<br>に変換**」を選択しないと改行しない

<!-- Wysiwyg エディタ -->
<?php the_field( 'フィールド名' ); ?>

<!-- メール -->
<?php the_field( 'フィールド名' ); ?>
※ メールアドレスの書式以外はエラー

<!-- URL -->
<?php the_field( 'フィールド名' ); ?>
※ URLの書式以外はエラー

<!-- 数値 -->
<?php the_field( 'フィールド名' ); ?>
※ 半角の数以外はエラー

<!-- Select -->
<?php the_field( 'フィールド名' ); ?>

<!-- ラジオボタン -->
<?php the_field( 'フィールド名' ); ?>

<!-- チェックボックス -->
【カンマ区切りで出力(非推奨)】
<?php the_field( 'フィールド名' ); ?>

【ulとliで出力】
<?php
  $check = get_field('フィールド名');
  if ($check):
?>
<ul class="">
  <?php foreach ($check as $check) : ?>
  <li class="">
    <?php echo $check; ?>
  </li>
  <?php endforeach; ?>
</ul>
<?php endif; ?>

<!-- 真/偽 -->
<?php if(get_field( 'フィールド名' )): ?>
<div class="">出力したい内容</div>
<?php endif; ?>


  ```
  
  フィールドタイプをURLにして以下のようにすれば可能
  ```php
<section style="background-image:url(<?php the_field('フィールド名'); ?>);">
</section>
  ```
  