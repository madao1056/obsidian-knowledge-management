---
notion_id: cf156a68-aa19-457c-b28d-a6e96c95309c
account: Secondary
title: WordPressキャッシュ対策
url: https://www.notion.so/WordPress-cf156a68aa19457cb28da6e96c95309c
created_time: 2023-08-02T14:06:00.000Z
last_edited_time: 2023-08-17T02:26:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.427530
---
# WordPressキャッシュ対策

---
### 🔹背景
- テストサイトの確認時にcssファイルやjsファイルを更新した際に、キャッシュが残っていて、スーパーリロード（キャッシュクリア）をしないと見れない。
- スーパーリロードやキャッシュクリアと伝えてもその言葉を知らない人もいるため、いちいち「Command＋Shift+R」をさせないといけない。
---
### 🔹考え方
- スーパーリロードをすること自体、お相手に手間がかかるし、それを伝えるのも手間になる
- 更新した時に通常のリロードで変わる方法がある。
- ファイルを読み込む関数（wp_enqueue_style,wp_enqueue_script)のバージョンを常に更新する
- [wp_enqueue_styleとwp_enqueue_scriptについて](https://wemo.tech/205)
---
### 🔹実装方法
### 🔹コード
```php
//その日の日付を秒数まで出力してくれるコード
date("ymdHis", filemtime( get_stylesheet_directory().'/style.css'))
```
```php
//使用例）styles.cssに対して
//バージョンを管理する第4引数（'1.0.1'）に上記コードを記述。
//パス（get_stylesheet_directory().'/style.css'）は第2引数と合わせること
//wp_enqueue_style( $handle(第1引数), $src(第2引数), $deps(第3引数), $ver(第4引数), $media(第5引数) )


//Before
wp_enqueue_style('my', get_template_directory_uri() . '/assets/css/styles.css', array(), **'1.0.1'**, 'all');

//After
wp_enqueue_style('my', get_template_directory_uri() . '/assets/css/styles.css', array(), **date("ymdHis", filemtime(get_stylesheet_directory() . '/assets/css/styles.css'))**, 'all');
```

## タグ

#Web制作 

## 関連ドキュメント

- [[../02_Web制作/菱田さま　先方FB修正.md|菱田さま　先方FB修正]]
- [[../02_Web制作/株式会社season2様コーポレートサイト.md|株式会社season2様コーポレートサイト]]
- [[../02_Web制作/営業文添削用.md|営業文添削用]]
- [[../02_Web制作/Brain購入特典.md|Brain購入特典]]
- [[../02_Web制作/管理画面の「投稿」名を変更したり、使わないカテゴリーやタグを非表示にする.md|管理画面の「投稿」名を変更したり、使わないカテゴリーやタグを非表示にする]]
