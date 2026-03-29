""" Homework 2 task 4 """


DEFAULT_TIME = 60


def training_session(rounds: int) -> None:
    """ Calculate and print training`s session duration returns None """
    def adjust_time() -> int:
        """ Set time duration -5, returns time reduced by 5 """
        nonlocal additional_line
        additional_line = "(після коригування часу)"
        return time_per_round -5

    time_per_round = DEFAULT_TIME
    additional_line = ""
    for i in range(1, rounds + 1):
        print(f"Раунд {i}: {time_per_round} хвилин {additional_line}")
        time_per_round = adjust_time()


def main():
    """main def"""
    print("Результат:")
    training_session(5)


if __name__ == "__main__":
    main()
