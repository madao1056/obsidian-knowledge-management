---
notion_id: 95a4d324-0d56-4a3a-86a3-c77b79b93f43
account: Main
title: カバー様 (holizontal)管理シート
url: https://www.notion.so/holizontal-95a4d3240d564a3a86a3c77b79b93f43
created_time: 2023-07-12T01:50:00.000Z
last_edited_time: 2023-08-28T06:58:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:15.093329
---
# カバー様 (holizontal)管理シート

※「▶︎」をクリックすると**トグルが開きます**
<details>
<summary>目次</summary>
</details>
# 基本情報
---
---
# 進捗管理
---
# 確認事項
---
## 未対応事項メモ
持ってるボールがあれば追加
---
# 品質管理
- [x] ❗️品質管理時は共有を**編集可**にすること
## 端末ブラウザチェック
## ご報告一覧（詳細は各項目を開いてご確認ください）
- **コンソールエラー**
  - [ ] 検証ツールで確認（YouTubeAPIが絡む部分でエラーあり）
- **表示崩れ**
  - [x] インナー幅以上(1920px)
  - [x] ブレイクポイント+1px
  - [x] ブレイクポイント-1px
  - [x] 375px
  - [x] 320px
- **フォントの反映**
  - [x] 「WhatFont（Chromeのプラグイン）」で確認
- **画像について**
  - [x] 画像最適化（最適な形式で書き出されているかどうか）
写真などはwebp、jpg、png、ロゴなどベクター画像にすべきものはsvg
  - [x] FV、MV以外に遅延処理を行なっているか
  - [x] Retinaディスプレイ対応のため画像は2倍書き出し→圧縮して表示
  - [x] alt確認
  - [x] 不要な画像の削除
- **スクリプトタグ**
  - [x] 最初の表示に関係のないスクリプトタグについて遅延処理を行なっているか
- **アニメーション**
  - [x] 動きが指示通りになっている
  - [x] 不自然な動きがない
  - [x] ホバー時のカーソルはポインター
  - [x] リンクチェック
- **metaタグ**
  - [x] OGPタグ
  - [x] faviconの有無
- **閉じタグチェック**
  - [x] 「HTMLエラーチェッカー（Chromeのプラグイン）」で確認
- **HTML・CSSの文法**
  - [ ] HTML（以下のエラー表示のみ）
  - YouTubeIDを属性としていることにエラー表示となるが、参考サイトでも同じエラー表示が出るため、そのままにしています（TOPページ,MOVIEページ）
  - [x] CSS
修正ファイル
- WP管理画面：ABOUT（固定ページ）カスタムHTML
- header.php
- page-about.php
- js/script.js
- css/styles.css
- css/styles.css.map
- images/top/kv_about.webp
- images/top/kv_about_hover.webp

## タグ

#Web制作 

## 関連ドキュメント

- [[../02_Web制作/カバー様 (holizontal).md|カバー様 (holizontal)]]
- [[../01_よしなに対応/確認事項.md|確認事項]]
- [[../02_Web制作/参考サイト.md|参考サイト]]
- [[../02_Web制作/基本情報.md|基本情報]]
- [[../02_Web制作/header.php.md|header.php]]
