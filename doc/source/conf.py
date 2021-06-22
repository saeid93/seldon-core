# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import sphinx_material

sys.path.insert(0, os.path.abspath("../.."))

# -- Project information -----------------------------------------------------

project = "seldon-core"
copyright = "2019, Seldon Technologies Ltd"
author = "Seldon Technologies Ltd"

# The short X.Y version
# import seldon-core

# version = seldon-core.__version__
# The full version, including alpha/beta/rc tags
# release = seldon-core.__version__


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
    #    'recommonmark',
    "m2r2",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    # Automatically generate API docs,
    # see https://github.com/rtfd/readthedocs.org/issues/1139
    "sphinxcontrib.apidoc",
    "nbsphinx",
    "nbsphinx_link",  # for linking notebooks from outside sphinx source root
    # Fix `ipython3` warning
    # https://github.com/spatialaudio/nbsphinx/issues/24
    "IPython.sphinxext.ipython_console_highlighting",
]

# Ignore py:class warnings about 3rd party deps or ignored packages (e.g.
# generated proto)
# https://stackoverflow.com/a/30624034/5015573
nitpick_ignore = [
    ("py:class", "google.protobuf.any_pb2.Any"),
    ("py:class", "google.protobuf.struct_pb2.ListValue"),
    ("py:class", "gunicorn.app.base.BaseApplication"),
    ("py:class", "numpy.ndarray"),
    ("py:class", "pandas.core.frame.DataFrame"),
    ("py:class", "proto.prediction_pb2.DefaultData"),
    ("py:class", "proto.prediction_pb2.Feedback"),
    ("py:class", "proto.prediction_pb2.SeldonMessage"),
    ("py:class", "proto.prediction_pb2.SeldonMessageList"),
    ("py:class", "proto.prediction_pb2.SeldonModelMetadata"),
    ("py:data", "google.protobuf.any_pb2.Any"),
]

# Avoid "Duplicate explicit target name" warnings
m2r_anonymous_references = True

# nbsphinx settings
# nbsphinx_execute = 'auto'
nbsphinx_execute = "never"

# apidoc settings
apidoc_module_dir = "../../python/seldon_core"
apidoc_output_dir = "python/api"
apidoc_excluded_paths = ["**/*test*"]
apidoc_module_first = True

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = False

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = [".rst", ".md"]
# source_suffix = '.rst'

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

is_fast_build = os.environ.get("FAST_BUILD", "False")
if is_fast_build.lower() == "true":
    exclude_patterns = ["examples", "python/api"]

is_linkcheck = os.environ.get("LINKCHECK", "False")
if is_linkcheck.lower() == "true":
    exclude_patterns = [
        # Ignore all PR and issues links
        "reference/changelog.rst",
        # Ignore old releases
        "reference/release-0.2.3.md",
        "reference/release-0.2.5.md",
        "reference/release-0.2.6.md",
        "reference/release-0.2.7.md",
        "reference/release-0.3.0.md",
        "reference/release-0.4.0.md",
        "python/api",
    ]

linkcheck_ignore = [
    # Ignore localhost links
    "http://0.0.0.0",
    "http://localhost",
    # Ignore relative links (i.e. starting with `../` or `./`)
    r"^\.{1,2}/",
    # Ignore image links, which are not getting replaced with the correct link
    # More info in this issue: https://github.com/miyakogi/m2r/issues/49
    r"^(?!http).*\.png$",
    # Ignore Google Calendar links which seem to require auth
    "https://calendar.google.com",
]
# Ignore anchors, as they doesn't seem to work very well
linkcheck_anchors_ignore = [".*"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# Chosen Themes:
# * https://github.com/bashtage/sphinx-material/
# * https://github.com/myyasuda/sphinx_materialdesign_theme
html_theme = "sphinx_material"

if html_theme == "sphinx_material":
    html_theme_options = {
        "google_analytics_account": "GTM-WT76RV",
        "base_url": "https://docs.seldon.io/projects/seldon-core/",
        "color_primary": "indigo",
        "color_accent": "teal",
        "repo_url": "https://github.com/SeldonIO/seldon-core/",
        "repo_name": "Seldon Core",
        "nav_title": "Seldon Core Documentation",
        "globaltoc_depth": 1,
        "globaltoc_collapse": False,
        "globaltoc_includehidden": False,
        "repo_type": "github",
        "nav_links": [
            {
                "href": "https://docs.seldon.io/projects/seldon-core/en/latest/",
                "internal": False,
                "title": "🚀 Our Other Projects & Products:",
            },
            {
                "href": "https://docs.seldon.io/projects/alibi/en/stable/",
                "internal": False,
                "title": "Alibi Explain",
            },
            {
                "href": "https://docs.seldon.io/projects/alibi-detect/en/stable/",
                "internal": False,
                "title": "Alibi Detect",
            },
            {
                "href": "https://github.com/SeldonIO/mlserver",
                "internal": False,
                "title": "MLServer",
            },
            {
                "href": "https://tempo.readthedocs.io/en/latest/",
                "internal": False,
                "title": "Tempo SDK",
            },
            {
                "href": "https://deploy.seldon.io",
                "internal": False,
                "title": "Seldon Deploy (Enterprise)",
            },
            {
                "href": "https://github.com/SeldonIO/seldon-deploy-sdk#seldon-deploy-sdk",
                "internal": False,
                "title": "Seldon Deploy SDK (Enterprise)",
            },
        ],
    }

    extensions.append("sphinx_material")
    html_theme_path = sphinx_material.html_theme_path()
    html_context = sphinx_material.get_html_context()

html_sidebars = {"**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]}

# The Seldon Logo located at the top of the navigation bar.
html_logo = "Seldon_White.png"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.

html_extra_path = ["_extra"]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "seldon-coredoc"

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "seldon-core.tex",
        "seldon-core Documentation",
        "Seldon Technologies Ltd",
        "manual",
    ),
]

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "seldon-core", "seldon-core Documentation", [author], 1)]

# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "seldon-core",
        "seldon-core Documentation",
        author,
        "seldon-core",
        "One line description of project.",
        "Miscellaneous",
    ),
]

# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ["search.html"]

# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {"https://docs.python.org/": None}

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# from https://github.com/vidartf/nbsphinx-link/blob/master/docs/source/conf.py

# Ensure env.metadata[env.docname]['nbsphinx-link-target']
# points relative to repo root:
here = os.path.dirname(__file__)
repo = os.path.join(here, "..", "..")
nbsphinx_link_target_root = repo

# from https://github.com/vidartf/nbsphinx-link/blob/master/docs/source/conf.py for custom tags
import subprocess

try:
    git_rev = subprocess.check_output(
        ["git", "describe", "--exact-match", "HEAD"], universal_newlines=True
    )
except subprocess.CalledProcessError:
    try:
        git_rev = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], universal_newlines=True
        )
    except subprocess.CalledProcessError:
        git_rev = ""
if git_rev:
    git_rev = git_rev.splitlines()[0] + "/"

nbsphinx_prolog = (
    r"""
{% if env.metadata[env.docname]['nbsphinx-link-target'] %}
{% set docpath = env.metadata[env.docname]['nbsphinx-link-target'] %}
{% else %}
{% set docpath = env.doc2path(env.docname, base='docs/source/') %}
{% endif %}

.. only:: html

    .. role:: raw-html(raw)
        :format: html

    .. nbinfo::
        This page was generated from `{{ docpath }}`__.

    __ https://github.com/SeldonIO/seldon-core/blob/
        """
    + git_rev
    + r"{{ docpath }}"
)
