---
notion_id: 29e1dd47-caa1-40e7-8255-c85cf666a9cb
account: Secondary
title: swiperのpadding-top管理
url: https://www.notion.so/swiper-padding-top-29e1dd47caa140e78255c85cf666a9cb
created_time: 2022-05-29T10:04:00.000Z
last_edited_time: 2022-05-29T10:05:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.490375
---
# swiperのpadding-top管理

```scss
.swiper {
  position: relative;
  width: 100%;
}

.swiper::before {
  content: "";
  padding-top: 48.61111%;
  display: block;
}

.swiper-wrapper {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.swiper-wrapper img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
}
```