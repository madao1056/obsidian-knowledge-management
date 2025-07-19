---
notion_id: 289e6791-ace8-4b38-8429-4ad4d7b3688d
account: Secondary
title: 内部SEO
url: https://www.notion.so/SEO-289e6791ace84b3884294ad4d7b3688d
created_time: 2024-02-06T06:22:00.000Z
last_edited_time: 2024-02-06T06:49:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.402311
---
# 内部SEO

## 説明動画
- h1タグは1ページにつき1つまで
  - TOPページはロゴがh1、下層ページは条件分岐してpタグにする。
そして下層ページの見だしをh1タグに（[参考コード](/9eb7ec8f77d445e9b2ea9b50f7c43e6b#65f6104793e64771a27b5103c325d772)）
- sectionタグには見だしタグ必須
  <details>
  <summary>具体例</summary>
  </details>
- imgタグは遅延処理を行い、widthとheightをつける。（FV、MVのように最初に表示される部分は遅延処理をしない）
  <details>
  <summary>具体例</summary>
  </details>
- alt属性への記載は必須ではない（テキストの重複はさせない）※見出しタグを使用する際はつけるべき
- 見出しタグ以外で画像を囲む親要素はp、div、figure(alt 属性に適切な代替テキストを記述した場合)くらいで十分
- 画像の圧縮はWebp形式が圧縮率いい
- 住所にはaddressタグを使用
  <details>
  <summary>具体例</summary>
  </details>
- 項目に対して説明があるときはdl,dt,ddタグを使用（会社概要とか）
  <details>
  <summary>具体例</summary>
  </details>
- scriptタグはbody終了タグの直前に書くか、遅延処理をしてheadタグ内に記載しましょう！（[参考サイト](https://takayamato.com/defer_async/)）
  <details>
  <summary>具体例</summary>
  </details>
- **W3Cチェックは絶対にクリアしましょう！**
- WordPressの実装でタイムタグを使用する時はW3Cに則った形式で書く
  <details>
  <summary>具体例（詳しくは[こちら](/9eb7ec8f77d445e9b2ea9b50f7c43e6b#8e8f653a4275455d8380b10543ee083c)）</summary>
  </details>
- ファビコン（SEOには直接的な関係はない）
- メタ情報
  <details>
  <summary>メタタグについて</summary>
  </details>

## タグ

#マーケティング #65f6104793e64771a27b5103c325d772)） #8e8f653a4275455d8380b10543ee083c)）</summary> 

## 関連ドキュメント

- [[../01_よしなに対応/グッサポ７大特典.md|グッサポ７大特典]]
- [[../04_ビジネス/営業文（最新） (10_20).md|営業文（最新） (10_20)]]
- [[../02_Web制作/WordPress外部ファイル読み込み.md|WordPress外部ファイル読み込み]]
- [[../99_その他/テキスト.md|テキスト]]
- [[../02_Web制作/chouetteria シュエッテリア様.md|chouetteria シュエッテリア様]]
