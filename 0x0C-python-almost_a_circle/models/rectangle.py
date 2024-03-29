#!/usr/bin/python3
"""
Defines a class Rectangle that inherits from Base
"""


from models.base import Base


class Rectangle(Base):
    """
    Class that defines properties of Rectangle.

    Attributes:

        width (int): width of rectangle.
        height (int): height of rectangle.
        x (int): x.
        y (int): y.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Creates new instances of rectangle.

        Args:

            width (int): width of rectangle.
            height (int): height of rectangle.
            x (int, optional): x. Defaults to 0.
            y (int, optional): y. Defaults to 0.
            id (int, optional): Identity number of rectangle. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Width returner method.

        Returns:

            int: width of rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Property setter for width of rectangle.

        Args:

            value (int): width of rectangle.

        Raises:

            TypeError: if width is not an integer.
            ValueError: if width is less than or equal to zero.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Height retriever.

        Returns:

            int: height of rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Property setter for height of rectangle.

        Args:

            value (int): height of rectangle.

        Raises:

            TypeError: if height is not an integer.
            ValueError: if height is less than or equal to zero.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        x coordinate retriever.

        Returns:

            int: x.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Property setter for x.

        Args:

            value (int): x.

        Raises:

            TypeError: if x is not an integer.
            ValueError: if x is less than or equal to zero.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        y coordinate retriever.

        Returns:

            int: y.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Property setter for y.

        Args:

            value (int): y.

        Raises:

            TypeError: if y is not an integer.
            ValueError: if y is less than or equal to zero.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates area of a rectangle.

        Returns:

            int: area.
        """
        return self.__width * self.__height

    def display(self):
        """
        A method to display rectangle with #
        """
        for yc in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__width):
                if j == 0:
                    for xc in range(self.__x):
                        print(" ", end="")
                print("#", end="")
            print()

    def __str__(self):
        """
        String representation of the Rectangle.

        Returns:

            str: [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return ("[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}".format
                (self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute.

        Args:

            *args (tuple): arguments.
            **kwargs (dict): double pointer to a dictionary.
        """
        if args is not None and len(args) != 0:
            list_atrribs = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_atrribs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Creates the dictionary representation of a Rectangle.

        Returns:
            diction: Key value pair of dic. rectangle.
        """
        diction = {}
        diction["x"] = self.__x
        diction["y"] = self.__y
        diction["id"] = self.id
        diction["height"] = self.__height
        diction["width"] = self.__width
        return (diction)
