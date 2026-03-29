""" Homework 3 task 2 """


import math
from __future__ import annotations


class Vector:
    """ Class Vector """
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def length(self) -> float:
        """ Returns length of the vector with x,y coordinates"""
        return math.sqrt(self.x**2 + self.y**2)

    def __add__(self, other: Vector) -> Vector:
        """ Returns the result of adding vector instances """
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        """ Returns the result of subtracting vector instances """
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, number: int) -> Vector:
        """ Returns the result of multiplying vector instances """
        return Vector(self.x * number, self.y * number)

    def __lt__(self, other: Vector) -> bool:
        """ Returns the result of comparing `v1 < v2` vector instances """
        return self.length() < other.length()

    def __eq__(self, other: Vector) -> bool:
        """ Returns the result of comparing vectors for equality """
        return self.length() == other.length()

    def __repr__(self) -> str:
        """ Returns vectors representation """
        return f"Vector({self.x}, {self.y})"


def main():
    """main def"""
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)

    print("v1 + v2 =", v1 + v2)
    print("v1 - v2 =", v1 - v2)
    print("v1 * 2 =", v1 * 2)

    print("Length v1 =", v1.length())
    print("v1 < v2:", v1 < v2)
    print("v1 == v2:", v1 == v2)


if __name__ == "__main__":
    main()
