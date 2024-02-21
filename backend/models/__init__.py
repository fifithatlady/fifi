#!/usr/bin/python3
"""Create a unique storage instance for your QuickSearch Estates application"""

from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.city import City
from models.county import County
from models.place import Place
from models.province import Province
from models.review import Review
from models.security import Security
from models.user import User
from models.continent import Continent
from models.suburb import Suburb
from models.property import Property
from models.amenity import Amenity
from models.preference import Preference
from os import getenv

# Determine the type of storage to use based on environment variable
if getenv("QUICK_SEARCH_ESTATE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()

# Reload data from storage
storage.reload()

