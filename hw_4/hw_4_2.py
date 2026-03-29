""" Homework 4 task 2 """


def main(file_path):
    """Reads numbers from a file and calculates the arithmetic mean"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read().split()

            if not data:
                print("Файл порожній. Середнє арифметичне обчислити неможливо.")
                return

            numbers = [float(x) for x in data]

            average = sum(numbers) / len(numbers)
            print(f"Середнє арифметичне: {average}")

    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{file_path}' не знайдено.")
    except ValueError:
        print("Помилка: Файл містить нечислові дані (літери або спецсимволи).")
    except Exception as e:
        print(f"Сталася непередбачена помилка: {e}")


if __name__ == "__main__":
    main('numbers.txt')
