---
notion_id: 0c21ea03-9c08-47c6-a734-216ab94e1b7e
account: Secondary
title: Youtubeの埋め込みをAPIで制御する
url: https://www.notion.so/Youtube-API-0c21ea039c0847c6a734216ab94e1b7e
created_time: 2023-07-27T04:49:00.000Z
last_edited_time: 2024-05-07T06:18:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.395116
---
# Youtubeの埋め込みをAPIで制御する

全体説明動画
参考画像
---
### 🔹背景
- キービジュアルにYouTubeを埋め込んで表示させたい
- 動画終了時の関連動画のままで止まってしまうので、見た目が悪くなるのをなんとかしたい
---
### 🔹考え方
- YouTubeAPIを使って、自動再生、再生後のサムネイル表示、サムネイルをクリックしたときにまた再生されるようにJavaScriptを使ってYouTubeを操作できるようにする。
---
### 🔹実装方法
1. 動画もつける
### 🔹コード
```php
<div class="p-kv">
  <div class="p-kv__movie">
<!-- id="player"要素の中にYouTubeを入れる -->
		<div id="player"></div>
<!-- id="customThumbnailContainer"要素を動画が終わったら表示させる、JSの方でクリックしたら動画が再生される -->
	  <div id="customThumbnailContainer">
	    <img id="customThumbnailImage" src="<?php echo get_template_directory_uri() ?>/assets/images/common/thumbnail.webp" alt="Thumbnail">
		</div>
	</div>
</div>
```
```sass
.p-kv__movie {
  height: fit-content;
  width: 100%;
  margin: 0 auto;
  position: relative;
}
#customThumbnailContainer {
  position: absolute;
  top: 0;
  left: 0;
  display: none;
  width: 100%;
  height: auto;
  aspect-ratio: 16/9;
  object-fit: cover;
}

#customThumbnailImage {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
```
```javascript
// ==========
// youtube KV
// ==========
$(function () {
  var w = $(window).width()
  var h = $(window).height()
  var tag = document.createElement('script');
  tag.src = "https://www.youtube.com/iframe_api";
  var firstScriptTag = document.getElementsByTagName('script')[0];
  firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
  var player;
  window.onYouTubeIframeAPIReady = function () {
    player = new YT.Player('player', {
      width: w,
      height: h,
      videoId: 'youtubeID',
      playerVars: {
        autoplay: 1,
      },
      events: {
        'onReady': onPlayerReady,
        'onStateChange': onPlayerStateChange
      }
    });
  }
  function onPlayerReady(event) {
    event.target.setVolume(0);
  }
  function onPlayerStateChange(event) {
    if (event.data === YT.PlayerState.ENDED) {
      displayCustomThumbnail();
    }
  }
  function displayCustomThumbnail() {
    const customThumbnailContainer = document.getElementById('customThumbnailContainer');
    customThumbnailContainer.style.display = 'block';
  }
  customThumbnailContainer.addEventListener('click', function () {
    customThumbnailContainer.style.display = 'none';
    player.playVideo();
  });
});
```
```javascript
// ==========
// youtube KV ※コメント付き
// ==========

// ページが読み込まれた際に実行される関数
$(function () {
  // ウィンドウの幅と高さを取得
  var w = $(window).width()
  var h = $(window).height()

  // YouTubeのIFrame APIを読み込むためのスクリプトを生成し、ページに追加する
  var tag = document.createElement('script');
  tag.src = "https://www.youtube.com/iframe_api";
  var firstScriptTag = document.getElementsByTagName('script')[0];
  firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

  // YouTubeのプレーヤーを格納する変数
  var player;

  // YouTubeのIFrame APIの読み込みが完了したときに実行されるコールバック関数
  window.onYouTubeIframeAPIReady = function () {
    // プレーヤーを作成し、ウィンドウの幅と高さに合わせる
    player = new YT.Player('player', {
      width: w,
      height: h,
      videoId: 'youtubeID', // YouTube動画のIDを指定（実際のIDは"youtubeID"の部分に置き換える必要がある）
      playerVars: {
        autoplay: 1, // プレーヤーが読み込まれたら自動的に再生を開始
      },
      events: {
        'onReady': onPlayerReady, // プレーヤーの準備ができたときに実行されるコールバック関数
        'onStateChange': onPlayerStateChange // プレーヤーの状態が変化したときに実行されるコールバック関数
      }
    });
  }

  // プレーヤーの準備ができたときに実行されるコールバック関数
  function onPlayerReady(event) {
    // プレーヤーの音量を0に設定（無音にする）
    event.target.setVolume(0);
  }

  // プレーヤーの状態が変化したときに実行されるコールバック関数
  function onPlayerStateChange(event) {
    // 動画の再生が終了したとき（ENDED状態になったとき）にカスタムサムネイルを表示する関数を呼び出す
    if (event.data === YT.PlayerState.ENDED) {
      displayCustomThumbnail();
    }
  }

  // カスタムサムネイルを表示する関数
  function displayCustomThumbnail() {
    // カスタムサムネイルを表示するための要素を取得
    const customThumbnailContainer = document.getElementById('customThumbnailContainer');
    // カスタムサムネイルを表示するための要素を表示する（デフォルトでは非表示にしておく）
    customThumbnailContainer.style.display = 'block';
  }

  // カスタムサムネイルがクリックされたときに実行される処理
  customThumbnailContainer.addEventListener('click', function () {
    // カスタムサムネイルを非表示にする
    customThumbnailContainer.style.display = 'none';
    // プレーヤーを再生する
    player.playVideo();
  });
});
```