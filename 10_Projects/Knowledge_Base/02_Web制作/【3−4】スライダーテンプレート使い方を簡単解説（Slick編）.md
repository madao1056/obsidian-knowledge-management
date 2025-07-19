---
notion_id: c41a00d9-4596-454e-a5fd-113ccedaa13d
account: Main
title: 【3−4】スライダーテンプレート使い方を簡単解説（Slick編）
url: https://www.notion.so/3-4-Slick-c41a00d94596454ea5fd113ccedaa13d
created_time: 2023-09-11T00:13:00.000Z
last_edited_time: 2023-09-11T00:13:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:15.088197
---
# 【3−4】スライダーテンプレート使い方を簡単解説（Slick編）

【目次】
  
# 今回行うこと
Slick.jsを使用して、投稿記事のサムネイルをスライダー表示するためのテンプレートを作成する
【完成イメージ】
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/736adce6-a3a4-4a64-9f74-d9aa055c96d2/bbc097a1-eaef-46cc-b9f4-155472e80c11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662D35XM6%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T044543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDcHA30WPxA4o%2B%2FhLhyLvddbkAefFtHuuwjS5pIAhyu8AiBkJN9GYr3EioMbxmQtJUs7nbJvE1ZSLJRZW1q42nUUmyqIBAid%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9pGRUr1lzOECxAjnKtwDv57nmn0MUlBHDJov6ROAN8XdFTiujyjIL8lZ2UNeHbrpS8OHL1yLQFvn5hdKDiBAKpp0qcSFBzDTwZOfAYiRDMzVEpNUk%2FuJY30lrbppuNLx2NuGHhEihviAHkrtnJZXxVmOQjjelr6tmLu%2FQIhaDixViX6hdpC5YwxlovziUin9mrHgSmRwY5NlNu%2B00zbgEDAR%2BwQgAptr%2BMmUdt6A1PaPbfs0TlbFRulN1VD3y0FpEy1YH3wdue6eYmbWMx43OMO3lCdP6UolNlytbOimxczWneW%2BvHlcDWYfw0lJSNO%2FVzGoMW3Nk7yfF5DAjYa3oa%2BUekyyqaF%2BWaTB5S3NAl13Evwx75jgYJFELO%2BK4BdKJ9vW8rM0slx1zh4%2FBLtKTEXf18gQQ40fd3nmlimVrXgU%2Fet%2BIZzVv1YHAzrReTpBCCThzz8BQL8tlLy9r8GIFdY5hoCq%2FFka4ovrmtld69ka0AgS5VQLCzrnfs3IzFrpB6sy58cgeNIdXzfIh1NFcu5WNasdMZ%2FCTM7rTlLnX4AnPwdiieJRzoE1wf4PYe38Ylvkcawp54FzXVS7IOMv664jweleKXNo1VVkDyqPpkT2v37RVOPJpqz3tXr0kFONwF4LtYPmnqf%2Fxs0wsarswwY6pgGV%2BtOg4LJO3PKwMe1hHuheHFms7T31n0JbrM6ai7hb%2BalJR1Rd5mxNgJvbf%2FUdo260Xirhx%2F1LRCf%2BhGrtOvrIq9inHxQbu75ueEc0UMfvZPcY5%2Be8igIytcmi6Q%2Bt0gvEf31LBCjAOAtDONxZN8gJYamvJ0pY%2Fca0SV5ue4E4j9O4RivgqmKLS1Dx2rD15f6zys4A73gWtYmJdpJ4aHNdbxZzevqZ&X-Amz-Signature=82ea1300e84a6845ac095b4db14e0e9e6a2d7816363b12fd421dd160d73d2fd0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
【手順】
1.テンプレートファイルをテーマとして設定する
2.投稿記事を登録する
3.設定確認
4.動作確認
5.CSSの設定
# Slick.jsを使用してスライダーのテンプレートを作成する
## 【注意事項】
- 次の内容は、**「**[3−2スライダーテンプレート使い方を簡単解説（Splide編）](/ee85db2a990e4f4799f330df78d39fc2)**」**を確認してください。
  1.テンプレートファイルをテーマとして設定する
  2.投稿記事を登録する
## 3.設定確認
### Slickで動作するよう設定する
「$slider_library」を「slick」に変更する
■parts/functions-lib/func-enqueue-assets.php（一部抜粋）
```php
function my_script_init()
{
  global $slider_library;
  $slider_library = 'slick'; //splide,swiper,slickから選択する

  :（省略）

}
```
## 4.動作確認
### （１）gulpを実行する
※既に実施済みの場合は、スキップしてください
- gulpfile.jsの設定を変更してください
  ![](https://prod-files-secure.s3.us-west-2.amazonaws.com/736adce6-a3a4-4a64-9f74-d9aa055c96d2/361d857a-b048-4684-ae53-0eaab8de8f48/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHJUKISC%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T044544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCIjKVBuLaxq2WtBADLbdfvy5605gpBIOmXAiq1UPayhgIgcmAWXhZzbJzOYYZXnDntdI%2F%2Fl8ygwLJ%2FSRZEKdghQd4qiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHSe28MVnxnLhKpg5ircA%2F5NdXXXhwFc5aJHeisb%2BoYHbRAd%2BlwGy0zOyxE9AcqvH6zqNb9Bg1B6B1ArYR%2BbFBN0HZBgs0IqJfCMNMI%2BCuX1FeQ7HuC9CuOr1nZsnwhvheLh9ysIg751qTXUnoaRmScFfh0G0ZJ5rFA48Ikj9uwwxKEBNYSKH8r94%2F7%2B6HrxbAbhHKd%2F8lOSiC%2F1uTKL7OC%2BIL1he98ojkzsI6n2Wn5%2FRu3DSwzJ8%2FIJrYiMNI1ManUBppVufY9qBjeDr5tOR2qQJ3bBcOaaOaTQcN89X6GxC%2FIWFeFQjl748pcfUw0kplfcQgKuUY4qFBkrUjZzm0Qnbo5UkOnSScWwSow%2B6ved%2B8S0LhysGcBwtXA%2BzK6ucj%2Fy8dNUXXqFMNDSAWvzBZfutr7NaSl5o40yNYBO%2BRqPKnps%2FGsqB7Ca%2BuZtWqNefXn6rHm8KEtgdW01ABjAam2OkbfZS89Db1D2BCFfv8WBrpLR72faSq7uwlpJTm2BtkSQ8W9G1LplPE6V8D1sVognVeqMWKl5DjBwFXck9E7icUU5bF3MveFlJGK2zbCyJ8ijUjF2icox%2BclcLtMXODjBVaFkTzLzumaXggE58exBwecVp9AOgZRxsYoNKBhOQjnuIZYblQ43rM9GMI2r7MMGOqUBnvKTlt3oej7HEhqRwG5EiZMqCbUkDVQmirAw80nIoVP0flO2af2Gg5L4a4fVVTIaGCYoJmrEKB4dol1zoBa0n%2FIYAz4wGKxaND07zwNhte9H%2F7JlDQGmSx7fCKnaAz7cgJtjv%2BR%2FjLs37GBYlIzLRQxEQ4He4lwuuksdM3fn71te660JVcxuOgwCu%2BQwqNQpQPnfNfJ58EL%2FPNW0lr%2FLo6ESnfrZ&X-Amz-Signature=5be8b3ead3cc6bd8334dc9d6975144a444ecb387c170b9aaa2b862218f07388d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
  
  ![](https://prod-files-secure.s3.us-west-2.amazonaws.com/736adce6-a3a4-4a64-9f74-d9aa055c96d2/e6e5a21a-2bbf-4b67-bf17-c09e645e54ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHJUKISC%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T044544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCIjKVBuLaxq2WtBADLbdfvy5605gpBIOmXAiq1UPayhgIgcmAWXhZzbJzOYYZXnDntdI%2F%2Fl8ygwLJ%2FSRZEKdghQd4qiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHSe28MVnxnLhKpg5ircA%2F5NdXXXhwFc5aJHeisb%2BoYHbRAd%2BlwGy0zOyxE9AcqvH6zqNb9Bg1B6B1ArYR%2BbFBN0HZBgs0IqJfCMNMI%2BCuX1FeQ7HuC9CuOr1nZsnwhvheLh9ysIg751qTXUnoaRmScFfh0G0ZJ5rFA48Ikj9uwwxKEBNYSKH8r94%2F7%2B6HrxbAbhHKd%2F8lOSiC%2F1uTKL7OC%2BIL1he98ojkzsI6n2Wn5%2FRu3DSwzJ8%2FIJrYiMNI1ManUBppVufY9qBjeDr5tOR2qQJ3bBcOaaOaTQcN89X6GxC%2FIWFeFQjl748pcfUw0kplfcQgKuUY4qFBkrUjZzm0Qnbo5UkOnSScWwSow%2B6ved%2B8S0LhysGcBwtXA%2BzK6ucj%2Fy8dNUXXqFMNDSAWvzBZfutr7NaSl5o40yNYBO%2BRqPKnps%2FGsqB7Ca%2BuZtWqNefXn6rHm8KEtgdW01ABjAam2OkbfZS89Db1D2BCFfv8WBrpLR72faSq7uwlpJTm2BtkSQ8W9G1LplPE6V8D1sVognVeqMWKl5DjBwFXck9E7icUU5bF3MveFlJGK2zbCyJ8ijUjF2icox%2BclcLtMXODjBVaFkTzLzumaXggE58exBwecVp9AOgZRxsYoNKBhOQjnuIZYblQ43rM9GMI2r7MMGOqUBnvKTlt3oej7HEhqRwG5EiZMqCbUkDVQmirAw80nIoVP0flO2af2Gg5L4a4fVVTIaGCYoJmrEKB4dol1zoBa0n%2FIYAz4wGKxaND07zwNhte9H%2F7JlDQGmSx7fCKnaAz7cgJtjv%2BR%2FjLs37GBYlIzLRQxEQ4He4lwuuksdM3fn71te660JVcxuOgwCu%2BQwqNQpQPnfNfJ58EL%2FPNW0lr%2FLo6ESnfrZ&X-Amz-Signature=ce0f4f3752c5140861a21fa5c112e8902b058fccb376b9249c39e6d8f66c7acb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/736adce6-a3a4-4a64-9f74-d9aa055c96d2/adc01b5f-59b8-46b0-9721-cc5473a31ca6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662D35XM6%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T044543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDcHA30WPxA4o%2B%2FhLhyLvddbkAefFtHuuwjS5pIAhyu8AiBkJN9GYr3EioMbxmQtJUs7nbJvE1ZSLJRZW1q42nUUmyqIBAid%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9pGRUr1lzOECxAjnKtwDv57nmn0MUlBHDJov6ROAN8XdFTiujyjIL8lZ2UNeHbrpS8OHL1yLQFvn5hdKDiBAKpp0qcSFBzDTwZOfAYiRDMzVEpNUk%2FuJY30lrbppuNLx2NuGHhEihviAHkrtnJZXxVmOQjjelr6tmLu%2FQIhaDixViX6hdpC5YwxlovziUin9mrHgSmRwY5NlNu%2B00zbgEDAR%2BwQgAptr%2BMmUdt6A1PaPbfs0TlbFRulN1VD3y0FpEy1YH3wdue6eYmbWMx43OMO3lCdP6UolNlytbOimxczWneW%2BvHlcDWYfw0lJSNO%2FVzGoMW3Nk7yfF5DAjYa3oa%2BUekyyqaF%2BWaTB5S3NAl13Evwx75jgYJFELO%2BK4BdKJ9vW8rM0slx1zh4%2FBLtKTEXf18gQQ40fd3nmlimVrXgU%2Fet%2BIZzVv1YHAzrReTpBCCThzz8BQL8tlLy9r8GIFdY5hoCq%2FFka4ovrmtld69ka0AgS5VQLCzrnfs3IzFrpB6sy58cgeNIdXzfIh1NFcu5WNasdMZ%2FCTM7rTlLnX4AnPwdiieJRzoE1wf4PYe38Ylvkcawp54FzXVS7IOMv664jweleKXNo1VVkDyqPpkT2v37RVOPJpqz3tXr0kFONwF4LtYPmnqf%2Fxs0wsarswwY6pgGV%2BtOg4LJO3PKwMe1hHuheHFms7T31n0JbrM6ai7hb%2BalJR1Rd5mxNgJvbf%2FUdo260Xirhx%2F1LRCf%2BhGrtOvrIq9inHxQbu75ueEc0UMfvZPcY5%2Be8igIytcmi6Q%2Bt0gvEf31LBCjAOAtDONxZN8gJYamvJ0pY%2Fca0SV5ue4E4j9O4RivgqmKLS1Dx2rD15f6zys4A73gWtYmJdpJ4aHNdbxZzevqZ&X-Amz-Signature=b36cea0e0b30e37c1278918f6b941777746ad6761d5bf81e26a260d8eabd70c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
## 5.CSSの設定
- 必要に応じて設定してください。スライダーに関連した設定は以下の通り設定しています。
- 複数のスライダーで個別の設定を行う可能性を考慮して、スライダー固有のクラスである「slider」、「slick-list」などに対して直接CSSを当てずに、親である「p-top-post」の子クラスに対してCSSを当てる形をとっています。
■src/scss/object/project/p-top-post.scss（抜粋）
```sass
：（省略）

.p-top-post__inner {
  margin: 5% 5% 0 5%;
}

//　slick用
.p-top-post .slick-track {
  display: block;
  width: 100%;
}

.p-top-post .slick-slide {
  display: block;
  width: 100%;
  height: 100%;
  margin: 0 5px;
}

.p-top-post .slick-slide img {
  display: block;
  width: 100%;
  height: 100%;
  aspect-ratio: 600 / 300;
  object-fit: cover;
}
.p-top-post .slick-next,
.p-top-post .slick-prev {
  background: gray;
}

：（省略）
```
# 今回行ったこと
Slick.jsを使用してスライダーのテンプレートを作成しました
【手順】
1.テンプレートファイルをテーマとして設定する
2.投稿記事を登録する
3.設定確認
4.動作確認
5.CSSの設定

## タグ

#Web制作 

## 関連ドキュメント

- [[../02_Web制作/swiper.md|swiper]]
- [[../02_Web制作/済.md|済]]
- [[../99_その他/FV.md|FV]]
- [[../01_よしなに対応/「.md|「]]
- [[../99_その他/Untitled.md|Untitled]]
