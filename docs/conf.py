# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Quantity Test'
copyright = '2026, Stuart Mumford'
author = 'Stuart Mumford'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
import astropy.units as u
from typing import Annotated, get_origin

extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon", "sphinx.ext.intersphinx"]

use_sphinx_autodoc_typehints = True
if use_sphinx_autodoc_typehints:
    extensions += ["sphinx_autodoc_typehints"]
    typehints_annotated_metadata = (u.Unit, str, u.PhysicalType, u.IrreducibleUnit)
else:
    autodoc_typehints = "description"

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "astropy": ("https://docs.astropy.org/en/stable/", None),
}

def quantity_formatter(annotation, config):
    if (get_origin(annotation) is Annotated) and issubclass(annotation.__origin__, u.Quantity):
        metadata = getattr(annotation, "__metadata__", None)
        if metadata and isinstance(metadata[0], (u.Unit, u.IrreducibleUnit, u.CompositeUnit, u.PhysicalType)):
            atype = annotation.__origin__
            atype_name = atype.__name__
            atype_fqn = f"{atype.__module__}.{atype_name}"
            if isinstance(metadata[0], u.PhysicalType):
                aunit = str(metadata[0])
            else:
                aunit = metadata[0].to_string()
            return f":class:`{atype_name}[{aunit}] <{atype_fqn}>`"

typehints_formatter = quantity_formatter
# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
