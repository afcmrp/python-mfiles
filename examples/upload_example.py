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

# Upload file
my_client.upload_file(FILE_NAME)

# Upload again as new object with some extra meta data
my_client.upload_file(FILE_NAME, extra_info=FILE_EXTRA_INFO)
