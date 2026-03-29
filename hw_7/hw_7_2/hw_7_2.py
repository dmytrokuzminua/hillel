"""Homework 7 task 2"""


import requests


def download_page(url: str, output_file: str) -> None:
    """Loads the page content from a URL and saves it to a file"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP помилка: {http_err}")
        return
    except requests.exceptions.ConnectionError:
        print("Помилка з'єднання. Сторінка недоступна.")
        return
    except requests.exceptions.Timeout:
        print("Таймаут підключення до сторінки.")
        return
    except requests.exceptions.RequestException as err:
        print(f"Невідома помилка: {err}")
        return

    # save site to the file
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(response.text)
        print(f"Сторінка успішно збережена у {output_file}")
    except Exception as e:
        print(f"Помилка запису у файл: {e}")


if __name__ == "__main__":
    url = "https://www.google.com/"
    output_file = "page.txt"
    download_page(url, output_file)