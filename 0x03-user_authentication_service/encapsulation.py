#!/usr/bin/python3

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Getter for the radius attribute"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Setter for the radius attribute"""
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @radius.deleter
    def radius(self):
        """Deleter for the radius attribute"""
        del self._radius


# Usage
c = Circle(5)
print(c.radius)     # 5
c.radius = 10       # Set a new value
print(c.radius)     # 10
# c.radius = -5     # This would raise a ValueError
del c.radius        # Deletes the radius attribute
