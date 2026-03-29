""" Homework 5 task 1 """


class MyClass:
    """Test class"""
    def __init__(self, value: int|float|str) -> None:
        self.value = value

    def say_hello(self) -> str:
        """Returs value of 'self.value' """
        return f"Hello, {self.value}"


def analyze_object(obj) -> None:
    """Analyzing object and print type of object, 
    methods & attributes, types of methods & attributes"""
    print(f"Тип об'єкта: {type(obj)}\n")

    attributes = dir(obj)

    print("Методи та атрибути об'єкта:")
    for attr in attributes:
        print(attr)

    print("\nТип кожного атрибута:")
    for attr in attributes:
        try:
            attr_value = getattr(obj, attr)
            print(f"{attr}: {type(attr_value)}")
        except Exception as e:
            print(f"{attr}: Не вдалося отримати ({e})")


def main():
    """main def"""
    obj = MyClass("World")
    analyze_object(obj)
    print("\n")
    analyze_object("Test string: class str")


if __name__ == "__main__":
    main()
