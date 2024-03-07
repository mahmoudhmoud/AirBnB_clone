#!/usr/bin/python3
"""importing storge instance ensure to Link BaseModel to FileStorage:"""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """methods : save
                 to_dic
                 __str__
    """
    def __init__(self, *args, **kwargs):
        """
        in the else clause we added 'storage.new()' to check
        If it's a new instance, add a call to the new method on the storage instance
        to add the object to the __objects dictionary.
        """

        if kwargs:
            del kwargs["__class__"]
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    v = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, v)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        

    def save(self):
        """
        we added 'storage.save()' to call save method of
        the FileStorage instance (storage) to save  the data to the file.
        also helps to Link BaseModel to FileStorage:
        """

        self.updated_at = datetime.now()


    def to_dict(self):
        '''
        return: a dictionary containing  all keys/values of __dict__ of the instance
        '''
        dic = {}

        dic["__class__"] = self.__class__.__name__
        for key, val in self.__dict__.items():
            if isinstance(val, (datetime,)):
                dic[key] = val.isoformat()
            else:
                dic[key] = val
        return dic

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
