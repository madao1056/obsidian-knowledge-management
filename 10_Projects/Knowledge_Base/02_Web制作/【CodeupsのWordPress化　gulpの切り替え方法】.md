---
notion_id: a3083cf3-0503-4ceb-bec5-89e780a74842
account: Secondary
title: 【CodeupsのWordPress化　gulpの切り替え方法】
url: https://www.notion.so/Codeups-WordPress-gulp-a3083cf305034cebbec589e780a74842
created_time: 2022-03-17T06:12:00.000Z
last_edited_time: 2022-03-17T06:12:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.535657
---
# 【CodeupsのWordPress化　gulpの切り替え方法】

【CodeupsのWordPress化　gulpの切り替え方法】

gulpをDartsassからwp-flocss-rem-fromSPに切り替えるのにめちゃくちゃ手間取ったので、
これから始める方のためにやり方を共有します！

※macのM1を使っている人向けの説明です！intelはやり方違うかもしれません。

【Youtubeのライブコーディングについて】
ライブコーディングは、最新のDartsassではなく、
wp-flocss-rem-fromSPを使っていました。

ライブコーディングと同じ環境でWordPress化を進めたい方は、
Dartsassからwp-flocss-rem-fromSPへ切り替える必要があります。
（もちろんDartSassのままWordPress化をしていくのもアリです。
本来はそっちが正しいのかも）


【つまづいた点】
この2点です。
1. gulp v14系がインストール出来ない
2. gulp14系をインストールしたらDartsassのgulpが動かなくなった

僕は丸1日ググってましたが、
これを見て、後に続く方の作業時間が10分に短縮されるのを切に願います。

忘れないうちに一気に書いたので、結論はまとめていません。

詰まった箇所から解決までを順番に書いているので、
上から順に見ていけば、解決出来るようになっています！

ここから↓

・Githubでwp-flocss-rem-fromSPをダウンロード
[https://github.com/webonds2081/wp-flocss-rem-fromSP](https://github.com/webonds2081/wp-flocss-rem-fromSP)
これはライブコーディング#1-0で説明してるファイルです。

・npm i⇨npx gulpで起動を試すも動かない。
ここまでは予想通り。node.jsのバージョンv16系になっているから。

・ここから詰まる。
[https://www.notion.so/Mac-gulp-3d0ab7cf7cb54ed4a3d62795fd5c3fea](/3d0ab7cf7cb54ed4a3d62795fd5c3fea)
このマニュアルに沿ってv16をアンインストールしようと思っても出来ない。
-bash: nodebrew: command not foundとエラーが表示される。

・理由がわからなかったので、このマニュアルを初めからやり直すことにする。
[https://tips-web.net/gulp4-mac/](https://tips-web.net/gulp4-mac/)

・一番初めのHomebrewのバージョンを確認したら、
-bash: nodebrew: command not foundとエラーが表示される。
なぜ？先月インストールしたはずなのに。

・再インストールしようと公式HPからコードをコピペして実行。
-bash: nodebrew: command not found
なぜ？

・ここでテンパってしまい、すっかり忘れていたのが、
M1はこっちのマニュアルだった。
[https://qiita.com/ren_nomura/items/2b0c30501792477bb594](https://qiita.com/ren_nomura/items/2b0c30501792477bb594)

・Homebrewのインストール完了

・v16のアンインストールはこのマニュアル
[https://www.notion.so/Mac-gulp-3d0ab7cf7cb54ed4a3d62795fd5c3fea](/3d0ab7cf7cb54ed4a3d62795fd5c3fea)
ようやくアンインストールが出来た。


・v14のインストールはこのマニュアル
[https://kamoqq.info/post/how-to-install-nodejs14-on-apple-silicon-mac-with-nodebrew/](https://kamoqq.info/post/how-to-install-nodejs14-on-apple-silicon-mac-with-nodebrew/)
@あおはるさんに教えて頂きました。ありがとうございます。

・#1-1ライブコーディング
27分ごろから見る。　Themeフォルダ内にwp-flocss-rem-fromSPを入れる。

・41:00 名前を変えるところはやらなくて良いっぽい。動画#1-0を代わりにみる。

・ここでnpm i→npx gulpを入力したら「Sassをコンパイルしました」と表示されたので、
成功か？と思ったがchromeでウインドウが立ち上がらない。DartSassのは立ち上がるのに。なぜ？
⇨これで問題なし。

2つのgulpファイルで以下の違いがあるみたい。
　DartSass 　chromeのウインドウが自動で立ち上がって、vs codeの変更箇所は自動で更新される
   wp-flocss-rem-fromSP 　chromeのウインドウは自動で立ち上がらない。vs codeの変更箇所はchromeで開いているWordPressのページをリロードすると更新される

ここまででwp-flocss-rem-fromSPは使えるようになった。


次の問題
【DartSassのgulpが立ち上がらない】

・nodeをv14にしたためにDartsassが使えなくなった。

・nodeのバージョンを切り替えられるようにしたい。

・今インストールされているバージョンを確認する。
nodebrew lsをターミナルに入力
-bash: nodebrew: command not foundが表示される
なぜ？

・またHomebrewが消えていた！再度Homebrewをインストール

・nodeのv16をインストール
ターミナルにnodebrew install-binary v16.14.0を入力

・nodebrew lsをターミナルに入力すると
v14.18.1
v16.14.0

current: v14.18.1
と表示されるはず。現在はv14.18.1を使っている状態。

・ターミナルにnodebrew use v16.14.0を入力

nodebrew lsをターミナルに入力すると
v14.18.1
v16.14.0

current: v16.14.0
と表示されるはず。

・これでDartsassのgulpも立ち上がります！！！

・wp-flocss-rem-fromSPを使いたい時は、
ターミナルにnodebrew use v14.18.1を入力すれば切り替えられます！

以上です。いやーここまで長かった。。

## タグ

#Web制作 #1-0を代わりにみる。 #1-1ライブコーディング #1-0で説明してるファイルです。 

## 関連ドキュメント

- [[../02_Web制作/同じブラウザでもアカウントが違うだけでWordPressのjQueryが読み込まれなくなる事象！？.md|同じブラウザでもアカウントが違うだけでWordPressのjQueryが読み込まれなくなる事象！？]]
- [[../02_Web制作/Trym.md|Trym]]
- [[../01_よしなに対応/yukariさん.md|yukariさん]]
- [[../99_その他/x.md|x]]
- [[../01_よしなに対応/オリジナル営業文.md|オリジナル営業文]]
