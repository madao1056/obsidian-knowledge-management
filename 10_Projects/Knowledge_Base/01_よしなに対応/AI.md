---
notion_id: 217ade4a-d294-808b-ab0c-cd659f274ea1
account: Main
title: AI
url: https://www.notion.so/AI-217ade4ad294808bab0ccd659f274ea1
created_time: 2025-06-19T14:45:00.000Z
last_edited_time: 2025-07-12T05:16:00.000Z
sync_status: full_content
sync_time: 2025-07-12T15:10:47.594716
---
# AI

  ---
  ### 🔧 事前準備
  - Google アカウント（個人）
  - 管理したいビジネスのGoogleビジネスプロフィール権限
  - GCP（Google Cloud Platform）にアクセス可能
  ---
  ### ✅ Step 1. GCPプロジェクト作成とAPI有効化
  1. Google Cloud Console にアクセス
  1. 新しいプロジェクトを作成（例：`GBP-AutoPoster`）
  1. 左メニュー「APIとサービス > ライブラリ」で以下を検索・有効化：
  ```plain text
nginx
コピーする編集する
Business Profile API


  ```
  ---
  ### ✅ Step 2. OAuthクライアント作成（Playground用）
  1. 「APIとサービス > 認証情報 > 認証情報を作成 > OAuth 2.0 クライアントID」
  1. アプリの種類 → **「デスクトップアプリ」**
  1. 作成後、**クライアントID / クライアントシークレット**を控える
  ---
  ### ✅ Step 3. OAuth Playgroundでトークン取得
  1. OAuth Playground にアクセス
  1. ⚙️設定アイコン → `Use your own OAuth credentials` をONにして、
  1. Step 1 で Scope を追加：
  ```plain text
arduino
コピーする編集する
https://www.googleapis.com/auth/business.manage


  ```
  1. 「Authorize APIs」→ Googleログイン → 許可
  1. 「Exchange authorization code for tokens」クリック
  1. `Access Token` と `Refresh Token` を控える
  ---
  ### ✅ Step 4. アカウントID（accountId）の取得
  以下をリクエスト：
  ```plain text
http
コピーする編集する
GET https://mybusinessbusinessinformation.googleapis.com/v1/accounts
Authorization: Bearer {AccessToken}


  ```
  返却データのうち `type` が `LOCATION_GROUP` のアカウントIDを選ぶ：
  ```json
json
コピーする編集する
{
  "type": "LOCATION_GROUP",
  "name": "accounts/104977584544894683787"
}


  ```
  この `"accounts/~~~"` の数字部分が `accountId`
  ---
  ### ✅ Step 5. ロケーションID（locationId）の取得
  ```plain text
http
コピーする編集する
GET https://mybusinessbusinessinformation.googleapis.com/v1/accounts/{accountId}/locations?read_mask=name,title
Authorization: Bearer {AccessToken}


  ```
  レスポンス例：
  ```json
json
コピーする編集する
{
  "locations": [
    {
      "name": "locations/5299935210298410809",
      "title": "enen ホームページ制作"
    }
  ]
}


  ```
  この `"locations/~~~"` の数字部分が `locationId`
  ---
  ### ✅ Step 6. 環境変数（.env例）
  ```plain text
env
コピーする編集する
GBP_ACCESS_TOKEN=ya29.xxxxxxxx
GBP_REFRESH_TOKEN=1//0gxxxxxxx
GBP_CLIENT_ID=xxxxxxxxxxx.apps.googleusercontent.com
GBP_CLIENT_SECRET=xxxxxxxx
ACCOUNT_ID=104977584544894683787  # LOCATION_GROUP
LOCATION_ID=5299935210298410809  # 店舗ID


  ```
  ---
  ### 📌 よくある落とし穴まとめ
  ---
  ### 🎯 この設定でできること（応用）
  - MEO投稿の自動化（定期投稿）
  - 店舗情報の一括更新
  - 営業時間・商品・画像の同期
  - クライアント別にAPI認証を切り分けるマルチテナント対応 etc
  はい、承知いたしました。この情報はアプリ上には表示せず、ご参考までにお伝えします。
  先ほどのWeb調査の結果から、A社・B社・C社は特定の1社を指しているわけではなく、市場にあるMEOツールの価格帯や機能性を元にした**代表的なモデル（ペルソナ）**として設定しています。
  それぞれのモデルに該当する具体的なツール例は以下のようになります。
  - **A社（基本ツール / 月額5,000円前後）のモデル:**
  - **B社（標準ツール / 月額12,000円前後）のモデル:**
  - **C社（高機能ツール / 月額20,000円前後）のモデル:**
  ダッシュボードの比較表は、このように市場の各価格帯の代表的な機能と、ユーザー様が組み立てたプランのコストパフォーマンスを比較し、価値を分かりやすく感じていただくことを目的としています。
  # MEOチェキ
  # MEOアナリティクス
  # 検索ドーン
  # cooboo
  使用AIモデル gpt-4-turbo-preview 現在 gpt-4-turbo にリダイレクトされる、比較的高性能なモデルです。
  それでは、この情報と最新のAPI価格を元に、利益率のファクトチェックを行います。
  ---
  # AIの従量課金
  # 1テナントあたりの月額コスト
  # **結論：どのくらい**テナント**見込めば良いか？**

## タグ

#よしなに対応 

## 関連ドキュメント

- [[../01_よしなに対応/クライアント対応に必須『質問力』＆『設計力』
〜AI時代でもこれだけは変わらない〜.md|クライアント対応に必須『質問力』＆『設計力』]]
- [[../01_よしなに対応/ログジさん.md|ログジさん]]
- [[../01_よしなに対応/みさ👶.md|みさ👶]]
- [[../01_よしなに対応/グッサポ動画文字起こしまとめ.md|グッサポ動画文字起こしまとめ]]
- [[../01_よしなに対応/まりあさん『よしなに対応』ぶち上げ企画.md|まりあさん『よしなに対応』ぶち上げ企画]]
