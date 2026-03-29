""" Homework 5 task 3 """


import inspect
import importlib


def analyze_module(module_name: str) -> None:
    """Import module by name investigates it 
    and prints a list of all classes, functions"""
    module = importlib.import_module(module_name)

    functions = []
    classes = []

    for name, obj in inspect.getmembers(module):
        if inspect.isfunction(obj) or inspect.isbuiltin(obj):
            try:
                sig = inspect.signature(obj)
                functions.append(f"- {name}{sig}")
            except ValueError:
                functions.append(f"- {name}(...)")
        elif inspect.isclass(obj):
            classes.append(f"- {name}")

    print("Функції:\n")
    if functions:
        for func in functions:
            print(func)
    else:
        print("- <немає функцій>")

    print("\nКласи:\n")
    if classes:
        for cls in classes:
            print(cls)
    else:
        print("- <немає класів>")


def main():
    """main def"""
    analyze_module("math")


if __name__ == "__main__":
    main()
