---
notion_id: 1a993c45-a2e2-498a-98d8-d3c0f0de57e2
account: Secondary
title: Swiper（fraction & progressbar）
url: https://www.notion.so/Swiper-fraction-progressbar-1a993c45a2e2498a98d8d3c0f0de57e2
created_time: 2023-01-28T05:36:00.000Z
last_edited_time: 2023-01-28T05:39:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.466180
---
# Swiper（fraction & progressbar）

```html
<div class="swiper">
<!-- Slider main container -->
<div class="swiper-container">
  <!-- Additional required wrapper -->
  <div class="swiper-wrapper">
    <!-- Slides -->
    <div class="swiper-slide">
      <div class="title">Slider with slide progressbar</div>
      <div class="description">Lorem ipsum dolor sit amet</div>
    </div>
    <div class="swiper-slide">
      <div class="title">Slide 2</div>
      <div class="description">Lorem ipsum dolor sit amet</div>
    </div>
    <div class="swiper-slide">
      <div class="title">Slide 3</div>
      <div class="description">Lorem ipsum dolor sit amet</div>
    </div>
  </div>
  <!-- If we need pagination -->
  <div class="swiper-pagination swiper-pagination--test"></div>

  <!-- If we need navigation buttons -->
  <div class="swiper-button-prev"></div>
  <div class="swiper-button-next"></div>
  <!-- Progressbar -->
  <div class="swiper-progress-bar">
    <span class="slide_progress-bar"></span>
  </div>
</div>
</div>
```
```scss
.swiper {
  position: relative;
  height: rem(500);
  background: #eee;
  font-family: Helvetica Neue, Helvetica, Arial, sans-serif;
  font-size: 14px;
  color: #000;
  margin: 0;
  padding: 0;
}

.swiper-container {
  overflow: hidden;
  width: 100%;
  height: 100%;
}

.swiper-button {

  &-next,
  &-prev {
    color: #000;
  }
}

.swiper-slide-duplicate,
.swiper-slide {
  background-position: center center;
  background-size: cover;
  text-align: center;
  font-size: 18px;
  background: #fff;

  /* Center slide text vertically */
  display: flex;
  flex-flow: column nowrap;
  justify-content: center;
  align-items: center;

  /* Slide content */
  .description,
  .title {
    display: block;
    opacity: 0;
    transition: 0.5s ease 0.5s;
  }

  &-active {

    .description,
    .title {
      opacity: 1;
    }

    .title {
      margin-bottom: 0.5rem;
      font-size: 24px;
      color: #000;
      transition: opacity 0.5s ease 0.5s;
    }

    .description {
      font-size: 16px;
      color: #777;
      transition: opacity 0.5s ease 0.75s;
    }
  }
}

.swiper-progress-bar {
  position: relative;
  width: rem(200) ;
  display: block;
  z-index: 1;
  height: 2px;

  .slide_progress-bar {
    position: absolute;
    height: 2px;
    background: rgba(0, 0, 0, 0.3);
    width: auto;
    clear: both;
    opacity: 0;
    bottom: 32px;
    left: rem(10) ;
    right: 0;

    &:after {
      position: absolute;
      top: 0;
      left: 0;
      background: #000;
      height: 100%;
      width: 0;
      content: "";
      transition: 0.1s width linear;
    }
  }

  &.active {
    .slide_progress-bar {
      opacity: 1;
    }
  }

  &.animate {
    .slide_progress-bar {
      &:after {
        transition: width linear;
        transition-delay: unset;
        width: 100%;
        transition-duration: 1s;
      }
    }
  }
}

.swiper-pagination--test {
  color: transparent;
  display: flex;
  
  position: relative;
}

.swiper-pagination--test span {
  color: #000;
  display: block;
  position: absolute;
  bottom: rem(10) ;
}

.swiper-pagination--test span:last-child {
  margin-left: rem(210);
}
```
```javascript
$(document).ready(function () {
  var swiper = new Swiper(".swiper-container", {
    autoplay: {
      delay: 1000,
      disableOnInteraction: false
    },
    speed: 500,
    loop: true,
    pagination: {
      el: ".swiper-pagination",
      type: "fraction"
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev"
    },
    on: {
      init: function () {
        $(".swiper-progress-bar").removeClass("animate");
        $(".swiper-progress-bar").removeClass("active");
        $(".swiper-progress-bar").eq(0).addClass("animate");
        $(".swiper-progress-bar").eq(0).addClass("active");
      },
      slideChangeTransitionStart: function () {
        $(".swiper-progress-bar").removeClass("animate");
        $(".swiper-progress-bar").removeClass("active");
        $(".swiper-progress-bar").eq(0).addClass("active");
      },
      slideChangeTransitionEnd: function () {
        $(".swiper-progress-bar").eq(0).addClass("animate");
      }
    }
  });
  $(".swiper-container").hover(function () {
    swiper.autoplay.stop();
    $(".swiper-progress-bar").removeClass("animate");
  }, function () {
    swiper.autoplay.start();
    $(".swiper-progress-bar").addClass("animate");
  });
});
```