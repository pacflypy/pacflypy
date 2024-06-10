import os
import sys
from recommonmark.transform import AutoStructify
import sphinx_rtd_theme

sys.path.insert(0, os.path.abspath('.'))

project = 'pacflypy'
copyright = '2024, paclflypy, Kevin Alexander Krefting'
author = 'paclflypy, Kevin Alexander Krefting'
release = '0.2.4'

extensions = [
    'recommonmark',
    'sphinx_rtd_theme',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'de'

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

def setup(app):
    app.add_config_value('recommonmark_config', {
        'auto_toc_tree_section': 'Contents',
    }, True)
    app.add_transform(AutoStructify)
