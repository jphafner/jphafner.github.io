#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jeffrey P Hafner'
SITENAME = u'jphafner'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'
LOCALE = 'en_US.UTF-8'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'https://github.com/jphafner'),
          ('facebook', 'https://facebook.com/jhafne'),
          ('Linkedin', 'https://linkedin.com/in/jphafner'),)

DEFAULT_PAGINATION = 10

THEME = "/home/ballbot/Projects/pelican-themes/notebook"
#THEME = "/home/ballbot/Projects/pelican-themes/mnmlist"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

