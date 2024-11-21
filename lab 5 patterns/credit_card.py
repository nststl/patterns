# credit_card.py
import hashlib

class CreditCard:
    def __init__(self, client: str, account_number: str, credit_limit: float, grace_period: int, cvv: str):
        self.client = client
        self.account_number = account_number
        self.credit_limit = credit_limit
        self.grace_period = grace_period
        self._cvv_hash = None  # CVV зберігається як хеш

    def encrypt(self, value: str) -> None:
        # Шифруємо CVV (хешуємо за допомогою SHA-256)
        self._cvv_hash = hashlib.sha256(value.encode()).hexdigest()

    def decrypt(self) -> str:
        # Хеш неможливо розшифрувати. Це тут для довідки.
        return "CVV захищено хешуванням і не може бути розшифровано"

    @property
    def cvv(self):
        # Повертаємо хеш CVV
        return self._cvv_hash

    @cvv.setter
    def cvv(self, value: str):
        self.encrypt(value)  # При встановленні CVV його хешуємо

    def give_details(self, *args) -> dict:
        return {
            "client": self.client,
            "account_number": self.account_number,
            "credit_limit": self.credit_limit,
            "grace_period": self.grace_period,
            "cvv_hash": self._cvv_hash  # Повертаємо хеш CVV
        }
