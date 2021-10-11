from random import randint


class BankAccount:
    """Класс для создания учетной записи клиента банка."""

    def __init__(self, name: str, balance: float = 0.0) -> None:
        """Инициализирует имя и начальный баланс."""
        self.id = randint(1, 100)
        self.name = name
        self.balance = balance
        print('Учетная запись клиента банка создана.')

    def get_id(self) -> int:
        """Возвращает ID клиента."""
        return self.id

    def get_name(self) -> str:
        """Возвращает имя."""
        return self.name

    def get_balance(self) -> float:
        """Возвращает баланс."""
        return self.balance

    def set_earn(self, earn_value: float) -> None:
        """Внести валюту на счет."""
        self.balance += earn_value

    def set_withdrawal(self, withdrawal_value: float) -> None:
        """Снятие валюты со счета."""
        self.balance -= withdrawal_value