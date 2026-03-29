""" Homework 3 task 1 """


from __future__ import annotations


class Fraction:
    """Class for adding, subtracting, multiplying, and dividing two instances"""
    def __init__(self, numerator: int, denominator: int) -> None:
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other: Fraction) -> Fraction:
        """Method for adding fractions, returns fraction"""
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __sub__(self, other: Fraction) -> Fraction:
        """Method for subtracting fractions, returns fraction"""
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __mul__(self, other: Fraction) -> Fraction:
        """Method for multiplying fractions, returns fraction"""
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __truediv__(self, other: Fraction) -> Fraction:
        """Method for dividing fractions, returns fraction"""
        if other.denominator == 0:
            raise ValueError("Denominator cannot be zero")
        num = self.numerator * other.denominator
        den = self.denominator * other.numerator
        return Fraction(num, den)

    def __repr__(self) -> str:
        return f"{self.numerator}/{self.denominator}"


def main():
    """main def"""
    a = Fraction(1, 2)
    b = Fraction(3, 4)

    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)


if __name__ == "__main__":
    main()
