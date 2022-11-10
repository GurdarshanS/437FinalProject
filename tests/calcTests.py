import unittest
from calculator import Calculator as c


class TestMethods(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(c.addition(2, 4), 6)

    def test_subtraction(self):
        self.assertEqual(c.subtraction(2, 4), -2)

    def test_multiplication(self):
        self.assertEqual(c.multiplication(2, 4), 8)

    def test_division(self):
        self.assertEqual(c.division(2, 4), 0.5)


if __name__ == '__main__':
    unittest.main()
