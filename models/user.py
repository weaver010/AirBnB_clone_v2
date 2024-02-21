#!/usr/bin/python3
""" User class."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Represents a user for a MySQL database.
    Attributes:
        __tablename__ : The name of table to store users.
        email:The useremail 
        password : The user password.
        first_name : The user first name.
        last_name : The userlast name.
        places : The User-Place 
        reviews: The User-Review 
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")
