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

if (__name__ == '__main__'):
    import sys
    from decimal import *

    usage_msg = '''
    cuboid

    Calculates volume, surface and perimeter of a rectangular cuboid

    Usage: 
    cuboid <edge a> <edge b> <edge c>
    '''

    def usage(err=''):
        if err:
            print(f'\n    Error:\n    {err}')
        print(usage_msg)
        sys.exit(1)

    if len(sys.argv) != 4:
        usage('Expecting 3 arguments')

    valid = list()

    for a in sys.argv[1:]:
        try:
            x = Decimal(a)
            if x < 0:
                raise ValueError()
        except (ValueError, InvalidOperation) as e:
            usage('All edges of a cuboid must be positive real numbers')

        valid.append(x)

    c = Cuboid(*valid)
    print(c)
    print(f'Volume: {round(c.volume(), 2)}')
    print(f'Surface: {round(c.surface(), 2)}')
    print(f'Perimeter: {round(c.perimeter(), 2)}')


