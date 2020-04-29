"""Python wrapper around the M-Files API.

Simplifies search, upload, download and creation of objects in M-Files vaults.
When authentication is needed credentials are fetched from environment
variables ``MFILES_USER`` and ``MFILES_PASS``. If they are not set the
credentials are fetched from user input using ``input()`` and ``get_pass()``.
To supply credentials programatically you can initialize the ``MFilesClient()``
object with username and password.

M-Files property IDs for all object types are abstracted, so you can upload a
``Document`` using ``upload_file()`` with ``object_type="Document"`` and
correct IDs will be fetched from the server.
"""

from mfiles.client import MFilesClient
from mfiles.errors import MFilesException
