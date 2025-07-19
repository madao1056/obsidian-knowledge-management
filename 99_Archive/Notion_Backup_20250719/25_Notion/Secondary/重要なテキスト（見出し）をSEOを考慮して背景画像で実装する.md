---
notion_id: ac16d3d9-1643-4f49-b85f-5b3293874c0f
account: Secondary
title: 重要なテキスト（見出し）をSEOを考慮して背景画像で実装する
url: https://www.notion.so/SEO-ac16d3d916434f49b85f5b3293874c0f
created_time: 2024-01-18T00:22:00.000Z
last_edited_time: 2025-05-04T07:57:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.364992
---
# 重要なテキスト（見出し）をSEOを考慮して背景画像で実装する

全体説明動画
参考画像
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/d58fe38c-a9d4-4466-aed9-85604b7b2c6d/14ab9552-296c-4564-9154-f0e0b38d1ee6/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88_2024-01-18_9.30.35.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RWSOLBXT%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T070103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDNENla7WOW%2FSnbW6Y94jlP44KTrDFmT4DXiW%2B5M0SgUAIgJCkIBBIWkU7zeMCP42AlxvZXg4NrGbVOtMNhRDajspwqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG%2B1xf%2BilNo6xH0%2BiircA4JHgp8CSf%2Bnf0M8BMlBli07i07Ncp8R1rskHdbm0IMHTFkbLysdHEeciaMzRQVGxKcZaYMdKmSmRJTui%2FyfsYLRmgQByFdPyAKLJTGlyDjzgrdmCeto6Ajz1%2FEPTDYD%2BATWtbYSxxiX1IUY0c6W4VeZYIyAQm1FLzdjCJKJ3uEqQy8XYX7kzuFHyN5vY8gcoW8eV9zGPcI1alddTYjUQCIL91xGJZryZTiGA5ibJXscPSi5w8FS3ncqzOPt7rxMAmN9J6FoEp0qD%2FyoZ3gn1O69wFKwaaLQKSRo062mwk%2B0nNDEk0k8NUQfJAzaY3T%2BgO85F6BQi79dxbU6CHsAJLYHxuqLuMiQogvTmLVyXeg4cpbdc8uVKLC63o%2BD0pqVgT3A3dUqfaFndXOjCJiPTtNd%2BjL250dejhpWEM3f%2F%2Ba%2BcV%2FFuKSfCSFhkXzBbAlm7HPX5X1EX4Fiw4UqcNR4iX4HXUZCZEzC1BZUf4oM%2FcBA9UP8B4x0V5S4GuS0HTlgJpg5%2F0Ku%2FyWIiivVPWLwFONrbCYYAj2V3O8N0ZnCcUa0CW%2Fl%2BbXxs2LuteXOAIb%2BOhRH%2Ff99iJy0qJ96Xr2uom2xM2EcOQFTUEN3m1RqqMKZmBf%2B92%2Fa9DKpNqrOMN3F7MMGOqUB7J6Us6tDvsmwd4MKI5hPlNTA2jKtkAT7s9WgUGTbVLkJr2mesaNys4xHH9%2BBMMRZhiK1ZOsqT%2BjRwHPZRE45ucQ2TCxbgHMfXazt8Yq6VqyyHfhmUOTvr5DHPm5jb%2FihCVmm5r4Fb%2FGqCcl46H0of9T0Mn0T%2B4065EeVsScUTToCBzB5nJb6WsWi%2BvGrWCF3WZk8kLdxgO9MkDVWRHGnWRUSx4KZ&X-Amz-Signature=f42f9a13f9589320a67eca56103934e34d5d224f5d83ecb08ff30e51f5f3bb9a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
---
### 🔹背景
- 見出しが特殊なフォントを使っていて、画像の書き出しで実装するしかなかった
---
### 🔹考え方
- 見出しで4、５箇所しか使用されていないフォントをわざわざ読み込むのはページスピードを下げる要因にもなるので、少ない箇所の特殊なフォントはできるだけ画像として処理したい。
- SEOを考えると、見出しを画像で書き出すのが一般的だが、文字としてhtmlに残しておければそれに越したことはない。
- 背景画像として、書き出した画像を入れて、文字を範囲外に移動させることでhtmlにもテキストとして表示させることができ、かつデザインも再現できる。
- 隠しテキストになるものは以下のようなもの。
「文字色を透明にする」「文字サイズを0にする」「背景色を同じ色にする」「CSSで隠す」 「画像に文字を埋め込む」「JavaScriptを使用して文字を埋め込む」
text-indent: -9999pxとすると違反の対象になる→101%は現状問題なさそうだが、グレーゾーンであることは確かなので、**実装は自己責任**で行う。
- 現状は問題ない実装方法だと考える。
（実際に広告をしている方からの情報になるが、ここも自己責任で実装を判断する）
---
### 🔹実装方法
1. 動画もつける
### 🔹コード
```html
<h2 class="text-hidden">ここにテキストも入れます</h2>
```
```scss
.text-hidden {
  text-indent: 101%;
  overflow: hidden;
  white-space: nowrap;
  background-image: url(../images/top/img_text.svg);
  background-repeat: no-repeat;
  background-size: contain;
  background-position: center;
}
```