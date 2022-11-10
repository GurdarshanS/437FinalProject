import unittest
from calculator import Calculator


class TestMethods(unittest.TestCase):
    
    def test_addition(self):
        c = Calculator()
        self.assertEqual(c.addition(2, 4), 6)

    def test_subtraction(self):
        c = Calculator()
        self.assertEqual(c.subtraction(2, 4), -2)

    def test_multiplication(self):
        c = Calculator()
        self.assertEqual(c.multiplication(2, 4), 8)

    def test_division(self):
        c = Calculator()
        self.assertEqual(c.division(2, 4), 0.5)


if __name__ == '__main__':
    unittest.main()
