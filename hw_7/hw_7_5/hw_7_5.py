"""Homework 7 task 5"""


import xml.etree.ElementTree as EntEl


XML_FILE = "products.xml"

def read_products(file_path: str):
    """Reads an XML file and outputs product names and quantities"""
    try:
        tree = EntEl.parse(file_path)
        root = tree.getroot()
        print("Список продуктів:")
        for product in root.findall("product"):
            name = product.find("name").text
            quantity = product.find("quantity").text
            print(f"{name}: {quantity} шт.")
        return tree, root
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
        return None, None
    except EntEl.ParseError:
        print(f"Помилка розбору XML у файлі {file_path}.")
        return None, None


def update_quantity(file_path: str, product_name: str, new_quantity: int) -> None:
    """Updates the quantity of a specific product in an XML file"""
    tree, root = read_products(file_path)
    if root is None:
        return

    found = False
    for product in root.findall("product"):
        name = product.find("name").text
        if name == product_name:
            product.find("quantity").text = str(new_quantity)
            found = True
            break

    if found:
        tree.write(file_path, encoding="utf-8", xml_declaration=True)
        print(f"Кількість продукту '{product_name}' оновлено на {new_quantity} шт.")
    else:
        print(f"Продукт '{product_name}' не знайдено.")


if __name__ == "__main__":
    read_products(XML_FILE)
    update_quantity(XML_FILE, "Молоко", 30)
    read_products(XML_FILE)
