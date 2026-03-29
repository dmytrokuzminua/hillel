""" Homework 2 task 5 """


events = []


def event_calendar():
    """Event calendar function, returns functions """
    def add_event(event: str) -> None:
        """Add event to calendar"""
        events.append(event)
        print(f"Подію {event} додано.")

    def delete_event(event: str) -> None:
        """Delete event from calendar returns None"""
        if event in events:
            events.remove(event)
            print(f"Подію {event} видалено.")
        else:
            print("Подію не знайдено.")

    def view_events() -> None:
        """Print all future events returns None"""
        if events:
            print("Майбутні події:")
            for e in events:
                print("-", e)
        else:
            print("Подій немає.")

    return add_event, delete_event, view_events


def main():
    """main def"""
    add_event, delete_event, view_events = event_calendar()
    add_event("Зробити домашку")
    add_event("Передивитись запис зустрічі")
    view_events()

    delete_event("Зробити домашку")
    view_events()


if __name__ == "__main__":
    main()
