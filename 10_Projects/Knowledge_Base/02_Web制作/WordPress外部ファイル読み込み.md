---
notion_id: 5a9d6d94-f9a3-4d4d-bf7b-a6274947fdd4
account: Secondary
title: WordPress外部ファイル読み込み
url: https://www.notion.so/WordPress-5a9d6d94f9a34d4dbf7ba6274947fdd4
created_time: 2022-04-22T00:56:00.000Z
last_edited_time: 2022-04-22T02:04:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.529223
---
# WordPress外部ファイル読み込み

### 目的・やりたいこと
- GSAPをWordPress内で実装
### やり方・方法
- wp_enqueue_script　関数を使ってGSAP公式HPよりCDNを読み込む
### エラー
<details>
<summary>エラー１（ブラウザがエラー表示で見れない）</summary>
</details>
  - 赤枠と黄枠に注目
  - ブラウザの表示
<details>
<summary>エラー２（GSAPが効いていない）</summary>
</details>
  - 赤枠と黄線に注目
  - ブラウザの表示
### 解決法
<details>
<summary>解決法１（ブラウザがエラー表示で見れない）</summary>
</details>
  - 一つのファイルに対して$handle、$depsの表示を同じにしない
例）$handle→gsap-js、$deps→gsap
  ![](https://prod-files-secure.s3.us-west-2.amazonaws.com/d58fe38c-a9d4-4466-aed9-85604b7b2c6d/f2d6ce96-8533-4f61-ba53-fe0410a5faaa/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88_2022-04-21_16.47.23.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W2NIE2ZF%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T061110Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDaR17iCO1jVFmTIvaFKQ0KUT4MJzseeC3dcArNscmpzwIgK%2BgcZ8vI93ccecfLfeNSCC7HABEDA1gJhKxdomoTXL4qiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJE3tY348ghLoGLT6yrcA1xwKaZ4t0sH9sPSQPR8xP4vwCso%2F29XhXHgoq%2FJRsrGRedX5eBxxs7Dx06j8u2UHZ2QwwL37XMiiN%2FvPBHqOumt%2FuA4G8qiULdRYSixDK%2FthwBG1dMoyoVcNPs5kS2eANRzjMRgOmRJ6z5h1OReSAxqcT9nXwK6myshVJs3fupW09XPoZ5tlLyDm3%2FioOGfNDGszeylc%2BwXRkprBxJZq0WQg2ppJZ3UU67XMZOvySBgAb8KUMKVqp8UGlIaTpeyR8i2YM56%2BERAZF%2BRbu12LmDHPD9CiwcgeiVh1w%2FjGf0kTmdHDXwxY9Bj%2Fk%2FwKOj0aFAW34%2FbdDofHWWUyPDOSPw3iIjIReWRydsDXtG8crvEJF%2FotUYOOLxhzli6V2kG8DSuzvarhYsxG%2BgkGwSG9ZIVyYwnEe4%2BEgcPT0IzDl92MVwEEcCRZ4BVUM91GObD7lgcnBOwbPfORKwHxYFjcc11YX9M4U9hZjZF8VvOJ7rbRkipkxryyp2s2ZCFmncbWFKN0QnIvwXd%2BN9MhP9tZp6hnIH9lWX1M3ixubqG5lgav7QAhDKTei9x%2Fcs0wwHVcD8CgTHtRsyIy2x6WpmBbEuiHvbVujlxLA2%2BsFxO%2FBSsWKM%2F7dwRuRxx05KeMLvF7MMGOqUB2zCZAJDDObphosIhKEdee9mV%2BPaW50n8QAl8%2BNcdkTb5wNnKVzbkpBc6sPGGbBrL0h5AFTsmr7cLwnV3ncad%2BtoIUywlwEjd8DlrIsv3Pevp%2BBkTAIyr8zX7nW%2Figwh7nc7LgrXwsyJssQEWYFy7CjmliPB6N%2B58D0%2FzH5lAFPpLvamII65O1Ncw1hSzqXrBb4wPdNAyCZuEiBMnDuSikYyJqt4P&X-Amz-Signature=a0ef8b91fbf07a104b0e46d9193e927ec88e3acb328d4d2c77b73c2303e9e9ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
  - ブラウザの表示（元に戻るが、GSAPが効いていない）
<details>
<summary>解決法２（GSAPが効いていない）</summary>
</details>
  - 関数の引数の意味を理解する
  ```php
wp_enqueue_script($handle, $src, $deps, $ver, $in_footer);
  ```
  <details>
  <summary>3つのgsapファイルについて</summary>
  </details>
  - 【$handle：custom-gsap】
　GSAPのメインCDNなのでどこにも依存しない（$deps：false or array()でOK）
  - 【$handle：gsap-ScrollTrigger】
　GSAPのメインCDNに依存する（$deps：array(’custom-gsap’)となる）
  - 【$handle：gsap-js】
　GSAPのメインCDNに依存する（$deps：array(’custom-gsap’)となる）
  ※読み込む順番も大事！！（上から順に読み込まれることを考えておく）
  ![](https://prod-files-secure.s3.us-west-2.amazonaws.com/d58fe38c-a9d4-4466-aed9-85604b7b2c6d/bdcf49fc-a8eb-4dc2-8865-83427794636b/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88_2022-04-22_10.54.20.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643UJXUDS%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T061110Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICrotd3Xi5hQrCBJ%2BtYOCCGYUIFz9t6eoc2%2FbHS9sIw%2BAiBYZEowmSl4XbeU80NMjIO58GtMjjRN6aNUXTdu8BLA0CqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7dIQShlXikobcph0KtwDobtST4VSwWHi8seOpg9oeJh0VeRCOXgsRJDkfrwC23DNLvOnscVY97ityMaFGgRp%2B41fjSM0ANJ%2BvelDtT%2BQXwkMq7yZ5ZlqCImojhaSc5U5V3vXZZ9Prj9JVaHyOsGpudQBMr7ylw%2FCEdiqNQof6GRcwEH7KdWafk1R1nUz7MQyZ7nC17sx957T7Ff4m9opX7BR3fhZ5OFflrkVCfKgyvC9juPBywfBivb1rhRxa4cJKX9qYi6%2FtMZABG9CHtj3SpZ%2BbizlnLaDURA3EzfeKs6TO6Ad9jeBlaEsj2jIb7HTSxp70GGZ4GoJ%2FVNw47u%2Fkg12qF1w0XFDrl1zcrBCrdhgAZai2Mlvaq9oIkH%2BwoprO4bM%2FpxetAMq5PTTdJNS4u17q3stfPoDgXoRwN9LmxNMWJIYHEEYJJKwCmUfL4NU0xGMItKjA0Fy1iM2azi7fcSmWXJHxqOCeQHjqILaW9TlvNySu1Ib51Gf70NdpBlyj02YpFufoOM%2B9B9QotZjYEk%2B%2Fx0MxrXRlnWkpFUiA3Z2OdLNK0vi12jim2e9m%2FH%2FF5G49gNS5NW2u24%2BZZ38ogO7o8QVt61bjwaddx1eJWAnR1Q6TL4%2F5STGE4zNbYj%2BnOMLLa6e5GShaRswrsXswwY6pgGB5wy4IbgfUUEE3R3E6zwPVGRKMWNjRtVhBt%2F3kacbY8Inw5Nn1QNK%2BS%2F9vqcEJiAHxon4XOYF2rvGsQMzNcQXrJTlQzoHMelYCyWwXDVrHeJXcuElH6reyopQaFmIc5Qsy%2BA7Edjm3gIfx2noIeCTu8642YglzkCy7CIGf5afUUhjXgkPa5uX6QsOs3%2FD2%2B32fE9ULo8xO%2BDO2udJivfxE9mtu2UI&X-Amz-Signature=216f34222d540cd37cd0e15fc58c5b3d9528d430816f24bc9276ba1bb3827300&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
  - ブラウザの表示（きちんと読み込まれた！）
[Bookmark](https://wemo.tech/205)

## タグ

#Web制作 

## 関連ドキュメント

- [[../02_Web制作/chouetteria シュエッテリア様.md|chouetteria シュエッテリア様]]
- [[../02_Web制作/GSAP.md|GSAP]]
- [[../02_Web制作/三友運輸株式会社様 コーポレートサイト.md|三友運輸株式会社様 コーポレートサイト]]
- [[../02_Web制作/WordPress案件見積もり方法.md|WordPress案件見積もり方法]]
- [[../02_Web制作/コーポレートサイト部分WP化.md|コーポレートサイト部分WP化]]
