#!/usr/bin/python3
"""FileStorage class"""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """FileStorage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """all
        """
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
            cls_dict = {}
            for k, v in self.__objects.items():
                if type(v) == cls:
                    cls_dict[k] = v
            return cls_dict
        return self.__objects

    def new(self, obj):
        """new"""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """save"""
        odict = {i: self.__objects[i].to_dict() for i in self.__objects.keys()}
        with open(self.__file_path, "w", encoding="utf-8") as e:
            json.dump(odict, e)

    def reload(self):
        """reload"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as e:
                for i in json.load(e).values():
                    name = i["__class__"]
                    del i["__class__"]
                    self.new(eval(name)(**i))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete"""
        try:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        except (AttributeError, KeyError):
            pass

    def close(self):
        """close"""
        self.reload()
