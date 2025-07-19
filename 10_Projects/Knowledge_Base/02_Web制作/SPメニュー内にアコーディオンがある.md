---
notion_id: a11be9a8-ee3d-4f6b-a1eb-ed569641d4d4
account: Secondary
title: SPメニュー内にアコーディオンがある
url: https://www.notion.so/SP-a11be9a8ee3d4f6ba1ebed569641d4d4
created_time: 2023-05-14T11:40:00.000Z
last_edited_time: 2023-06-13T02:28:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.443116
---
# SPメニュー内にアコーディオンがある

- NGな実装と比較してみました↓こんなSPメニューは嫌ですよね。。
---
### 🔹背景
- スマホのメニューの表示は仕様には無いですが「これって普通そうするでしょ？」
的な動きが多く含まれています
---
### 🔹考え方
- ユーザー目線（ユーザビリティ）を考えた実装が複数かくれているので、実際に自分が操作してみて、違和感のないように、違和感に気づくように日常から意識しておきましょう
- 今後運営していく中で項目が増える可能性も十分にあり得ます。『画面高さ＜メニュー高さ』となることを考慮してスクロールできるようにしておきましょう！
- メニューを開いた時には元の画面を固定させてスクロールさせるのはメニュー画面だけにしておきましょう
- メニュー内にアコーディオンがある場合はメニューを閉じる時にアコーディオンも全て閉じるようにしておきましょう
- 『画面高さ＞メニュー高さ』の時に後ろの要素にオーバーレイをつけておくといいです！
間違ってリンクボタンに当たってしまって別ページに移動してしまうと萎えますよね…
---
### 🔹実装方法
### 🔹コード
```html
<header class="p-header">
    <div class="p-header__inner">

			<!-- ---------- 
			ここにPCの要素が入ります 
			 ---------- -->

			<!-- ----- SPのオーバーレイ要素囲うために
								 divタグ(p-header__spnavBox)を作ります ----- -->
			<div class="p-header__spnavBox js-drawer-menu">
        <div class="p-header__spnav p-spnav">
					<!-- ----- SPの要素始まり ----- -->
					<!-- ----- アコーディオンの要素始まり　----- -->
          <div class="p-spnav__item p-spnav__item--accordion p-accordion js-accordion">事業紹介</div>
          <div class="p-accordion__inner ">
            <ul class="p-accordion__items">
              <li class="p-accordion__item"><a href="">アコーディオンタイトル</a></li>
              <li class="p-accordion__item">
                <a href="">アコーディオン項目その１</a>
              </li>
              <li class="p-accordion__item">
                <a href="">アコーディオン項目その2</a>
              </li>
              <li class="p-accordion__item">
                <a href="">アコーディオン項目その3</a>
              </li>
            </ul>
          </div>
					<!-- ----- アコーディオンの要素終わり　----- -->
					<!-- ----- リンクのみの要素　----- -->
          <div class="p-spnav__item p-spnav__item--arrow"><a href="./">リンクタイトルその１</a></div>
          <div class="p-spnav__item p-spnav__item--arrow"><a href="./">リンクタイトルその2</a></div>
					<!-- ----- お問合せボタンの要素　----- -->
          <div class="p-spnav__item"><a href="./" class="p-spnav__cta"><span>お問い合わせ</span></a></div>
        </div>
				<!-- ----- SPの要素終わり　----- -->
				<!-- ----- オーバーレイの要素　&thinsp;=半角スペースのようなもの　----- -->
        <div class="p-header__overlay js-overlay">&thinsp;</div>
      </div>
    </div>
  </header>
```
<details>
<summary>_p-header.scss</summary>
</details>
  ```scss
@use "global" as *;
.p-header {
  height: rem(80);
  background-color: #fff;
  position: fixed;
  right: 0;
  width: 100%;
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  z-index: 999;
  @include mq(md) {
    height: rem(60);
  }
}
.p-header__inner {
  width: 100%;
  height: inherit;
  padding-left: rem(25);
  @include mq(md) {
    padding-left: rem(20);
  }
}
.p-header__container {
  padding-left: rem(10);
  position: fixed;
  width: 100%;
  display: flex;
  align-items: center;
  height: inherit;
  z-index: 999;
  @include mq(md) {
    width: calc(100% - rem(20));
    padding-left: 0;
    justify-content: space-between;
    flex-shrink: 3;
  }
}
.p-header__title {
  display: flex;
  align-items: center;
}

.p-header__title h1 {
  margin-left: rem(10);
}


.p-header__spnavBox {
  display: none;
  @include mq(md) {
    width: 100%;
    height: calc(100% - rem(60));//ヘッダー高さを引いたもの
    position: fixed;
    overflow-y: auto;//Y軸に対してスクロールをさせる
    top: rem(60);
    left: 0;
    z-index: 10;
  }
}

.p-header__overlay {
  opacity: 0;
  position: absolute;
  left: 0;
  top: 0;
  transition: all .3s ease-out;
  visibility: hidden;
  height: calc(100vh - rem(60));
  width: 100%;
  z-index: -1;
  background-color: rgba(58, 62, 51, 0.85);
  cursor: pointer;
  display: block;
}

.p-header__overlay.active {
  opacity: 1;
  visibility: visible;
}
  ```
<details>
<summary>_p-spnav.scss</summary>
</details>
  ```scss
@use "global" as *;
.p-spnav {
  background-color: #3a3e33;
  width: 100%;
  padding: rem(40) rem(20);
  @include mq(md) {
  }
}

.p-spnav__item {
  position: relative;
  color: #fbfff3;
  border-bottom: 1px solid #fbfff3;
}

.p-spnav__item.p-spnav__item--arrow::after {
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  content: "";
  display: inline-block;
  vertical-align: middle;
  border-style: solid;
  border-width: 0 2px 2px 0;
  vertical-align: middle;
  height: 7px;
  width: 7px;
  border-color: #fbfff3;
  transform: rotate(-45deg);
  margin-top: 1px;
  position: absolute;
  right: 24px;
  top: calc(50% - 4px);
}

.p-spnav__item:last-child {
  text-align: center;
  padding: rem(20) 0;
  color: #3a3e33;
  border-bottom: none;
}

.p-spnav__item a {
  padding: rem(20);
  display: block;
}
.p-spnav__cta {
  background-color: #fbfff3;
  text-align: center;
  color: #3a3e33;
}
  ```
<details>
<summary>_p-accordion.scss</summary>
</details>
  ```scss
//p-accordion要素
@use "global" as *;
.p-accordion {
    padding: rem(20);
    transition-duration: 0.2s;
}

.p-accordion::before,
.p-accordion::after {
    background-repeat: no-repeat;
    background-position: center;
    background-size: cover;
    content: "";
    display: inline-block;
    vertical-align: middle;
    background-color: #fbfff3;
    border: none;
    margin-top: 0;
    position: absolute;
    right: rem(27);
    transition: transform 250ms;
    top: calc(50% - 5px);
    height: rem(10);
    width: rem(2);
}

.p-accordion::after {
    transform: rotate(90deg);
}
.p-accordion.open::before {
    transform: rotate(90deg);
}

.p-accordion__inner {
    background-color: #d9dfc9;
    display: none;
    padding: rem(18) rem(20);
}

.p-accordion__items {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
}

.p-accordion__item:nth-child(n + 3) {
    margin-top: rem(22);
}

.p-accordion__item a {
    display: flex;
    align-items: flex-start;
    font-size: rem(13);
    font-weight: 400;
    line-height: 1.46154;
}

.p-accordion__item a::before {
    background-repeat: no-repeat;
    background-position: center;
    background-size: cover;
    content: "";
    margin-top: rem(10);
    display: inline-block;
    vertical-align: middle;
    background-color: #3a3e33;
    margin-right: rem(10);
    height: 1px;
    width: 5px;
}

//footer部分
.p-accordion__inner.p-accordion__inner--ft {
    background-color: #D9DFC9;
}
  ```
```scss
//ナビメニュー表示時に後ろの要素を固定（スクロールさせない）
body.hidden {
  overflow: hidden;
}
```
```javascript
//================
// ドロワーメニュー
//================
$(".js-hamburger").on('click', function () {
//ハンバーガーボタンをクリックしたら処理
  
	$(this).toggleClass("active");
	//ハンバーガーメニューを×にしたり、三にしたり
  
	$(".js-drawer-menu").fadeToggle();
	//ナビメニューをフェードイン・アウトさせる
  
	$(".js-overlay").toggleClass("active");
	//オーバーレイの付け外し
  
	$("body").toggleClass("hidden");
	//bodyタグにhiddenクラスを追加→overflow:hidden;を付け外し
  
	$(".js-accordion").removeClass("open");
  //アコーディオンが開いていた時に”-”を”＋”に戻す処理をopenクラスで制御
	
	$(".p-accordion__inner").slideUp();
	//アコーディオンを閉じる
});

//================
// オーバーレイ
//================
$(".js-overlay").on('click', function () {
//オーバーレイをクリックしたら処理
  $(this).removeClass("active");
  //オーバーレイを非表示に
	
	$(".js-drawer-menu").fadeOut();
  //ナビメニューをフェードアウトさせる

	$("body").removeClass("hidden");
  //bodyタグからhiddenクラスを削除→overflow:hidden;を外す

	$(".js-accordion").removeClass("open");
  //アコーディオンが開いていた時に”-”を”＋”に戻す処理をopenクラスで制御

	$(".p-accordion__inner").slideUp();
	//アコーディオンを閉じる
});

//================
// spアコーディオン
//================
$(".js-accordion").on('click', function () {
//アコーディオンをクリックしたら処理
  $(this).next(".p-accordion__inner").slideToggle();
	//クリックした要素の次の要素（スライドさせる本体）をスライド表示・非表示

  $(this).toggleClass("open");
	//アコーディオンの+,-をopenクラスで制御
});
```
説明無しver
```javascript
//================
// ドロワーメニュー
//================
$(".js-hamburger").on('click', function () {
  $(this).toggleClass("active");
  $(".js-drawer-menu").fadeToggle();
  $(".js-overlay").toggleClass("active");
  $("body").toggleClass("hidden");
  $(".js-accordion").removeClass("open");
  $(".p-accordion__inner").slideUp();
});

//================
// オーバーレイ
//================
$(".js-overlay").on('click', function () {
  $(this).removeClass("active");
  $(".js-drawer-menu").fadeOut();
  $("body").removeClass("hidden");
  $(".js-accordion").removeClass("open");
  $(".p-accordion__inner").slideUp();
});

//================
// spアコーディオン
//================

$(".js-accordion").on('click', function () {
  $(this).next(".p-accordion__inner").slideToggle();
  $(this).toggleClass("open");
});
```

## タグ

#fff; #D9DFC9; #d9dfc9; #Web制作 #fbfff3; #3a3e33; 

## 関連ドキュメント

- [[../02_Web制作/オーバーレイ.md|オーバーレイ]]
- [[../02_Web制作/ハンバーガーメニュー.md|ハンバーガーメニュー]]
- [[../02_Web制作/アコーディオン.md|アコーディオン]]
- [[../99_その他/left.md|left]]
- [[../99_その他/height.md|height]]
