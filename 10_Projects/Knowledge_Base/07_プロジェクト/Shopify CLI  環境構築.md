---
notion_id: c5f8cf96-775f-4d35-9073-1c83d10e0221
account: Secondary
title: Shopify CLI  環境構築
url: https://www.notion.so/Shopify-CLI-c5f8cf96775f4d3590731c83d10e0221
created_time: 2022-09-17T07:39:00.000Z
last_edited_time: 2023-05-24T01:58:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.447356
---
# Shopify CLI  環境構築

⏲読了目安　10~15分
> **目次**
# Shopify CLIとは？
Shopify CLIは、Shopify（ショッピファイ）のアプリやテーマの構築を支援する
コマンドラインインターフェースツールで、開発者が使用するコマンドラインです。
Shopify CLIをダウンロードすれば、アプリやテーマを開発できるだけでなく、ローカルで編集したコードをご自身のShopifyストアに反映させることができます。また特徴の一つにGitでのソースコード管理がShopify CLIを用いることで可能になります。
### Theme Kitとの違いは？
しかしながら、「Shopify　環境構築」と検索すると、長らく使われてきたShopify Theme Kitの情報が多くヒットするため、混乱する方もおられるでしょう。そこでまずTheme Kitとの違いを説明していきます。
端的に言えば、Shopify CLIとTheme Kitの違いは、使用しているテーマがOnline Store 2.0以降かどうかです。Shopify Online Store 2.0以降のテーマをローカル環境で扱いたい方はShopify CLIになりますが、Shopify Online Store 2.0以前のテーマの場合は、Theme Kit を利用する必要があります。
詳しくは下記の記事をご覧ください
[Bookmark](https://ichyaku.com/shopify-theme-kit/)
> 💡 まとめると…
  - ShopifyCLIとはコマンドラインインターフェースツールである。
  - CLIではテーマ開発だけでなくローカルでのコード編集をストアに反映できる。
  - Gitでのソースコード管理が出来るため柔軟に開発ができる。
  - Theme Kitとの違いはOnline Store2.0に対応しているか否かである。
Shopify CLIでの特徴の一つにGit GitHubでソースコード管理が出来ると挙げましたが
Git、GitHubとは何でしょうか？
## 補章　Git Githubとは？
  
  Gitとは端的に言うと**ファイルの変更履歴を管理してくれるシステムのひとつです。**
  
  例えば、自分一人でも作業の変更を保存していたら、書き換えたファイル名が最新版(1).docs 修正版(2).docs　最新版(1)コピー.docs　オリジナル(1).docsのように何のファイルなのかが全く分からなくなってしまった経験はないでしょうか？　これが大人数で同時に作業をし沢山の修正を行うプログラムならなおさら無秩序な状況になってしまうのは言うまでもないでしょう。
  
  **そこでGit GitHubの出番です。**Git、GitHubは**誰が　いつ　どこを　**変更したのかを保存してくれる非常に便利なツールです。
  Gitで管理されているおかげで前の修正場所が分かったり、他のエンジニアと同時に仕事が出来るのです。Shopifyでのテーマ開発でも、もちろん例外ではなく基本的にはGitを用いてバージョン管理を行います。Shopify側もGithubとの連携やブランチの接続など多くのサポートをしてくれているので、是非Git,GitHubを使いこなせるようになりましょう。
  
  更に詳しく知りたい方は下記の記事や動画での学習をおすすめします。
  [Bookmark](https://www.r-staffing.co.jp/engineer/entry/20190621_1)
  [Bookmark](https://tech-blog.rakus.co.jp/entry/20200529/git)
すでにご存じの方はShopify CLI 導入準備にお進みください。
# Shopify CLI 導入
## Step 0 Rubyのインストール
Shopify CLIを導入するためには　Windows Ruby 2.7以上が必要です。
＊MacではRubyもしくはHomebrewでインストールできます。
Rubyのインストールは下記サイトをご参照ください。
[Bookmark](https://web-camp.io/magazine/archives/15051)
```ruby
ruby -v
```
上記のコマンドを打ち込み下記の画像のようにRubyのバージョンが出力されれば大丈夫です。
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/d58fe38c-a9d4-4466-aed9-85604b7b2c6d/4aec9d31-e82d-4aa9-9364-4f6edf81fce6/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88_2022-08-04_172344.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIE375P4%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T060940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA0KTLductUDo3gqClMpYFvnxINbqPot9BcKzEm7QFNMAiEAtftYQYGM9TVfiNkBQtkp2NmufyGz2ECv00NSgUli%2BAIqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHZgdYz6giGAhlRUBircA%2FW8QjdM2W78P9jjtQeR%2BRP7hxlURsyBy1GSyxABx3YS1v0Pb1v30lJAejkACySD5rX14UW9MbOjjsmJelHVmaBAqehz4bjnTnGNoxalAP1ESXV2WvFGke30J0PPVz2Uo5Bpg0yZ3pXdCzefrP9aLCTOq%2Ffbk0B88uPLQIqtd8eep%2FIm4vGPjWIrQP6oXJWhpuZFbM7Rgb8xmMS51QllRGv1tzq4j8kw6fN783h2E%2BcTiHitDMoxEqfB%2Fts5VaeHESoj2Nxxwmya7Zp8GhKXLO6XflMNLvLp58axOjow1EtBMJDF%2BghzzVwJy76DDPqefjLHzAAVWqRVClzpqwsxTkF2D%2FqwdPFzxIcTpxVCluFaH%2FEc0VpHRl8qsFG4RdLYIWgObL%2F1N%2FcE7ow6t81DiqiXMpwjQcbVdq8EwPzstSXrk3GyXfBbKOUwYE%2B5NRk8pdDSozMmeZA%2F5MV2MOp0z5C1bkDPSCeHpRJx9OYV08pnmQ9fPB7Se0iTfQpnHM92iH%2FS9A1WB%2FeVsVCuC4qR8UyMFPwoXQ4PtBmfREGKg9IZZVZFU6deV3LDerHyvbtJ30oNoBL6wWhuCgBqdEfn5yxoFSLJ8gRk6%2FSVuNsmzq8rsNeWyPsGIDyWRsRnMN%2FF7MMGOqUBOQb6nna4QWEI%2BTk7Xr2p%2F88obuuHqOQidQG4pjF43pmPUCLM%2BHl2AVWyn7thEm4XiGWpAvicNgLmQLzaM8JZdpyXsCEr8pl4cL0jdOG%2FvC0z1o1NwE%2B%2BWb6EVgpI6OGUnVmhKgRZ7hqm5attgMD%2F6RGR0VtZn2x23284wcIZwB1Is2%2BY0kZJ%2FdoTKW72lRz4lPRbjxEscLZKBtkiqnkFNzYKL248&X-Amz-Signature=bf5ccf3b58ff900e708be5401f6bb060bd2b95897213cb96423e61fe995ed802&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
ではいよいよShopify CLIをインストールしていきます。
## Step 1 Shopify CLI インストール
```ruby
gem install shopify-cli
```
windowsの方は 上記のコマンドをコマンドラインで打ち込んでください。
＊必ずCommand Prompt with Rubyに打ち込んでください。通常のコマンドプロンプトでは
エラーが出る可能性があります。
＊Macの方は下記のコマンドを実行してください。
```ruby
brew tap shopify/shopify
brew install shopify-cli 
```
上記の手順がすべて完了したらShopify CLIのインストールの完了です。
## Step 2 認証
次に自分の持っているアカウントとShopify CLIを紐づける作業を行います。
Shopify storeのdomainが必要です。（アカウント作成が必要です）
まず下記のコマンドを入力してください
```ruby
shopify login --store <DOMAIN>
```
上記のコマンドを実行し警告が出る場合、allow accessをクリックしてください。
メールアドレスとパスワード入力後、下記の文字が表示されたら完了です。
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/d58fe38c-a9d4-4466-aed9-85604b7b2c6d/b2675474-b902-40ec-881c-d6fc4d8c1fe7/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88_2022-08-04_185132.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIE375P4%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T060941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA0KTLductUDo3gqClMpYFvnxINbqPot9BcKzEm7QFNMAiEAtftYQYGM9TVfiNkBQtkp2NmufyGz2ECv00NSgUli%2BAIqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHZgdYz6giGAhlRUBircA%2FW8QjdM2W78P9jjtQeR%2BRP7hxlURsyBy1GSyxABx3YS1v0Pb1v30lJAejkACySD5rX14UW9MbOjjsmJelHVmaBAqehz4bjnTnGNoxalAP1ESXV2WvFGke30J0PPVz2Uo5Bpg0yZ3pXdCzefrP9aLCTOq%2Ffbk0B88uPLQIqtd8eep%2FIm4vGPjWIrQP6oXJWhpuZFbM7Rgb8xmMS51QllRGv1tzq4j8kw6fN783h2E%2BcTiHitDMoxEqfB%2Fts5VaeHESoj2Nxxwmya7Zp8GhKXLO6XflMNLvLp58axOjow1EtBMJDF%2BghzzVwJy76DDPqefjLHzAAVWqRVClzpqwsxTkF2D%2FqwdPFzxIcTpxVCluFaH%2FEc0VpHRl8qsFG4RdLYIWgObL%2F1N%2FcE7ow6t81DiqiXMpwjQcbVdq8EwPzstSXrk3GyXfBbKOUwYE%2B5NRk8pdDSozMmeZA%2F5MV2MOp0z5C1bkDPSCeHpRJx9OYV08pnmQ9fPB7Se0iTfQpnHM92iH%2FS9A1WB%2FeVsVCuC4qR8UyMFPwoXQ4PtBmfREGKg9IZZVZFU6deV3LDerHyvbtJ30oNoBL6wWhuCgBqdEfn5yxoFSLJ8gRk6%2FSVuNsmzq8rsNeWyPsGIDyWRsRnMN%2FF7MMGOqUBOQb6nna4QWEI%2BTk7Xr2p%2F88obuuHqOQidQG4pjF43pmPUCLM%2BHl2AVWyn7thEm4XiGWpAvicNgLmQLzaM8JZdpyXsCEr8pl4cL0jdOG%2FvC0z1o1NwE%2B%2BWb6EVgpI6OGUnVmhKgRZ7hqm5attgMD%2F6RGR0VtZn2x23284wcIZwB1Is2%2BY0kZJ%2FdoTKW72lRz4lPRbjxEscLZKBtkiqnkFNzYKL248&X-Amz-Signature=ecee1059f50dec8f77e81609ebf39ef37c3e520ccc98f8097863bc06db54c9f0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
その後コマンドプロンプトに下記の画像のような表示がでたらログイン完了です。
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/d58fe38c-a9d4-4466-aed9-85604b7b2c6d/b1662d32-636e-47a2-acd4-268256b889fc/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88_2022-08-04_185438.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIE375P4%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T060941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA0KTLductUDo3gqClMpYFvnxINbqPot9BcKzEm7QFNMAiEAtftYQYGM9TVfiNkBQtkp2NmufyGz2ECv00NSgUli%2BAIqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHZgdYz6giGAhlRUBircA%2FW8QjdM2W78P9jjtQeR%2BRP7hxlURsyBy1GSyxABx3YS1v0Pb1v30lJAejkACySD5rX14UW9MbOjjsmJelHVmaBAqehz4bjnTnGNoxalAP1ESXV2WvFGke30J0PPVz2Uo5Bpg0yZ3pXdCzefrP9aLCTOq%2Ffbk0B88uPLQIqtd8eep%2FIm4vGPjWIrQP6oXJWhpuZFbM7Rgb8xmMS51QllRGv1tzq4j8kw6fN783h2E%2BcTiHitDMoxEqfB%2Fts5VaeHESoj2Nxxwmya7Zp8GhKXLO6XflMNLvLp58axOjow1EtBMJDF%2BghzzVwJy76DDPqefjLHzAAVWqRVClzpqwsxTkF2D%2FqwdPFzxIcTpxVCluFaH%2FEc0VpHRl8qsFG4RdLYIWgObL%2F1N%2FcE7ow6t81DiqiXMpwjQcbVdq8EwPzstSXrk3GyXfBbKOUwYE%2B5NRk8pdDSozMmeZA%2F5MV2MOp0z5C1bkDPSCeHpRJx9OYV08pnmQ9fPB7Se0iTfQpnHM92iH%2FS9A1WB%2FeVsVCuC4qR8UyMFPwoXQ4PtBmfREGKg9IZZVZFU6deV3LDerHyvbtJ30oNoBL6wWhuCgBqdEfn5yxoFSLJ8gRk6%2FSVuNsmzq8rsNeWyPsGIDyWRsRnMN%2FF7MMGOqUBOQb6nna4QWEI%2BTk7Xr2p%2F88obuuHqOQidQG4pjF43pmPUCLM%2BHl2AVWyn7thEm4XiGWpAvicNgLmQLzaM8JZdpyXsCEr8pl4cL0jdOG%2FvC0z1o1NwE%2B%2BWb6EVgpI6OGUnVmhKgRZ7hqm5attgMD%2F6RGR0VtZn2x23284wcIZwB1Is2%2BY0kZJ%2FdoTKW72lRz4lPRbjxEscLZKBtkiqnkFNzYKL248&X-Amz-Signature=a5ebcf887eb44c7a6eb006aa58b693d53de05dce7414cb8b3efb2a7074530dfa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
上記の画像のような表示が出ればログイン完了です。
以上で認証が完了しました。
# 新規テーマ作成とカスタマイズ方法
上記の手順を終え、ShopifyCLIをインストールできたと思います。
それでは Shopify CLIを用いて新規テーマを作成してみましょう。
```ruby
shopify theme init 
```
上記のコマンドを実行すると　**?Theme name **と表示されます。そこでダウンロードしたいテーマの名前を聞かれます。そのためDawnBFCMと入力しましょう。
**DawnBFCM**
と入力するとDawnと呼ばれるShopify側が無料で提供されているテーマがダウンロードされます。
以上で新規テーマダウンロードは完了です。
より詳しく知りたい方は下記の公式ドキュメントをご参照ください。
[Bookmark](https://shopify.dev/themes/tools/cli/theme-commands)
## **ShopifyストアとローカルのShopify CLIを接続する**
ここまででDawnというデフォルトのテーマがローカル環境にダウンロードされましたが、このテーマに編集を加えた場合どのように変更を確認すれば良いのでしょうか？
このセクションでは**ShopifyストアとローカルのShopify CLIを接続する方法**を学びます。
接続することによりコード編集がリアルタイムで確認することが出来るため、**今後の開発にも必要不可欠です。**
しかしながら、エラーに直面しやすく一番躓きやすい箇所ですので実際のエラーも踏まえながら説明していきます。（筆者である私も２時間以上このエラーにはまりました）
```ruby
shopify theme serve
```
上記のコマンドでうまくいった場合、このような画面が表示されます
### よくあるErrorと解決策
ただ上記のコマンドで多くの方はエラーに引っかかってしまうと思います。
またそのエラーはほとんどの場合が認証エラーで
### 認証エラー
  ```ruby
X You are not authorized to edit themes on [xxx].myshopify.com.
Make sure you are a user of that store, and allowed to edit themes.
  ```
  
  ターミナルに上記のような表示が出ます。
  
  基本的にはこのエラー解決はターミナル上で下記のコマンドを実行しログアウトを行います。
  ```ruby
shopify logout
  ```
  
  またターミナルだけでなくストア側でもログアウトを行うことによりエラーが解消されます。
  
  上記の手順で解消されるとは思いますが、解消されない方は解決策としていくつかの有用な記事を掲載させていただくので、エラー解決の一助としてください。
  
  **・Qitaの該当エラーの記事**
  [Bookmark](https://qiita.com/technosource_jp/items/d3cb129f30f591890384)
  **・筆者である私が参考にさせて頂いた記事**
  [Bookmark](https://okalog.info/shopify-cli-error/)
  ・**Shopify公式の該当エラーに対するDisccusion**
  [Bookmark](https://community.shopify.com/c/technical-q-a/shopify-theme-serve-not-working-in-shopify-cli/td-p/1231086)
---
### バージョン低いエラー
  以下のエラーがでる場合、ruby のバージョンが低いことが原因
  ```plain text
shopify: command not found
  ```
  ```plain text
$ cd
$ vi ~/.bash_profile
export PATH="~/.rbenv/shims:/usr/local/bin:$PATH"
eval "$(rbenv init -)"
$ source ~/.bash_profile
  ```
  [Bookmark](https://qiita.com/opiyo_taku/items/3312a75d5916f6cd32b1)
  
---
### 予期せぬエラー
  ```plain text
✗ An unexpected error occured.
        To submit an issue include the stack trace.
        To print the stack trace, add the environment variable SHOPIFY_CLI_STACKTRACE=1.
  ```
  ```plain text
shopify logout

shopify login --store=nakajin-dev.myshopify.com

もしくは以下
shopify login --store https://nakajin-dev.myshopify.com/admin
  ```
  
  [Bookmark](https://zenn.dev/maneko/scraps/867afb20d7005a)
  [Bookmark](https://www.evoworx.co.jp/blog/shopify-cli/)
ここまでの手順が完了しましたらShopify CLIでの環境構築並びに新規テーマ作成は**完了**です。
ここまで読んでいただきありがとうございました。
# **shopify theme コマンドについて**
  - shopify theme -h
  - shopify theme init
  - shopify theme check
  - shopify theme pull [-i ダウンロードしたいテーマのID]
  - shopify theme serve
  - shopify theme list
  - shopify theme open
  - shopify theme push
  - shopify theme share
  - shopify theme publish
  - shopify theme package
  - shopify theme delete
補章としてGithubを用いたストアとの接続方法を説明させて頂いてるのでよろしければ
お読みください。