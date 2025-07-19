---
notion_id: 93316e00-c639-4321-a2ae-2a9140c5a23f
account: Main
title: Gulpエラー
url: https://www.notion.so/Gulp-93316e00c6394321a2ae2a9140c5a23f
created_time: 2024-01-27T03:17:00.000Z
last_edited_time: 2024-01-27T03:20:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:15.045438
---
# Gulpエラー

Gulpエラー発声
## 現象
npx gulp でエラー
 一度、濃度モジュールを消してもエラーが消えない。
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/736adce6-a3a4-4a64-9f74-d9aa055c96d2/1e0020c9-6e1c-4756-92de-7078d9379d92/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHEFBO2U%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T042317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH2mE7qvoR2yW28kSKJp4i5tDWVMySyjHBY0h8UtUJn%2BAiEAxZrUqeEtKZUbbpHoeHRk3X8xt12%2FN%2BngfNmt%2Fo1CpDQqiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOuzsKxaa9L%2BGRJp%2BCrcA8mbaAkpRHRzigLZWJ2FiTQEMOpCU5N42R%2BVESpmSceotYF8y3J9Si8f04XJtgMu%2FMHXD6LW7YT1xVf6MG%2BwKtL3Xylcsul5aWfZU9Rv6LzaeQ%2BM5RTESGl9YPNGe8efUC8VheL4MVXwMe4xUyiZXvr9NlrNr1gWJ7hHLRrzHtJ3xo3zaJ9fS5CSGJrSbYYItVCrYcPnsE9ANnAYUDcTTcvHlT7nQmEEle9vD4jKwy1NOZ%2FOv13LMW%2BE%2BVGB8%2F6mvp66Czw6sienSIluOW5PGT%2F8cihwDlXr5pZ%2Bf31qK1IbLAxizL%2FCEQOsDGjn%2Fa%2BGW%2FuHaJS9vexsj2gDOtztPorfWGLCJSrN9gXDrEHZrJgbecpPqPi4Pd1S5NjGT6ai4CtaR3lBQFyEjhQjKIOhvKZYwizejTcOX702gaEOju%2FooBZpGS9INMKRUjYisSz50Bi1lTaz4VlJFKW5By6Wtb2RIGLFRchEDzO7nP7J07ltDCochBMJQqXVVJvMc1fFJIOhidGMC8tu0IjmZ4j%2BTSQpPztto6xncMoRya1okWuU41ND7HlD0qOWbb8Ae2DxebFEG112bn1kImY%2BrlstIZYGKTaaaj%2B0nYl%2B0y78xrlOV9zvszXUwiLPU7OEMKSq7MMGOqUBh789kYKDRa6juZiaoyMe2u209SNB7gD267VT8u7nqOGk%2BgVBdV2877rutA7cspdq5dMSmWkWocU4mJ1eh2fIkhrfvjlfiFRy9wVcgRaIcmzOFdJSPEOi3I2OsQo1YQhCdK3ZJovmlWj7ydTBc6y66T5hh0Y0cRs%2F%2BHsYFmX7D0ZlFy8Ccfm%2BwZaCPDuFZp3JQNwkIH%2FH1NmVsKSCqjYd8Bfk%2FO53&X-Amz-Signature=e4496699ce144d4607586744b428a7db6dbd67fcaef5ca31c24d115dee3597c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```plain text
Error: listen EADDRINUSE: address already in use :::3001
```
上記エラーで検索
出てきた記事↓
[Bookmark](https://qiita.com/YukiYamam/items/a29ede2a77ce9535886d)
要は外で3001が使われているから、もう使えないよと言うエラー
記事を参照して解決しました！
複数ガルプを立ち上げたときに起こる可能性がある？（でも、これまでは特にエラーなかった）

## タグ

#その他 

## 関連ドキュメント

- [[../99_その他/JS.md|JS]]
- [[../99_その他/Untitled.md|Untitled]]
- [[../99_その他/gulp.md|gulp]]
- [[../99_その他/x.md|x]]
- [[../99_その他/y.md|y]]
