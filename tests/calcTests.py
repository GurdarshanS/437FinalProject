import unittest
from calculator import Calculator


# Integration Tests
class TestMethods(unittest.TestCase):
    def test_addition(self):
        c = Calculator()
        self.assertEqual(c.addition(2, 4), 6)
        self.assertEqual(c.subtraction(c.addition(2, 4), 3), 3)

    def test_subtraction(self):
        c = Calculator()
        self.assertEqual(c.subtraction(2, 4), -2)
        self.assertEqual(c.addition(c.subtraction(2, 4), 2), 0)

    def test_multiplication(self):
        c = Calculator()
        self.assertEqual(c.multiplication(2, 4), 8)
        self.assertEqual(c.division(c.multiplication(2, 4), 8), 1)

    def test_division(self):
        c = Calculator()
        self.assertEqual(c.division(2, 4), 0.5)
        self.assertEqual(c.multiplication(c.division(2, 4), 3), 1.5)


if __name__ == '__main__':
    unittest.main()
