# pylint: disable=missing-module-docstring

from setuptools import setup, find_packages

PYPI_DESCRIPTION = """
Python wrapper around the M-Files API.

Documentation: https://mfiles.readthedocs.io/en/latest/
"""

setup(
    name='mfiles',
    packages=find_packages(),
    version='0.5.0',
    license='MIT',
    description='M-Files API wrapper',
    long_description=PYPI_DESCRIPTION,
    author='Emil Hjelm',
    author_email='emil.hjelm@climeon.com',
    url='https://github.com/afcmrp/mfiles',
    keywords=['M-Files', 'mfiles', 'REST', 'API'],
    python_requires='!=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Operating System :: OS Independent',
    ],
)
