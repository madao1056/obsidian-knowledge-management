---
notion_id: 9a0ef66e-e64e-460b-95a5-7f2f40ecf71c
account: Secondary
title: ダークモード実装（DartSass用）
url: https://www.notion.so/DartSass-9a0ef66ee64e460b95a57f2f40ecf71c
created_time: 2023-08-17T12:35:00.000Z
last_edited_time: 2023-08-17T12:54:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.427421
---
# ダークモード実装（DartSass用）

```javascript
// ==========
  // ダークモード
  // ==========
  var checkboxes = document.querySelectorAll('input[name=mode]');
  var savedTheme = localStorage.getItem('theme'); // ページ読み込み時に保存されたテーマを読み込む
  var savedCheckboxState = localStorage.getItem('checkboxState'); // ページ読み込み時に保存されたチェックボックスの状態を読み込む
  // ページ読み込み時に保存されたテーマを適用する
  if (savedTheme) {
    document.documentElement.setAttribute('data-theme', savedTheme);
  }
  // ページ読み込み時に保存されたチェックボックスの状態を適用する
  if (savedCheckboxState === 'checked') {
    checkboxes.forEach(function (checkbox) {
      checkbox.checked = true;
    });
  }
  checkboxes.forEach(function (checkbox) {
    checkbox.addEventListener('change', function () {
      if (this.checked) {
        trans();
        document.documentElement.setAttribute('data-theme', 'dark');
        localStorage.setItem('theme', 'dark'); // ダークモードを選択したらテーマを保存する
        localStorage.setItem('checkboxState', 'checked'); // チェックボックスの状態を保存する
      } else {
        trans();
        document.documentElement.setAttribute('data-theme', 'light');
        localStorage.setItem('theme', 'light'); // ライトモードを選択したらテーマを保存する
        localStorage.setItem('checkboxState', 'unchecked'); // チェックボックスの状態を保存する
      }
    });
  });

  let trans = () => {
    document.documentElement.classList.add('transition');
    window.setTimeout(() => {
      document.documentElement.classList.remove('transition');
    }, 1)
  }
```
```html
<div class="p-dark">
	<input class="p-dark__toggle" type="checkbox" id="switch" name="mode">
	<label for="switch">&thinsp;</label>
  <p class="p-dark__txt">color</p>
</div>
```
```scss
@use "global" as *;

@keyframes fade {
  0% {
    opacity: 0;
  }
  50% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}
//ダークモード中にページ移管した時に初動がチェックした状態に切り替わるまでの間を見えなくするために0.4秒透過させている（0.8sのうちの50％=0.4sはopacity: 0;）
.p-dark {
  opacity: 0;
  animation: fade 0.8s linear forwards;
}

input.p-dark__toggle[type="checkbox"] {
  height: 0;
  width: 0;
  visibility: hidden;
}

.p-dark__toggle + label {
  cursor: pointer;
  width: rem(47);
  height: rem(25);
  background: #d1daf0;
  border: rem(2) solid #fff;
  margin: 0 auto;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: rem(100);
  position: relative;
  @include mq(md) {
    width: rem(40);
    height: rem(20);
  }
}
.p-dark__toggle + label:before,
.p-dark__toggle + label:after {
  content: "";
  border-radius: 50%;
  position: absolute;
  top: 50%;
  transform: translate(0, -50%) rotate(-70deg);
  transition: all 0.3s ease-out;
}
.p-dark__toggle + label:after {
  left: rem(-4);
  background-image: conic-gradient(
    #d1708d 0,
    #9485cd 28%,
    #c2cbf9 28%,
    #c2cbf9 45%,
    #7f8de3 45%,
    #a78bc9 65%,
    #debfec 65%,
    #f3afcd 100%
  );
  width: rem(27);
  height: rem(27);
  @include mq(md) {
    width: rem(25);
    height: rem(25);
  }
}

html[data-theme="dark"] .p-dark__toggle + label:after {
  background-image: conic-gradient(
    #091533 0,
    #091533 28%,
    #12285c 28%,
    #12285c 45%,
    #091533 45%,
    #091533 65%,
    #12285c 65%,
    #12285c 100%
  );
}

input.p-dark__toggle:checked + label {
  background: linear-gradient(270deg, #6895fd 0%, #e36a7b 100%) border-box border-box;
}

input.p-dark__toggle:checked + label:after {
  left: calc(50% + rem(4));
}
.p-dark__toggle + label:before {
  left: rem(-6);
  background-image: conic-gradient(#fff 0%, #fff 30%, transparent 30%, transparent 58%, #fff 60%, #fff 100%);
  width: rem(31);
  height: rem(31);
  @include mq(md) {
    width: rem(29);
    height: rem(29);
    background-image: conic-gradient(#fff 0%, #fff 33%, transparent 33%, transparent 55%, #fff 57%, #fff 100%);
  }
}
html[data-theme="dark"] .p-dark__toggle + label:before {
  left: calc(50% + rem(4) - 2px);
  transform: translate(0, -50%) rotate(-250deg);
}

.p-dark__txt {
  text-transform: uppercase;
  font-size: rem(11);
  text-align: center;
  font-weight: 500;
  margin-top: rem(10);
  letter-spacing: 0.1em;
}

//ここからは_base.scssに入れた方が管理しやすいかも
html.transition,
html.transition *,
html.transition *::before,
html.transition *::after {
  transition: cubic-bezier(0.68, -0.55, 0.27, 1.55) 420ms;
  transition-delay: 0s;
}
//本来はrootだけでいけるはずだが、DartSassはうまくいかず。html:rootとしたらうまく実装できた。
//ただ、ターミナルにはvariable '--lightBg' is undefined and used without a fallbackと出る（特にエラーではなさそう）
html:root {
  --lightBtn: #475066;
  --lightBg: #fff;
  --lightColor: #232323;
  --copyColor: #4d4d4d;
  --numColor: #6b7385;
  --hColor: #091533;
  --lightBgOpacity: rgba(255, 255, 255, 0.8);
  --hoverColor: #6895fd;
}

html {
  background: var(--lightBg);
}
//必要な分だけ変数を追加
html[data-theme="dark"] {
  background: var(--lightBg);
  color: var(--lightColor);
  --lightBtn: #d1daf0;
  --lightBg: #091533;
  --lightColor: #fff;
  --copyColor: #9097a7;
  --numColor: #9097a7;
  --hColor: #95afee;
  --lightBgOpacity: rgba(0, 0, 0, 0.8);
  --hoverColor: #e36a7b;
}
```

## タグ

#debfec #091533 #4d4d4d; #475066; #f3afcd #232323; #d1708d #e36a7b; #12285c #fff #fff; #c2cbf9 #091533; #9097a7; #d1daf0; #95afee; #6b7385; #9485cd #Web制作 #6895fd; #7f8de3 #6895fd #e36a7b #a78bc9 

## 関連ドキュメント

- [[../99_その他/left.md|left]]
- [[../99_その他/height.md|height]]
- [[../99_その他/margin.md|margin]]
- [[../99_その他/top.md|top]]
- [[../99_その他/x.md|x]]
