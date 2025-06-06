# noqa: INP001
import sys
from pathlib import Path

sys.path.insert(0, str(Path("../../").resolve()))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "NMEA2000"
copyright = "2022, Finn Böger"  # noqa: A001
author = "Finn Böger"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.autodoc", "sphinx.ext.viewcode", "sphinx_autodoc_typehints"]

autodoc_default_flags = [
    "members",
    "undoc-members",
    "private-members",
    "special-members",
    "inherited-members",
    "show-inheritance",
]
autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "special-members": "__init__",
    "undoc-members": True,
    "exclude-members": None,
    "show-inheritance": True,
    "private-members": None,
}
always_document_param_types = False
typehints_use_signature = True
typehints_use_signature_return = True
typehints_defaults = "comma"
templates_path = ["_templates"]
exclude_patterns: list[str] = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
