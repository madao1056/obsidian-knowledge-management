---
notion_id: 1cc5b47a-cebc-4f8e-b8ec-e6ca2b5395a4
account: Main
title: 【2−2】スライダーテンプレート使い方を簡単解説（Splide編）
url: https://www.notion.so/2-2-Splide-1cc5b47acebc4f8eb8ece6ca2b5395a4
created_time: 2023-09-11T00:13:00.000Z
last_edited_time: 2023-09-11T00:13:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:15.086216
---
# 【2−2】スライダーテンプレート使い方を簡単解説（Splide編）

【目次】
# 今回行うこと
Splide.jsを使用してスライダーのテンプレートを作成する
【完成イメージ】
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/736adce6-a3a4-4a64-9f74-d9aa055c96d2/f6af8c0f-d2f5-4dd2-b74f-cfeed7256bf0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWERSM7G%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T044501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF9Obw1A%2FEQyvnm05veAPEQWJZPuusXTxGY4H6yWo%2BelAiEA5u%2FiCjeJyDgxsS5AvNPHYRje2Ls%2BMz0qYLWmMFSJoHsqiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL7ab0l2QbQIULBXnCrcAy515RyOn314DPJw2dL8P87M0BAVmIofSpOZag%2FuoHOOYgDhDmjCOurdLqlhArwhkuSo3n8y93fTRKY6ZbFVFqQjPhEEwDllzlzWdTzRLMrMarwwHAdN9wxE0%2B4ZdT8HE96Djl2ATI3T%2FfayUClQqCm%2F4GtLOtCI0XhrUUZPa3xXnh6HrlqfddHPP83K2ZhQOuyvvrUBcC5okqDuKvgON3ixSa0ZhnzjRocLzMOuiOFXDS%2BzR%2BFjDCpGjQlbs5m7tRAQZgObPEoI4bCyLUCSZRJavghQBb%2FbK7jx%2BDsRHpse8ONqt1kOH91h0osj4mWipq8FzQQenp21wA1mtcihYgHGVr7AWV%2BWZ2HN%2FphXN1Mq4T9nwULhQbojJNyg5u4CK2sAFCjwKU8JzthHp%2F0BRB0I%2FiF3ImUzzTUKvhta6hRvQKkVD2G9cYIfSA3s3epxDMolFs28jVxdaPq58lbWeXfFlhz2Yps7VPplcLRApj%2BkQnJM8t7DjKFIcxeYIOomXOwlVMWuzrwyWV3uPHEg0TB4377ZWlZENjCB40%2BSPtfac8J2jIVvMvBGZTMeCLcezzgcB8rMgdoxaKoWHzTYyZJLsX8yjrZK6SlI7k4rqXnD%2F6gDYYYNTczm6WzhMNyq7MMGOqUBNvfn2brgDVFmWoSc7NGR0TWo8CgHeS5kUT6I184KKbSqWxF4nAhm0gLeNYh1E8qI%2BjhfSUpFtAOt%2B0Pp7FN7e77t5yhzTP9%2Be%2FJzQiw4P4UVgemawMy%2FXVrDXQa2FsSPjntfbsdC6prRmq1WQ0lBfKQCKPTGvyc8X7jCg%2BJaS6M%2F%2FhfmD3xrk2RUkTwZ0Yjo8FqAbxD9pVN6x2%2Bq5sK20ejiGd0o&X-Amz-Signature=b05e817029060aa2aface636fd6c367234b2df77c3e18b030669b90dbf12bbba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
【手順】
1.テンプレートファイルをテーマとして設定する
2.Advanced Custom Fieldsプラグインをインストール
3.カスタムフィールド設定データをインポート
4.投稿タイプ「MVスライダー」に画像等を設定する
5.設定確認
6.動作確認
7.CSSの設定
> 💡 **１章で実施した内容も含めて説明していますので、ご了承ください！**
# Splide.jsを使用してスライダーのテンプレートを作成する
## 1.テンプレートファイルをテーマとして設定する
※既に実施済みの場合は、スキップしてください。
### （１）次のzipファイルをダウンロードする
### （２）テーマとして追加する
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/736adce6-a3a4-4a64-9f74-d9aa055c96d2/a7678141-a004-4ca9-9a9b-638c9b760232/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWERSM7G%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T044501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF9Obw1A%2FEQyvnm05veAPEQWJZPuusXTxGY4H6yWo%2BelAiEA5u%2FiCjeJyDgxsS5AvNPHYRje2Ls%2BMz0qYLWmMFSJoHsqiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL7ab0l2QbQIULBXnCrcAy515RyOn314DPJw2dL8P87M0BAVmIofSpOZag%2FuoHOOYgDhDmjCOurdLqlhArwhkuSo3n8y93fTRKY6ZbFVFqQjPhEEwDllzlzWdTzRLMrMarwwHAdN9wxE0%2B4ZdT8HE96Djl2ATI3T%2FfayUClQqCm%2F4GtLOtCI0XhrUUZPa3xXnh6HrlqfddHPP83K2ZhQOuyvvrUBcC5okqDuKvgON3ixSa0ZhnzjRocLzMOuiOFXDS%2BzR%2BFjDCpGjQlbs5m7tRAQZgObPEoI4bCyLUCSZRJavghQBb%2FbK7jx%2BDsRHpse8ONqt1kOH91h0osj4mWipq8FzQQenp21wA1mtcihYgHGVr7AWV%2BWZ2HN%2FphXN1Mq4T9nwULhQbojJNyg5u4CK2sAFCjwKU8JzthHp%2F0BRB0I%2FiF3ImUzzTUKvhta6hRvQKkVD2G9cYIfSA3s3epxDMolFs28jVxdaPq58lbWeXfFlhz2Yps7VPplcLRApj%2BkQnJM8t7DjKFIcxeYIOomXOwlVMWuzrwyWV3uPHEg0TB4377ZWlZENjCB40%2BSPtfac8J2jIVvMvBGZTMeCLcezzgcB8rMgdoxaKoWHzTYyZJLsX8yjrZK6SlI7k4rqXnD%2F6gDYYYNTczm6WzhMNyq7MMGOqUBNvfn2brgDVFmWoSc7NGR0TWo8CgHeS5kUT6I184KKbSqWxF4nAhm0gLeNYh1E8qI%2BjhfSUpFtAOt%2B0Pp7FN7e77t5yhzTP9%2Be%2FJzQiw4P4UVgemawMy%2FXVrDXQa2FsSPjntfbsdC6prRmq1WQ0lBfKQCKPTGvyc8X7jCg%2BJaS6M%2F%2FhfmD3xrk2RUkTwZ0Yjo8FqAbxD9pVN6x2%2Bq5sK20ejiGd0o&X-Amz-Signature=f14188b728fc4f0a045c1c34e2528c3ff5155d6a2c5522b070d1ab2ca79ee0b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
## 2.Advanced Custom Fieldsプラグインをインストール
※既に実施済みの場合は、スキップしてください。
### （１）Advanced Custom Fieldsプラグインをインストールする。
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/736adce6-a3a4-4a64-9f74-d9aa055c96d2/a4038958-2bf1-46a5-a3ae-0c24e5faf612/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWERSM7G%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T044501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF9Obw1A%2FEQyvnm05veAPEQWJZPuusXTxGY4H6yWo%2BelAiEA5u%2FiCjeJyDgxsS5AvNPHYRje2Ls%2BMz0qYLWmMFSJoHsqiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL7ab0l2QbQIULBXnCrcAy515RyOn314DPJw2dL8P87M0BAVmIofSpOZag%2FuoHOOYgDhDmjCOurdLqlhArwhkuSo3n8y93fTRKY6ZbFVFqQjPhEEwDllzlzWdTzRLMrMarwwHAdN9wxE0%2B4ZdT8HE96Djl2ATI3T%2FfayUClQqCm%2F4GtLOtCI0XhrUUZPa3xXnh6HrlqfddHPP83K2ZhQOuyvvrUBcC5okqDuKvgON3ixSa0ZhnzjRocLzMOuiOFXDS%2BzR%2BFjDCpGjQlbs5m7tRAQZgObPEoI4bCyLUCSZRJavghQBb%2FbK7jx%2BDsRHpse8ONqt1kOH91h0osj4mWipq8FzQQenp21wA1mtcihYgHGVr7AWV%2BWZ2HN%2FphXN1Mq4T9nwULhQbojJNyg5u4CK2sAFCjwKU8JzthHp%2F0BRB0I%2FiF3ImUzzTUKvhta6hRvQKkVD2G9cYIfSA3s3epxDMolFs28jVxdaPq58lbWeXfFlhz2Yps7VPplcLRApj%2BkQnJM8t7DjKFIcxeYIOomXOwlVMWuzrwyWV3uPHEg0TB4377ZWlZENjCB40%2BSPtfac8J2jIVvMvBGZTMeCLcezzgcB8rMgdoxaKoWHzTYyZJLsX8yjrZK6SlI7k4rqXnD%2F6gDYYYNTczm6WzhMNyq7MMGOqUBNvfn2brgDVFmWoSc7NGR0TWo8CgHeS5kUT6I184KKbSqWxF4nAhm0gLeNYh1E8qI%2BjhfSUpFtAOt%2B0Pp7FN7e77t5yhzTP9%2Be%2FJzQiw4P4UVgemawMy%2FXVrDXQa2FsSPjntfbsdC6prRmq1WQ0lBfKQCKPTGvyc8X7jCg%2BJaS6M%2F%2FhfmD3xrk2RUkTwZ0Yjo8FqAbxD9pVN6x2%2Bq5sK20ejiGd0o&X-Amz-Signature=1bddd7c3d94796d25633dfad5cc2ec810f93267ae272c35410d4b0d0e398f87c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
### （２）Advanced Custom Fieldsプラグインを有効化する。
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/736adce6-a3a4-4a64-9f74-d9aa055c96d2/87f59ba6-b813-4e47-a01d-b9f2de48f1d9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWERSM7G%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T044501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF9Obw1A%2FEQyvnm05veAPEQWJZPuusXTxGY4H6yWo%2BelAiEA5u%2FiCjeJyDgxsS5AvNPHYRje2Ls%2BMz0qYLWmMFSJoHsqiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL7ab0l2QbQIULBXnCrcAy515RyOn314DPJw2dL8P87M0BAVmIofSpOZag%2FuoHOOYgDhDmjCOurdLqlhArwhkuSo3n8y93fTRKY6ZbFVFqQjPhEEwDllzlzWdTzRLMrMarwwHAdN9wxE0%2B4ZdT8HE96Djl2ATI3T%2FfayUClQqCm%2F4GtLOtCI0XhrUUZPa3xXnh6HrlqfddHPP83K2ZhQOuyvvrUBcC5okqDuKvgON3ixSa0ZhnzjRocLzMOuiOFXDS%2BzR%2BFjDCpGjQlbs5m7tRAQZgObPEoI4bCyLUCSZRJavghQBb%2FbK7jx%2BDsRHpse8ONqt1kOH91h0osj4mWipq8FzQQenp21wA1mtcihYgHGVr7AWV%2BWZ2HN%2FphXN1Mq4T9nwULhQbojJNyg5u4CK2sAFCjwKU8JzthHp%2F0BRB0I%2FiF3ImUzzTUKvhta6hRvQKkVD2G9cYIfSA3s3epxDMolFs28jVxdaPq58lbWeXfFlhz2Yps7VPplcLRApj%2BkQnJM8t7DjKFIcxeYIOomXOwlVMWuzrwyWV3uPHEg0TB4377ZWlZENjCB40%2BSPtfac8J2jIVvMvBGZTMeCLcezzgcB8rMgdoxaKoWHzTYyZJLsX8yjrZK6SlI7k4rqXnD%2F6gDYYYNTczm6WzhMNyq7MMGOqUBNvfn2brgDVFmWoSc7NGR0TWo8CgHeS5kUT6I184KKbSqWxF4nAhm0gLeNYh1E8qI%2BjhfSUpFtAOt%2B0Pp7FN7e77t5yhzTP9%2Be%2FJzQiw4P4UVgemawMy%2FXVrDXQa2FsSPjntfbsdC6prRmq1WQ0lBfKQCKPTGvyc8X7jCg%2BJaS6M%2F%2FhfmD3xrk2RUkTwZ0Yjo8FqAbxD9pVN6x2%2Bq5sK20ejiGd0o&X-Amz-Signature=e327dbdde1e3af86437d98dd8fa46be8c882668ce7fe6d7f9c54af58fa122998&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
## 3.カスタムフィールド設定データをインポート
※既に実施済みの場合は、スキップしてください。
### （１）次のjsonファイルをダウンロードする。
- 次のZipファイルをダウンロードして、解凍した「acf-export-mv-slider.json」を使用してください。
### （２）Advanced Custom Fieldの設定画面からインポートする。
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/736adce6-a3a4-4a64-9f74-d9aa055c96d2/0a69829a-437f-430b-b70e-8f3abfd06da6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWERSM7G%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T044501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF9Obw1A%2FEQyvnm05veAPEQWJZPuusXTxGY4H6yWo%2BelAiEA5u%2FiCjeJyDgxsS5AvNPHYRje2Ls%2BMz0qYLWmMFSJoHsqiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL7ab0l2QbQIULBXnCrcAy515RyOn314DPJw2dL8P87M0BAVmIofSpOZag%2FuoHOOYgDhDmjCOurdLqlhArwhkuSo3n8y93fTRKY6ZbFVFqQjPhEEwDllzlzWdTzRLMrMarwwHAdN9wxE0%2B4ZdT8HE96Djl2ATI3T%2FfayUClQqCm%2F4GtLOtCI0XhrUUZPa3xXnh6HrlqfddHPP83K2ZhQOuyvvrUBcC5okqDuKvgON3ixSa0ZhnzjRocLzMOuiOFXDS%2BzR%2BFjDCpGjQlbs5m7tRAQZgObPEoI4bCyLUCSZRJavghQBb%2FbK7jx%2BDsRHpse8ONqt1kOH91h0osj4mWipq8FzQQenp21wA1mtcihYgHGVr7AWV%2BWZ2HN%2FphXN1Mq4T9nwULhQbojJNyg5u4CK2sAFCjwKU8JzthHp%2F0BRB0I%2FiF3ImUzzTUKvhta6hRvQKkVD2G9cYIfSA3s3epxDMolFs28jVxdaPq58lbWeXfFlhz2Yps7VPplcLRApj%2BkQnJM8t7DjKFIcxeYIOomXOwlVMWuzrwyWV3uPHEg0TB4377ZWlZENjCB40%2BSPtfac8J2jIVvMvBGZTMeCLcezzgcB8rMgdoxaKoWHzTYyZJLsX8yjrZK6SlI7k4rqXnD%2F6gDYYYNTczm6WzhMNyq7MMGOqUBNvfn2brgDVFmWoSc7NGR0TWo8CgHeS5kUT6I184KKbSqWxF4nAhm0gLeNYh1E8qI%2BjhfSUpFtAOt%2B0Pp7FN7e77t5yhzTP9%2Be%2FJzQiw4P4UVgemawMy%2FXVrDXQa2FsSPjntfbsdC6prRmq1WQ0lBfKQCKPTGvyc8X7jCg%2BJaS6M%2F%2FhfmD3xrk2RUkTwZ0Yjo8FqAbxD9pVN6x2%2Bq5sK20ejiGd0o&X-Amz-Signature=692895692b0f591e78d9b92281e48bee2bd199a15965a580fbc455148caa5a3c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
### （３）スライダーの設定ができていることを確認する
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/736adce6-a3a4-4a64-9f74-d9aa055c96d2/15926675-6fb6-4aa5-a392-859488b39a11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWERSM7G%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T044501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF9Obw1A%2FEQyvnm05veAPEQWJZPuusXTxGY4H6yWo%2BelAiEA5u%2FiCjeJyDgxsS5AvNPHYRje2Ls%2BMz0qYLWmMFSJoHsqiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL7ab0l2QbQIULBXnCrcAy515RyOn314DPJw2dL8P87M0BAVmIofSpOZag%2FuoHOOYgDhDmjCOurdLqlhArwhkuSo3n8y93fTRKY6ZbFVFqQjPhEEwDllzlzWdTzRLMrMarwwHAdN9wxE0%2B4ZdT8HE96Djl2ATI3T%2FfayUClQqCm%2F4GtLOtCI0XhrUUZPa3xXnh6HrlqfddHPP83K2ZhQOuyvvrUBcC5okqDuKvgON3ixSa0ZhnzjRocLzMOuiOFXDS%2BzR%2BFjDCpGjQlbs5m7tRAQZgObPEoI4bCyLUCSZRJavghQBb%2FbK7jx%2BDsRHpse8ONqt1kOH91h0osj4mWipq8FzQQenp21wA1mtcihYgHGVr7AWV%2BWZ2HN%2FphXN1Mq4T9nwULhQbojJNyg5u4CK2sAFCjwKU8JzthHp%2F0BRB0I%2FiF3ImUzzTUKvhta6hRvQKkVD2G9cYIfSA3s3epxDMolFs28jVxdaPq58lbWeXfFlhz2Yps7VPplcLRApj%2BkQnJM8t7DjKFIcxeYIOomXOwlVMWuzrwyWV3uPHEg0TB4377ZWlZENjCB40%2BSPtfac8J2jIVvMvBGZTMeCLcezzgcB8rMgdoxaKoWHzTYyZJLsX8yjrZK6SlI7k4rqXnD%2F6gDYYYNTczm6WzhMNyq7MMGOqUBNvfn2brgDVFmWoSc7NGR0TWo8CgHeS5kUT6I184KKbSqWxF4nAhm0gLeNYh1E8qI%2BjhfSUpFtAOt%2B0Pp7FN7e77t5yhzTP9%2Be%2FJzQiw4P4UVgemawMy%2FXVrDXQa2FsSPjntfbsdC6prRmq1WQ0lBfKQCKPTGvyc8X7jCg%2BJaS6M%2F%2FhfmD3xrk2RUkTwZ0Yjo8FqAbxD9pVN6x2%2Bq5sK20ejiGd0o&X-Amz-Signature=bc656adc413f7bf8d09972aefb00dc9213c91f0d85b8c925aa158cca3dfb5965&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
## 4.投稿タイプ「MVスライダー」に画像等を設定する
※既に実施済みの場合は、スキップしてください。
### （１）メインビューに表示したい内容を設定する
■設定例
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/736adce6-a3a4-4a64-9f74-d9aa055c96d2/5f7c2b8e-770d-4c04-9d5c-8a567205c8a0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWERSM7G%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T044501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF9Obw1A%2FEQyvnm05veAPEQWJZPuusXTxGY4H6yWo%2BelAiEA5u%2FiCjeJyDgxsS5AvNPHYRje2Ls%2BMz0qYLWmMFSJoHsqiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL7ab0l2QbQIULBXnCrcAy515RyOn314DPJw2dL8P87M0BAVmIofSpOZag%2FuoHOOYgDhDmjCOurdLqlhArwhkuSo3n8y93fTRKY6ZbFVFqQjPhEEwDllzlzWdTzRLMrMarwwHAdN9wxE0%2B4ZdT8HE96Djl2ATI3T%2FfayUClQqCm%2F4GtLOtCI0XhrUUZPa3xXnh6HrlqfddHPP83K2ZhQOuyvvrUBcC5okqDuKvgON3ixSa0ZhnzjRocLzMOuiOFXDS%2BzR%2BFjDCpGjQlbs5m7tRAQZgObPEoI4bCyLUCSZRJavghQBb%2FbK7jx%2BDsRHpse8ONqt1kOH91h0osj4mWipq8FzQQenp21wA1mtcihYgHGVr7AWV%2BWZ2HN%2FphXN1Mq4T9nwULhQbojJNyg5u4CK2sAFCjwKU8JzthHp%2F0BRB0I%2FiF3ImUzzTUKvhta6hRvQKkVD2G9cYIfSA3s3epxDMolFs28jVxdaPq58lbWeXfFlhz2Yps7VPplcLRApj%2BkQnJM8t7DjKFIcxeYIOomXOwlVMWuzrwyWV3uPHEg0TB4377ZWlZENjCB40%2BSPtfac8J2jIVvMvBGZTMeCLcezzgcB8rMgdoxaKoWHzTYyZJLsX8yjrZK6SlI7k4rqXnD%2F6gDYYYNTczm6WzhMNyq7MMGOqUBNvfn2brgDVFmWoSc7NGR0TWo8CgHeS5kUT6I184KKbSqWxF4nAhm0gLeNYh1E8qI%2BjhfSUpFtAOt%2B0Pp7FN7e77t5yhzTP9%2Be%2FJzQiw4P4UVgemawMy%2FXVrDXQa2FsSPjntfbsdC6prRmq1WQ0lBfKQCKPTGvyc8X7jCg%2BJaS6M%2F%2FhfmD3xrk2RUkTwZ0Yjo8FqAbxD9pVN6x2%2Bq5sK20ejiGd0o&X-Amz-Signature=09226bdf3074423e6663b451cb6a937cfbd6c6d3c14f0fd668a9c0025580bb9b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
■設定内容
■参考（テスト用画像は以下から取得しています。申し訳ありませんが、ご準備ください！）
[Bookmark](https://pixabay.com/ja/)
### （２）表示したい件数分登録する
■設定例
  登録日時の降順（以下画面の表示順）で表示されます。
  表示件数、表示順については、「[【2−11】１から作って使えるようにじっくり解説（PHPのコードを詳しく解説](/88a58b7826df4b85923c5f831c63a8d8)」で解説しています。
  ![](https://prod-files-secure.s3.us-west-2.amazonaws.com/736adce6-a3a4-4a64-9f74-d9aa055c96d2/f5ffecc5-4f08-4558-840c-5c6929458a26/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUXQDHB4%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T044502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCeUz%2FKILSXKutssqTn5No5KbWF8ogxr798Gd9r8qRC3QIgcvD8C7CNQk5K08wZTh0m8kZBZ5WmZae4JQ%2FckJYyurMqiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFys4culcw%2Bp8dXUGSrcA9X%2BdznF6X%2BpiX0oxf1npgIWLU%2B7zPvFqZJmxy%2F7UYP%2BPTBFBBxJBPHTiumZ3nukkvOJPC%2FXQTvabJLSmmf%2B8iDe%2BBX3YW%2B%2FYU6ZjSeq2zNxzcKDuQo0rVNDRvujGsQa3nO12HTl6JOYxIEoXbYEnSgwBRd%2FdbHzy6XO7RNZwn6dRy183a9XIVjW3v5Bjks3b5E534CQpowB6VxF0IRZTtsiUiyhV4F32L4hPECPT1DTOxsfSfvULdeA4YoSM91sWUp07bM6Hd5b6xQrgmsZE%2BtMxet8fTuvbfgBz%2FwGTFAaqDNBtpwJ3MVn22kGUlZ3VbeVU%2FC8KaHs8JkP6l4tdCBAqR9gHJ6p7inxbnUS0SWaEEdfrpRXjCo4uv52NF454QzYClOwDxlMjGCb9es86sMJJDOF%2BynOnQMoNh3zKqwdDdYKivee2xXBWQyhprYV7B1Fmh13qZ46e6OA8XqNKeHwON%2BxSNQaxs2rEqfL22t8wq9k9O9Md3X9Z3h4fZA%2BSoAaUhQpA1aeD9T99%2F7pwqyniNxYhtOPpdUPIh0vX1zbxXTfL1SoqJ%2Fg9R2kUbAPep0f87Of5%2B1CTuF8LchHEUs5jDQYlRswqJU9Eb5mqb6pfdlCQ%2FwIQJ%2FsPEIwMP2q7MMGOqUBH6zTEP0TKqA6FCeZ8fPI7esk6nXEHaymjg8KeqE9bTDEEa8at6cWAcNEl3D7%2BhUoio%2F1em7rplaJZxxyGsuNstldLKJKMBykVu7IpVK0Sd6z7x4tsIWJJ79MnX3it%2BBXvtTLYDKBjDPjeiPjixrO%2FF0b24ZFClaK1%2Bn8M5%2BEE1O7mrlGkBnM2DD9tu4e94lHesWBOSFqW2%2FBjvxZ4iqktyGkZcj5&X-Amz-Signature=7c861d3110c2ba2cb7e322e541648e7def4d2af72c3341ec0e52f1a5eb5c5f29&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
## 5.設定確認
### Splideで動作するよう設定する
「$slider_library」を「splide」に設定する。
なお、「$slider_library」は、スライダーの切り替え以外の用途では絶対に使用しないでください！
■parts/functions-lib/func-enqueue-assets.php（一部抜粋）
```php
function my_script_init()
{
  global $slider_library;
  $slider_library = 'splide'; //splide,swiper,slickから選択する

  :（省略）

}
```
## 6.動作確認
### （１）gulpを実行する
※既に実施済みの場合は、スキップしてください
※テーマテンプレート内にある、README.mdもご覧ください。
- gulpfile.jsの設定を変更してください
  ![](https://prod-files-secure.s3.us-west-2.amazonaws.com/736adce6-a3a4-4a64-9f74-d9aa055c96d2/361d857a-b048-4684-ae53-0eaab8de8f48/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNTVSKFT%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T044502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDLmO8tPENvp62nIi2pnH9jotjYz6%2BoFx658%2FgGaCwDmAiBpgyYf7omWDaIQ52yP1R5P%2Bi19wxhLHRCj%2FmgKTdxhAyqIBAid%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMiVH2uzRWWhGINbF2KtwDwXHhgXqtDtkZ2iDcu%2BfyUImKa2b6ey0xTHj3kB%2BbttbWM%2F%2FrmojgDgTSQneY0GdQLBhOo8FASvyofnVPctowUnkI%2FkR%2BDp6qbNh6KVfWDfbkc9R5%2FG3cUrGZ9dDYNh%2BFTu1kbJj%2FnpvMAt7%2B7FDj8Bv4%2FDd4w7pS7gAJy0%2FkKJyf2%2BtQ2xrfJO9y4JItvrsrYGDb3VcXwWHlhcfda%2B92MnJ2Dy6NArlcwf8wq9WDgWnN41aHFNGto0t%2Ft9sZOWF%2FXbWKFj5XTJebcI7wwSEy4dvnit%2FDSK%2FJLi8QnDAaA%2BOoh05MynigVnisr3r43KymGWvQVb5c4FBXQ4ujz5Fk2Ak8M9Lgk1K%2BPEXAQYNtldxLckkFg8hRY8mT26%2FvQ5NteXpTYNbRvCPD2hMcf5GREaXLbMXxSu77pOzrREl%2F%2B338pYIw9ZELjReKckuEbpm2a%2Bk%2Fotr2Sa7dumQTo2I%2FJD6WYQJUUIAwC0Mot%2BTh1xCnzjKJS1MlW0tTVzOqURY%2B0cKFk1fg0bsBztJBjzWaTPSyz39LDX%2FjQARqYk9EOH8eeqwRCqJsiuI9esbnouEjseyg2Q7WD0TZCuRaNedbluOWryLu06G7X6hfzy7mH5Jn%2FiERepmMHo8f4HUw46rswwY6pgFqFPz2xrFf2l%2BaK6MDVoub6xX7UJBHUAr6Hhgft1%2BowSxJqy1C8G%2BaeAL%2FIZzNeb7Hjgx%2FNYyib6q9KS8eJIAavUqeYHQGnvBXTh02R51q5ek83SMgVEJHaTVZ91EbTUuWq3oTlA59JrYqw76tUoSg4ijJ5FXLC1BfhoG6OV5UvMR9P5MIv%2FM%2BwBqV%2FbGweZko4JoLQd26ZTIUkSRSh3NTJmmGHSbX&X-Amz-Signature=e471e89eb8d9d01608dabd086b4994481a950a45f264d1590c347bdca84ad902&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
  
  ![](https://prod-files-secure.s3.us-west-2.amazonaws.com/736adce6-a3a4-4a64-9f74-d9aa055c96d2/e6e5a21a-2bbf-4b67-bf17-c09e645e54ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNTVSKFT%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T044502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDLmO8tPENvp62nIi2pnH9jotjYz6%2BoFx658%2FgGaCwDmAiBpgyYf7omWDaIQ52yP1R5P%2Bi19wxhLHRCj%2FmgKTdxhAyqIBAid%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMiVH2uzRWWhGINbF2KtwDwXHhgXqtDtkZ2iDcu%2BfyUImKa2b6ey0xTHj3kB%2BbttbWM%2F%2FrmojgDgTSQneY0GdQLBhOo8FASvyofnVPctowUnkI%2FkR%2BDp6qbNh6KVfWDfbkc9R5%2FG3cUrGZ9dDYNh%2BFTu1kbJj%2FnpvMAt7%2B7FDj8Bv4%2FDd4w7pS7gAJy0%2FkKJyf2%2BtQ2xrfJO9y4JItvrsrYGDb3VcXwWHlhcfda%2B92MnJ2Dy6NArlcwf8wq9WDgWnN41aHFNGto0t%2Ft9sZOWF%2FXbWKFj5XTJebcI7wwSEy4dvnit%2FDSK%2FJLi8QnDAaA%2BOoh05MynigVnisr3r43KymGWvQVb5c4FBXQ4ujz5Fk2Ak8M9Lgk1K%2BPEXAQYNtldxLckkFg8hRY8mT26%2FvQ5NteXpTYNbRvCPD2hMcf5GREaXLbMXxSu77pOzrREl%2F%2B338pYIw9ZELjReKckuEbpm2a%2Bk%2Fotr2Sa7dumQTo2I%2FJD6WYQJUUIAwC0Mot%2BTh1xCnzjKJS1MlW0tTVzOqURY%2B0cKFk1fg0bsBztJBjzWaTPSyz39LDX%2FjQARqYk9EOH8eeqwRCqJsiuI9esbnouEjseyg2Q7WD0TZCuRaNedbluOWryLu06G7X6hfzy7mH5Jn%2FiERepmMHo8f4HUw46rswwY6pgFqFPz2xrFf2l%2BaK6MDVoub6xX7UJBHUAr6Hhgft1%2BowSxJqy1C8G%2BaeAL%2FIZzNeb7Hjgx%2FNYyib6q9KS8eJIAavUqeYHQGnvBXTh02R51q5ek83SMgVEJHaTVZ91EbTUuWq3oTlA59JrYqw76tUoSg4ijJ5FXLC1BfhoG6OV5UvMR9P5MIv%2FM%2BwBqV%2FbGweZko4JoLQd26ZTIUkSRSh3NTJmmGHSbX&X-Amz-Signature=09d33e801bbc9daa2e2d8715c2d916a6e335ef451e5ec19a53325daa60f6d6d5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
  - 管理画面のURLのうち上記のように、「/wp-admin/…」より前の部分をコピーして、以下、gulpfile.jsの
  ```php
const browserSyncOption = {
  proxy: "http://toolwordpress.local",// ローカルにある「Site Domain」に合わせる
  notify: false,// ブラウザ更新時に出てくる通知を非表示にする
}
  ```
- VSCodeで「Command（Ctrl）+J」 でターミナルを起動します。
- gulpフォルダに移動して、gulpを実行してください
```plain text
//以下を１行ずつ実行してください
cd gulp
npm i
npx gulp
```
※gulpの実行は、Node.js、npmのインストールが前提になりますので、インストールされていない場合は、以下参考にインストール後、gulpの実行を行ってください。
■参考（Node.js、npmのインストール　Macの場合）
[Bookmark](https://tips-web.net/gulp4-mac/)
■参考（Node.js、npmのインストール　Macの場合）
[Bookmark](https://tips-web.net/gulp4-windows/)
### （２）設定した内容でスライダーが動くことを確認する
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/736adce6-a3a4-4a64-9f74-d9aa055c96d2/f6af8c0f-d2f5-4dd2-b74f-cfeed7256bf0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWERSM7G%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T044501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF9Obw1A%2FEQyvnm05veAPEQWJZPuusXTxGY4H6yWo%2BelAiEA5u%2FiCjeJyDgxsS5AvNPHYRje2Ls%2BMz0qYLWmMFSJoHsqiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL7ab0l2QbQIULBXnCrcAy515RyOn314DPJw2dL8P87M0BAVmIofSpOZag%2FuoHOOYgDhDmjCOurdLqlhArwhkuSo3n8y93fTRKY6ZbFVFqQjPhEEwDllzlzWdTzRLMrMarwwHAdN9wxE0%2B4ZdT8HE96Djl2ATI3T%2FfayUClQqCm%2F4GtLOtCI0XhrUUZPa3xXnh6HrlqfddHPP83K2ZhQOuyvvrUBcC5okqDuKvgON3ixSa0ZhnzjRocLzMOuiOFXDS%2BzR%2BFjDCpGjQlbs5m7tRAQZgObPEoI4bCyLUCSZRJavghQBb%2FbK7jx%2BDsRHpse8ONqt1kOH91h0osj4mWipq8FzQQenp21wA1mtcihYgHGVr7AWV%2BWZ2HN%2FphXN1Mq4T9nwULhQbojJNyg5u4CK2sAFCjwKU8JzthHp%2F0BRB0I%2FiF3ImUzzTUKvhta6hRvQKkVD2G9cYIfSA3s3epxDMolFs28jVxdaPq58lbWeXfFlhz2Yps7VPplcLRApj%2BkQnJM8t7DjKFIcxeYIOomXOwlVMWuzrwyWV3uPHEg0TB4377ZWlZENjCB40%2BSPtfac8J2jIVvMvBGZTMeCLcezzgcB8rMgdoxaKoWHzTYyZJLsX8yjrZK6SlI7k4rqXnD%2F6gDYYYNTczm6WzhMNyq7MMGOqUBNvfn2brgDVFmWoSc7NGR0TWo8CgHeS5kUT6I184KKbSqWxF4nAhm0gLeNYh1E8qI%2BjhfSUpFtAOt%2B0Pp7FN7e77t5yhzTP9%2Be%2FJzQiw4P4UVgemawMy%2FXVrDXQa2FsSPjntfbsdC6prRmq1WQ0lBfKQCKPTGvyc8X7jCg%2BJaS6M%2F%2FhfmD3xrk2RUkTwZ0Yjo8FqAbxD9pVN6x2%2Bq5sK20ejiGd0o&X-Amz-Signature=b05e817029060aa2aface636fd6c367234b2df77c3e18b030669b90dbf12bbba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
## 7.CSSの設定
- 必要に応じて設定してください。スライダーに関連した設定は以下の通り設定しています。
- 複数のスライダーで個別の設定を行う可能性を考慮して、スライダー固有のクラスである「splide」、「splide__slide」などに対して直接CSSを当てずに、親である「p-top-mv-splide」の子クラスに対してCSSを当てる形をとっています。
■src/scss/object/project/p-top-mv-splide.scss
```sass
@use 'foundation' as *;
.p-top-mv-splide__inner {
  margin: 5% 5% 0 5%;
}

.p-top-mv-splide .splide {

}

.p-top-mv-splide .splide__slide {
  display: block;
  width: 100%;
  aspect-ratio: 600 / 300;
}

.p-top-mv-splide .splide__slide picture {
  height: inherit;
  height: 100%;
}

.p-top-mv-splide .splide__slide img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
```
# 今回行ったこと
Splide.jsを使用してスライダーのテンプレートを作成する
【手順】
1.テンプレートファイルをテーマとして設定する
2.Advanced Custom Fieldsプラグインをインストール
3.カスタムフィールド設定データをインポート

## タグ

#Web制作 

## 関連ドキュメント

- [[../04_ビジネス/テンプレート.md|テンプレート]]
- [[../99_その他/JS.md|JS]]
- [[../99_その他/width.md|width]]
- [[../99_その他/Advanced Custom Fields.md|Advanced Custom Fields]]
- [[../99_その他/目次.md|目次]]
