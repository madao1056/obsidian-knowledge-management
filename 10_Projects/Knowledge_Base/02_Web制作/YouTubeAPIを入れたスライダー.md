---
notion_id: e3b00597-9e5f-40e3-ba90-49871548d39d
account: Secondary
title: YouTubeAPIを入れたスライダー
url: https://www.notion.so/YouTubeAPI-e3b005979e5f40e3ba9049871548d39d
created_time: 2023-08-17T12:55:00.000Z
last_edited_time: 2023-08-17T13:08:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.427330
---
# YouTubeAPIを入れたスライダー

ACF（カスタムフィールド）にてフィールドタイプ”テキスト”のIDが”youtube_id”というYouTubeIDを入れるフィールドも実装すること
```javascript
// ==========
  // youtube replace
  // ==========
  function ImageToYoutubeReplace(ytImage) {
    let youtubeId = ytImage.getAttribute('youtubeid');
    let youtubeVideo = '<iframe class="p-movie__youtube" youtubeid="' + youtubeId + '" src="https://www.youtube.com/embed/' + youtubeId + '?playsinline=1&enablejsapi=1&rel=0" frameborder="0" allowfullscreen></iframe>'
    ytImage.innerHTML = youtubeVideo;
    ytImage.classList.add('play');
  };
  function YoutubeToImageReplace(ytIframe) {
    let youtubeId = ytIframe.getAttribute('youtubeid');
    let youtubeImage = '<img src="http://img.youtube.com/vi/' + youtubeId + '/maxresdefault.jpg" alt="thumbs">'
    ytIframe.innerHTML = youtubeImage;
    ytIframe.classList.remove('play');
  };

  //---------- youtube swiper --------------
  let sliderYtSet = {
    centeredSlides: true,
    loop: true,
    slidesPerView: "auto",
    pagination: {
      el: ".youtube-swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".youtube-swiper-button-next",
      prevEl: ".youtube-swiper-button-prev",
    },
    on: {
      slideChange: function () {
        const ytVideoPlayerBoxes = document.querySelectorAll('.p-movie__slideBox');
        ytVideoPlayerBoxes.forEach((ytVideoPlayerBox) => {
          YoutubeToImageReplace(ytVideoPlayerBox);
          ytVideoPlayerBox.parentNode.classList.remove('play');
        });
      }
    }
  }
  const sliderYtNum = document.querySelectorAll('.youtube_swiper .swiper-slide').length;
  if (sliderYtNum == 1) {
    sliderYtSet = {
      loop: false,
    };
  }
  sliderYt = new Swiper('.youtube_swiper', sliderYtSet);

  //----------------youtube--------------
  const ytVideoPlayerBoxes = document.querySelectorAll('.p-movie__slideBox');
  ytVideoPlayerBoxes.forEach((ytVideoPlayerBox) => {
    ytVideoPlayerBox.addEventListener('click', () => {
      ImageToYoutubeReplace(ytVideoPlayerBox);
      ytVideoPlayerBox.parentNode.classList.add('play');
    });
  });
```
```php
<section class="p-movie l-movie">
	<div class="p-movie__inner">
    <?php
    $movie_query = new WP_Query(
      array(
        'post_type'      => 'post',
        'posts_per_page' => 5,
      )
    );
    ?>
    <?php
    if ($movie_query->post_count === 1) {
      // 投稿が1つの場合の処理
      echo '<div class="p-movie__container p-movie__container--only">';
    } else {
      echo '<div class="p-movie__container">';
    }
    ?>
    <div class="p-movie__wrap">
      <div class="p-movie__main">
        <div class="p-movie__swiperWrap">
          <div class="swiper youtube_swiper">
            <div class="swiper-wrapper">

              <?php if ($movie_query->have_posts()) : ?>
                <?php while ($movie_query->have_posts()) : ?>
                  <?php $movie_query->the_post(); ?>
                  <div class="swiper-slide p-movie__slide">
                    <?php $terms = get_the_terms($post->ID, 'news_cat');
                    $draught_links = array();
                    if ($terms && !is_wp_error($terms)) :
                      foreach ($terms as $term) {
                        $draught_links[] = $term->name;
                      }
                      $on_draught = join(", ", $draught_links);
                      echo '<span class="c-new">' . $on_draught . '</span>';
                      echo '<div class="p-movie__slideInner">';
                    else :
                      echo '<div class="p-movie__slideInner p-movie__slideInner--mt">';
                    endif; ?>
                    <div class=" p-movie__slideBox" youtubeid="<?php the_field('youtube_id'); ?>">
                      <img src="https://img.youtube.com/vi/<?php the_field('youtube_id'); ?>/maxresdefault.jpg" alt="#">
                    </div>
                  </div>
            </div>
          <?php endwhile; ?>
        <?php else : ?>
          <p>記事がありません。</p>
        <?php endif; ?>
          </div>
          <?php if ($movie_query->post_count !== 1) : ?>
            <div class="p-movie__controller">
              <div class="swiper-button-next youtube-swiper-button-next"></div>
              <div class="swiper-button-prev youtube-swiper-button-prev"></div>
              <div class="swiper-pagination youtube-swiper-pagination"></div>
              <div class="p-movie__btn l-inner">
                <a href="<?php echo $movie ?>" class="c-btn blue">view all</a>
              </div>
            </div>
          <?php endif; ?>
          <?php wp_reset_postdata(); ?>
        </div>
      </div>
    </div>
  </div>
  </div>
  </div>
</section>
```
```scss
@use "global" as *;

.p-movie {
  position: relative;
}
.p-movie__youtube {
  width: 100%;
  height: auto;
  aspect-ratio: 16/9;
  border-radius: rem(10);
}
.p-movie__container {
  margin-top: rem(50);
  position: relative;
  display: block;
  width: 100%;
  height: auto;
  overflow: hidden;
  @include mq(md) {
    margin-top: rem(20);
  }
}
.p-movie__container--only {
  max-width: calc(rem(705) + rem(21));
  margin-left: auto;
  margin-right: auto;
  @include mq(md) {
    max-width: rem(600);
  }
}
.p-movie__main {
  position: relative;
}

.p-movie__content {
  position: relative;
  padding-bottom: rem(100);
}

.p-movie__slide {
  width: calc(rem(705) + rem(21));
  padding: 0 rem(21);
  @include mq(md) {
    width: 100%;
    padding: 0 rem(25);
  }
}

.p-movie__slide img {
  width: 100%;
  height: auto;
  aspect-ratio: 16/9;
  object-fit: cover;
  border-radius: rem(10);
}
.p-movie__controller {
  position: relative;
  height: rem(100);
  @include mq(md) {
    height: rem(130);
  }
}
.p-movie__wrap {
  position: relative;
  display: block;
  height: 100%;
  margin: 0 auto;
}

.p-movie__slideInner {
  margin-top: rem(18);
  opacity: 0.4;
  transition: all 0.3s ease-out;
  @include mq(md) {
    margin-top: rem(9);
  }
}
.p-movie__slideInner--mt {
  margin-top: rem(42);
  @include mq(md) {
    margin-top: rem(33);
  }
}
.swiper-slide-active .p-movie__slideInner {
  opacity: 1;
}
.p-movie__slideBox {
  pointer-events: none;
  position: relative;
}
.swiper-slide-active .p-movie__slideBox {
  pointer-events: initial;
  cursor: pointer;
}
.swiper-slide-active .p-movie__slideBox::after {
  opacity: 0.6;
  transform: translate(-50%, -50%) scale(1);
}
.p-movie__slideBox::after {
  position: absolute;
  display: block;
  content: "";
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%) scale(0.2);
  width: rem(100);
  height: rem(100);
  pointer-events: none;
  background: no-repeat center url(../images/common/pray_btn.svg);
  background-size: contain;
  pointer-events: none;
  opacity: 0;
  transition: 0.4s;
  @include mq(md) {
    width: rem(50);
    height: rem(50);
  }
}
.swiper-slide.swiper-slide-active .p-movie__slideInner.play .p-movie__slideBox::after {
  opacity: 0;
}

.p-movie__swiperWrap {
  position: relative;
  overflow: hidden;
  padding-bottom: 1px;
}
.p-movie__swiperWrap .youtube_swiper {
  position: relative;
  overflow: visible;
}
.p-movie__btn {
  position: absolute;
  top: 56%;
  left: 50%;
  transform: translate(-50%, -50%);
  display: block;
  width: 100%;
  height: auto;
  text-align: end;
  @include mq(md) {
    position: static;
    transform: none;
    text-align: center;
    padding-top: rem(83);
  }
}
.swiper-pagination.swiper-pagination-bullets.swiper-pagination-horizontal {
  position: absolute;
  top: 50%;
  left: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  width: fit-content;
  transform: translate(-50%, -50%);
  height: rem(14);
  margin: 0 auto;
  cursor: pointer;
  @include mq(md) {
    top: 30%;
  }
}

.p-movie__controller .swiper-button-prev,
.p-movie__controller .swiper-button-next {
  top: 50%;
  margin-top: 0;
  display: block;
  width: rem(50);
  height: rem(50);
  transition: all 0.3s ease-out;
  @include mq(md) {
    top: 30%;
  }
}

.p-movie__controller .swiper-button-prev::before,
.p-movie__controller .swiper-button-prev::after,
.p-movie__controller .swiper-button-next::before,
.p-movie__controller .swiper-button-next::after {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  display: block;
  width: rem(15);
  height: rem(19);
  mask-image: url(../images/common/mark_next_b.svg);
  mask-repeat: no-repeat;
  mask-size: contain;
  mask-position: center;
  transition: all 0.3s ease-out;
}
.p-movie__controller .swiper-button-prev::before,
.p-movie__controller .swiper-button-next::before {
  background: #333;
  opacity: 1;
}
.p-movie__controller .swiper-button-prev::after,
.p-movie__controller .swiper-button-next::after {
  background: linear-gradient(180deg, #6895fd 0%, #e36a7b 100%) border-box border-box;
  opacity: 0;
}
.p-movie__controller .swiper-button-prev {
  transform: translate(-50%, -50%) scale(-1, 1);
  left: calc(50% - rem(110));
  @include mq(md) {
    left: calc(50% - rem(80));
  }
}
.p-movie__controller .swiper-button-next {
  transform: translate(-50%, -50%);
  left: calc(50% + rem(110));
  @include mq(md) {
    left: calc(50% + rem(80));
  }
}
.p-movie__controller .swiper-button-prev:hover::before,
.p-movie__controller .swiper-button-prev:hover::after,
.p-movie__controller .swiper-button-next:hover::before,
.p-movie__controller .swiper-button-next:hover::after {
  transform: translate(-20%, -50%);
}
.p-movie__controller .swiper-button-prev:hover::before,
.p-movie__controller .swiper-button-next:hover::before {
  opacity: 0;
}
.p-movie__controller .swiper-button-prev:hover::after,
.p-movie__controller .swiper-button-next:hover::after {
  opacity: 1;
}
.swiper-pagination-horizontal.swiper-pagination-bullets .swiper-pagination-bullet {
  margin: 0 rem(8);
  @include mq(md) {
    margin: 0 rem(5);
  }
}
.swiper-pagination-bullet {
  width: rem(10);
  height: rem(10);
  @include mq(md) {
    width: rem(8);
    height: rem(8);
  }
}
.swiper-pagination .swiper-pagination-bullet {
  background: var(--numColor);
  border: 0;
  opacity: 1;
  position: relative;
}
.swiper-pagination .swiper-pagination-bullet.swiper-pagination-bullet-active {
  position: relative;
  background: linear-gradient(180deg, #6895fd 0%, #e36a7b 100%) border-box border-box;
}
.swiper-pagination .swiper-pagination-bullet.swiper-pagination-bullet-active::before {
  content: "";
  width: rem(17);
  height: rem(17);
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  border-radius: 50%;
  z-index: -1;
  border: 1px solid transparent;
  background: linear-gradient(270deg, #6895fd 0%, #e36a7b 100%) border-box border-box;
  @include mq(md) {
    width: rem(15);
    height: rem(15);
  }
}
.swiper-pagination .swiper-pagination-bullet.swiper-pagination-bullet-active::after {
  content: "";
  border-radius: 50%;
  width: calc(rem(17) - 2px);
  height: calc(rem(17) - 2px);
  background: #333;
  position: absolute;
  z-index: -1;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  @include mq(md) {
    width: calc(rem(15) - 2px);
    height: calc(rem(15) - 2px);
  }
}
```