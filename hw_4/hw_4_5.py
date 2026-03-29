""" Homework 4 task 5 """


class InsufficientFundsException(Exception):
    """Exception: insufficient funds in the account"""
    def __init__(self, required_amount: int, current_balance: int, currency="UAH", transaction_type="purchase") -> None:
        self.required_amount = required_amount
        self.current_balance = current_balance
        self.currency = currency
        self.transaction_type = transaction_type

        message = f"Недостатньо коштів для {transaction_type}: потрібно {required_amount} {currency}"
        super().__init__(message)


class BankAccount:
    """Class Bank account"""
    def __init__(self, owner: str, balance: int, currency="UAH") -> None:
        self.owner = owner
        self.balance = balance
        self.currency = currency

    def cash_withdrawal(self, amount: int) -> None:
        """Cash withdrawal method"""
        if amount > self.balance:
            raise InsufficientFundsException(amount, self.balance, self.currency, "withdrawal")
        self.balance -= amount
        print(f"Успішне зняття: {amount} {self.currency}. Залишок: {self.balance}")

    def make_purchase(self, item_name: str, price: int) -> None:
        """Purchase of goods method"""
        if price > self.balance:
            raise InsufficientFundsException(price, self.balance, self.currency, f"purchase of {item_name}")
        self.balance -= price
        print(f"Покупка '{item_name}' успішна! Залишок: {self.balance} {self.currency}")


def main():
    """main def"""
    account = BankAccount("Дмитро", 1500, "UAH")

    try:
        account.make_purchase("Навушники", 1200)
        account.cash_withdrawal(500)

    except InsufficientFundsException as e:
        print(f"\n[ВІДМОВА В ОПЕРАЦІЇ]")
        print(f"Тип транзакції: {e.transaction_type}")
        print(f"Ваш баланс: {e.current_balance} {e.currency}")
        print(f"Необхідна сума: {e.required_amount} {e.currency}")
        print(f"Бракує: {e.required_amount - e.current_balance} {e.currency}")


if __name__ == "__main__":
    main()
