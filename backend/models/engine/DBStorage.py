#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.listing import Listing

class NannyDBStorage:
    """Database storage class for nanny-related data."""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize NannyDBStorage with MySQL database."""
        # Updated host and removed password
        mysql_info = {
            'host': '54.236.47.250',
            'user': 'ubuntu',
            'database': 'nanny_jobs'
        }
        self.__engine = create_engine(f"mysql://{mysql_info['user']}@{mysql_info['host']}/{mysql_info['database']}", echo=False)
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine)
        self.__session = scoped_session(session_factory)

    def all(self, cls=None):
        """Query all objects of a given class."""
        objects = {}
        classes = [User, Listing]
        if cls:
            if cls in classes:
                objects = {obj.id: obj for obj in self.__session.query(cls).all()}
        else:
            for cls in classes:
                objects.update({obj.id: obj for obj in self.__session.query(cls).all()})
        return objects

    def new(self, obj):
        """Add a new object to the database."""
        self.__session.add(obj)

    def save(self):
        """Commit changes to the database."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the database."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reload objects from the database."""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine))

    def close(self):
        """Close the session."""
        self.__session.close()

