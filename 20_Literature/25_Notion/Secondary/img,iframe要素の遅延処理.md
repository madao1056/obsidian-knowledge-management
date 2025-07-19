---
notion_id: c213c2e9-91b0-4ecd-8741-7ce19cdf9ea6
account: Secondary
title: img,iframe要素の遅延処理
url: https://www.notion.so/img-iframe-c213c2e991b04ecd87417ce19cdf9ea6
created_time: 2022-08-30T05:29:00.000Z
last_edited_time: 2022-08-30T06:47:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.473315
---
# img,iframe要素の遅延処理

- ２パターンあり
1. JSライブラリを用いた実装
  ```javascript
/*ライブラリ読み込み*/
<script src="https://cdn.jsdelivr.net/npm/lazyload@2.0.0-rc.2/lazyload.js"></script>

/* 関数を実行する　*/
<script> lazyload(); </script>
  ```
  ```html
<!--　Class名とsrc,data-srcに注目 "src"属性にダミーを用意し、実際の画像は"data-src"属性に書く　-->
<img class="lazyload"　src="img/dammy.jpg"　data-src="img/logo.png" alt="" width="600" height="400"/>
  ```
1. loading属性を用いた実装
  ```html
<!--ユーザーがオフスクリーンのiframeや画像の近くをスクロールするまで、それらの読み込みを遅延できる-->
<img loading="lazy"  src="img/logo.jpg" alt=""　width="600" height="400">
<iframe src="https://example.com" loading="lazy" width="600" height="400"></iframe>
<!--ブラウザによって対応していない・・・まぁやって損はない-->

<!--　逆にすぐ読み込ませたい場合は　loading=”eager”　-->
  ```
  ```javascript
/*JavaScriptを使用して動的にiframeを作成する必要がある場合*/
var iframe = document.createElement('iframe');
iframe.src = 'https://example.com';
iframe.loading = 'lazy';
document.body.appendChild(iframe);
  ```
  <details>
  <summary>対応ブラウザ</summary>
  </details>