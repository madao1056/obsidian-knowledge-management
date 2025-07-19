---
notion_id: 25ab14ef-af3a-48a0-975f-0b2ca06aa42e
account: Main
title: 【2−7】カスタマイズ方法をポイント解説（見た目カスタマイズSlick編）
url: https://www.notion.so/2-7-Slick-25ab14efaf3a48a0975f0b2ca06aa42e
created_time: 2023-09-11T00:13:00.000Z
last_edited_time: 2023-09-11T00:13:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:15.085620
---
# 【2−7】カスタマイズ方法をポイント解説（見た目カスタマイズSlick編）

【目次】
## Slickのオプションを変更して見た目をカスタマイズ
- Slickのオプションを変更してスライダーの見た目をカスタマイズします。
- よく使用するオプションの解説をします。
> 💡 「【2−4】スライダーテンプレート使い方を簡単解説（Slick編）」を事前に実施した上で進めてください。
■src/js/script.js（抜粋）
```javascript
//slick slider
$('#mv_slider').slick({
  speed: 3000,  // スライドのアニメーション速度をミリ秒単位で設定します
  autoplay: true,  // true:自動的にスライドさせる, false:手動でスライドさせる
  autoplaySpeed: 3000,  // 自動的にスライドする間隔をミリ秒単位で指定します
  // fade:  // true:フェード効果を使います, false:スライド効果を使います
  arrows: true,  // true:矢印ナビゲーションを表示します, false:矢印ナビゲーションを表示しません
  slidesToShow: 1,  // 一度に表示するスライド数を設定します
  slidesToScroll: 1,  // 一度にスクロールするスライド数を設定します
  // centerMode: true,  // true:アクティブなスライドを中央に表示します, false:左から順にスライドを表示します
  pauseOnHover: true,  // true:ホバー時に自動再生を一時停止します, false:ホバー時でも自動再生を続行します
  dots: true,  // ドットの表示
  responsive: [  // レスポンシブ対応の設定
    {
      breakpoint: 767,  // 画面幅が**767px以下**のときに適用
      settings: {
        slidesToShow: 1,  // 一度に表示するスライド数を設定します
      }
    }
  ]
});
```
■参考（公式ページ）
[Bookmark](https://kenwheeler.github.io/slick/)
■参考（日本語サイト）
[Bookmark](https://junpei-sugiyama.com/slick-option/)

## タグ

#mv_slider').slick({ #よしなに対応 

## 関連ドキュメント

- [[../01_よしなに対応/slick.md|slick]]
- [[../04_ビジネス/テンプレート.md|テンプレート]]
- [[../99_その他/目次.md|目次]]
- [[../99_その他/top.md|top]]
- [[../99_その他/x.md|x]]
