---
notion_id: ee5a1de1-491e-4575-b821-27d12afbaed8
account: Secondary
title: アニメーション(zoomup-down)
url: https://www.notion.so/zoomup-down-ee5a1de1491e4575b82127d12afbaed8
created_time: 2022-05-31T23:40:00.000Z
last_edited_time: 2023-12-04T15:33:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.409659
---
# アニメーション(zoomup-down)

```scss
animation: expansion .8s infinite alternate;

@keyframes expansion{
0%, 10% {
    transform: scale(1);
}
90%, 100% {
    transform: scale(0.96);
}
}
```