#!/usr/bin/python3
""" BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()


class BaseModel:
    """ BaseModel class
    """

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel
        """
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.utcnow()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

    def save(self):
        """save"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Return a dictionary
        """
        awes = self.__dict__.copy()
        awes["__class__"] = str(type(self).__name__)
        awes["created_at"] = self.created_at.isoformat()
        awes["updated_at"] = self.updated_at.isoformat()
        awes.pop("_sa_instance_state", None)
        return awes

    def delete(self):
        """Delete"""
        models.storage.delete(self)

    def __str__(self):
        """__str__"""
        s = self.__dict__.copy()
        s.pop("_sa_instance_state", None)
        return "[{}] ({}) {}".format(type(self).__name__, self.id, s)
