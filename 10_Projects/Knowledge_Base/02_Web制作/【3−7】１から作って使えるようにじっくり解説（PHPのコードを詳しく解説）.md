---
notion_id: b5d8fcc1-3fd9-47a7-984b-34b64638ae62
account: Main
title: 【3−7】１から作って使えるようにじっくり解説（PHPのコードを詳しく解説）
url: https://www.notion.so/3-7-PHP-b5d8fcc13fd947a7984b34b64638ae62
created_time: 2023-09-11T00:13:00.000Z
last_edited_time: 2023-09-11T00:13:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:15.087662
---
# 【3−7】１から作って使えるようにじっくり解説（PHPのコードを詳しく解説）

【目次】
# 今回解説すること
投稿記事のスライダーで使用しているPHPのコードを詳しく解説します。
【解説内容】
1.スライダー作成の全体像
2.front-page.phpの解説
3.p-top-post.phpの解説
4.p-splide-post.phpの解説
# スライダーで使用しているPHPのコードを詳しく解説
## 1.スライダー作成の全体像
PHPファイルを分割して、get_template_partを使用して呼び出します。
Splide.jsを使用する場合のパターンは次のとおりです。
```plain text
front-page.php
 　└-p-top-post.php
　　　　└-p-splide-post.php
```
## 2.front-page.phpの解説
コードを見やすくするため、ファイル分割して、get_template_partを使用して、呼び出しています。
get_template_partで呼び出しする際、**「.php」は記載しません**。
■front-page.php
```php
<?php get_template_part('parts/project/p-top-post'); ?>
```
## 3.p-top-post.phpの解説
- get_template_partでSplide.jsに対応したファイルを呼び出します。
- サブループ用の変数として、配列変数$argsを定義して、受渡します。
- 「post_type」に「post」を設定します。カスタム投稿の場合は、カスタム投稿タイプの設定を行います。
■parts/project/p-top-post.php
```php
<?php
global $slider_library;
$post_type = 'post';
$post_type_data = get_post_type_object($post_type);
$post_type_label = $post_type_data->labels->name;
?>
<div class="p-top-post">
  <div class="p-top-post__inner">
    <h2 class="c-common-title">EVENT</h2>
    <!-- 投稿記事のラベルをタイトルにする場合は、以下を使用します -->
    <!-- <h2 class="c-common-title"><?php //echo $post_type_label; ?></h2> -->
    <?php
    $args = array(
      'post_type' => $post_type,
      'posts_per_page' => -1, // 取得する投稿数を設定（−1は無制限）
      'order' => 'DESC', //並び順を指定
      'orderby' => 'date',  // 並び変える項目を設定
    );

    if ($slider_library === 'swiper') {
      get_template_part('parts/common/p-swiper-post', null, $args);
    } elseif ($slider_library === 'slick') {
      get_template_part('parts/common/p-slick-post', null, $args);
    } else {
      get_template_part('parts/common/p-splide-post', null, $args);
    }
    ?>
  </div>
</div>
<?php
?>
```
## 4.p-splide-post.phpの解説
### （１）$argsについて
- サブクエリで使用する「$args」にはp-top-post.phpから渡された情報がセットされています。
  ■parts/common/p-splide-post.php（抜粋）
  ```php
// 新規WP_Queryオブジェクトを作成し、クエリを実行
$the_query = new WP_Query($args);
if ($the_query->have_posts()) : // 投稿がある場合
  while ($the_query->have_posts()) :

:（省略）

	endwhile;
endif;

  ```
  
  ■参考（WP_Queryパラメータの設定）
  [Bookmark](https://developer.wordpress.org/reference/classes/wp_query/#parameters)
  
  ■参考（日本語サイト）
  [Bookmark](https://wemo.tech/160)
  
### （２）Splide用のクラスについて
- クラス名はSplide用のクラス名に設定してあります。「splide」、「splide__track」、「splide__list」、「splide__slide」は変更できません。
  ■parts/common/p-splide-post.php（抜粋）
  ```php
<div id="<?php echo esc_attr($args['post_type']); ?>" class="splide">
  <div class="splide__track">
    <div class="splide__list">

:（省略）

			<div class="splide__slide">

:（省略）

			</div>
		</div>
	</div>
</div>
  ```
  
### （３）JavaScriptで指定するセレクタについて
- JavaScriptで指定するIDは、以下で指定するIDと共通の設定にする必要があります。
■parts/common/p-splide-post.php（抜粋）
```php
<?php echo esc_attr($args['post_type']); ?>"
```
■src/js/script.js（抜粋）
```php
// Splideの読み込み
new Splide('#post',
  {
    type: 'loop',   // slide,loop,fade から選択
    speed: 3000,    // スライダーの移動時間をミリ秒単位で指定

:（省略）

}
```
### （４）記事の各フィールド情報を取得
- 記事のサムネイル、タイトルを取得します。
  ■parts/common/p-splide-post.php（抜粋）
  ```php
// 各フィールドの情報を取得
<?php if (has_post_thumbnail()) : ?>
  <div class="splide__slide">
    <a href="<?php the_permalink(); ?>">
      <?php the_post_thumbnail(); ?>
      <h3 class="c-contents-title">
        <?php the_title(); ?>
      </h3>
    </a>
  </div>
<?php endif; ?>
  ```
  
# 今回解説したこと
投稿記事のスライダーで使用しているPHPのコードを詳しく解説しました。
【解説内容】
1.スライダー作成の全体像
2.front-page.phpの解説
3.p-top-post.phpの解説
4.p-splide-post.phpの解説

## タグ

#parameters) #post', #Web制作 

## 関連ドキュメント

- [[../01_よしなに対応/「.md|「]]
- [[../01_よしなに対応/slick.md|slick]]
- [[../02_Web制作/swiper.md|swiper]]
- [[../02_Web制作/サブループ.md|サブループ]]
- [[../02_Web制作/front-page.php.md|front-page.php]]
