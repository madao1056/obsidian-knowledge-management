---
notion_id: 217ade4a-d294-807f-ae4b-ff259d82e7cb
account: Main
title: Google Business Profile API 設定マニュアル（MEO自動化用）
url: https://www.notion.so/Google-Business-Profile-API-MEO-217ade4ad294807fae4bff259d82e7cb
created_time: 2025-06-19T14:45:00.000Z
last_edited_time: 2025-06-19T14:45:00.000Z
sync_status: full_content
sync_time: 2025-07-12T15:11:36.458915
---

# Google Business Profile API 設定マニュアル（MEO自動化用）

*[divider]*

### 🔧 事前準備

- Google アカウント（個人）

- 管理したいビジネスのGoogleビジネスプロフィール権限

- GCP（Google Cloud Platform）にアクセス可能

*[divider]*

### ✅ Step 1. GCPプロジェクト作成とAPI有効化

1. Google Cloud Console にアクセス

1. 新しいプロジェクトを作成（例：`GBP-AutoPoster`）

1. 左メニュー「APIとサービス > ライブラリ」で以下を検索・有効化：

```plain text
nginx
コピーする編集する
Business Profile API


```

*[divider]*

### ✅ Step 2. OAuthクライアント作成（Playground用）

1. 「APIとサービス > 認証情報 > 認証情報を作成 > OAuth 2.0 クライアントID」

1. アプリの種類 → **「デスクトップアプリ」**

1. 作成後、**クライアントID / クライアントシークレット**を控える

*[divider]*

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

*[divider]*

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

*[divider]*

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

*[divider]*

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

*[divider]*

### 📌 よくある落とし穴まとめ

*[table]*

*[divider]*

### 🎯 この設定でできること（応用）

- MEO投稿の自動化（定期投稿）

- 店舗情報の一括更新

- 営業時間・商品・画像の同期

- クライアント別にAPI認証を切り分けるマルチテナント対応 etc


---

*Synced from Notion Main account at 2025-07-12 15:11:36*
