---
notion_id: 8650f07c-de4d-49d4-a1ee-d4f0df496c69
account: Secondary
title: VScodeユーザースニペット集
url: https://www.notion.so/VScode-8650f07cde4d49d4a1eed4f0df496c69
created_time: 2024-02-06T06:15:00.000Z
last_edited_time: 2024-02-06T06:50:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.402222
---
# VScodeユーザースニペット集

## 説明動画
気になるものがあれば適宜スニペット登録してください。更新したら情報共有します！
<details>
<summary>html.json</summary>
</details>
  ```plain text
  "dummy_img": {
    "prefix": "dummy_img",//ダミー画像をウェブ上から持ってくる（背景グレーの”200x300”ってテキストが入る）
    "body": [
      "<img src=\"https://placehold.jp/200x300.png\" alt=\"\">"
    ]
  },
  "if": {
    "prefix": "if",//if文
    "body": [
      "<?php if($1): ?>",
      "<?php else: ?>",
      "<?php endif; ?>"
    ]
  },
  "php": {
    "prefix": "php",//php構文
    "body": [
      "<?php $1 ?>"
    ]
  },
  "var_dump": {
    "prefix": "var_dump",//var_dump構文
    "body": [
      "<?php var_dump() ?>"
    ]
  },
  "pc-sp_img": {
    "prefix": "pic-ps",//画面サイズに応じて画像を出しわけする
    "body": [
      "<picture>",
      "<source srcset=\"\" media=\"(max-width: 767px)\"/>",
      "<img decoding=\"async\" loading=\"lazy\" src=\"\" alt=\"\" width=\"\" height=\"\">",
      "</picture>"
    ],
    "description": "pcとsp画像出し分け"
  },
  "webP code": {
    "prefix": "webp",//Webp画像の出しわけ＋画面サイズに応じて画像を出しわけ
    "body": [
      "<picture>",
      "<source srcset=\"\" type=\"image/webp\" media=\"(max-width: 767px)\"/>",
      "<source srcset=\"\" media=\"(max-width: 767px)\"/>",
      "<source srcset=\".webp\" type=\"image/webp\">",
      "<img decoding=\"async\" loading=\"lazy\" src=\".jpg\" alt=\"\" width=\"\" height=\"\">",
      "</picture>"
    ],
    "description": "webp拡張子出し分け"
  },
  "img": {
    "prefix": "img_with_WH",//imgタグに遅延処理と幅・高さを追加
    "body": [
      "<img decoding=\"async\" loading=\"lazy\" src=\"$1\" alt=\"\" width=\"\" height=\"\">"
    ],
    "description": "widthとheightも付加"
  },
  "atag": {
    "prefix": "a",//aタグクリック時に別タブで開く（セキュリティを加味）
    "body": [
      "<a href=\"\" target=\"_blank\" rel=\"noopener noreferrer\">$1</a>"
    ],
    "description": "セキュリティを加味"
  },
  "copy": {
    "prefix": "copy",//コピーライト→©️
    "body": [
      "&copy;$1"
    ],
    "description": "copy"
  },
}
  ```
<details>
<summary>javascript.json</summary>
</details>
  ```plain text
  "DOMContentLoaded": {
    "prefix": "document",
    "description": "DOM要素がロードされたら",//ロードが完了したときに実行される関数
    "body": [
      "document.addEventListener('DOMContentLoaded',function(){",
      "～ここに処理を記載～",
      "});"
    ]
  },
  "setTimeout": {
    "prefix": "setTimeout",//処理を遅らせたい場合に使用
    "description": "遅延処理",
    "body": [
      "setTimeout(function(){",
      "～ここに処理を記載～",
      "},1000);"
    ]
  },
  "use strict": {
    "prefix": "use strict",//本来エラーだけどエラーとして出てこないものをスルーせずにちゃんとエラーとして表示する
    "description": "厳格モード",
    "body": [
      "'use strict';"
    ]
  },
	"Print to console": {
    "prefix": "cl",//コンソールに出力して変数の値などを確認する
    "description": "Log output to console",
    "body": [
      "console.log($1);"
    ]
  },
  ```
<details>
<summary>css.json</summary>
</details>
  ```plain text
	"左右中央": {//要素の左右中央寄せ
		"prefix": "mie",
		"body": [
			"margin-inline: auto;"
		]
	},
	"margin中央揃え": {//要素の左右中央寄せ
		"prefix": "mauto",
		"body": [
			"margin: 0 auto;"
		]
	},
	"比率管理": {//aspect-ratioプロパティをつかった要素の比率管理（主に画像）
		"prefix": "width_asp",
		"body": [
			"max-width: rem($1);",
			"width: 100%;",
			"height: auto;",
			"aspect-ratio: $2/$3;",
			"object-fit: cover;"
		]
	},
	"textarea横固定": {//textarea要素の横幅を固定
    "prefix": "textareavertical",
    "body": [
      "resize: vertical;"
    ]
  },
	"data属性を擬似要素に反映": {//data属性の指定
		"prefix": "content_data",
		"body": [
			"content: attr(data-en) \"\";"
		]
	},
	"親要素はみ出し": {//親要素よりはみ出した装飾やデザインがある時
		"prefix": "over",
		"body": [
			"margin: 0 calc(50% - 50vw);",
			"padding: 0 calc(50vw - 50%);",
			"width: 100vw;",
		]
	},
	"計算式": {//calc関数の設定（７６８pxの時に◯rem）
    "prefix": "calcset",
    "body": [
      "calc($1 / 678 * 100vw)",
    ]
  },
	"font-set": {//文字指定一式
		"prefix": "fset",
		"body": [
			"font-size: $1;",
			"font-weight: bold;",
			"line-height: $2;",
			"letter-spacing: $3em;"
		]
	},
	"flexBox両サイド": {//flexの両端揃え
		"prefix": "fsb",
		"body": [
			"display: flex;",
			"flex-wrap: wrap;",
			"align-items: center;",
			"justify-content: space-between;"
		]
	},
	"absolute中央": {//絶対値での上下左右中央揃え
		"prefix": "aba",
		"body": [
			"position: absolute;",
			"top: 50%;",
			"left: 50%;",
			"transform: translate(-50%, -50%);",
		]
	},
	"absoluteY軸中央": {//絶対値での上下中央揃え
		"prefix": "aby",
		"body": [
			"position: absolute;",
			"top: 50%;",
			"left: $1;",
			"transform: translateY(-50%);",
		]
	},
	"absoluteX軸中央": {//絶対値での左右中央揃え
		"prefix": "abx",
		"body": [
			"position: absolute;",
			"top: $1;",
			"left: 50%;",
			"transform: translateX(-50%);",
		]
	},
	"背景画像set": {//背景画像のよく使うプロパティ一式
		"prefix": "bgimgset",
		"body": [
			"background-image: url($1);",
			"background-repeat: no-repeat;",
			"background-position:center;",
			"background-size:cover;",
		]
	},
	"@media_max": {//メディアクエリ（768pxより小さい）
		"prefix": "medmax",
		"body": [
			"@media screen and (max-width: 768px) {",
			"}",
		]
	},
	"@media_min": {//メディアクエリ（768pxより大きい）
		"prefix": "medmin",
		"body": [
			"@media screen and (min-width: 768px) {",
			"}",
		]
	},
	"下向き:く": {//これ→ ∨
		"prefix": "arrow-bottom",
		"body": [
			"content: '';",
			"display: inline-block;",
			"width: 1rem;",
			"height: 1rem;",
			"border-bottom: 1px solid #000;",
			"border-right: 1px solid #000;",
			"transform: rotate(45deg);"
		]
	},
	"上向き:く": {//これ→ ^
		"prefix": "arrow-top",
		"body": [
			"content: '';",
			"display: inline-block;",
			"width: 1rem;",
			"height: 1rem;",
			"border-top: 1px solid #000;",
			"border-left: 1px solid #000;",
			"transform: rotate(45deg);"
		]
	},
	"左向き:く": {//これ→ <
		"prefix": "arrow-left",
		"body": [
			"content: '';",
			"display: inline-block;",
			"width: 1rem;",
			"height: 1rem;",
			"border-bottom: 1px solid #000;",
			"border-left: 1px solid #000;",
			"transform: rotate(45deg);"
		]
	},
	"右向き:く": {//これ→ >
		"prefix": "arrow-right",
		"body": [
			"content: '';",
			"display: inline-block;",
			"width: 1rem;",
			"height: 1rem;",
			"border-top: 1px solid #000;",
			"border-right: 1px solid #000;",
			"transform: rotate(45deg);"
		]
	},
	"下向き三角": {//これ→ ▼
		"prefix": "triangle-bottom",
		"body": [
			"content: '';",
			"display:inline-block;",
			"width: 0;",
			"height :0;",
			"border-style: solid;",
			"border-width: 2rem 1.25rem 0 1.25rem;",
			"border-color: #333 transparent transparent transparent;"
		]
	},
	"上向き三角": {//これ→ ▲
		"prefix": "triangle-top",
		"body": [
			"content: '';",
			"display:inline-block;",
			"width: 0;",
			"height :0;",
			"border-style: solid;",
			"border-width: 0 1.25rem 2rem 1.25rem;",
			"border-color: transparent transparent #333 transparent;"
		]
	},
	"左向き三角": {//これ→ ◀︎
		"prefix": "triangle-left",
		"body": [
			"content: '';",
			"display:inline-block;",
			"width: 0;",
			"height :0;",
			"border-style: solid;",
			"border-width: 1.25rem 2rem 1.25rem 0;",
			"border-color: transparent #333 transparent transparent;"
		]
	},
	"右向き三角": {//これ→ ▶︎
		"prefix": "triangle-right",
		"body": [
			"content: '';",
			"display:inline-block;",
			"width: 0;",
			"height :0;",
			"border-style: solid;",
			"border-width: 1.25rem 0 1.25rem 2rem;",
			"border-color: transparent transparent transparent #333;"
		]
	},
	"マーカー線": {//文字にマーカーを引いたようにする ※spanで囲う
		"prefix": "maker",
		"body": [
			"background:linear-gradient(transparent 70%, $1 70%);"
		]
	},
	"max-widthセット": {//最大値の設定
		"prefix": "max",
		"body": [
			"max-width: $1rem;",
			"width:100%;"
		]
	}
  ```
<details>
<summary>scss.json</summary>
</details>
  ```plain text
"左右中央": {//要素の左右中央寄せ
    "prefix": "mie",
    "body": [
      "margin-inline: auto;"
    ]
  },
  "margin中央揃え": {//要素の左右中央寄せ
    "prefix": "mauto",
    "body": [
      "margin: 0 auto;"
    ]
  },
  "比率管理": {//aspect-ratioプロパティをつかった要素の比率管理（主に画像）
    "prefix": "width_asp",
    "body": [
      "max-width: rem($1);",
      "width: 100%;",
      "height: auto;",
      "aspect-ratio: $2/$3;",
      "object-fit: cover;"
    ]
  },
  "textarea横固定": {//textarea要素の横幅を固定
    "prefix": "textareavertical",
    "body": [
      "resize: vertical;"
    ]
  },
  "data属性を擬似要素に反映": {//data属性の指定
    "prefix": "content_data",
    "body": [
      "content: attr(data-en) \"\";"
    ]
  },
  "親要素はみ出し": {//親要素よりはみ出した装飾やデザインがある時
    "prefix": "over",
    "body": [
      "margin: 0 calc(50% - 50vw);",
      "padding: 0 calc(50vw - 50%);",
      "width: 100vw;",
    ]
  },
  "計算式": {//calc関数の設定（７６８pxの時に◯rem）
    "prefix": "calcset",
    "body": [
      "calc($1 / 678 * 100vw)",
    ]
  },
  "背景画像中央": {//backgroundプロパティ一括指定
    "prefix": "bgimg-center",
    "body": [
      "background: url($1) no-repeat center / contain;"
    ]
  },
	"svgset": {//mask設定一式（svg画像のカラー変更時）
    "prefix": "svgset",
    "body": [
      "mask-image: url($1);",
      "mask-repeat: no-repeat;",
      "mask-position: center;",
      "background-color: #333",
    ]
  },
  "font-set": {//文字指定一式
    "prefix": "fset",
    "body": [
      "font-size: rem();",
      "font-weight: bold;",
      "line-height: calc( / );",
      "letter-spacing: em;"
    ]
  },
  "下向き:く": {//これ→ ∨
    "prefix": "arrow-bottom",
    "body": [
      "content: '';",
      "display: inline-block;",
      "width: rem(15);",
      "height: rem(15);",
      "border-bottom: 1px solid #000;",
      "border-right: 1px solid #000;",
      "transform: rotate(45deg);"
    ]
  },
  "上向き:く": {//これ→ ^
    "prefix": "arrow-top",
    "body": [
      "content: '';",
      "display: inline-block;",
      "width: rem(15);",
      "height: rem(15);",
      "border-top: 1px solid #000;",
      "border-left: 1px solid #000;",
      "transform: rotate(45deg);"
    ]
  },
  "左向き:く": {//これ→ <
    "prefix": "arrow-left",
    "body": [
      "content: '';",
      "display: inline-block;",
      "width: rem(15);",
      "height: rem(15);",
      "border-bottom: 1px solid #000;",
      "border-left: 1px solid #000;",
      "transform: rotate(45deg);"
    ]
  },
  "右向き:く": {//これ→ >
    "prefix": "arrow-right",
    "body": [
      "content: '';",
      "display: inline-block;",
      "width: rem(15);",
      "height: rem(15);",
      "border-top: 1px solid #000;",
      "border-right: 1px solid #000;",
      "transform: rotate(45deg);"
    ]
  },
  "下向き三角": {//これ→ ▼
    "prefix": "triangle-bottom",
    "body": [
      "content: '';",
      "display:inline-block;",
      "width: 0;",
      "height :0;",
      "border-style: solid;",
      "border-width: rem(30) rem(20) 0 rem(20);",
      "border-color: #333 transparent transparent transparent;"
    ]
  },
  "上向き三角": {//これ→ ▲
    "prefix": "triangle-top",
    "body": [
      "content: '';",
      "display:inline-block;",
      "width: 0;",
      "height :0;",
      "border-style: solid;",
      "border-width: 0 rem(20) rem(30) rem(20);",
      "border-color: transparent transparent #333 transparent;"
    ]
  },
  "左向き三角": {//これ→ ◀︎
    "prefix": "triangle-left",
    "body": [
      "content: '';",
      "display:inline-block;",
      "width: 0;",
      "height :0;",
      "border-style: solid;",
      "border-width: rem(20) rem(30) rem(20) 0;",
      "border-color: transparent #333 transparent transparent;"
    ]
  },
  "右向き三角": {//これ→ ▶︎
    "prefix": "triangle-right",
    "body": [
      "content: '';",
      "display:inline-block;",
      "width: 0;",
      "height :0;",
      "border-style: solid;",
      "border-width: rem(20) 0 rem(20) rem(30);",
      "border-color: transparent transparent transparent #333;"
    ]
  },
  "マーカー線": {//文字にマーカーを引いたようにする ※spanで囲う
    "prefix": "maker",
    "body": [
      "background:linear-gradient(transparent 70%, $1 70%);"
    ]
  },
  "flexBoxFull": {//flexの両端揃え
    "prefix": "fsb",
    "body": [
      "display: flex;",
			"flex-wrap: wrap;",
      "align-items: center;",
      "justify-content: space-between;"
    ]
  },
  "rem()": {//rem指定（gulp専用）
    "prefix": "rem",
    "body": [
      "rem($1)"
    ]
  },
  "absolute中央": {//絶対値での上下左右中央揃え
    "prefix": "absolute-center",
    "body": [
      "position: absolute;",
      "top: 50%;",
      "left: 50%;",
      "transform: translate(-50%, -50%);"
    ]
  },
  "absolute縦中央": {//絶対値での上下中央揃え
    "prefix": "absolute-Y",
    "body": [
      "position: absolute;",
      "top: 50%;",
      "left: $1;",
      "transform: translateY(-50%);"
    ]
  },
  "absolute横中央": {//絶対値での左右中央揃え
    "prefix": "absolute-X",
    "body": [
      "position: absolute;",
      "top: $1;",
      "left: 50%;",
      "transform: translateX(-50%);"
    ]
  },
  "@media_max": {//メディアクエリ（768pxより小さい）
    "prefix": "mediamax",
    "body": [
      "@media screen and (max-width: 768px) {",
      "}"
    ]
  },
  "@media_min": {//メディアクエリ（768pxより大きい）
    "prefix": "mediamin",
    "body": [
      "@media screen and (min-width: 768px) {",
      "}"
    ]
  },
  "@include-md_margin-top": {//メディアクエリ＋上部余白（gulp環境）
    "prefix": "mdm",
    "body": [
      "@include mq(md){",
      " margin-top: rem($1);",
      "}"
    ]
  },
  "@include-md_font": {//メディアクエリ＋文字サイズ（gulp環境）
    "prefix": "mdf",
    "body": [
      "@include mq(md){",
      " font-size: rem($1);",
      "}"
    ]
  },
  "@include-md_sp_main": {//メディアクエリ（gulp環境）
    "prefix": "md",
    "body": [
      "@include mq(md){",
      "",
      "}"
    ]
  },
  "@include-tab_sp_main": {//メディアクエリその２（gulp環境）
    "prefix": "tab",
    "body": [
      "@include mq(tab){",
      "",
      "}"
    ]
  },
  "Dartsass@use": {//DartScssのscssファイル専用
    "prefix": "use",
    "body": [
      "@use 'global' as *;",
      ""
    ]
  },
  "max-width,width": {//最大値の設定
    "prefix": "max",
    "body": [
      "max-width:rem($1);",
      "width:100%;"
    ]
  },
  "overlay": {//要素（画像）にオーバーレイをつける
    "prefix": "overlay",
    "body": [
      "position: absolute;",
      "content: \"\";",
      "background: rgba($color: #000000, $alpha: 0.3);",
      "width: 100%;",
      "height: 100%;",
      "top: 0;",
      "left: 0;"
    ]
  }
  ```