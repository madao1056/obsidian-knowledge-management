---
notion_id: ce92ed5f-19c9-4134-b27f-6a5538cde3ad
account: Secondary
title: パララックス（Safari対応）
url: https://www.notion.so/Safari-ce92ed5f19c94134b27f6a5538cde3ad
created_time: 2023-05-15T23:08:00.000Z
last_edited_time: 2023-05-15T23:15:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.447885
---
# パララックス（Safari対応）

```html
<div class="parallax">
      <div class="parallax__bg"></div>
ここに要素が入る
</div>
```
```scss
@use "global" as *;

.parallax {
  position: relative;
  overflow: hidden;
}

.parallax__bg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  clip-path: polygon(0 0, 100% 0, 100% 100%, 0% 100%);
  z-index: -1;
  background: transparent;
}

.parallax__bg::before {
  content: "";
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: url(../images/common/bg-parallax.jpg) center / cover no-repeat;
  z-index: -1;

  @include mq("md") {
    background-image: url(../images/common/bg-parallax-sp.jpg);
    background-size: 100% 100%;
  }
}
```

## タグ

#よしなに対応 

## 関連ドキュメント

- [[../01_よしなに対応/パララックスでbackground-attachment_ fixed;は使用不可.md|パララックスでbackground-attachment_ fixed;は使用不可]]
- [[../99_その他/left.md|left]]
- [[../99_その他/height.md|height]]
- [[../99_その他/top.md|top]]
- [[../99_その他/x.md|x]]
