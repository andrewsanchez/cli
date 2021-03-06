from setuptools import setup, find_packages
from pathlib import Path

text = Path("./jupyter_book/__init__.py").read_text()
for line in text.split("\n"):
    if "__version__" in line:
        break
version = line.split("= ")[-1].strip('"')

# Documentation requirements
path_doc_reqs = Path(__file__).parent.joinpath("docs", "requirements.txt")
doc_reqs = [
    ii for ii in path_doc_reqs.read_text().split("\n") if not ii.startswith("#")
]
test_reqs = [
    "coverage",
    "pytest>=3.6,<4",
    "pytest-cov",
    "beautifulsoup4",
    "matplotlib",
    "pytest-regressions",
    "jupytext",
] + doc_reqs
setup(
    name="jupyter-book",
    version=version,
    python_requires=">=3.6",
    author="Project Jupyter Contributors",
    author_email="jupyter@googlegroups.com",
    url="https://jupyterbook.org/",
    project_urls={
        "Documentation": "https://jupyterbook.org",
        "Funding": "https://jupyter.org/about",
        "Source": "https://github.com/jupyter/jupyter-book/",
        "Tracker": "https://github.com/jupyter/jupyter-book/issues",
    },
    # this should be a whitespace separated string of keywords, not a list
    keywords="reproducible science environments scholarship notebook",
    description="Jupyter Book: Create an online book with Jupyter Notebooks",
    long_description=open("./README.md", "r").read(),
    long_description_content_type="text/markdown",
    license="BSD",
    packages=find_packages(),
    install_requires=[
        "pyyaml",
        "docutils>=0.15",
        "sphinx<3",
        (
            "myst-nb @ "
            "https://github.com/ExecutableBookProject/myst-nb/archive/master.zip"  # noqa E501
        ),
        "click",
        "setuptools",
        "nbformat",
        "nbconvert",
        "nbclient",
        (
            "sphinx_togglebutton @ "
            "https://github.com/ExecutableBookProject/sphinx-togglebutton/archive/master.zip"  # noqa E501
        ),
        "sphinx-copybutton",
        "sphinxcontrib-bibtex",
        (
            "sphinx_book_theme @ "
            "https://github.com/ExecutableBookProject/sphinx-book-theme/archive/master.zip"  # noqa E501
        ),
    ],
    extras_require={
        "code_style": ["flake8<3.8.0,>=3.7.0", "black", "pre-commit==1.17.0"],
        "sphinx": doc_reqs,
        "testing": test_reqs,
        "pdf_html": "pyppeteer",
    },
    entry_points={
        "console_scripts": [
            "jb = jupyter_book.commands:main",
            "jupyter-book = jupyter_book.commands:main",
        ]
    },
    package_data={"jupyter_book": ["default_config.yml", "book_template/*"]},
    include_package_data=True,
)
