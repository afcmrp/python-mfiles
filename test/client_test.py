"""Test cases for client.py"""

from mfiles.client import MFilesClient

TEST_USER = "test_user"
TEST_PASS = "test_pass"

def test_init():
    """Test creation of MFilesClient object."""
    MFilesClient(user=TEST_USER, password=TEST_PASS)
