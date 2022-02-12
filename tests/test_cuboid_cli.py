import unittest
from cuboid.cli import cli

class TestCuboidCli(unittest.TestCase):
    def test_rwong_input_param_count(self):
        with self.assertRaises(SystemExit) as e:
            cli(1, 2)

        self.assertEqual(e.exception.code, 1)

    def test_throws_on_invalid_type(self):
        with self.assertRaises(SystemExit) as e:
            cli('foo', 'bar', 'baz')

        self.assertEqual(e.exception.code, 1)

