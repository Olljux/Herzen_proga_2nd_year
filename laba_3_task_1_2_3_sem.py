import logging
import math
import statistics

logging.basicConfig(level=logging.INFO, format='%(message)s')


def convert_precision(tolerance):
    return abs(int(round(math.log10(tolerance))))


def logging_calculate(func_calc):
    def wrapper(a, b, action, *args, tolerance=1e-6):
        logging.info(
            f"Вызов функции {func_calc.__name__}, с аргументами a={a}, b={b}, action={action}, args={args}, tolerance={tolerance}")
        result = func_calc(a, b, action, *args, tolerance=tolerance)
        logging.info(f"Результат вычислений: {result}")
        return result

    return wrapper


@logging_calculate
def calculate(a, b, action, *args, tolerance=1e-6):
    precision = convert_precision(tolerance)

    if action in {"+", "-", "*", "/"}:
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

    # Для статистических функций объединяем a, b и *args в один список
    values = (a, b) + args

    if action == "medium":
        return round(sum(values) / len(values), precision)

    elif action == "variance":
        if len(values) < 2:
            print("Not enough values for variance")
            return None
        return round(statistics.variance(values), precision)

    elif action == "std_deviation":
        if len(values) < 2:
            print("Not enough values for std_deviation")
            return None
        return round(statistics.stdev(values), precision)

    elif action == "median":
        return round(statistics.median(values), precision)

    elif action == "iqr":
        if len(values) < 4:
            print("Not enough values for iqr")
            return None
        q1 = statistics.quantiles(values, n=4)[0]
        q3 = statistics.quantiles(values, n=4)[2]
        return round(q3 - q1, precision)

    else:
        print("Unknown operation")
        return None


def main():
    print("input two operands:")
    a = float(input())
    b = float(input())
    action = input()
    print("input additional operands separated by space (or enter to skip):")
    extra = input()
    args = tuple(map(float, extra.split())) if extra else ()
    tolerance = 1e-6
    result = calculate(a, b, action, *args, tolerance=tolerance)
    print(f"Result: {result}")


main()