#!/usr/bin/python3
"""create a class Base"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        list_dict = []
        if list_objs is not None:
            for obj in list_objs:
                list_dict.append(obj.to_dictionary())
        with open("{}.json".format(cls.__name__), "w") as f:
            f.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dum = cls(1, 1)
        elif cls.__name__ == "Square":
            dum = cls(1)
        dum.update(**dictionary)
        return dum

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                obj_list = cls.from_json_string(json_string)
                instances = [cls.create(**obj_dict) for obj_dict in obj_list]
                return instances
        except FileNotFoundError:
            return []

    def save_to_file_csv(cls, list_objs):
        """Writes the CSV string representation of list_objs to a file"""
        list_dict = []
        if list_objs is not None:
            for obj in list_objs:
                list_dict.append(obj.to_dictionary())
        with open("{}.csv".format(cls.__name__), "w") as f:
            f.write(cls.to_json_string(list_dict))

    def load_from_file_csv(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                obj_list = cls.from_json_string(json_string)
                instances = [cls.create(**obj_dict) for obj_dict in obj_list]
                return instances
        except FileNotFoundError:
            return []
