from setuptools import setup, find_packages

PYPI_DESCRIPTION = """
Python wrapper around the M-Files API.

Enables search, upload, download and creation of objects in M-Files vaults.
When authentication is needed credentials are fetched from environment
variables ``MFILES_USER`` and ``MFILES_PASS``. If they are not set the
credentials are fetched from user input using ``input()`` and ``get_pass()``.
To supply credentials programatically you can call the ``login()`` method with
username and password before using the API, and all subsequent calls will be
authenticated with the same token.

M-Files property IDs for all object types are abstracted, so you can upload a
``Document`` using ``upload_file()`` with ``object_type="Document"`` and
correct IDs will be fetched from the server.
"""

setup(
    name = 'mfiles',
    packages = find_packages(),
    version = '0.2',
    license='MIT',
    description = 'M-Files API wrapper',
    long_description = PYPI_DESCRIPTION,
    author = 'Emil Hjelm',
    author_email = 'emil.hjelm@climeon.com',
    url = 'https://github.com/afcmrp/mfiles',
    download_url = 'https://github.com/user/reponame/archive/v_02.tar.gz',
    keywords = ['M-Files', 'mfiles', 'REST', 'API'],
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
