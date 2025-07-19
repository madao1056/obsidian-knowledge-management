---
notion_id: cb5fdfda-439b-4d85-a054-52e1a79331d2
account: Secondary
title: accordionその２（スライド）
url: https://www.notion.so/accordion-cb5fdfda439b4d85a05452e1a79331d2
created_time: 2022-05-19T05:36:00.000Z
last_edited_time: 2023-07-11T15:13:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.440067
---
# accordionその２（スライド）

<details>
<summary>html</summary>
</details>
  ```html
<dl class="accordion js-accordion">
  <div class="accordion__item js-accordion-trigger">
    <dt class="accordion__title">DEMO1のタイトル</dt>
    <dd class="accordion__content">DEMO1のコンテンツ</dd>
  </div>
  <div class="accordion__item js-accordion-trigger">
    <dt class="accordion__title">DEMO1のタイトル</dt>
    <dd class="accordion__content">DEMO1のコンテンツ</dd>
  </div>
  <div class="accordion__item js-accordion-trigger">
    <dt class="accordion__title">DEMO1のタイトル</dt>
    <dd class="accordion__content">DEMO1のコンテンツ</dd>
  </div>
</dl>
  ```
<details>
<summary>scss</summary>
</details>
  ```scss
@use "global" as *;

/* アコーディオン全体 */
.accordion {
  max-width: 800px;
  margin: 0 auto;
}

/* アコーディオン */
.accordion__item {
  border: 1px solid #ccc;
  margin-top: 10px;
  cursor: pointer;
}

/* アコーディオンのタイトル */
.accordion__title {
  position: relative;
  padding: 15px 60px 15px 20px;
  font-weight: bold;
  cursor: pointer;
}

/* (+)アイコン */
.accordion__title::before,
.accordion__title::after {
  content: "";
  position: absolute;
  right: 20px;
  top: 0;
  bottom: 0;
  margin: auto 0;
  background-color: #3abec1;
  width: 20px;
  height: 4px;
  transition: all 0.3s;
}

.accordion__title::after {
  transform: rotate(90deg);
}

/* アコーディオンのコンテンツ */
.accordion__content {
  padding: 0 20px 15px 20px;
  display: none;
  cursor: pointer;
}

.accordion__content.is-open {
  display: block;
}

/* アコーディオン展開時の(-)アイコン */
.accordion__item.is-active .accordion__title::before {
  transform: rotate(180deg);
}

.accordion__item.is-active .accordion__title::after {
  transform: rotate(180deg);
  opacity: 0;
}
  ```
<details>
<summary>javascript(click)</summary>
</details>
  ```javascript
/* =================================================== */
// slideUp, slideDown, slideToggle関数を定義
/* =================================================== */

// 要素をスライドしながら非表示にする関数(jQueryのslideUpと同じ)
const slideUp = (el, duration = 300) => {
  el.style.height = el.offsetHeight + "px";
  el.offsetHeight;
  el.style.transitionProperty = "height, margin, padding";
  el.style.transitionDuration = duration + "ms";
  el.style.transitionTimingFunction = "ease";
  el.style.overflow = "hidden";
  el.style.height = 0;
  el.style.paddingTop = 0;
  el.style.paddingBottom = 0;
  el.style.marginTop = 0;
  el.style.marginBottom = 0;
  setTimeout(() => {
    el.style.display = "none";
    el.style.removeProperty("height");
    el.style.removeProperty("padding-top");
    el.style.removeProperty("padding-bottom");
    el.style.removeProperty("margin-top");
    el.style.removeProperty("margin-bottom");
    el.style.removeProperty("overflow");
    el.style.removeProperty("transition-duration");
    el.style.removeProperty("transition-property");
    el.style.removeProperty("transition-timing-function");
    el.classList.remove("is-open");
  }, duration);
};

// 要素をスライドしながら表示する関数(jQueryのslideDownと同じ)
const slideDown = (el, duration = 300) => {
  el.classList.add("is-open");
  el.style.removeProperty("display");
  let display = window.getComputedStyle(el).display;
  if (display === "none") {
    display = "block";
  }
  el.style.display = display;
  let height = el.offsetHeight;
  el.style.overflow = "hidden";
  el.style.height = 0;
  el.style.paddingTop = 0;
  el.style.paddingBottom = 0;
  el.style.marginTop = 0;
  el.style.marginBottom = 0;
  el.offsetHeight;
  el.style.transitionProperty = "height, margin, padding";
  el.style.transitionDuration = duration + "ms";
  el.style.transitionTimingFunction = "ease";
  el.style.height = height + "px";
  el.style.removeProperty("padding-top");
  el.style.removeProperty("padding-bottom");
  el.style.removeProperty("margin-top");
  el.style.removeProperty("margin-bottom");
  setTimeout(() => {
    el.style.removeProperty("height");
    el.style.removeProperty("overflow");
    el.style.removeProperty("transition-duration");
    el.style.removeProperty("transition-property");
    el.style.removeProperty("transition-timing-function");
  }, duration);
};

// 要素をスライドしながら交互に表示/非表示にする関数(jQueryのslideToggleと同じ)
const slideToggle = (el, duration = 300) => {
  if (window.getComputedStyle(el).display === "none") {
    return slideDown(el, duration);
  } else {
    return slideUp(el, duration);
  }
};

/* =================================================== */
// DOM操作
/* =================================================== */

// アコーディオンを全て取得
const accordions = document.querySelectorAll(".js-accordion");
// 取得したアコーディオンをArrayに変換(IE対策)
const accordionsArr = Array.prototype.slice.call(accordions);

accordionsArr.forEach((accordion) => {
  // Triggerを全て取得
  const accordionTriggers = accordion.querySelectorAll(".js-accordion-trigger");
  // TriggerをArrayに変換(IE対策)
  const accordionTriggersArr = Array.prototype.slice.call(accordionTriggers);

  accordionTriggersArr.forEach((trigger) => {
    // Triggerにクリックイベントを付与
    trigger.addEventListener("click", () => {
      // '.is-active'クラスを付与or削除
      trigger.classList.toggle("is-active");
      // 開閉させる要素を取得
      const content = trigger.querySelector(".accordion__content");
      // 要素を展開or閉じる
      slideToggle(content);
    });
  });
});
  ```