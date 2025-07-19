---
notion_id: 54340b0d-08c5-4345-be88-828a611ca552
account: Secondary
title: meta タグ
url: https://www.notion.so/meta-54340b0d08c54345be88828a611ca552
created_time: 2022-03-06T05:06:00.000Z
last_edited_time: 2022-03-06T05:17:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.538571
---
# meta タグ

**headタグの中のmeta系の情報は指定されることも多い
キーワードやタイトルやDescriptionなど情報頂いてページそれぞれに設定することは必須
案件毎で内容が変わってくるけど毎回一旦これをhead内コピペして毎度設定**
```html
<head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# website: http://ogp.me/ns/website#">
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1.0" />
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <meta name="format-detection" content="telephone=no">
  <title>タイトルが入るよ★</title>
  <!-- SEO系 -->
  <meta name="description" content="120文字以内！">
  <meta name="keywords" content="これは今はGoogleでは特に必要ないと言われてますがキーワードお願いされることも多々ある" />
  <!-- OGP -->
  <meta property="og:title" content="このページのタイトル/ページごとのタイトルにするお">
  <meta property="og:site_name" content="サイト名">
  <meta property="og:description" content="90文字くらい推奨">
  <meta property="og:type" content="TOPページはwebsite、子ページはarticle">
  <meta property="og:url" content="このページのURL">
  <meta property="og:image" content="1200×630以上推奨、絶対パス!!">
  <meta name="twitter:card" content="summary or summary_large_image">
  <meta name="twitter:site" content="@ユーザー名">
  <meta name="format-detection" content="telephone=no">
  <!-- タッチアイコン -->
  <link rel="apple-touch-icon" sizes="192x192" href="">
  <link rel="shortcut icon" sizes="192x192" href="">
 <!-- ファビコン -->
  <link rel="icon" href="" />  
 <!-- クローラー -->
  <meta name="robots" content="noindex">
</head>
```