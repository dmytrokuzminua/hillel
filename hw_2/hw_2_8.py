""" Homework 2 task 8  """


from typing import Callable, Any, Optional, Union, Dict


UserSettingsCallable = Callable[[str, Optional[str], Optional[Union[str, bool]]], Any]

def create_user_settings() -> UserSettingsCallable:
    """Func of creating user's settings, returns closured function 'user_settings' """
    settings: Dict[str, Union[str, bool]] = {
        "theme": "light",
        "language": "uk",
        "notifications": True
        }

    def user_settings(action: str, key: Optional[str] = None, value: Optional[Union[str, bool]] = None) -> Any:
        """ Show or update user settings, returns settings or set settings """
        nonlocal settings
        if action == "view":
            return settings
        if action == "update":
            if key in settings:
                settings[key] = value  # type: ignore (якщо value може бути None)
                print(f"Налаштування '{key}' змінено на {value}")
            else:
                print(f"Налаштування '{key}' не існує")
        else:
            print("Невідома команда. Використовуйте 'view' or 'update'.")
    return user_settings


def main():
    """main def"""
    settings = create_user_settings()

    print(settings("view"))
    settings("update", "theme", "dark")
    settings("update", "language", "en")
    print(settings("view"))
    settings("update", "font_size", 12) # Тест помилкового значення налаштування


if __name__ == "__main__":
    main()
