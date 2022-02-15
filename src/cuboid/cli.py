import sys
from decimal import Decimal, InvalidOperation
from cuboid import Cuboid

usage_msg = '''
    cuboid

    Calculates volume, surface and perimeter of a rectangular cuboid

    Usage:
    cuboid <edge a> <edge b> <edge c>
'''


def usage(err=None):
    if err:
        print(f'\n    Error:\n    {err}')
    print(usage_msg)
    sys.exit(1)


def cli(*args):
    """
    Takes three arguments representing positive real numbers
    as edges of a rectangular cuboid and prints its volume,
    surface area and the sum of the sides.
    """
    if len(args) == 0:
        usage()

    if len(args) != 3:
        usage('Expecting 3 arguments')

    valid = list()

    for a in args:
        try:
            x = Decimal(a)
            if x <= 0:
                raise ValueError()
        except (ValueError, InvalidOperation):
            usage('All edges of a cuboid must be positive real numbers')

        valid.append(x)

    c = Cuboid(*valid)
    print(c)
    print(f'Volume: {round(c.volume(), 2)}')
    print(f'Surface: {round(c.surface(), 2)}')
    print(f'Perimeter: {round(c.perimeter(), 2)}')


def main():
    cli(*sys.argv[1:])
