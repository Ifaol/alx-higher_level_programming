#!/usr/bin/python3
"""
This module has the Base class.
"""


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
