---
notion_id: 89b134ad-c9c6-4b1f-ab47-ab2302a2d6b4
account: Main
title: MISUMIアニメーション
url: https://www.notion.so/MISUMI-89b134adc9c64b1fab47ab2302a2d6b4
created_time: 2023-08-24T01:34:00.000Z
last_edited_time: 2024-01-23T13:06:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:15.050360
---
# MISUMIアニメーション

歯車くるくる
[https://codepen.io/snowleo208/pen/jXLowg](https://codepen.io/snowleo208/pen/jXLowg)
モーションパス
[https://www.webdesignleaves.com/pr/jquery/web-animation-api-basic.html](https://www.webdesignleaves.com/pr/jquery/web-animation-api-basic.html)
  ※「▶︎」をクリックすると**トグルが開きます**
  <details>
  <summary>目次</summary>
  </details>
  # 基本情報
  - FTP情報
  ---
  ---
  ## 案件仕様情報一覧
  - [ ]  Photoshop、Illustratorの場合カラーモードがRGBになっているか
  - 情報共有されたものをコピペ（リンクも可）
  ---
  # 進捗管理（完了後スクショを載せる）
  ## スクリーンショット
  ## パーツ管理（FLOCSS）※チーム制作
  ---
  # 確認事項一覧（対応履歴）
  ---
  ## 未対応事項メモ
  持ってるボールがあれば追加
  ---
  # 品質管理
  ## 納品データ
  Gulp環境含む or 含まない
  ## 各ブラウザ検証
  【検証内容】
  - フォントが反映されているか
  - 表示崩れはないか
  - 挙動がおかしい箇所はないか（アニメーション、ホバー時、JS実装箇所）
  ## 品質チェック項目
  - **仕様の抜け漏れ**
  - **コンソールエラー**
  - **表示崩れ**
  - **フォントの反映**
  - **画像について**
  - **スクリプトタグ**
  - **アニメーション**
  - **metaタグ**
  - **閉じタグチェック**
  - **HTML・CSSの文法**
  # 各tweenについて
_p-gearAnimation.scssで指定している
各tween毎の transition設定
  - 該当SCSSファイル → _p-gearAnimation.scss
  【**実装の概要**】
  script.js内にGSAPのコードを記述。
  最初のギア（小）が左にスライドする動き以外はクラス名を付与するのみになります。
以下の一覧表の「個別指定のclass名」に 〝is-active〟クラスを付与して、
次のようにCSSプロパティを当てています。
  ```plain text
is-activeなし
↓
opacity: 0;
visibility: hidden;

is-activeあり
↓
opacity: 1;
visibility: visible;
  ```
  また、**すべての要素のアニメーション効果**を
opacity、visibilityともに次のように設定しています。
  ```plain text
transition:
    opacity 0.8s ease-in,
    visibility 0.8s ease-in;
  ```
  ---
  
  
  
  
  
  
  
  
  # 各要素とクラスの関係性
  以下にどの要素（ギアや矢印）がどのクラス名に該当しているかの一覧を示します。
**要素名は画像を参照**してください。
**class名はp-gearAnimation.scssを参照**してください。
並び順：画像No.1→3
  ![参考画像３](https://prod-files-secure.s3.us-west-2.amazonaws.com/736adce6-a3a4-4a64-9f74-d9aa055c96d2/d512b131-e82c-4040-be6d-8109c6dfefdb/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88_2024-01-23_22.53.51.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6323FXD%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T042411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEE4ilKOkfsikI8Kzw96fkJGgCpNsa7C2XVaADZAAQ2WAiEAq52mJFxp9moQ7ZlXj1Gk0ekYowbECANO6vC%2FL%2BJzMoAqiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF%2BlfxfAyxghLedwbyrcA5S8UImbbOhcEeU61cOq7sBKPVGQSRUmRuVNqrNjnQX4i2DDjrr56rUdRR405yWJIhsxevsXJTU2yBf1wEtLCBk8YmArn0Ms2mnQlnX1BXoXcLy1Ef%2FYPkgE6D%2F7ZGOegxRVXaUTFKxirQtZjRaHmykzibC4EVMnEpTBUas13Vj2M1it%2Fsaf5FUPjITTW36QMbj85HeehEhZ1CNGo1nXFBBCr%2BXqNDUvdFqYFMkFycv2EtafnJl%2BCZe90N97D0K9mKV7QE2FiKe4c%2Bt6BHk48qynZFpITHg8zsZ4qMLua513fnCpR4J8jlLOqt%2BAdFerpj1n%2B94NGBiZ%2BtttetDC4ZXQhyMTo0f8cr24LMH%2BPssLpfR6G%2B%2F8fJOlOOZ09usojUAWhz9yZr%2Ffe3ImMIk5idDISXgUj8pLpM%2BBbS%2F%2FzZ2a3f%2Bu0NcrKujcWgq3BuSiuMgOIv1rbupUc9Yh%2Fh9%2BKmasASDMk38cJ%2F5Gh57ycYm%2FMR1SvmojCCHcqcnbc0B86Z7YiIAS%2FR0ALP2d5C7IRssc2VE3yhyZB6sH9Z7Njcn52ONjL9mYAuEEGU2bfso18CwF86vB9IkUZZjZJEIvHR%2B276cuZZSCu%2BXR1MuuG%2BFZm5ym%2FBYSUOhSVQ%2BGMKWq7MMGOqUBYdbinwVbWSkF4GMDomEMD0H8w1ZlQv%2F0ha2tTI%2Fcnf84BdF85T2nWmkYApy4nqQQ3evirL2auRQUVcA7r83n5RmLVjww7urr2jOTRKnNie8SROiajLKhqYdUU%2FVFKBo%2BDoEQzJsGVF5rjtJtw3aPWvue0ZPWJSLdmYfCmZVuIxBONwkwoabbUsM7JlMrNd3vwdRILlV42ML5Wly1vo1KLboRJCrv&X-Amz-Signature=b76478a5672384660f12eb08bc1e50294dc08ab43cfad4cfc4b81f83944ff18b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
  ---
  # 各tweenについて
ScrollTriger.createのstartプロパティ値
  以下に各要素（ギアや矢印）のScrollTriger.createのstartプロパティ値の一覧を示します。
  要素名は **各要素とクラスの関係性 **の画像を参照してください。
  基準は 〝.p-gearAnimation〟クラスでheight: 2500vhを指定しており、
2500vhを100％とした時の割合で設定しています。
  ギヤ２についてはギヤ内の矢印がテキストの下に来るため、
別々に書き出して調整しています。
  並び順：アニメーション順
  ---