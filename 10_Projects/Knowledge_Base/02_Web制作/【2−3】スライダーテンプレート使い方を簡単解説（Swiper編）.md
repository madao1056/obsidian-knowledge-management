---
notion_id: a18f9025-dd1a-4a19-80d8-15d936578515
account: Main
title: 【2−3】スライダーテンプレート使い方を簡単解説（Swiper編）
url: https://www.notion.so/2-3-Swiper-a18f9025dd1a4a1980d815d936578515
created_time: 2023-09-11T00:13:00.000Z
last_edited_time: 2023-09-11T00:13:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:15.086312
---
# 【2−3】スライダーテンプレート使い方を簡単解説（Swiper編）

【目次】
# 今回行うこと
Swiper.jsを使用してスライダーのテンプレートを作成する
【完成イメージ】
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/736adce6-a3a4-4a64-9f74-d9aa055c96d2/521d75a4-2bc1-40e1-b2c4-18214c897b82/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRMOW4TG%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T044507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCfRFDK%2Fj74spyJz97qMa0A81XEXCAPRFCm9XF6T63HrgIhALS2c95AKUhdzc233A%2Bmw4AZlMQTEPQSY3vCJtaXMjGlKogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxqX9zBp2Mxfj4tT%2FAq3AM6rSxMc%2FAWAVIx%2Bi%2B7tl1YK%2FYAWXR50tr0tj1sOUZ%2BhT94cSOk2MYbkO20cLG53mHwSq5hPrAuf3XWiem3cjx4A0si4V2kWnX1vDt9LyvwJRSlKhDh%2B8k6k%2FjSA7Us%2Ba2a3GQnFF0kmZAjoqQ4IGfYE2yrDkkfIqBsjkTn3I4ZNI%2FT7gfRG7jzuohUe5DtsfW91jdxzxjrvBOes3ji61kBoge3iK2W08bM6mHM0pzvmdcgsabjcXv9hO3McosV8VfIA9KSkORu2wZswbrffJtIMTvZFaMnYoXCd%2B0oEzJ8U4iGim2dw0D8ITjDdl92NlVN6B%2BuQ9YvBFqhe8y1asa550Crtf4ezErqIRafgXHaLof3kV4v0IxjMKH8ZFMFUzezF6RDEnuZ0SzhhPzMolV%2Fqb8%2BzvV65W0OI%2FlUYumk7owC4lgRNGpoMTkPWL51fXfHFEqmhBpUSlijoU78ALriWbT2Cg1K4uFiJHdhzBTwRJuXZ69wnLXDb6hiRWipLJo%2FcGsYR44kNSwdQm1cqiTkdAtzoFquaAXlhiTIKyO09bJQO57XBRNqdDC5JmIT5sYqiJdR77EfdCZS5sXTGEfIjOZloFWKhEwG13lWIMk0iUUy4ZOD1N9MrB6M%2BTD8quzDBjqkAbHAJfBUgUIZNkN0CFSaxpMtxtOlvdfy7I6%2FTnCsftBE2nDEkGjkePDw5VN4XKkDwEEPvLKWHo5NdLPoPpQCcXI8keR8Q0IqICtmDG3pRMlJmbWJkqvXtH4yZwNCta5iYIaKkDVjuaeBtlF9%2BiJc%2BTW7fcdyeax3JLqKgYBTGez9ixNkngpqX94%2BxDRoFCkj74ESZKAIy6F586i1t%2B6riUkOmLzb&X-Amz-Signature=b1ef31004f7390dd066cf33c1077a7ff2d57c9138d4d2151b9d1ba4eec51af6e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
【手順】
1.テンプレートファイルをテーマとして設定する
2.Advanced Custom Fieldsプラグインをインストール
3.カスタムフィールド設定データをインポート
4.投稿タイプ「MVスライダー」に画像等を設定する
5.設定確認
6.動作確認
7.CSSの設定
# Swiper.jsを使用してスライダーのテンプレートを作成する
## 【注意事項】
- Swiper9が最新ですが、動作が不安定に感じたため、Swiper8を使用しています。（2023年6月時点）
- 次の内容は、**「**[**スライダーテンプレート使い方を簡単解説（Splide編）**](/1cc5b47acebc4f8eb8ece6ca2b5395a4)**」**を確認してください。
  1.テンプレートファイルをテーマとして設定する
  2.Advanced Custom Fieldsプラグインをインストール
  3.カスタムフィールド設定データをインポート
  4.投稿タイプ「MVスライダー」に画像等を設定する
## 5.設定確認
### Swiperで動作するよう設定する
「$slider_library」を「swiper」に変更する。
なお、「$slider_library」は、スライダーの切り替え以外の用途では絶対に使用しないでください！
■parts/functions-lib/func-enqueue-assets.php（一部抜粋）
```php
function my_script_init()
{
  global $slider_library;
  $slider_library = 'swiper'; //splide,swiper,slickから選択する

  :（省略）

}
```
## 6.動作確認
### （１）gulpを実行する
※既に実施済みの場合は、スキップしてください
- gulpfile.jsの設定を変更してください
  ![](https://prod-files-secure.s3.us-west-2.amazonaws.com/736adce6-a3a4-4a64-9f74-d9aa055c96d2/361d857a-b048-4684-ae53-0eaab8de8f48/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ARSAGOA%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T044509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDdbugQPgiQkfC6uNmQu3pEUyhnm2pmA7R19eQso5aY5AIgINzm7ptbEZj9YsriD6kahbb36peAkQTk7aRkV%2FMvzUAqiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPKJnvPYRdwn72piSCrcA62cFgsXeLjiELgv35VMUzFxelZmACdksLAMmD1VG%2BhFQK0Y8nBxv9hFSII1lSlPtHJwDY1RBZ0%2BhKetcJTBTnRDOMtbCPrIG%2B7YQyFYeiPTycHmnze7jj8SlE3pzUrVgPk8Wlq7FDuXvtdojKic5glyLn0DwCd9mfnnXaWSUWLJsvm9s9PvZhQLTXMNFusQl5Peq5qrDTnsNFbbi%2F5pe5XKqEFWLPb81P4YrKiMA7b8koxJm9YfrRJztFnzPIoanuoD6k4JSMAsko7Siy8K7orVzBz%2FViCrxoWAfp4QDnvjJsWsn1isUIzc1hTkVT4L8g3O%2BwKhrcsmzRlxeslbydvSrxM%2Bz6P8g41gZR8NWYx3wLu9g%2BcoLEgQkQjvgQFbVxBI4Z99q8r4FDrIhj3vAwUDN%2F5k4r0hurKAmShNO%2BhbG1gLxge5DpB1KYXN7v88ZneQPGJ6kyKPMj0K4Lih8LdAyLtu0labSwxFkZpPo1OaXrr6kbH8WpgJ0x1ELnk3s4QAByaxqWJAONadXqp75PoFuMlZAfGAbKKfaDFqf3TJ7eCP7x%2FkhzITCJkszyKsZqXsP0BnGZ%2FIKvf38LY4HsThwE61CAb5i6yGB3Js0kshiseMAz2BjnKtAUTuMNiq7MMGOqUBtCjwaobO4Uz%2BPHQpVPJ5axaz6iWDSAXA4F4WHUWEN%2B%2BQUYg5TrYNuFaV5PZVZxjVsNyXrsocrgg%2FICDvsQ7II%2B6ZhO1UUytxM6X7%2FZzMGyqvbrQX9%2FFNk7nNyuFI95%2BVb%2B3mxekauvo1IAQUsgoLg9L%2BUMjAWKd%2FUjvcly7qLIPE1LFZqCa3T4z7F%2F3FF2XFsCKuHUXA6zO22sVY5LwFRBkLEEgX&X-Amz-Signature=dabb1ae70143d51289d5e2547125c1a2a192a6503fb329b4cc2ea74eaf442931&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
  
  ![](https://prod-files-secure.s3.us-west-2.amazonaws.com/736adce6-a3a4-4a64-9f74-d9aa055c96d2/e6e5a21a-2bbf-4b67-bf17-c09e645e54ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ARSAGOA%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T044509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDdbugQPgiQkfC6uNmQu3pEUyhnm2pmA7R19eQso5aY5AIgINzm7ptbEZj9YsriD6kahbb36peAkQTk7aRkV%2FMvzUAqiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPKJnvPYRdwn72piSCrcA62cFgsXeLjiELgv35VMUzFxelZmACdksLAMmD1VG%2BhFQK0Y8nBxv9hFSII1lSlPtHJwDY1RBZ0%2BhKetcJTBTnRDOMtbCPrIG%2B7YQyFYeiPTycHmnze7jj8SlE3pzUrVgPk8Wlq7FDuXvtdojKic5glyLn0DwCd9mfnnXaWSUWLJsvm9s9PvZhQLTXMNFusQl5Peq5qrDTnsNFbbi%2F5pe5XKqEFWLPb81P4YrKiMA7b8koxJm9YfrRJztFnzPIoanuoD6k4JSMAsko7Siy8K7orVzBz%2FViCrxoWAfp4QDnvjJsWsn1isUIzc1hTkVT4L8g3O%2BwKhrcsmzRlxeslbydvSrxM%2Bz6P8g41gZR8NWYx3wLu9g%2BcoLEgQkQjvgQFbVxBI4Z99q8r4FDrIhj3vAwUDN%2F5k4r0hurKAmShNO%2BhbG1gLxge5DpB1KYXN7v88ZneQPGJ6kyKPMj0K4Lih8LdAyLtu0labSwxFkZpPo1OaXrr6kbH8WpgJ0x1ELnk3s4QAByaxqWJAONadXqp75PoFuMlZAfGAbKKfaDFqf3TJ7eCP7x%2FkhzITCJkszyKsZqXsP0BnGZ%2FIKvf38LY4HsThwE61CAb5i6yGB3Js0kshiseMAz2BjnKtAUTuMNiq7MMGOqUBtCjwaobO4Uz%2BPHQpVPJ5axaz6iWDSAXA4F4WHUWEN%2B%2BQUYg5TrYNuFaV5PZVZxjVsNyXrsocrgg%2FICDvsQ7II%2B6ZhO1UUytxM6X7%2FZzMGyqvbrQX9%2FFNk7nNyuFI95%2BVb%2B3mxekauvo1IAQUsgoLg9L%2BUMjAWKd%2FUjvcly7qLIPE1LFZqCa3T4z7F%2F3FF2XFsCKuHUXA6zO22sVY5LwFRBkLEEgX&X-Amz-Signature=751e93a49375e9c8a7982034a3938e38f49265b57907d4a0478847480d17c8cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
  - 管理画面のURLのうち上記のように、「/wp-admin/…」より前の部分をコピーして、以下、gulpfile.jsの
  ```php
const browserSyncOption = {
  proxy: "http://toolwordpress.local",// ローカルにある「Site Domain」に合わせる
  notify: false,// ブラウザ更新時に出てくる通知を非表示にする
}
  ```
- VSCodeで「Command（Ctrl）+J」 でターミナルを起動します。
- gulpフォルダに移動して、gulpを実行してください
```plain text
//以下を１行ずつ実行してください
cd gulp
npm i
npx gulp
```
### （２）設定した内容でスライダーが動くことを確認する
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/736adce6-a3a4-4a64-9f74-d9aa055c96d2/521d75a4-2bc1-40e1-b2c4-18214c897b82/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRMOW4TG%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T044507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCfRFDK%2Fj74spyJz97qMa0A81XEXCAPRFCm9XF6T63HrgIhALS2c95AKUhdzc233A%2Bmw4AZlMQTEPQSY3vCJtaXMjGlKogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxqX9zBp2Mxfj4tT%2FAq3AM6rSxMc%2FAWAVIx%2Bi%2B7tl1YK%2FYAWXR50tr0tj1sOUZ%2BhT94cSOk2MYbkO20cLG53mHwSq5hPrAuf3XWiem3cjx4A0si4V2kWnX1vDt9LyvwJRSlKhDh%2B8k6k%2FjSA7Us%2Ba2a3GQnFF0kmZAjoqQ4IGfYE2yrDkkfIqBsjkTn3I4ZNI%2FT7gfRG7jzuohUe5DtsfW91jdxzxjrvBOes3ji61kBoge3iK2W08bM6mHM0pzvmdcgsabjcXv9hO3McosV8VfIA9KSkORu2wZswbrffJtIMTvZFaMnYoXCd%2B0oEzJ8U4iGim2dw0D8ITjDdl92NlVN6B%2BuQ9YvBFqhe8y1asa550Crtf4ezErqIRafgXHaLof3kV4v0IxjMKH8ZFMFUzezF6RDEnuZ0SzhhPzMolV%2Fqb8%2BzvV65W0OI%2FlUYumk7owC4lgRNGpoMTkPWL51fXfHFEqmhBpUSlijoU78ALriWbT2Cg1K4uFiJHdhzBTwRJuXZ69wnLXDb6hiRWipLJo%2FcGsYR44kNSwdQm1cqiTkdAtzoFquaAXlhiTIKyO09bJQO57XBRNqdDC5JmIT5sYqiJdR77EfdCZS5sXTGEfIjOZloFWKhEwG13lWIMk0iUUy4ZOD1N9MrB6M%2BTD8quzDBjqkAbHAJfBUgUIZNkN0CFSaxpMtxtOlvdfy7I6%2FTnCsftBE2nDEkGjkePDw5VN4XKkDwEEPvLKWHo5NdLPoPpQCcXI8keR8Q0IqICtmDG3pRMlJmbWJkqvXtH4yZwNCta5iYIaKkDVjuaeBtlF9%2BiJc%2BTW7fcdyeax3JLqKgYBTGez9ixNkngpqX94%2BxDRoFCkj74ESZKAIy6F586i1t%2B6riUkOmLzb&X-Amz-Signature=b1ef31004f7390dd066cf33c1077a7ff2d57c9138d4d2151b9d1ba4eec51af6e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
## 7.CSSの設定
- 必要に応じて設定してください。スライダーに関連した設定は以下の通り設定しています。
- 複数のスライダーで個別の設定を行う可能性を考慮して、スライダー固有のクラスである「swiper」、「swiper-slide」などに対して直接CSSを当てずに、親である「p-top-mv-swiper」の子クラスに対してCSSを当てる形をとっています。
■src/scss/object/project/p-top-mv-swiper.scss
```sass
@use 'foundation' as *;

.p-top-mv-swiper__inner {
  margin: 5% 5% 0 5%;
}
.p-top-mv-swiper .swiper-slide{
  display: block;
  width: 100%;
  aspect-ratio: 600 / 300;
}

.p-top-mv-swiper .swiper-slide picture {
  height: inherit;
  height: 100%;
}
.p-top-mv-swiper .swiper-slide img{
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.p-top-mv-swiper .swiper-button-prev,
.p-top-mv-swiper .swiper-button-next {
  text-rendering:initial;
}
```
# 今回行ったこと
Swiper.jsを使用してスライダーのテンプレートを作成する
【手順】
1.テンプレートファイルをテーマとして設定する
2.Advanced Custom Fieldsプラグインをインストール
3.カスタムフィールド設定データをインポート
4.投稿タイプ「MVスライダー」に画像等を設定する
5.設定確認
6.動作確認
7.CSSの設定

## タグ

#Web制作 

## 関連ドキュメント

- [[../02_Web制作/swiper.md|swiper]]
- [[../02_Web制作/【2−6】カスタマイズ方法をポイント解説（見た目カスタマイズSwiper編）.md|【2−6】カスタマイズ方法をポイント解説（見た目カスタマイズSwiper編）]]
- [[../02_Web制作/済.md|済]]
- [[../99_その他/LP.md|LP]]
- [[../99_その他/Untitled.md|Untitled]]
