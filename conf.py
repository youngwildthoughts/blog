# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/blog/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Prism",
    "type": "git",
    "url": "https://github.com/Reedo0910/Maverick-Theme-Prism.git",
    "branch": "deploy"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "youngwildthoughts/blog@gh-pages"
}

# 站点设置
site_name = "少年奇思录"
site_logo = "${static_prefix}logo.png"
site_build_date = "2020-07-23T10:51+08:00"
author = "xiezy thomas"
email = "xiezy.thomas@foxmail.com"
author_homepage = "https://www.imalan.cn"
description = "旅程本身即是奖赏!"
key_words = ['interesting', 'blog']
language = 'zh-CN'
external_links = [
    {
        "name": "Maverick",
        "url": "https://youngwildthoughts.github.io/",
        "brief": "来点正经的"
    },
    {
        "name": "🕺",
        "url": "https://space.bilibili.com/404796475",
        "brief": "聊点八卦的"
    }
]
nav = [
    {
        "name": "主页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "合集",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "找我",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]



head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
