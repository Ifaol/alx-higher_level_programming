#!/usr/bin/python3
"""
A square class module
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class that defines properties of Square.

    Attributes:

        size (int): width and height of Square.
        x (int): x coordinate of z square.
        y (int): y coordinate of z square.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Creates new instances of Square.

        Args:

            size (int): width and height of square.
            x (int, optional): x. Defaults to 0.
            y (int, optional): y. Defaults to 0.
            id (int, optional): Identity number of square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Prints square

        Returns:

            str: [Square] (<id>) <x>/<y> - <size>
        """
        return ("[Square] ({:d}) {:d}/{:d} - {:d}".
                format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """
        size retriever.

        Returns:

            int: size of square.
        """
        return self.height

    @size.setter
    def size(self, value):
        """
        Property setter for height and width of square.

        Args:

            value (int): height and width of square.

        Raises:

            TypeError: if size is not an integer.
            ValueError: if size is less than or equal to zero.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.height = value
        self.width = value

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute.

        Args:

            *args (tuple): arguments.
            **kwargs (dict): double pointer to a dictionary.
        """
        if args is not None and len(args) != 0:
            list_atrribs = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_atrribs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Creates the dictionary representation of a Square.

        Returns:

            diction: Key value pair of dic. Square.
        """
        diction = {}
        diction["id"] = self.id
        diction["x"] = self.x
        diction["size"] = self.size
        diction["y"] = self.y
        return (diction)
