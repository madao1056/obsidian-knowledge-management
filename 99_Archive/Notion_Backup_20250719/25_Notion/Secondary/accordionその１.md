---
notion_id: 1f9a19b9-d5d2-42d0-8908-18bb6d4f8718
account: Secondary
title: accordionその１
url: https://www.notion.so/accordion-1f9a19b9d5d242d0890818bb6d4f8718
created_time: 2022-04-23T06:11:00.000Z
last_edited_time: 2023-10-10T05:29:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.417727
---
# accordionその１

<details>
<summary>html</summary>
</details>
  ```html
<section class="accordion">
      <div class="accordion-container">
        <div class="accordion-title jsAccordionTitle">アコーディオンその１</div>
        <div class="accordion-content">
          ここにアコーディオンの内容が入ります。改行されてもボックスは自動的に拡張されます。
        </div>
        <div class="accordion-title jsAccordionTitle">アコーディオンその2</div>
        <div class="accordion-content">
          ここにアコーディオンの内容が入ります。改行されてもボックスは自動的に拡張されます。
        </div>
        <div class="accordion-title jsAccordionTitle">アコーディオンその3</div>
        <div class="accordion-content">
          ここにアコーディオンの内容が入ります。改行されてもボックスは自動的に拡張されます。
        </div>
      </div>
      <!-- accordion__container -->
    </section>
    <!-- /.accordion -->
  ```
<details>
<summary>scss</summary>
</details>
  ```scss
@use "global" as *;

.accordion {
  margin-top: 10px;
}

.accordion-container {
  width: 500px;
  margin: 0 auto;
}

.accordion-title {
  background-color: #fff;
  border-top: 1px solid rgb(1, 3, 39);
  color: rgb(1, 3, 39);
  font-size: 18px;
  padding: 12px 12px 12px 32px;
  position: relative;
  cursor: pointer;
  user-select: none;
  &:last-of-type {
    border-bottom: 1px solid rgb(1, 3, 39);
  }
}

.accordion-title::before,
.accordion-title::after {
  content: "";
  display: block;
  background-color: rgb(1, 3, 39);
  position: absolute;
  top: 50%;
  width: 15px;
  height: 2px;
  right: 25px;
}

.accordion-title::after {
  transform: rotate(90deg);
  transition-duration: 0.3s;
}

.accordion-title:hover,
.accordion-title:active,
.accordion-title.is-active {
  text-decoration: underline;
}

.accordion-title.is-active::before {
  opacity: 0;
}

.accordion-title.is-active::after {
  transform: rotate(0);
}

.accordion-content {
  border-left: 1px solid transparent;
  border-right: 1px solid transparent;
  padding: 0 18px;
  line-height: 0;
  height: 0;
  overflow: hidden;
  opacity: 0;
  transition-duration: 0.3s;
}

.accordion-content.is-open {
  background-color: #e7e7e7;
  padding: 12px 18px;
  margin: 12px 0;
  line-height: normal; /* numberに書き換える*/
  height: auto;
  opacity: 1;
}
  ```
<details>
<summary>javascript(click)</summary>
</details>
  ```javascript
const title = document.querySelectorAll(".jsAccordionTitle");
//forEachでtitleを一つ一つtitleEachに入れている
title.forEach((titleEach) => {
  //nextElementSiblingはjQueryのnext()みたいなもの
  let content = titleEach.nextElementSibling;
  titleEach.addEventListener("click", () => {
    titleEach.classList.toggle("is-active");
    content.classList.toggle("is-open");
  });
});
  ```
<details>
<summary>javascript(hover)</summary>
</details>
  ```javascript
const title = document.querySelectorAll(".jsAccordionTitle");
//forEachでtitleを一つ一つtitleEachに入れている
title.forEach((titleEach) => {
  //nextElementSiblingはjQueryのnext()みたいなもの
  let content = titleEach.nextElementSibling;
  titleEach.addEventListener("mouseover", () => {
    titleEach.classList.toggle("is-active");
    content.classList.toggle("is-open");
  });
  titleEach.addEventListener("mouseout", () => {
    titleEach.classList.toggle("is-active");
    content.classList.toggle("is-open");
  });
});
  ```
<details>
<summary>jQuery(click)</summary>
</details>
  ```javascript
$(function () {
  $(".jsAccordionTitle").on("click", function () {
    //nextは次の要素を取得する、今回はクリック要素の次の要素にis-showクラスをつけている
    $(this).next().toggleClass("is-open");
    //クリックした要素自体にもclass付与
    $(this).toggleClass("is-active");
  });
});
  ```