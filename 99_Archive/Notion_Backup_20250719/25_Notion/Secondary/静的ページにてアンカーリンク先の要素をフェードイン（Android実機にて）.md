---
notion_id: 081416cb-7af6-4709-8f3a-3c71fc38e0e0
account: Secondary
title: 静的ページにてアンカーリンク先の要素をフェードイン（Android実機にて）
url: https://www.notion.so/Android-081416cb7af647098f3a3c71fc38e0e0
created_time: 2023-07-27T00:26:00.000Z
last_edited_time: 2023-07-27T00:32:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.436419
---
# 静的ページにてアンカーリンク先の要素をフェードイン（Android実機にて）

```javascript
// スムーススクロール (絶対パスのリンク先が現在のページであった場合でも作動。ヘッダーの高さ考慮。)
//これは静的ページだと効かない？
$(document).on('click', 'a[href*="#"]', function () {
    let time = 400;
    let header = $('header').innerHeight();
    let target = $(this.hash);
    console.log(target);
    if (!target.length) return;
    let targetY = target.offset().top - header;
    $('html,body').animate({ scrollTop: targetY }, time, 'swing');
    return false;
  });

//ここからが追記内容。URLから#以降を探して任意のidがあった際にフェードインのエフェクトを改めてかける。
//URLの#以降の部分をチェックする関数を作成
  function checkURLHash() {
    // 現在のURLを取得
    const currentURL = window.location.href;
    // #以降の部分を取得
    const hashPart = currentURL.split('#')[1];
    // 複数の特定の文字列を配列として定義
    const targetHashes = ['new_face', 'academy', 'senior'];

    // 配列内に特定の文字列が含まれているかチェック
    for (const targetHash of targetHashes) {
      if (hashPart === targetHash) {
        return true;
      }
    }
    return false;
  }

  //チェック関数を呼び出し、結果を使って処理を行う
  if (checkURLHash()) {
    // 特定の#から始まる列がURLに含まれている場合の処理
    scroll_effect();
    // ここに追加の処理を書く
  } else {
    // 特定の#から始まる列がURLに含まれていない場合の処理
    scroll_effect();
  }

// スクロールアニメージョン
  $(window).on('scroll load resize', function () {
    scroll_effect();
  });

  function scroll_effect() {
    let windowHeight = $(window).height();
    $('.c-fadeIn').each(function () {
      let elemPos = $(this).offset().top;
      let scroll = $(window).scrollTop();
      if (scroll > elemPos - windowHeight + 30) {
        $(this).addClass('is-active');
      } else { }
    });
  };
```
```scss
@use "global" as *;

// 下からフワッと
.c-fadeIn {
  opacity: 0;
  transform: translate3d(0, rem(80), 0);
  transition-timing-function: cubic-bezier(0.25, 0.74, 0.22, 0.99), cubic-bezier(0.25, 0.74, 0.22, 0.99);
  transition-duration: 1.6s, 1.6s;
  transition-property: transform, opacity;
}

.c-fadeIn.is-active {
  opacity: 1;
  transform: translateZ(0);
}
```