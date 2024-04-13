#!/usr/bin/python3


class Square:
    """
    Represents properties of square by: (based on 5-square.py).

    Attributes:
        size: square size (1 side).
    """
    def __init__(self, size=0, position=(0, 0)):
        """Creates new square instances.

        Args:
            __size (int) : square size(1 side).
            __position (tuple): square pos.
        """
        self.size = size
        self.position = position

    def area(self):
        """Calculates square's area.

        Returns: Current area of square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Returns the size of a square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Property size setter.

        Args:
            value (int): square size (1 side).

        Raises:
            TypeError: size must be int.
            ValueError: size must be >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Returns square position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Property setter for pos.

        Args:
            value (tuple): Square pos.

        Raises:
            TypeError: position must be a tuple of 2 positive integers
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """prints in stdout the square through the # character
        """

        if self.__size == 0:
            print()
        else:
            for P in range(self.__position[1]):
                print()
            for T in range(self.__size):
                for B in range(self.__position[0]):
                    print(" ",  end="")
                print("#" * (self.__size))

    def __str__(self):
        """Prints square offsetting by position with # SYMBOL

        Returns:  square.
        """
        if self.__size == 0:
            return ''
        new_lines = '\n' * self.position[1]
        spaces = ' ' * self.position[0]
        hashes = '#' * self.size
        return new_lines + '\n'.join(spaces + hashes for e in range(self.size))
