---
notion_id: 7a8d33f3-e1cf-4d10-80e1-27840e1c45fa
account: Secondary
title: gulp
url: https://www.notion.so/gulp-7a8d33f3e1cf4d1080e127840e1c45fa
created_time: 2022-08-21T23:54:00.000Z
last_edited_time: 2022-08-22T01:57:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.475079
---
# gulp

- 目次
# gulpを使用する環境作り
  1. Node.jsのインストール
  1. npm が使用可能になる
  1. gulp をnpm でインストール可能になる
  1. 詳細はこのサイトへ
# ファイルを人に渡すときの注意点
  ”npm i”コマンドでパッ毛字をインストールするときに生成される”node_modules”フォルダと”pakage-lock.json”は渡さないこと
  特に”node_modules”フォルダはクソ重たい・・・
# 作り方
  元ファイルはこちら
  1. gulpfile.jsをsrcフォルダと同じ階層に作成
  1. ターミナルを開き、”npm init -y”を入力すると”package.json”ファイルが生成される
  1. ターミナルで”npm i gulp”を入力しnpmを使ってgulpをインストールすると”node_modules”フォルダと”package-lock.json”ファイルが生成される。
これで人に渡す時に余分なファイル（”node_modules”フォルダと”package-lock.json”ファイル）を渡さなくても相手側で”npm i”と入力すれば同じ環境が作れる。
  # 機能の追加方法

## タグ

#その他 

## 関連ドキュメント

- [[../99_その他/y.md|y]]
- [[../02_Web制作/Gulp環境でメディアクエリをまとめて生成したcssファイルを作成する.md|Gulp環境でメディアクエリをまとめて生成したcssファイルを作成する]]
- [[../02_Web制作/VScodeユーザースニペット集.md|VScodeユーザースニペット集]]
- [[../02_Web制作/【CodeupsのWordPress化　gulpの切り替え方法】.md|【CodeupsのWordPress化　gulpの切り替え方法】]]
- [[../07_プロジェクト/納品前チェックシート.md|納品前チェックシート]]
