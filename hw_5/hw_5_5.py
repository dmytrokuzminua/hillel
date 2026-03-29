""" Homework 5 task 5 """


class MutableClass:
    """Mutable class with the ability 
    to dynamically add and remove object attributes"""
    def __init__(self):
        self.name = None

    def add_attribute(self, name: str, value: str) -> None:
        """Add attribute to object"""
        setattr(self, name, value)

    def remove_attribute(self, name: str) -> None:
        """Remove attribute from object"""
        if hasattr(self, name):
            delattr(self, name)
        else:
            raise AttributeError(f"Атрибут '{name}' не існує")


def main():
    """main def"""
    obj = MutableClass()

    obj.add_attribute("name", "Python")
    print(obj.name)

    obj.remove_attribute("name")


if __name__ == "__main__":
    main()
