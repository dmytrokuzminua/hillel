""" Homework 5 task 6 """


class MyClass:
    """My test Class for calling with proxy"""
    def greet(self, name: str) -> str:
        """Returns greeting string 'Hello...'"""
        return f"Hello, {name}!"


class Proxy:
    """Proxy class for redirecting method 
    calls to this object"""
    def __init__(self, obj: MyClass) -> None:
        """init proxy class"""
        self._obj = obj

    def __getattr__(self, name: str) -> str:
        """Get the """
        attr = getattr(self._obj, name)

        if callable(attr):
            def wrapper(*args, **kwargs) -> MyClass:
                """Logs the call, returns method`s call result"""
                print("Calling method:")
                print(f"{name} with args: {args}")
                return attr(*args, **kwargs)
            return wrapper

        return attr


def main():
    """main def"""
    obj = MyClass()
    proxy = Proxy(obj)

    print(proxy.greet("Alice"))


if __name__ == "__main__":
    main()
