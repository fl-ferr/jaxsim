# Configuration file for the Sphinx documentation builder.
import os
import sys

from pkg_resources import get_distribution

if os.environ.get("READTHEDOCS"):
    checkout_name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))
    os.environ["CONDA_PREFIX"] = os.path.realpath(
        os.path.join("..", "..", "conda", checkout_name)
    )

import jaxsim

# -- Version information

sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath("../"))
sys.path.insert(0, os.path.abspath("../../"))

module_path = os.path.abspath("../src/")
sys.path.insert(0, module_path)

__version__ = get_distribution("jaxsim").version

# -- Project information

project = "JAXsim"
copyright = "2022, Artificial and Mechanical Intelligence"
author = "Artificial and Mechanical Intelligence"

release = f"{__version__}"
version = f"main ({__version__})"

# -- General configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
    "sphinx_rtd_theme",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "sphinx_multiversion",
    "enum_tools.autoenum",
    "myst_nb",
    "sphinx_gallery.gen_gallery",
    "sphinxcontrib.collections",
    "sphinx_design",
]

# -- Options for intersphinx extension

language = "en"

html_theme = "sphinx_book_theme"

templates_path = ["_templates"]

html_title = f"JAXsim {version}"

master_doc = "index"

autodoc_typehints_format = "short"

autodoc_typehints = "description"

autosummary_generate = True

epub_show_urls = "footnote"

autodoc_type_aliases = {
    "jaxsim.typing.PyTree": "jaxsim.typing.PyTree",
    "jaxsim.typing.Vector": "jaxsim.typing.Vector",
    "jaxsim.typing.Matrix": "jaxsim.typing.Matrix",
    "jaxsim.typing.Array": "jaxsim.typing.Array",
    "jaxsim.typing.Int": "jaxsim.typing.Int",
    "jaxsim.typing.Bool": "jaxsim.typing.Bool",
    "jaxsim.typing.Float": "jaxsim.typing.Float",
    "jaxsim.typing.ScalarLike": "jaxsim.typing.ScalarLike",
    "jaxsim.typing.ArrayLike": "jaxsim.typing.ArrayLike",
    "jaxsim.typing.VectorLike": "jaxsim.typing.VectorLike",
    "jaxsim.typing.MatrixLike": "jaxsim.typing.MatrixLike",
    "jaxsim.typing.IntLike": "jaxsim.typing.IntLike",
    "jaxsim.typing.BoolLike": "jaxsim.typing.BoolLike",
    "jaxsim.typing.FloatLike": "jaxsim.typing.FloatLike",
}

# -- Options for sphinx-collections

collections = {
    "examples": {"driver": "copy_folder", "source": "../examples/", "ignore": "assets"}
}

# -- Options for sphinx-gallery ----------------------------------------------

sphinx_gallery_conf = {
    "examples_dirs": "_collections/examples",
    "gallery_dirs": ("_collections/generated_examples/"),
    "doc_module": "jaxsim",
    "backreferences_dir": os.path.join("modules", "generated"),
}

# -- Options for myst -------------------------------------------------------
myst_enable_extensions = [
    "amsmath",
    "dollarmath",
]
nb_execution_mode = "force"
nb_execution_allow_errors = False
nb_render_image_options = {}

source_suffix = [".rst", ".md", ".ipynb"]
