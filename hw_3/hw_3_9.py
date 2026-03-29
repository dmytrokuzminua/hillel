""" Homework 3 task 9 """


class ProductWithGetSet:
    """Class Product with setter/getter"""
    def __init__(self, name: str, price: int|float) -> None:
        self.name = name
        self._price = None
        self.set_price(price)

    def get_price(self) -> int|float:
        """Returns price"""
        return self._price

    def set_price(self, value: int|float):
        """Set new price value"""
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    def __repr__(self) -> str:
        return f"{self.name}: ${self._price:.2f}"


class ProductWithProperty:
    """Class Product with property"""
    def __init__(self, name: str, price: int|float):
        self.name = name
        self._price = None
        self.price = price

    @property
    def price(self) -> int|float:
        """Returns price"""
        return self._price

    @price.setter
    def price(self, value: int|float):
        """Set new price value"""
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    def __repr__(self) -> str:
        return f"{self.name}: ${self._price:.2f}"


class PriceDescriptor:
    """Class Price`s descriptor"""
    def __init__(self, name: str ="price") -> None:
        self.name = name

    def __get__(self, instance, owner):
        """Returns price"""
        if instance is None:
            return self
        return instance.__dict__.get(self.name, 0)

    def __set__(self, instance, value) -> None:
        """Set new price value"""
        if value < 0:
            raise ValueError("Price cannot be negative")
        instance.__dict__[self.name] = value


class ProductWithDescriptor:
    """Class Product with descriptor"""
    price = PriceDescriptor()

    def __init__(self, name: str, price: int|float) -> None:
        self.name = name
        self.price = price

    def __repr__(self) -> str:
        return f"{self.name}: ${self.price:.2f}"


def main():
    """main def"""
    print("=== Testing get/set methods ===")
    p1 = ProductWithGetSet("Apple", 10)
    print(p1)
    p1.set_price(15)
    print("Updated price:", p1.get_price())
    try:
        p1.set_price(-5)
    except ValueError as e:
        print("Error:", e)

    print("\n=== Testing @property ===")
    p2 = ProductWithProperty("Banana", 5)
    print(p2)
    p2.price = 8
    print("Updated price:", p2.price)
    try:
        p2.price = -2
    except ValueError as e:
        print("Error:", e)

    print("\n=== Testing descriptor ===")
    p3 = ProductWithDescriptor("Orange", 12)
    print(p3)
    p3.price = 20
    print("Updated price:", p3.price)
    try:
        p3.price = -10
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()

"""Висновок: я вважаю, що @property в данному прикладі ннайбільш підходящий.
При цьому варианті не програма не перенавантажується кодом, але зберігається
гнучкість та можливість валідації у .setter"""
