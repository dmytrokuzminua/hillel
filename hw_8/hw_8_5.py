""" Homework 8 task 5 """


import pytest


def divide(a: int, b: int) -> float:
    """ Divide two numbers """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


def test_divide_normal():
    """ Test divide normal function """
    assert divide(6, 2) == 3.0
    assert divide(5, 2) == 2.5
    assert divide(-10, 2) == -5.0
    assert divide(0, 5) == 0.0


def test_divide_zero():
    """ Test divide zero function """
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
    with pytest.raises(ZeroDivisionError):
        divide(100, 0)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 2, 3.0),
        (5, 2, 2.5),
        (-4, 2, -2.0),
        (0, 10, 0.0),
        (9, 3, 3.0),
    ]
)
def test_divide_param(a, b, expected):
    """ Test divide function with params """
    assert divide(a, b) == expected
