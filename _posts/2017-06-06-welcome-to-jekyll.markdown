---
layout: post
title:  "创建 《小武成长记》 网站"
date:   2017-06-06 15:22:50 +0800
categories: jekyll update
---

## 创建 github pages

* <https://github.com/> 登录 github 。
* <https://github.com/organizations/new> 创建一个新的组织 `growth15`, 意为 *小武成长记*。
* <https://github.com/organizations/growth15/repositories/new> 点击右侧 `New` 创建一个仓库 `growth15.github.io`。

## 上传网站

* <https://jekyllrb.com> 使用 `jekyll`

```bash
$ gem install jekyll bundler
$ jekyll new growth15
$ cd growth15
$ bundle exec jekyll serve  # 或者 jekyll serve 访问 http://localhost:4000 预览
$ vim CNAME                 # 内容为 jiaxianhua.com 用于自定义域名
$ vim README.md             # readme 说明文件
$ vim Rakefile              # rake 用于创建新的 post
$ git init
$ git add -A
$ git commit -m "first commit"
$ git remote add origin https://github.com/growth15/growth15.github.io.git
$ git push -u origin master
```

## 配置顶级域名

* <https://www.dnspod.cn/console/dashboard> 在 dnspod 上面配置 DNS

![DNSPod](https://firebasestorage.googleapis.com/v0/b/growth15-a8c59.appspot.com/o/2017%2F06%2F06%2FDNSPod.png?alt=media&token=1e214c48-2875-4dfe-98da-d3d697c6a3a2)

* <https://www.godaddy.com> 在 godaddy 上面购买域名, Godaddy 注册商域名修改DNS地址

![DNS](https://firebasestorage.googleapis.com/v0/b/growth15-a8c59.appspot.com/o/2017%2F06%2F06%2FDNS.png?alt=media&token=ed46dca9-b24f-4c9b-baf5-46a837623d2b)

![Demain](https://firebasestorage.googleapis.com/v0/b/growth15-a8c59.appspot.com/o/2017%2F06%2F06%2FDomains.png?alt=media&token=151988a2-3405-4dd6-b00c-2519d9e54080)

## 存放图片视频

* <https://firebase.google.com> 使用 `firebase` 存储文件
* <https://console.firebase.google.com> 转到控制台，点击 `添加项目`, 项目名称 *growth15*
* <https://console.firebase.google.com/project/growth15-a8c59/storage/files> 点击左侧 `Storage`, 创建文件夹或者上传文件

![firebase](https://firebasestorage.googleapis.com/v0/b/growth15-a8c59.appspot.com/o/2017%2F06%2F06%2Ffirebase.png?alt=media&token=e65742fc-22bc-4486-9191-bff2c49c508c)
![storage](https://firebasestorage.googleapis.com/v0/b/growth15-a8c59.appspot.com/o/2017%2F06%2F06%2FStorage.png?alt=media&token=fde5eb3c-6585-4a95-bad9-9f350bca8ccb)
