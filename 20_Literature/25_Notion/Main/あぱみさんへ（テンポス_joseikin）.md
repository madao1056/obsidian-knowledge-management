---
notion_id: eba83cfc-4c42-496a-92a8-5d531ced516d
account: Main
title: あぱみさんへ（テンポス_joseikin）
url: https://www.notion.so/_joseikin-eba83cfc4c42496a92a85d531ced516d
created_time: 2023-08-30T01:44:00.000Z
last_edited_time: 2023-08-31T02:18:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:15.092992
---
# あぱみさんへ（テンポス_joseikin）

# デザインデータ
[https://xgf.nu/gPbDz](https://xgf.nu/gPbDz)
作業範囲
- お問い合わせページ
- サンクスページ
---
# 作業内容
以下2ページの静的コーディング
※TOPページとの共通パーツは含みません。
※確認ページはありません（実装不要）
- お問い合わせページ
- サンクスページ
---
# Gulp環境
### 仕様
  - PCファースト
  - 1rem→10pxにしてます
rem()表記はそのまま使用できます
  - css設計
  - インナー幅
  - font
  - color
  - htmlファイルも準備していますのでご活用ください！
メタ関係をすでに入れています！
### 作業環境データ
[https://xgf.nu/pXP4s](https://xgf.nu/pXP4s)
---
# フォームメーラーデータ
（DLして開いてください※ブラウザで開くと文字化けします）
デザインと差異がある場合はソースコード優先でOKです
差異の報告だけお願いします！
---
# 品質管理について
CodeUpsのものか、ご自身でお持ちのもので大丈夫です！
---
# 納品方法について
Zipファイル納品
---
# 費用について
**18,000円(税抜)**
- お問い合わせページ
- サンクスページ
# 初稿提出
**9/4(AM)までにいただけると助かります！**
# 追加情報
base.scssの以下赤枠部分を変更しましたのでご連絡します！
環境を揃えていただけると幸いです！コピペ用に下記にコードを貼りますね！
```scss
@use "global" as *;

// インナー幅＋余白
$breakpointInner: $innerWidth + strip-unit($padding-pc) * 2;

// ルートフォント設定
html {
  // インナー幅＋余白+1px ~
  font-size: 62.5%;

  // 768px ~ インナー幅＋余白
  @media (max-width: $breakpointInner) {
    font-size: vw(strip-unit($breakpointInner), 10);
  }

  // 376px ~ 767px
  @include mq(md) {
    font-size: 62.5%;
  }

  // ~ 375px
  @media (max-width: 428px) {
    font-size: vw(428, 10);
  }
}

// フォント、カラー設定
body {
  font-family: $font-main;
  color: $black;
  background-color: #f4f4f4;
  font-size: 1.6rem;
  line-height: calc(30 / 16);
  @include mq(md) {
    font-size: 1.3rem;
    line-height: calc(30 / 13);
  }
}

// ホバー
a,
button {
  transition: 0.3s;
  &:hover {
    opacity: 0.7;
    cursor: pointer;
    @include mq(md) {
      opacity: 1;
    }
  }
}
```