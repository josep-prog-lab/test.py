#!/usr/bin/python3
# This module defines a Rectangle class.

class Rectangle:
    """Represents a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """Return a string representation of the rectangle using print_symbol."""
        if self.width == 0 or self.height == 0:
            return ""
        rect = ""
        for i in range(self.height):
            rect += str(self.print_symbol) * self.width
            if i < self.height - 1:
                rect += "\n"
        return rect

    def __repr__(self):
        """Return a string representation for recreating the rectangle."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Print a message when an instance is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
