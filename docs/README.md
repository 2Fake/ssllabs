# ssllabs Documentation

The documentation is generated using [Sphinx](https://www.sphinx-doc.org).

## System requirements

Defining the system requirements with exact versions typically is difficult. But there is a tested environment:

* Linux
* Python 3.11.6
* Sphinx 7.2.6
* m2r2 0.3.3
* pydata_sphinx_theme 0.14.4

## Building the docs

First you need to take care of the requirements.

```bash
pip install -e .[docs]
```

Then just use the make file.

```bash
cd docs
make html
```

You will find the build documentation in ```docs/_build/html``` afterwards.
