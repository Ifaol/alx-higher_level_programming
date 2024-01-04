#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """
    Class that defines properties of rectangle: (based on 6-rectangle.py)
    Attributes:
        width (int): width of the rectangle.
        height (int): height of the rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        creates new instances of rectangle

        Args:
            width (int, optional): width of rectangle. Defaults to 0.
            height (int, optional): height of rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        width retriver
        Returns:
            int: the width of the rectangle
        """
        return self.__width

    @property
    def height(self):
        """
        height retriver
        Returns:
            int: the height of the rectangle
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Property setter for width of rectangle.
        Args:
            value (int): width of the rectangle.
        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """
        Property setter for height of recyangle.
        Args:
            value (int): height of the rectangle.
        Raises:
            TypeError: if height is not an integer.
            ValueError: if height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        calculates area of the rectangle
        Returns:
            int: area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates perimeter of a rectangle
        Returns:
            int: perimeter.
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """
        Prints the rectangle with the character # .
        Returns:
            str: the rectangle
        """
        rectangle = []
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append(str(self.print_symbol))
            if i != self.__height - 1:
                rectangle.append("\n")
        return "".join(rectangle)

    def __repr__(self):
        """
        Returns a string representation of the rectangle.
        Returns:
            str: the rectangle representation.
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        Deletes an instance of a class
        """
        print("{:s}".format("Bye rectangle..."))
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Computes the area of two rectangles and compares them.
        Args:
            rect_1 (Rectangle): first rectangle.
            rect_2 (Rectangle): second rectangle.
        Returns:
            Rectangle: the rectangle with the biggest area else rect_1 if
            areas are equal
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = rect_1.area()
        area_2 = rect_2.area()
        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Create a new Rectangle instance representing a square.
        Args:
            size: The size of the square (width and height).
        Returns:
            Rectangle: A new Rectangle instance representing a square.
        """
        return cls(width=size, height=size)
