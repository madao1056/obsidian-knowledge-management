---
notion_id: fffd0c30-9401-81e9-a54d-d7b9ff909b4b
account: Secondary
title: 既存テーマ（SWELL）でcssファイルが読み込まれない
url: https://www.notion.so/SWELL-css-fffd0c30940181e9a54dd7b9ff909b4b
created_time: 2024-09-20T01:11:00.000Z
last_edited_time: 2024-09-20T01:11:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.384545
---
# 既存テーマ（SWELL）でcssファイルが読み込まれない

# 概要
- SWELLで作成されたものに下層ページを1ページ追加
- cssファイルが読み込まれない
# 解決のヒント
- functions.phpの読み込みコード（子テーマの読み込みは使う関数が違う）
- WPのheader.footerを読み込む記述をしているか？
- SCSSを使う場合、コンパイルをしているか？
- 検証ツールを使って、一つ一つ解決してく