import unittest
from result import runner_up_score


class TestStringMethods(unittest.TestCase):

    def test_runner_up_score(self):
        self.assertEqual(runner_up_score())

        if __name__ == "__main__":
    unittest.main()