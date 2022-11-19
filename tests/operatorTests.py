import unittest
from add import Addition
from sub import Subtraction
from mul import Multiplication
from div import Division


# Unit Tests
class TestMethods(unittest.TestCase):
    def test_addition(self):
        a = Addition()
        self.assertEqual(a.addition(2, 4), 6)

    def test_subtraction(self):
        s = Subtraction()
        self.assertEqual(s.subtraction(2, 4), -2)

    def test_multiplication(self):
        m = Multiplication()
        self.assertEqual(m.multiplication(2, 3), 6)

    def test_division(self):
        d = Division()
        self.assertEqual(d.division(4, 2), 2)


if __name__ == '__main__':
    unittest.main()
