import logging
import math

logging.basicConfig(level=logging.INFO, format='%(message)s')

def convert_precision(tolerance):
    """
    Convert a tolerance value like 1e-6 to an integer precision (e.g., 6).

    :param float tolerance: Tolerance value.
    :return: Number of digits for rounding.
    :rtype: int
    """
    return abs(int(round(math.log10(tolerance))))

def logging_calculate(func_calc):
    def wrapper(a, b, action, tolerance=1e-6):
        logging.info(f"Вызов функции {func_calc.__name__}, с аргументами a = {a}, b = {b}, действием: {action}, tolerance = {tolerance}")
        result = func_calc(a, b, action, tolerance=tolerance)
        logging.info(f"Результат вычислений: {result}")
        return result
    return wrapper

@logging_calculate
def calculate(a, b, action, tolerance=1e-6):
    """
    Perform an arithmetical operation and return the result with specified precision.

    :param int|float a: First operand
    :param int|float b: Second operand
    :param str action: Operation sign ("+", "-", "*", "/")
    :param float tolerance: Rounding tolerance (default 1e-6)
    :return: Rounded result of operation
    """
    precision = convert_precision(tolerance)
    if action == "+":
        return round(a + b, precision)
    elif action == "-":
        return round(a - b, precision)
    elif action == "*":
        return round(a * b, precision)
    elif action == "/":
        if b == 0:
            print("Cant divide!")
            return None
        return round(a / b, precision)
    else:
        print("Unknown operation")
        return None

def main():
    """
    Input of operands and operation, compute the result using the function calculate.
    """
    print("input two operands and action:")
    a = int(input())
    b = int(input())
    action = str(input())
    print(calculate(a, b, action))

main()