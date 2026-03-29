""" Homework 7 task 1 """


from math_utils import factorial, gcd
from string_utils import to_uppercase, strip_spaces


def main():
    """Main def"""
    print("---Math Utilities---")
    print("Factorial of 5:", factorial(5))
    print("GCD of 12 and 18:", gcd(12, 18))

    print("\n---String Utilities---")
    text = "   hello world   "
    print("Original text:", repr(text))
    print("Uppercase:", to_uppercase(text))
    print("Stripped:", repr(strip_spaces(text)))


if __name__ == "__main__":
    main()
