#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Doc'
SITEURL = ''
SITENAME = "ildoc's"
SITETITLE = "ildoc's"
SITESUBTITLE = ''
SITEURL = 'http://localhost:8000'

DELETE_OUTPUT_DIRECTORY = True

PATH = 'content'
ARTICLE_PATHS = ['posts']
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
STATIC_PATHS = [
    'images',
    'extra/robots.txt',
    'extra/favicon.ico'
]
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

PLUGIN_PATHS = ['plugins']
PLUGINS = ['sitemap']

DEFAULT_METADATA = {
    'status': 'draft',
}

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

ROBOTS = 'index, follow'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'Italian'

GITHUB_URL = 'http://github.com/ildoc/'
DISQUS_SITENAME = ''


THEME = 'theme/pelican-blue'
THEME_STATIC_DIR = THEME + '/static'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
MENUITEMS = (('Home', '/'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/il_doc'),
          ('GitHub', 'https://github.com/ildoc'),)

DEFAULT_PAGINATION = 10

DATE_FORMATS = {
    'it': '%a, %d/%m/%Y',
}

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}


# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
