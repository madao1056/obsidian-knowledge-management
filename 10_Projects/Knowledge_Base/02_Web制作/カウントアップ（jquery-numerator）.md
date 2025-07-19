---
notion_id: e5106ef5-d999-413c-8f9a-9a52d8b8ca36
account: Secondary
title: カウントアップ（jquery-numerator）
url: https://www.notion.so/jquery-numerator-e5106ef5d999413c8f9a9a52d8b8ca36
created_time: 2022-10-09T14:00:00.000Z
last_edited_time: 2023-12-04T15:18:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.410049
---
# カウントアップ（jquery-numerator）

```html
<p class="js-count"><span class="js-num" data-num="15">0</span>名</p>
```
```javascript
// カウントアップ
  $(function () {
    $(window).on("load scroll", function () {
      $(".js-count").each(function () {
        var txtPos = $(this).offset().top;
        var scroll = $(window).scrollTop();
        var windowHeight = $(window).height();
        if (scroll > txtPos - windowHeight + windowHeight / 8) { // 画面サイズの下から1/5までスクロールしたらカウントアップを開始
          if ($(".js-num", this).attr("data-num").indexOf(".") > -1) {
            var rounding = 1;
          } else {
            var rounding = 0;
          }
          $(".js-num", this).numerator({
            easing: "linear", // カウントアップの動き
            duration: 1000, // カウントアップの時間
            toValue: $(".js-num", this).attr("data-num"), // カウントアップする数値
            rounding: rounding, // 小数点以下の桁数（初期値：0）
          });
        }
      });
    });
  });
```

## タグ

#Web制作 

## 関連ドキュメント

- [[../99_その他/top.md|top]]
- [[../99_その他/x.md|x]]
- [[../99_その他/y.md|y]]
