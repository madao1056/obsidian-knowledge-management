---
notion_id: 72d355cf-3e4e-4ebb-83c4-5827b8e75b8a
account: Secondary
title: GSAP（timelineとscrollTrigger）
url: https://www.notion.so/GSAP-timeline-scrollTrigger-72d355cf3e4e4ebb83c45827b8e75b8a
created_time: 2022-04-24T06:23:00.000Z
last_edited_time: 2022-10-11T13:24:00.000Z
sync_status: placeholder
sync_time: 2025-07-12T15:01:47.471990
---
# GSAP（timelineとscrollTrigger）

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/d58fe38c-a9d4-4466-aed9-85604b7b2c6d/46c28952-eb8a-4029-a7fd-99d0f0a6a8ad/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88_2022-04-24_14.40.39.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632UVS5IB%2F20250719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250719T060627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDKEPNLfyijK1bKabrvGj60npZk3coP2jwooPUm8mcjpAiBBM7y6YNlo8bZs6g2dH8YhlwkJKF%2BvMKxcQEhWfwBrWCqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZi48SAGJxiYue2E9KtwDY2Gas4EHHkUmEBzwk1xkxIByKDbLoJcSRqX%2BzeEDtYYGTaxbTPO9prr5mWi8lyOUshUfHxJX3OmlFBCT1JhdXGlMnnFbOopA%2FMiQ9TfRBqamj4VTJ3LjDqrv759TIBuJVC%2F%2FvJVKWg1R8yTXhxz6vs0eu4lOWrWkxeHGL9A8fdZkrPK1aCjIzVZGkSxzoqU0pgio51xO4z%2Ftq9jHIbQU6I1AR23Aow%2BsLCv6idfCXpR8dK4McMrZbwfv8Ar1xDAftXk6YZe9ItMpUXLxvCC7jupAZP98sntPQKI%2FtgYz5XXjbzlfunYe9Hafk3rYtPQ3hJ3Y5lzQzkU3a9O6aosSu5XsoOSaL1vzaV0J%2FB1F8S629S49FAna6evm%2FN%2BUfeUTSshV3zsY5cCAD0jgBz6wqI39jz8ZVLiEmfaaAcV4hzH5e9JGul%2FKPZBo%2BAG%2F2oSdhfzB5rXjpUCCqwziVoqA5SYhR2yue7Z6SNqFD3Q1bwRcvXprnkDPQvpn%2Fph2NTfHXDhw14A4mhb2H7p%2FOj9NszoqZ9GpxSIQikZkZV2EqkIcMUqwgz46u3o4SMX4ils56rEitlQmi1eXk2x6%2Fnm71hWzvmrA5x4l5rlGTO6F9iCCvL2puLLHcMdHjBUwvsXswwY6pgElpczQQb6jMLuNbjpAFG4OBS2nReHN6MPjFloc4FzuflV3vLEZrfWmRXa4es2Pv7625PkCPwu%2BwITAukXL56YJrQhii4fg2pHqmZp0dVqgYDZmLX2%2FnW50DieAzXAHOk61LBzkhc3l7%2FlUG2KFgSs3DKs921zNl8TOmClbdm%2Brpzodwoyf2E3v1%2BheF%2BrhvQ%2F5g2hB70FtqaQvBqYxyLXvvUYj%2Fx2U&X-Amz-Signature=915b68569227d66b53c8e0dcbc4277cde32cb510bf649df1b744ed758da0c5aa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```javascript
//timelineとscrollTriggerを使ったコード例
const tlWorks = gsap.timeline({
  scrollTrigger: {
    trigger: '.js-works',
    start: 'top 70%',
    markers: true,
  },
});

tlWorks
.from(".js-works", {
  opacity: 0,
  duration: 1.5,
})
  .from(".js-worksL", {
  x: "-100%",
  opacity: 0,
  ease: "back.out(0.7)",
  duration: 1.5,
}, "works")
  .from(".js-worksR", {
  x: "100%",
  opacity: 0,
  ease: "back.out(0.8)",
  duration: 1.5,
}, "works");
```

## タグ

#Web制作 

## 関連ドキュメント

- [[../02_Web制作/GSAP.md|GSAP]]
- [[../99_その他/top.md|top]]
- [[../99_その他/x.md|x]]
- [[../99_その他/y.md|y]]
