---
notion_id: 7d6d62b4-9887-405b-9a44-57c6498023a2
account: Secondary
title: 連続する文字に１文字ずつspanタグをつけたい
url: https://www.notion.so/span-7d6d62b49887405b9a4457c6498023a2
created_time: 2022-04-25T05:22:00.000Z
last_edited_time: 2024-02-01T05:49:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.404374
---
# 連続する文字に１文字ずつspanタグをつけたい

- javascript
  ```javascript
var textWrap = document.querySelectorAll('.js-span');
textWrap.forEach((t) => (
    t.innerHTML = t.textContent.replace(/\S/g,'<span>$&</span>')
));
  ```
  textWrapという関数を指定
  querySelectorAllで「.js-span」のclassを取得
  「.js-span」のインナーhtmlを書き換える
  「textContent」でそれぞれの文字を取ってきて、<span>$&</span>で囲みなさいという意味
- jQuery
  ```javascript
// プラグイン化
$.fn.letterSpan = function() {

    // idではなくclassを使い複数設定する想定で each を使う
    $(this).each(function() {
        var text = $.trim(this.textContent),
            html = "";

        text.split("").forEach(function(v) {
            html += "<span>" + v + "</span>";
        });

        this.innerHTML = html;
    });
};

// 上記同様に #js-page-title に反映
$("#js-page-title").letterSpan();

// .js-letter-span クラスのコンテナ全てに反映
$(".js-letter-span").letterSpan();
  ```
  - 改行に対応したコード↓

## タグ

#js-page-title").letterSpan(); #js-page-title #よしなに対応 

## 関連ドキュメント

- [[../99_その他/x.md|x]]
- [[../99_その他/y.md|y]]
- [[../01_よしなに対応/サンワードメディア.md|サンワードメディア]]
- [[../01_よしなに対応/slick.md|slick]]
- [[../01_よしなに対応/maruさん『よしなに対応』ぶち上げ企画.md|maruさん『よしなに対応』ぶち上げ企画]]
