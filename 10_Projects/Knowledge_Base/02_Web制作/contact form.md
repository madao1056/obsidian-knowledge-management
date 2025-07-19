---
notion_id: 8b17a798-2ed0-4cec-9d9e-254aad1347a9
account: Secondary
title: contact form
url: https://www.notion.so/contact-form-8b17a7982ed04cec9d9e254aad1347a9
created_time: 2022-04-01T01:43:00.000Z
last_edited_time: 2022-04-03T20:38:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.532373
---
# contact form

[Bookmark](https://terupro.net/contact-form)
```javascript
$(function() {
	/* 「同意する」チェックイベント */
	$('[type="checkbox"]').on('click', function(){
		if($('[type="checkbox"]').prop("checked")){
			$('[type="submit"]').css('background-color', 'rgb(51, 51, 255)');
		} else {
			$('[type="submit"]').css('background-color', 'rgb(102, 102, 102)');
		}
	});

	/* 「同意する」がチェックされていない場合submit=false */
	$('[type="submit"]').on('click', function(){
		if ($('[type="submit"]').css('background-color') == 'rgb(102, 102, 102)') {
			return false;
		}
	});
});
```

## タグ

#Web制作 

## 関連ドキュメント

- [[../02_Web制作/Contact Form 7.md|Contact Form 7]]
- [[../02_Web制作/エラーメッセージを項目ごとに変更.md|エラーメッセージを項目ごとに変更]]
- [[../99_その他/x.md|x]]
- [[../99_その他/y.md|y]]
