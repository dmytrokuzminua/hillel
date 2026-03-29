""" Homework 3 task 7 """


import math
from __future__ import annotations


class Vector:
    """Vector class"""
    def __init__(self, *components) -> None:
        """ *components: vector coordinates (arbitrary number of dimensions) """
        if not components:
            raise ValueError("Vector must have at least one component")
        self.components = tuple(components)

    def length(self) -> int|float:
        """Calculating the length of the vector, returns it"""
        return math.sqrt(sum(x**2 for x in self.components))

    def __add__(self, other: Vector) -> Vector:
        """Adding vectors, returns Vector instance"""
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions")
        result = tuple(a + b for a, b in zip(self.components, other.components))
        return Vector(*result)

    def __sub__(self, other: Vector) -> Vector:
        """Subtraction of vectors, returns Vector instance"""
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions")
        result = tuple(a - b for a, b in zip(self.components, other.components))
        return Vector(*result)

    def __mul__(self, other: Vector) -> int:
        """Scalar product, returns Vector instance"""
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions")
        return sum(a * b for a, b in zip(self.components, other.components))

    def __lt__(self, other: Vector) -> bool:
        """Comparing vectors by length"""
        return self.length() < other.length()

    def __eq__(self, other: Vector) -> bool:
        """Checks the equality of vectors"""
        return self.length() == other.length()

    def __gt__(self, other: Vector) -> bool:
        """the first vector is greater than the second"""
        return self.length() > other.length()

    def __repr__(self) -> str:
        return f"Vector{self.components}"


def main():
    """main def"""
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)

    print("v1 =", v1)
    print("v2 =", v2)

    print("v1 + v2 =", v1 + v2)
    print("v1 - v2 =", v1 - v2)
    print("v1 · v2 =", v1 * v2)

    print("Length v1 =", v1.length())
    print("Length v2 =", v2.length())

    print("v1 < v2:", v1 < v2)
    print("v1 == v2:", v1 == v2)
    print("v1 > v2:", v1 > v2)


if __name__ == "__main__":
    main()
