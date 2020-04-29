"""M-Files standard definitions.

For detailed information, see:
https://developer.m-files.com/APIs/REST-API/Reference
"""

# Default M-Files object for object creation
OBJ = {
    "PropertyValues": [
        {
            "PropertyDef": 0, # "Name" property ID
            "TypedValue": {
                "DataType": 1,
                "Value": "" # Actual name goes here
            }
        },
        {
            "PropertyDef": 100, # "Class" property ID
            "TypedValue": {
                "DataType": 9,
                "Lookup": {
                    "Item": 0, # Class ID goes here
                    "Version": -1
                }
            }
        }
    ]
}

# Property field of object
OBJ_PROPERTY = {
    "PropertyDef": 0, # Property ID
    "TypedValue": {
        "DataType": 0
    }
}

# DataTypes
# https://developer.m-files.com/APIs/REST-API/Reference/enumerations/mfdatatype/

LOOKUP_DATATYPES = [9, 10]

# Standard MFDataType
DATATYPE = {
    "Value": 0 # Datatype ID
}

# Lookup MFDataType
LOOKUP_DATATYPE = {
    "Lookup": {
        "Item": "", # Custom datatype ID
        "Version": -1
    }
}
