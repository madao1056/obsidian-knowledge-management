---
notion_id: b204d602-ebb0-46c4-b41d-5253fdfbe347
account: Secondary
title: ページ遷移なしの絞り込み検索(Ajax)
url: https://www.notion.so/Ajax-b204d602ebb046c4b41d5253fdfbe347
created_time: 2023-07-16T09:10:00.000Z
last_edited_time: 2023-09-07T15:14:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.425319
---
# ページ遷移なしの絞り込み検索(Ajax)

```php
<!-- ajax-search.php -->
<?php
$post_type = 'jobs';
$jobs_area_obj = get_field_object('jobs_area');
$jobs_area_choices = $jobs_area_obj['choices'];
$jobs_area_choices_keys = array();
foreach ($jobs_area_choices as $key => $value) {
  $jobs_area_choices_keys[] = $key;
}
$jobs_area_labels = $jobs_area_obj['value'];
$jobs_area = $_GET['jobs_area'] ?? null;
if ($jobs_area == 'all' || $jobs_area == '') {
  $jobs_area = $jobs_area_choices_keys;
}

$jobs_skills_selected = array();
$jobs_skill = array();
$jobs_skill_terms = get_terms('jobs_skill', array('orderby' => 'term_order', 'order' => 'ASC'));
$jobs_skills = $_GET['jobs_skill'] ?? null;
if ($jobs_skills) {
  foreach ((array)$jobs_skills as $value) {
    $jobs_skills_selected[] = htmlspecialchars($value);
    $jobs_skill[] = htmlspecialchars($value);
  }
} else {
  foreach ($jobs_skill_terms as $jobs_skill_term) {
    $jobs_skill[] = $jobs_skill_term->slug;
  }
}

$programmings_selected = array();
$programming = array();
$programming_terms = get_terms('programming', array('orderby' => 'term_order', 'order' => 'ASC'));
$programmings = $_GET['programming'] ?? null;
if ($programmings) {
  foreach ((array)$programmings as $value) {
    $programmings_selected[] = htmlspecialchars($value);
    $programming[] = htmlspecialchars($value);
  }
} else {
  foreach ($programming_terms as $programming_term) {
    $programming[] = $programming_term->slug;
  }
}

// フリーのキーワード検索を取得
$free_keyword = isset($_GET['s']) ? $_GET['s'] : '';

$the_query = new WP_Query(array(
  'post_status' => 'publish',
  'post_type' => $post_type,
  'tax_query' => array(
    'relation' => 'AND',
    array(
      'taxonomy' => 'jobs_skill',
      'field' => 'slug',
      'terms' => $jobs_skill,
    ),
    array(
      'taxonomy' => 'programming',
      'field' => 'slug',
      'terms' => $programming,
    )
  ),
  'meta_query' => array(
    'relation' => 'AND',
    array(
      'key' => 'jobs_area',
      'value' => $jobs_area,
      'compare' => 'IN'
    )
  ),
  's' => $free_keyword,
  'posts_per_page' => -1,
  'orderby' => 'date',
  'order' => 'DESC',
));
$search_results_count = $the_query->found_posts;
if ($search_results_count > 0) {
  echo '<p class="p-result__num">検索結果は ' . $search_results_count . ' 件です。</p>';
}

if ($the_query->have_posts()) {
  $html = '';
  while ($the_query->have_posts()) {
    $the_query->the_post();
    $jobs_title = get_the_title();
    $jobs_area = get_field('jobs_area');
    $jobs_img = get_field('jobs_img');

    $html_result = '<ul>';
    $jobs_skill_cats = wp_get_object_terms($post->ID, 'jobs_skill');
    foreach ($jobs_skill_cats as $jobs_skill_cat) {
      $jobs_skill_cat_name = $jobs_skill_cat->name;
      $html_result .= '<li>' . $jobs_skill_cat_name . '</li>';
    }
    $programming_result .= '</ul>';
    $programming_result = '<ul>';
    $programming_cats = wp_get_object_terms($post->ID, 'programming');
    foreach ($programming_cats as $programming_cat) {
      $programming_cat_name = $programming_cat->name;
      $programming_result .= '<li>' . $programming_cat_name . '</li>';
    }
    $programming_result .= '</ul>';

    $html .= '<div class="p-result__item">';
    $html .= '<div class="p-result__head">';
    $html .= '<p class="p-result__img">';
    $html .= '<img decoding="async" loading="lazy" src="' . $jobs_img . '" alt="" width="150" height="150">';
    $html .= '</p>';
    $html .= '<h2 class="p-result__ttl">' . $jobs_title . '</h2>';
    $html .= '</div>';
    $html .= '<div class="p-result__body">';
    $html .= '<table class="p-result__table">
        <tr><th>地域</th><td>' . $jobs_area . '</td></tr>
        <tr><th>スキル</th><td>' . $html_result . '</td></tr>
        <tr><th>言語</th><td>' . $programming_result . '</td></tr>
      </table>';
    $html .= '<p class="p-result__link">';
    $html .= '<a href="' . get_the_permalink() . '">詳しく見る</a>';
    $html .= '</p>';
    $html .= '</div>';
    $html .= '</div>';
  }
  echo $html;
} else {
  echo 'ありません。';
}
```
```php
<!-- archive-jobs.php -->
<?php get_header(); ?>
<section class="p-archive l-archive">
  <div class="p-archive__inner l-inner">
    <div class="p-archive__wrap p-jobs">
      <?php
      // カスタム投稿タイプ
      $post_type = 'jobs';
      ?>

      <?php
      $jobs_area_obj = get_field_object('jobs_area');
      $jobs_area_choices = $jobs_area_obj['choices'];
      $jobs_area_choices_keys = array();
      foreach ($jobs_area_choices as $key => $value) {
        $jobs_area_choices_keys[] = $key;
      }
      $jobs_area_labels = $jobs_area_obj['value'];
      $jobs_area = $_GET['jobs_area'] ?? null;
      if ($jobs_area == 'all' || $jobs_area == '') {
        $jobs_area = $jobs_area_choices_keys;
      }

      $jobs_skills_selected = array();
      $jobs_skill = array();
      $jobs_skill_terms = get_terms('jobs_skill', array('orderby' => 'term_order', 'order' => 'ASC'));
      $jobs_skills = $_GET['jobs_skill'] ?? null;
      if ($jobs_skills) {
        foreach ((array)$jobs_skills as $value) {
          $jobs_skills_selected[] = htmlspecialchars($value);
          $jobs_skill[] = htmlspecialchars($value);
        }
      } else {
        foreach ($jobs_skill_terms as $jobs_skill_term) {
          $jobs_skill[] = null;
        }
      }

      $programmings_selected = array();
      $programming = array();
      $programming_terms = get_terms('programming', array('orderby' => 'term_order', 'order' => 'ASC'));
      $programmings = $_GET['programming'] ?? null;
      if ($programmings) {
        foreach ((array)$programmings as $value) {
          $programmings_selected[] = htmlspecialchars($value);
          $programming[] = htmlspecialchars($value);
        }
      } else {
        foreach ($programming_terms as $programming_term) {
          $programming[] = null;
        }
      }

      // フリーのキーワード検索を取得
      $free_keyword = isset($_GET['s']) ?? null;
      $free_keyword_choices_keys = array();
      if ($free_keyword == '') {
        $free_keyword = $free_keyword_choices_keys;
      }
      ?>
      <div class="p-jobs_form">
        <form method="get" action="<?php echo home_url('/'); ?>jobs/">
          <div class="p-jobs_content">
            <h3 class="p-jobs_ttl">フリーワード</h3>
            <div class="p-jobs_wrap p-jobs_wrap--text">
              <input id="s-box" name="s" type="text" placeholder="キーワードを入力" />
              <!-- <button type="submit" id="s-btn-area">
                <p id="s-btn" class="p-jobs__btn">検索</p>
              </button> -->
            </div>
          </div>
          <div class="p-jobs_content">
            <h3 class="p-jobs_ttl">エリアから絞り込む</h3>
            <div class="p-jobs_wrap">
              <select name="jobs_area">
                <option value="all">すべて</option>
                <?php
                foreach ($jobs_area_choices as $key => $value) {
                  echo '<option value="' . $key . '" ';
                  if ($jobs_area) {
                    if ($key == $jobs_area) {
                      echo 'selected="selected"';
                    }
                  }
                  echo '>' . $value . '</option>';
                }
                ?>
              </select>
            </div>
          </div>
          <div class="p-jobs_content">
            <h3 class="p-jobs_ttl">スキルから絞り込む</h3>
            <div class="p-jobs_wrap p-jobs_wrap--label">
              <?php foreach ($jobs_skill_terms as $jobs_skill_term) {
                echo '<label><input type="checkbox" name="jobs_skill[]" value="' . $jobs_skill_term->slug . '" ';
                if ($jobs_skills_selected) { //選択した項目はページ遷移後 checked
                  foreach ($jobs_skills_selected as $value) {
                    if ($value == $jobs_skill_term->slug) {
                      echo 'checked';
                    }
                  }
                }
                echo '> ' . $jobs_skill_term->name . '</label>';
              } ?>
            </div>
          </div>
          <div class="p-jobs_content">
            <h3 class="p-jobs_ttl">言語から絞り込む</h3>
            <div class="p-jobs_wrap p-jobs_wrap--label">
              <?php foreach ($programming_terms as $programming_term) {
                echo '<label><input type="checkbox" name="programming[]" value="' . $programming_term->slug . '" ';
                if ($programmings_selected) { //選択した項目はページ遷移後 checked
                  foreach ($programmings_selected as $value) {
                    if ($value == $programming_term->slug) {
                      echo 'checked';
                    }
                  }
                }
                echo '> ' . $programming_term->name . '</label>';
              } ?>
            </div>
          </div>
        </form>
      </div>
      <div class="p-jobs_results p-result">
        <div class="p-result__wrap">
          <div id="search-result" class="p-result__content"></div>
        </div>
      </div>
    </div>
  </div>
</section>


<?php get_footer(); ?>
```
```php
//functions.php
//================================
// ページ遷移なしの絞り込み検索(Ajax)
//================================
/* フォームの内容を取得してAjaxに送信するプログラムが記述されたJavascriptをheadタグにキュー */
add_action('wp_enqueue_scripts', function () {
	$handle = 'search';
	$file = get_template_directory_uri() . '/assets/js/' . $handle . '.js';
	wp_register_script($handle, $file, array('jquery'), '3.6.0', true);

	$localize = [
		'ajax_url' => admin_url('admin-ajax.php'),
		'action' => 'view_search_results',
		'nonce' => wp_create_nonce('view_search_results')
	];
	wp_localize_script($handle, 'localize', $localize);
	wp_enqueue_script($handle);
});


/* Ajaxから取得したnonceを認証し、認証通過したらテンプレートを出力する */
function view_search_results()
{
	$nonce = $_REQUEST['nonce'];
	if (wp_verify_nonce($nonce, 'view_search_results')) {
		get_template_part('page-templates/ajax-search');
	}
	die();
}

add_action('wp_ajax_view_search_results', 'view_search_results'); //第一引数は wp_ajax_{ファンクション名} にする
add_action('wp_ajax_nopriv_view_search_results', 'view_search_results'); //第一引数は wp_ajax_nopriv_{ファンクション名} にする
```
```javascript
'use strict';
$("select[name='jobs_area'], input[name='jobs_skill[]'],input[name='programming[]'").change(function () {
  dispLoading();

  let jobs_skill = [];
  $("[name='jobs_skill[]']:checked").each(function () {
    jobs_skill.push(this.value);
  });
  let programming = [];
  $("[name='programming[]']:checked").each(function () {
    programming.push(this.value);
  });

  let freeKeyword = $("input[name='s']").val();
  console.log(freeKeyword);
  $.ajax({
    type: 'GET',
    url: localize.ajax_url,
    data: {
      'action': 'view_search_results',
      'jobs_area': $('[name=jobs_area]').val(),
      'jobs_skill': jobs_skill,
      'programming': programming,
      's': freeKeyword,
      'nonce': localize.nonce
    },
    success: function (response) {
      $('#search-result').html(response);
    }
  })
    // 処理終了時
    .always(function (response) {
      removeLoading();
    });

  return false;
});

/* ------------------------------
 Loading
 ------------------------------ */
function dispLoading(msg) {
  if (msg == undefined) {
    msg = "";
  }
  var dispMsg = "<div class='loadingMsg'>" + msg + "</div>";
  if ($("#loading").length == 0) {
    $("body").append("<div id='loading'>" + dispMsg + "</div>");
  }
}

function removeLoading() {
  $("#loading").fadeOut('fast').queue(function () {
    $("#loading").remove();
  })
}
```

## タグ

#loading").fadeOut('fast').queue(function #loading").length #Web制作 #search-result').html(response); #loading").remove(); 

## 関連ドキュメント

- [[../02_Web制作/search.php.md|search.php]]
- [[../99_その他/x.md|x]]
- [[../99_その他/y.md|y]]
- [[../99_その他/テンプレート.md|テンプレート]]
