""" Homework 5 task 10 """


from __future__ import annotations


class SingletonMeta(type):
    """Meta class that checks for a singleton"""
    _instances = {}

    def __call__(cls: Singleton, *args, **kwargs) -> Singleton:
        """Makes the object callable as a function"""
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    """Singlton class"""
    def __init__(self) -> None:
        print("Creating instance")


def main():
    """main def"""
    obj1 = Singleton()
    obj2 = Singleton()

    print(obj1 is obj2)


if __name__ == "__main__":
    main()
