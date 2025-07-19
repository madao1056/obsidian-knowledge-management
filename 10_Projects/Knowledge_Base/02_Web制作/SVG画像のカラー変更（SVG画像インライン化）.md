---
notion_id: a070e291-e5d1-4bcc-b39d-628e30816518
account: Secondary
title: SVG画像のカラー変更（SVG画像インライン化）
url: https://www.notion.so/SVG-SVG-a070e291e5d14bccb39d628e30816518
created_time: 2022-12-22T04:35:00.000Z
last_edited_time: 2023-05-07T07:49:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.448613
---
# SVG画像のカラー変更（SVG画像インライン化）

- CDN
  ```plain text
<script src="https://unpkg.com/desvg@1.0.2/desvg.js"></script>
  ```
  <details>
  <summary>一応中身も</summary>
  </details>
  
- js
  ```javascript
window.addEventListener('load', function () {
  deSVG('.replaced-svg', true);
});
  ```
  
- css
  ```css
.replaced-svg { //クラス名変えるならjsの方もね
  fill: red;
}

.icon-link:hover .replaced-svg g,
.icon-link:hover .replaced-svg path {
  fill: green;
}
  ```
- html
  ```html
<img class="replaced-svg" src="./images/sample.svg" alt="">
  ```