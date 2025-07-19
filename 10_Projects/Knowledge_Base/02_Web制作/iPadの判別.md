---
notion_id: 7e2d6506-59cc-48b9-95e1-454a8370d292
account: Secondary
title: iPadの判別
url: https://www.notion.so/iPad-7e2d650659cc48b995e1454a8370d292
created_time: 2022-05-08T23:54:00.000Z
last_edited_time: 2022-05-08T23:54:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.504157
---
# iPadの判別

```javascript
// iPad
var ua = window.navigator.userAgent.toLowerCase();
if (
  ua.indexOf("ipad") > -1 ||
  (ua.indexOf("macintosh") > -1 && "ontouchend" in document)
) {
	// iPadでの動作を記入
} else {
	// iPad以外での動作を記入
}
```
[Bookmark](https://junpei-sugiyama.com/ipad-useragent/)

## タグ

#Web制作 

## 関連ドキュメント

- [[../99_その他/x.md|x]]
- [[../99_その他/y.md|y]]
