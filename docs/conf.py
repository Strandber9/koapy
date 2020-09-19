#!/usr/bin/env python
#
# koapy documentation build configuration file, created by
# sphinx-quickstart on Fri Jun  9 13:47:02 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another
# directory, add these directories to sys.path here. If the directory is
# relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
#
import os
import sys

# -- Directory and import setting ---

doc_dir = os.path.abspath(os.path.dirname(__file__))
project_dir = os.path.abspath(os.path.join(doc_dir, '..'))
module_dir = os.path.abspath(os.path.join(project_dir, 'koapy'))

sys.path.insert(0, project_dir)

import koapy

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.githubpages',
    'sphinx.ext.imgconverter',
    'sphinx.ext.todo',
]

autosummary_generate = True

# -- Apidoc hook setting ---
# https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html

from sphinx.ext import apidoc

def run_apidoc(_):
    apidoc.main(['-e', '-o', doc_dir, module_dir, '--force', '--doc-project', 'Koapy'])

def setup(app):
    app.connect('builder-inited', run_apidoc)

# -- Autoapi setting ---
# https://github.com/readthedocs/sphinx-autoapi
# See also if interested, https://github.com/rdb/sphinx-autopackagesummary

extensions.append('autoapi.extension')

autoapi_type = 'python'
autoapi_dirs = [module_dir]

# -- Autodoc configuration ---

autodoc_mock_imports = ['PyQt5', 'sip', 'numpy', 'pandas']
autodoc_warningiserror = True

# -- Autodoc mocking configuration ---

from unittest.mock import MagicMock

class QClass:
    pass

PyQt5 = MagicMock()
PyQt5.QtWidgets.QWidget = QClass
PyQt5.QtCore.QObject = QClass

sys.modules.update({
    'PyQt5.QtWidgets': PyQt5.QtWidgets,
    'PyQt5.QtCore': PyQt5.QtCore,
})

# -- Warnings related setting ---

suppress_warnings = []
keep_warnings = True

# -- Translation related configuration ---

gettext_uuid = True
gettext_compact = False

# -- General configuration ---------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'KOAPY'
copyright = "2020, Yunseong Hwang" # pylint: disable=redefined-builtin
author = "Yunseong Hwang"

# The version info for the project you're documenting, acts as replacement
# for |version| and |release|, also used in various other places throughout
# the built documents.
#
# The short X.Y version.
version = koapy.__version__
# The full version, including alpha/beta/rc tags.
release = koapy.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output -------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a
# theme further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for HTMLHelp output ---------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'koapydoc'


# -- Options for LaTeX output ------------------------------------------

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'preamble': r"""
    \usepackage{kotex}
    """,
    'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass
# [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'koapy.tex',
     'KOAPY Documentation',
     'Yunseong Hwang', 'manual'),
]


# -- Options for manual page output ------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'koapy',
     'KOAPY Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'koapy',
     'KOAPY Documentation',
     author,
     'koapy',
     'One line description of project.',
     'Miscellaneous'),
]
