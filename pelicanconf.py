﻿#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Cow'

SITENAME = u'Coding Our World'
SITEURL = 'http://www.xycoding.com'
SITESUBTITLE = 'Life is not fair -- Get used to it!'

#DISPLAY_PAGES_ON_MENU = True
#DISPLAY_CATEGORIES_ON_MENU = True
MENUITEMS = (
    ('Categories', '/functions/categories.html'),
    ('Tags', '/functions/tags.html'),
    ('Archives', '/functions/archives.html'),
    ('Random Article', '/functions/random.html'),    
)

#DEFAULT_METADATA = (('yeah', 'it is'),)
TIMEZONE = 'Asia/Shanghai'

GITHUB_URL = 'https://github.com/cowfighting'
FACEBOOK_URL = 'https://www.facebook.com/yang.xu.96558061'
GOOGLEPLUS_URL = 'https://plus.google.com/u/0/117263032165097338865'
TWITTER_URL = 'https://twitter.com/xuyangfighting'

DEFAULT_LANG = 'zh'

DEFAULT_PAGINATION = 4

THEME = 'xycoding-gum'

DISQUS_SITENAME = 'xycoding'

GOOGLE_ANALYTICS_ID = 'UA-46026074-1'

GOOGLE_ANALYTICS_SITENAME = 'www.xycoding.com'

ARTICLE_URL = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

#PAGE_URL = 'pages/{slug}.html'
#PAGE_SAVE_AS = 'pages/{slug}.html'

CATEGORIES_URL = 'functions/categories.html'
CATEGORIES_SAVE_AS = 'functions/categories.html'

TAGS_URL = 'functions/tags.html'
TAGS_SAVE_AS = 'functions/tags.html'

ARCHIVES_URL = 'functions/archives.html'
ARCHIVES_SAVE_AS = 'functions/archives.html'

AUTHORS_URL = 'functions/authors.html'
AUTHORS_SAVE_AS = 'functions/authors.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

#FEED_RSS = 'feeds/all.rss.xml'
#CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

# Social widget
SOCIAL = (
    ('RSS', '/feeds/all.atom.xml'),
    ('GitHub', 'https://github.com/cowfighting'),     
    ('FaceBook', 'https://www.facebook.com/yang.xu.96558061'),
    ('StackOverFlow', 'http://stackoverflow.com/users/2664546/cow'),
    (u'微博', 'http://weibo.com/u/1989085547'),
    (u'腾讯微博', 'http://t.qq.com/xuyang1121'),
    ('Qzone', 'http://user.qzone.qq.com/541959443'),
    (u'豆瓣', 'http://www.douban.com/people/38146008/'),
)

# Links
LINKS = (
    ('Python', 'http://python.org/'),
    ('Pelican', 'http://docs.getpelican.com/'),
)

# plugins
PLUGIN_PATH = 'pelican-plugins'
PLUGINS = ['summary','sitemap','random_article','neighbors','global_license']
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.7,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
RANDOM = 'functions/random.html'
LICENSE = '码字比码代码还辛苦，转载请注明来源<a href="http://www.xycoding.com/" target="_blank">Coding Our World</a>'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True



