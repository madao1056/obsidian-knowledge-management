---
notion_id: 5b7a8d39-fb6c-49ec-8d8f-eda23ad0b139
account: Secondary
title: FAQ（よくある質問）の仕様をクリアするために提案したこと
url: https://www.notion.so/FAQ-5b7a8d39fb6c49ec8d8feda23ad0b139
created_time: 2023-06-09T14:21:00.000Z
last_edited_time: 2023-06-19T08:18:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.441322
---
# FAQ（よくある質問）の仕様をクリアするために提案したこと

---
### 🔹背景
- よくある質問を以下の仕様で作りたいとの要望
  - 各項目でFAQを作れるようにしたい
  - 管理画面から大枠のジャンル・質問・回答を入力できるように
  - 回答についてはテキストカラーを変更したり、リンクを入れたりできるようにしたい
---
### 🔹考え方
- 管理画面からの入力を可能にするということで、まず浮かんだのはカスタムフィールド
  - カスタムフィールドれあれば、繰り返しフィールドでタイトルと回答を作れる。
  - ACFのプロ版にすれば繰り返しフィールドも使える
- しかし、回答の仕様（カラーの変更・リンク設置）をクリアすることができない
- 回答の仕様はまるで投稿ページや固定ページのよう…はっ！
  - 投稿を使ってできないかを考える
  - 投稿のタイトルを質問にする
  - 回答はその投稿ページの内容を反映させればなんでもできる
  - 大枠のジャンルをどうするか？
  - 投稿機能を使って、各カテゴリーごとに*foreach*文を回し、該当するカテゴリーの投稿を取得すれば表示できる
---
### 🔹参考リンク
**JavaScript参考記事**
[Bookmark](https://zenn.dev/kagan/articles/711ae425300ac5)
**details と summary タグを使うメリット参照記事**
[Bookmark](https://tiny.foto-note.com/web/details-summary/)
> **details と summary タグを使うメリット
**
  detailsとsummaryを使うと**スクリーンリーダーが開閉の状態についても読み上げ**してくれます。
また**サイト内で単語検索、ヒットしたときに、アコーディオンが開いてくれている**。
タグを使うだけで、なにもしなくても最適化されているのがスバラシですね◎
  読み上げや検索のことも考えたdetails と summary タグ、IEでは動きませんが、主要ブラウザで使用可能。
IEは滅亡したので！使いましょう。
### 🔹コード
```php
<section class="p-faq">
      <?php
      $terms = get_terms(// タクソノミー"question-ttl"のタームを取得
        'question-ttl',
        array(
          'order' => 'ASC',// 昇順（小さい順）
          'orderby' => 'term_id',//term_idで並び替え、初期値はname
        )
      );
      foreach ($terms as $term) : ?>
        <?php
        $query = new WP_Query(
          array(
            'posts_per_page' => -1,//取得する投稿数の上限値なし
            'tax_query' => array(//条件にあった記事だけ取得
              array(
                'taxonomy' => 'question-ttl',//タクソノミーを指定
                'field' => 'slug',//ターム名をスラッグで指定する
                'terms' => $term->slug, // タームごとにスラッグを配列に入れる。
              )
            ),
          )
        );
        ?>
        <?php if ($query->have_posts()) : ?>
          <!-- タームを表示 -->
          <div class="p-faq__ttlWrap">
            <p class="p-faq__ttlNum"><?php echo $term->slug; ?></p><!-- Q1とか -->
            <h2 class="p-faq__ttl"><?php echo $term->name; ?></h2><!-- カテゴリーの名前になる -->
          </div>
          <!-- タームに属する記事をループで表示 -->
          <ul class="p-faq__items">
            <?php while ($query->have_posts()) : $query->the_post(); ?>
              <li>
                <details class="js-details"><!-- アコーディオンの１塊 -->
                  <summary class="js-summary">
                    <h3 class="p-faq__question"><?php the_title(); ?><span>&thinsp;</span></h3><!-- spanタグで＋,-を操作 -->
                  </summary>
                  <div class="p-faq__answer js-content">
                    <?php the_content(); ?>
                  </div>
                </details>
              </li>
            <?php endwhile; ?>
          </ul>
        <?php else : ?>
          <p>投稿はありません。</p>
        <?php endif; ?>
      <?php endforeach; ?>
      <?php wp_reset_postdata(); ?>
    </section>
```
```scss
@use "global" as *;

.p-faq__items {
  margin-top: rem(28);

  @include mq(md) {
    margin-top: rem(15);
  }
}

.p-faq__items li + li {
  margin-top: rem(30);

  @include mq(md) {
    margin-top: rem(27);
  }
}

.p-faq__ttlWrap {
  display: flex;
  justify-content: flex-start;
}

.p-faq__ttlWrap:nth-child(n + 2) {
  margin-top: rem(60);

  @include mq(md) {
    margin-top: rem(45);
  }
}

.p-faq__ttlNum {
  color: #ee8d1e;
  font-size: rem(32);
  font-weight: 600;
  line-height: calc(40 / 32);
  position: relative;
  padding-right: rem(17);
  text-transform: uppercase;

  @include mq(md) {
    padding-right: rem(12);
    font-size: rem(27);
  }
}

.p-faq__ttlNum::after {
  content: "";
  position: absolute;
  top: rem(22);
  right: 0;
  transform: translate(100%, -50%) rotate(3deg);
  width: 0;
  height: 0;
  border-style: solid;
  border-width: rem(8) 0 rem(12) rem(12);
  border-color: transparent transparent transparent #86bfc9;
  transition: all 0.3s ease;

  @include mq(md) {
    top: rem(18);
    border-width: rem(6) 0 rem(10) rem(10);
  }
}

.p-faq__ttl {
  color: #c283b6;
  font-size: rem(32);
  line-height: calc(40 / 32);
  font-weight: 600;
  margin-left: rem(20);

  @include mq(md) {
    margin-left: rem(20);
    font-size: rem(27);
  }
}

.p-faq__items details {
  background-color: #e5f0fd;
}

.p-faq__question {
  position: relative;
  cursor: pointer;
  font-size: 1rem;
  font-weight: normal;
  padding: rem(22) rem(70) rem(22) rem(25);
  transition: all 0.5s ease;
  font-size: rem(24);
  font-weight: 600;
  line-height: calc(30 / 24);
  color: #5887bf;
  display: flex;
  justify-content: space-between;
  align-items: center;
  @include mq(md) {
    font-size: rem(22);
    padding: rem(20) rem(50) rem(20) rem(16);
  }
}
/*アイコンの＋と-*/
.p-faq__question span::before,
.p-faq__question span::after {
  content: "";
  position: absolute;
  top: 50%;
  right: rem(25);
  transform: translateY(-50%);
  width: rem(20);
  height: 3px;
  background-color: #5887bf;
  transition: all 0.3s ease;

  @include mq(md) {
    right: rem(20);
    top: rem(30);
  }
}

.p-faq__question span::before {
  transform: translateY(-50%) rotate(0deg);
}

.p-faq__question span::after {
  transform: translateY(-50%) rotate(90deg);
}

.p-faq__question span.is-opened::after {
  transform: translateY(-50%) rotate(180deg);
}

.p-faq__answer {
  word-wrap: break-word;
  overflow: hidden;//これがないとアコーディオンの挙動に違和感がでる
}
.p-faq__answer > * {
  padding: rem(10) rem(25) rem(25);//p-faq__answerに直接paddingを指定するとカクつく
}
.p-faq__answer a {
  color: #5887bf;
  text-decoration: underline;
}

.p-faq__btn {
  margin-top: rem(80);

  @include mq(md) {
    padding: 0 rem(15);
    margin-top: rem(32);
  }
}
```
```javascript
//===============
//  アコーディオン
//===============
document.addEventListener("DOMContentLoaded", () => {
  setUpAccordion();
});

/**
 * ブラウザの標準機能(Web Animations API)を使ってアコーディオンのアニメーションを制御します
 */
const setUpAccordion = () => {
  const details = document.querySelectorAll(".js-details");
  const RUNNING_VALUE = "running"; // アニメーション実行中のときに付与する予定のカスタムデータ属性の値
  const IS_OPENED_CLASS = "is-opened"; // アイコン操作用のクラス名

  details.forEach((element) => {
    const summary = element.querySelector(".js-summary");
    const content = element.querySelector(".js-content");

    summary.addEventListener("click", (event) => {
      // デフォルトの挙動を無効化
      event.preventDefault();

      // 連打防止用。アニメーション中だったらクリックイベントを受け付けないでリターンする
      if (element.dataset.animStatus === RUNNING_VALUE) {
        return;
      }

      let icon = element.children[0].children[0].children[0];
      // detailsのopen属性を判定
      if (element.open) {
        // アコーディオンを閉じるときの処理
        // アイコン操作用クラスを切り替える(クラスを取り除く)
        element.classList.toggle(IS_OPENED_CLASS);
        // アニメーションを実行
        const closingAnim = content.animate(closingAnimKeyframes(content), animTiming);
        // アニメーション実行中用の値を付与
        element.dataset.animStatus = RUNNING_VALUE;

        icon.classList.toggle(IS_OPENED_CLASS);
        // アニメーションの完了後に
        closingAnim.onfinish = () => {
          // open属性を取り除く
          element.removeAttribute("open");
          // アニメーション実行中用の値を取り除く
          element.dataset.animStatus = "";
        };
      } else {
        // アコーディオンを開くときの処理
        // open属性を付与
        element.setAttribute("open", "true");

        // アイコン操作用クラスを切り替える(クラスを付与)
        element.classList.toggle(IS_OPENED_CLASS);
        // アニメーションを実行
        const openingAnim = content.animate(openingAnimKeyframes(content), animTiming);
        // アニメーション実行中用の値を入れる
        element.dataset.animStatus = RUNNING_VALUE;

        icon.classList.toggle(IS_OPENED_CLASS);
        // アニメーション完了後にアニメーション実行中用の値を取り除く
        openingAnim.onfinish = () => {
          element.dataset.animStatus = "";
        };
      }
    });
  });
}

/**
 * アニメーションの時間とイージング
 */
const animTiming = {
  duration: 400,
  easing: "ease-out"
};

/**
 * アコーディオンを閉じるときのキーフレーム
 */
const closingAnimKeyframes = (content) => [
  {
    height: content.offsetHeight + 'px', // height: "auto"だとうまく計算されないため要素の高さを指定する
    opacity: 1,
  }, {
    height: 0,
    opacity: 0,
  }
];

/**
 * アコーディオンを開くときのキーフレーム
 */
const openingAnimKeyframes = (content) => [
  {
    height: 0,
    opacity: 0,
  }, {
    height: content.offsetHeight + 'px',
    opacity: 1,
  }
];
```

## タグ

#ee8d1e; #5887bf; #e5f0fd; #c283b6; #86bfc9; #よしなに対応 

## 関連ドキュメント

- [[../01_よしなに対応/ざっきーさん.md|ざっきーさん]]
- [[../01_よしなに対応/かおりさん（実務）.md|かおりさん（実務）]]
- [[../01_よしなに対応/よしなに対応鉄板ポイント（やり取り編）.md|よしなに対応鉄板ポイント（やり取り編）]]
- [[../01_よしなに対応/やり取りの根本的な考え方.md|やり取りの根本的な考え方]]
- [[../01_よしなに対応/実際にあった”目からウロコ”の案件対応術.md|実際にあった”目からウロコ”の案件対応術]]
