---
notion_id: 849a2a56-b560-4062-9b60-bcf27e5d96a8
account: Main
title: FVについて
url: https://www.notion.so/FV-849a2a56b56040629b60bcf27e5d96a8
created_time: 2023-05-07T14:53:00.000Z
last_edited_time: 2023-05-10T00:20:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:15.112344
---
# FVについて

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/736adce6-a3a4-4a64-9f74-d9aa055c96d2/e177d2e0-32a8-49c3-b4f3-d84a163b4a5e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673WGIPDP%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T042251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBdgqVuAjci3z%2Bo4U0vd6OnswzPnKGQ%2BJZulsYao8JPzAiBp1Y8igaWpSUFwGNUEwMU17kVy6V7B%2Fm4gWZYmzGl2tCqIBAid%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM5%2FKJy%2B29waNIWzOLKtwDb9SKf63aA6UrdWNoN%2BjRp87i7PWY9fT9F1cPsreO%2BRQRUENy1tWmf%2FRUGJE0EoVJeEoJDDovTA1Bu1y9kJCeuSG5LAx2Q3j595lCXNozL8dYP0wNQVcdT0CL9azg%2F9W%2BAMj3%2FRwayl3qK7UcRd4JK%2Fdoal6Y2ead52xv8zrrLMkWzWQvK0hCE%2BL64PnYF38P3vEMDn0rDeZQAVMUjpNrPf%2BSybfcqNg0lJ3DegcumljdSfcIfw%2BsRmMMyjPYVP6Aipgg0rH5gcm2BDxd%2FSRpsskJ0qDaFc9HKk6uGNnd0uGPzU2DhZndJN82PcedzOMcSQu4h%2BQQkdEjdhX4TMn39ErPFQux7sKSyqls8vJxlnte4GsgWr46ZzMrvfrYgmZ9uO4n0RKggWb7dlPwxA1%2Fbv3QRjdPbLMXWiwopcMsXWp7E7%2FBeljEiDYG7jPq%2FmM9q1oRyIBlQJEOxz%2FZE087XgMKlLCtDd9ZfcyD6RsMQJtxKGquSd8O4UQOsrpZPo8Lvws5y8eIv4FQSSuz0HgugIrI1Fpapvv87vmBLp9gbsMYstcCUmFfOgbhKTDZxKrY2NybEDF2wk5ey9hY8Q%2B%2BnddMVMosEx2jS7bHC2KG72pIR1wmKnS102tdNccw0qrswwY6pgHGj48GaL2Op9jFyp6ptkFD9kRcuZkxxXfxeJfIRpwRF%2B4Q2Ru5YnMrfj%2FeeDun4fmCaHhp1j7Qu7if5APc7T%2By500yArAgaNOskdsMvi91z1os4Pnvtm8zpiHHitS6BF9TsPEs8TbNQ9jLp0d6nH295cAKEp2txfCUlrfcrL7NZJriI%2FJaGOXbmwpNqic8c9e14a8ywVPTikKsnQZxySpfL5%2FRzV0O&X-Amz-Signature=97ba38ac13fe0d3efde37df737dea85c2be23535f4bbe3ba6f9ac2c8792c86c2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
【修正詳細】
デザインカンプの画面幅1920pxより小さくなった場合に見切れてしまうので、画面幅が変わっても比率を同じようにしていただきたいです
【期待値】
画面幅が可変しても表示がカンプ通り
.mvクラスのアスペクト比を固定
その他、ロゴ、テキストも1920px時の画面幅の比率で管理する（PC時↓）
```css
.mv{
width: 100%;
height: 100%;
aspect-ratio: 1920/708;
}
.mv__inner{
padding: calc(88/1920*100vw) 0 calc(265/1920*100vw);
}
.mv__logo img{
width: calc(635/1920*100vw);
height: auto;
}
.mv__title h2{
font-size: calc(72/1920*100vw);
}
.mv__text p{
font-size: clamp(1rem, 0.714rem + 0.446vw, 1.25rem);//1920px→20px,1024px→16px
}
```

## タグ

#Web制作 

## 関連ドキュメント

- [[../02_Web制作/スマホのFVについて.md|スマホのFVについて]]
- [[../02_Web制作/デザイン.md|デザイン]]
- [[../99_その他/Untitled.md|Untitled]]
- [[../99_その他/その他.md|その他]]
- [[../99_その他/width.md|width]]
