---
notion_id: 0ab0e471-91f6-4a64-8fe4-0c054fec55c4
account: Main
title: 【3−3】スライダーテンプレート使い方を簡単解説（Swiper編）
url: https://www.notion.so/3-3-Swiper-0ab0e47191f64a648fe40c054fec55c4
created_time: 2023-09-11T00:13:00.000Z
last_edited_time: 2023-09-11T00:13:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:15.087978
---
# 【3−3】スライダーテンプレート使い方を簡単解説（Swiper編）

【目次】
  
# 今回行うこと
Swiper.jsを使用して、投稿記事のサムネイルをスライダー表示するためのテンプレートを作成する
【完成イメージ】
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/736adce6-a3a4-4a64-9f74-d9aa055c96d2/95222c89-c445-4990-b355-8e65902d750a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBZP3RJJ%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T044541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIET8ylg622nmdv4ZFzi%2FJw7M4Pm7o2oviad7s94mQi7RAiEAiKgnqc5tttKtG8CW%2FhrbmTXAxNEjVTW7cPtubCKv8KgqiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAmNyTmBGyOHYTHalCrcAxHYuAzUebL1RxFV%2FCKJis7iIap%2FeLDVN7%2FuuAFrXmnZKDS10qtSLh7XPfq7r1iJkhVYThRXf1NLyewr6gXMvVe3BnDACCV8HrEyV1Zif3zwKag1RwDG12BjYFR3rge9xVj9gUfHWkNyWYDzYMJ76IbPcQ4Bs2H0FZ%2BPNrQoeU%2B%2BAsqph1kiXTuLXdNDZT%2Fe9pK8Q24iu1bnG1SsiorOwIPP%2FgndvpyfXNpYoVUe7c%2FMKBR9eWjbqm63R2JMr7TjIIpizSNKRwlpphBd9AkJzVxozTua0vf48wtn3cs7sgIFN8ptgLx7Gwh5db4V4sHm%2FqYnVQOyzFnIoV0aoS6xUVyGipOSCrc6jAMKcEdH6Q5OL24C1icVPET05Nrh643H7O2PyGKHRuKW9XzSI28%2FErN8pwWahOTVDf4jbmGkOIfLOIiBlNaU6Ril4tb9biCS6P9pBYypK3YL7xhAlPcImjMWXLbbxHX58hkTTgxRjbwowg0hTUdqkeJY1dvG0R1wWXnTbHpSqYJ7K41ULHDxIGSkqah%2BwNHJ3TYqoMa%2Fr521bEFv%2FHR0Mg8x6O6WYl%2FLD%2FrvP5iGwcYjZczuKM%2B5unK0WSFsRI02F8LyG8SZzuATfUJT1CK1Cr79UZA8MKSq7MMGOqUBQOF0IqMY26duzVKZIggjfBjRkUekWTmbJSdwrGKP3AJsgsH0VW62pHmsz%2BhpRETkIRCeNggL0P95W8K6GqCya6AGdazqPdlcfu0AfYkOibRNJUnX%2BG8gN%2FYI6aamV%2BtUbwAYYNsY4SPahGwL3KNYwGvO6rThwTGb6u3MYqQFGf9oSnZ0dH%2FVTzh1PB5FxFGAiQzUfpAQrm%2Bng%2BTo9HRMEkwBTH4T&X-Amz-Signature=2af711b69a492ab4bc58e6a277d2a6c023211a70299b606728675c42e6b3adab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
【手順】
1.テンプレートファイルをテーマとして設定する
2.投稿記事を登録する
3.設定確認
4.動作確認
5.CSSの設定
# Swiperを使用してスライダーのテンプレートを作成する
## 【注意事項】
- 次の内容は、**「**[3−2スライダーテンプレート使い方を簡単解説（Splide編）](/ee85db2a990e4f4799f330df78d39fc2)**」**を確認してください。
  1.テンプレートファイルをテーマとして設定する
  2.投稿記事を登録する
## 3.設定確認
### Swiperで動作するよう設定する
「$slider_library」を「swiper」に変更する
■parts/functions-lib/func-enqueue-assets.php（一部抜粋）
```php
function my_script_init()
{
  global $slider_library;
  $slider_library = 'swiper'; //splide,swiper,slickから選択する

  :（省略）

}
```
## 4.動作確認
### （１）gulpを実行する
※既に実施済みの場合は、スキップしてください
- gulpfile.jsの設定を変更してください
  ![](https://prod-files-secure.s3.us-west-2.amazonaws.com/736adce6-a3a4-4a64-9f74-d9aa055c96d2/361d857a-b048-4684-ae53-0eaab8de8f48/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTDMGCFR%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T044542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDZmZG6vmaw4rOKUGE0Che1ig9PFVyLt5lrLp4ezG1EwwIhAKYNS%2Fhy9tt%2FQWoxY3xoBKn8F8ljKVvk9zGBmwhsrF%2F7KogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyTKxekW%2FCyij8yl64q3ANB1GGexBzncAiCzSunh%2F%2Fnf14ntSlE5XH%2B9%2Ba%2FPQsj1ZQCKiHZ33%2F%2B8iO2uz34gV3e%2FH0sRGr0rG1qOSjTSbY02whNjj9jOXAbd%2B3xJfApOOfXu%2B%2B6TD64Gp9RX%2F82XZLXLWZ9XXWZ%2BQE7ehtCAShlA0L4evCo5t0nisxQlTrLP8Q3lqZlsl3zXNKwAbpDLX0XbcnpIKdqXMOZkHrCJPVsnL22cN48579ShqwfR0fNHJ%2FhyKwtVHqSoBNqKwaRy5dHNIlIYWxAhOwL5K9z05SSQIob3rlhW98Kjhfx2cYBn6cxwJAoiZHAmRdS0rU6DgVPT2kPmKsShNevChztSdiZtZax%2Bwx%2Bx9ynLmNOl1SsWtW3K%2B%2Bk5E281Nwf2yKOun50dIbitrSgGRlDSv1addg5DtsrcQU7KQLOts8t%2BUoaRdiPafT8yoimn4oYZ7ix0BgjkGorNZtAHLWrO7GjRcz4bzE7ZYMGvwlCARumVG7pH3l1bJxsUx4gNPS%2BePELYRLHBUs5KXoTr3WBY1ImdlP4FgK61OxtpyytcgW6L1o45o26XPDAILEjORpIDvJdaVG8cjo%2BgsgQocNt%2BG7MX5PO6XAh7AYM9ZFZHnK%2FUoXx8LiVqVRsajaBvDbKeTDCquzDBjqkAWIAQtcm6vYgaqtD6HH9rNC6nX8vHVKmH15nIuF2XGVgG0tZfRM28TGTmZB4Gvxwtio9kbQ7aillrvMPl%2By8UVI9q0s%2Blb71kK2029FMix3J8Q1l0njl71YLd2PGGW8kk%2Fx%2BDTk2egmDaAgnnZiZGHt63d4R2z54GtS%2BeTGcE5gIc9WwsiUbpXN0%2B4abEyHj0UKnVt4jUuU7z%2BPblfm%2BWivMLhZE&X-Amz-Signature=2b70f3c8b2aeeb68f2b42eff8e9242737e630da9b08f66840469f387f8aefa96&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
  
  ![](https://prod-files-secure.s3.us-west-2.amazonaws.com/736adce6-a3a4-4a64-9f74-d9aa055c96d2/e6e5a21a-2bbf-4b67-bf17-c09e645e54ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTDMGCFR%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T044542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDZmZG6vmaw4rOKUGE0Che1ig9PFVyLt5lrLp4ezG1EwwIhAKYNS%2Fhy9tt%2FQWoxY3xoBKn8F8ljKVvk9zGBmwhsrF%2F7KogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyTKxekW%2FCyij8yl64q3ANB1GGexBzncAiCzSunh%2F%2Fnf14ntSlE5XH%2B9%2Ba%2FPQsj1ZQCKiHZ33%2F%2B8iO2uz34gV3e%2FH0sRGr0rG1qOSjTSbY02whNjj9jOXAbd%2B3xJfApOOfXu%2B%2B6TD64Gp9RX%2F82XZLXLWZ9XXWZ%2BQE7ehtCAShlA0L4evCo5t0nisxQlTrLP8Q3lqZlsl3zXNKwAbpDLX0XbcnpIKdqXMOZkHrCJPVsnL22cN48579ShqwfR0fNHJ%2FhyKwtVHqSoBNqKwaRy5dHNIlIYWxAhOwL5K9z05SSQIob3rlhW98Kjhfx2cYBn6cxwJAoiZHAmRdS0rU6DgVPT2kPmKsShNevChztSdiZtZax%2Bwx%2Bx9ynLmNOl1SsWtW3K%2B%2Bk5E281Nwf2yKOun50dIbitrSgGRlDSv1addg5DtsrcQU7KQLOts8t%2BUoaRdiPafT8yoimn4oYZ7ix0BgjkGorNZtAHLWrO7GjRcz4bzE7ZYMGvwlCARumVG7pH3l1bJxsUx4gNPS%2BePELYRLHBUs5KXoTr3WBY1ImdlP4FgK61OxtpyytcgW6L1o45o26XPDAILEjORpIDvJdaVG8cjo%2BgsgQocNt%2BG7MX5PO6XAh7AYM9ZFZHnK%2FUoXx8LiVqVRsajaBvDbKeTDCquzDBjqkAWIAQtcm6vYgaqtD6HH9rNC6nX8vHVKmH15nIuF2XGVgG0tZfRM28TGTmZB4Gvxwtio9kbQ7aillrvMPl%2By8UVI9q0s%2Blb71kK2029FMix3J8Q1l0njl71YLd2PGGW8kk%2Fx%2BDTk2egmDaAgnnZiZGHt63d4R2z54GtS%2BeTGcE5gIc9WwsiUbpXN0%2B4abEyHj0UKnVt4jUuU7z%2BPblfm%2BWivMLhZE&X-Amz-Signature=a6ee2d3272cb16f3a84ead4ccc30291f2200f3a4cf4f3e3a5fab10fcf9e3caeb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/736adce6-a3a4-4a64-9f74-d9aa055c96d2/6a68bf54-ecea-41ce-87c3-88b8e7620c41/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBZP3RJJ%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T044541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIET8ylg622nmdv4ZFzi%2FJw7M4Pm7o2oviad7s94mQi7RAiEAiKgnqc5tttKtG8CW%2FhrbmTXAxNEjVTW7cPtubCKv8KgqiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAmNyTmBGyOHYTHalCrcAxHYuAzUebL1RxFV%2FCKJis7iIap%2FeLDVN7%2FuuAFrXmnZKDS10qtSLh7XPfq7r1iJkhVYThRXf1NLyewr6gXMvVe3BnDACCV8HrEyV1Zif3zwKag1RwDG12BjYFR3rge9xVj9gUfHWkNyWYDzYMJ76IbPcQ4Bs2H0FZ%2BPNrQoeU%2B%2BAsqph1kiXTuLXdNDZT%2Fe9pK8Q24iu1bnG1SsiorOwIPP%2FgndvpyfXNpYoVUe7c%2FMKBR9eWjbqm63R2JMr7TjIIpizSNKRwlpphBd9AkJzVxozTua0vf48wtn3cs7sgIFN8ptgLx7Gwh5db4V4sHm%2FqYnVQOyzFnIoV0aoS6xUVyGipOSCrc6jAMKcEdH6Q5OL24C1icVPET05Nrh643H7O2PyGKHRuKW9XzSI28%2FErN8pwWahOTVDf4jbmGkOIfLOIiBlNaU6Ril4tb9biCS6P9pBYypK3YL7xhAlPcImjMWXLbbxHX58hkTTgxRjbwowg0hTUdqkeJY1dvG0R1wWXnTbHpSqYJ7K41ULHDxIGSkqah%2BwNHJ3TYqoMa%2Fr521bEFv%2FHR0Mg8x6O6WYl%2FLD%2FrvP5iGwcYjZczuKM%2B5unK0WSFsRI02F8LyG8SZzuATfUJT1CK1Cr79UZA8MKSq7MMGOqUBQOF0IqMY26duzVKZIggjfBjRkUekWTmbJSdwrGKP3AJsgsH0VW62pHmsz%2BhpRETkIRCeNggL0P95W8K6GqCya6AGdazqPdlcfu0AfYkOibRNJUnX%2BG8gN%2FYI6aamV%2BtUbwAYYNsY4SPahGwL3KNYwGvO6rThwTGb6u3MYqQFGf9oSnZ0dH%2FVTzh1PB5FxFGAiQzUfpAQrm%2Bng%2BTo9HRMEkwBTH4T&X-Amz-Signature=87fa39bdd164c3ecb89887c2b1e8bd9b7d5dc71d18dcb42211cd68360fc7e968&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
## 5.CSSの設定
- 必要に応じて設定してください。スライダーに関連した設定は以下の通り設定しています。
- 複数のスライダーで個別の設定を行う可能性を考慮して、スライダー固有のクラスである「swiper」、「swiper-slide」などに対して直接CSSを当てずに、親である「p-top-post」の子クラスに対してCSSを当てる形をとっています。
■src/scss/object/project/p-top-post.scss
```sass
：（省略）

.p-top-post .swiper {
  padding-bottom: 20px;
}

.p-top-post .swiper-slide {
  display: block;
  width: 100%;
  aspect-ratio: 600 / 300;
}

.p-top-post .swiper-slide img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.p-top-post .swiper-pagination {
  bottom: 0;
}

.p-top-post .swiper-button-prev,
.p-top-post .swiper-button-next {
  text-rendering: initial;
}

：（省略）
```
# 今回行ったこと
Swiper.jsを使用してスライダーのテンプレートを作成しました
【手順】
1.テンプレートファイルをテーマとして設定する
2.投稿記事を登録する
3.設定確認
4.動作確認
5.CSSの設定

## タグ

#Web制作 

## 関連ドキュメント

- [[../02_Web制作/済.md|済]]
- [[../04_ビジネス/テンプレート.md|テンプレート]]
- [[../01_よしなに対応/AI.md|AI]]
- [[../99_その他/JS.md|JS]]
- [[../99_その他/width.md|width]]
