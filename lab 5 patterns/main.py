# main.py
from credit_card import CreditCard
from bank_info import BankInfo
from bank_customer import PersonalInfo, BankCustomer
from decorators import GoldenCreditCard, CorporateCreditCard, VIPCustomer

# Створення об'єктів
personal_info = PersonalInfo(name="Іван Іванов", address="вул. Центральна, 10", phone_number="099-123-4567")
credit_card = CreditCard(client="Іван Іванов", account_number="1234-5678-9876", credit_limit=5000.00, grace_period=30, cvv="123")
credit_card.cvv = "123"  # Встановлюємо CVV (воно буде зашифровано)

bank_info = BankInfo(bank_name="Глобальний банк", holder_name="Іван Іванов", account_number=credit_card.account_number)

bank_customer = BankCustomer(personal_info=personal_info, bank_info=bank_info)

# Декорування кредитної картки
golden_credit_card = GoldenCreditCard(credit_card)
corporate_credit_card = CorporateCreditCard(credit_card)

# Декорування клієнта
vip_customer = VIPCustomer(bank_customer)

# Тестуємо декоровані об'єкти
print(golden_credit_card.give_details())
print(corporate_credit_card.give_details())
print(vip_customer.give_details())
