""" Classwork 10"""


import sqlite3


def init_db(db_name="students.db"):

        conn = None
        try:
            conn = sqlite3.connect(db_name)
            cursor = conn.cursor()

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT,
                age INTEGER,
                phone TEXT,
                email TEXT)""")

            students_data = [
                ("Dmytro", "Kuzmin", 30, "+380501234567", "Dmytro.Kuzmin@example.com"),
                ("Roman", "Litvitskiy", 22, "+380671234567", "Roman.Litvitskiy@example.com"),
                ("Zahar", "Nevidomo", 19, "+380931234567", "Zahar.Nevidomo@example.com"),
                ("Dmytro", "Brikaylo", 21, "+380661234567", "Dmytro.Brikaylo@example.com"),
                ("Ivan", "Mazepa", 23, "+380991234567", "Ivan.Mazepa@example.com")
            ]

            cursor.executemany("""
            INSERT INTO students (first_name, last_name, age, phone, email)
            VALUES (?, ?, ?, ?, ?)
            """, students_data)

            conn.commit()

            cursor.execute("SELECT * FROM students")
            rows = cursor.fetchall()

            for row in rows:
                print(row)

        except sqlite3.Error as e:
            print(f"Помилка роботи з БД: {e}")

        finally:
            if conn:
                conn.close()
                print("З'єднання закрито")



if __name__ == "__main__":
    init_db()