""" Homework 5 task 8 """


import inspect


class Parent:
    """Parent class"""
    def parent_method(self) -> None:
        """Test method of Parent class"""
        pass

    def print_something(self) -> None:
        """Test method of Parent class"""
        pass


class Child(Parent):
    """Child class"""
    def child_method(self) -> None:
        """Test method of Child class"""
        pass


def analyze_inheritance(cls: Child) -> None:
    """Analyzes the inheritance of a class, 
    prints all the methods it inherits from base classes"""
    inherited_methods = []

    for base in cls.__mro__[1:]:
        for name, obj in inspect.getmembers(base, predicate=inspect.isfunction):
            if not hasattr(cls, name) or getattr(cls, name) == obj:
                inherited_methods.append((name, base.__name__))

    print(f"Клас {cls.__name__} наслідує:\n")
    if inherited_methods:
        for name, base_name in inherited_methods:
            print(f"- {name} з {base_name}")
    else:
        print("- <немає успадкованих методів>")


def main():
    """main def"""
    analyze_inheritance(Child)


if __name__ == "__main__":
    main()
