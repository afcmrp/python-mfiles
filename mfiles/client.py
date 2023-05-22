"""M-Files client methods.

For more information, see:
https://developer.m-files.com/APIs/REST-API/Reference
"""

# Standard modules
from copy import deepcopy
from getpass import getpass
import json
from os import getcwd, getenv
from os.path import splitext

# External modules
import requests

# Internal modules
from mfiles.definitions import DATATYPE, LOOKUP_DATATYPE, LOOKUP_DATATYPES, \
    OBJ, OBJ_PROPERTY
from mfiles.errors import MFilesException

# M-files server info
DEFAULT_URL = "http://localhost/m-files/REST/"

class MFilesClient():
    """M-Files client.

    Parameters:
        server (str): API URL. Defaults to ``"http://localhost/m-files/REST/"``
        user (str): User to login with. If not supplied it will be fetched
                    from environment variable ``MFILES_USER``, if not set
                    it will be fetched using ``input()``.
        password (str): User password. If not supplied it will be
                        fetched from environment variable ``MFILES_PASS``,
                        if not set it will be fetched using ``getpass()``.
        vault (str): M-Files vault GUID to connect to.
    """
    # pylint: disable=too-many-public-methods

    def __init__(self, server=DEFAULT_URL, user=None, password=None, vault=None):
        self.user = user
        self.password = password
        self.vault = vault
        self.server = ""
        self.headers = {"X-Authentication": ""}
        self.set_server(server)

    def set_server(self, server):
        """Set the M-Files server API URL."""
        if server[-1] != "/":
            server += "/"
        self.server = server
        self.login()

    def set_user(self, user):
        """Set the M-Files user."""
        self.user = user
        self.login()

    def set_password(self, password):
        """Set the M-Files user password."""
        self.password = password
        self.login()

    def set_vault(self, vault):
        """Set the M-Files vault GUID to connect to."""
        self.vault = vault
        self.login()

    def login(self, server=None, user=None, password=None, vault=None):
        """Logs in the user to M-Files.

        Logs in and prepares the authentication token, ready to be used in
        http request header as authentication.

        Parameters:
            server (str): API URL.
            user (str): User to login with. If not supplied it will be fetched
                        from environment variable ``MFILES_USER``, if not set
                        it will be fetched using ``input()``.
            password (str): User password. If not supplied it will be
                            fetched from environment variable ``MFILES_PASS``,
                            if not set it will be fetched using ``getpass()``.
            vault (str): M-Files vault GUID to connect to.
        """
        env_server = getenv("MFILES_URL")
        env_user = getenv("MFILES_USER")
        env_pass = getenv("MFILES_PASS")
        env_vault = getenv("MFILES_VAULT")
        programmatic_user = user or self.user or env_user
        programmatic_pass = password or self.password or env_pass
        self.server = server or self.server or env_server
        self.user = programmatic_user or input("M-Files mail: ")
        self.password = programmatic_pass or getpass("M-Files password: ")
        self.vault = vault or self.vault or env_vault
        if not all([self.server, self.user, self.password, self.vault]):
            return
        auth = json.dumps({"Username": self.user,
                           "Password": self.password,
                           "VaultGuid": self.vault})
        request_url = self.server + "server/authenticationtokens"
        response = requests.post(request_url, data=auth)
        print(response.text)
        auth_token = json.loads(response.text)["Value"]
        self.headers = {"X-Authentication": auth_token}

    def get(self, endpoint):
        """General purpose GET method.

        Parameters:
            endpoint (str): Endpoint on form ``"path/to/endpoint"``.

        Raises:
            MFilesException: If request returns status code != 200.

        Returns:
            dict: Dictionary with request result.
        """
        if endpoint[0] == "/":
            endpoint = endpoint[1:]
        request_url = self.server + endpoint
        response = requests.get(request_url, headers=self.headers)
        if response.status_code != 200:
            raise MFilesException(response.text)
        return response.json()

    def put(self, endpoint, data=None):
        """General purpose PUT method.

        Parameters:
            endpoint (str): Endpoint on form ``"path/to/endpoint"``.
            data (str): Data to use in PUT request.

        Raises:
            MFilesException: If request returns status code != 200.

        Returns:
            dict: Dictionary with request result.
        """
        if endpoint[0] == "/":
            endpoint = endpoint[1:]
        request_url = self.server + endpoint
        response = requests.put(request_url, headers=self.headers, data=data)
        if response.status_code != 200:
            raise MFilesException(response.text)
        return response.json()

    def post(self, endpoint, data=None):
        """General purpose POST method.

        Parameters:
            endpoint (str): Endpoint on form ``"path/to/endpoint"``.
            data (str): Data to use in POST request.

        Raises:
            MFilesException: If request returns status code != 200.

        Returns:
            dict: Dictionary with request result.
        """
        if endpoint[0] == "/":
            endpoint = endpoint[1:]
        request_url = self.server + endpoint
        response = requests.post(request_url, headers=self.headers, data=data)
        if response.status_code != 200:
            raise MFilesException(response.text)
        return response.json()

    def quick_search(self, query):
        """Perform a quick search in the M-Files vault.

        This returns the same results as if the query was
        performed against the M-Files client search box.

        Parameters:
            query (str): Search query.

        Returns:
            list: A list of matching items.
        """
        search_query = "objects?q=" + query
        return self.get(search_query)

    def search(self, query):
        """Perform a search in the M-Files vault.

        Parameters:
            query (str): Search query.

        Returns:
            list: A list of matching items.
        """
        search_query = "objects?" + query
        return self.get(search_query)

    def objects(self):
        """Get all object types in the M-Files vault."""
        response = self.get("structure/objecttypes")
        return response

    def classes(self):
        """Get all classes in the M-Files vault."""
        response = self.get("structure/classes")
        return response

    def properties(self):
        """Get all property definitions in the M-Files vault."""
        response = self.get("structure/properties")
        return response

    def class_details(self, class_id):
        """Get details for a specific class in the M-Files vault."""
        endpoint = "structure/classes/%d" % class_id
        response = self.get(endpoint)
        return response

    def value_lists(self):
        """Get all value lists in the M-Files vault."""
        response = self.get("valuelists")
        return response

    def value_list_items(self, list_id):
        """Get items for a specific value list in the M-Files vault."""
        endpoint = "valuelists/%d/items" % list_id
        response = self.get(endpoint)
        return response

    def get_value_id(self, value_name, list_id, owner_ids):
        """Get the ID of a specific value in a specific value list.

        Parameters:
            value_name (str): Name of the value list option to look for.
            list_id (int): ID of the list to look in.
            owner_ids (list): IDs of potential list owners.

        Raises:
            MFilesException: If the value name can't be found in the list.

        Returns:
            int: ID of value in value list.
        """
        list_items = self.value_list_items(list_id)
        for item in list_items["Items"]:
            same_name = item["Name"] == value_name
            ok_owner = not item["HasOwner"] or item["OwnerID"] in owner_ids
            if same_name and ok_owner:
                return item["ID"]
        raise MFilesException("Value name %s not recognized" % value_name)

    def get_types(self, category="object"):
        """Get info for all types from a type category.

        Parameters:
            category (str): Type category. Can be any of ``"object"``,
                            ``"class"``, ``"property"``. Defaults to
                            ``"object"``.

        Raises:
            MFilesException: If the category supplied doesn't exist.

        Returns:
            list: List of dicts with information about the types.
        """
        if category == "object":
            types = self.objects()
        elif category == "class":
            types = self.classes()
        elif category == "property":
            types = self.properties()
        else:
            raise MFilesException("Type name %s not recognized" % category)
        return types

    def get_info(self, name, category="object"):
        """Get general info of a type by name.

        Parameters:
            name (str): Name of type to get info from.
            category (str): Type name. Can be any of ``"object"``,
                            ``"class"``, ``"property"``. Defaults to
                            ``"object"``.

        Raises:
            MFilesException: If the property name can't be found.

        Returns:
            dict: Dictionary with information about the type.
        """
        types = self.get_types(category)
        for type_info in types:
            if type_info["Name"] == name:
                return type_info
        raise MFilesException("Property %s could not be found in vault" % name)

    def get_info_id(self, type_id, category="object"):
        """Get general info of a type by id.

        Parameters:
            type_id (str): ID of type to get info from.
            category (str): Type category. Can be any of ``"object"``,
                            ``"class"``, ``"property"``. Defaults to
                            ``"object"``.

        Raises:
            MFilesException: If the property ID can't be found.

        Returns:
            dict: Dictionary with information about the type.
        """
        types = self.get_types(category)
        for type_info in types:
            if type_info["ID"] == type_id:
                return type_info
        raise MFilesException("Property ID %s could not be found in vault" % \
                              type_id)

    def translate_name(self, name, category="object"):
        """Translate a name into its ID as recognized by the server.

        Parameters:
            name (str): Name to translate.
            category (str): Type category. Can be any of ``"object"``,
                            ``"class"``, ``"property"``. Defaults to
                            ``"object"``.

        Returns:
            int: ID of ``name``.
        """
        return self.get_info(name, category)["ID"]

    def get_property(self, property_name, owners, property_value):
        """Get a certain property built as M-Files expects it.

        Parameters:
            property_name (str): Property name.
            owners (list): List of ints with possible owners IDs.
            property_value (any): Value to set property to.

        Return:
            dict: Property with required keys and values.
        """
        property_info = self.get_info(property_name, "property")
        prop = deepcopy(OBJ_PROPERTY)
        prop["PropertyDef"] = property_info["ID"]
        prop["TypedValue"]["DataType"] = property_info["DataType"]
        if property_info["DataType"] in LOOKUP_DATATYPES:
            # DataType needs to be looked up
            datatype_id = self.get_value_id(property_value,
                                            property_info["ValueList"],
                                            owners)
            datatype = deepcopy(LOOKUP_DATATYPE)
            datatype["Lookup"]["Item"] = datatype_id
        else:
            datatype = deepcopy(DATATYPE)
            datatype["Value"] = property_value
        prop["TypedValue"].update(datatype)
        return prop

    def create_object(self, name, object_type=0, object_class=0,
                      extra_info=None, file_info=None):
        """Create M-Files object and upload it to the vault.

        Parameters:
            name (str): Name of new object.
            object_type (str, int): Object type. If integer, the type will
                                    not be attempted to be translated. If
                                    string, the type will be transated into
                                    the property ID the server expects for the
                                    given type.
            object_class (str, int): Object class, same translation principle
                                     as for object_type.
            extra_info (dict): Additional object information.
            file_info (dict): Eventual file information for object. Dict
                              that must contain keys ``UploadID``, ``Title``,
                              ``Extension``, ``Size``.

        Raises:
            MFilesException: If the object can't be created.

        Returns:
            dict: Dictionary with object information.
        """
        # pylint: disable=too-many-arguments
        extra_info = extra_info or {}
        file_info = file_info or []
        if isinstance(object_type, str):
            object_type = self.translate_name(object_type, "object")
        if isinstance(object_class, str):
            object_class = self.translate_name(object_class, "class")
        # Start building object
        obj = deepcopy(OBJ)
        # Set mandatory info
        obj["PropertyValues"][0]["TypedValue"]["Value"] = name
        obj["PropertyValues"][1]["TypedValue"]["Lookup"]["Item"] = object_class
        # Add any additionally supplied properties
        for property_name in extra_info:
            owners = [object_class, object_type]
            prop = self.get_property(property_name, owners,
                                     extra_info[property_name])
            obj["PropertyValues"].append(prop)
        obj["Files"] = [file_info]
        data = json.dumps(obj)
        endpoint = "objects/%s" % object_type
        return self.post(endpoint, data)

    def check_out(self, object_id, object_type=0):
        """Check out an object from M-Files."""
        data = json.dumps({"Value": "2"}) # Checked out by me
        endpoint = "objects/%s/%s/latest/checkedout" % \
            (object_type, object_id)
        return self.put(endpoint, data)

    def check_in(self, object_id, object_version, object_type=0):
        """Check in an object to M-Files."""
        data = json.dumps({"Value": "0"}) # Checked in
        endpoint = "objects/%s/%s/%s/checkedout" % \
            (object_type, object_id, object_version)
        return self.put(endpoint, data)

    def upload_file(self, file_path, object_type=0, object_class=0,
                    extra_info=None):
        """Upload a file to M-Files.

        Parameters:
            file_path (str): Path to file to upload.
            object_type (str, int): Object type. If integer, the type will
                                    not be attempted to be translated. If
                                    string, the type will be transated into
                                    the property ID the server expects for the
                                    given type.
            object_class (str, int): Object class, same translation principle
                                     as for object_type.
            extra_info (dict): Additional object information.

        Raises:
            MFilesException: If the file can't be uploaded.

        Returns:
            dict: Dictionary with API request result.
        """
        # Upload file to temporary storage
        endpoint = "files"
        with open(file_path, mode="rb") as file_stream:
            content = file_stream.read()
        upload_info = self.post(endpoint, content)

        # Create object
        object_name, objext_ext = splitext(file_path)
        file_info = {
            "UploadID": upload_info["UploadID"],
            "Title": object_name,
            "Extension": objext_ext[1:],
            "Size": upload_info["Size"]
        }

        obj_info = self.create_object(object_name, object_type, object_class,
                                      extra_info, file_info)
        return obj_info

    def download_file(self, local_path, object_type, object_id, file_id,
                      object_version="latest"):
        """Download a file from M-Files.

        Parameters:
            object_type (int): Object type ID.
            object_id (int): Object ID.
            file_id (int): File ID.
            object_version (int, str): Object version. Defaults to
                                       ``"latest"``.
            local_path (str): Path to download file to.

        Raises:
            MFilesException: If the file can't be downloaded.

        Returns:
            bool: True if file is found and downloaded successfully.
        """
        # pylint: disable=too-many-arguments
        request_url = "%sobjects/%s/%s/%s/files/%s/content" % \
            (self.server, object_type, object_id, object_version, file_id)
        response = requests.get(request_url, headers=self.headers)
        if response.status_code != 200:
            raise MFilesException(response.text)
        with open(local_path, mode="wb+") as file_stream:
            file_stream.write(response.content)
        return True

    def download_file_name(self, file_name, local_path=None):
        """Download a file from M-Files by its name.

        Caution:
            This searches for the file and downloads the top
            result. This is not always guaranteed to be the
            intended file. A better way is to use search to
            find the correct file and then use the function
            ``download_file()`` to download the file by using
            file and object id.

        Parameters:
            file_name (str): Name of file to download.
            local_path (str): Path to download file to. Defaults
                            to file name and current directory.

        Returns:
            bool: True if file is found and downloaded.
        """
        items = self.quick_search(file_name)
        if not items:
            return False
        item = items["Items"][0]
        obj_type = item["ObjVer"]["Type"]
        obj_id = item["ObjVer"]["ID"]
        obj_version = item["ObjVer"]["Version"]
        file_id = item["Files"][0]["ID"]
        local_path = local_path or getcwd() + "\\" + file_name
        download_ok = self.download_file(local_path=local_path,
                                         object_type=obj_type,
                                         object_id=obj_id, file_id=file_id,
                                         object_version=obj_version)
        return download_ok

    def delete_object(self, object_type, object_id):
        """Delete M-Files object.

        Note:
            Deleting an object means flagging an object for deletion.
            Most users will not see the object anymore, but administators
            will still be able to access it.
        """
        endpoint = "objects/%s/%s/deleted" % (object_type, object_id)
        return self.put(endpoint)

    def destroy_object(self, object_type, object_id):
        """Destroy M-Files object.

        Caution:
            Destroying an object means unrecoverably deleting all
            versions of the object. Use with caution.
        """
        request_url = "%sobjects/%s/%s/latest?allVersions=true" % \
            (self.server, object_type, object_id)
        response = requests.delete(request_url, headers=self.headers)
        if response.status_code != 200:
            raise MFilesException(response.text)
        return response
