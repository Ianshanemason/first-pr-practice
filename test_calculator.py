import unittest

from calculator import add, subtract, multiply, divide


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 1), 4)

    def test_multiply(self):
        self.assertEqual(multiply(4, 6), 24)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)


if __name__ == "__main__":
    unittest.main()
