---
notion_id: 82c9c014-295d-4527-9908-80cb48338a5c
account: Main
title: 誤動作？Shopifyパートナーの切り替え時にCLIが過去のデータを引っ張ってくる
url: https://www.notion.so/Shopify-CLI-82c9c014295d4527990880cb48338a5c
created_time: 2023-12-19T14:01:00.000Z
last_edited_time: 2023-12-19T14:08:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:15.067490
---
# 誤動作？Shopifyパートナーの切り替え時にCLIが過去のデータを引っ張ってくる

# 経緯
以前、自分のアカウントでコラボレーターとして構築して、今回パートナーとして、[https://partners.shopify.com/](https://partners.shopify.com/)のアカウントを先方のもので構築しようとした時に誤動作発生。
テーマをCLIでpullしようとした時に、旋回構築していたファイルをなぜか持ってきてしまう
パートナーアカウントで入っているはずなのにCLIに反映されない。
# 解決
1. まず、shopify auth logoutをターイナルで打ってログアウトする
1. [https://partners.shopify.com/](https://partners.shopify.com/)のパートナーとしてログインした状態の画面を開いたまま、
CLIで
  ```plain text
shopify theme dev --store ドメイン.myshopify.com
  ```
  とコマンドを打ってば、無事に入れ替えが成功した。