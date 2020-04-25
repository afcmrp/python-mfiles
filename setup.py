# pylint: disable=missing-module-docstring

from setuptools import setup, find_packages

PYPI_DESCRIPTION = """
Python wrapper around the M-Files API.

Documentation: https://mfiles.readthedocs.io/en/latest/
"""

setup(
    name='mfiles',
    packages=find_packages(),
    version='0.4.0',
    license='MIT',
    description='M-Files API wrapper',
    long_description=PYPI_DESCRIPTION,
    author='Emil Hjelm',
    author_email='emil.hjelm@climeon.com',
    url='https://github.com/afcmrp/mfiles',
    keywords=['M-Files', 'mfiles', 'REST', 'API'],
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
