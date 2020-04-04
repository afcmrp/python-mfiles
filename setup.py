from setuptools import setup, find_packages

setup(
    name = 'mfiles',
    packages = find_packages(),
    version = '0.1',
    license='MIT',
    description = 'M-Files API wrapper',
    author = 'Emil Hjelm',
    author_email = 'emil.hjelm@climeon.com',
    url = 'https://github.com/afcmrp/mfiles',
    download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',
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
