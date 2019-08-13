import unittest


def square(i):
    return i * i


def numbers(j):
    my_numbers = range(j)
    results = []

    if 20 > j > 0:
        for element in my_numbers:
            results.append(square(element))
        return results


g = numbers(25)
print(g)
numbers(-5)


class TestSimpleFunctions(unittest.TestCase):
    # a = 2

    # def square(self, i):
    #     self.a = 5
    #     if i % 2 == 0:
    #         return i ** 2

    def test_square(self):
        self.assertEqual(square(2), 4)
        self.assertNotEqual(square(2), 8)

    def test_numbers(self):
        self.assertEqual(numbers(2), [0, 1])
        self.assertEqual(numbers(-5), None)
        self.assertEqual(numbers(25), None)