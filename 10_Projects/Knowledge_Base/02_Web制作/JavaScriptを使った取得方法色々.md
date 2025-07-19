---
notion_id: f44e979b-9ab3-4e36-8f2a-5962f38f7de9
account: Secondary
title: JavaScriptを使った取得方法色々
url: https://www.notion.so/JavaScript-f44e979b9ab34e368f2a5962f38f7de9
created_time: 2022-05-02T05:19:00.000Z
last_edited_time: 2023-12-04T15:26:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.409755
---
# JavaScriptを使った取得方法色々

- div要素クラス名’classname’の一番最初のものを取得
  ```javascript
const totoro = document.querySelector('div.classname');
totoro.style.display = "none";
  ```
- span要素クラス名’classname’全てを取得
  ```javascript
const hachi = document.querySelectorAll('span.classname');
hachi.forEach(function(value) { //取得した要素をvalueにひとつづつ代入し以下の処理を行う
        value.style.color = "red"; 
        value.style.lineHeight = "1.5"; 
    });
  ```
  ```javascript
const kuro = document.querySelectorAll('span.classname');
kuro.forEach(function(value) { //取得した要素をvalueにひとつづつ代入し以下の処理を行う
        const kuroKro = value.querySelector('label'); //span要素クラス名’classname’の中の’label’要素の一番最初のものをkuroKroに代入
        kuroKro.classList.add('hellow', 'ok', 'xxx'); //label’要素にclass'hellow', 'ok', 'xxx'を追加
    });
  ```
- 擬似要素を取得（DOMで擬似要素は操作できない）
  ```javascript
const str = getComputedStyle(document.querySelector("article"), "::before").display;
//article要素の擬似要素のcssプロパティ’display’の値を取得
  ```
- URLを取得してページごとにDOMを操作する
  ```javascript
window.onload = () => {
        let url = location.href;// URLの取得
        if (url == "https://サイトURL/page-slug/") {
        // if (url == "http://localhost:3000/") {
            const newIcon = document.querySelectorAll('.p-cards__new');
            newIcon.forEach(function (value) { 
                value.style.display = "flex";
            });
        }
    }
  ```