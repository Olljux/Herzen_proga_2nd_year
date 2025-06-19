import unittest
from laba_1_task_3_1 import calculate

class TestCalculate(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculate(5, 7, "+"), 12)

    def test_subtraction(self):
        self.assertEqual(calculate(6, 7, "-"), -1)

    def test_multiplication(self):
        self.assertEqual(calculate(5, 7, "*"), 35)

    def test_division(self):
        self.assertEqual(calculate(10, 2, "/"), 5)

    def test_division_by_zero(self):
        self.assertIsNone(calculate(10, 0, "/"))  # потому что при делении на 0 просто print

if __name__ == '__main__':
    unittest.main()