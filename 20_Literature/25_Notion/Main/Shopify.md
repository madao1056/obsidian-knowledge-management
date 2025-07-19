---
notion_id: 571f7c0e-878c-4888-bc7e-79e2546d726c
account: Main
title: Shopify
url: https://www.notion.so/Shopify-571f7c0e878c4888bc7e79e2546d726c
created_time: 2023-11-01T03:17:00.000Z
last_edited_time: 2025-07-12T05:13:00.000Z
sync_status: full_content
sync_time: 2025-07-12T15:11:07.555244
---
# Shopify

  ### 代表的なお気に入り機能のアプリ
  
  以下は、アカウント登録　→　マイページ　→　お気に入りリスト一覧がどう見えるのか？
まとめたもの
  <details>
  <summary>**Wishlist Plus**</summary>
  </details>
  <details>
  <summary>**Wishlist**</summary>
  </details>
  <details>
  <summary>**Wishlist Hero**</summary>
  </details>
  <details>
  <summary>**Smart Wishlist**</summary>
  </details>
  
  参考記事
  [Bookmark](https://cavedescript.com/blogs/column/wishlist)
  
  # 既存情報
  ## **【制作ボリューム】**
  ・TOP
・商品ページ
・商品１０商品
・法的ページ各種
・その他ページ（カートページ、チェックアウト、ログインページ、会員登録ページ）
  ## **【お客様情報】**
  ・海外向けのアニメグッズのECサイト（toB向け）
・１〜２月は閑散期なのでその間に準備したい
・お客様側に英語の翻訳ができる人がいる
・3〜4月頃にリリース
・既存サイトの方でブログや問い合わせ、about usページなどを作って、Shopify側は必要最低限に（コスト削減のため？）
・テーマはDawnを予定（理由はコスト面？）
  追記
  基本的にカリフォルニア、テキサスが中心となりそうなので、
ある程度配送料はパターン化しているような気もしています
  ## **【私が調査した内容】**
  ・サブスク費用→1.5万/月 程度（Shopifyベーシック、その他アプリ含めた費用）
・定番アプリ（ブログやお問い合わせ機能がないと仮定）
　∟お気に入り機能（[Wishlist Hero](https://apps.shopify.com/wishlist-hero?locale=ja) $4/月）
　∟SNS連携関連アプリ（instaなど無料〜）
　∟顧客情報、注文情報の出力（[Matrixify](https://apps.shopify.com/excel-export-import?locale=ja) $20/月）
　∟言語セレクター（[Geolocation](https://apps.shopify.com/geolocation?locale=ja)無料）
　∟通貨の多言語（[BEST Currency Converter](https://apps.shopify.com/doubly-currency-converter?locale=ja)5通貨までなら無料）
　∟翻訳アプリ（[Shopify Translate & Adapt](https://apps.shopify.com/translate-and-adapt?locale=ja) 無料）
　∟海外発送（[easyRates](https://apps.shopify.com/easy-rates-japan-post?surface_detail=lunaris&surface_inter_position=1&surface_intra_position=2&surface_type=search&locale=ja) $9.90/月 & [easyLabel](https://apps.shopify.com/easy-label-japan-post?locale=ja) $14.90/月）※EMSを使用する場合
  ## **【その他】**
  ・現状お客さまとは1回軽くヒアリング
・第2回ヒアリング前にしっかり調査しておきたい
  ---
  # 【結論】
  対応可能な範囲は「翻訳（法的を除く）」「通貨設定」「配送料の設定」ぐらいまでです
（その他はお客様側で対応）
  ---
  # 【お客様への質問内容】
  ・法的な部分が絡む翻訳もお客様側で可能なのか？
　（特商法 , 個人情報 , 配送 , 支払い , 利用規約など）
・購入後の手続き等は考慮されているか？
・海外はどこの国？数カ国あるか？
・商品は今後増える予定があるのか？
・配送方法などはどんなルートを考えているのか？（**DHLとFeDex**）
・グッズにTシャツなどサイズがあったり色違いのグッズはあるか？（アプリ選定で知っておきたいです）
  # リキマスの方々から情報共有
  - 法的部分について
  - 関税の徴収について
  - 翻訳について
  - 配送について
  - カスタマー対応
  - お客様との契約について
  - 海外発送アプリ（easyRates）について
[Shopify公式](https://help.shopify.com/ja/manual/shipping/setting-up-and-managing-your-shipping/enabling-shipping-carriers)より、ShopifyのプレミアムまたはPlusのプランが必要
クライアントにランニングコスト面でのヒアリングも必要です（結構な金額）
なので、配送をEMS以外、にするか配送量を調査して手動で設定するかになりそうです。
  # 実際に海外サイトを運用している方からの情報共有
  - 体感的に
  
  - ラベル印刷
  [Bookmark](https://www.kwm.co.jp/blog/google-merchant-center/)
  Shopify連携
  [Bookmark](https://blog.dfplus.io/column/s5y-google-merchant-center/)
  
- 気になるアプリ一覧（まだ未使用）
  [**配送料カスタム.amp**](https://apps.shopify.com/amp-custom-delivery-charge-prd?locale=ja)
  [**ハルクフォームビルダー**](https://apps.shopify.com/form-builder-by-hulkapps?locale=ja)
  [**Zepto Product Personalizer**](https://apps.shopify.com/product-personalizer?locale=ja)
  - 空タグは非表示になる（base.cssにて）
  - 見出しタグやpタグに余白は基本ついている（Down）
  - aタグには基本下線がつく（Down）
  - Downはspファースト（テーマによって違う）
  - dl,dt,ddタグはdivタグに変換される
  - 非表示のクラス名が元々ある（Dawn）`*small-hide*`*、*`*medium-hide*`*、*`*large-up-hide*`
  - カートページの追加ボタン（<button>タグ）の中に要素（今回はアイコンSVG）を入れるとカラー変更など切り替え時に動的に〝カートへ追加する〟テキストが差し込まれる[https://gyazo.com/aab415ce12099eebcad2b5d787f156da](https://gyazo.com/aab415ce12099eebcad2b5d787f156da)
  - **ブロック上限はあるのか**
  ### カリカリーナ案件にて
  - 商品ページの画像クリック→モーダル表示は`product-modal.js`で制御されている
  - メタフィールドをカート内で非同期処理したい場合は直接メタフィールドは取れない
  - ブログ記事にて〝前の記事〟[blog.previous_article]、〝次の記事〟[*blog*.next_article]は公開日時が同日（一括公開した時）だとバグる
  - 人気順（順位は管理画面で手動変更可能）で番号をつけることはできたが、for文が50回までの制限があるため、５０商品までしか登録できない（それ以上になるとどうなるか不明：未検証）
  ### カケザン案件にて
  - 年齢認証の要素を画面固定で表示していたが、 表示されるときに、下のファーストビューがちらつく現象が発生。
 原因は、年齢認証の背景画像（バックグラウンドイメージ） を指定していたため、 CSSの読み込みが終わるまでの間で、若干のチラつきが出てきた。
 解決策としては、背景画像ではなく、画像の読み込みとして、 CSSにてボディータグにディスプレイノン 指定し、 JSにてローディング後にボディータグをディスプレイブロックとすることでちらつきを改善できた。
  ### [**【Shopify】日付の表示形式（フォーマット）を変更する方法**](https://ikdlog.com/date-format/)
  ### REDAPPLE案件にて
  <details>
  <summary>メタフィールドのリッチテキストは出力方法が独特（[参考サイト](https://community.shopify.com/c/%E6%8A%80%E8%A1%93%E7%9A%84%E3%81%AAq-a/%E3%83%A1%E3%82%BF%E3%83%95%E3%82%A3%E3%83%BC%E3%83%AB%E3%83%89-%E3%83%AA%E3%83%83%E3%83%81%E3%83%86%E3%82%AD%E3%82%B9%E3%83%88-%E3%82%92%E5%95%86%E5%93%81%E3%83%9A%E3%83%BC%E3%82%B8%E3%81%AB%E8%A1%A8%E7%A4%BA%E3%81%95%E3%81%9B%E3%81%9F%E3%81%84/m-p/2244314)）</summary>
  </details>
  
  # ０から作る時のcssのポイント
  1. 見出しタグ、pタグには`margin:0;`をつける
  1. リストには以下を付与
  1. aタグには以下を付与
  1. imgタグには以下を付与
  1. 375px以下の表示崩れに対応(ルートフォント62.5％を想定)
  1. 
  
  # 経緯
  以前、自分のアカウントでコラボレーターとして構築して、今回パートナーとして、[https://partners.shopify.com/](https://partners.shopify.com/)のアカウントを先方のもので構築しようとした時に誤動作発生。
  
  テーマをCLIでpullしようとした時に、旋回構築していたファイルをなぜか持ってきてしまう
パートナーアカウントで入っているはずなのにCLIに反映されない。
  # 解決
  1. まず、shopify auth logoutをターイナルで打ってログアウトする
  1. [https://partners.shopify.com/](https://partners.shopify.com/)のパートナーとしてログインした状態の画面を開いたまま、
CLIで