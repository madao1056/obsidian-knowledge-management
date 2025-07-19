---
notion_id: a9e366ca-cb9a-4a5c-aa7d-fde694c056fd
account: Main
title: 【2−4】スライダーテンプレート使い方を簡単解説（Slick編）
url: https://www.notion.so/2-4-Slick-a9e366cacb9a4a5caa7dfde694c056fd
created_time: 2023-09-11T00:13:00.000Z
last_edited_time: 2023-09-11T00:13:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:15.086117
---
# 【2−4】スライダーテンプレート使い方を簡単解説（Slick編）

【目次】
# 今回行うこと
Slick.jsを使用してスライダーのテンプレートを作成する
【完成イメージ】
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/736adce6-a3a4-4a64-9f74-d9aa055c96d2/2fe0c340-591f-4dd3-9a22-c6ac30b65ff4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCIYD6RN%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T044516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCHh8jJXZdRJOsh2LNilBQ2t%2BQwDsokSw5%2B1E1vSVA3NwIhAKkyb%2F5DPKKu5LF%2BpgnaWgJxjRtMEtgLgGuDky0clC%2BZKogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx56iHJxJVSc2LVMnkq3ANeR6u17c0%2FPMZ%2BXbqq4JgwckqcJnPJSg4dOjiL%2FT950m3J7by5S4gJtXo%2Fzy0CmxMrF2E%2FtyEhmMHdW5c6ye1vAhA%2BKYG6gOxyUYeuM4OIZ%2BOnGj1iRIbsYqTRVfOi%2FGhrPs5Mmr5x3IgPpH5ZjDUL7KvtmYcSZ9Ln9ULEtLdl9ZPcygB%2B0riZPE19ql0LKo0Ujq80QPVgBdj5EvOtEWB6%2BQDEvg8XEUZFK%2BCdZPOS9OyySrZbhf2OOe0r2Jti7dDdDz8p5eNfDmQyFV9kXH9pAd39b67xODxjwelvM4BriiPqDBwREIqJHEbVG3Xcz35SaI6yKlvby0fvRR3i0AWGT4td2LVOL74cboz5Zt0Ub1R0%2BDiH6v%2B%2BnhaY7kuS%2FMpUPX9MlGj6RFLOwLMET9DSQUDd15i3ggowq4EK1AOTxbspsGU%2FGv%2BeR%2B1T3YlBLJiLG%2FQwtM2ddw8F3KCeWFXyfVAa1BJwbX4%2FeJENTDJmY6WyN8oqg1coT9AsrjSHwaCgMHYCFMKIBc%2BMTs8gxqUz0ceu3MpsawLXC%2FrIqYKamTDx9nLN%2FQUyrDquZwcKbwTDtWjjmXj6nm3zu7kuszOTcKiy7P3OrIDVTqnRC3CPjOSRQlCeYkz8%2FssJGTDiquzDBjqkAezy%2Fn0PCDx2n2oOHsWS8Nq9qz7DN5DQu9ROiCcrIcpZdZOowKa96N7EtARWz4cQhrHU5dWn87s5DE6csJ0T2C3ixcJaiZ%2BQA54RCrdWao%2F%2BZNzOxUd4G%2Fez2Mjj3iCtyStXBVTShMcQ7oGZvYMbcxTl0bhmVbgv0HHOmxurxwigqaX6l3cNIm0J3kdKN%2F07QHXMQi2a2l2e5mEAuc5YXGLTFK7r&X-Amz-Signature=e5f2ad0643c885ea006049a922697a2a86b65354efdcefb48aeb1074037437d1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
【手順】
1.テンプレートファイルをテーマとして設定する
2.Advanced Custom Fieldsプラグインをインストール
3.カスタムフィールド設定データをインポート
4.投稿タイプ「MVスライダー」に画像等を設定する
5.設定確認
6.動作確認
7.CSSの設定
# Slick.jsを使用してスライダーのテンプレートを作成する
## 【注意事項】
- 次の内容は、**「**[**スライダーテンプレート使い方を簡単解説（Splide編）**](/1cc5b47acebc4f8eb8ece6ca2b5395a4)**」**を確認してください。
  1.テンプレートファイルをテーマとして設定する
  2.Advanced Custom Fieldsプラグインをインストール
  3.カスタムフィールド設定データをインポート
  4.投稿タイプ「MVスライダー」に画像等を設定する
## 5.設定確認
### Slickで動作するよう設定する
「$slider_library」を「slick」に変更する。
なお、「$slider_library」は、スライダーの切り替え以外の用途では絶対に使用しないでください！
■parts/functions-lib/func-enqueue-assets.php（一部抜粋）
```php
function my_script_init()
{
  global $slider_library;
  $slider_library = 'slick'; //splide,swiper,slickから選択する

  :（省略）

}
```
## 6.動作確認
### （１）gulpを実行する
※既に実施済みの場合は、スキップしてください
- gulpfile.jsの設定を変更してください
  ![](https://prod-files-secure.s3.us-west-2.amazonaws.com/736adce6-a3a4-4a64-9f74-d9aa055c96d2/361d857a-b048-4684-ae53-0eaab8de8f48/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466466QRLJM%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T044520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCXS7zu91qs%2FPu2wNU8KJOPVCEAFhGoKypVO2ZJ%2FHvAfgIgFU65Takqt8QimrfZfPAhUaUrtzObi%2F%2BUu7MpHBUx1VUqiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKyE3ng1UYACRuE1HyrcAy57fxzrA1XG%2BC1kWYix4Whu7k6b8EX%2F5Luosygvz1LwiCcez2bp0PwZYeitGPfh2MROjmGHH5smBQbqJyDQv%2FhAVkcRNahpsXSIAAAoPnuqoTmOX%2Bk7Nz9d4NTMMIgJ5zktzCUSpT9JJysZTF1clMBAhXw4b28OV48H1no5y0gBwTTV%2FiOAo%2BTMTg9xF1ZKwwW2NSynYtGvO%2Bs1CCmVz%2FfwCJmHdOvjT11doJNJXxqW5XjjFSueDfkU57tGZTs%2FGXh8LqnyS3zFGoX8wPbdWHIclqNCb0TyIncuwRZfzXOnW7LItLgOxHmusi4V598bI0yODalj9G5%2FVD9RPnm2EdkhM%2BlSs3iGg03VO2SdNq5DVyNdFT5%2FWxL1j6zOfYHzkxY1wCVhMqNaRVJGvEmCCVK8OE%2BZ4GFnLa%2FYwAIzFTLuvR7Yj%2F23Ks7WCtDKUpjJJ6sqN7FUACRmLWP6b%2B8qM9z%2Bf3ZQeJVmn00nE4es5LR8jPgS3dmGtObLpFz2GdHo9vzjuVYjfZuWI6YFJwDV39HRjs%2Fan1qQO%2F0GruGrjiKa3%2Fb%2FtfibfFPIxXRL215QQRgnHl7iDJjPoT7yKQf9R4xdp4iRaGROu7ueWC9pBmXPBCGZcGEqhSEsXkJSMNKq7MMGOqUBKFYf5evaUPbam2zJhEp3aGXVlJPjEUM7AFnS4d0HuFg5W0LfwjIYeg7dipmsARdOjpZu6%2FOvbJX9iSGB0%2FuAEv7gjmxtDLggm3gbXCcdZI%2Fl01qPzkAm2b0%2BoGIuHCZxwPclW2bMiBP03CRRgmwA6Yfwl67fTRQ%2BoCu19O4UhaBHXVSxzoxVNctLmHox42WOBFh70r3G5gW9jZvg77uKtaZgvJSO&X-Amz-Signature=f7e94f6643b2c71b207c7ea1f987518eac36d2df0d95f5c20e3b461ea71c700d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
  
  ![](https://prod-files-secure.s3.us-west-2.amazonaws.com/736adce6-a3a4-4a64-9f74-d9aa055c96d2/e6e5a21a-2bbf-4b67-bf17-c09e645e54ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466466QRLJM%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T044520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCXS7zu91qs%2FPu2wNU8KJOPVCEAFhGoKypVO2ZJ%2FHvAfgIgFU65Takqt8QimrfZfPAhUaUrtzObi%2F%2BUu7MpHBUx1VUqiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKyE3ng1UYACRuE1HyrcAy57fxzrA1XG%2BC1kWYix4Whu7k6b8EX%2F5Luosygvz1LwiCcez2bp0PwZYeitGPfh2MROjmGHH5smBQbqJyDQv%2FhAVkcRNahpsXSIAAAoPnuqoTmOX%2Bk7Nz9d4NTMMIgJ5zktzCUSpT9JJysZTF1clMBAhXw4b28OV48H1no5y0gBwTTV%2FiOAo%2BTMTg9xF1ZKwwW2NSynYtGvO%2Bs1CCmVz%2FfwCJmHdOvjT11doJNJXxqW5XjjFSueDfkU57tGZTs%2FGXh8LqnyS3zFGoX8wPbdWHIclqNCb0TyIncuwRZfzXOnW7LItLgOxHmusi4V598bI0yODalj9G5%2FVD9RPnm2EdkhM%2BlSs3iGg03VO2SdNq5DVyNdFT5%2FWxL1j6zOfYHzkxY1wCVhMqNaRVJGvEmCCVK8OE%2BZ4GFnLa%2FYwAIzFTLuvR7Yj%2F23Ks7WCtDKUpjJJ6sqN7FUACRmLWP6b%2B8qM9z%2Bf3ZQeJVmn00nE4es5LR8jPgS3dmGtObLpFz2GdHo9vzjuVYjfZuWI6YFJwDV39HRjs%2Fan1qQO%2F0GruGrjiKa3%2Fb%2FtfibfFPIxXRL215QQRgnHl7iDJjPoT7yKQf9R4xdp4iRaGROu7ueWC9pBmXPBCGZcGEqhSEsXkJSMNKq7MMGOqUBKFYf5evaUPbam2zJhEp3aGXVlJPjEUM7AFnS4d0HuFg5W0LfwjIYeg7dipmsARdOjpZu6%2FOvbJX9iSGB0%2FuAEv7gjmxtDLggm3gbXCcdZI%2Fl01qPzkAm2b0%2BoGIuHCZxwPclW2bMiBP03CRRgmwA6Yfwl67fTRQ%2BoCu19O4UhaBHXVSxzoxVNctLmHox42WOBFh70r3G5gW9jZvg77uKtaZgvJSO&X-Amz-Signature=0a244bc509b49b3ff15d5d9b696cb2fd955a828f2dc52a3dbe0e83cb1fff24c4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/736adce6-a3a4-4a64-9f74-d9aa055c96d2/16715b02-f6a6-4208-8b3a-145cacbfa2dc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCIYD6RN%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T044516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCHh8jJXZdRJOsh2LNilBQ2t%2BQwDsokSw5%2B1E1vSVA3NwIhAKkyb%2F5DPKKu5LF%2BpgnaWgJxjRtMEtgLgGuDky0clC%2BZKogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx56iHJxJVSc2LVMnkq3ANeR6u17c0%2FPMZ%2BXbqq4JgwckqcJnPJSg4dOjiL%2FT950m3J7by5S4gJtXo%2Fzy0CmxMrF2E%2FtyEhmMHdW5c6ye1vAhA%2BKYG6gOxyUYeuM4OIZ%2BOnGj1iRIbsYqTRVfOi%2FGhrPs5Mmr5x3IgPpH5ZjDUL7KvtmYcSZ9Ln9ULEtLdl9ZPcygB%2B0riZPE19ql0LKo0Ujq80QPVgBdj5EvOtEWB6%2BQDEvg8XEUZFK%2BCdZPOS9OyySrZbhf2OOe0r2Jti7dDdDz8p5eNfDmQyFV9kXH9pAd39b67xODxjwelvM4BriiPqDBwREIqJHEbVG3Xcz35SaI6yKlvby0fvRR3i0AWGT4td2LVOL74cboz5Zt0Ub1R0%2BDiH6v%2B%2BnhaY7kuS%2FMpUPX9MlGj6RFLOwLMET9DSQUDd15i3ggowq4EK1AOTxbspsGU%2FGv%2BeR%2B1T3YlBLJiLG%2FQwtM2ddw8F3KCeWFXyfVAa1BJwbX4%2FeJENTDJmY6WyN8oqg1coT9AsrjSHwaCgMHYCFMKIBc%2BMTs8gxqUz0ceu3MpsawLXC%2FrIqYKamTDx9nLN%2FQUyrDquZwcKbwTDtWjjmXj6nm3zu7kuszOTcKiy7P3OrIDVTqnRC3CPjOSRQlCeYkz8%2FssJGTDiquzDBjqkAezy%2Fn0PCDx2n2oOHsWS8Nq9qz7DN5DQu9ROiCcrIcpZdZOowKa96N7EtARWz4cQhrHU5dWn87s5DE6csJ0T2C3ixcJaiZ%2BQA54RCrdWao%2F%2BZNzOxUd4G%2Fez2Mjj3iCtyStXBVTShMcQ7oGZvYMbcxTl0bhmVbgv0HHOmxurxwigqaX6l3cNIm0J3kdKN%2F07QHXMQi2a2l2e5mEAuc5YXGLTFK7r&X-Amz-Signature=123d7709a6724d09d9a4fffb6ac679c22960e57b57a5382edf6c343afed17b13&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
## 7.CSSの設定
- 必要に応じて設定してください。スライダーに関連した設定は以下の通り設定しています。
- 複数のスライダーで個別の設定を行う可能性を考慮して、スライダー固有のクラスである「slick-slider」、「slick-slide」などに対して直接CSSを当てずに、親である「p-top-mv-slick」の子クラスに対してCSSを当てる形をとっています。
■src/scss/object/project/p-top-mv-slick.scss
```sass
@use 'foundation' as *;

.p-top-mv-slick {
  background: black;
}
.p-top-mv-slick__inner {
  margin: 5% 5% 0 5%;
}

.p-top-mv-slick .slick-track {
  display: block;
  width: 100%;
}

.p-top-mv-slick .slick-slide{
  display: block;
  width: 100%;
  aspect-ratio: 600 / 300;
  margin: 0 5px;
  }

.p-top-mv-slick .slick-slide picture {
  height: inherit;
  height: 100%;
}

.p-top-mv-slick .slick-slide img{
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
```
# 今回行ったこと
slick.jsを使用してスライダーのテンプレートを作成する
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
- [[../02_Web制作/済.md|済]]
- [[../01_よしなに対応/【2−7】カスタマイズ方法をポイント解説（見た目カスタマイズSlick編）.md|【2−7】カスタマイズ方法をポイント解説（見た目カスタマイズSlick編）]]
- [[../99_その他/AAA.md|AAA]]
- [[../99_その他/画像.md|画像]]
