#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *  # NoQA

SITEURL = 'http://dadounets.me'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

SOCIAL = (
    ('envelope', 'mailto:mariage@dadounets.me'),
    ('rss', SITEURL + '/feeds/all.atom.xml'),
    ('github', 'https://github.com/Natim/mariage'),
)

# Following items are often useful when publishing

DISQUS_SITENAME = "mariageseverineetremy"
