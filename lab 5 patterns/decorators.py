# decorators.py
from credit_card import CreditCard
from bank_customer import BankCustomer

# Декоратор для CreditCard
class CreditCardDecorator:
    def __init__(self, card: CreditCard):
        self._card = card

    def give_details(self, *args) -> dict:
        return self._card.give_details(*args)

class GoldenCreditCard(CreditCardDecorator):
    def __init__(self, card: CreditCard):
        super().__init__(card)

    def give_details(self, *args) -> dict:
        details = super().give_details(*args)
        details["card_type"] = "Золота кредитна картка"
        return details

class CorporateCreditCard(CreditCardDecorator):
    def __init__(self, card: CreditCard):
        super().__init__(card)

    def give_details(self, *args) -> dict:
        details = super().give_details(*args)
        details["card_type"] = "Корпоративна кредитна картка"
        return details

# Декоратор для BankCustomer
class CustomerDecorator:
    def __init__(self, customer: BankCustomer):
        self._customer = customer

    def give_details(self, *args) -> dict:
        return self._customer.give_details(*args)

class VIPCustomer(CustomerDecorator):
    def __init__(self, customer: BankCustomer):
        super().__init__(customer)

    def give_details(self, *args) -> dict:
        details = super().give_details(*args)
        details["customer_status"] = "VIP"
        return details
