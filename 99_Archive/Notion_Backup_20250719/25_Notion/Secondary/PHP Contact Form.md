---
notion_id: 9f8f56ac-57c7-4330-a4db-3e3eda6848be
account: Secondary
title: PHP Contact Form
url: https://www.notion.so/PHP-Contact-Form-9f8f56ac57c74330a4db3e3eda6848be
created_time: 2022-04-28T07:25:00.000Z
last_edited_time: 2022-06-12T23:53:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.489379
---
# PHP Contact Form

### MAMPからメール送信テストを行う
- 参考
  [Bookmark](https://www.webdesignleaves.com/pr/php/php_contact_form_01.php)
- 設定方法
  [Bookmark](https://dezanari.com/mamp-mail/)
  ```php
<?php
session_start();
$mode = 'input';
$errmessage = array();
if (isset($_POST['back']) && $_POST['back']) {
  // 何もしない
} else if (isset($_POST['confirm']) && $_POST['confirm']) {
  // 確認画面
  if (!$_POST['user-name']) {
    $errmessage[0] = "名前を入力してください";
  } else if (mb_strlen($_POST['user-name']) >= 20) {
    $errmessage[0] = "名前は20文字以内にしてください";
  }
  //htmlspecialchars → 特殊な文字列を変換して返す  ENT_QUOTES → クオート（シングルとダブル）「'、"」を安全な文字列にする
  $_SESSION['user-name'] = htmlspecialchars($_POST['user-name'], ENT_QUOTES);

  if (!$_POST['email']) {
    $errmessage[1] = "Eメールを入力してください";
  } else if (mb_strlen($_POST['email']) >= 100) {
    $errmessage[1] = "Eメールは100文字以内にしてください";
  } else if (!filter_var($_POST['email'], FILTER_VALIDATE_EMAIL)) {
    $errmessage[1] = "メールアドレスが不正です";
  }
  $_SESSION['email']    = htmlspecialchars($_POST['email'], ENT_QUOTES);

  if (!$_POST['message']) {
    $errmessage[2] = "お問い合わせ内容を入力してください";
  } else if (mb_strlen($_POST['message']) > 2000) {
    $errmessage[2] = "お問い合わせ内容は2000文字以内にしてください";
  }
  $_SESSION['message'] = htmlspecialchars($_POST['message'], ENT_QUOTES);

  if ($errmessage) {
    $mode = 'input';
  } else {
    $mode = 'confirm';
  }
} else if (isset($_POST['send']) && $_POST['send']) {
  // 送信ボタンを押したとき
  $message  = "お問い合わせを受け付けました \r\n"
    . "名前：" . $_SESSION['user-name'] . "\r\n"
    . "email：" . $_SESSION['email'] . "\r\n"
    . "お問い合わせ内容：\r\n"
    . preg_replace("/\r\n|\r|\n/", "\r\n", $_SESSION['message']);
  mail($_SESSION['email'], 'お問い合わせありがとうございます', $message);
  mail('gussan.web@gmail.com', 'お問い合わせが送信されました', $message);
  $_SESSION = array();
  $mode = 'send';
} else {
  $_SESSION['user-name'] = "";
  $_SESSION['email']    = "";
  $_SESSION['message']  = "";
}
?>
<!DOCTYPE html>
<html lang="ja">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>お問い合わせページ</title>
</head>

<body>
  <?php if ($mode == 'input') { ?>
    <!-- 入力画面 -->
    <form action="./contactform.php" method="post">
      名前 <input type="text" name="user-name" value="<?php echo $_SESSION['user-name'] ?>"><br>
      <?php
      //isset → 変数が宣言されていること、そして null とは異なることを検査する
      if (isset($errmessage[0]) && $errmessage[0]) {
        echo '<div style="color:red;">';
        //implode → 配列要素を文字列により連結する
        // echo implode('<br>', $errmessage );
        echo  $errmessage[0];
        echo '</div>';
      }
      ?>
      Eメール <input type="email" name="email" value="<?php echo $_SESSION['email'] ?>"><br>
      <?php
      if (isset($errmessage[1]) && $errmessage[1]) {
        echo '<div style="color:red;">';
        echo  $errmessage[1];
        echo '</div>';
      }
      ?>
      お問い合わせ内容<br>
      <?php
      if (isset($errmessage[2]) && $errmessage[2]) {
        echo '<div style="color:red;">';
        echo  $errmessage[2];
        echo '</div>';
      }
      ?>
      <textarea cols="40" rows="8" name="message"><?php echo $_SESSION['message'] ?></textarea><br>
      <input type="submit" name="confirm" value="確認" />
    </form>
  <?php } else if ($mode == 'confirm') { ?>
    <!-- 確認画面 -->
    <form action="./contactform.php" method="post">
      名前： <?php echo $_SESSION['user-name'] ?><br>
      Eメール： <?php echo $_SESSION['email'] ?><br>
      お問い合わせ内容<br>
      <?php echo nl2br($_SESSION['message']) ?><br>
      <input type="submit" name="back" value="戻る" />
      <input type="submit" name="send" value="送信" />
    </form>
  <?php } else { ?>
    <!-- 完了画面 -->
    <p>ありがとうございます。お問い合わせの受付が完了いたしました。</p>
    <p>ご入力いただいたメールアドレス宛に、お問い合わせ内容の確認メールをお送りいたしましのでご確認ください。</p>
    <p>確認メールが届かない場合は、メールアドレスが誤っているか、迷惑メールフォルダなどに振り分けられている可能性がございますので、ご確認をお願いいたします。</p>
    <p>お問い合わせいただいた内容は確認後、3営業日以内に担当者よりご連絡させていただきます。いましばらくお待ちください。</p>
    <p>なお、上記期間内に返信がない場合は、送信トラブルの可能性がございます。お手数ですが再度お問い合わせいただけますと幸いです。</p>
    <p>今後ともどうぞよろしくお願いいたします。</p>
  <?php } ?>
</body>

</html>
  ```