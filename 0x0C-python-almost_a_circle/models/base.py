#!/usr/bin/python3
"""
This module has the Base class.
"""


import json
import os.path
import csv
import turtle


class Base:
    """
    This is a class for managing id attribute in all future classes.

    Attributes:

        __nb_objects (int): private class attribute to track objects created.

        id (int): public instance attribute representing the unique id.

    Methods:

        __init__(self, id=None): Class constr. to init. the object's id.

    Usage:

        Designed to be inherited by other classes to manage the id attribute.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor.

        Args:

            id (int): !None, assign id. Els, ++ __nb_objects and assign id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of a python list_dictionaries.

        Args:

            list_dictionaries (list): list of dictionaries.

        Returns:

            json_str: json string representation of py dict.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        It writes a JSON string representation of list_objs to a file.

        Args:

            list_objs (list): a list of instances of a Base class.
        """
        f_name = "{0}.json".format(cls.__name__)
        if list_objs is None:
            list_objs = []
        with open(f_name, 'w') as file:
            js = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            file.write(js)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns a list of the JSON string.

        Args:

            json_string (str): A string representing a list of dictionaries.

        Returns:

            list: JSON string representation json_string
        """
        if json_string is None or not json_string:
            return []
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance of cls with all attributes already set.

        Args:

            dictionary (dict): double pointer to a dictionary.
            cls (any): a rectangle or square class.

        Returns:

            list: an instance with all attributes already set.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return(dummy)

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances.

        Args:

            cls (any): a rectangle or square class.

        Returns:

            list: list of instances.
        """
        f_name = "{0}.json".format(cls.__name__)
        try:
            with open(f_name, 'r') as file:
                json_data = file.read()
                list_of_dicts = cls.from_json_string(json_data)
                instances_list = [cls.create(**d) for d in list_of_dicts]
                return instances_list
        except FileNotFoundError:
            return []
