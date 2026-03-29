""" Homework 4 task 4 """


class InsufficientResourcesException(Exception):
    """Exclusion: lack of resources for activities"""
    def __init__(self, required_resource: str, required_amount: int, current_amount: int) -> None:
        self.required_resource = required_resource
        self.required_amount = required_amount
        self.current_amount = current_amount

        self.missing_amount = required_amount - current_amount

        super().__init__(f"Недостатньо ресурсу: {required_resource}")


class Player:
    """Class Player"""
    def __init__(self, name: str, gold: int, mana: int) -> None:
        self.name = name
        self.resources = {"золото": gold, "мана": mana}

    def perform_action(self, action_name: str, cost_type: int, cost_value: int) -> None:
        """Perform an action"""
        print(f"--- Спроба: {action_name} (Вартість: {cost_value} {cost_type}) ---")

        current = self.resources.get(cost_type, 0)

        if current < cost_value:
            raise InsufficientResourcesException(cost_type, cost_value, current)

        self.resources[cost_type] -= cost_value
        print(f"Успіх! Залишок {cost_type}: {self.resources[cost_type]}")


def main():
    """main def"""
    hero = Player("Gendalf", gold=50, mana=20)

    try:
        hero.perform_action("Купівля меча", "золото", 30)
        hero.perform_action("Закляття вогню", "мана", 100)

    except InsufficientResourcesException as e:
        print(f"ПОМИЛКА: Вам не вистачає {e.missing_amount} од. ресурсу '{e.required_resource}'!")
        print(f"Маєте: {e.current_amount}, Потрібно: {e.required_amount}")


if __name__ == "__main__":
    main()
