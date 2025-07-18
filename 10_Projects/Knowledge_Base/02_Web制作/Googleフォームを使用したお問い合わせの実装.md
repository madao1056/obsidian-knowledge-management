---
notion_id: 895c6bd8-9180-4243-9276-cb80658a9570
account: Secondary
title: Googleフォームを使用したお問い合わせの実装
url: https://www.notion.so/Google-895c6bd8918042439276cb80658a9570
created_time: 2022-06-12T23:53:00.000Z
last_edited_time: 2022-06-18T10:54:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.489265
---
# Googleフォームを使用したお問い合わせの実装

# 実装内容
- [Googleフォームと自作のお問い合わせフォームを紐付け](/895c6bd8918042439276cb80658a9570#945d075d7f0241949a4f3a789bf149d7)
- フォームは複数（４つ）作成　※デザインはコーディング済み
- [各管理アドレスに自動通知メールを送る](/895c6bd8918042439276cb80658a9570#f70afe8fc25242e69d03a39d7a90a850)
- [自動返信メール（送信元は各管理アドレス）](/895c6bd8918042439276cb80658a9570#f46b8c63d48a490cbe92f6680968e86c)
- [送信完了後、トップページに飛ばす](/895c6bd8918042439276cb80658a9570#352254b1c1c248cf99353a2c62ced169)
---
# 必要なもの
- マスターアカウント１つ（マスアカ）
- 管理用アカウント（管理アカ）
- 自作のフォーム（HTML/CSS）
---
# 手順
## Googleフォームと自作のお問い合わせフォームを紐付け
1. マスアカにてオリ自作の問い合わせ項目と同じ項目をGoogleフォームで作成
1. Googleフォームで作成したフォームから必要なコードを取得（検証ツールにて「Command＋F」で検索）
  1. Googleフォームの<form action=”https://docs.google.com/forms/〜formResponse”のURL部分をコピー
  1. 自作のフォームの「form」タグに同じようにペースト
  1. Googleフォームの各項目に割り振られているname="entry.123456789”の赤文字部分をコピー
ポイント：各項目に任意のテキストを入れて検証ツールのコード内で任意のテキストを検索をすると見つけやすい
  1. 自作のフォームのname属性にペースト
  <details>
  <summary>参考スクショ</summary>
  </details>
1. コピペが終わったら実際に入力してみてGoogleフォームの送信完了画面に行ったら成功
---
## 各管理アドレスに自動通知メールを送る
- ちなみに
  自動通知メールは**Googleフォームの標準機能を使う方法**もあるが、マスアカにしか通知が来ない。
Google以外のアドレスや複数宛先にメール通知を設定したいときは、Google Apps Script（GAS）を使用する。
- マスアカに通知メールを送る（標準機能）
  <details>
  <summary>メールスクショ（設定が正常に行われて、回答がきた場合、こんなのが送られてくる）</summary>
  </details>
  1. 「回答」→「3点リーダー」→「新しい回答についてのメール通知を受け取る」をクリック→✅がつけばOK
  1. 確認時は少しタイムラグがある（回答して30秒後くらい）
- Google以外のアドレスや複数宛先にメール通知を設定する
  <details>
  <summary>メールスクショ（設定が正常に行われて、回答がきた場合、こんなのが送られてくる）</summary>
  </details>
  1. スクリプトエディタを開く
  1. ファイル名を変更（任意）→以下のコードをコピペ→保存する
  1. トリガーの設定
---
## 自動返信メール（送信元は各管理アドレス）
- 試したこと（NG集）
  1. **Google フォームの画面から設定する手順｜回答を自動返信する(**[**参考リンク**](https://blog.hubspot.jp/google-forms-automatic-reply)**)**
  1. **Google フォームの拡張機能（アドオン）を追加する**
  1. **Google フォームのスプレッドシートを使った自動返信（GAS使用）(**[**参考リンク**](https://blog.hubspot.jp/google-forms-automatic-reply)**)**
- 自動返信メールの設定（自作部分あり）
  ```plain text
考え方
1. 「各管理アドレスに自動通知メールを送る」と同様にフォーム自体のGASに書けば良い。
2. 回答者が記載したメールアドレスを取得 → そのメールを返信メールに設定。
3. 管理者のメールから送られるように設定を追加する。（マスアカと管理アカを紐づける必要あり）
  ```
  1. スクリプトエディタに新しくコードファイルを作成し自作コードをコピペ（[スクリプトエディタを開く](/895c6bd8918042439276cb80658a9570#3016a462a5cd437687396bb243ff2f81)を参考）
  1. トリガー設定へ（[トリガーの設定](/895c6bd8918042439276cb80658a9570#2427b5c0199543e6a0d76b549fe92df2)を参考）※関数名を変更することを忘れずに
  1. 追加されていれば完了
  1. 管理者のメールから送られるように設定を追加
  1. 送信完了後、トップページに飛ばす
  

## タグ

#Web制作 #f70afe8fc25242e69d03a39d7a90a850) #f46b8c63d48a490cbe92f6680968e86c) #2427b5c0199543e6a0d76b549fe92df2)を参考）※関数名を変更することを忘れずに #945d075d7f0241949a4f3a789bf149d7) #352254b1c1c248cf99353a2c62ced169) #3016a462a5cd437687396bb243ff2f81)を参考） 

## 関連ドキュメント

- [[../02_Web制作/ぐっさん@田舎のプログラミング初心者.md|ぐっさん@田舎のプログラミング初心者]]
- [[../01_よしなに対応/グルコン.md|グルコン]]
- [[../99_その他/お問い合わせ.md|お問い合わせ]]
- [[../01_よしなに対応/よしなにイフゼン.md|よしなにイフゼン]]
- [[../02_Web制作/Trym.md|Trym]]
