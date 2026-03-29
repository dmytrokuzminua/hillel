""" Homework 3 task 8 """


from __future__ import annotations


class Price:
    """Class Price"""
    def __init__(self, amount: int|float) -> None:
        self.amount = round(float(amount), 2)

    def __add__(self, other: Price) -> float:
        """Adding prices"""
        if not isinstance(other, Price):
            raise TypeError("Can only add Price with Price")
        return Price(self.amount + other.amount)

    def __sub__(self, other: Price) -> float:
        """Subtraction of prices"""
        if not isinstance(other, Price):
            raise TypeError("Can only subtract Price with Price")
        return Price(self.amount - other.amount)

    def __eq__(self, other: Price) -> bool:
        """Price comparison"""
        return self.amount == other.amount

    def __lt__(self, other: Price)-> bool:
        """The first price is less than the second."""    
        return self.amount < other.amount

    def __le__(self, other: Price)-> bool:
        """The first price is less or equal than the second."""
        return self.amount <= other.amount

    def __gt__(self, other: Price)-> bool:
        """the first price is higher than the second"""
        return self.amount > other.amount

    def __ge__(self, other: Price)-> bool:
        """the first price is higher or equal than the second"""
        return self.amount >= other.amount

    def __repr__(self) -> str:
        return f"${self.amount:.2f}"


def main():
    """main def"""
    price1 = Price(10)
    price2 = Price(5.678)
    price3 = Price(15.999)

    print("Prices:", price1, price2, price3)

    print("Addition:", price1 + price2)
    print("Subtraction:", price3 - price1)

    print("Comparison:")
    print(price1 < price2)
    print(price2 == Price(5.68))
    print(price3 > price1)


if __name__ == "__main__":
    main()
