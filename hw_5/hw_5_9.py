""" Homework 5 task 9 """


class DynamicProperties:
    """Class for adding properties dynamicly"""
    def __init__(self) -> None:
        self._values = {}

    def add_property(self, name: str, default_value=None) -> None:
        """Adding property to the object, set & get it"""
        self._values[name] = default_value

        def getter(self):
            """Property getter, returns property value"""
            return self._values[name]

        def setter(self, value) -> None:
            """Property setter"""
            self._values[name] = value

        setattr(self.__class__, name, property(getter, setter))


def main():
    """main def"""
    obj = DynamicProperties()

    obj.add_property('name', 'default_name')
    print(obj.name)

    obj.name = "Python"
    print(obj.name)


if __name__ == "__main__":
    main()
