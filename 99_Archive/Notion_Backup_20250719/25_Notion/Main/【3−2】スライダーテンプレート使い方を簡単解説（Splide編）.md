---
notion_id: ee85db2a-990e-4f47-99f3-30df78d39fc2
account: Main
title: 【3−2】スライダーテンプレート使い方を簡単解説（Splide編）
url: https://www.notion.so/3-2-Splide-ee85db2a990e4f4799f330df78d39fc2
created_time: 2023-09-11T00:13:00.000Z
last_edited_time: 2023-09-11T00:13:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:15.088522
---
# 【3−2】スライダーテンプレート使い方を簡単解説（Splide編）

【目次】
  
# 今回行うこと
Splide.jsを使用して、投稿記事のサムネイルをスライダー表示するためのテンプレートを作成する
【完成イメージ】
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/736adce6-a3a4-4a64-9f74-d9aa055c96d2/01ad3b9c-24e4-44f2-88b4-6400cf9870d5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665M4V7LSI%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T044538Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCZXxKIty97FZfCEubOp2SWxffxyzp1e8q%2F%2FLQ9o8nfgIhAPE%2F4YW9J5d%2BDa7zUeVIj9zxleK4pSxETuVCex38NF%2B%2FKogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyZ9TAWsVVrWr4OnOgq3APxf2%2FPYU60Lijtr4sf5dHoskhZJTmUi8%2FTPXmHRcS6kvC1gmRRdNLNNxndTXnRvoZo4ZxPM3fOW9muwGkAooWt4lSMVa3gkvDsg%2FsZR67z%2Fy2Cm5nYR3PuvfdI%2BF21iwcxamn17AAq44%2B6FJRqbV2c9kUJA0%2BZit0GOH1ApKDZpe3oxcFBAK6sPtaxkUD%2FqrXOU14VfsmR744Vtxo1BVNzZ0yMbx62Nqobcs6ZQLcUps9E3K7gEPOJKi9WFkKOHpjwfHAb4mQA5wS4bisaOisopnWzNWrQHOiqPJJAJQPhT5WFWCDdPuw0SbXly%2FQey8VpSdclOql9tb8hMLYPJA1wRssSheXdurHXjQJe%2BTKhvf6PH6ezpR03NK05cTvUzlidqH5u34mPf6cwlBVikqUuVQQ361R4WEHojYQDBOUYWYVcPN41OR5d3mtQL1EwcfMlqR6scYqg9pmg5XxEmSoyxt1zSdFAAYl10y1%2BPzkbO0C0rnaYNoRDAqYYq2MAUz5C78hC0sURMaoJ%2FPioyqucA2E75ErOYktiZ6M8HVbyFjCHdh%2F26f4bvRnG3DnbAJ56Ey2364FPdpAyRg0u6yy0LZYt0o5AWrIawlPsOP4EN9onSKwlxMBSXZuErDCkquzDBjqkAegHTB13SgSROQFhOl1%2BzS3U2vKqpGv14axT9Xjr0Jvp9dNS%2FNAUzimyjE0Zzyrh%2BmHpIHLgzrbf9IM%2F4Sz7ZAh34qg0Hr%2F0ZD51wlJi%2F3qlUJ%2BP3AnIhGVup3wYxCVuekxb58tQG3OTyRjBtWiBdtoq4Q4pMpU2apIWYXL8srh95j%2BIhIiwg1QlBNwz%2BIRRACbR5GYQvMQ%2BIY6M%2FXUi8oAX3mJm&X-Amz-Signature=6d093c4b08c6ffbabe1b6d62c13de998f59eca13874129de9e946b9cd7b681f7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
【手順】
1.テンプレートファイルをテーマとして設定する
2.投稿記事を登録する
3.設定確認
4.動作確認
5.CSSの設定
# Splide.jsを使用してスライダーのテンプレートを作成する
## 【注意事項】
- 次の内容は、**「**[2−2スライダーテンプレート使い方を簡単解説（Splide編）](/1cc5b47acebc4f8eb8ece6ca2b5395a4)**」**を確認してください。
  1.テンプレートファイルをテーマとして設定する
  ※既に実施済みの場合は、スキップしてください。
  
## 2.投稿記事を登録する
※既に実施済みの場合は、スキップしてください。
### （１）記事を登録する
■設定例
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/736adce6-a3a4-4a64-9f74-d9aa055c96d2/b4deb9a2-5c52-43fc-9236-2be6fc2409ca/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665M4V7LSI%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T044538Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCZXxKIty97FZfCEubOp2SWxffxyzp1e8q%2F%2FLQ9o8nfgIhAPE%2F4YW9J5d%2BDa7zUeVIj9zxleK4pSxETuVCex38NF%2B%2FKogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyZ9TAWsVVrWr4OnOgq3APxf2%2FPYU60Lijtr4sf5dHoskhZJTmUi8%2FTPXmHRcS6kvC1gmRRdNLNNxndTXnRvoZo4ZxPM3fOW9muwGkAooWt4lSMVa3gkvDsg%2FsZR67z%2Fy2Cm5nYR3PuvfdI%2BF21iwcxamn17AAq44%2B6FJRqbV2c9kUJA0%2BZit0GOH1ApKDZpe3oxcFBAK6sPtaxkUD%2FqrXOU14VfsmR744Vtxo1BVNzZ0yMbx62Nqobcs6ZQLcUps9E3K7gEPOJKi9WFkKOHpjwfHAb4mQA5wS4bisaOisopnWzNWrQHOiqPJJAJQPhT5WFWCDdPuw0SbXly%2FQey8VpSdclOql9tb8hMLYPJA1wRssSheXdurHXjQJe%2BTKhvf6PH6ezpR03NK05cTvUzlidqH5u34mPf6cwlBVikqUuVQQ361R4WEHojYQDBOUYWYVcPN41OR5d3mtQL1EwcfMlqR6scYqg9pmg5XxEmSoyxt1zSdFAAYl10y1%2BPzkbO0C0rnaYNoRDAqYYq2MAUz5C78hC0sURMaoJ%2FPioyqucA2E75ErOYktiZ6M8HVbyFjCHdh%2F26f4bvRnG3DnbAJ56Ey2364FPdpAyRg0u6yy0LZYt0o5AWrIawlPsOP4EN9onSKwlxMBSXZuErDCkquzDBjqkAegHTB13SgSROQFhOl1%2BzS3U2vKqpGv14axT9Xjr0Jvp9dNS%2FNAUzimyjE0Zzyrh%2BmHpIHLgzrbf9IM%2F4Sz7ZAh34qg0Hr%2F0ZD51wlJi%2F3qlUJ%2BP3AnIhGVup3wYxCVuekxb58tQG3OTyRjBtWiBdtoq4Q4pMpU2apIWYXL8srh95j%2BIhIiwg1QlBNwz%2BIRRACbR5GYQvMQ%2BIY6M%2FXUi8oAX3mJm&X-Amz-Signature=2d41a198a8d5b7c40d0ac67110b738c82e154eb775472d3e423800ec89fbff7f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
■参考（テスト用画像は以下から取得しています。申し訳ありませんが、ご準備ください！）
[Bookmark](https://pixabay.com/ja/)
### （２）必要な件数分登録する
■設定例
登録日時の降順（以下画面の表示順）で表示されます。
表示件数、表示順については、「【[3−7】１から作って使えるようにじっくり解説（PHPのコードを詳しく解説）](/b5d8fcc13fd947a7984b34b64638ae62)」で解説しています。
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/736adce6-a3a4-4a64-9f74-d9aa055c96d2/ea6a2623-90f2-4f6e-9144-e77b4e9a6b9a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665M4V7LSI%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T044538Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCZXxKIty97FZfCEubOp2SWxffxyzp1e8q%2F%2FLQ9o8nfgIhAPE%2F4YW9J5d%2BDa7zUeVIj9zxleK4pSxETuVCex38NF%2B%2FKogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyZ9TAWsVVrWr4OnOgq3APxf2%2FPYU60Lijtr4sf5dHoskhZJTmUi8%2FTPXmHRcS6kvC1gmRRdNLNNxndTXnRvoZo4ZxPM3fOW9muwGkAooWt4lSMVa3gkvDsg%2FsZR67z%2Fy2Cm5nYR3PuvfdI%2BF21iwcxamn17AAq44%2B6FJRqbV2c9kUJA0%2BZit0GOH1ApKDZpe3oxcFBAK6sPtaxkUD%2FqrXOU14VfsmR744Vtxo1BVNzZ0yMbx62Nqobcs6ZQLcUps9E3K7gEPOJKi9WFkKOHpjwfHAb4mQA5wS4bisaOisopnWzNWrQHOiqPJJAJQPhT5WFWCDdPuw0SbXly%2FQey8VpSdclOql9tb8hMLYPJA1wRssSheXdurHXjQJe%2BTKhvf6PH6ezpR03NK05cTvUzlidqH5u34mPf6cwlBVikqUuVQQ361R4WEHojYQDBOUYWYVcPN41OR5d3mtQL1EwcfMlqR6scYqg9pmg5XxEmSoyxt1zSdFAAYl10y1%2BPzkbO0C0rnaYNoRDAqYYq2MAUz5C78hC0sURMaoJ%2FPioyqucA2E75ErOYktiZ6M8HVbyFjCHdh%2F26f4bvRnG3DnbAJ56Ey2364FPdpAyRg0u6yy0LZYt0o5AWrIawlPsOP4EN9onSKwlxMBSXZuErDCkquzDBjqkAegHTB13SgSROQFhOl1%2BzS3U2vKqpGv14axT9Xjr0Jvp9dNS%2FNAUzimyjE0Zzyrh%2BmHpIHLgzrbf9IM%2F4Sz7ZAh34qg0Hr%2F0ZD51wlJi%2F3qlUJ%2BP3AnIhGVup3wYxCVuekxb58tQG3OTyRjBtWiBdtoq4Q4pMpU2apIWYXL8srh95j%2BIhIiwg1QlBNwz%2BIRRACbR5GYQvMQ%2BIY6M%2FXUi8oAX3mJm&X-Amz-Signature=ccd4a1bb6af298fa0806f27310ef53a703f56d6bc03dc25f9d12779ae238f4c2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
## 3.設定確認
### Splideで動作するよう設定する
「$slider_library」を「splide」に変更する
■parts/functions-lib/func-enqueue-assets.php（一部抜粋）
```php
function my_script_init()
{
  global $slider_library;
  $slider_library = 'splide'; //splide,swiper,slickから選択する

  :（省略）

}
```
## 4.動作確認
### （１）gulpを実行する
※既に実施済みの場合は、スキップしてください
- gulpfile.jsの設定を変更してください
  ![](https://prod-files-secure.s3.us-west-2.amazonaws.com/736adce6-a3a4-4a64-9f74-d9aa055c96d2/361d857a-b048-4684-ae53-0eaab8de8f48/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TL35JQQV%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T044539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDoRKxXsZDBpJberG6EtKa3NUjeeOX0v%2BIqcJp885v9BgIhAI7Hx645FsMmwY99SRHgPMUe3k8TLNpW2ItgI2c9faEGKogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwuRJienZ7PLLulSEEq3ANBN%2FWBuK%2BAiIF%2B6uN5pMrSL6PL5xhoptwxepr8I2hmRTEnc9hjBijdgcyb%2B6D%2B%2BhSlv2OFjriY8TbSVCo0I8Tg0uCuXT32rSegFD4BCoCulr3wyQIt6cXDI1dr7cjbiaUOsM6SjvI5A4DcSgOAvdYHxGuLMyA1kvN3btRlBINecUICZgOBbrs%2BwLsDsyAwV4%2Bns1Am4GmS31%2FvVlYwLrWEohBdUF2Lb0P4xwf6iLJUCdiVHorfhJRYokIZEZ3wf9GUWKehNpWYjhbX8uHhQM%2FzSwXjE4Hv6FWpTjjnZcIfnvGBRDg6Ws7tJxMVbMkVGGYGELRILlVQL6LpJvflq7kvmd%2BL6ln%2BHKn3xPcPss7O0mA%2BqmtwUS9pgOcr8c1ZYwkq4KJWQW7cAOgsNxEcN34B1R8kZx0KtuM9rKwJ%2BmyY3ZSVRV3K7WlIZD4gIpXfpjN5UOjxhM3ZL1IBCKhdlUuyAugqZODCZuct9K%2BSy7H%2BXf%2BmoHXegWY53pMtlxBNDoUb7XS%2FUz5kjG46qaGCd6MM39xki%2ByQnOtEd4HQYouS3FJv4aEk0MSdoIfD4LAOcrQ69bvPoYe%2FcAmIyiZxJPdb2aVyfZyWLfKcAXm9bD0LjioBK5NN2CWJCe2A9jDpquzDBjqkARL0SV%2FZ%2BIrTTx5WDvX%2BKkULtyP7gi%2FnK5nSd4LuVyRkqgidUob5WXHkgAFDkcX6eX7v1CyCkmL%2BNQ58R9beZBmuIP21KvZVbbDKJFnpgW8VnMf%2BahbA7ofi%2BOgfWg%2Bk1MyJ5cRh%2FjLqt3OMQOPZUHac1j7ey%2B1ONb4oKEvIT1IwnwVwRunwedd8%2FnW%2FmxJyX3okqmhB%2F40tNztpHT9zFQJ5RUX7&X-Amz-Signature=2f2b2f3c7154337fc5b8e9bdc987fc84a3e7908deb5234486161dd988cf8c3c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
  
  ![](https://prod-files-secure.s3.us-west-2.amazonaws.com/736adce6-a3a4-4a64-9f74-d9aa055c96d2/e6e5a21a-2bbf-4b67-bf17-c09e645e54ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TL35JQQV%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T044539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDoRKxXsZDBpJberG6EtKa3NUjeeOX0v%2BIqcJp885v9BgIhAI7Hx645FsMmwY99SRHgPMUe3k8TLNpW2ItgI2c9faEGKogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwuRJienZ7PLLulSEEq3ANBN%2FWBuK%2BAiIF%2B6uN5pMrSL6PL5xhoptwxepr8I2hmRTEnc9hjBijdgcyb%2B6D%2B%2BhSlv2OFjriY8TbSVCo0I8Tg0uCuXT32rSegFD4BCoCulr3wyQIt6cXDI1dr7cjbiaUOsM6SjvI5A4DcSgOAvdYHxGuLMyA1kvN3btRlBINecUICZgOBbrs%2BwLsDsyAwV4%2Bns1Am4GmS31%2FvVlYwLrWEohBdUF2Lb0P4xwf6iLJUCdiVHorfhJRYokIZEZ3wf9GUWKehNpWYjhbX8uHhQM%2FzSwXjE4Hv6FWpTjjnZcIfnvGBRDg6Ws7tJxMVbMkVGGYGELRILlVQL6LpJvflq7kvmd%2BL6ln%2BHKn3xPcPss7O0mA%2BqmtwUS9pgOcr8c1ZYwkq4KJWQW7cAOgsNxEcN34B1R8kZx0KtuM9rKwJ%2BmyY3ZSVRV3K7WlIZD4gIpXfpjN5UOjxhM3ZL1IBCKhdlUuyAugqZODCZuct9K%2BSy7H%2BXf%2BmoHXegWY53pMtlxBNDoUb7XS%2FUz5kjG46qaGCd6MM39xki%2ByQnOtEd4HQYouS3FJv4aEk0MSdoIfD4LAOcrQ69bvPoYe%2FcAmIyiZxJPdb2aVyfZyWLfKcAXm9bD0LjioBK5NN2CWJCe2A9jDpquzDBjqkARL0SV%2FZ%2BIrTTx5WDvX%2BKkULtyP7gi%2FnK5nSd4LuVyRkqgidUob5WXHkgAFDkcX6eX7v1CyCkmL%2BNQ58R9beZBmuIP21KvZVbbDKJFnpgW8VnMf%2BahbA7ofi%2BOgfWg%2Bk1MyJ5cRh%2FjLqt3OMQOPZUHac1j7ey%2B1ONb4oKEvIT1IwnwVwRunwedd8%2FnW%2FmxJyX3okqmhB%2F40tNztpHT9zFQJ5RUX7&X-Amz-Signature=1bc7490f8a4f2d41f37df4e995e7d52abf1b5de2b620e56cbd5be182dd6c3f17&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/736adce6-a3a4-4a64-9f74-d9aa055c96d2/a98b1a3f-3e17-4920-a45f-8a64bb13e377/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665M4V7LSI%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T044538Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCZXxKIty97FZfCEubOp2SWxffxyzp1e8q%2F%2FLQ9o8nfgIhAPE%2F4YW9J5d%2BDa7zUeVIj9zxleK4pSxETuVCex38NF%2B%2FKogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyZ9TAWsVVrWr4OnOgq3APxf2%2FPYU60Lijtr4sf5dHoskhZJTmUi8%2FTPXmHRcS6kvC1gmRRdNLNNxndTXnRvoZo4ZxPM3fOW9muwGkAooWt4lSMVa3gkvDsg%2FsZR67z%2Fy2Cm5nYR3PuvfdI%2BF21iwcxamn17AAq44%2B6FJRqbV2c9kUJA0%2BZit0GOH1ApKDZpe3oxcFBAK6sPtaxkUD%2FqrXOU14VfsmR744Vtxo1BVNzZ0yMbx62Nqobcs6ZQLcUps9E3K7gEPOJKi9WFkKOHpjwfHAb4mQA5wS4bisaOisopnWzNWrQHOiqPJJAJQPhT5WFWCDdPuw0SbXly%2FQey8VpSdclOql9tb8hMLYPJA1wRssSheXdurHXjQJe%2BTKhvf6PH6ezpR03NK05cTvUzlidqH5u34mPf6cwlBVikqUuVQQ361R4WEHojYQDBOUYWYVcPN41OR5d3mtQL1EwcfMlqR6scYqg9pmg5XxEmSoyxt1zSdFAAYl10y1%2BPzkbO0C0rnaYNoRDAqYYq2MAUz5C78hC0sURMaoJ%2FPioyqucA2E75ErOYktiZ6M8HVbyFjCHdh%2F26f4bvRnG3DnbAJ56Ey2364FPdpAyRg0u6yy0LZYt0o5AWrIawlPsOP4EN9onSKwlxMBSXZuErDCkquzDBjqkAegHTB13SgSROQFhOl1%2BzS3U2vKqpGv14axT9Xjr0Jvp9dNS%2FNAUzimyjE0Zzyrh%2BmHpIHLgzrbf9IM%2F4Sz7ZAh34qg0Hr%2F0ZD51wlJi%2F3qlUJ%2BP3AnIhGVup3wYxCVuekxb58tQG3OTyRjBtWiBdtoq4Q4pMpU2apIWYXL8srh95j%2BIhIiwg1QlBNwz%2BIRRACbR5GYQvMQ%2BIY6M%2FXUi8oAX3mJm&X-Amz-Signature=68863a97beb32d041b4dd7f4ec5b319a84dddb61d57ae9048071aeb948da79fa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
## 5.CSSの設定
- 必要に応じて設定してください。スライダーに関連した設定は以下の通り設定しています。
- 複数のスライダーで個別の設定を行う可能性を考慮して、スライダー固有のクラスである「splide」、「splide__slide」などに対して直接CSSを当てずに、親である「p-top-post」の子クラスに対してCSSを当てる形をとっています。
■parts/project/p-top-post.php
```sass
@use 'foundation' as *;

.p-top-post__inner {
  margin: 5% 5% 0 5%;
}

.p-top-post .splide {

}

.p-top-post .splide__slide {
  display: block;
  width: 100%;
}

.p-top-post .splide__slide a {
  display: block;
  aspect-ratio: 600 / 400;
}

.p-top-post .splide__slide img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.p-top-post .splide__pagination {
  bottom: -2em;
}

.p-top-post .splide__pagination__page.is-active {
  background-color: blue;
}

：（省略）
```
# 今回行ったこと
Splide.jsを使用してスライダーのテンプレートを作成しました
【手順】
1.テンプレートファイルをテーマとして設定する
2.投稿記事を登録する
3.設定確認
4.動作確認
5.CSSの設定