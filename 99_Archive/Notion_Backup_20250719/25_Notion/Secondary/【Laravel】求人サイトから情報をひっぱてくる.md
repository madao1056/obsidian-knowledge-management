---
notion_id: c1afb8fb-fa55-439b-883e-d5babd07522d
account: Secondary
title: 【Laravel】求人サイトから情報をひっぱてくる
url: https://www.notion.so/Laravel-c1afb8fbfa55439b883ed5babd07522d
created_time: 2022-04-07T00:05:00.000Z
last_edited_time: 2022-05-16T02:07:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.492241
---
# 【Laravel】求人サイトから情報をひっぱてくる

<details>
<summary>制作手順</summary>
</details>
  <details>
  <summary>1.要件整理/仕様策定</summary>
  </details>
  <details>
  <summary>技術選定</summary>
  </details>
  <details>
  <summary>設計（ここから実装）08:00〜20:00</summary>
  </details>
  <details>
  <summary>実装　20:00〜</summary>
  </details>
  - 納品
- 一度閉じてからの起動方法(※Dockerインストール)
  1. Dockerを起動
  1. 該当ディレクトリ内でターミナルを開き、
”./vendor/bin/sail up”または
”./vendor/bin/sail up -d”（バックグランド）でDockerのコンテナ起動
  1. “./vendor/bin/sail artisan scrape:mynavi”で実行
- 起動→停止
  1. ”./vendor/bin/sail up”で起動したら→”ctl + C”
”./vendor/bin/sail up -d”で起動したら→”./vendor/bin/sail stop”
  1. 該当ディレクトリ内でターミナルを開き。”./vendor/bin/sail up -d”でDockerのコンテナ起動
  1. “./vendor/bin/sail artisan scrape:mynavi”で実行