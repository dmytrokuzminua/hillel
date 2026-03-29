""" Homework 4 task 3 """


class GameEventException(Exception):
    """Base class for game events"""
    def __init__(self, event_type: str, details: dict) -> None:
        self.event_type = event_type
        self.details = details
        super().__init__(f"Game Event: {event_type}")


def play_turn(hp: int, exp: int) -> None:
    """Simulation of a game move"""
    if hp <= 0:
        raise GameEventException("death", {
            "reason": "падання в прірву",
            "location": "Ліс"
        })

    if exp >= 100:
        raise GameEventException("levelUp", {
            "new_level": 5,
            "bonus_points": 10,
            "unlocked_skill": "Fireball"
        })


def main():
    """main def"""
    try:
        play_turn(hp=50, exp=120)

    except GameEventException as e:
        print(f"--- [ПОДІЯ: {e.event_type.upper()}] ---")

        if e.event_type == "death":
            print(f"Гравця розбито! Причина: {e.details['reason']}.")
            print("Гра закінчена.")

        elif e.event_type == "levelUp":
            print(f"Вітаємо! Ваш новий рівень: {e.details['new_level']}.")
            print(f"Отримано очок: {e.details['bonus_points']}. Навичка: {e.details['unlocked_skill']}.")

    except Exception as e:
        print(f"Критична помилка системи: {e}")


if __name__ == "__main__":
    main()
