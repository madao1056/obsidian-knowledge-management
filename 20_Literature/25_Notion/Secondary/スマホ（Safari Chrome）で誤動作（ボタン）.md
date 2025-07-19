---
notion_id: fffd0c30-9401-811a-99a9-cda39816dd53
account: Secondary
title: スマホ（Safari Chrome）で誤動作（ボタン）
url: https://www.notion.so/Safari-Chrome-fffd0c309401811a99a9cda39816dd53
created_time: 2024-09-20T01:11:00.000Z
last_edited_time: 2024-09-20T01:11:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.384737
---
# スマホ（Safari Chrome）で誤動作（ボタン）

# 概要
- スマホ（Safari Chrome）でボタンをタップしても1回目が反応しない
- 2回目から反応する
- 他のボタンの同様
# 解決のヒント
[Bookmark](https://snow-monkey.2inc.org/forums/topic/スマホのchromeでのみhoverが効いて2クリックしないと遷/)
- bodyタグに`ontouchstart`という属性を追加する
コレで不具合は解消された。