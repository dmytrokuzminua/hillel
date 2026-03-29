""" Homework 3 task 6 """


import re


class User:
    """User class"""
    def __init__(self, first_name: str, last_name: str, email: str) -> None:
        self._first_name = first_name
        self._last_name = last_name
        self._email = None
        self.email = email

    @property
    def first_name(self) -> str:
        """Returns first_name property"""
        return self._first_name

    @first_name.setter
    def first_name(self, value: str) -> None:
        """First_name setter"""
        if not value:
            raise ValueError("First name cannot be empty")
        self._first_name = value

    @property
    def last_name(self) -> str:
        """Returns last_name property"""
        return self._last_name

    @last_name.setter
    def last_name(self, value: str) -> None:
        """Last_name setter"""
        if not value:
            raise ValueError("Last name cannot be empty")
        self._last_name = value

    @property
    def email(self) -> str:
        """Returns Email property"""
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        """Email setter with validate"""
        if self.validate_email(value):
            self._email = value
        else:
            raise ValueError(f"Invalid email address: {value}")

    @staticmethod
    def validate_email(email: str) -> bool:
        """ Simple format check email: something@something.domain """
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None

    def __repr__(self) -> str:
        return f"User({self.first_name} {self.last_name}, {self.email})"


def main():
    """main def"""
    user1 = User("Ivan", "Mazepa", "ivan.mazepa@example.com")
    print(user1)

    user1.first_name = "Taras"
    user1.last_name = "Shevchenko"
    print("Updated:", user1)

    try:
        user1.email = "invalid-email.com"
    except ValueError as e:
        print("Error:", e)

    print("Email valid?", User.validate_email("test@domain.org"))


if __name__ == "__main__":
    main()
