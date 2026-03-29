"""Homework 7 task 3"""


import csv


CSV_FILE = "students.csv"

def read_students(file_path: str) -> list:
    """Reads data from a CSV file and returns a list of students as dictionaries"""
    students = []
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row['Вік'] = int(row['Вік'])
                row['Оцінка'] = int(row['Оцінка'])
                students.append(row)
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
    return students


def calculate_average_grade(students: list) -> float:
    """Calculates the average grade of students"""
    if not students:
        return 0
    total = sum(student['Оцінка'] for student in students)
    return total / len(students)


def add_student(file_path: str, name: str, age: int, grade: int) -> None:
    """Adds a new student to the CSV file"""
    try:
        with open(file_path, mode='a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([name, age, grade])
        print(f"Студент {name} успішно доданий.")
    except Exception as e:
        print(f"Помилка при додаванні студента: {e}")


if __name__ == "__main__":
    students = read_students(CSV_FILE)
    print("Список студентів:")
    for s in students:
        print(s)

    avg = calculate_average_grade(students)
    print(f"\nСередня оцінка студентів: {avg:.2f}")

    add_student(CSV_FILE, "Олена", 23, 92)

    students = read_students(CSV_FILE)
    avg = calculate_average_grade(students)
    print(f"\nНова середня оцінка студентів: {avg:.2f}")
