#!/usr/bin/env python3

class Cuboid:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __repr__(self):
        return f'Cuboid[{self.a}, {self.b}, {self.c}]'

    def __str__(self):
        return repr(self)

    def volume(self):
        return self.a*self.b*self.c

    def surface(self):
        return 2 * (self.a*self.b + self.a*self.c + self.b*self.c)

    def perimeter(self):
        return 4 * (self.a + self.b + self.c)
