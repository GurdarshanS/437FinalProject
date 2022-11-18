import unittest
from add import Addition
from sub import Subtraction

# Unit Tests
class TestMethods(unittest.TestCase):
    def test_addition(self):
        a = Addition()
        self.assertEqual(a.addition(2, 4), 6)

    def test_subtraction(self):
        s = Subtraction()
        self.assertEqual(s.subtraction(2, 4), -2)


if __name__ == '__main__':
    unittest.main()
