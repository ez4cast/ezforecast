import os
import sys

project = 'eZforecast'
copyright = '2021, eZforecast'
author = 'ezforecast'
version = '0.0.1'
release = '0.0.1'
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
pygments_style = 'sphinx'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['static']

autodoc_default_options = {
    'special-members': '__init__',
}

sys.path.insert(0, os.path.abspath('../..'))
extensions = ['sphinx.ext.autodoc', 'sphinx_rtd_theme']
