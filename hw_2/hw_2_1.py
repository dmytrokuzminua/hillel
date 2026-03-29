""" Homework 2 task 1 """


def sum(*args: int|float) -> None:
    """own function with name -sum- returns None"""
    print("This is my custom sum function!")


def main():
    """main def"""
    my_list = [1,5,7,9]
    print(f"step 1: {__builtins__.sum(my_list)}")
    print(f"step 2: {sum(my_list)}") # print message and returns None
    print(f"step 3: {__builtins__.sum(my_list)}")


if __name__ == "__main__":
    main()
