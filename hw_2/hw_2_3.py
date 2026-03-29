""" Homework 2 task 3 """


discount = 0.1 


def create_order(price: float, add_addit_disc: bool) -> None:
    """ Create order function returns None """
    def apply_additional_discount() -> float:
        """ Add additional discount, returns new discount"""
        nonlocal new_price
        new_price = price * (1 - discount - 0.1)
        return discount + 0.1

    new_price = price * (1 - discount)
    if add_addit_disc:
        print(f"Початкова ціна: {price}, кінцева ціна зі знижкою {apply_additional_discount()*100}%: {new_price}")
    else:
        print(f"Початкова ціна: {price}, кінцева ціна зі знижкою {discount*100}%: {new_price}")


def main():
    """main def"""
    create_order(1000, False)
    create_order(1000, True)


if __name__ == "__main__":
    main()
