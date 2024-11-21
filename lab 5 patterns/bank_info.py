# bank_info.py
from typing import List

class BankInfo:
    def __init__(self, bank_name: str, holder_name: str, account_number: str):
        self.bank_name = bank_name
        self.holder_name = holder_name
        self.accounts_number = [account_number]
        self.credit_history = {}

    def transaction_list(self, account_number: str) -> List[str]:
        # Приклад довільних транзакцій для цього рахунку
        transactions = [
            f"Транзакція 1 для рахунку {account_number}",
            f"Транзакція 2 для рахунку {account_number}"
        ]
        return transactions

    def give_details(self, *args) -> dict:
        return {
            "bank_name": self.bank_name,
            "holder_name": self.holder_name,
            "accounts_number": self.accounts_number,
            "credit_history": self.credit_history,
            "transactions": self.transaction_list(self.accounts_number[0])
        }
