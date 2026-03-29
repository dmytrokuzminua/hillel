""" Homework 5 task 4 """


def create_class(class_name: str, methods: dict):
    """Creating a class using 'type', returns new class"""
    return type(class_name, (), methods)


def say_hello(self) -> str:
    """Say Hello test method"""
    return "Hello!"


def say_goodbye(self) -> str:
    """Say Goodbye test method"""
    return "Goodbye!"


def main():
    """main def"""
    methods = {
        "say_hello": say_hello,
        "say_goodbye": say_goodbye
    }

    MyDynamicClass = create_class("MyDynamicClass", methods)

    obj = MyDynamicClass()
    print(obj.say_hello())
    print(obj.say_goodbye())


if __name__ == "__main__":
    main()
