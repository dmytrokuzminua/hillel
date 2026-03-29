""" Homework 5 task 2 """


class Calculator:
    """Class for adding & subtracting two values"""
    def add(self, a: int|float, b: int|float) -> int|float:
        """ Adding a+b & returns value"""
        return a + b

    def subtract(self, a: int|float, b: int|float) -> int|float:
        """ Subtracting a-b & returns value"""
        return a - b


def call_function(obj: Calculator, method_name: str, *args) -> int|float:
    """ Get method of object by name & call it with *args """
    method = getattr(obj, method_name)
    return method(*args)


def main():
    """main def"""
    calc = Calculator()
    print(call_function(calc, "add", 10, 5))
    print(call_function(calc, "subtract", 10, 5))


if __name__ == "__main__":
    main()
