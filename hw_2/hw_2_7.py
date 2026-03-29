""" Homework 2 task 7 """


total_expense = 0


def add_expense(new_sum: int|float) -> None:
    """ Adds the sum of expenses, returns None """
    global total_expense
    total_expense += new_sum
    print(f"Додано витрату: {new_sum}")


def get_expense() -> float:
    """ Returns the sum of expenses """
    return total_expense


def main():
    """main def"""
    while True:
        print("\nТрекер")
        print("add - Додати витрату")
        print("view - Показати загальну суму")
        print("exit - Вийти")

        command = input("Оберіть дію: ")

        if command == "add":
            amount = float(input("Введіть суму витрати: "))
            add_expense(amount)
        elif command == "view":
            print(f"Загальна сума витрат: {get_expense()}")
        elif command == "exit":
            print("Вихід з програми.")
            break
        else:
            print("Неіснуюча команда!")


if __name__ == "__main__":
    main()
