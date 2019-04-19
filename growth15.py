#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itchat
import re
import time
import os

def post(text):
    post_head = """---
layout: post
title: {title}
subtitle:
author: 小武奶奶
date: {date}
categories:
tag:
---

"""
    now = time.localtime()
    title = time.strftime("%Y 年 %m 月 %d 日")
    date = time.strftime("%Y-%m-%d %H:%M:%S +0800")

    content = post_head.format(title=title, date=date)
    content += text
    filename = time.strftime("_posts/%Y-%m-%d-%H-%M-%S-growth15.md")
    with open(filename, 'w') as f:
        f.write(content)

    commit = "git commit -m '{}'".format(title)
    os.system("git add -A")
    os.system(commit)
    os.system("git push")
    print("post done!")

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    text = msg.text
    nickname = msg.user.NickName

    if (nickname == '贾献华' or nickname == '安琴'):
        post(text)

if __name__ == '__main__':
    itchat.auto_login(enableCmdQR=2)
    itchat.run()
