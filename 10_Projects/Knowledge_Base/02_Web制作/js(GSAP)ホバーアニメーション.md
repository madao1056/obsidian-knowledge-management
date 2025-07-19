---
notion_id: 25cee4fe-83f9-414b-a898-bca6e85255fe
account: Secondary
title: js(GSAP)ホバーアニメーション
url: https://www.notion.so/js-GSAP-25cee4fe83f9414ba898bca6e85255fe
created_time: 2024-03-11T12:48:00.000Z
last_edited_time: 2024-03-11T12:54:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.395984
---
# js(GSAP)ホバーアニメーション

```html
<head>
	<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script>
	<script defer src="./js/script.js"></script>
</head>


<div class="p-test__btn">
	<a href="#" class="c-link js-link">c-link</a>
</div>

<div class="p-test__btn">
　<a href="#" class="c-btn js-btn">c-btn</a>
</div>
```
- _c-btn.scss
  ```scss
@use "global" as *;
.c-btn {
  font-size: rem(15.4);
  font-weight: 500;
  color: #fff;
  padding: rem(10);
  width: rem(200);
  text-align: center;
  display: inline-block;
  background-color: #333;
  &:hover {
    opacity: 1;
  }
}
.c-btn__text-wrap {
  position: relative;
}
.c-btn__after {
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  align-items: center;
  width: 100%;
  justify-content: center;
}
.c-btn__before {
  display: flex;
  align-items: center;
  justify-content: center;
}

  ```
- _c-link.scss
  ```scss
@use "global" as *;

.c-link{
  text-transform: uppercase;
  letter-spacing: .2em;
  font-size: rem(15.4);
  padding-bottom: rem(10);
  border-bottom: 1px solid #333;
  display: inline-block;
  max-width: 200px;
  width: 100%;
  position: relative;
  --opacity: 1;
  --right: 0;
  &:hover{
    opacity: 1;
  }
  &::before{
    position: absolute;
    content: '';
    opacity: var(--opacity);
    right: var(--right);
    top: 20%;
    width: rem(10);
    height: rem(10);
    background: url("../images/common/link-arrow-black.svg") no-repeat center center / contain;
  }
}

.c-link__text-wrap{
  position: relative;
  overflow: hidden;
}
.c-link__after{
    position: absolute;
    top: 0;
    left: 0;
    display: flex;
    align-items: center;
}
.c-link__before{
    display: flex;
    align-items: center;
}

  ```
```javascript

/* js-btn */
let btnHover = document.querySelectorAll('.js-btn');
btnHover.forEach((target) => {
  newText = target.innerHTML;
  newTextBefore = "<div class='c-btn__before'>" + newText + "</div>";
  newTextAfter = "<div class='c-btn__after'>" + newText + "</div>";
  newText = "<div class='c-btn__text-wrap'>" + newTextBefore + newTextAfter + "</div>";
  target.innerHTML = newText;
});
/* ホバーした時の動き */
btnHover.forEach((target) => {
  let before = target.querySelector('.c-btn__before');
  let after = target.querySelector('.c-btn__after');
  target.addEventListener('mouseenter', () => {
    gsap.timeline()
      .fromTo(before, { y: '0%' }, { y: '-100%', ease: "power2.out", duration: .4 })
      .fromTo(after, { y: '100%' }, { y: '0%', ease: "power2.out", duration: .4 }, '<')
      .fromTo(before, { autoAlpha: 1 }, { autoAlpha: 0 }, '-=.3')
      .fromTo(after, { autoAlpha: 0 }, { autoAlpha: 1 }, '<')
  })
  target.addEventListener('mouseleave', () => {
    gsap.timeline()
      .fromTo(before, { y: '-100%' }, { y: '0%', ease: "power2.out", duration: .4 })
      .fromTo(after, { y: '0%' }, { y: '100%', ease: "power2.out", duration: .4 }, '<')
      .fromTo(before, { autoAlpha: 0 }, { autoAlpha: 1 }, '-=.3')
      .fromTo(after, { autoAlpha: 1 }, { autoAlpha: 0 }, '<')
  });
});

```