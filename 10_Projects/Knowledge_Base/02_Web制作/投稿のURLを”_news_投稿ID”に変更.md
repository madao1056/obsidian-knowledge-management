---
notion_id: 3a8a0923-cea4-424b-bcc9-6428b2378b14
account: Secondary
title: 投稿のURLを”/news/投稿ID”に変更
url: https://www.notion.so/URL-news-ID-3a8a0923cea4424bbcc96428b2378b14
created_time: 2023-09-07T15:53:00.000Z
last_edited_time: 2023-09-07T15:56:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.424590
---
# 投稿のURLを”_news_投稿ID”に変更

- functions.php
  ```php
//===============================
// 投稿のURLを”/news/投稿ID”に変更
//===============================
function add_article_post_permalink($permalink)
{
	$permalink = '/news' . $permalink;
	return $permalink;
}
add_filter('pre_post_link', 'add_article_post_permalink');

function add_article_post_rewrite_rules($post_rewrite)
{
	$return_rule = array();
	foreach ($post_rewrite as $regex => $rewrite) {
		$return_rule['news/' . $regex] = $rewrite;
	}
	return $return_rule;
}
add_filter('post_rewrite_rules', 'add_article_post_rewrite_rules');
  ```
WP管理画面のパーマリンク設定は
`https://sample.jp`/%post_id%/
にすること

## タグ

#Web制作 

## 関連ドキュメント

- [[../99_その他/y.md|y]]
