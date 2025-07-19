---
notion_id: 517f4d8f-cf83-4764-99cd-1f7c6a2f2702
account: Secondary
title: Shopify Theme Kit（Theme Accessアプリ使用）
url: https://www.notion.so/Shopify-Theme-Kit-Theme-Access-517f4d8fcf83476499cd1f7c6a2f2702
created_time: 2022-11-20T03:46:00.000Z
last_edited_time: 2022-11-20T05:44:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.468794
---
# Shopify Theme Kit（Theme Accessアプリ使用）

- 参考URL
  [Bookmark](https://arutega.jp/shopify_env/)
## **Theme Kitのインストール**
1. Shopifyパートナーへの登録
1. ターミナルアプリを起動させ、以下のコマンドをコピペして実行すればインストール
  ```plain text
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
  ```
1. 以下のコマンドラインでTheme Kitのインストールが開始
  ```plain text
1: brew tap shopify/shopify
2: brew install themekit
  ```
  ※パスワードが求められるので、パスワードを入力
1. 以下の画面が表示されるので、もう一度エンターを押すとインストールが開始されます。「Installtion successful!」と表示されれば、インストールが成功しています。
  ![](https://prod-files-secure.s3.us-west-2.amazonaws.com/d58fe38c-a9d4-4466-aed9-85604b7b2c6d/bb4c3c92-d638-416b-9bc5-b5ab15015c9a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLZA36OW%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T060954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB0V3CoKKrdK3uXEooPD%2FSpj8ExXQaLsF7Ntcx1%2FHrleAiEA3z%2FGcrlxqugtr9HVft4AK65PxUgY%2FN%2BFmxFJV7uP1WYqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOSB7IJR%2FELrht%2FRSCrcA6JyMDbSf%2B%2Fuza8ha9Zq89pl62sUD%2BotAa9Sm9Dk1RU7qaHl1ysoowPm7ySjhrzAYVdjfrynJKyCDotuZaW5DuRGPoPRoxPKN%2B35X7HLbXyAGdvWeysfJ2vlVFuO%2FhBNYCuYa5XIEdNiB1LRMa5rWRr9No27BXGj0uLnxgU5OCNrUZw%2FUr65KakhHRvOzIOCmhuZL7vEP7YBjgp4MdgodOI8Ijzk4CeKF70G8QcJ97XUl1vumD3XRZpUcYtLhPoN%2B2LKdX%2F2ktinj%2BRbvJKVtnDtM8qU%2Bz1k8OsEt7A5jktZ2MMwHqXQKMS6DIujOa6MpXC3Iwe6mVoXMnqqRjkgKJ%2BXktKV3tZHmGcAleR104sJTSCC7lDslDnEB0W28TK4W9PhszLY2styv2ZBwrmjZV8F%2BU%2BPr5vv0T08H8peOr5MrJvw3rZIs6JCIKqFiNRALeKBxPaIJe33CaTkSpw6Omk4zFYfEhti%2Bglyj0Xh0PyvfkzxKZhcwPQWdrVI2I60zRo67mkxji%2BMVWA%2BDGUZUAjI6JOmLy0y6U7eoJCY9PA748yLtmJkLeDP43%2BGRdZ5PA4xzHFicmijd3K4XP5afx4Z7TS9EMtVUrpWQJ9l7K%2BMyFMIBQpvgH9ht2m2MKbF7MMGOqUBjQMQlwHKoolC%2Bwajqb33gFVvmjMqQNAHUL2BNROfu9AzEx%2FqMnWQV3CaZK4t9WdJxi6L1EomgS37GgxgiodjXfHuCiE3VWul%2BxelcyBwkbyFG29eX%2BmdDZ7Cldx%2BbAFYTA9%2Fd6bYlLYF8zxeOqWG4q72b%2FDH8fk1yEMOvCRq4Z4GMaSy%2F1mS3wjKC5A67JrHOViI5%2FOMOe9X%2FzEhu8%2FxJl4oK3p8&X-Amz-Signature=0dc0ba9f1956490e600c3c88aafc59e83fc74822d580f01ee1956b23171a2df3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
1. インストールされているかの確認は、以下のコマンドでチェック。以下のコマンド一覧が表示されます。
  ```plain text
theme --help
  ```
  ![](https://prod-files-secure.s3.us-west-2.amazonaws.com/d58fe38c-a9d4-4466-aed9-85604b7b2c6d/20709963-a5b0-478c-84d1-01669f7d0941/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S4OJMXSD%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T060955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHzvS1l7EmCUMEfbZ8GsvxTsyy%2B61q%2FHOMySDiKyaXc8AiEA8L9YvMNAvHUHqLYQginnKvaj1IK62sPdHOPOqX1FXGQqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIBRZfP9KkgfO6rdCircA05fIIN%2BLswzN6jvWbvTTmPSsytST71r4DMtfllmQO9%2FOrES5Wv7m2IEOlu0UxaTPgK8Tli%2Frolgqse29jBSJwH%2BFe6mN2Hnctm43aA%2B7fM0yl1inbLEZEHDAoAq0L21sYiVu1Ss03szN1ItMDSvneAuhva91sAoEMwedHwT8C9WqesodJeb2%2FUCHXPXAoqQIv4Rlgix5WVxcWzpMG0y6M4pvrJfvBrvXnDeoA%2BGPt9deDfImmyfAkKUDZR896oPkfD7twxhS8oX%2BpTLx3%2FjZAtbv42rIl1dE4TxWoR1ebG%2BV1zucX8rA8uxvyeNf2kVNsgQBKDsvkkfm41hPL2H34lqZ2E%2FrjVKrhGexmhqWFHlr9X7iMQbcnX%2F8uy4Tp2v1ydRljJ%2F5FD%2F94VE1MPcguHqwlNGZa5jnh2XiFG4VkIcHLGpQbeMgi%2FOfdvFgGMLfLI7P1rEw235pDfDDfuhgSeXz7037b57YnrMV09BtTK67GRYetPEdqJhfrSII6MMgiSx5Z1D%2F8Yg0FOIoru7Gt7J3YHo6FyGZVbzdVGxWI%2B%2FeeZbazz%2FCn6OUv3NZRINNMGcQkNX%2BMBlthg4bLA18asBEaL244yo%2FrQtsgY1OZNv%2Bh6nsGY8C6Dfr7j4MO7F7MMGOqUBKVHE05NK1Crf4ba7u%2FFBB0%2FqVLwFc7vZO6QQxTLpY3HshiC61Lj1gpJ6sYZ9N075dppzk7%2BI7JcomCPzPbQsAWXLlaJnq2n6KJNGx63%2FwI3lQZ9BjVRWD3KDvlt%2Bm2a7OopvE%2FNZ%2F89RLxe3IphgryGXE4e56ETH0EuXVw5d9bsJE1bKfzySJGcj3CLwqIMbuOBdHIx3DLgpun0jlt7PuxoTt7MK&X-Amz-Signature=01d844e91fd24f477cbf5a5f49ec894342fbc71080e76b850ef36d2ba6e309bd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
## **APIキーの発効**
以前のやり方ではできなくなっている（プライベートアプリの開発はもうできない）
[Bookmark](https://apps.shopify.com/theme-access?locale=ja&st_source=autocomplete)
1. アプリストアから「Theme Access」をインストール
  1. パスワードを作成
  1. 必要事項を入力し、右下の「パスワードを作成」をクリック
  1. 登録したメールアドレスにパスワードが届くのでコピーしてメモ
※一度した表示されないようなので確実に残しておくこと
1. 公式の方法を参考にターミナルを操作
  [Bookmark](https://shopify.dev/themes/tools/theme-kit/getting-started#step-3-connect-to-an-existing-theme)
  ※パラメーターに URL プロトコル (HTTP または HTTPS) を含めない
  ```plain text
theme get --list --password=[your-password] --store="[your-store.myshopify.com]"
  ```
1. 出てきたtheme-id（Available theme versions）をメモ
  ![](https://prod-files-secure.s3.us-west-2.amazonaws.com/d58fe38c-a9d4-4466-aed9-85604b7b2c6d/f552dad7-613c-43dc-bfc0-2b3bfe7d34c9/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88_2022-11-20_14.37.17.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YD73JVD%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T060956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6bAEfhTAP%2FThbauzsUiTv5TfJjiuTa8Xh%2BN4%2F4%2FFSaAIgQmV6yNhrOKSvjMEZNo%2BSEanu8GEdktBQmx5PCePQPewqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDINrqM0WH%2FVxQGY69CrcA1U4PH8nDlCo0t%2Babp6fNx1uIT1WP7EI2ewsoB88CN%2FNx3gP9nYpruH4cf2O8p5NYvtUCVAf7IiJodXZHCQT%2FCV3MFkP%2BjyrHo%2FpUeMSMlq5yGigiSRPTPStJdGhyl%2FskJjIarKx3aCUwM7Nq7jAjGWv%2FG8MXR4eTJMkPfGm1uqBn4d3PaK9yhQIIMnKYBzDEVQMGxmElBNGX3jTqxZblit%2BWx34wThw0NemLJ2BkticByq4H3POo5JolJowmtTSscE0MAeAv2g4qSdqUbwgkXg78c%2FxCOtCmA4uASinkyqwreywJjiJE5fS6dLgzBJ3nz84qD0rteossZBgwHf7gb%2FxU38BbFYdhLYDrfaS7Vi9KJPssocXJadhF8kS9Ox4AK1i2ToyPzr1u4uEpzzkGL817ORl1aFNh07PZyOvVG8oppV%2F21fXS4hSyVi2ZsZjNsmWJKXiSJn2NfRhhO2wHFVbOPwBDZSBsl%2BtAHhyRHjp%2F1hpo2PDy8bHpZ%2BdCqoFitM1M9ZGfWyXuf4SUcPRPjTDza0qaOJCyLENcRe9MhtQ2%2BjzfhfuEtl8FGrrz1jlQEegk8MeHYgseuu7ILrpLFkxupHGnDbHYBx0rMOmDOd30Vd9GYeKdhWlotdTMODF7MMGOqUBV0c8%2BEL2rc0R72A4tOc8R5bVu05%2FsSYpjyUcu4yZmue9lEHRQ9Jo3vuYXt6YRZRQnSmXhwd2Xp7zOPad%2BdHRZAAakinlw6XUXgNtSNkp8blujAjZ3CAxwj0i%2BXNz6BP2Mkt2e6WbBuKTDbk3uaXVOGSRmY73BlbUxGqlpso4zF%2FnR%2FEblWLAUgErgaTR4YEqEJnmIu83MQvw4CF%2BKOInXuY1%2FbZ%2B&X-Amz-Signature=e7fe63bf8c42c5a11b63731b7863a21b1f62d9efbfd52760b18c33ec57f6a606&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
1. 任意のディレクトリに移動して以下のコマンドを実行すればローカルにダウンロードされる
  ```plain text
theme get --password=[your-password] --store="[your-store.myshopify.com]" --themeid=[your-theme-id]
  ```

## タグ

#その他 #step-3-connect-to-an-existing-theme) 

## 関連ドキュメント

- [[../99_その他/Untitled.md|Untitled]]
- [[../99_その他/shopify.md|shopify]]
- [[../99_その他/x.md|x]]
- [[../99_その他/y.md|y]]
- [[../99_その他/メモ.md|メモ]]
