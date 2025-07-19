---
notion_id: f8b1e594-a138-473c-b0d3-16bb28aa5f00
account: Secondary
title: Instagram Graph API(インスタの写真を埋め込む)
url: https://www.notion.so/Instagram-Graph-API-f8b1e594a138473cb0d316bb28aa5f00
created_time: 2023-09-14T03:10:00.000Z
last_edited_time: 2023-09-14T03:11:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.419363
---
# Instagram Graph API(インスタの写真を埋め込む)

---
<details>
<summary>目次</summary>
</details>
---
2022/07/23作成→2022/07/25更新
# はじめに
- 参考にした記事
  [Bookmark](https://arrown-blog.com/instagram-graph-api/)
  **※↑参考ブログのままだと最後のサンプルコードでエラーになりました・・・もちろん解決策済み。**
## 目的
インスタグラムの情報をWebサイトに埋め込んで表示させたい！（そのためだけの情報なので枝葉の情報は無し）
- WordPress以外の実装方法
  - JavaScriptのみを使用したコード
  - JavaScriptとPHPを使用したコード
- WordPress（PHPのみ）での実装方法
## 手順を簡単に
前提→「Instagram Graph API」を使用
- 共通部分
  1. Instagramのプロアカウント（旧称：ビジネスアカウント）に変更
  1. FaceBookページを用意し、Instagramのプロアカウントと連携
  1. FaceBook開発者ページのGraph APIエクスプローラーから、アクセストークンを3段階取得（3番目のアクセストークンを使用）
  1. InstagramビジネスアカウントIDを取得
- WordPress以外（JavaScript or JavaScript&PHP）の実装方法
- WordPress（PHP）での実装方法
---
# 共通部分
## 1. Instagramのプロアカウント（旧称：ビジネスアカウント）に変更
  [Bookmark](https://arrown-blog.com/instagram-business-account/)
  １.「設定」→「プロアカウント」
  ![](https://prod-files-secure.s3.us-west-2.amazonaws.com/d58fe38c-a9d4-4466-aed9-85604b7b2c6d/ba9c7349-604e-4a85-bf51-56cea076e886/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88_2022-07-23_14.46.56.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VE5CVCK%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T060742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGLntWhf0rVEasWeCiGvA3%2F5FCyfWxJYVDyY5JQ5XtiLAiEAyKkmUHFz2XmMRfXGEKW8tT%2BmJcH8gd7eK8rc3pZwjjMqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKhqQAzp8rJuj%2BShdCrcA3kCTm5gUts24o2BqFGeR%2FjLVYSPmflEwOTofEogN4SL6PnKAAnkim6KROZrGkq4kcXJQsIMecal4%2BX7Pk%2FyuhrjEEHqWnQidJTYVNRwUaS1wA6Y0VWohzkrwcm5fRbKgVLVwh0OuD3JPTpaOFooN4gTaxy%2FQlNkBvUk%2FpygJ%2FfjyFKk683EFBGfysRIeDnsob09HRRIUGaQXrSdNDwGbx%2FjbDt05Yl3KONKekJyhQ1bof1FgWCQLXedqUEfXw95UwUSOkF%2FNXxA2GMsUlxrtpvkgyAwRUUpWBhcplRDaPYmzeh4x9jPLQxghDvwoRb4JQuto3nMGO2I2%2Blf%2BlE%2FMUsRO2Hy1iTgxJN7fcjWOmrAuU9BrVvzbYp13My6YvAvMdynOEWLIMFjPOPMT4DSHJPilG46D7uSPuMjSagpEPLygSbjW98dUwt3GwnfixE80ospg%2BkuipB3RAGW%2BdyaTBj5HvDriq8obdums%2BAxZe0FdEsBQGjfGjDAf2lAGPwOHjiTtRsmRKBpLF2RWbZJDrCxCFz7nuwqeSR11Nsye66ca4zDI%2F%2F0NrdUybh2Esa1rirlsdT55mxbNKUpQBbgzgMIauWQKljY6lt4DRBtDihBMGPi%2B1Xw0pncX0%2FSMOvF7MMGOqUBMSjV7z4Cjaki%2BqvPjvy4IklwYsYP8rDYtt8dFoYnzmJvE4iN8k7%2BLPaS2i2bQQGjJzgggRYk6EvWk2az%2BtmQlkaOXcXygOgjebT%2FDfbaYV94KilzjMLawOhlP9Gzo9pnNMFr5xcbfJ6qLnNHtdUc6%2FUUAFLJGUpR5U9%2Bl%2FwSFjxcj%2BudcpomIw1dlyrmuUP9F8noGyJE0ODVdmuKPeHTJXLPrqpx&X-Amz-Signature=e1837d3ae52e7ec92f8c5d0c2ff196b6814390ca79024dab1c5216c14562051c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
  ![](https://prod-files-secure.s3.us-west-2.amazonaws.com/d58fe38c-a9d4-4466-aed9-85604b7b2c6d/ff6d59ca-c2d6-49dd-920f-2eec38917bf3/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88_2022-07-23_14.49.45.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VE5CVCK%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T060742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGLntWhf0rVEasWeCiGvA3%2F5FCyfWxJYVDyY5JQ5XtiLAiEAyKkmUHFz2XmMRfXGEKW8tT%2BmJcH8gd7eK8rc3pZwjjMqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKhqQAzp8rJuj%2BShdCrcA3kCTm5gUts24o2BqFGeR%2FjLVYSPmflEwOTofEogN4SL6PnKAAnkim6KROZrGkq4kcXJQsIMecal4%2BX7Pk%2FyuhrjEEHqWnQidJTYVNRwUaS1wA6Y0VWohzkrwcm5fRbKgVLVwh0OuD3JPTpaOFooN4gTaxy%2FQlNkBvUk%2FpygJ%2FfjyFKk683EFBGfysRIeDnsob09HRRIUGaQXrSdNDwGbx%2FjbDt05Yl3KONKekJyhQ1bof1FgWCQLXedqUEfXw95UwUSOkF%2FNXxA2GMsUlxrtpvkgyAwRUUpWBhcplRDaPYmzeh4x9jPLQxghDvwoRb4JQuto3nMGO2I2%2Blf%2BlE%2FMUsRO2Hy1iTgxJN7fcjWOmrAuU9BrVvzbYp13My6YvAvMdynOEWLIMFjPOPMT4DSHJPilG46D7uSPuMjSagpEPLygSbjW98dUwt3GwnfixE80ospg%2BkuipB3RAGW%2BdyaTBj5HvDriq8obdums%2BAxZe0FdEsBQGjfGjDAf2lAGPwOHjiTtRsmRKBpLF2RWbZJDrCxCFz7nuwqeSR11Nsye66ca4zDI%2F%2F0NrdUybh2Esa1rirlsdT55mxbNKUpQBbgzgMIauWQKljY6lt4DRBtDihBMGPi%2B1Xw0pncX0%2FSMOvF7MMGOqUBMSjV7z4Cjaki%2BqvPjvy4IklwYsYP8rDYtt8dFoYnzmJvE4iN8k7%2BLPaS2i2bQQGjJzgggRYk6EvWk2az%2BtmQlkaOXcXygOgjebT%2FDfbaYV94KilzjMLawOhlP9Gzo9pnNMFr5xcbfJ6qLnNHtdUc6%2FUUAFLJGUpR5U9%2Bl%2FwSFjxcj%2BudcpomIw1dlyrmuUP9F8noGyJE0ODVdmuKPeHTJXLPrqpx&X-Amz-Signature=527f5dcd65831515f026b428b58f436b1684aa6adbcb302606baed4f3ca79d17&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
  ２.ビジネス or クリエーターアカウントの必要事項を入力。入力終えたら完了！簡単。
  住所うまく入らなかったんだけど。まぁクリーエーターで登録しとく。
  - クリエーターアカウント
  - ビジネスアカウント
## 2. **FaceBookページとInstagramビジネスアカウントを連携**
  ### 前準備
  ※これはスマホから。PCだと**[ページ]**がない
  1. Instagramプロフィールを開く
  1. **[プロフィールを編集]**を選択
  1. [ビジネスの公開情報]で、**[ページ]**を選択
  1. **[Facebookページを作成]**または**[既存ページをリンク]**をタップ
  1. リンクしたいページの中からいずれかのページを選択するか、**[新しいFacebookページを作成]**を選択
  1. ページを選択するか、新しいページを作成したら、**[完了]**をタップ
  ### 連携
  1. Instagramのビジネスアカウントと連携させたFaceBookページを開いて、「**設定**」を選択(左下)
  1. 赤枠で囲んだ箇所にある「**Instagram**」を選択
  1. すでに作成されていればここにInstagramアカウント情報が出てくる。
出てきていない場合は「**アカウントをリンク**」を選択し、
**プロアカウントにしたInstagramアカウントのIDとパスワードを使ってログイン**
  1. **FaceBookアプリを作成するために**、[FaceBook開発者ページ](https://developers.facebook.com/)にアクセスし「スタート」をクリック。手順に沿って進める
  1. **FaceBookアプリを作成する
「アプリを作成」**をクリックすると以下のページになる。アプリタイプがよくわからん！という人は[詳しくはこちら](https://developers.facebook.com/docs/development/create-an-app/app-dashboard/app-types)を参照してね
## 3.FaceBook開発者ページのGraph APIエクスプローラーから、アクセストークンを合計3回取得（3番目のアクセストークンを使用）
  [FaceBook開発者ページのGraph APIエクスプローラー](https://developers.facebook.com/tools/explorer/)にアクセス
  **アクセストークンと呼ばれる許可証のコード（英数字の文字の羅列）を****3段階に渡って取得**
  ここが少し複雑なので慎重にやっていきましょう！
  「ユーザーまたはページ」の箇所を「ユーザーアクセストークンを取得（ユーザートークン）」に選択
  <details>
  <summary>**1段階目のアクセストークンを取得**</summary>
  </details>
  <details>
  <summary>**2段階目のアクセストークンを取得**</summary>
  </details>
  <details>
  <summary>**3段階目のアクセストークンを取得**</summary>
  </details>
## 4.**InstagramビジネスアカウントIDを取得**
  - **事前確認**
  - **InstagramビジネスアカウントIDを取得**
---
# WordPress以外の実装方法
## **Instagram Graph API経由でインスタの写真をWebサイトに表示する**
### **概要**
1. JavaScriptだけで行う方法
1. PHPなどサーバサイドプログラムを使って行う方法
2つの方法があるみたいです。しか〜し！JavaScriptだけではセキュリティ的にあやしいという記事も。ここは実装環境で変わってくるのでなんとも言えないです。
### JavaScriptのみを使用したコード（[舞たけさん](https://twitter.com/maitake_web)から情報共有していただきました！）
<details>
<summary>HTML</summary>
</details>
  ```html
<div class="section">
  <div class="insta__logo">
    <span class="insta__logo-wrap">
      <span class="insta__icon">
				<img loading="lazy" src="./img/test.png" alt="Instagram">
			</span>
      <p class="insta__logo-text">Instagram</p>
    </span>
  </div>
  <ul class="insta__list js-insta__list"></ul>
</div>
  ```
<details>
<summary>JavaScript</summary>
</details>
  ```javascript
  $(function () {
    $.ajax({
      type: 'GET',
      url: 'https://graph.facebook.com/v12.0/【InstagramビジネスアカウントID】?fields=name,media .limit(6){ caption,media_url,thumbnail_url,permalink,like_count,comments_count,media_type}&access_token=【3番目のアクセストークン】', //limit()の数字は投稿取得上限数
      dataType: 'json',
      success: function (json) {
        let html = '';
        let insta = json.media.data;
        for (let i = 0; i < insta.length; i++) {
          let media_type = insta[i].media_type;
          if (insta[i].media_type == "IMAGE" || insta[i].media_type == "CAROUSEL_ALBUM") {
            html += '<li><a href="' + insta[i].permalink + '" target="_blank" rel="noopener noreferrer"><div class="insta__img"><img loading="lazy" src="' + insta[i].media_url + '"><div class="insta__imgMask"><p class="imgMask__caption"><img src="./img/nice-icon.png" alt="いいね">' + insta[i].like_count + '<img src="./img/comment-icon.png" alt="コメント">' + insta[i].comments_count + '</p></div></div></a></li>';
          } else if (media_type == "VIDEO") {
            html += '<li><a href="' + insta[i].permalink + '" target="_blank" rel="noopener noreferrer"><div class="insta__img"><img loading="lazy" src="' + insta[i].thumbnail_url + '"><div class="insta__imgMask"><span class="insta__videoIcon"><img src="./img/video-icon.png" alt="動画"></span><p class="imgMask__caption"><img src="./img/nice-icon.png" alt="いいね">' + insta[i].like_count + '<img src="./img/comment-icon.png" alt="コメント">' + insta[i].comments_count + '</p></div></div></a></li>';
            let media_type = '';
          }
        }
        $(".js-insta__list").append(html);
      },
      error: function () {
        $(".js-insta__list").append("<p>データが見つかりません</p>"); //読み込めなかったときの処理
      }
    });
  });
  ```
<details>
<summary>CSS（適宜修正してね）</summary>
</details>
  ```css
/*インスタグラム
------------------------------------------*/
/* logo */
.section{
	position:relative;
	height:0;
	padding-bottom:calc(67% + 55px)
}

.insta__logo {
  position: relative;
  background: #fff;
}

.insta__logo:before {
  position: absolute;
  top: calc(50% - 2px);
  left: 0;
  width: 100%;
  height: 4px;
  content: '';
  background: -webkit-linear-gradient(120deg, #427eff 0%, #f13f79 70%) no-repeat;
  background: linear-gradient(120deg, #427eff 0%, #f13f79 70%) no-repeat;
}

.insta__logo-wrap {
  width: fit-content;
  margin: 0 auto;
  padding: 0 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  line-height: 1;
  position: relative;
  background: #fff;
}

.insta__icon {
  width: 30px;
  height: 30px;
  margin-right: 10px;
}

.insta__icon img {
  width: 100%;
  height: 100%;
}

.insta__logo-text {
  font-size: 1.8em;
  font-family: YuMincho, "Yu Mincho", "Hiragino Mincho ProN", "serif";
  font-weight: bold;
  transform: translateY(3px);
  margin: 0;
}

/* list */
.insta__list a {
  text-decoration: none;
}

.insta__list {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-auto-rows: 1fr;
  grid-gap: 2.5vw;
}

/* img */
.insta__img {
  width: 100%;
  height: 0;
  padding-bottom: 100%;
  border-radius: 6px;
  overflow: hidden;
  position: relative;
  border-radius: 5px;
}

.insta__list img {
  width: 100%;
}

.insta__imgMask {
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  opacity: 0;
  background-color: rgba(0, 0, 0, 0.4);
  -webkit-transition: all 0.2s ease;
  transition: all 0.2s ease;
}

.insta__img:hover .insta__imgMask {
  opacity: 1;
}

.imgMask__caption {
  display: flex;
  align-items: center;
  color: #fff;
}

.imgMask__caption img {
  width: 1.2em;
  height: 1.2em;
  margin-right: 4px;
}

.imgMask__caption img:last-child {
  margin-left: 12px;
}

.insta__videoIcon {
  position: absolute;
  top: 0;
  right: 0;
  width: 2.4em;
  height: 2.4em;
  margin-right: 8px;
}

.insta__videoIcon img {
  width: 100%;
}
  ```
### JavaScriptとPHPを使用したコード
  ファイルのディレクトリ構造
  ![](https://prod-files-secure.s3.us-west-2.amazonaws.com/d58fe38c-a9d4-4466-aed9-85604b7b2c6d/6876af9d-3882-4ff8-8fc6-9c8a98e00f78/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXFETLZ7%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T060745Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIQCrjMPIMY%2BIL7nW3CcgUF3ntI1YE0aC4rhOFp%2BeunLXGgIfWGSlfLFGYl8WcMYQ2LNfSxk%2Fiqbahz6Qwcy%2BWt%2FVgCqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZ8wrQPx6Sm4P%2FB4nKtwD4DFRMpEmdzp0akGilr3L6d6CcSHcxq%2FOMhsWTBk7VF7itaUbw%2FJXWFIRyBaLRDqAq9B11cSn9W0zb7S5Sw1rmmWJor23dKZhMhNoM%2F3pzySoot5FvyZlNxeUVyV8qMfvY1foCy67qFI1qC2PebTC08QrM93l%2F2%2FmKBENH9OZo0l5IP20njdWx%2BOhGxakU0yUVoPbuCEnlLprdE5X%2F1vIZfvtCqYhLvJAZy1PFlafffuzczsKLUr%2Fx09vonIy5Q7MReLfzDZn%2BUe6bK5WTBuPuQQczkIx1LSgO7yupTMBpzgfa1K6eru%2Fe%2FrF9Wwat3rFyWiGM1tNtzbk47GNO3O25HchrCv0WagtoYpr2oSnxUbGTNam%2FZB8tHDusM0bGxEAOIg%2BhtY1SvY5%2FGoa0ghns8Zh6xkELi3tgZqT08FTUJxjoNFgYw0JB1XZfBzmLYgmYPOAcK7E8VXtKCrO5eX49DTBZy5bdYHo5s4NjAQTO84%2F5MIOFdDR5FJciB%2BjmW%2BIPgx5FD5UuCo86giBvYLtVniWpiOgHC35yK5qGwtBJbNIfNkXXZwwVkcndfWjr1ry7ILymYXoPC38KwokeoXX0HXimOMftAL53YOm6sXUvO2vEDbLwR7mci9dacYw%2BsTswwY6pgGMRid82ooRaksa6C1TdLxfFSALHdhjlUEUALH5Wt9Mg5nR8YlKPJRMAjmpUUapCLgI4Wm2rn%2F7mgrVavE%2FK4ZYZz%2FUdQZEcIB0kT516wxixHxRbh100YxNm%2Fi7Vto2WXvH18PJvdbad9Jk8OH%2Fj9ZPAxYDDdnRDV1YuCdZrUlkovibCcS4ulYyguqRI%2FAgGGZZ5oJZnU9vLU4hKU6gwOuar2ncdcbw&X-Amz-Signature=d7bf32dc5a37aeae8759d15f8ab8adeecf070b7b2547b4d9d941a48537598d80&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
  1. Axiosを使ったInstagram Graph API経由でインスタの写真を取得するためのサンプルコード
  1. jQueryを使ったInstagram Graph API経由でインスタの写真を取得するためのサンプルコード
  PHPを使用した方法で２つの方法を紹介！したかったのですが、Axiosを使ったものはエラー解決できず・・・
  2番のjQueryを使った方法で実装していきます！
  <details>
  <summary>**jQueryを使ったInstagram Graph API経由でインスタの写真を取得するためのサンプルコード****※参考ブログと若干違います・・・**</summary>
  </details>
---
# WordPress（PHPのみ）での実装方法
- 参考記事
  [Bookmark](https://inokawablog.org/wordpress/instagram-graph-api-wordpress/)
  **※↑参考ブログからリンク飛べるようにしたり、表示数指定したりと改造してます。**
## **Instagram Graph API経由でインスタの写真をWebサイトに表示する**
<details>
<summary>コード</summary>
</details>
  <details>
  <summary>PHP</summary>
  </details>
  <details>
  <summary>CSS</summary>
  </details>
  <details>
  <summary>JavaScript(連携には関係無し：フェードイン動きの部分)</summary>
  </details>
  
# まとめ
共通部分さえクリアすれば、あとはある程度の環境ではどうにかなりそうです。またAPI経由で引き出せる情報も全部理解してるわけではないので他の情報を引っ張ってきたいならググってみましょう。
いやーAPI面白いかも。