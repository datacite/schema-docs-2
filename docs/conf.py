# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'DataCite Metadata Schema'
author = 'DataCite Metadata Working Group'
copyright = "Creative Commons Attribution 4.0 International (CC BY 4.0)"
license_url = "https://creativecommons.org/licenses/by/4.0/"

release = '4.6'
version = '4.6'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_comments',
    'sphinx_design'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_logo = "_static/DataCite-Logo_secondary-bicolor-light.png"

html_theme_options = {
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': True
}

# -- Options for EPUB output
epub_show_urls = 'footnote'


# These folders are copied to the documentation's HTML output
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.css',
]

# comments_config = {
#    "utterances": {
#       "repo": "github-org/github-repo",
#       "optional": "config"
#    }
# }

# LaTeX configuration

latex_engine = "xelatex"

# latex_logo = "_static/DataCite-Logo_primary.png"

    # \addto\captionsenglish{\renewcommand{\tablename}{ }}
    # \addto\captionsenglish{\renewcommand{\thetable}{ }}

# Continuous footnote numbering (see https://github.com/sphinx-doc/sphinx/issues/3652)
latex_elements = {
    'releasename': "Version",
    'pointsize': '11pt',
    'sphinxsetup': 'TitleColor={HTML}{434343}, InnerLinkColor={HTML}{0071b2}, OuterLinkColor={HTML}{0071b2}',
    'preamble': r'''
    \usepackage[sfdefault]{roboto}
    \usepackage[T1]{fontenc}
    \usepackage{normalcolor}
    \usepackage{xcolor}
    \definecolor[named]{DarkGrey}{HTML}{434343}
    \setnormalcolor{DarkGrey}
    \renewcommand{\sphinxtablecontinued}[1]{}
    \renewcommand{\familydefault}{\sfdefault}
    \makeatletter
    \def\FNH@footnoteenv@i[#1]{\FNH@footnoteenv}
    \def\FNH@footnotetextenv@i[#1]{\FNH@footnotetextenv}
    \def\sphinxfootnotemark [#1]%
       {\ifx\thepage\relax\else\protect\spx@opt@BeforeFootnote
                                 \protect\footnotemark\fi}%
    \makeatother
'''
}

latex_documents = [
  ('index', 'DataCite-MetadataKernel_v4.6.tex',
    u'DataCite Metadata Schema Documentation',
    u'DataCite Metadata Working Group', 'howto'),
]
