---
notion_id: d971aa75-dedf-4103-a5c4-aaa51b79a39c
account: Secondary
title: インスタのAPI連携(インスタから画像を出力)
url: https://www.notion.so/API-d971aa75dedf4103a5c4aaa51b79a39c
created_time: 2022-06-28T21:09:00.000Z
last_edited_time: 2022-06-28T21:10:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.488402
---
# インスタのAPI連携(インスタから画像を出力)

CSSは調整してね
```javascript
jQuery(function ($){
  let list = '';
  const limit = 5; //表示件数
  const accessToken = ''; // アクセストークン
const businessID = ''; //instagram_business_accountのID
 const url = `https://graph.facebook.com/v10.0/${businessID}?fields=name,media.limit(${limit}){caption,media_url,thumbnail_url,permalink,like_count,comments_count,media_type}&access_token=${accessToken}`;
  $.ajax({
    url: url
  }).done((res)=> {
    const data = res.media;
    $.each(data, function(index, val) {
      $.each(val, function(i, item) {
        console.log(item);
        if(item.media_url){
          //メディアのタイプがビデオの場合、サムネを取得
          media = (item.media_type == 'VIDEO' ? item.thumbnail_url : item.media_url);

          // 一覧を変数listに格納
          list +=
          `<li>
            <a href="${item.permalink}" target="_blank" rel="noopener">
            <img src="${media}">
            <span class="like"><i class="fa fa-heart"></i>${item.like_count}</span></a>
          </li>`;
        }
      })
    });
  $('#insta').html('<ul>'+list+'</ul>');
  }).fail(function(jqXHR, status) {
   $('#insta').html('<p>読み込みに失敗しました。</p>');
  });
});
```
```html
<div id="insta"></div>
```

## タグ

#insta').html('<ul>'+list+'</ul>'); #insta').html('<p>読み込みに失敗しました。</p>'); #Web制作 

## 関連ドキュメント

- [[../99_その他/x.md|x]]
- [[../99_その他/y.md|y]]
