import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

def logging_calculate(func_calc):
    def wrapper(a, b, action):
        logging.info(f"Вызов функции {func_calc.__name__}, с аргументами a = {a}, b = {b}, действием: {action}")
        result = func_calc(a, b, action)
        logging.info(f"Результа вычислений: {result}")
        return result
    return wrapper

@logging_calculate
def calculate(a, b, action):
    """
     Perform an arithmetical operation and return the result.

    :param int a: The first operand
    :param int b: The second operand
    :param str action: The sign of arithmetical operation
    """
    if action == "+":
        return a + b
    if action == "-":
        return a - b
    if action == "*":
        return a * b
    if action == "/":
        if b == 0:
            print("Cant split!")
        else:
            return a / b
def test(x):
    """
    Testing the function calculate.

    :param str x: The sign of arithmetical operation
    """
    if x == "+":
        assert calculate(5, 7, "+") == 12 #True
    if x == "-":
        assert calculate(6, 7, "-") == 99 #False
    if x == "*":
        assert calculate(5, 7, "*") == 35 #True
    if x == "/":
        assert calculate(10, 2, "/") == 7 #False
def main():
    """
    Input of operands and operation, compute the result using the function calculate.
    """
    print("input two operands and action:")
    a = int(input())
    b = int(input())
    action = str(input())
    print(calculate(a, b, action))
    test(action)

main()



