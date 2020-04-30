"""Release script to assist pushing new tags and uploading packages to PyPI."""

import os

if __name__ == "__main__":
    new_ver = input("New version: ") # pylint: disable=invalid-name
    os.system("tbump %s" % new_ver)
    os.system("python setup.py sdist")
    os.system("twine upload dist/mfiles-%s.tar.gz" % new_ver)
