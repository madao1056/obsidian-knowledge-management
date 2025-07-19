---
notion_id: dafbf5ab-0837-4c86-9e93-0a4fd99ac85e
account: Secondary
title: スクロールして表示、フッター付近で消えるpagetopボタン
url: https://www.notion.so/pagetop-dafbf5ab08374c869e930a4fd99ac85e
created_time: 2023-03-03T06:03:00.000Z
last_edited_time: 2023-03-03T06:04:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.454614
---
# スクロールして表示、フッター付近で消えるpagetopボタン

```javascript
// ページトップボタン
let topBtn = $('.js-pagetop');
topBtn.hide();
let footer = $('.p-footer').innerHeight()
$(window).scroll(function () {
  let point = window.pageYOffset; // 現在のスクロール地点 
  let docHeight = $(document).height(); // ドキュメントの高さ
  let dispHeight = $(window).height(); // 表示領域の高さ
  if ($(this).scrollTop() > 500 && point < docHeight - dispHeight - footer + 150) { // スクロール地点>ドキュメントの高さ-表示領域-footerの高さ
    $('.js-pagetop').fadeIn();//footerより下にスクロールしたらis-hiddenを追加
  } else {
    $('.js-pagetop').fadeOut(); //footerより上にスクロールしたらis-hiddenを削除
  }
});
// ページトップボタンをクリックしたらスクロールして上に戻る
topBtn.click(function () {
  $('body,html').animate({
    scrollTop: 0
  }, 300, 'swing');
  return false;
});
```

## タグ

#Web制作 

## 関連ドキュメント

- [[../99_その他/pagetop.md|pagetop]]
- [[../99_その他/ページトップボタン.md|ページトップボタン]]
- [[../99_その他/height.md|height]]
- [[../99_その他/ボタン.md|ボタン]]
- [[../99_その他/top.md|top]]
