#!/usr/bin/python3
"""Module that defines a Square class with size and position"""


class Square:
    """A class that defines a square with private size and position"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with optional size and position

        Args:
            size: The size of the square (default is 0)
            position: The position of the square (default is (0, 0))
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method to retrieve the size

        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size with validation

        Args:
            value: The new size value

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter method to retrieve the position

        Returns:
            The position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method to set the position with validation

        Args:
            value: The new position value

        Raises:
            TypeError: If value is not a tuple of 2 positive integers
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square

        Returns:
            The area of the square (size * size)
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character # at the given position

        If size is 0, print an empty line
        Position[1] adds vertical offset (empty lines before the square)
        Position[0] adds horizontal offset (spaces before each row)
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
