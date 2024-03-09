#!/usr/bin/python3
"""Basemodel : the parent class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.state import State


class FileStorage:
    """
    a class that serializes instances to a JSON file and deserializes
    JSON file to instances.
    private class attributes: __file_path, __objects
    why we make them private it helps to ensure that the data is
    stored in a secure place
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        return: dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
         add an object (obj) to the dictionary __objects.
         key:  based on the class name and its id attribute.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        converting dictionary (__objects) into a JSON format,
        and storing that JSON data in a file
        """
        objects = FileStorage.__objects
        dic_objects = {}

        for key in objects.keys():
            dic_objects[key] = objects[key].to_dict()

        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            json.dump(dic_objects, f)

    def reload(self):
        """
        deserialize the data in our JSON file back to the dictionary __objects
        (only if the JSON file (__file_path)) exists, otherwise, do nothing).
        """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as js:

                s_dic = json.load(js)

                for key, value in s_dic.items():
                    cls_name = value["__class__"]
                    self.new(eval(cls_name)(**value))

        except FileNotFoundError:
            pass
