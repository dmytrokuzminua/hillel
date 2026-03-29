""" Homework 8 task 3 """


class UserManager:
    """Class to manage users"""
    def __init__(self):
        self.users = []

    def add_user(self, name: str, age: int) -> None:
        """Add a new user"""
        self.users.append({"name": name, "age": age})

    def remove_user(self, name: str) -> None:
        """Remove a user"""
        self.users = [u for u in self.users if u["name"] != name]

    def get_all_users(self) -> list:
        """Return list of all users"""
        return self.users
