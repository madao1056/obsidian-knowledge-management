---
notion_id: 6acaf709-56b9-4bc0-b593-0b970392ea75
account: Secondary
title: 個別のブラウザのみ適用のCSSの書き方
url: https://www.notion.so/CSS-6acaf70956b94bc0b5930b970392ea75
created_time: 2023-07-13T15:44:00.000Z
last_edited_time: 2023-07-13T15:45:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.437525
---
# 個別のブラウザのみ適用のCSSの書き方

## **Edgeのみに適用**
```css
@supports (-ms-ime-align: auto) {
  span {
    color:#c00;
  }
}
```
## **IEのみに適用**
```css
@media all and (-ms-high-contrast: none) {
  span {
    color:#c00;
  }
}
```
## **Firefoxのみに適用**
```css
@-moz-document url-prefix() {
  span {
    color:#0c0;
  }
}
```
## **Chromeのみに適用**
```css
@media screen and (-webkit-min-device-pixel-ratio:0) {
  span {
    color:#00c;
  }
}
```
## **Safariのみに適用**
### *最新のsafari用*
```css
::-webkit-full-page-media, :future, :root
 span {
  color:#c0c;
}
```
### *古いsafari用*
```css
@media screen and (-webkit-min-device-pixel-ratio: 0) {
  ::i-block-chrome,
  span {
  color:#c0c;
}
}
```

## タグ

#0c0; #c00; #00c; #Web制作 #c0c; 

## 関連ドキュメント

- [[../99_その他/y.md|y]]
