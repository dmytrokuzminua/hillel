""" Homework 8 task 4
for run  python -m doctest -v hw_8_4.py """


def is_even(n: int) -> bool:
    """
    Checks if a number is even
    >>> is_even(2)
    True
    >>> is_even(3)
    False
    >>> is_even(0)
    True
    >>> is_even(-4)
    True
    >>> is_even(-5)
    False
    """
    return n % 2 == 0


def factorial(n: int) -> int:
    """
    Calculates the factorial of a number n (n!)
    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(5)
    120
    >>> factorial(3)
    6
    >>> factorial(10)
    3628800
    >>> factorial(-1)  # Для від'ємних чисел має викликати ValueError
    Traceback (most recent call last):
        ...
    ValueError: n must be non-negative
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
