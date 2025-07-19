---
notion_id: f8162693-0ab6-4157-821f-d8f890cc69c9
account: Main
title: フードプレイスHPサービスページ・コーディングマニュアル
url: https://www.notion.so/HP-f81626930ab64157821fd8f890cc69c9
created_time: 2022-06-24T03:18:00.000Z
last_edited_time: 2022-06-24T03:18:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:15.153687
---
# フードプレイスHPサービスページ・コーディングマニュアル

## **◆読み込むCSS**
css/style.css
css/style_service.css
※上記2つのCSSは編集不可でお願い致します。
HTMLファイル名.css
新規でページを作成する場合には、作成するページの「HTMLのファイル名.css」を作成してHTMLに読み込んで下さい。
## **・ディレクトリ、ファイル名**
・ページ独自のcssやjsのファイル名は該当のhtmlと同じものを設定
・cssやjs、imgなどの格納場所は「public_html」直下のそれぞれのフォルダ内に格納をする。
例）
tenposfoodplace.jp/public_html/css/homepage.css
tenposfoodplace.jp/public_html/js/homepage.js
## **◆ID・クラス名の付け方**
### **・HTML**
・bodyタグにページ独自のIDを付与する。
例）
飲食店向けホームページ作成　→ homepage
・sectionタグにIDを付与する。
例）
飲食店向けホームページ作成ページの料金案内セクション
→sec-cost、homepage-costなど
どこのセクションなのか分かるよう命名する
※「sec-01」「content-02」のようにxx番目という名前にしない（後に順番が変わる可能性があるため）
### **・CSS**
・commonなど共通のセレクタ以外の記述は必ずページIDとセクションIDを付ける
例）
飲食店向けホームページ作成ページ内、料金案内セクションのテキストのセレクタ
→#homepage #sec-cost p {〜}など
・セクションなどをコメントアウトで見やすく区切る
例）
/* ———————
sec-cost
———————- */
/*— sec-cost —-*/
・レスポンシブはセクションごとに記述（ファイル末尾にまとめて記述しない）