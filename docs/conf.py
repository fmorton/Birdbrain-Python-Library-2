# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.extlinks',
    'sphinx.ext.ifconfig',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
]
source_suffix = '.rst'
master_doc = 'index'
project = 'BirdBrain-Python-Library-2'
year = '2022'
author = 'Frank Morton'
copyright = '{0}, {1}'.format(year, author)
version = release = '0.9.4'

pygments_style = 'trac'
templates_path = ['.']
extlinks = {
    'issue': ('https://github.com/fmorton/BirdBrain-Python-Library-2/issues/%s', 'issue #%s'),
    'pr': ('https://github.com/fmorton/BirdBrain-Python-Library-2/pull/%s', 'PR #%s'),
}
# on_rtd is whether we are on readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only set the theme if we're building docs locally
    html_theme = 'sphinx_rtd_theme'

html_use_smartypants = True
html_last_updated_fmt = '%b %d, %Y'
html_split_index = False
html_sidebars = {
    '**': ['searchbox.html', 'globaltoc.html', 'sourcelink.html'],
}
html_short_title = '%s-%s' % (project, version)

napoleon_use_ivar = True
napoleon_use_rtype = False
napoleon_use_param = False
