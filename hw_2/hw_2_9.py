""" Homework 2 task 9  """


def memoize(func):
    """ Cash function, returns function 'wrapper'"""
    cache = {}

    def wrapper(n):
        if n in cache:
            return cache[n]
        result = func(n)
        cache[n] = result
        return result

    return wrapper


def factorial(n: int) -> int:
    """ Factorial recurtion functuon, returns n! """
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


def main():
    """main def"""
    cached_factorial = memoize(factorial)

    for i in range(10):
        print(f"{i}! = {cached_factorial(i)}")


if __name__ == "__main__":
    main()
