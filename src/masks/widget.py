import datetime

from src.masks.mask_account import get_mask_account
from src.masks.mask_card_number import get_mask_card_number


def mask_account_card(type_and_number: str) -> str:
    """
    Функция принимает на вход тип и номер карты или счета строку с замаскированным номером.

    Пример ввода:
    Visa Platinum 7000792289606361

    Пример вывода:
    Visa Platinum 7000 79** **** 6361
    """

    type_result = ""
    number_result = ""
    number_counter = 0

    for i in type_and_number:
        if i.isalpha():
            type_result += i
        elif i == " ":
            type_result += i
        elif i.isdigit():
            number_result += i
            number_counter += 1

    if number_counter == 16:

        return f"{type_result} {get_mask_card_number(number_result)}"

    else:

        return f"{type_result} {get_mask_account(number_result)}"


def get_date(user_date: str) -> str:
    """
    Функция принимает на вход строку с датой в одном формате, а возвращает в другом

    Пример ввода:
    2024-03-11T02:26:18.671407

    Пример вывода:
    ДД.ММ.ГГГГ
    """

    date_format = datetime.datetime.strptime(user_date, "%Y-%m-%dT%H:%M:%S.%f")

    new_date = date_format.strftime("%d.%m.%Y")

    return new_date
