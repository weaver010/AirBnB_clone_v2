#!/usr/bin/python3
"""State class."""
import models
from os import getenv
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State class
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",  backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get a list of all related City objects."""
            c_l = []
            for i in list(models.storage.all(City).values()):
                if i.state_id == self.id:
                    c_l.append(i)
            return c_l
