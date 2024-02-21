#!/usr/bin/python3
"""This module defines all models for Nanny Jobs"""

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Table, Float, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import uuid
from datetime import datetime

Base = declarative_base()

class BaseModel:
    """Base model class for all models"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Return string representation of the object"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Save the object to the database"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def delete(self):
        """Delete the object from the database"""
        from models import storage
        storage.delete(self)

    def to_dict(self):
        """Return dictionary representation of the object"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = type(self).__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in new_dict:
            del new_dict['_sa_instance_state']
        return new_dict


class Nanny(BaseModel, Base):
    """Nanny model"""
    __tablename__ = 'nannies'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    # Other nanny-related attributes can be added here


class Family(BaseModel, Base):
    """Family model"""
    __tablename__ = 'families'
    # Define family-related attributes


class Application(BaseModel, Base):
    """Application model"""
    __tablename__ = 'applications'
    # Define application-related attributes


class Review(BaseModel, Base):
    """Review model"""
    __tablename__ = 'reviews'
    # Define review-related attributes and relationships

