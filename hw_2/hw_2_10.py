""" Homework 2 task 10 """


def create_product(name: str, price: int|float, quantity: int):
    """ Create product and change the price, returns currying functions 'get_info' & 'change_price' """
    def get_info() -> str:
        """ Returns product`s info"""
        return f"Товар: {name}, Ціна: {price}, Кількість: {quantity}"

    def change_price(new_price: int|float) -> None:
        """ Change the price of the product"""
        nonlocal price
        if new_price >= 0:
            price = new_price
            print(f"Ціна товару '{name}' змінена на {price}")
        else:
            print("Ціна не може бути від’ємною!")

    return get_info, change_price


def main():
    """main def"""
    get_product_info, change_product_price = create_product("Ноутбук", 15000, 10)

    print(get_product_info())
    change_product_price(14000)
    print(get_product_info())


if __name__ == "__main__":
    main()
