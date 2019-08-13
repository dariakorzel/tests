import unittest
from loop import square
from loop import numbers


class TestSimpleFunctions(unittest.TestCase):

    def test_square(self):
        self.assertEqual(square(2), 4)
        self.assertNotEqual(square(2), 8)

    def test_numbers(self):
        self.assertEqual(numbers(2), [0, 1])
        self.assertEqual(numbers(-5), None)
        self.assertEqual(numbers(25), None)