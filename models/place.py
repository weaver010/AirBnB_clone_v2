#!/usr/bin/python3
""" Place class."""
import models
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy.orm import relationship


association_table = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True, nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ Place for a MySQL database.

    Attributes:
        __tablename__: The name of  table to store places.
        city_id : The city id.
        user_id: The  user id.
        name:  name.
        description:  description.
        number_rooms : number of rooms.
        number_bathrooms : number of bathrooms.
        max_guest :  maximum number of guests.
        price_by_night : price by night.
        latitude : latitude.
        longitude : longitude.
        reviews :Review
        amenities : Amenity
        amenity_ids:  id amenities.
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """list of all  Reviews."""
            review_l = []
            for i in list(models.storage.all(Review).values()):
                if i.place_id == self.id:
                    review_l.append(i)
            return review_l

        @property
        def amenities(self):
            """Get/set  Amenities."""
            amenity_l = []
            for j in list(models.storage.all(Amenity).values()):
                if j.id in self.amenity_ids:
                    amenity_l.append(j)
            return amenity_l

        @amenities.setter
        def amenities(self, value):
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
