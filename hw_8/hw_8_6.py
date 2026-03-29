""" Homework 8 task 6 """


class BankAccount:
    """Class BankAccount"""
    def __init__(self, initial_balance: float = 0.0):
        self._balance = initial_balance

    def deposit(self, amount: float) -> None:
        """Deposit funds amount"""
        if amount < 0:
            raise ValueError("Amount must be positive")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        """Withdraw funds if there is enough in the account"""
        if amount < 0:
            raise ValueError("Amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    def get_balance(self) -> float:
        """Returns the current balance"""
        return self._balance
