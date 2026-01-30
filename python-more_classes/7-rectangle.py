#!/usr/bin/python3
"""Module that defines a Rectangle class with width and height"""


class Rectangle:
    """Rectangle class with private width and height attributes

    Attributes:
        number_of_instances (int): number of Rectangle instances
        print_symbol: symbol used for string representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle

        Args:
            width (int): width of the rectangle (default 0)
            height (int): height of the rectangle (default 0)
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width attribute

        Args:
            value (int): width value to set

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height attribute

        Args:
            value (int): height value to set

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the rectangle area

        Returns:
            int: area of the rectangle (width * height)
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the rectangle perimeter

        Returns:
            int: perimeter of the rectangle, or 0 if width or height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return string representation of the rectangle

        Returns:
            str: rectangle drawn with print_symbol characters,
                 empty if width or height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle = []
        for i in range(self.__height):
            rectangle.append(str(self.print_symbol) * self.__width)
        return "\n".join(rectangle)

    def __repr__(self):
        """Return string representation to recreate the rectangle

        Returns:
            str: string in format Rectangle(width, height)
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print message when a Rectangle instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
