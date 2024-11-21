# bank_customer.py
from dataclasses import dataclass
from bank_info import BankInfo
from credit_card import CreditCard

@dataclass
class PersonalInfo:
    name: str
    address: str
    phone_number: str

class BankCustomer:
    def __init__(self, personal_info: PersonalInfo, bank_info: BankInfo):
        self.personal_info = personal_info
        self.bank_details = bank_info

    def give_details(self, *args) -> dict:
        personal_details = {
            "name": self.personal_info.name,
            "address": self.personal_info.address,
            "phone_number": self.personal_info.phone_number
        }
        bank_details = self.bank_details.give_details(*args)
        personal_details.update(bank_details)
        return personal_details
