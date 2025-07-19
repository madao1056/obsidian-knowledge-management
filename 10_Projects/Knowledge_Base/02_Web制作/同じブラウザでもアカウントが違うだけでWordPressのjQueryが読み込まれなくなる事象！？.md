---
notion_id: 0a1496eb-3379-4d19-ae4f-f374730aa048
account: Secondary
title: 同じブラウザでもアカウントが違うだけでWordPressのjQueryが読み込まれなくなる事象！？
url: https://www.notion.so/WordPress-jQuery-0a1496eb33794d19ae4ff374730aa048
created_time: 2022-07-31T22:54:00.000Z
last_edited_time: 2022-09-01T07:03:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.473004
---
# 同じブラウザでもアカウントが違うだけでWordPressのjQueryが読み込まれなくなる事象！？

### 解決策
functions.phpのcssやjavascriptを読み込むところに以下の一文を追加するだけ。無事に確認できました。
なぜこのようなことが起きたのかははっきりとは変わりませんが、しっかりと明記してあげないといけないのかな〜という感じです。
**CodeUpsで配布されているものには記載ありません。
**今まで私も不自由なく使っていたんですが、今回初めてこんな現象に遭遇しましたので共有します。
```php
wp_enqueue_script("jquery");
```
### 作業環境
Mac book Pro
### 使用ブラウザ
Chrome
### 作業内容
静的コーディング（制作会社仕様）をWordPress化するためにローカル環境で作業→テスト環境にアップ
### エラー内容
作業中は特に問題なくローカル環境でWordPressが正常に表示されていた。
しかし、別アカ（ゲストモード）で開くと、なぜか画表示崩れ（気づいたのはテスト環境に上げて先方に確認を取ってもらう段階、確認してみると、ローカルでも別アカ時は表示崩れを起こしていた）。
ん〜？と思い、検証ツールでConsoleを見ると、以下のスクショ。
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/d58fe38c-a9d4-4466-aed9-85604b7b2c6d/c88775aa-1dd3-411e-b4d6-ada6c1824b29/_2022-08-01_7.54.10.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q65UE4HM%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T064805Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCazCu3b%2F4Ww67c0LC997YAIpWQ%2FBwYpCR0E5ILjxwaCQIgYLNbAy6dtFRYnMf7EyzIHKPaH3IKTJnJA11HeQse7NkqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCHH26E9CCs05KID6CrcA8G0DI2pIlq8Ab2B9PZtZRi6dQFcJL5pnKa45skV2qiZmjdr72VbzsyXi7PQMSYdl4l2HWfyTdTzB6g8CdT9BQqEHgyEocxWEr4CVuVu%2BoxJhtTs0w7inODyT%2BeK4s3IW%2B9ICpZxeRp6cSDqMl%2BAn1AUyuX00BbnyTVyjMBRd0JLCkJTfh8tqwTOh%2BCMvvhtGVhW0HkGKiHqXVv4nYPWijNOwOYKq0YFU%2BWTAeZLHf2kD7RoN4qMgxNHI%2BHHmQTL3k%2F%2BJcW3MBjzljkWWyVgRmaptDR4HSxlsKuWWaQt9KJ1ddvsg2BK%2FGsXYA8%2FbIZwTl60Xre2sDON0tIGk6NCXhrw%2BurqhmPoWq%2BnPiiWT%2FfeZAI34k9xWs5NNZrc66WP4XGqrLZQXZte9OmuBoxAnO6Kggy7dWWaMkGMC8AaZt%2B360%2BDDuTsPfwOw3aHwMtImWkvydkRWfEu6lJuj5GmS1igFpNteCo0EPHHmRFYQJ%2BKJa2dMLLcVrky7iozcHfZxtruLcylx7PYVKgjq823krHCq4tfxnvS1fIWCHirLx9TpR0d0cCajnxMjTAy%2FxzQ4trhLBi2KkBQy4WYSmCW142fS%2FJtGkwfGWB2cSEJOJOSO2eumxkSWepAgS3BMMbF7MMGOqUBgqPovcxALf9WF0bga2RBGkUYbsYBiD08qtlWxDCsgbUYsfowEWGFrXMotYGVls3PC4LYu6kKhFzopdg8A6HnNj1h6GnzPIBhDf78jAMepl6Vl2IC6ec0JkJYHEJUNacN6PSU86TR2uS%2BEsJxnq8c%2Fa%2BvuxUsENNXuCfIYa0RFUttiZnd%2FB2QZAzsgB7iTsRSxM8MjzSd6kSqvCFBfTi3Z6pXIUwe&X-Amz-Signature=2920c6976297bbca047f5bf3a8bb23fef369828ededf2b27d8caf29b186eda6a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
jQueryが読み込まれていない！？作業中はなんとも無かったのに・・・？
WordPressって標準で読み込まれるんじゃないの？と思っていたが、functions.phpにちゃんと読み込んでねというコードを書く必要があるみたい。
[Bookmark](https://wp-load.in/wordpress/wordpress-jquery-loading)
- 上記参考サイト引用スクショ
  ![](https://prod-files-secure.s3.us-west-2.amazonaws.com/d58fe38c-a9d4-4466-aed9-85604b7b2c6d/f7eb6a04-2ea4-42b4-96c7-a27f34d6bd5d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZKXCYID%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T064805Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIES2kNKynHyrx9diQYtYs5zIzxeUBmhdgUSj8C80dyXxAiEAnLmNLQqT%2B7Q5LfILZka5JjqLK4Xzmg15DjtKl8Os14EqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCbyRlMpfP7m8FySWyrcA439wM5P%2FChwBZQ55HhSE8xdXIGirJBS6QPwmK6yiZCFU5yZjJlgvhX0nPA7GbM%2B8NOMbyAcGffqbgXYtqAKLdvujPyZbpkk%2BOZw4Zcsq3DuGamoXvbr%2BnvbgLHRYYqCTRj9F0BjSEm%2FlmhB%2FxxFVh2B%2FOSYShnCH%2BFaKFZ%2FVYhgpoCPFZl%2BvNsYhf%2FOevi1Nj0cKuQ8ESnn6bCB8Aph7n%2ByHKiabnWNgS2essvATtDCjUsY5Vnbi2qhEq0AcLGreCy1wkf4z%2B1Ylv%2FBqo1J5yyV%2FmcRJSs13J5Foyl6Tyvxg6AdCeEzM9%2Fwow6OsHYLhKPXa3UApaCG1rUsQz3mggX6XkvQW8A75K7ITWQZIGJzvqYidsR79%2BJBT0qXWzFtm3fFecOs5%2BFaeKHNBJxT582zgMnVAdUqd546w%2FCImIfCJbLQ2kpdwH5xd6IOPNgPVZL9CbJ25pWgsl2EmG5bg4o3UlbT2h61qwtyosRQjQyTW1YjV1b6VkbPLvUGGrP7XKbvpTlX8hexop1EcEggmDjDPI6X5y%2FvgWVxESXkqE4FCsN%2F01zIobRq8of7OiWue1%2FiNTAJMQ5JkDD6hYP2%2BDJxFtvG555gYimb6HMLKmNqIC0KHk3x3NDkMKpkMKTF7MMGOqUB0udaOZsXBGohbQluZ711nmQF1wGzh3AJ%2FUdUXnZxccrfW6ttaTP4rHtdrCxjHV7RSQBo8yqKUlKhaMPSpAWgWw9QTMqfYsYb8GSwzZkj0WXVlsyO5hNOqzm6BLXnEfVFYY2QBMRmoNM%2Bbdq%2Fu520SQzHDdUrkNwjMNvKZvE41ATm6XXkRIScgLbhounfErvq0CZTsBf8teSDmkpCrAcE2tm%2BWOSM&X-Amz-Signature=5bd992fba4490570f3cadcf66a1654e22396684dbfc8906c823f927a9a1b82a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
### 結論
functions.phpのcssやjavascriptを読み込むところに以下の一文を追加するだけ。
```php
wp_enqueue_script("jquery");
```

## タグ

#Web制作 

## 関連ドキュメント

- [[../02_Web制作/Trym.md|Trym]]
- [[../99_その他/y.md|y]]
- [[../01_よしなに対応/グルコン.md|グルコン]]
- [[../02_Web制作/コーポレートサイト部分WP化.md|コーポレートサイト部分WP化]]
- [[../02_Web制作/✅masayukiさん.md|✅masayukiさん]]
