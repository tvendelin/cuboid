#!/usr/bin/env python3

class Cuboid:
    """Represents a rectangular cuboid"""
    def __init__(self, a, b, c):
        """Takes cuboid edges a, b, c and returns an instance of Cuboid"""
        self.a = a
        self.b = b
        self.c = c

    def __repr__(self):
        return f'Cuboid[{self.a}, {self.b}, {self.c}]'

    def __str__(self):
        return repr(self)

    def volume(self):
        """Returns the volume of a Cuboid"""
        return self.a*self.b*self.c

    def surface(self):
        """Returns the surface area of a Cuboid"""
        return 2 * (self.a*self.b + self.a*self.c + self.b*self.c)

    def perimeter(self):
        """Returns the sum of all sides of a Cuboid"""
        return 4 * (self.a + self.b + self.c)
