"""Math utilities module for hw_7_1"""


def factorial(n: int) -> int:
    """Calculates the factorial of a number n"""
    if n < 0:
        raise ValueError("n має бути >= 0")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def gcd(a: int, b: int) -> int:
    """Finds the greatest common divisor of two numbers"""
    while b:
        a, b = b, a % b
    return abs(a)
