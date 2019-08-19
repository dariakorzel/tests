import unittest
from result import iterable_sum


class TestStringMethods(unittest.TestCase):

    def test_iterable_sum(self):
        a = [1, 2, 3]
        self.assertEqual(iterable_sum(a), 6)


if __name__ == "__main__":
    unittest.main()
