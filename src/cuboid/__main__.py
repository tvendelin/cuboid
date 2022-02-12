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



