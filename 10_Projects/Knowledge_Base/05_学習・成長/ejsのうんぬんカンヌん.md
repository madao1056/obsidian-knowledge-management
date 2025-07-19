---
notion_id: 4bb1b286-752e-44a5-8934-47a7cc581557
account: Secondary
title: ejsのうんぬんカンヌん
url: https://www.notion.so/ejs-4bb1b286752e44a5893447a7cc581557
created_time: 2022-04-01T00:14:00.000Z
last_edited_time: 2022-04-01T01:11:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.533304
---
# ejsのうんぬんカンヌん

- 参考記事
  [Bookmark](https://uetani33.net/ejs-howto/)
<details>
<summary>メリット</summary>
</details>
  - htmlをパーツ化してヘッダーやフッターなどを別ファイルに作れる
  - 変数を設定して、それを反映したhtmlが生成できる
  - html内でループ処理を書いて楽に記述できる
<details>
<summary>他のテンプレートエンジンと比較（pugやslim、Middlemanなどがある）</summary>
</details>
  - htmlの記述の中に、<%= ejs %>のように記述して書くので簡単（phpと同じ感じ）
  - 文法がjavascriptなのでejsの学習コストが少ない
  - 学習コストが少ない分、他のテンプレートエンジンに比べて機能が少ない
<details>
<summary>使い方</summary>
</details>
  - <% %>：Javascriptの変数の宣言やifやforなどのjavascriptの記述をします。
  - <%= %>：囲われた中にあるejsの変数の出力を行います（エスケープする）
  - <%- %>：囲われた中にあるejsの変数の出力を行います（エスケープしない）
<details>
<summary>使い方（具体例）</summary>
</details>
  <details>
  <summary>変数を宣言</summary>
  </details>
  <details>
  <summary>文字を代入</summary>
  </details>
  <details>
  <summary>if文（条件分岐</summary>
  </details>
  <details>
  <summary>for文（繰り返し処理）</summary>
  </details>
  <details>
  <summary>コメントアウト（ejs内）</summary>
  </details>
  <details>
  <summary>パーツのインクルード</summary>
  </details>
<details>
<summary>ejsのテンプレートのサンプル</summary>
</details>
  ejsの階層が変わった時は、pathの変数を変更すればOK　↓index.ejsファイル
  ```html
<%# baseMetaにページの基本情報を。 %>
<%
const baseMeta = {
  ttl: 'ページタイトル',
  desc: 'ディスクリプション',
  url: 'test.html',
  path: './'
};
%>

<%#
インクルード時に、baseMetaに最初に定義したbaseMetaを渡す。
するとインクルード先で、baseMeta.ttlという風にして使用できる。
%>
<%- include(baseMeta.path + 'parts/_head', {baseMeta: baseMeta}) %>
<%- include(baseMeta.path + 'parts/_header', {baseMeta: baseMeta}) %>

<!-- ここにメインの記述 -->

<%- include(baseMeta.path + 'parts/_footer', {baseMeta: baseMeta}) %>
<%- include(baseMeta.path + 'parts/_footerHead', {baseMeta: baseMeta}) %>
  ```
  インクルード先の例　↓_head.ejs内
  ```html
<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="UTF-8">
    <title><%= baseMeta.ttl %></title>
    <meta name="description" content="<%= baseMeta.desc %>">
    <link rel="stylesheet" href="<%= baseMeta.path %>/css/index.css">
  </head>
  <body>
  ```