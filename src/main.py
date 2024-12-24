from src.masks.mask_account import get_mask_account
from src.masks.mask_card_number import get_mask_card_number

user_card_number = int(input("Введите номер карты: "))
user_account = int(input("Введите номер счёта: "))

card_number = user_card_number
account_number = user_account

print(get_mask_card_number(card_number))
print(get_mask_account(account_number))
