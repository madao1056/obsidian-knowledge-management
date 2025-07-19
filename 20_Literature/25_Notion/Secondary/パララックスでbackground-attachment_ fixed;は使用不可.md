---
notion_id: ab77a0aa-aac4-4bf7-a2ea-371d35fd9852
account: Secondary
title: パララックスでbackground-attachment: fixed;は使用不可
url: https://www.notion.so/background-attachment-fixed-ab77a0aaaac44bf7a2ea371d35fd9852
created_time: 2023-05-07T09:01:00.000Z
last_edited_time: 2023-06-25T07:24:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.440692
---
# パララックスでbackground-attachment_ fixed;は使用不可

Safariは
**background-attachment: fixed;とbackground-sizeを同時に指定すると動かなくなる**
公式でも確認されているiOSの不具合です
【解決策】
**position: fixed; or position: stickyを使用する**
position: fixed;使用↓
[Bookmark](https://itokoba.com/archives/2375)
position: sticky;使用↓
[Bookmark](https://codepen.io/kouk05/pen/MWrWGOa)
# 実案件でたどり着いたSafariでも崩れないパララックス
コードスニペット内リンク→[パララックス（Safari対応）](https://www.notion.so/ce92ed5f19c94134b27f6a5538cde3ad) 