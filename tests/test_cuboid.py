import unittest
from decimal import Decimal
from cuboid import Cuboid

class TestCuboidDecimal(unittest.TestCase):
    def setUp(self):
        self.cuboid = Cuboid(Decimal(1.2), Decimal(1.3), Decimal(1.4))

    def test_volume(self):
        self.assertEqual(round(self.cuboid.volume(), 4), Decimal('2.184'))

    def test_surface(self):
        self.assertEqual(round(self.cuboid.surface(), 4), Decimal('10.12'))

    def test_perimeter(self):
        self.assertEqual(round(self.cuboid.perimeter(), 4), Decimal('15.6'))


class TestCuboidInt(unittest.TestCase):
    def setUp(self):
        self.cuboid = Cuboid(2, 3, 4)

    def test_volume(self):
        self.assertEqual(self.cuboid.volume(), 24)

    def test_surface(self):
        self.assertEqual(self.cuboid.surface(), 52)

    def test_perimeter(self):
        self.assertEqual(self.cuboid.perimeter(), 36)
