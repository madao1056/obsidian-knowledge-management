---
notion_id: 8ab047b4-7350-4d91-8199-ec3934aac10e
account: Secondary
title: JSの”offset().top”で高さが取得できない
url: https://www.notion.so/JS-offset-top-8ab047b473504d918199ec3934aac10e
created_time: 2023-05-07T08:17:00.000Z
last_edited_time: 2023-05-07T08:23:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.448313
---
# JSの”offset().top”で高さが取得できない

JSの”offset().top”はその要素にzoomプロパティやdisplay:none;をしていると高さが取得できない
※zoomプロパティは非推奨→[`transform: scale()`](https://developer.mozilla.org/ja/docs/Web/CSS/transform-function/scale)を使う
また高さを取得する要素自体がなくてもコンソールでエラーを起こす
【解決策】
```php
if ($('.sample').length) {
  var sampleSet = $('.sample').offset().top;
}
```