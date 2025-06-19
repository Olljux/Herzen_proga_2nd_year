import unittest
from laba_3_task_1_1_3_sem import calculate, convert_precision

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
        self.assertIsNone(calculate(10, 0, "/"))  # при делении на 0 возвращаем None

    def test_convert_precision(self):
        self.assertEqual(convert_precision(1e-6), 6)
        self.assertEqual(convert_precision(1e-3), 3)
        self.assertEqual(convert_precision(0.1), 1)
        self.assertEqual(convert_precision(1), 0)
        self.assertEqual(convert_precision(1e-10), 10)

if __name__ == '__main__':
    unittest.main()