import unittest
from laba_3_task_1_2_3_sem import calculate, convert_precision

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
        self.assertIsNone(calculate(10, 0, "/"))

    def test_medium(self):
        self.assertEqual(calculate(1, 3, "medium", 5, 7), 4)

    def test_variance(self):
        self.assertEqual(calculate(1, 2, "variance", 3, 4), 1.666667)

    def test_std_deviation(self):
        self.assertEqual(calculate(1, 2, "std_deviation", 3, 4), 1.290994)

    def test_median(self):
        self.assertEqual(calculate(1, 2, "median", 3, 4, 5), 3)

    def test_iqr(self):
        self.assertEqual(calculate(1, 2, "iqr", 3, 4, 5, 6), 3.5)

    def test_unknown_action(self):
        self.assertIsNone(calculate(1, 2, "unknown"))

    def test_convert_precision(self):
        self.assertEqual(convert_precision(1e-6), 6)
        self.assertEqual(convert_precision(1e-3), 3)
        self.assertEqual(convert_precision(0.1), 1)
        self.assertEqual(convert_precision(1), 0)
        self.assertEqual(convert_precision(1e-10), 10)

if __name__ == '__main__':
    unittest.main()