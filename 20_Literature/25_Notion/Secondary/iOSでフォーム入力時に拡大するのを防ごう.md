---
notion_id: 7bd81c4e-ec44-4c79-a64f-823085a701d3
account: Secondary
title: iOSでフォーム入力時に拡大するのを防ごう
url: https://www.notion.so/iOS-7bd81c4eec444c79a64f823085a701d3
created_time: 2023-07-21T00:47:00.000Z
last_edited_time: 2023-07-21T00:51:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.437215
---
# iOSでフォーム入力時に拡大するのを防ごう

フォームを入力する際に画面が拡大する現象が発生。
原因はinputタグ内のfont-sizeが15px以下だったために起こるiphoneのデフォルトの機能だった。
（動画の時はfont-size:13px;）
**解決策はfont-sizeを16px以上にすればOK。**