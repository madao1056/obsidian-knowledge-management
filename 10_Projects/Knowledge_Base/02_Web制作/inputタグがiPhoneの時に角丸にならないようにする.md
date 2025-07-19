---
notion_id: aae01a61-1abf-4916-a3db-e239827560e6
account: Secondary
title: inputタグがiPhoneの時に角丸にならないようにする
url: https://www.notion.so/input-iPhone-aae01a611abf4916a3dbe239827560e6
created_time: 2023-07-20T05:00:00.000Z
last_edited_time: 2023-07-20T05:05:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.437317
---
# inputタグがiPhoneの時に角丸にならないようにする

iPhoneで確認した際にinputタグのデザインが異なる事象が発生しました。
原因はデフォルトの設定の違いによるものでした。
解決策は下記コードをreset.scssにコピペすればOKです！
reset.scssに追記↓
```scss
// inputタグがiPhoneの時に角丸にならないようにする
input[type="button"],
input[type="text"],
input[type="submit"],
input[type="image"],
textarea {
  -webkit-appearance: none;
  border-radius: 0;
}
```

## タグ

#Web制作 

## 関連ドキュメント

- [[../02_Web制作/デザイン.md|デザイン]]
- [[../99_その他/x.md|x]]
- [[../99_その他/y.md|y]]
- [[../02_Web制作/実装方法について.md|実装方法について]]
- [[../02_Web制作/スギノマシン様の採用サイトリニューアル業務.md|スギノマシン様の採用サイトリニューアル業務]]
