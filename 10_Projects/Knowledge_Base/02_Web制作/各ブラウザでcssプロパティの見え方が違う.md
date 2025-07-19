---
notion_id: 08ece897-2e12-4b4d-a271-24331924ba98
account: Secondary
title: 各ブラウザでcssプロパティの見え方が違う
url: https://www.notion.so/css-08ece8972e124b4da27124331924ba98
created_time: 2023-07-13T15:39:00.000Z
last_edited_time: 2023-07-13T15:44:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.438795
---
# 各ブラウザでcssプロパティの見え方が違う

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

- [[../99_その他/x.md|x]]
- [[../99_その他/y.md|y]]
