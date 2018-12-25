#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHORS = (
    u'Robin Hubscher',
    u'Mathilde Prudent',
)

SITENAME = u'Mariage Mathilde & Robin'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

# Social widget
SOCIAL = (('Github', 'https://github.com/Natim/mariage-robin-mathilde'),)

DEFAULT_PAGINATION = False

THEME = "pure"

COVER_IMG_URL = '/theme/sidebar.jpg'

SOCIAL = (
    ('envelope', 'mailto:prudent.mathilde@gmail.com,hubscher.phil@gmail.com'),
    ('rss', SITEURL + '/feeds/all.atom.xml'),
    ('github', 'https://github.com/Natim/mariage-robin-mathilde'),
)

MENUITEMS = (
    ('Nouvelles', 'archives.html'),
    (u'Venir', 'pages/venir.html'),
    (u'Se loger', 'pages/se-loger.html'),
    (u'Contactez-nous', 'pages/a-propos.html'),
)
STATIC_PATHS = ['images', 'extra/robots.txt']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
}
PLUGIN_PATHS = ['plugins']
PLUGINS = ['post_stats', 'liquid_tags.video']
RESPONSIVE_IMAGES = True
