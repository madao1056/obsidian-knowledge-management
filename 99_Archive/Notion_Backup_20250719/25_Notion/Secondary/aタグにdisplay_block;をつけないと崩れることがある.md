---
notion_id: 7e559e5c-b1d7-4002-bff9-e3334463b772
account: Secondary
title: aタグにdisplay:block;をつけないと崩れることがある
url: https://www.notion.so/a-display-block-7e559e5cb1d74002bff9e3334463b772
created_time: 2023-05-07T08:14:00.000Z
last_edited_time: 2023-06-25T07:26:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.440586
---
# aタグにdisplay_block;をつけないと崩れることがある

Safariで検証した際にChromeは正常に表示されたが、Safariで表示が崩れた
原因はaタグにdisplay:block;がついていなかったから
特にaタグ内でabsoluteを使用するときなどに表示崩れが起きるので、脳死でdisplay:block;はつけておいた方がいい