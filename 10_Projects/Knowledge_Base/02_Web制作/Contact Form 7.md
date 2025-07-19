---
notion_id: ee9fd776-62b2-487b-a9a2-14f5ba6bbb4d
account: Secondary
title: Contact Form 7
url: https://www.notion.so/Contact-Form-7-ee9fd77662b2487ba9a214f5ba6bbb4d
created_time: 2022-05-08T23:54:00.000Z
last_edited_time: 2022-05-08T23:54:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.512344
---
# Contact Form 7

  ```php
【ショートコードをテンプレートに書く方法】

<!-- Contact Form7などのショートコードの読み込み -->
<?php echo do_shortcode( 'ショートコード名' ); ?>
  ```
  
  Contact Form7のショートコードはこちら↓
  
  ![](https://prod-files-secure.s3.us-west-2.amazonaws.com/d58fe38c-a9d4-4466-aed9-85604b7b2c6d/32feb25b-aa03-45aa-8a0f-cee965cbcbfd/short-code01.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQKSQRXU%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T060526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGe8o0dDrYJwAv9oGGF8G%2BvRzrh%2FsLGaVbHHFFsj6m%2BjAiBCjNBnV%2Bx%2BDDyRfVs7pOgoeZU%2BZiv%2FeKbviFjZlBHMJyqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTW7mRdry%2FEp%2BdLknKtwDYzAcqxPQLUktwi0cCtDWdJ88Orx1x%2BXRoU70CFrOok%2Bjj6SIYWtiSEfqTYoOdvsVfx2uBdcd3dze1GB3pptcIUveAgZwSXVYp7Xip4ZfP00tePy7aEjPOkZ5S05bgwJC%2BcpKc3s3g9Ed7Rob5o6MGzSJrAuvVko8iY4QhhsiPTU6RMGWjqxzeHbagor7vJqJMuGJ3RqYJK%2FlCDOteUPfgEp5A1%2B5LpcrlE3L2riOIhnI8TM3HoRtFXCjz3Ezc9Ah1oBFUt7ultsO0wFCVBZjzbZ2CMyZvZLxVehVx9kJWyp604MbJDUvKtlyodUYyhd7IvtzxHMaRDlutg%2B5rkKcuiV72U57vt%2BlYDx40a40bZV1pZRDUP68oJSkgYCninBRAHq3XMVhA4fYm%2BWQHP3WfgXVlIWizB5fdR7IdNoDtNbz6ZVbkN42rDomPiZJBCEjcxPpDyg1XNJIBj7MD2ddyiTg6RE%2Bb88gE1PG%2FBKjKnE2T9J4ZQeTw344Om7m5M0LMNJMqxoXtl4X%2B7ukymN9WCWniBZI3K5rqkboM9frH9IfXaH4ygGy6q2DZrc5Nvz44AXXHnafo7oJDttf6e4b9CCEcLx%2FAi91nAVs1hk%2FJWkjxV%2BanVTGcl2en48w5sXswwY6pgFPNrNkk2mS3a3alY3vtCDV9myBZSnqGmhg%2Fo54yNYxZu8ms34dx4m%2BZEgxaFgTaErRybteJNWVtAtXRE0wczPM3gyeP9vV3OI9TigTMZPKrHDT9DtII4IX4b2d696yctf58QAMb%2FczsTDsjdzeFBK9GTvm%2F34Hzoq7V6OKu3OXGcCpFxZtLMEZR%2BHBJHm1V1RPDxPwR7JJ6xnIFZQ4HRt%2BVa8Upw82&X-Amz-Signature=7fb2e8811db56d0f3e48d3ab084d0ee0bb53ea630091a4c3e2043b5c1d98ff22&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
  
  もしくはこちら↓
  
  ![](https://prod-files-secure.s3.us-west-2.amazonaws.com/d58fe38c-a9d4-4466-aed9-85604b7b2c6d/b8381c3b-6a5e-4df5-82c9-d398f2c634ec/short-code02.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQKSQRXU%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T060526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGe8o0dDrYJwAv9oGGF8G%2BvRzrh%2FsLGaVbHHFFsj6m%2BjAiBCjNBnV%2Bx%2BDDyRfVs7pOgoeZU%2BZiv%2FeKbviFjZlBHMJyqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTW7mRdry%2FEp%2BdLknKtwDYzAcqxPQLUktwi0cCtDWdJ88Orx1x%2BXRoU70CFrOok%2Bjj6SIYWtiSEfqTYoOdvsVfx2uBdcd3dze1GB3pptcIUveAgZwSXVYp7Xip4ZfP00tePy7aEjPOkZ5S05bgwJC%2BcpKc3s3g9Ed7Rob5o6MGzSJrAuvVko8iY4QhhsiPTU6RMGWjqxzeHbagor7vJqJMuGJ3RqYJK%2FlCDOteUPfgEp5A1%2B5LpcrlE3L2riOIhnI8TM3HoRtFXCjz3Ezc9Ah1oBFUt7ultsO0wFCVBZjzbZ2CMyZvZLxVehVx9kJWyp604MbJDUvKtlyodUYyhd7IvtzxHMaRDlutg%2B5rkKcuiV72U57vt%2BlYDx40a40bZV1pZRDUP68oJSkgYCninBRAHq3XMVhA4fYm%2BWQHP3WfgXVlIWizB5fdR7IdNoDtNbz6ZVbkN42rDomPiZJBCEjcxPpDyg1XNJIBj7MD2ddyiTg6RE%2Bb88gE1PG%2FBKjKnE2T9J4ZQeTw344Om7m5M0LMNJMqxoXtl4X%2B7ukymN9WCWniBZI3K5rqkboM9frH9IfXaH4ygGy6q2DZrc5Nvz44AXXHnafo7oJDttf6e4b9CCEcLx%2FAi91nAVs1hk%2FJWkjxV%2BanVTGcl2en48w5sXswwY6pgFPNrNkk2mS3a3alY3vtCDV9myBZSnqGmhg%2Fo54yNYxZu8ms34dx4m%2BZEgxaFgTaErRybteJNWVtAtXRE0wczPM3gyeP9vV3OI9TigTMZPKrHDT9DtII4IX4b2d696yctf58QAMb%2FczsTDsjdzeFBK9GTvm%2F34Hzoq7V6OKu3OXGcCpFxZtLMEZR%2BHBJHm1V1RPDxPwR7JJ6xnIFZQ4HRt%2BVa8Upw82&X-Amz-Signature=a89be07506db35d7c22b1edc63c4747508bc7dd67550223edbd3537492ac2914&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
  ```css
div.wpcf7 .ajax-loader {
	display: none !important;
}
  ```
  
  ```css
.wpcf7-mail-sent-ok {
	display: none !important;
}
  ```
  
  functions.phpに以下のコードを追記
  ```php
// ContactForm7で自動挿入されるPタグ、brタグを削除
  add_filter('wpcf7_autop_or_not', 'wpcf7_autop_return_false');
  function wpcf7_autop_return_false() {
    return false;
  }
  ```
  
  functions.phpに以下のコードを追記
  ```php
add_action( 'wp_footer', 'add_origin_thanks_page' );
 function add_origin_thanks_page() {
 $thanks = home_url('/thanks/');
 $recruit = home_url('/recruit/');
   echo <<< EOC
     <script>
       var thanksPage = {
         フォームID: '{$thanks}',
         フォームID: '{$recruit}',
       };
     document.addEventListener( 'wpcf7mailsent', function( event ) {
       location = thanksPage[event.detail.contactFormId];
     }, false );
     </script>
   EOC;
 }
  ```
  ※ 変更するのはフォームIDと遷移先のURL
  詳細はこちらを参照
  [Bookmark](https://junpei-sugiyama.com/contact-form-7-thanks-page/)
  function.phpに以下のコードを追記
  ```php
//確認用メールアドレスの設定
function wpcf7_main_validation_filter( $result, $tag ) {
  $type = $tag['type'];
  $name = $tag['name'];
  $_POST[$name] = trim( strtr( (string) $_POST[$name], "\n", " " ) );
  if ( 'email' == $type || 'email*' == $type ) {
    if (preg_match('/(.*)_confirm$/', $name, $matches)){
      $target_name = $matches[1];
      if ($_POST[$name] != $_POST[$target_name]) {
        if (method_exists($result, 'invalidate')) {
          $result->invalidate( $tag,"確認用のメールアドレスが一致していません");
      } else {
          $result['valid'] = false;
          $result['reason'][$name] = '確認用のメールアドレスが一致していません';
        }
      }
    }
  }
  return $result;
}
add_filter( 'wpcf7_validate_email', 'wpcf7_main_validation_filter', 11, 2 );
add_filter( 'wpcf7_validate_email*', 'wpcf7_main_validation_filter', 11, 2 );
  ```
  
  Contact Form7の編集画面ではこのように書きます。
  
  ![](https://prod-files-secure.s3.us-west-2.amazonaws.com/d58fe38c-a9d4-4466-aed9-85604b7b2c6d/057467b0-6716-456a-901d-cf97a8db1abf/contact-form7-confirm.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2VBIFVX%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T060528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDRbyhyZBONbpqXzGgv582LXMjQjwl5ACUhi1ISqZM8XAiEA3BwO3SlyxAyjiyvOtsZVLg8rY7kqhXhTfhE%2Fs%2FFyiWIqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJgOQTrdhFiWeMn%2FoSrcA0YxaJdeHq7eRx59gSv%2Fm7Gsc1ElUNwNOmoiKlIj52iSdEXbRaHR0yGZZ2KPQsFutUVjsDHj3FBrmL1tqRKfNBnON%2FmXGR4tKpHGDxjtMI1C8NUPAIEsNGAi%2BhsyPjU7dy5rfzG1a41Xwb9aAfaNfOJylbaxNUJgLKasiy%2FkA9%2B%2Bc3ofSK9F7kmiMqUVBgu6H4OBsfS%2F9gN%2FH015oo4PTO0DL4m6QaBD0%2FLwiN9%2B7dHJ7DhUN4ExFO6UanChJzqO%2FXBWMsTrjUu5UT04QzXEkhUWskrRuWM%2BU4VPbtNNvYyFFDSQFzXL4G5pYFtD4VyrRzh%2FTqd7mAtCLdH0OL202%2FS0uNFgcfm%2FncKqZwz9V1S1mCTRUQ13YXcFjrZk0CUehHtqqKQSg7XiOPrG6IHZD3NMNq%2BzyIW0ROhiTsaSsEIEnXov94TmIqAaBzEC6sztoebK9CmXJJMGymcsH76Oegq67mzdy8d%2BwKrtGlWVdB25GGWmWffvjL8ynI1zkAygKeetoBuIaTESqkAn5CVe%2FRqYqm%2BwxVYfabqrZQuFjFSCFC65iilI6HAmaDj4fXlJxJ3691wmXsh0GsDdzTmjkUOGj2wgETd%2FddGHFaOEMddDU3fcUABSqwScV9V7MKbF7MMGOqUBNXO1frdNHRs6fXn6N5BngPz6Q3I15LkFSI1r7Pl1HRxjo49HALK1WG4y1U4E%2F9NgO3vsX8k6vDqp5GbiMVKanRQhSMJ%2BTMVs0fa7vW9QXHLb0RF91t4ZWT6sKnmc9%2BTy3E8rHu5xFIw4WINyPKgco32FCUjCwuB968ZUtSOt2awOpzpn5gAFR8xBi8R70nIBVDSaZX%2BYWxMA8tuO2MvsC9SVwZY2&X-Amz-Signature=fc82576f98b7c2e8c9ee36e2cc369eb0ca3b3cafce7cf4ef8c3fd9bdddd31e49&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
  
  管理画面の編集画面
  ```basic
[email* your-email　　class:class名1 class:class名2]
  ```
  ※ classとclassの間のスペースは半角スペース
  初期設定では選択肢の1番目が自動で選択されますが、これを非表示またはテキストに変更。
  ```scss
[select* select-type class:class名 **first_as_label ""** "選択肢1" "選択肢2"]
  ```
  ※ first_as_label "" が非表示にする為の記述（先頭は空欄になる）
  ※ first_as_label "選択して下さい" と書けば初期表示は「選択して下さい」になる
  →これは選択肢に入らないので、入力必須でこれが選択されているとエラーになります。
  ※ include_blank にすると先頭は「- - -」になる
  
  functions.phpに以下のコードを追記。
  **※ お問い合わせフォーム編集画面で必須にする為の ’＊’ は削除する**
  ```php
// contact form 7 エラーメッセージ変更
function custom_wpcf7_validate_name( $result, $tags ) {
  foreach ( $tags as $tag ) {
    $name = $tag['name'];
    if ( $name == 'your-name' ) {
      $input = $_POST[ $name ];
      if ($input == '') {
        $result->invalidate( $name, 'お名前は必須です。' );
      }
    }
    if ( $name == 'your-email' ) {
      $yourmail = $_POST[ $name ];
      if ($yourmail == '') {
        $result->invalidate( $name, 'メールアドレスは必須です。' );
      }
    }
    if ( $name == 'your-email_confirm' ) {
      $yourmail = $_POST[ $name ];
      if ($yourmail == '') {
        $result->invalidate( $name, 'メールアドレス確認は必須です。' );
      }
    }
    if ( $name == 'your-tel' ) {
      $yourtel = $_POST[ $name ];
      if ($yourtel == '') {
        $result->invalidate( $name, '電話番号は必須です。' );
      }
    }
  }
  return $result;
}
add_filter( 'wpcf7_validate', 'custom_wpcf7_validate_name', 11, 2 );
  ```
  変更するのは ’your-name’ などの項目名とエラーメッセージです。
  項目名はこちらになります。
  ![](https://prod-files-secure.s3.us-west-2.amazonaws.com/d58fe38c-a9d4-4466-aed9-85604b7b2c6d/44a11bc2-cf65-488d-8b1e-9218da409ce4/%E9%A0%85%E7%9B%AE%E5%90%8D.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNV3OWO4%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T060532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDfPKSGE8Zp5lDYHA%2FKYtcjdcCZvxp5sbWYNpvryFVV4AiEA0o8MHJmR%2Bjt%2F%2BvqieuEN%2Fi3V37mz1d1jmwZ9UyAvBLoqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHA8sA1CBCyY5he4SSrcAwVJab1%2B8xw0qYrHhBKEzfDyubAhYUXXx%2B%2FicFq0VhFkjJGZumPlcMB8ZlTw1aCxLjAN8hhnzG75ATi981%2FQxLBDiUTVSUqwcbuLwk1IgnjDcujsOOCXov%2BD%2B6%2FrISrdjQTel7aYvkDfOOwuZrCjGnMB6bdlKS4wAIuH16urR6U5zKsrnqJ3u9E%2FtIFdcTzzKPo9AqpGnVswUJPN%2Fet63Nn698WhrGuoFERaufh5pkrf3AJqA9S585Mescb0RUMrXkdeN384LYWNR7YdIaYiq3Fji832u1IIYnpYTwyZHYvVlO1lkDU0cBV69nMdGVUnmqZsdkDnHJgFbOvtLAP%2FiUDCqsjoLRQjaWiXpIuB3o2HUTfNllo2xXKsjtDUnPlcjjQVOAb4cPxaa5BUID1I1EUy4e7bebcESiYyUaxk%2BP1xdk9NxUQlsbs5Dj9yDT2foJ9sLUqLnu%2FM9NeJifPtWdGjdvV4yjK8qE%2F6q8RW3TNfvQUD1Xxu5gfdge8QcjB28VW%2BmZaRQO%2BiwHsRieWbbb3G5beVMNgL%2FjmDhj%2Bes%2Buv2%2F78pkc1An6LnvHvqPR%2FNA%2FVQKp3ULlkvrecuM1GG10rnoYjkYXAiwmQll8Ip1k9jHBBgGX6aPpn%2FtowMKXF7MMGOqUBq37ffsPF5%2FUZ5YfSnqQ615Cy8kwvlDKmYZDteJOL2UVENrLccwy8obtKfh03DMugxBrn6BVA0dVz1cTPSg6DIJlHnQeVeX0lebCoX593g7vfRHtY1HbUDivC9uKrl08a2lQTGxjw5CqiafWeklAcjPdSftqweXDfYYokEE8A7iXPzEuGS0TI0nqx%2Fu6tH0KNZPW4osCRILR4tb%2BUKOoHSEE7JWq5&X-Amz-Signature=d9b32f8c208912e729f710799f97008baf88533ae2a36aac0d84cc0b95a8ffec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
  
  
  Contact From7の編集画面、メールタブで送信先にメールアドレスを入力しますが、複数の場合は間にカンマ「,」を入れるだけでOKです。
  ![](https://prod-files-secure.s3.us-west-2.amazonaws.com/d58fe38c-a9d4-4466-aed9-85604b7b2c6d/fdc4e1a1-d1db-4ec4-b971-0f165fa2e0bd/contact-form7-mail-address04.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTJ6IAR4%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T060533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF6NJi%2Bg8RMvtaFU0GSU3L2qG0Ld9VdP7cS0FwLqMTEuAiEAsJbmlQMOvCtU%2FiwLgfwXzpovxFWJ728dSFVLSt%2FJeUcqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFsswIso67zMas%2FjXSrcA6Gb%2F2HAmzZqDoP9uaym6GA7W21tHKSdCZM4QDuPgGvv%2FIho5xtBo7RszfvGc9VhJvuCEikSFfZMQ4d8npQkgMceMPNzLdMm0VQ7uBLccuuc18JHXigZy6tRQswvjOyOKKfw2Hk8w5AN6l98FrMOoAZDVSW1cy1Hyb7xPAjm8dmxjO2f%2Fn1oT8myStxpzL3IU%2FEJuO71M6NRomuwyCbv%2Fv7B1dv0EpoGu6%2FCRVizBZRZPeE16b3Ch%2B3rUh3gmTYD9gEaFpd3dZvfbGGvUJt0iMDuN8d7dhNb4%2BySg4NkCXI1h0wbAiYYlIbxZiDAnuEeR%2FGHIPYlTpDt1pC%2BLbBJ0XNIvbTp8535fXCY33MIL5M%2BgHgzJGAQM4kWiFLyBOt1HLfQA%2F%2Fv8KFe%2Ff9s91b26%2FDrnu3FMnBWVju75ePcSIdQbH6qt6iGhWnrJ6t57J6bmEkbTG9G4dAUAYh9bVHk1alYS9W%2Fn6JQZyzZodRD5eNTatUj%2F5bacHIusFstl3JPI7Qg47e1f8IU5xmEtsl1SNLuO3em4oSKU1brTQGWwBoWqMCWdQuck2r18Mxi2WVbpaYq9G17JwqRGfNYXYh7J31gYN0VLiLspLJww0GatLegNAIkG%2Fq1OUurK2NFMPbF7MMGOqUBs9uu4KMCLnQjhQkHY6L8%2FDBFxSy0VaubmTbRjR3%2FVvH2uExQShqxtF9jYxf%2FUrAFb7zJab3KYKcvpfZeO4%2FynwWYChBZrFj7zlu%2BtNkmFJ%2B%2FZFHI4mLDozG6EysV47P9%2Bw7LPbisibF3RYXM39WDtM6%2B73rAZAZR%2BCd0LKw0Pe0r0A86KWJZCZu%2FqSHOJCtnwCM1PQMSEAZGft4mKf1topSX12qD&X-Amz-Signature=cb9696e83b911ab1aa141b66783cf305b944d66aa17c6b68ff776e1e0c72e032&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
  一応ブログも書いてるのでよろしければ参照下さい。
  [Bookmark](https://junpei-sugiyama.com/contact-form7-mail-address/)
セレクトボックスの矢印変更はこちらを参照
[Bookmark](https://junpei-sugiyama.com/select-arrow/)
※ お問い合わせフォームの編集画面で、閉じタグ後のコメントアウトは削除する（崩れるため）

## タグ

#Web制作 

## 関連ドキュメント

- [[../02_Web制作/フォームで選択した値に応じて、確認画面で出力するデータを絞り込みたい.md|フォームで選択した値に応じて、確認画面で出力するデータを絞り込みたい]]
- [[../02_Web制作/電話番号.md|電話番号]]
- [[../02_Web制作/管理画面からメニューを非表示.md|管理画面からメニューを非表示]]
- [[../99_その他/テキスト.md|テキスト]]
- [[../99_その他/タブ.md|タブ]]
