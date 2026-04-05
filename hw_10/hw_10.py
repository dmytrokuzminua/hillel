"""Homework 10
console application for managing the "Kinobase" database """


import sqlite3
from datetime import datetime


def create_connection() -> tuple[sqlite3.Connection, sqlite3.Cursor]:
    """Create connection to database & cursor & returns they"""
    conn = sqlite3.connect("cinema.db")
    cursor = conn.cursor()
    return conn, cursor


def movie_age(year: int) -> int:
    """Returns the age of the movi. Is substituted into a database query"""
    return datetime.now().year - year


def create_tables(conn: sqlite3.Connection) -> None:
    try:
        with conn:
            conn.execute("""
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                release_year INTEGER,
                genre TEXT
            )
            """)

            conn.execute("""
            CREATE TABLE IF NOT EXISTS actors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                birth_year INTEGER
            )
            """)

            conn.execute("""
            CREATE TABLE IF NOT EXISTS movie_cast (
                movie_id INTEGER,
                actor_id INTEGER,
                PRIMARY KEY(movie_id, actor_id),
                FOREIGN KEY(movie_id) REFERENCES movies(id) ON DELETE CASCADE,
                FOREIGN KEY(actor_id) REFERENCES actors(id) ON DELETE CASCADE
            )
            """)

        conn.create_function("movie_age", 1, movie_age)

    except sqlite3.Error as e:
        print("Помилка при створенні таблиць:", e)


def add_movie(conn: sqlite3.Connection, cursor: sqlite3.Cursor) -> None:
    """Adds a movie to the database and the movie cast"""
    title = input("Назва: ")
    year = int(input("Рік: "))
    genre = input("Жанр: ")

    cursor.execute("INSERT INTO movies (title, release_year, genre) VALUES (?, ?, ?)",
                   (title, year, genre))
    movie_id = cursor.lastrowid

    cursor.execute("SELECT id, name FROM actors")
    actors = cursor.fetchall()

    if actors:
        print("Список акторів:")
        for actor in actors:
            print(f"{actor[0]}: {actor[1]}")

        ids = input("Введіть ID акторів через кому: ")
        for aid in ids.split(","):
            cursor.execute("INSERT INTO movie_cast VALUES (?, ?)",
                           (movie_id, int(aid)))

    conn.commit()


def add_actor(conn: sqlite3.Connection, cursor: sqlite3.Cursor) -> None:
    """Add new record to the actors table in the database"""
    name = input("Ім'я: ")
    year = int(input("Рік народження: "))
    cursor.execute("INSERT INTO actors (name, birth_year) VALUES (?, ?)",
                   (name, year))
    conn.commit()


def show_movies_with_actors(cursor: sqlite3.Cursor) -> None:
    """Show all movies with actors"""
    cursor.execute("""
    SELECT m.title, GROUP_CONCAT(a.name, ', ')
    FROM movies m
    INNER JOIN movie_cast mc ON m.id = mc.movie_id
    INNER JOIN actors a ON mc.actor_id = a.id
    GROUP BY m.id
    """)

    for i, row in enumerate(cursor.fetchall(), 1):
        print(f"{i}. {row[0]} — {row[1]}")


def show_genres(cursor: sqlite3.Cursor) -> None:
    """Show unique genres"""
    cursor.execute("SELECT DISTINCT genre FROM movies")
    for g in cursor.fetchall():
        print(g[0])


def count_by_genre(cursor: sqlite3.Cursor) -> None:
    """Show number of movies by genre"""
    cursor.execute("""
    SELECT genre, COUNT(*)
    FROM movies
    GROUP BY genre
    """)
    for row in cursor.fetchall():
        print(f"{row[0]}: {row[1]}")


def avg_actor_birth_by_genre(cursor: sqlite3.Cursor) -> None:
    """Show the average year of birth of actors in films of a specific genre"""
    genre = input("Введіть жанр: ")

    cursor.execute("""
    SELECT a.birth_year
    FROM actors a
    INNER JOIN movie_cast mc ON a.id = mc.actor_id
    INNER JOIN movies m ON m.id = mc.movie_id
    WHERE m.genre = ?
    """, (genre,))

    rows = cursor.fetchall()

    if not rows:
        print("Немає даних")
        return

    current_year = datetime.now().year

    ages = []
    for (birth_year,) in rows:
        age = current_year - birth_year
        ages.append(age)

    avg_age = sum(ages) / len(ages)

    print(f"Середній вік акторів: {round(avg_age, 2)}")


def search_movie(cursor: sqlite3.Cursor) -> None:
    """Search movie by keyword"""
    keyword = input("Ключове слово: ")

    if not keyword:
        print("Порожній запит")
        return

    cursor.execute("""
    SELECT title, release_year
    FROM movies
    WHERE title LIKE ? COLLATE NOCASE
    """, (f"%{keyword}%",))

    results = cursor.fetchall()

    if results:
        print("Знайдені фільми:")
        for i, row in enumerate(results, 1):
            print(f"{i}. {row[0]} ({row[1]})")
    else:
        print("Нічого не знайдено")


def pagination(cursor: sqlite3.Cursor) -> None:
    """Show movies (with pagination)"""
    limit = int(input("Скільки показати: "))
    offset = int(input("Зсув: "))

    cursor.execute("""
    SELECT title FROM movies
    LIMIT ? OFFSET ?
    """, (limit, offset))

    for row in cursor.fetchall():
        print(row[0])


def union_query(cursor: sqlite3.Cursor) -> None:
    """Show all actors' names and all movie titles"""
    cursor.execute("""
    SELECT name FROM actors
    UNION
    SELECT title FROM movies
    """)
    for row in cursor.fetchall():
        print(row[0])


def show_movie_age(cursor: sqlite3.Cursor) -> None:
    """Show age of movie"""
    cursor.execute("""
    SELECT title, movie_age(release_year)
    FROM movies
    """)
    for row in cursor.fetchall():
        print(f"{row[0]} — {row[1]} років")


def main():
    """Main def"""
    try:
        conn, cursor = create_connection()
        with conn:
            create_tables(conn)

        while True:
            print("""
            1. Додати фільм
            2. Додати актора
            3. Показати всі фільми з акторами
            4. Показати унікальні жанри
            5. Показати кількість фільмів за жанром
            6. Середній рік народження акторів за жанром
            7. Пошук фільму
            8. Пагінація
            9. UNION (актори + фільми)
            10. Вік фільмів
            0. Вихід
            """)

            choice = input("Вибір: ")

            if choice == "1":
                add_movie(conn, cursor)
            elif choice == "2":
                add_actor(conn, cursor)
            elif choice == "3":
                show_movies_with_actors(cursor)
            elif choice == "4":
                show_genres(cursor)
            elif choice == "5":
                count_by_genre(cursor)
            elif choice == "6":
                avg_actor_birth_by_genre(cursor)
            elif choice == "7":
                search_movie(cursor)
            elif choice == "8":
                pagination(cursor)
            elif choice == "9":
                union_query(cursor)
            elif choice == "10":
                show_movie_age(cursor)
            elif choice == "0":
                break
            else:
                print("Невірний вибір")

        conn.close()

    except sqlite3.Error as e:
        print("Критична помилка БД:", e)


if __name__ == "__main__":
    main()
