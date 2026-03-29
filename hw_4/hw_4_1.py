""" Homework 4 task 1 """


class UnknownOperationError(Exception):
    """Own exception for unknown operations"""
    pass


def main():
    """main def"""
    print("Калькулятор (формату: 10 + 5). Введіть 'off' для выходу.")

    while True:
        user_input = input("> ").strip().lower()
        if user_input == 'off':
            break

        try:
            parts = user_input.split()
            if len(parts) != 3:
                raise ValueError("Неправильний формат. Потрібно: Число Операція Число")

            num1 = float(parts[0])
            op = parts[1]
            num2 = float(parts[2])

            if op == '+':
                res = num1 + num2
            elif op == '-':
                res = num1 - num2
            elif op == '*':
                res = num1 * num2
            elif op == '/':
                res = num1 / num2
            else:
                raise UnknownOperationError(f"Операція '{op}' не подтримується")

            print(f"Результат: {res}")

        except ValueError as e:
            print(f"Помилка значення: {e}")
        except ZeroDivisionError:
            print("Помилка: Поділ на нуль!")
        except UnknownOperationError as e:
            print(f"Помилка операції: {e}")
        except OverflowError:
            print("Помилка: Число занадто велике (переповнення)!")


if __name__ == "__main__":
    main()
