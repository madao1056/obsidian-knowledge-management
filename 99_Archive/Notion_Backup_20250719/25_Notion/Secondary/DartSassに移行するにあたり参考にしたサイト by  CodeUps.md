---
notion_id: 480cf07d-3b47-453d-b8a7-9e550ab418f0
account: Secondary
title: DartSassに移行するにあたり参考にしたサイト by  CodeUps
url: https://www.notion.so/DartSass-by-CodeUps-480cf07d3b47453db8a79e550ab418f0
created_time: 2021-12-26T18:42:00.000Z
last_edited_time: 2022-03-28T21:14:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.533863
---
# DartSassに移行するにあたり参考にしたサイト by  CodeUps

## はじめに
いつもCodeUpsをご贔屓いただきありがとうございます！
こちらではDartSassについて参考にしたサイトをまとめています！
多くの記事を参考にしてDartSassへの移行をすることができました。
調べると情報は出てきますが、ほぼ全てが_index.scssに集約して…と書いてあるのですが、その方法を取らずしてなんとか対応出来ています。
作成した時点では同じやり方をしている記事が見当たらず、（現時点では）唯一無二の一番利便性の高いgulpフォルダ構成となっていると思います…もっといいやり方あるかもしれませんが。
改善の必要が出てくれば都度修正を行います。
厚かましいことを言いますが、これらの情報をまとめて形にして提供することは非常に価値があると思います。
これらを調べ理解し実装するということは、CodeUpsを運営している自分自身の実力証明のひとつにもなると思っています。
必要なGulpファイルや調べるにあたり参考にした記事（主に公式ですが）をみなさまに共有しますが、制作者として、フリーランスとして自分から情報を取りに行く姿勢は絶対に見せるようにしましょう！
先程、価値のあるものとお伝えはしましたが、もちろん無償で提供します！
特に見返りは求めませんが、TwtterなどでCodeUpsについて発信していただき、さらなる発展にご助力いただければ嬉しいです！
## 公式サイト
### **gulp-sass****（今回こちらを採用）**
[Bookmark](https://www.npmjs.com/package/gulp-sass)
> To use `gulp-sass`, you must install both `gulp-sass` itself *and* a Sass compiler. `gulp-sass` supports both [**Dart Sass**](http://sass-lang.com/dart-sass) and [**Node Sass**](https://github.com/sass/node-sass), but Node Sass is [**deprecated**](https://sass-lang.com/blog/libsass-is-deprecated). We recommend that you use Dart Sass for new projects, and migrate Node Sass projects to Dart Sass when possible.
※バージョン5以降はDartSass対応との記述ありのためこちらを採用
> `gulp-sass` version 5 requires Node 12 or later, and introduces some breaking changes. Additionally, changes in Node itself mean that we should no longer use Node fibers to speed up asynchronous rendering with Dart Sass.
※Node12以降に対応しているとの記述あり
### **gulp-dart-sass****（不採用）**
[Bookmark](https://www.npmjs.com/package/gulp-dart-sass)
### **gulp-sass-glob-use-forward**
[Bookmark](https://www.npmjs.com/package/gulp-sass-glob-use-forward)
関連：**gulp-dart-sass で glob したい  **[https://qiita.com/taqumo/items/8f726268f4723202e451](https://qiita.com/taqumo/items/8f726268f4723202e451)
※ うまく昨日しなかった
### **@useと@forward**
[Bookmark](https://sass-lang.com/documentation/at-rules/use)
[Bookmark](https://sass-lang.com/documentation/at-rules/forward)
👇上記の内容が日本語でまとめられてる
[Bookmark](https://blog.rhyztech.net/sass_use_and_forward/)
## 調べるにあたり読み漁った個人ブログ
### **Sassで@useと@forwardを使ったサイト設計 - @importから切り替える手順**
[Bookmark](https://yumegori.com/dart-sass-method)
### **Using Gulp with Dart Sass（英語のブログサイト）**
[Bookmark](https://zellwk.com/blog/dart-sass-gulp/)
**以下の考え方を採用してます**
> **Including special paths

**If you’ve downloaded any packages with npm, you can include them in `gulp-sass` so you can write lesser code to import the file. `includePath` takes in an array. Feel free to include any additional paths if you need to!
  ![](https://prod-files-secure.s3.us-west-2.amazonaws.com/d58fe38c-a9d4-4466-aed9-85604b7b2c6d/481469ea-4230-4f66-90c6-fe80ea23b201/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88_2021-11-25_17.06.58.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRT2DHXK%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T060557Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB%2Fw%2FELo4b%2BFdyqmQgJ8G%2FLUr3aGEiqOiRyZrylY%2FE2zAiBFUITo7Q8Cm%2FaFmAejiHBDxu4CXym1Z6jD6jcp%2FEDYxCqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsLgStS1N2hNjwGleKtwDt6rjEyFYzVgZS5niBvgGhBYyP5blQ4fJihAu%2BBUnjYEY3xBW4tH9byhDJNi6QtYeOzxLPMxnHu4ge9kVCDpN4AZ%2FbWjs81Z2ufqE5%2B2CI6TBaM7rPpWE2bM9%2Fcyz2lDDVOhRw4wtnhIrwfeTAywHrTM%2BNwqN1%2FpAuA%2B4aEhnGcCCBUUHM5uB81Vx%2BWlLsjiG%2FpGEK3OMWVbsa7E3RDgOG8ozStomZ6OL2bgFkZtAVYRiFSEZviWqeWokU7TlodWP8MMMABIExCQxj4V2CI1MU4T3h0Ljyo6a3aOOiJMYjJhkuKL5voplhBX2qSY1xfBxxPg6WJf9KVG4Wg08AwRUlC01WZ7xts5O7bhYQB2WRBLAbw%2FNhXcUp002ppvOkm%2B%2FS%2FywYqlkg%2BlwQ39VZVjyk0hP1HXPMaxgywYl98GJxLBvxccJUwUsQBpQ6C%2BGyGLYPTT6tYHbhJW%2FNo%2B3C5p1Hx5bdctZDJgJHH5EnnkmbQoR5mS5AWhCtDV%2BTcME8AcS4erbdj7daYJ5PltmTq26GeMibLjHdiipjlYRaltl7FFl01oSXqv2vJpjQi8tkg%2FQ%2Bt7wZzDh1cvJwNosy0V8CDa84AztxWQ6ZQYNGhfpSHU3y0DfheP%2FNj2Wz88w68XswwY6pgH6%2F03tF6douoGYWEVlZCs2Pu%2F8bRa8VyY%2FW47vcBJqFX7L59OriFK%2BzLy28YjUJfP8qFUVF7t7Glftz7AHFLCtV7WZP0s6RrC7GdBV%2FU5%2F9TTQQdycPon%2FDN8Zm7764V%2B1Dq4wK8MdJPtDfNIWDE3pLLCFmSVpIje%2FAXbVlLdQ5qkEU24Yfa07ukuBQEhc5mTwVmoKlG8z2WLozG1pzTzLQflkDWKD&X-Amz-Signature=41e19437aa775f276adb7baf5b5589eaeda95cf72f1be6eba0e5e95605a94c5e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
### **Dart Sass（@use）の基本的な書き方と@importから乗り換える方法**
[Bookmark](https://haniwaman.com/dart-sass/)
## 備考
### gulp-sourcemaps（今回からSourceMapsいれてます）
[Bookmark](https://www.npmjs.com/package/gulp-sourcemaps)
### たまたま考え方がほぼ一致した記事
[Bookmark](https://notes.sharesl.net/articles/2423/)
### 以下の記事たちはLibSassからDartSassに移行する際に参考にしました！
[Bookmark](https://sass-lang.com/documentation/cli/migrator)
[Bookmark](https://sass-lang.com/documentation/breaking-changes/slash-div)
[Bookmark](https://cumak.net/blog/dart-sass/)
[Bookmark](https://suzunon.com/web-develop/css/from-import-to-use-in-sass/)
[Bookmark](https://mykii.blog/sass-migrator/)
## 最後に
すでに出来ている環境をお渡ししていますが、常に勉強し常に対応していかなければいけません。今のこれらの知識も1年後には時代遅れになっている可能性も高いです！
日々、自分の知識を増やしていきましょう！
**これからもCodeUpsをよろしくおねがいします。**