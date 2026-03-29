""" Homework 2 task 2 """


subscribers = []


def  subscribe(new_subscriber: str) -> None:
    """ Add new subscriber to subscribers """
    def confirm_subscription() -> None:
        """ Confirm a new subscriber returns None"""
        print(f"Підписка підтверджена для {new_subscriber}.")

    subscribers.append(new_subscriber)
    confirm_subscription()


def unsubscribe(subscriber_to_delete: str) -> None:
    """ Delete targeted subcriber returns None """
    if subscriber_to_delete in subscribers:
        subscribers.remove(subscriber_to_delete)
        print(f"Підписника {subscriber_to_delete} вилучено!")
    else:
        print(f"Підписника {subscriber_to_delete} не знайдено!")


def main():
    """main def"""
    subscribe("Олена")
    subscribe("Ігор")
    print(subscribers)
    print(unsubscribe("Ігор"))
    print(unsubscribe("Олександр"))  # Тест помилкової відписки
    print(subscribers)


if __name__ == "__main__":
    main()
