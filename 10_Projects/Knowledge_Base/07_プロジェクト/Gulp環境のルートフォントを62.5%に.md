---
notion_id: ab124d8f-a6e5-4c87-90b5-19b47f7280e3
account: Secondary
title: Gulp環境のルートフォントを62.5%に
url: https://www.notion.so/Gulp-62-5-ab124d8fa6e54c8790b519b47f7280e3
created_time: 2023-05-27T14:28:00.000Z
last_edited_time: 2023-07-03T12:38:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.440300
---
# Gulp環境のルートフォントを62.5%に

---
### 🔹背景
- 制作会社の仕様でルートフォントを62.5%(1rem→10px)にする必要がありました
---
### 🔹考え方
- Gulp環境のルートフォントの設定を調整すれば後からでも変えることができます！
---
### 🔹実装方法
1. rem(○○)という計算式を設定している箇所を修正していきます
  1. `_function.scss` もしくは `_setting.scss`に以下のような記述があります
`@return math.div($pixels, 16) * 1rem;`
  1.  @return math.div($pixels, 16) * 1rem; →  @return math.div($pixels, 10) * 1rem;
に修正します
1. ルートフォントを設定している箇所を修正していきます
  1. `_base.scss`に記述されているルートフォントに以下のような記述があります
`font-size: 100%;`
`font-size: vw(○○, 16);`
  1. font-size: 100%; → font-size: 62.5%;
font-size: vw(○○, 16); → font-size: vw(○○, 10);に修正します
1. これでルートフォントを62.5%にすることができます！
例）32px→3.2rem
### 🔹コード
```scss
//_function.scss or _setting.scss
@function rem($pixels) {
  // 16で割らずに１０で割る
    @return math.div($pixels, 10) * 1rem;
}


// _base.scss
html {
  // ルートフォントの基準を62.5%に
  font-size: 62.5%;

  // 768px ~ インナー幅＋余白
  @media ( max-width: $breakpointInner ) {
    // フォントサイズを10px基準にする
    font-size: vw(strip-unit($breakpointInner), 10);
  }

  // 376px ~ 767px
  @include mq(md) {
    // ルートフォントの基準を62.5%に
    font-size: 62.5%;
  }

  // ~ 375px
  @media (max-width: 375px) {
    // フォントサイズを10px基準にする
    font-size: vw(375, 10);
  }
}


// bodyタグのフォントサイズを1．６remに（これがないとデフォルトが10pxになります）
body{
	font-size: 1.6rem;
}
```