"""Homework 7 task 4"""


import json


JSON_FILE = "books.json"


def load_books(file_path: str) -> list:
    """Loads a list of books from a JSON file"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            books = json.load(f)
        return books
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
        return []
    except json.JSONDecodeError:
        print(f"Помилка розбору JSON у файлі {file_path}.")
        return []


def show_available_books(books: list) -> None:
    """Displays a list of available books (availability=True)"""
    available_books = [book for book in books if book.get("наявність") is True]
    if not available_books:
        print("Доступних книг немає.")
    else:
        print("Доступні книги:")
        for book in available_books:
            print(f"{book['назва']} (Автор: {book['автор']}, Рік: {book['рік']})")


def add_book(file_path: str, title: str, author: str, year: int, available: bool) -> None:
    """Adds a new book to the JSON file"""
    books = load_books(file_path)
    new_book = {
        "назва": title,
        "автор": author,
        "рік": year,
        "наявність": available
    }
    books.append(new_book)
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(books, f, ensure_ascii=False, indent=4)
        print(f"Книга '{title}' успішно додана.")
    except Exception as e:
        print(f"Помилка при збереженні файлу: {e}")


if __name__ == "__main__":
    books = load_books(JSON_FILE)
    show_available_books(books)

    add_book(JSON_FILE, "Книга 3", "Автор 3", 2022, True)

    books = load_books(JSON_FILE)
    show_available_books(books)
