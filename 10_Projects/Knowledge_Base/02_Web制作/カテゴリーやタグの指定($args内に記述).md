---
notion_id: afbe7142-73bd-4814-88b5-74a90d3362da
account: Secondary
title: カテゴリーやタグの指定($args内に記述)
url: https://www.notion.so/args-afbe714273bd481488b574a90d3362da
created_time: 2022-05-08T23:54:00.000Z
last_edited_time: 2022-05-08T23:54:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.506709
---
# カテゴリーやタグの指定($args内に記述)

※スラッグ名やIDなどは仮です。
```php
/* 通常の投稿、カスタム投稿共通 */
$args = array(
	/* 表示順 */
	'orderby' => 'title', // タイトル順
	'orderby' => 'rand', // ランダム(更新するたびに変わる)
	'orderby' => 'ID', // ID順
	'orderby' => 'author', // 著者順
	'orderby' => 'name', // スラッグ順
	'orderby' => 'type', // 投稿タイプ順
);

/* 通常の投稿 */
$args = array(
	/* カテゴリーの指定 */
	'cat' => 3, // カテゴリーIDを指定
	'cat' => -3, // カテゴリーIDを指定して除外
	'cat' => array( 3, -5 ), // カテゴリーIDを複数指定(除外するカテゴリーは -(マイナス)を付ける)
	'category_name' => 'blog', // カテゴリースラッグを指定(カテゴリースラッグ'blog'の場合)
	'category_name' => 'blog, news', // カテゴリースラッグを複数指定
	'category__and' => array( 3, 5 ), // カテゴリーID3かつ5
	'category__in' => array( 3, 5 ), // カテゴリーID3または5
	'category__not_in' => array( 3, 5 ), // カテゴリーID3と5以外
	/* タグの指定 */
	'tag_id' => 5, // タグIDを指定
	'tag' => 'blog, news', // タグスラッグを指定（blogまたはnews）
	'tag' => 'blog + news', // タグスラッグを指定（blogかつnews）
	'tag__and' => array( 3, 5 ), // タグID3かつ5
	'tag__in' => array( 3, 5 ), // タグID3または5
	'tag__not_in' => array( 3, 5 ), // タグID3と5以
	'tag_slug__and'=> array( 'blog', 'news' ), // タグスラッグを指定（blogかつnews）
	'tag_slug__in'=> array( 'blog', 'news' ), // タグスラッグを指定（blogまたはnews）
);

/* カスタム投稿 */
$args = [
  'tax_query' => array(
    array(
      'taxonomy' => 'blog_category', // タクソノミーを指定(タクソノミースラッグ)
			'field' => 'id', // タームをIDで指定する場合に書く
			'field' => 'slug', // タームをスラッグで指定する場合に書く
			'terms' => array( 3, 5 ), // タームをIDで指定
			'terms' => array( 'blog', 'news' ), // タームをスラッグで指定
			'operator' => 'AND', // termsが複数ある時の条件(全て含む)
			'operator' => 'IN', // termsが複数ある時の条件(いずれかを含む,)
			'operator' => 'NOT IN', // termsが複数ある時の条件(含まない)
    ),
  )
];

/* カスタム投稿での条件の組み合わせ */
$args = [
  'tax_query' => array(
		'relation' => 'AND', // 条件1と条件2を全て含む投稿を表示
		'relation' => 'OR', //  条件1と条件2どちらかを含む投稿を表示
		/* 条件1 */
    array(
			'taxonomy' => 'blog_category', // タクソノミーを指定(タクソノミースラッグ)
      'field' => 'id', // タームをIDで指定する場合に書く
			'terms' => array( 3, 5 ), // タームをIDで指定
    ),
		/* 条件2 */
		array(
			'taxonomy' => 'news_category', // タクソノミーを指定(タクソノミースラッグ)
	    'field' => 'slug', // タームをスラッグで指定する場合に書く
			'terms' => array( 'area', 'weather' ), // タームをスラッグで指定
    ),
  )
];
```
## カテゴリーやタグのIDやスラッグの確認方法
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/d58fe38c-a9d4-4466-aed9-85604b7b2c6d/36d2cf5e-8112-4ec5-8837-b5a07ae7ce9d/%E3%82%AB%E3%83%86%E3%82%B3%E3%82%99%E3%83%AA%E3%83%BCID%E3%81%AE%E7%A2%BA%E8%AA%8D.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FAOC6X5%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T062801Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD9H4dyFDcOLq97IkmWYORPzftVWtCSQIa3n4pxxBdt9gIgd0F783QRCqdaYqz4rlVq2da5u0RYzv73BwifU0JaqGcqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKqNDsPsQg463PtjayrcA4TeXKnHsMYlARcxjRK6z0EzVuu1Ge2MH8PY7qYhdFJCGOHLZ%2F2X1uMafmBu3aVm%2F2ieNZ04d9Z4728meMvuC7Y6S4PT%2FNcF2dwGns9sbwMWsx1i8E%2FrBRxy1sk8BBr%2BYUf%2BJNah9%2FJxvQmuTYyNpamblJ6eP2tstURJqj8xp1DjA0VTi2XigmCfjqe7FNrRfAet6KsRfZtOpZ36O85CRkyjZluW4hTGaeoSY5NuLWznmPlxjMm5Bb%2BFfyJexAC41gkNmYYDqoxIIZXv4dlfg3BtqHPdM0OaTeDado07bLE9BHMPQ7EJBpgux%2BPbZ8kLAJJEoVgtMi5yaG63Q3wmGPvRohLQoeOk2QlNG7V3Gvhw9%2BIlXfKHFvOMZZkuSeYSlPIV5JzGRy9Ekfe0U2jWA3m4TXrtDGB3bSBTSFlZmb8zhw%2BfsVfALUtgjE9iNQT8xg1e2FYaaW5QmY5PuMQsLwNDMQNrcLUm66ySQKn34NTniIdRi6qyjH5zemJCn4agIgk%2BdbR53RzDNmVUJHBYQqrF59hxVrAzzOXMHJpLuBl6uKrPhwtsTz8D7%2BUW1uqMw9wxyaaHZ0JZVS6i98n8AnRVEaqJZ%2F1eBHM8T06yAN5iZW0KraNrliANLvA8MLLF7MMGOqUB%2FQrEQQsoEsybQejoYEEVMK%2BYpSXCyRjonAVp4Q5NJqoD%2BhDolKZ0Y3hCC%2BWPoty2MnSpFGrM5%2B9BR%2BYS2Poj7XvxWjhFNajyknt2QgKPnf7IF4FakRFjmSZHvZRKc9UvT%2BJkcnOY6uo9kinewCuC4rwsjN3LXvFtXANbOpJPvuvZjlxHb6AJoOam5b69xg4pyZeE%2F0MsjfVTQjrDYFX94W0XgQNM&X-Amz-Signature=4728d98271396822146c9ff9af93212b00bfaefdc026ce8b8212d8354647a049&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## タグ

#Web制作 

## 関連ドキュメント

- [[../02_Web制作/カスタム投稿.md|カスタム投稿]]
- [[../99_その他/タイトル.md|タイトル]]
- [[../99_その他/x.md|x]]
- [[../99_その他/y.md|y]]
