---
notion_id: 3aefd5fb-06bb-4105-8760-f20fa1843bc8
account: Secondary
title: PC・スマホ・タブレットの分岐
url: https://www.notion.so/PC-3aefd5fb06bb41058760f20fa1843bc8
created_time: 2022-05-08T23:54:00.000Z
last_edited_time: 2022-05-08T23:54:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.503886
---
# PC・スマホ・タブレットの分岐

## **「スマホ・タブレット」と「PC」の条件分岐**
```javascript
if (navigator.userAgent.match(/(iPhone|iPad|iPod|Android)/i)) {
  // スマホ・タブレット（iOS・Android）の場合の処理を記述
} else {
  // PCの場合の処理を記述
}
```
## **「スマホ」と「PC・タブレット」の条件分岐**
```javascript
if (navigator.userAgent.match(/(iPhone|iPod|Android.*Mobile)/i)) {
  // スマホ（iPhone・Androidスマホ）の場合の処理を記述
} else {
  // PC・タブレットの場合の処理を記述
}
```
## ウィンドウサイズで判別
```javascript
if (window.matchMedia("(max-width: 767px)").matches) {
  // ウィンドウサイズが 767px以下の場合に有効にしたい処理
}
```