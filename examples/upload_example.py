"""Example for how to upload a file to M-Files."""

import mfiles

# Connection details (replace as appropriate)
MY_SERVER = "https://my-mfiles-server.com/REST/" # Enter your M-Files server address here
MY_USER = "TestUser" # Enter your M-Files user name here
MY_PASSWORD = "SecretPassword" # Enter your M-Files password here
MY_VAULT = "{01234567-89AB-CDEF-0123-456789ABCDEF}" # Enter your M-Files vault GUID here

# File info for test file
FILE_NAME = "test_upload.txt"
FILE_CONTENT = "This file was uploaded from Python via the 'mfiles' package."
FILE_TYPE = "Document" # Replace with a object type defined in your server
FILE_CLASS = "General document" # Replace with a object class defined in your server

# Extra info depends on what fields are defined in the M-Files server.
FILE_EXTRA_INFO = {
    "Document Type": "Report",
    "Document Title": FILE_NAME[:-4]
}

# Initialize MFilesClient
my_client = mfiles.MFilesClient(server=MY_SERVER,
                                user=MY_USER,
                                password=MY_PASSWORD,
                                vault=MY_VAULT)

# Create simple file to upload
with open(FILE_NAME, mode="w+") as f:
    f.write(FILE_CONTENT)

# Upload file using property IDs. Using the default IDs 0 is usually accepted
# by the server, but it's not guaranteed. (Depending on properties set up in
# the server.)
my_client.upload_file(FILE_NAME)

# Upload again as new object with some extra meta data, this time using
# type names instead of IDs. This depends completely on what
# types/classes/properties are set up on the server.
my_client.upload_file(FILE_NAME, object_type=FILE_TYPE, object_class=FILE_CLASS,
                      extra_info=FILE_EXTRA_INFO)
