---
notion_id: c875c1bf-4fd3-4dd0-8b81-eba15fe90db4
account: Main
title: WebGLのアニメーション
url: https://www.notion.so/WebGL-c875c1bf4fd34dd08b81eba15fe90db4
created_time: 2023-01-19T05:50:00.000Z
last_edited_time: 2023-10-14T06:25:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:15.081311
---
# WebGLのアニメーション

**望んでいる実装**
MV　3枚の画像のアニメーション　（TweenMaxとthree.jsを使用）
- 次スライドへのアニメーションは参考サイト3と同じようにする。
- レスポンシブ時も同じ画像で、画面からはみ出した分は見切れるよう実装したい。
（object-fit: cover;を効かせたい）
**現状**
- object-fit: cover; が効かず、画面幅を狭めると画像が縮んでしまう。
- shopify 側のLiquidでの高さや幅の設定の原因と切り分けるため、いったん静的で検証。
　以下ソースコードのように静的な時点で　object-fit:cover;が既に効いていない状態です。
　そのため、まずJSやCSSに問題があると考えました。

　静的コーディング段階でobject-fit:cover;　が効いている
　→　shopifyだと効かない
　という状態であれば、おっしゃるとおりLiquidでの幅指定などが
　原因に考えられると推察しますが今回はその以前の問題のようです。
**解決できたコード：**
<details>
<summary>html</summary>
</details>
  ```javascript
<!--head内　読み込み-->

<!-- JavaScript -->
  <script src="https://code.jquery.com/jquery-3.6.0.js"></script>
  <script defer src="./js/script.js"></script>
<!-- TweenMaxとthree.jsを読み込み -->
  <script src='https://cdnjs.cloudflare.com/ajax/libs/gsap/2.1.3/TweenMax.min.js'></script>
  <script src='https://cdnjs.cloudflare.com/ajax/libs/three.js/109/three.min.js'></script>
  ```
  ```html
<!-- test -->
  <div class="wapper_img">
    <div class="slider js-slider">
      <div class="slider__inner js-slider__inner">
      </div>
      <div class="slide js-slide"></div>
      <div class="slide js-slide"></div>
      <div class="slide js-slide"></div>
      <nav class="slider__nav js-slider__nav">
        <div class="slider-bullet js-slider-bullet">
          <span class="slider-bullet__text js-slider-bullet__text">01</span>
          <span class="slider-bullet__line js-slider-bullet__line"></span>
        </div>
        <div class="slider-bullet js-slider-bullet">
          <span class="slider-bullet__text js-slider-bullet__text">02</span>
          <span class="slider-bullet__line js-slider-bullet__line"></span>
        </div>
        <div class="slider-bullet js-slider-bullet">
          <span class="slider-bullet__text js-slider-bullet__text">03</span>
          <span class="slider-bullet__line js-slider-bullet__line"></span>
        </div>
      </nav>
      <div class="scroll js-scroll">Scroll</div>
    </div>
  </div>
  <!-- //test -->
  ```
<details>
<summary>css</summary>
</details>
  ```css
.wapper_img .slider {
    height: 600px;
		width:100%;
  }
.slider__nav.js-slider__nav,
.scroll {
  display: none;
}
.slider__inner{
  height: 600px !important;
  position: relative;
}

.slider canvas{
    object-fit: cover;
    height: 100% !important;
    width: auto !important;
    object-position: center;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%,-50%) scale(1);
    text-align: center;
}
  ```
<details>
<summary>js</summary>
</details>
  ```javascript
jQuery(function ($) { // この中であればWordpressでも「$」が使用可能になる

  // test sectionの　animation
  class Slider {
    constructor() {
      this.bindAll()
      
      this.vert = `
      varying vec2 vUv;
      void main() {
        vUv = uv;
        gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
      }
      `
  
      this.frag = `
      varying vec2 vUv;
  
      uniform sampler2D texture1;
      uniform sampler2D texture2;
      uniform sampler2D disp;
  
      uniform float dispPower;
      uniform float intensity;
  
      uniform vec2 size;
      uniform vec2 res;
  
      vec2 backgroundCoverUv( vec2 screenSize, vec2 imageSize, vec2 uv ) {
        float screenRatio = screenSize.x / screenSize.y;
        float imageRatio = imageSize.x / imageSize.y;
        vec2 newSize = screenRatio < imageRatio 
            ? vec2(imageSize.x * (screenSize.y / imageSize.y), screenSize.y)
            : vec2(screenSize.x, imageSize.y * (screenSize.x / imageSize.x));
        vec2 newOffset = (screenRatio < imageRatio 
            ? vec2((newSize.x - screenSize.x) / 2.0, 0.0) 
            : vec2(0.0, (newSize.y - screenSize.y) / 2.0)) / newSize;
        return uv * screenSize / newSize + newOffset;
      }
  
      void main() {
        vec2 uv = vUv;
        
        vec4 disp = texture2D(disp, uv);
        vec2 dispVec = vec2(disp.x, disp.y);
        
        vec2 distPos1 = uv + (dispVec * intensity * dispPower);
        vec2 distPos2 = uv + (dispVec * -(intensity * (1.0 - dispPower)));
        
        vec4 _texture1 = texture2D(texture1, distPos1);
        vec4 _texture2 = texture2D(texture2, distPos2);
        
        gl_FragColor = mix(_texture1, _texture2, dispPower);
      }
      `
      
      this.el = document.querySelector('.js-slider')
      this.inner = this.el.querySelector('.js-slider__inner')
      this.slides = [...this.el.querySelectorAll('.js-slide')]
      this.bullets = [...this.el.querySelectorAll('.js-slider-bullet')]
      
      this.renderer = null
      this.scene = null
      this.clock = null
      this.camera = null
      
      //画像3枚の設定
      this.images = [
        'https://s3-us-west-2.amazonaws.com/s.cdpn.io/58281/bg1.jpg',
      　'https://s3-us-west-2.amazonaws.com/s.cdpn.io/58281/bg2.jpg',
      　'https://s3-us-west-2.amazonaws.com/s.cdpn.io/58281/bg3.jpg'
      ]
      
      this.data = {
        current: 0,
        next: 1,
        total: this.images.length - 1,
        delta: 0
      }
      
      this.state = {
        animating: false,
        text: false,
        initial: true
      }
      
      this.textures = null
      
      this.init()
    }
    
    bindAll() {
      ['render', 'nextSlide']
      .forEach(fn => this[fn] = this[fn].bind(this))
    }
    
    setStyles() {
      this.slides.forEach((slide, index) => {
        if (index === 0) return
        
        TweenMax.set(slide, { autoAlpha: 0 })
      })
      
      this.bullets.forEach((bullet, index) => {
        if (index === 0) return
        
        const txt = bullet.querySelector('.js-slider-bullet__text')
        const line = bullet.querySelector('.js-slider-bullet__line')
        
        TweenMax.set(txt, {
          alpha: 0.25
        })
        TweenMax.set(line, {
          scaleX: 0,
          transformOrigin: 'left'
        })
      })
    }
    
    cameraSetup() {
      this.camera = new THREE.OrthographicCamera(
        this.el.offsetWidth / -2,
        this.el.offsetWidth / 2,
        this.el.offsetHeight / 2,
        this.el.offsetHeight / -2,
        1,
        1000
      )
  
      this.camera.lookAt(this.scene.position)
      this.camera.position.z = 1
    }
  
    setup() {
      this.scene = new THREE.Scene()
      this.clock = new THREE.Clock(true)
      
      this.renderer = new THREE.WebGLRenderer({ alpha: true })
      this.renderer.setPixelRatio(window.devicePixelRatio)
      this.renderer.setSize(this.el.offsetWidth, this.el.offsetHeight)
　　　　this.renderer.setSize(2600, 1712)
      
      this.inner.appendChild(this.renderer.domElement)
    }
    
    loadTextures() {
      const loader = new THREE.TextureLoader()
      loader.crossOrigin = ''
      
      this.textures = []
      this.images.forEach((image, index) => {
        const texture = loader.load(image + '?v=' + Date.now(), this.render)
        
        texture.minFilter = THREE.LinearFilter
        texture.generateMipmaps = false
        
        if (index === 0 && this.mat) {
          this.mat.uniforms.size.value = [
            texture.image.naturalWidth,
            texture.image.naturalHeight
          ]
        }
  
        this.textures.push(texture)
      })
      
      this.disp = loader.load('https://s3-us-west-2.amazonaws.com/s.cdpn.io/58281/rock-_disp.png', this.render)
      this.disp.magFilter = this.disp.minFilter = THREE.LinearFilter
      this.disp.wrapS = this.disp.wrapT = THREE.RepeatWrapping
    }
    
    createMesh() {
      this.mat = new THREE.ShaderMaterial( {
        uniforms: {
          dispPower: { type: 'f', value: 0.0 },
          intensity: { type: 'f', value: 0.5 },
          res: { value: new THREE.Vector2(window.innerWidth, window.innerHeight) },
          size: { value: new THREE.Vector2(1, 1) },
          texture1: { type: 't', value: this.textures[0] },
          texture2: { type: 't', value: this.textures[1] },
          disp: { type: 't', value: this.disp }
        },
        transparent: true,
        vertexShader: this.vert,
        fragmentShader: this.frag
      })
  
      const geometry = new THREE.PlaneBufferGeometry(
        this.el.offsetWidth, 
        this.el.offsetHeight, 
        1
      )
      
      const mesh = new THREE.Mesh(geometry, this.mat)
  
      this.scene.add(mesh)    
    }
    
    transitionNext() {
      TweenMax.to(this.mat.uniforms.dispPower, 2.5, {
        value: 1,
        ease: Expo.easeInOut,
        onUpdate: this.render,
        onComplete: () => {
          this.mat.uniforms.dispPower.value = 0.0
          this.changeTexture()
          this.render.bind(this)
          this.state.animating = false
        }
      })
      
      const current = this.slides[this.data.current]
      const next = this.slides[this.data.next]
      
      const currentImages = current.querySelectorAll('.js-slide__img')
      const nextImages = next.querySelectorAll('.js-slide__img')
      
      const currentText = current.querySelectorAll('.js-slider__text-line div')
      const nextText = next.querySelectorAll('.js-slider__text-line div')
      
      const currentBullet = this.bullets[this.data.current]
      const nextBullet = this.bullets[this.data.next]
      
      const currentBulletTxt = currentBullet.querySelectorAll('.js-slider-bullet__text')
      const nextBulletTxt = nextBullet.querySelectorAll('.js-slider-bullet__text')
      
      const currentBulletLine = currentBullet.querySelectorAll('.js-slider-bullet__line')
      const nextBulletLine = nextBullet.querySelectorAll('.js-slider-bullet__line')
      
      const tl = new TimelineMax({ paused: true })
      
      if (this.state.initial) {
        TweenMax.to('.js-scroll', 1.5, {
          yPercent: 100,
          alpha: 0,
          ease: Power4.easeInOut
        })
        
        this.state.initial = false
      }
      
      tl
      .staggerFromTo(currentImages, 1.5, {
        yPercent: 0,
        scale: 1
      }, {
        yPercent: -185,
        scaleY: 1.5,
        ease: Expo.easeInOut
      }, 0.075)
      .to(currentBulletTxt, 1.5, {
        alpha: 0.25,
        ease: Linear.easeNone
      }, 0)
      .set(currentBulletLine, {
        transformOrigin: 'right'
      }, 0)
      .to(currentBulletLine, 1.5, {
        scaleX: 0,
        ease: Expo.easeInOut
      }, 0)
      
      if (currentText) {
        tl
        .fromTo(currentText, 2, {
          yPercent: 0
        }, {
          yPercent: -100,
          ease: Power4.easeInOut
        }, 0)  
      }
      
      tl
      .set(current, {
        autoAlpha: 0
      })
      .set(next, {
        autoAlpha: 1
      }, 1)
      
      if (nextText) {
        tl
        .fromTo(nextText, 2, {
          yPercent: 100
        }, {
          yPercent: 0,
          ease: Power4.easeOut
        }, 1.5)  
      }
      
      tl
      .staggerFromTo(nextImages, 1.5, {
        yPercent: 150,
        scaleY: 1.5
      }, {
        yPercent: 0,
        scaleY: 1,
        ease: Expo.easeInOut
      }, 0.075, 1)
      .to(nextBulletTxt, 1.5, {
        alpha: 1,
        ease: Linear.easeNone
      }, 1)
      .set(nextBulletLine, {
        transformOrigin: 'left'
      }, 1)
      .to(nextBulletLine, 1.5, {
        scaleX: 1,
        ease: Expo.easeInOut
      }, 1)
      
      tl.play()
    }
    
    prevSlide() {
      
    }
    
    nextSlide() {
      if (this.state.animating) return
      
      this.state.animating = true
      
      this.transitionNext()
      
      this.data.current = this.data.current === this.data.total ? 0 : this.data.current + 1
      this.data.next = this.data.current === this.data.total ? 0 : this.data.current + 1
    }
    
    changeTexture() {
      this.mat.uniforms.texture1.value = this.textures[this.data.current]
      this.mat.uniforms.texture2.value = this.textures[this.data.next]
    }

    listeners() {
       //window.addEventListener('wheel', this.nextSlide, { passive: true })
    　　//wheelでスライドではなく、5秒ごとにスライドに変更
        setInterval(this.nextSlide, 5000, { passive: true });
      }
    
    render() {
      this.renderer.render(this.scene, this.camera)
    }
    
    init() {
      this.setup()
      this.cameraSetup()
      this.loadTextures()
      this.createMesh()
      this.setStyles()
      this.render()
      this.listeners()
    }
  }
  
  // Toggle active link
  const links = document.querySelectorAll('.js-nav a')
  
  links.forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault()
      links.forEach(other => other.classList.remove('is-active'))
      link.classList.add('is-active')
    })
  })
  
  // Init classes
  const slider = new Slider()


});
  ```
実装参考サイト：
[参考サイト1](https://codepen.io/ReGGae/pen/bmyYEj)
[参考サイト2](https://kohimoto.com/labo/study/5016/)
同じようなアニメーションの参考サイト：
こちらでは、canvasタグに「object-fit: cover;」があたる。
→　画面幅を狭めても画像が見切れて、縮まない。
[参考サイト3](https://feel.kiyomizudera.or.jp/)

## タグ

#Web制作 

## 関連ドキュメント

- [[../02_Web制作/参考サイト.md|参考サイト]]
- [[../02_Web制作/テーマについて.md|テーマについて]]
- [[../02_Web制作/生活科学研究所.md|生活科学研究所]]
- [[../02_Web制作/ハラポンさん案件.md|ハラポンさん案件]]
- [[../02_Web制作/YouTube文字起こし（営業文について、濃縮還元）.md|YouTube文字起こし（営業文について、濃縮還元）]]
