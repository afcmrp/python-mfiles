"""Example for how to download a file from M-Files."""

import mfiles

# Connection details (replace as appropriate)
MY_SERVER = "https://my-mfiles-server.com/REST/" # Enter your M-Files server address here
MY_USER = "TestUser" # Enter your M-Files user name here
MY_PASSWORD = "SecretPassword" # Enter your M-Files password here
MY_VAULT = "{01234567-89AB-CDEF-0123-456789ABCDEF}" # Enter your M-Files vault GUID here

# Object details
TEST_FILE_NAME = "test_download.txt"

# Initialize MFilesClient
my_client = mfiles.MFilesClient(server=MY_SERVER,
                                user=MY_USER,
                                password=MY_PASSWORD,
                                vault=MY_VAULT)

# Download file
my_client.download_file_name(TEST_FILE_NAME)
