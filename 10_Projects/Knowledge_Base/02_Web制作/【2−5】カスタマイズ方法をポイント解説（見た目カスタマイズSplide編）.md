---
notion_id: 2c9c41bb-43e5-4bc5-8771-cda3d8c1235e
account: Main
title: 【2−5】カスタマイズ方法をポイント解説（見た目カスタマイズSplide編）
url: https://www.notion.so/2-5-Splide-2c9c41bb43e54bc58771cda3d8c1235e
created_time: 2023-09-11T00:13:00.000Z
last_edited_time: 2023-09-11T00:13:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:15.085916
---
# 【2−5】カスタマイズ方法をポイント解説（見た目カスタマイズSplide編）

【目次】
## Splideのオプションを変更して見た目をカスタマイズ
- Splideのオプションを変更してスライダーの見た目をカスタマイズします。
- よく使用するオプションの解説をします。
> 💡 「【2−2】スライダーテンプレート使い方を簡単解説（Splide編）」を事前に実施した上で進めてください。
■src/js/script.js（抜粋）
```javascript
：（省略）

new Splide('#mv_slider',
  {
    type: 'fade',   // slide,loop,fade から選択
    speed: 3000,    // スライダーの移動時間をミリ秒単位で指定
    autoplay: true, // 自動実行を有効にする true:有効、false:無効
    interval: 3000, // スライドが自動的に進むまでの時間をミリ秒単位で指定する
    rewind: true,    // true:スライダーの終わりまで行ったときに、先頭に巻き戻す(type:fade,slideの時使用)
    arrows: true,    // true:矢印ボタンを表示,false:非表示
    perPage: 1,      // 1ページに何枚のスライドを表示するかを指定
    breakpoints: {   // レスポンシブデザインのブレークポイントを指定（**指定したpx以下**の場合）
      767: {
        perPage: 1,  // 1ページに何枚のスライドを表示するかを指定
      }
    },
    perMove: 1,      // 1度の移動で、何枚のスライドを移動するかを指定
    focus: 'center', //これを指定すると中央にある画像にフォーカスされる
    gap: '10px',     // 画像間の余白の設定
    pauseOnHover: false // true:マウスがスライダーの上にある間は自動再生を一時停止します,false:停止しない
  }
).mount();

：（省略）
```
■参考（公式ページ）
[Bookmark](https://ja.splidejs.com/guides/options/)
[Bookmark](https://ja.splidejs.com/guides/)

## タグ

#Web制作 #mv_slider', 

## 関連ドキュメント

- [[../02_Web制作/デザイン.md|デザイン]]
- [[../02_Web制作/【2−2】スライダーテンプレート使い方を簡単解説（Splide編）.md|【2−2】スライダーテンプレート使い方を簡単解説（Splide編）]]
- [[../99_その他/画像.md|画像]]
- [[../04_ビジネス/テンプレート.md|テンプレート]]
- [[../99_その他/目次.md|目次]]
