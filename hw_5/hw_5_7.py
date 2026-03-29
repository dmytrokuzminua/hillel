""" Homework 5 task 7 """


from __future__ import annotations


class LogDecorator:
    """Decorator class, logs method calls"""
    def __init__(self, cls: MyClass) -> None:
        self.cls = cls

        for attr_name, attr_value in cls.__dict__.items():
            if callable(attr_value):
                setattr(cls, attr_name, self.make_wrapper(attr_name, attr_value))

    def make_wrapper(self, method_name: str, method) -> MyClass:
        """Make the wrapper"""
        def wrapper(self_obj, *args, **kwargs):
            """Wrapper for method calling"""
            print(f"Logging: {method_name} called with {args}")
            return method(self_obj, *args, **kwargs)
        return wrapper

    def __call__(self, *args, **kwargs) -> MyClass:
        """Method calling"""
        return self.cls(*args, **kwargs)


@LogDecorator
class MyClass:
    """My test class for adding & subtracting"""
    def add(self, a: int|float, b: int|float) -> int|float:
        """Adding a + b"""
        return a + b

    def subtract(self, a: int|float, b: int|float) -> int|float:
        """Subtracting a - b"""
        return a - b


def main():
    """main def"""
    obj = MyClass()
    obj.add(5, 3)
    obj.subtract(5, 3)


if __name__ == "__main__":
    main()
