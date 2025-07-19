---
notion_id: eba3b69d-fd94-4c4a-b472-b75ceb66ebca
account: Secondary
title: border-radiusがhoverアニメーション中に効かない
url: https://www.notion.so/border-radius-hover-eba3b69dfd944c4ab472b75ceb66ebca
created_time: 2023-05-07T07:52:00.000Z
last_edited_time: 2023-05-07T07:56:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.448515
---
# border-radiusがhoverアニメーション中に効かない

Safariで画像を丸角にしている際にアニメーション中にborder-radiusが効かない現象が発生
```css
overflow:hidden;
border-radius:20px;
以下を追加↓
position: relative;
z-index: 1;
```

## タグ

#Web制作 

## 関連ドキュメント

- [[../99_その他/x.md|x]]
- [[../99_その他/y.md|y]]
