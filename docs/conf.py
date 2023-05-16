# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'crepes'
copyright = '2023, Henrik Boström'
author = 'Henrik Boström'

# The short X.Y version
version = '0.4.0'

# The full version, including alpha/beta/rc tags
release = '0.4.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "numpydoc",
    "nbsphinx",
    "myst_parser",
#    'jupyter_sphinx'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


pygments_style = "sphinx"

# -- Options for HTML output -------------------------------------------------

html_theme = "pydata_sphinx_theme"

html_theme_options = {
    "navbar_end": ["navbar-icon-links"],
    "sidebarwidth": 270,
    "collapse_navigation": False,
    "navigation_depth": 4,
    "show_toc_level": 2,
    "github_url": "https://github.com/henrikbostrom/crepes"
}


html_sidebars = {}

html_context = {
    "default_mode": "light",
}

html_title = f"{project} v. {version}"
html_last_updated_fmt = "%b %d, %Y"


# -- Extension configuration -------------------------------------------------

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

autoclass_content = "both"

autodoc_member_order = "bysource"
autoclass_member_order = 'bysource'

autosummary_generate = True
autosummary_imported_members = True

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True
