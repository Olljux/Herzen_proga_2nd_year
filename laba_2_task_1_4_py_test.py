from laba_1_task_3_1 import calculate

def test_addition():
    assert calculate(5, 7, "+") == 12

def test_subtraction():
    assert calculate(6, 7, "-") == -1

def test_multiplication():
    assert calculate(5, 7, "*") == 35

def test_division():
    assert calculate(10, 2, "/") == 5

def test_division_by_zero():
    assert calculate(10, 0, "/") is None