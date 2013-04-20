# -*- coding: utf-8 -*-

import sys, os
extensions = []
templates_path = ['/Users/suzukiyousuke/Documents/dev/ebshelf/generator/templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'library-coffeescript'
copyright = u'Copyright (c) 2011 Alexander MacCaw (info@eribium.org)'
language = u'en'
version = '1.0'
release = '1.0'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = '/Users/suzukiyousuke/Documents/dev/ebshelf/generator/templates'

# -- Options for Epub output ---------------------------------------------------
# Bibliographic Dublin Core info.
epub_title = u'The Little Book On CoffeeScript'
epub_author = u'Alexander MacCaw'
epub_publisher = u'generated by ebshelf'
epub_copyright = u'Copyright (c) 2011 Alexander MacCaw (info@eribium.org)'
epub_cover = (u'cover.png','')
epub_identifier = u'https://github.com/minghai/library/tree/master/coffeescript'
epub_scheme = 'URL'
    