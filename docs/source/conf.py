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
from sphinx.ext.apidoc import main

sys.path.insert(0, os.path.abspath('../..'))


### for RTD to run apidoc automatically, code from https://github.com/readthedocs/readthedocs.org/issues/1139

def run_apidoc(_):
    sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    module = os.path.join(cur_dir, '../..', 'pycircle')
    main(['-e', '-o', cur_dir, module, '--force'])        # cur_dir is the output path *.rst will be in

def setup(app):
    app.connect('builder-inited', run_apidoc)


# -- Project information -----------------------------------------------------

project = 'MiscBeginnerSC'
copyright = '2020, beginnerSC'
author = 'beginnerSC'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [  'nbsphinx', 
                'sphinx.ext.autodoc', 
                'sphinx.ext.napoleon',
                'sphinx.ext.mathjax', 
                'sphinx.ext.viewcode', 
                'sphinx_copybutton', 
                'sphinx_rtd_dark_mode'
             ]

default_dark_mode = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'

# import pydata_sphinx_theme
# html_theme = 'pydata_sphinx_theme'


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

master_doc = 'index'
nbsphinx_allow_errors = True
nbsphinx_execute = 'never'
# nbsphinx_prompt_width = 0

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',
#
# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',
#
# Additional stuff for the LaTeX preamble.
#'preamble': '',
'preamble': r'''
\hypersetup{unicode=true}
\usepackage{CJKutf8}
\DeclareUnicodeCharacter{00A0}{\nobreakspace}
\DeclareUnicodeCharacter{2203}{\ensuremath{\exists}}
\DeclareUnicodeCharacter{2200}{\ensuremath{\forall}}
\DeclareUnicodeCharacter{2286}{\ensuremath{\subseteq}}
\DeclareUnicodeCharacter{2713}{x}
\DeclareUnicodeCharacter{27FA}{\ensuremath{\Longleftrightarrow}}
\DeclareUnicodeCharacter{221A}{\ensuremath{\sqrt{}}}
\DeclareUnicodeCharacter{221B}{\ensuremath{\sqrt[3]{}}}
\DeclareUnicodeCharacter{2295}{\ensuremath{\oplus}}
\DeclareUnicodeCharacter{2297}{\ensuremath{\otimes}}
\begin{CJK*}{UTF8}{bsmi}
\AtEndDocument{\end{CJK}}
''',
}
