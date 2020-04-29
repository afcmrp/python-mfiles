.. include:: doc/badges.rst

Introduction
-------------
Python wrapper around the M-Files API. Simple examples for how to use it can be
found under ``examples/``.

Install
-------------

To use this library, install the python requirements:

::

    pip install mfiles


You can also use Git to clone the repository from GitHub to install the latest
development version:

::

    git clone https://github.com/afcmrp/mfiles.git
    cd mfiles
    pip install .

Development
-------------

Code follows PEP-8. Docstrings follow Google Python style guide docstring
format. To develop and test this library, install the python dev requirements:

::

    pip install -r dev_requirements.txt

Testing
-------------

Testing is done through ``pytest`` and code coverage is done through
``coverage.py``.

Run tests

::

    pytest

Run tests and check coverage

::

    coverage run -m pytest

Check coverage report

::

    coverage report

For html report run

::

    coverage html
