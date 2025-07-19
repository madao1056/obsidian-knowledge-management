---
notion_id: c3c79594-5a1b-483f-a4e5-66f07a615603
account: Main
title: 【2−6】カスタマイズ方法をポイント解説（見た目カスタマイズSwiper編）
url: https://www.notion.so/2-6-Swiper-c3c795945a1b483fa4e566f07a615603
created_time: 2023-09-11T00:13:00.000Z
last_edited_time: 2023-09-11T00:13:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:15.085819
---
# 【2−6】カスタマイズ方法をポイント解説（見た目カスタマイズSwiper編）

【目次】
## Swiperのオプションを変更して見た目をカスタマイズ
- Swiperのオプションを変更してスライダーの見た目をカスタマイズします。
- よく使用するオプションの解説をします。
> 💡 「【2−3】スライダーテンプレート使い方を簡単解説（Swiper編）」を事前に実施した上で進めてください。
■src/js/script.js（抜粋）
```javascript
new Swiper('#mv_slider', {
  effect: 'slide', //slide:スライド,fade:フェード,cube:立方体の面のように回転しながら表示,
  loop: true,  // スライダーの終わりまで行ったときの動き。選択肢：true：ループする, false：巻き戻す
  speed: 3000,  // スライダーの移動時間をミリ秒単位で指定
  autoplay: {  // 自動実行を有効にする
    delay: 3000,  // スライドが自動的に進むまでの時間をミリ秒単位で指定する
    disableOnInteraction: false, // ユーザーのスワイプ操作後も自動再生を続ける。選択肢：true：スワイプ操作後に自動再生を停止する, false：スワイプ操作後も自動再生を続ける
  },
  pagination: {  // ページネーション設定
    el: ".swiper-pagination",  // クラス名、idなどのセレクタを指定する
    clickable: true,  // クリックしたスライドに移動するかどうか、true:クリック可、false：クリック不可
  },
  navigation: {  // 矢印ボタンを表示。
    nextEl: '.swiper-button-next',  // "次へ"ボタンのエレメントを指定するセレクタ
    prevEl: '.swiper-button-prev',  // "前へ"ボタンのエレメントを指定するセレクタ
  },
  slidesPerView: 1,  // 1ページに表示するスライド数
  spaceBetween: 10,  // 画像間の余白の設定
  centeredSlides: true,   // これを指定すると中央にある画像にフォーカスされる。選択肢：true：中央にフォーカス, false：中央にフォーカスしない
  breakpoints: {  // レスポンシブデザインのブレークポイントを指定（**指定したpx以上**の場合）
    768: {
      slidesPerView: 1,  // 1ページに表示するスライド数
    },
  },
});
```
■参考（公式ページ）
[Bookmark](https://swiperjs.com/swiper-api#parameters)
■参考（日本語で解説）
[Bookmark](https://pengi-n.co.jp/blog/library-swiper/)

## タグ

#parameters) #Web制作 #mv_slider', 

## 関連ドキュメント

- [[../02_Web制作/デザイン.md|デザイン]]
- [[../02_Web制作/ページネーション.md|ページネーション]]
- [[../04_ビジネス/テンプレート.md|テンプレート]]
- [[../99_その他/目次.md|目次]]
- [[../99_その他/Swiper.md|Swiper]]
